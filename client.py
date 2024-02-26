from bank import bankIAV


class Client:
    def __init__(self, name, username, password, accounts=None):
        self.name = name
        self.username = username
        self.password = password
        self.accounts = accounts

    def register_client(self):
        for client in bankIAV.clients:
            if self.username == client.username:
                return False
            bankIAV.clients.append(client)
        return True
