import gradio as gr
import requests
import tempfile
import os

API_URL = "http://127.0.0.1:8000/api/build"
BASE_URL = "http://127.0.0.1:8000"


def build_pipeline(prompt: str):
    if not prompt.strip():
        return "❌ Please enter a prompt", None

    try:
        # 1️⃣ Call backend
        response = requests.post(
            API_URL,
            json={"prompt": prompt},
            timeout=120
        )

        if response.status_code != 200:
            return f"❌ Error: {response.text}", None

        data = response.json()
        zip_url = BASE_URL + data["artifact_url"]

        # 2️⃣ Download ZIP
        zip_response = requests.get(zip_url)
        zip_response.raise_for_status()

        # 3️⃣ Save ZIP to temp file
        tmp_dir = tempfile.mkdtemp()
        zip_path = os.path.join(tmp_dir, "vision_pipeline.zip")

        with open(zip_path, "wb") as f:
            f.write(zip_response.content)

        return "✅ Pipeline built successfully!", zip_path

    except Exception as e:
        return f"❌ Failed: {str(e)}", None


with gr.Blocks(title="Vision Pipeline Compiler") as demo:
    gr.Markdown(
        """
        # 🚀 Vision Pipeline Compiler
        Turn a **text prompt** into a **runnable AI vision model**.

        ### Example prompts
        - Detect only persons and count them
        - Detect cars and buses in an image
        """
    )

    prompt_input = gr.Textbox(
        label="Describe the AI model you want",
        placeholder="Detect only persons and count them",
        lines=2
    )

    build_btn = gr.Button("Build AI Pipeline")

    status_output = gr.Textbox(label="Status")

    zip_output = gr.File(
        label="Download ZIP",
        file_types=[".zip"]
    )

    build_btn.click(
        fn=build_pipeline,
        inputs=prompt_input,
        outputs=[status_output, zip_output]
    )

demo.launch(share=True)

