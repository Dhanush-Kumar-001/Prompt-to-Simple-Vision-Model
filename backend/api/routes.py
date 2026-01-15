import uuid
from fastapi import APIRouter
from api.schemas import BuildPipelineRequest, BuildPipelineResponse
from api.errors import InvalidPromptError, PipelineBuildError

from llm.prompt_to_json import generate_pipeline_json
from compiler.pipeline_builder import build_execution_plan, build_pipeline_project
from packaging.zip_builder import create_zip

router = APIRouter(prefix="/api", tags=["Pipeline Builder"])


@router.post("/build", response_model=BuildPipelineResponse)
def build_pipeline_endpoint(request: BuildPipelineRequest):

    if not request.prompt.strip():
        raise InvalidPromptError()

    pipeline_id = str(uuid.uuid4())

    try:
        # Prompt → JSON
        pipeline_json = generate_pipeline_json(request.prompt)

        # JSON → execution plan
        execution_plan = build_execution_plan(pipeline_json)

        # Execution plan → project
        project_dir = build_pipeline_project(execution_plan)

        # Project → ZIP
        zip_filename = create_zip(project_dir)

    except Exception as e:
        raise PipelineBuildError(detail=str(e))

    artifact_url = f"/downloads/{zip_filename}"

    return BuildPipelineResponse(
        pipeline_id=pipeline_id,
        artifact_url=artifact_url
    )
