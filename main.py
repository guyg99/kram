from fastapi import FastAPI
from APIs.github_api import get_repo_name_and_desc

app = FastAPI()

@app.get("/")
def read_root():
    name,desc = get_repo_name_and_desc("guyg99","kram")
    result = {"Repo Name: ": name,
                  "Repo Desc: ": desc}
    return {"message": result}
