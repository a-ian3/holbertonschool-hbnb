from app.persistence.repository import InMemoryRepository

class HBnBFacade:
    def __init__(self):
        self.repo = InMemoryRepository()

    def create_user(self, data):
        return self.repo.create(data)

    def get_user(self, user_id):
        return self.repo.get(user_id)

    def get_all_users(self):
        return self.repo.all()

    def update_user(self, user_id, data):
        return self.repo.update(user_id, data)

