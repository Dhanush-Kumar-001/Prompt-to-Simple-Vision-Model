def resolve_output(output: dict) -> str:
    """
    Determines output behavior
    """
    output_type = output.get("type", "detect")

    if output_type not in ["detect", "count", "count_per_class"]:
        raise ValueError(f"Unsupported output type: {output_type}")

    return output_type
