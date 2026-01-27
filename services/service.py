class BillService:
    def __init__(self, repository):
        self.repository = repository

    def save_group(self):
        self.repository.save_group("group entity")

    


