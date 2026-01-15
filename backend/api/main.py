from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import router
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Vision Pipeline Compiler API",
    version="0.1.0",
    description="Prompt → Runnable AI Vision Pipelines"
)

app.mount(
    "/downloads",
    StaticFiles(directory="downloads"),
    name="downloads"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}
