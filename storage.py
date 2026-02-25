import json
import os

FILE_NAME = "plans.json"


def save_plan(plan_dict):

    data = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            data = json.load(file)

    data.append(plan_dict)

    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def load_plans():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)