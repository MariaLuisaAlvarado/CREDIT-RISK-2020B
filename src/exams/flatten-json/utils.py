import json


def flatten_dict(file):
    with open(file, "r") as f:
        file = json.loads(f.read())
    res = {}

    def flatten(key, value=""):
        if isinstance(key, list):
            for i in range(len(key)):
                flatten(key[i], value + '.' + str(i) if value else str(i))
        elif isinstance(key, dict):
            for k2, v in key.items():
                flatten(v, value + '.' + k2 if value else k2)
        else:
            res[value] = key

    flatten(file)
    return json.dumps(res, indent=4)
