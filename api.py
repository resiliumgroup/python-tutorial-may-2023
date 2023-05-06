import httpx

USERNAME = ""
PASSWORD = ""

def get_header():
    token = httpx.post("https://riskrunner.app/api/token", data={"username": USERNAME, "password": PASSWORD})
    return {"Authorization": f"Bearer {token.json()['access_token']}"}

def get_assessments():
    return httpx.get("https://riskrunner.app/api/assessments", headers=get_header())
