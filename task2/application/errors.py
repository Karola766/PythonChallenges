class NoItemFoundError(Exception):

    def __init__(self, task_id):
        self.id = task_id

    def __str__(self):
        return f"No item of id {self.id} found. Unable to proceed with command."
