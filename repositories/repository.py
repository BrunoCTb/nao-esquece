class BillRepository:
    def __init__(self, database):
        self.database = database

    def save_group(self, group):
        print('salvando grupo no repository')