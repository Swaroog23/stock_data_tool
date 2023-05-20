def validate_api_result(data):
    if "Error Message" in data:
        return -1
    return 0
