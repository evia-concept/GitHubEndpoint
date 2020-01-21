import unittest
import uuid
from collaborators.api.github_request import (
    list_organization_repositories,
    list_repository_contributors,
)
from collaborators.messages.error_messages import (
    null_argument_exception,
    not_allowed_argument_exception,
)

assertion_error_expected = "Error expected"
valid_organization_name = "microsoft"
valid_repository_name = "vscode"


class GithubRequest(unittest.TestCase):
    
    def _argument_null_or_empty_throw_exception(self, test_func, *args):

        try:
            test_func(*args)
            raise AssertionError(assertion_error_expected)

        except ValueError as msg:
            assert str(msg) == null_argument_exception

    def _argument_slash_or_backslash_return_404(self, test_func, *args):

        try:
            test_func(*args)
            raise AssertionError(assertion_error_expected)

        except ValueError as msg:
            assert str(msg) == not_allowed_argument_exception

    def _argument_not_exist_return_404(self, test_func, *args):

        assert test_func(*args).status_code == 404

    def _argument_valid_return_200(self, test_func, *args):

        assert test_func(*args).status_code == 200

    def test_list_organization_repositories_null_throw_exception(self):

        self._argument_null_or_empty_throw_exception(
            list_organization_repositories, None
        )

    def test_list_organization_repositories_empty_string_throw_exception(self):

        self._argument_null_or_empty_throw_exception(list_organization_repositories, "")

    def test_list_organization_repositories_backslash_throw_exception(self):

        self._argument_slash_or_backslash_return_404(
            list_organization_repositories, "..\\\\"
        )

    def test_list_organization_repositories_slash_throw_exception(self):

        self._argument_slash_or_backslash_return_404(
            list_organization_repositories, f"{valid_organization_name}/"
        )

    def test_list_organization_repositories_not_exist_return_404(self):

        self._argument_not_exist_return_404(
            list_organization_repositories, str(uuid.uuid4())
        )

    def test_list_organization_repositories_valid_return_200(self):

        self._argument_valid_return_200(
            list_organization_repositories, valid_organization_name
        )

    def test_list_repository_contributors_null_org_name_throw_exception(self):

        self._argument_null_or_empty_throw_exception(
            list_repository_contributors, None, valid_repository_name
        )

    def test_list_repository_contributors_null_repo_name_throw_exception(self):

        self._argument_null_or_empty_throw_exception(
            list_repository_contributors, valid_organization_name, None
        )

    def test_list_repository_contributors_empty_string_org_name_throw_exception(self):

        self._argument_null_or_empty_throw_exception(
            list_repository_contributors, "", valid_repository_name
        )

    def test_list_repository_contributors_empty_string_repo_name_throw_exception(self):

        self._argument_null_or_empty_throw_exception(
            list_repository_contributors, valid_organization_name, ""
        )

    def test_list_repository_contributors_backslash_org_name_throw_exception(self):

        self._argument_slash_or_backslash_return_404(
            list_repository_contributors, "..\\\\", valid_repository_name
        )

    def test_list_repository_contributors_backslash_repo_name_throw_exception(self):

        self._argument_slash_or_backslash_return_404(
            list_repository_contributors, valid_organization_name, "..\\\\"
        )

    def test_list_repository_contributors_slash_org_name_throw_exception(self):

        self._argument_slash_or_backslash_return_404(
            list_repository_contributors,
            valid_organization_name,
            f"{valid_repository_name}/",
        )

    def test_list_repository_contributors_slash_repo_name_throw_exception(self):

        self._argument_slash_or_backslash_return_404(
            list_repository_contributors,
            f"{valid_organization_name}/",
            valid_repository_name,
        )

    def test_list_repository_contributors_not_exist_org_name_return_404(self):

        self._argument_not_exist_return_404(
            list_repository_contributors, valid_organization_name, str(uuid.uuid4())
        )

    def test_list_repository_contributors_not_exist_repo_name_return_404(self):

        self._argument_not_exist_return_404(
            list_repository_contributors, str(uuid.uuid4()), valid_repository_name
        )

    def test_list_repository_contributors_valid_return_200(self):

        self._argument_valid_return_200(
            list_repository_contributors, valid_organization_name, valid_repository_name
        )
