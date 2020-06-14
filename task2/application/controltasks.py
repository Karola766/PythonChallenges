import datetime
import uuid


class ControlTasks:
    """Class controlling the task system. Calls model and view"""

    def __init__(self, task_model, task_view):
        self.view = task_view
        self.model = task_model
        connection = self.model.connect()
        self.model.create_table(connection)

    @staticmethod
    def hash(arg):
        """Because of click limitations, hashed identifiers will be stored in uuid form"""
        arg = str(hash(arg))
        return uuid.uuid5(uuid.NAMESPACE_X500, arg)

    def insert(self, name, deadline, description):
        task_id = str(ControlTasks.hash(name))
        connection = self.model.connect()
        self.model.insert_task(connection, task_id, name, deadline, description)
        self.view.task_added(task_id, name, deadline, description)

    def list(self, day_range):
        connection = self.model.connect()
        if not day_range:
            date = datetime.date.today()
            results = self.model.select_tasks(connection, date=date)
            self.view.task_list_day(results)
        else:
            results = self.model.select_tasks(connection)
            self.view.task_list_all(results)

    def remove(self, task_hash):
        connection = self.model.connect()
        self.model.remove_task(connection, task_hash)
        self.view.task_removed()

    def update(self, task_hash, name, deadline, description):
        connection = self.model.connect()
        self.model.update_task(connection, task_hash, name, deadline, description)
        self.view.task_updated(task_hash, name, deadline, description)
