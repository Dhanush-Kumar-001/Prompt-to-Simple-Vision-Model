import shutil
import os
import uuid

DOWNLOAD_DIR = "downloads"


def create_zip(project_dir: str) -> str:
    """
    Creates a zip and moves it to downloads/
    """
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)

    zip_name = f"{uuid.uuid4()}.zip"
    zip_path = os.path.join(DOWNLOAD_DIR, zip_name)

    shutil.make_archive(
        base_name=zip_path.replace(".zip", ""),
        format="zip",
        root_dir=project_dir
    )

    return zip_name   # return ONLY filename
