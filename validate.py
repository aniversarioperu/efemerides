import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError


def validate_data():
    with open('schema.json') as f:
        sc = json.load(f)
    
    with open('data.json') as f:
        op = json.load(f)
    
    try:
        validate(op, sc)
    except ValidationError as e:
        return "Not valid: {}".format(e)
    else:
        return "Valid"


if __name__ == "__main__":
    print(validate_data())
