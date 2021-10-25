import random
import time

from fixture.application import Application
from fixture.string_generator import random_string
from model.project import Project


def test_delete_project(app: Application):
    old_projects = app.soap.get_project_list()

    if (len(old_projects) == 0):
        project = Project(name=random_string("project_name", 10),
                          description=random_string("description", 10))
        app.project.add_project(project)
        old_projects = app.project.get_project_list()

    project_to_delete = random.choice(old_projects)

    app.project.del_project_by_id(project_to_delete.id)
    old_projects.remove(project_to_delete)

    time.sleep(1)
    new_projects = app.soap.get_project_list()

    assert sorted(old_projects, key=Project.sort_by_name) == sorted(
        new_projects, key=Project.sort_by_name)
