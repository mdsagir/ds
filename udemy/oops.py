from typing import List


class Employee:
    def __init__(self, name: str, clients: List[str]):
        self.name = name
        self.clients = clients

    def __str__(self):
        return f" __str__employee names is {self.name} and having no of clients : {self.clients}"

    def __(self):
        return f" __repr__employee names is {self.name} and having no of clients : {self.clients}"


client: List[str] = ["ILA Bank", "AMEX", "Axis"]
emp_name = 'sagir'

e1 = Employee(emp_name, client)
print(e1)
