from jsonschema import validate
from jsonschema.exceptions import ValidationError
from llm.json_schema import PIPELINE_JSON_SCHEMA


class InvalidPipelineJSON(Exception):
    pass


def validate_pipeline_json(data: dict):
    try:
        validate(instance=data, schema=PIPELINE_JSON_SCHEMA)
    except ValidationError as e:
        raise InvalidPipelineJSON(str(e))
