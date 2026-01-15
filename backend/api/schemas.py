from pydantic import BaseModel, Field
from typing import Optional


class BuildPipelineRequest(BaseModel):
    prompt: str = Field(
        ...,
        min_length=5,
        description="Natural language prompt describing the AI vision task"
    )


class BuildPipelineResponse(BaseModel):
    pipeline_id: str
    artifact_url: str
    status: str = "success"


class ErrorResponse(BaseModel):
    error: str
    detail: Optional[str] = None
