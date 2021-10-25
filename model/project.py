

class Project(object):
    def __init__(self, name, status=None, viewstate=None, description=None, id=None):
        self.name = name
        self.status = status
        self.viewstate = viewstate
        self.description = description
        self.id = id

    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self.description == other.description

    def __repr__(self):
        return "%s:%s;%s;%s" % (self.name, self.status, self.viewstate, self.description)

    def sort_by_name(project):
        return project.name
