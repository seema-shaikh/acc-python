def validate_payload(req):

    # 1. Key “value” not present in Json body parameter
    # 2. Type of “value” is not integer in Json body parameter

    if "value" not in req.keys():
        return {"status": "400", "msg": "Bad request", "description": "Key 'value' not present in Json body parameter"}
    elif not isinstance(req["value"], int):
        return {"status": "400", "msg": "Bad request", "description": "Type of 'value' is not integer in Json body paramete"}
    else:
        return True 