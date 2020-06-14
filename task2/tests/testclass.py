import unittest
import datetime

from task2.application.controltasks import ControlTasks
from task2.application.tasksmodel import TasksModel
from task2.application.tasksview import TasksView


class MyTestCase(unittest.TestCase):

    @staticmethod
    def prepare_environment(table_name):
        model = TasksModel()
        model.db_name = "test_db"
        model.tasks_table = table_name
        view = TasksView()
        return ControlTasks(model, view)

    def test_insert(self):
        central = self.prepare_environment("insert_test_table")
        connection = central.model.connect()
        list1 = central.model.select_tasks(connection)
        central.insert("Cleaning", None, "Now")
        list2 = central.model.select_tasks(connection)
        self.assertEqual(len(list1) + 1, len(list2))

    def test_remove(self):
        central = self.prepare_environment("remove_test_table")
        connection = central.model.connect()
        test_list = central.model.select_tasks(connection)
        if not test_list:
            central.insert("Test", None, "Test_Remove")
            test_list = central.model.select_tasks(connection)
        test_id = test_list[0][0]
        central.remove(test_id)
        test_list = central.model.select_tasks(connection)
        self.assertEqual(any(ele[0] == test_id for ele in test_list), False)

    def test_update(self):
        central = self.prepare_environment("update_test_table")
        connection = central.model.connect()
        test_list = central.model.select_tasks(connection)
        if not test_list:
            central.insert("Test", None, "Test_Update")
            test_list = central.model.select_tasks(connection)
        test_id = test_list[0][0]
        central.update(test_id, None, None, description="Update test")
        test_list = central.model.select_tasks(connection)
        self.assertEqual(any(ele[0] == test_id and ele[3] == "Update test" for ele in
                             test_list), True)

    def test_list(self):
        test_date = "12.06.2020"
        central = self.prepare_environment("list_test_table")
        connection = central.model.connect()
        central.insert("List_Test", test_date, "Testing")
        test_all = central.model.select_tasks(connection)
        self.assertEqual(any(ele[2] == test_date for ele in test_all), True)
        date = datetime.date.today()
        test_today = central.model.select_tasks(connection, date=date)
        self.assertEqual(any(ele[2] == test_date for ele in test_today), False)


if __name__ == '__main__':
    case = MyTestCase()
    case.test_insert()
    case.test_remove()
    case.test_update()
    case.test_list()
