import requests
import datetime
import json

from LPRS_SNA_TOKEN import bearer_token


def test_Check_Intersect():
    url="http://192.168.0.162:8064/api/GISTag/CheckIntersectPoint"
    headers={"Authorization":f"bearer {bearer_token}"}
    payload={
  "gisdata": "[{\"spatialReference\":{\"wkid\":4326},\"paths\":[[[74.01330544311708,15.97433221674104],[74.0149362265254,15.97294318691188],[74.01303364582779,15.973066962247696],[74.01330544311708,15.97433221674104]]]}]",
  "projectId": "01",
  "token": "kkhk"
}
    response=requests.post(url,headers=headers,json=payload)
    assert response.status_code==200,f"Expected Status Code 200 but got {response.status_code}"
    if response.status_code==200:
        try:
            data=response.json()
            print("Response Data: ",data)
            with open("CheckIntersect_response.json","w") as json_file:
                json.dump(data,json_file,indent=4)
        except requests.exceptions.JSONDecodeError:
            print("Response not in JSON")
    else:
        print("Response Code : ",response.status_code)
        print("Response text: ",response.text)
