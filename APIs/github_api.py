import os
import logging
from github import Github


GITHUB_API_KEY=os.environ.get('GITHUB_API_KEY')
# Disable logging from the 'github' library (optional, if desired)
logging.getLogger('github').setLevel(logging.WARNING)

g = Github(GITHUB_API_KEY)

def get_repo_from_url(repo_url):
    owner, name = repo_url.split('/')[-2:]
    repo = g.get_repo(f"{owner}/{name}")
    return repo

