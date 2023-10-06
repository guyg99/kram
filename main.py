from fastapi import FastAPI
from pydantic import BaseModel
from APIs.github_api import get_repo_from_url

app = FastAPI()

class UrlModel(BaseModel):
    repo_url: str

@app.get("/")
def read_root():
    return {"message": "Hey there!"}

@app.post("/get_contributors")
async def get_contributors(url: UrlModel):
    repo = get_repo_from_url(url.repo_url)
    contributors = repo.get_contributors()
    sorted_contributors = sorted(contributors, key=lambda x: x.contributions, reverse=True)

    # Get the top 10 contributors
    top_10_contributors = sorted_contributors[:10]
    top_10_contributors_serialized = [
    {"Login": contributor.login, "Contributions": contributor.contributions}
    for contributor in top_10_contributors]

    # Display the top 10 contributors and their contributions
    for contributor in top_10_contributors:
        print(f"Login: {contributor.login}, Contributions: {contributor.contributions}")



    result = {"Repo Name: ": repo.name,
              "Repo Description: ": repo.description,
              "Top Contributors: ": top_10_contributors_serialized}
    return {"message": result}