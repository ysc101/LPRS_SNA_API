import requests
import json

def test_create_token():
    url="http://192.168.0.162:8064/api/CreateToken/CreateToken"
    params={"Username":"MAKER1ASK",
            "Password":"Pass@123",
            "ProjectId":"02"}
    response=requests.get(url,params=params)
    assert response.status_code==200, f"Expected Status code 200,but got {response.status_code}"
    if response.status_code==200:
        try:
            data=response.json()
            print("Response Data: ",data)
            with open("token_response.json","w") as json_file:
                json.dump(data,json_file,indent=4)
        except requests.exceptions.JSONDecodeError:
            print("Response not in JSON")
    else:
        print("Resposne Code ",response.status_code)
        print(f"Response text,{response.text}")

