class TasksView:

    @staticmethod
    def display_task(task_id, name, deadline, description):
        print('ID:{} NAME:{} DEADLINE:{} DESCRIPTION:{}'.format(task_id, name,
                                                                deadline, description))

    @staticmethod
    def display_empty():
        print("----------------------------------------------")
        print("--------NO-RESULTING-RECORDS-FOUND------------")
        print("----------------------------------------------")

    @staticmethod
    def list_tasks(tasks):
        if tasks:
            for t in tasks:
                TasksView.display_task(*t)
        else:
            TasksView.display_empty()

    @staticmethod
    def task_added(task_id, name, deadline, description):
        print("----------------------------------------------")
        print("----------------TASK-ADDED--------------------")
        print("----------------------------------------------")
        TasksView.display_task(task_id, name, deadline, description)
        print("----------------------------------------------")
        print("----------------------------------------------")

    @staticmethod
    def task_updated(task_id, name, deadline, description):
        print("----------------------------------------------")
        print("---------------TASK-UPDATED-------------------")
        print("----------------------------------------------")
        TasksView.display_task(task_id, name, deadline, description)
        print("----------------------------------------------")
        print("----------------------------------------------")

    @staticmethod
    def task_removed():
        print("----------------------------------------------")
        print("---------------TASK-REMOVED-------------------")
        print("----------------------------------------------")

    @staticmethod
    def task_list_all(tasks):
        print("----------------------------------------------")
        print("-----------------ALL_TASKS--------------------")
        print("----------------------------------------------")
        TasksView.list_tasks(tasks)
        print("----------------------------------------------")
        print("----------------------------------------------")

    @staticmethod
    def task_list_day(tasks):
        print("----------------------------------------------")
        print("--------------TASKS-FOR-TODAY-----------------")
        print("----------------------------------------------")
        TasksView.list_tasks(tasks)
        print("----------------------------------------------")
        print("----------------------------------------------")
