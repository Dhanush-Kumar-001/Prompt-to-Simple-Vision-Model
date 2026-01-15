PIPELINE_JSON_SCHEMA = {
    "type": "object",
    "required": [
        "task",
        "target_classes",
        "input_type",
        "model",
        "inference",
        "output"
    ],
    "properties": {
        "task": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "string",
                "enum": [
                    "object_detection",
                    "segmentation",
                    "classification"
                ]
            }
        },
        "target_classes": {
            "type": "array",
            "items": {"type": "string"}
        },
        "input_type": {
            "type": "string",
            "enum": ["image"]
        },
        "model": {
            "type": "string",
            "enum": [
                "yolov8n", "yolov8s", "yolov8m", "yolov8l", "yolov8x",

                "yolov8n-seg", "yolov8s-seg", "yolov8m-seg", "yolov8l-seg", "yolov8x-seg",

                "yolov8n-cls", "yolov8s-cls", "yolov8m-cls", "yolov8l-cls", "yolov8x-cls",

                "yolov8n-pose", "yolov8s-pose", "yolov8m-pose", "yolov8l-pose", "yolov8x-pose"
            ]
        },
        "inference": {
            "type": "object"
        },
        "output": {
            "type": "object",
            "required": ["type"],
            "properties": {
                "type": {
                    "type": "string",
                    "enum": ["count", "detect", "count_per_class", "masks", "skeleton"]
                }
            }
        }
    },
    "additionalProperties": False
}
