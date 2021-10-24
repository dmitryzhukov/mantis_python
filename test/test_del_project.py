import random
import time

from fixture.application import Application
from fixture.string_generator import random_string
from model.project import Project


def test_delete_project(app: Application):
    old_projects = app.project.get_project_list()

    if (len(old_projects) == 0):
        project = Project(name=random_string("project_name", 10),
                          description=random_string("description", 10))
        app.project.add_project(project)
        old_projects = app.project.get_project_list()

    index = random.randrange(len(old_projects))

    app.project.del_project_by_index(index)
    old_projects[index:index + 1] = []

    time.sleep(1)
    new_projects = app.project.get_project_list()

    assert sorted(old_projects, key=Project.sort_by_name) == sorted(
        new_projects, key=Project.sort_by_name)
