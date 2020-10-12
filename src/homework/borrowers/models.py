import json
from typing import Dict

from .utils import get_current_utc


class Borrower:

    def __init__(self, email: str, age: int, income: float):
        self.created_at = get_current_utc()
        self.updated_at = self.created_at
        self.email = email
        self.age = age
        self.income = income

    def to_json(self) -> Dict:
        diccio = {"created_at": self.created_at,
                  "updated_at": self.updated_at,
                  "email": self.email,
                  "age": self.age,
                  "income": self.income}
        # TODO: return a json with the: email, age, income, created_at, and updated_at
        return diccio

    def save(self, file: str):
        with open('./borrowers/candidates.json', 'r') as f:
            data = json.loads(f.read())

        data["candidates"].append(self.to_json())
        data["updated_at"] = get_current_utc()
        with open('./borrowers/candidates.json', 'w') as f:
            json.dump(data, f, indent=4)

        # TODO: save the borrower into the json file!

    def update(self, file: str):
        # TODO: update the borrower on the json file that match the email of the current borrower.
        with open('./borrowers/candidates.json', 'r') as f:
            data = json.loads(f.read())
            can = data["candidates"]
            for child in can:
                if child["email"] == self.email:
                    child["updated_at"] = get_current_utc()
                    child["email"] = self.email
                    child["age"] = self.age
                    child["income"] = self.income
                    data["updated_at"] = get_current_utc()
                    with open('./borrowers/candidates.json', 'w') as f:
                        # string=json.dumps(data,indent=4)
                        # json.dump(string,f)
                        json.dump(data, f, indent=4)

                else:
                    pass
