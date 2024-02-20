# Market Compitator Analysis 

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

#### 5. What is in database and its purpose?
    The schema of the `orginization` relation is 
    `organization (id SERIAL PRIMARY KEY, name VARCHAR(255), sector VARCHAR(255), address TEXT)`.
    We are using this relation to store the companies. Later we are using the comapny `sector` to get the compitators using openAI text generation.

## Usage
1. Execute the command
    ```bash uvicorn main:app --port 8001
    Visit
    http://127.0.0.1:8001/
    ```


![alt text](<Screenshot from 2024-02-20 16-28-06.png>)