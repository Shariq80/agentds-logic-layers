import os
from agentds.client import BenchmarkClient

# Create client with API key and team name
api_key = os.environ.get("AGENTDS_API_KEY") 
team_name = os.environ.get("AGENTDS_TEAM_NAME")
client = BenchmarkClient(api_key, team_name)

# Authenticate with the provided credentials
if client.authenticate():
    print(f"Successfully authenticated as {client.team_name}")
else:
    print("Authentication failed. Check your API key and team name.")

# Get available domains
domains = client.get_domains()
print(f"Available domains: {domains}")

# Get challenge 1 for a specific domain
domain = "Insurance"
challenge_number = 1

# Submit a response
response = process()  # Your agent logic here
success = client.submit_prediction(domain, challenge_number, response)
