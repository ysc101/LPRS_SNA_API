import json


  # Open the JSON file and load data into a Python dictionary
with open("token_response.json", "r") as json_file:
  data = json.load(json_file)  # Convert JSON to Python dictionary

# Print loaded data
print("Loaded Data:", data)

# Access specific values
bearer_token = data.get("token")  # Extract token value
print("Extracted Token:", bearer_token)
