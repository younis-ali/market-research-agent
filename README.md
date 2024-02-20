# Market Compitator Analysis 
The Market Compitator Research Analysis uses fastAPI and leverages openAI to get the compitators of perticular company based on the sector it belongs.
We use fastAPI to doploy the apis and postgress sql to store the database. We initilally store some records of some dummy companies into a relation, then uses the information to promt openAI model to get the compitators based on sector and address information.
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/younis-ali/market-research-agent.git

2. Setup environment
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    setup  OPEN_AI_KEY as enivironment variable

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt

4. Locate `/resources/config.json` and setup postgress database configuration.
    ```bash
        "host": "your_host"
        "port": "your_port"
        "database": "your_database"
        "user": "your_username"
        "password": "your_password"

5. What is in database and its purpose?.
      The schema of the `orginization` relation is 
       `organization (id SERIAL PRIMARY KEY, name VARCHAR(255), sector VARCHAR(255), address TEXT)`.
       We are using this relation to store the companies. Later we are using the comapny `sector` to get the compitators using openAI text generation.

## Usage
1. Execute the command
      1. `uvicorn main:app --port 8001`
      2. Visit `http://127.0.0.1:8001/`

## Future Scope
1. Integration with external databases.
2. Use langchain for prompt engineering.
3. Integration with ERP Systems

## Screen Shots
1. Database snapshots
![image](https://github.com/younis-ali/market-research-agent/assets/32736581/a08a86a1-9c17-4d61-9c8f-9608cdf764cf)

2. User Interface
![alt text](<Screenshot from 2024-02-20 16-28-06.png>)
![image](https://github.com/younis-ali/market-research-agent/assets/32736581/e8390c5f-119d-4ff1-8b4b-f3308684b53b)
