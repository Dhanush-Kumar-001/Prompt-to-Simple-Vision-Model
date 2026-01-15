from compiler.task_router import route_task
from compiler.class_mapper import map_classes
from compiler.model_resolver import resolve_model
from compiler.output_resolver import resolve_output
from compiler.code_generator import generate_code

import tempfile
import shutil
import os


def enforce_output_defaults(output: dict) -> dict:
    """
    Ensures output.type always exists
    """
    if not output or "type" not in output:
        return {"type": "detect"}
    return output


def build_execution_plan(pipeline_json: dict) -> dict:
    # 🔹 MULTI-TASK SUPPORT
    tasks = pipeline_json["task"]  # now a list
    task_modes = [route_task(task) for task in tasks]

    # 🔹 OUTPUT DEFAULTS
    output = enforce_output_defaults(pipeline_json.get("output", {}))

    return {
        "task_modes": task_modes,                # 👈 LIST, not single
        "model_weights": resolve_model(pipeline_json["model"]),
        "class_ids": map_classes(pipeline_json["target_classes"]),
        "output_mode": resolve_output(output),
        "inference": pipeline_json["inference"]
    }


def build_pipeline_project(execution_plan: dict) -> str:
    project_dir = tempfile.mkdtemp(prefix="vision_pipeline_")

    # 1️⃣ Generate run.py
    generate_code(
        execution_plan=execution_plan,
        output_dir=project_dir
    )

    # 2️⃣ Copy runtime files
    runtime_dir = "runtime"

    shutil.copy(
        os.path.join(runtime_dir, "requirements.txt"),
        project_dir
    )

    shutil.copy(
        os.path.join(runtime_dir, "README.md"),
        project_dir
    )

    return project_dir
