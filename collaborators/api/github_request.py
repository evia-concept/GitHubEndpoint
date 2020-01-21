import requests


def list_organization_repositories(organization_name):

    # GET /orgs/:owner/repos -> name
    # Lists repositories for the specified organization.

    get_response = requests.get(
        f"https://api.github.com/orgs/{organization_name}/repos"
    )

    return get_response

def list_repository_contributors(organization_name, repository_name):

    # GET /repos/:owner/:repo/contributors -> login, contributions
    # Lists contributors to the specified repository and sorts them by the number of commits 
    # per contributor in descending order. This endpoint may return information that is a few 
    # hours old because the GitHub REST API v3 caches contributor data to improve performance.

    # GitHub identifies contributors by author email address. This endpoint groups contribution 
    # counts by GitHub user, which includes all associated email addresses. To improve performance, 
    # only the first 500 author email addresses in the repository link to GitHub users. The rest will 
    # appear as anonymous contributors without associated GitHub user information.

    get_response = requests.get(
        f"https://api.github.com/repos/{organization_name}/{repository_name}/contributors"
    )

    return get_response