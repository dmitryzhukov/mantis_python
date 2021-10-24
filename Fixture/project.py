from typing import List
from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_css_selector(
                "#sidebar ul > li:last-child").click()
            wd.find_element_by_css_selector(
                ".nav-tabs li:nth-child(3)").click()

    def get_project_list(self) -> List[Project]:
        wd = self.app.wd
        self.open_manage_project_page()
        projects: List[Project] = []
        rows = list(wd.find_elements_by_css_selector(
            ".widget-box:nth-of-type(2) tbody tr"))
        for row in rows:
            cells = row.find_elements_by_tag_name("td")
            name = cells[0].text
            status = cells[1].text
            viewstate = cells[3].text
            description = cells[4].text
            projects.append(Project(name=name, status=status,
                            viewstate=viewstate, description=description))

        return projects

    def open_add_page(self):
        wd = self.app.wd
        create_button = wd.find_element_by_css_selector(
            "form[action='manage_proj_create_page.php'] > button[type='submit']")
        create_button.click()

    def fill_add_project_form(self, project: Project):
        self.app.change_field_value("name", project.name)
        self.app.change_field_value("status", project.status)
        self.app.change_field_value("view_state", project.viewstate)
        self.app.change_field_value("description", project.description)

    def add_project(self, project: Project):
        wd = self.app.wd
        self.open_manage_project_page()
        self.open_add_page()
        self.fill_add_project_form(project)
        wd.find_element_by_css_selector(
            "#manage-project-create-form input[type='submit']").click()

    def del_project_by_index(self, index):
        wd = self.app.wd
        self.open_manage_project_page()
        row = wd.find_elements_by_css_selector(
            ".widget-box:nth-of-type(2) tbody tr")[index]
        row.find_elements_by_css_selector("td a")[0].click()
        wd.find_element_by_css_selector(
            "#project-delete-form input[type='submit']").click()
        wd.find_element_by_css_selector(
            "form input[type='submit']").click()
