from llm.prompt_to_json import generate_pipeline_json
from compiler.pipeline_builder import (
    build_execution_plan,
    build_pipeline_project
)

json_cfg = generate_pipeline_json(
    "i want an ai to segment dog in an image"
)

print("JSON CONFIG:")
print(json_cfg)

plan = build_execution_plan(json_cfg)

print("\nEXECUTION PLAN:")
print(plan)

project_path = build_pipeline_project(plan)

print("\nPROJECT GENERATED AT:")
print(project_path)
