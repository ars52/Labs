class UserAccount:

    def __init__(self, username: str, email: str, password: str):
        self.username = username
        self.email = email
        self.password = hash(password)

    def set_password(self, new_password: str) -> None:
        self.password = hash(new_password)

    def check_password(self, password: str) -> bool:
        return self.password == hash(password)


my_account = UserAccount('Arseniy', 'kazzz-2006@mail.ru', '290406')
print(my_account.set_password('23'))
print(my_account.check_password('23'))
