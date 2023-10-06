import os
import logging
from github import Github


GITHUB_API_KEY=os.environ.get('GITHUB_API_KEY')
# Disable logging from the 'github' library (optional, if desired)
logging.getLogger('github').setLevel(logging.WARNING)

g = Github(GITHUB_API_KEY)

def get_repo_name_and_desc(owner,repo_name):
    # Replace OWNER and REPO with the repository's owner and name
    repo = g.get_repo("guyg99/kram")
    return repo.name, repo.description

