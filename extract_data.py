# import requests
# import pandas as pd

# url = "https://jsonplaceholder.typicode.com/users"  

# # Example API
# response = requests.get(url)

# if response.status_code == 200:
#     data = response.json()
#     df = pd.DataFrame(data)
#     df = df[["id", "name"]]
#     print(df)
# else:
#     print("Failed to fetch data. Status code:", response.status_code)

import os

# Get the environment variable named "TOKEN"
token = os.getenv("TOKEN")

# Print the token value
print(f"Token = {token}")

# Check if the token matches the expected value
if token == "12345":
    print("valid")
else:
    print("invalid")
