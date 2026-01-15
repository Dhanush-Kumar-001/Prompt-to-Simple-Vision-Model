# 🚀 Vision Pipeline Compiler

Turn a **natural language prompt** into a **runnable AI vision pipeline**.

This project converts user prompts like:

- "Detect persons and count them"
- "Segment people in an image"
- "Classify this image"
- "Pose estimation of humans"

into a **ready-to-run Python project** using **YOLOv8 pre-trained models**.

---

## 🧠 How It Works (High Level)

User Prompt
↓
LLM → Structured JSON
↓
Schema Validation
↓
Execution Plan (Compiler)
↓
Template-Based Code Generation
↓
Runnable AI Vision Project (ZIP)


---

## 🧩 Architecture Overview

### 1️⃣ Base Template
- Loads model
- Loads input image
- Runs inference **once**
- Provides hooks for extensions

### 2️⃣ Task Templates (Capabilities)
- Detection
- Segmentation
- Classification
- Pose Estimation

These **only interpret model results**, they never run inference again.

### 3️⃣ Output Templates
- Bounding boxes
- Masks
- Count
- Count per class
- Classification output

These **consume prepared variables** and produce outputs.

---

## 📁 Project Structure

backend/
├── llm/
│ ├── prompt_to_json.py
│ ├── validator.py
│
├── compiler/
│ ├── pipeline_builder.py
│ ├── code_generator.py
│ ├── task_router.py
│ ├── output_resolver.py
│ ├── model_resolver.py
│
├── templates/
│ ├── base.py.jinja
│ ├── tasks/
│ │ ├── detect.py.jinja
│ │ ├── segment.py.jinja
│ │ ├── classify.py.jinja
│ │ └── pose.py.jinja
│ ├── outputs/
│ │ ├── detect.py.jinja
│ │ ├── count.py.jinja
│ │ ├── masks.py.jinja
│ │ └── classify.py.jinja
│
├── runtime/
│ ├── requirements.txt
│ └── README.md
│
└── api/
└── main.py


---

## 🧪 Example Usage

```python
from llm.prompt_to_json import generate_pipeline_json
from compiler.pipeline_builder import build_execution_plan, build_pipeline_project

json_cfg = generate_pipeline_json(
    "Segment people in an image and save masks"
)

plan = build_execution_plan(json_cfg)
project_path = build_pipeline_project(plan)

print("Pipeline generated at:", project_path)

