class BankAccountManager:
    def __init__(self):
        self.clients_base = {}

    def create_or_check_client(self, client):
        if client not in self.clients_base:
            self.clients_base[client] = 0

    def get_client_balance(self, client):
        if client in self.clients_base:
            return self.clients_base[client]
        else:
            return "ERROR"

    def get_operations(self, file_name):
        lines = []
        with open(file_name) as f:
            lines = f.readlines()
        self.lines = lines

    def manage_operations(self):
        for line in self.lines:
            operation, *params = line.split()

            if operation == "BALANCE":
                [client] = params

                print(self.get_client_balance(client))

            elif operation == "DEPOSIT" or operation == "WITHDRAW":
                client, amount = params

                self.create_or_check_client(client)

                amount = int(amount) if operation == "DEPOSIT" else -int(amount)
                self.clients_base[client] += amount

            elif operation == "TRANSFER":
                client_from, client_to, amount = params

                self.create_or_check_client(client_from)
                self.create_or_check_client(client_to)

                self.clients_base[client_from] -= int(amount)
                self.clients_base[client_to] += int(amount)

            elif operation == "INCOME":
                [percent] = params
                for client in self.clients_base:
                    current_amount = self.clients_base[client]
                    if current_amount > 0:
                        self.clients_base[client] += int(
                            (int(percent) / 100) * current_amount
                        )


bank1 = BankAccountManager()
bank1.get_operations("input.txt")
bank1.manage_operations()
