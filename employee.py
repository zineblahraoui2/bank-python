from bank import bankIAV


class Employee:
    def __init__(self, username, password, bank=None):
        self.username = username
        self.password = password
        self.bank = bank

    def authenticate(self):
        for employee in bankIAV.employees:
            if self.username == employee.username and self.password == employee.password:
                return Employee
        return None
