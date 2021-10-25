from model.project import Project
from suds.client import Client
from suds.wsdl import Port


class SoapHelper:
    def __init__(self, app) -> None:
        self.app = app

    def get_project_list(self):
        client = Client("%s/api/soap/mantisconnect.php?wsdl" %
                        self.app.base_url)
        projects = client.service.mc_projects_get_user_accessible(
            self.app.credentials.login, self.app.credentials.password)

        return list(map(lambda x: Project(name=x.name, description=x.description, id=x.id), projects))
