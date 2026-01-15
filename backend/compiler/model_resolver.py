YOLO_MODELS = {

    # ======================
    # OBJECT DETECTION
    # ======================
    "yolov8n": "yolov8n.pt",
    "yolov8s": "yolov8s.pt",
    "yolov8m": "yolov8m.pt",
    "yolov8l": "yolov8l.pt",
    "yolov8x": "yolov8x.pt",

    # ======================
    # INSTANCE SEGMENTATION
    # ======================
    "yolov8n-seg": "yolov8n-seg.pt",
    "yolov8s-seg": "yolov8s-seg.pt",
    "yolov8m-seg": "yolov8m-seg.pt",
    "yolov8l-seg": "yolov8l-seg.pt",
    "yolov8x-seg": "yolov8x-seg.pt",

    # ======================
    # IMAGE CLASSIFICATION
    # ======================
    "yolov8n-cls": "yolov8n-cls.pt",
    "yolov8s-cls": "yolov8s-cls.pt",
    "yolov8m-cls": "yolov8m-cls.pt",
    "yolov8l-cls": "yolov8l-cls.pt",
    "yolov8x-cls": "yolov8x-cls.pt",

    # ======================
    # POSE ESTIMATION
    # ======================
    "yolov8n-pose": "yolov8n-pose.pt",
    "yolov8s-pose": "yolov8s-pose.pt",
    "yolov8m-pose": "yolov8m-pose.pt",
    "yolov8l-pose": "yolov8l-pose.pt",
    "yolov8x-pose": "yolov8x-pose.pt",
}


def resolve_model(model_name: str) -> str:
    """
    Maps model name to YOLO weight file
    """
    if model_name not in YOLO_MODELS:
        raise ValueError(f"Unsupported model: {model_name}")

    return YOLO_MODELS[model_name]
