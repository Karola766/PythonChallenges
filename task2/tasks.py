import click
from task2.application.tasksmodel import TasksModel
from task2.application.tasksview import TasksView
from task2.application.controltasks import ControlTasks


def init():
    model = TasksModel()
    view = TasksView()
    return ControlTasks(model, view)


@click.group()
def cli():
    pass


@cli.command()
@click.option('--name', required=True, help='Task name')
@click.option('--deadline', help='Task deadline')
@click.option('--description', help='Task description')
def insert(name, deadline, description):
    init().insert(name, deadline, description)


@cli.command()
@click.option('--all', 'range', flag_value=True, help='Display all tasks.',
              default=True)
@click.option('--today', 'range', flag_value=False, help='Display tasks for today.')
def list(range):
    init().list(range)


@cli.command()
@click.argument('task_hash', type=click.UUID)
def remove(task_hash):
    init().remove(str(task_hash))


@cli.command()
@click.argument('task_hash', type=click.UUID)
@click.option('--name', help='Task name')
@click.option('--deadline', help='Task deadline')
@click.option('--description', help='Task description')
def update(task_hash, name, deadline, description):
    """Simple method for updating tasks."""
    init().update(str(task_hash), name, deadline, description)


if __name__ == '__main__':
    cli()
