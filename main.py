from repository import Repository
from utils import clear
# bankIVA is an object of Bank
from bank import bankIAV
from employee import Employee
from client import Client

john = Employee("e", "e")
bankIAV.employees.append(john)


def print_auth_menu():
    print('1. Employee authentication')


def print_account_details_menu(client):
    print(f'Welcome [{client.name}]')


while True:
    clear()
    print_auth_menu()
    choice = int(input("\nEnter your choice: "))

    match choice:
        # register
        case 1:
            # authenticate_employee()
            while True:
                clear()
                print('Enter employee credentials')
                username = input("Username: ")
                password = input("Password: ")
                temp = Employee(username, password)
                authenticated_employee = temp.authenticate()
                if authenticated_employee is not None:
                    break

            clear()
            print('Register client')
            name = input("Name: ")
            username = input("Username: ")
            password = input("Password: ")

            client = Client(name, username, password)
            if client.register_client():
                row = [client.name, client.username, client.password]
                Repository.add(row)
                print('Client registered successfully.')
                break

        # authenticate
        case 2:
            while True:
                clear()
                username = input("Username: ")
                password = input("Password: ")
                # client = authenticated_client(username, password, clients)
                if client is not None:
                    break

        case _:
            break
