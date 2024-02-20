
from src.mra import MarketResarchAgent
from src.db_client import DBClient

from fastapi import FastAPI, Request
from pydantic import BaseModel
import os
from openai import OpenAI

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

app.mount(
    "/market-research-agent/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "market-research-agent/static"),
    name="static",
)

# Model for competitor analysis request
class ComRequest(BaseModel):
    name: str

# Model for competitor analysis response
class ComResponse(BaseModel):
    company_name: str
    analysis: str

# Create an instance to the classes

agent = MarketResarchAgent()

# create the instace of database client by passing the database configuration json
dbObj = DBClient(config_path="resources/config.json")
dbObj.connect()

data = dbObj.execute_query(query="SELECT * FROM organization;")
print(data)

templates = Jinja2Templates(directory="templates")

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request}
    )

@app.get("/get_companies")
async def get_companies():
    data = dbObj.execute_query("SELECT name FROM organization;")
    company_names = []
    for company in data:
        company_names.append(company[0])
    
    return {"companies": company_names}

# Endpoint for market research analysis
@app.post("/analyse_competitors")
async def  analyze_competitors(company: ComRequest):
    data = dbObj.execute_query(f"select sector, address from organization where name = '{company.name}'")

    sector  = data[0][0]
    address = data[0][1]

    client = OpenAI()
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"Give me the list of competators of a company whose sector is {sector} and address is {address}"},
    ]
    )

    response_content = completion.choices[0].message.content
    response_json = {"message": response_content}

    return response_json
        
    
