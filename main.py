class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class Admin(User):
    def __init__(self, name, id, admin_id):
        super().__init__(name, id)  # Инициализация родительского класса User
        self.users = []  # Список пользователей
        self.admin_id = admin_id  # Идентификатор администратора

    def dostup(self):
        public_access = f"{self.name} - публичный доступ"
        private_access = f"{self.admin_id} - приватный доступ"
        return public_access, private_access

    def add_user(self, name, id):
        new_user = User(name, id)
        self.users.append(new_user)  # Добавляем нового пользователя в список

    def remove_user(self, name, id):
        user_to_remove = None
        for user in self.users:
            if user.name == name and user.id == id:
                user_to_remove = user
                break
        if user_to_remove:
            self.users.remove(user_to_remove)  # Удаляем пользователя из списка

    def list_users(self):
        return [(user.name, user.id) for user in self.users]  # Возвращаем список пользователей
