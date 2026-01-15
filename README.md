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
│   ├── prompt_to_json.py
│   ├── validator.py
│
├── compiler/
│   ├── pipeline_builder.py
│   ├── code_generator.py
│   ├── task_router.py
│   ├── output_resolver.py
│   ├── model_resolver.py
│
├── templates/
│   ├── base.py.jinja
│   ├── tasks/
│   │   ├── detect.py.jinja
│   │   ├── segment.py.jinja
│   │   ├── classify.py.jinja
│   │   └── pose.py.jinja
│   ├── outputs/
│       ├── detect.py.jinja
│       ├── count.py.jinja
│       ├── masks.py.jinja
│       └── classify.py.jinja
│
├── runtime/
│   ├── requirements.txt
│   └── README.md
│
└── api/
    └── main.py
    └── routes.py
    └── errors.py
    └── schemas.py

---

## 🚀 Get Started

Follow the steps below to run the Vision Pipeline Compiler locally.

---

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/vision-pipeline-compiler.git
cd Prompt-to-Simple-Vision-Model
```
### 2️⃣ Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```
### 3️⃣ Install Dependencies

```bash
pip install -r runtime/requirements.txt
```

### 4️⃣ Move to backend folder

```bash
cd backend
```

### 5️⃣ Configure Environment Variables
Create a .env file inside the backend/ directory:
```bash
GROQ_API_KEY=your_api_key_here
```

## ▶️ Running Backend and Frontend Together

The backend and frontend run as **two separate services**.  
Open **two terminals** and start each one as shown below.

---

### 🖥️ Terminal 1 — Backend (API)

```bash
uvicorn api.main:app --reload
```

### 🖥️ Terminal 2 — Frontend

```bash
cd frontend
python app.py
```
