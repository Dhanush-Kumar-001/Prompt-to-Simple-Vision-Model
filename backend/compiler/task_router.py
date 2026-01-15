def route_task(task: str) -> str:
    """
    Maps high-level task intent to internal pipeline mode
    """
    if task == "object_detection":
        return "detect"
    if task == "segmentation":
        return "segment"
    if task == "classification":
        return "classify"
    if task == "pose_estimation":
        return "pose"
    
    raise ValueError(f"Unsupported task: {task}")
