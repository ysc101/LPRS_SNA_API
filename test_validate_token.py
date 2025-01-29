import requests
import json
from datetime import datetime

from LPRS_SNA_TOKEN import bearer_token


def test_validate_token():
    url = "http://192.168.0.162:8064/api/GISTag/NICvalidatetoken"

    # Fix missing space after 'Bearer'
    headers = {
        "Authorization": f"Bearer {bearer_token}"  # Space added after 'Bearer'
    }

    # Fix incorrect token formatting in payload
    payload = {
        "uniqueID": "10001",
        "projectId": "01",
        "rddAssetCode": "1001",
        "token": bearer_token,  # Remove curly braces
        "requestdatetime": datetime.now().isoformat(),  # Convert datetime to ISO format
        "statusCode": 0,
        "statusDesc": "JE Maker Validate token"
    }

    response = requests.post(url, headers=headers, json=payload)

    # Improved assertion message
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"

    if response.status_code == 200:
        try:
            data = response.json()
            print("Response Data:", data)

            # Save JSON response to a file
            with open("validate_response.json", "w") as json_file:
                json.dump(data, json_file, indent=4)

        except requests.exceptions.JSONDecodeError:
            print("Response not in JSON format")
    else:
        print("Response Code:", response.status_code)
        print(f"Response Text: {response.text}")


# Run the function
test_validate_token()
