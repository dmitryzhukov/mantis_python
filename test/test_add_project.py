import time

from fixture.application import Application
from fixture.string_generator import random_string
from model.project import Project


def test_add_project(app: Application):
    old_projects = app.soap.get_project_list()

    project = Project(name=random_string("project_name", 10),
                      description=random_string("description", 10))
    app.project.add_project(project)

    old_projects.append(project)

    time.sleep(1)
    new_projects = app.soap.get_project_list()

    assert sorted(old_projects, key=Project.sort_by_name) == sorted(
        new_projects, key=Project.sort_by_name)
