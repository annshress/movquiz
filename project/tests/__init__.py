from project.utils import delete_code_file


class BaseTestMixin:
    def tearDown(self):
        # remove the codes file created during tests
        delete_code_file()
