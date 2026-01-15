import os
from jinja2 import Environment, FileSystemLoader


TASK_TEMPLATE_MAP = {
    "base": "base.py.jinja",
    "count": "count.py.jinja",
    "detect": "detect.py.jinja",
    "segment": "segment.py.jinja",
    "classify": "classify.py.jinja",
    "pose": "pose.py.jinja"
}


def indent(code: str, spaces: int = 4) -> str:
    pad = " " * spaces
    return "\n".join(
        pad + line if line.strip() else line
        for line in code.splitlines()
    )



def generate_code(execution_plan: dict, output_dir: str):
    """
    Generates run.py using base + multiple task templates
    """

    env = Environment(
        loader=FileSystemLoader("templates"),
        autoescape=False
    )

    # 🔹 Load base template
    base_template = env.get_template("base.py.jinja")

    # 🔹 Load task templates (MULTIPLE)
    task_snippets = []
    for task_mode in execution_plan["task_modes"]:
        task_template = env.get_template(f"tasks/{task_mode}.py.jinja")
        task_snippets.append(task_template.render())

    # 🔹 Load output template(s)
    output_mode = execution_plan["output_mode"]
    output_template = env.get_template(f"outputs/{output_mode}.py.jinja")
    output_snippet = output_template.render()

    # 🔹 Render final code
    rendered_code = base_template.render(
        model_weights=execution_plan["model_weights"],
        class_ids=execution_plan["class_ids"],
        inference=execution_plan["inference"],
        task_blocks="\n".join(task_snippets),
        output_blocks=output_snippet
    )

    os.makedirs(output_dir, exist_ok=True)

    with open(os.path.join(output_dir, "run.py"), "w", encoding="utf-8") as f:
        f.write(rendered_code)
