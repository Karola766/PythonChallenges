import sqlite3

from task2.application.errors import NoItemFoundError


class TasksModel:
    db_name = 'tasks_db'
    tasks_table = 'tasks_tb'

    def connect(self):
        if self is not None:
            formatted_name = '{}.db'.format(self.db_name)
            connection = sqlite3.connect(formatted_name)
        else:
            connection = sqlite3.connect(':memory:')
        return connection

    def create_table(self, connection):
        try:
            query = "CREATE TABLE {} (id TEXT PRIMARY KEY NOT NULL UNIQUE, " \
                    "name TEXT NOT NULL, deadline DATETIME, description TEXT)".format(
                self.tasks_table)
            connection.execute(query)
        except sqlite3.OperationalError as e:
            print(e)

    def check_existence(self, connection, task_id):
        query = 'SELECT EXISTS(SELECT 1 FROM {} WHERE id=? LIMIT 1)'.format(
            self.tasks_table)
        executed = connection.execute(query, (task_id,))
        result = executed.fetchone()
        if result:
            return True
        return False

    def insert_task(self, connection, task_id, name, deadline=None,
                    description=None):
        try:
            query = "INSERT INTO {} ('id', 'name', 'deadline', 'description') VALUES (" \
                    "?, ?, ?, ?)".format(self.tasks_table)
            connection.execute(query, (task_id, name, deadline, description))
            connection.commit()
        except sqlite3.IntegrityError as e:
            print(e)

    def update_task(self, connection, task_id, new_name=None, new_deadline=None,
                    new_description=None):
        if self.check_existence(connection, task_id):
            arg_dict = {}
            if new_name:
                arg_dict['name'] = new_name
            if new_deadline:
                arg_dict['deadline'] = new_deadline
            if new_description:
                arg_dict['description'] = new_description
            if arg_dict:
                args = ()
                query = "UPDATE {} SET".format(self.tasks_table)
                for k in arg_dict.keys():
                    query += " {}=?,".format(k)
                    args += (arg_dict[k],)
                query = query[:-1]
                query += " WHERE id=?"
                args += (task_id,)
                connection.execute(query, args)
                connection.commit()
        else:
            raise NoItemFoundError(task_id)

    def remove_task(self, connection, task_id):
        if self.check_existence(connection, task_id):
            query = "DELETE FROM {} WHERE id=?".format(self.tasks_table)
            connection.execute(query, (task_id,))
            connection.commit()
        else:
            raise NoItemFoundError(task_id)

    def select_tasks(self, connection, date=None):
        query = "SELECT * FROM {}".format(self.tasks_table)
        if date:
            query += " WHERE deadline=?"
            date = f"{date:%d.%m.%Y}"
            task_list = connection.execute(query, (date, ))
        else:
            task_list = connection.execute(query)
        return task_list.fetchall()
