class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id


class Admin(User):
    def __init__(self, name, id, admin):
        super().__init__(name, id)
        self._admin = admin
        self.users = []

    def dostup(self):
        self.public = f"{self.users} - публичный доступ"
        self.__private = f"{self.admin} - приватный доступ"

    def add_user(self, name, id):
        new_user = User(name, id)
        self.users.append(new_user)

    def remove_user(self, name, id):
        for user in self.users:
            if user.name == name and user.id == id:
                self.users.remove(user)
                break

    def list_users(self):
        return [(user.name, user.id) for user in self.users]

    def get_users(self):
        return [(user.name, user.id) for user in self.users]

    def get_admin(self):
        return self._admin


admin = Admin("Алексей", 7, "Админ")
admin.add_user("Степан", 4)

admin.add_user("Сергей", 3)

admin.add_user("Николай", 2)

admin.add_user("Наталья", 1)

print("Список пользователей: ", admin.get_users())

admin.remove_user("Николай", 2)

print("Список пользователей после удаления: ", admin.get_users())

print("Администратор: ", admin.get_admin())


