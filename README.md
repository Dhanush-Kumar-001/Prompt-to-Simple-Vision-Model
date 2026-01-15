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

```bash
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

```

---
## ℹ️ Important Information

This project uses **YOLOv8 pre-trained models** provided by Ultralytics.  
No model training or fine-tuning is performed.

Based on the user’s prompt, the system:
- Selects the appropriate YOLO model and task
- Generates a complete runnable pipeline using templates
- Packages the generated pipeline into a **ZIP file**

### 📦 Generated ZIP File

The downloaded ZIP file contains:
- `run.py` – executable inference script  
- `requirements.txt` – all required dependencies  
- `README.md` – instructions to run the pipeline  

You can extract the ZIP file and run the pipeline independently on any machine.

### ▶️ Running the Generated Pipeline

All instructions are already included inside the generated ZIP.  
In general, the steps are:

```bash
pip install -r requirements.txt
python run.py image.jpg
```
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

```bash
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

backend/
├── app.py

```
---

## 😎🤯🥳Output Screenshots
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/3d25442d-439d-415b-b850-ddf7b17ecf1d" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/783eda0c-d933-4d81-988e-fd2460838a88" />
<img width="1920" height="1020" alt="image" src="https://github.com/user-attachments/assets/3149f659-e297-48b6-919d-dd7c0391dceb" />

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
Past your API key in .env file inside the backend/ directory:
```bash
GROQ_API_KEY=your_api_key_here
```

## ▶️ Running Backend and Frontend Together

The backend and frontend run as **two separate services**.  
Open **two terminals** and start each one as shown below.


### 🖥️ Terminal 1 — Backend (API)

```bash
uvicorn api.main:app --reload
```

Example

```bash
(venv) PS C:\Users\dhanu\Downloads\Prompt-to-Simple-Vision-Model\backend> uvicorn api.main:app --reload
INFO:     Will watch for changes in these directories: ['C:\\Users\\dhanu\\Downloads\\Prompt-to-Simple-Vision-Model\\backend']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28300] using StatReload
INFO:     Started server process [20088]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

### 🖥️ Terminal 2 — Frontend

```bash
python -m venv venv
cd frontend
python app.py
```
Example

```bash
PS C:\Users\dhanu\Downloads\Prompt-to-Simple-Vision-Model> venv\Scripts\activate
(venv) PS C:\Users\dhanu\Downloads\Prompt-to-Simple-Vision-Model> cd frontend
>> python app.py
* Running on local URL:  http://127.0.0.1:7860
* Running on public URL: https://8aea232bd1ea5a1e43.gradio.live

This share link expires in 1 week. For free permanent hosting and GPU upgrades, run `gradio deploy` from the terminal in the working directory to deploy to Hugging Face Spaces (https://huggingface.co/spaces)
```
Click the IP address generated to run the model locally in your browser or the link to use in some other devices.
