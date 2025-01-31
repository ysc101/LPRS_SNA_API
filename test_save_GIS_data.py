import requests
import json
from datetime import datetime

from LPRS_SNA_TOKEN import bearer_token


def test_save_GIS_data():
 url="http://192.168.0.162:8064/api/GISTag/SaveGISData"

 headers={"Authorization":f"Bearer {bearer_token}"}

 payload={
  "activityCode": "4080",
  "gpcode": "4080",
  "dpancode": "4080",
  "gisdata": "[{\"spatialReference\":{\"wkid\":4326},\"paths\":[[[74.01330544311708,15.97433221674104],[74.0149362265254,15.97294318691188],[74.01303364582779,15.973066962247696],[74.01330544311708,15.97433221674104]]]}]",
  "otherGisData": "Other GIS data Kareems kitchen",
  "type": "P",
  "category": "Path",
  "uploadedDate": datetime.now().isoformat(),
  "token": "string",
  "rddassetCode": "140780",
  "projectId": "01",
  "createdDate":  datetime.now().isoformat(),
  "isactive": 0,
  "progressStatus": 1,
  "images": [{
      "imageSequenceNo": 22,
      "imageURL": "aaa/aaa22.jpg",
      "isPointInRoot": 0,
      "address": "MG nagar Belagavi "
    }]
        }
 response=requests.post(url,headers=headers,json=payload)
 assert response.status_code==200, f"expected Status Code 200 but got {response.status_code}"
 if response.status_code==200:
     try:
         data=response.json()
         print("Response Data: ",data)
         with open("GIS_Response.json" ,"w")as json_file:
            json.dump(data,json_file,indent=4)
     except requests.exceptions.JSONDecodeError:
         print("Response not in JSON")
 else:
     print("Response Code: ",response.status_code)
     print(f"Response Text ,{response.text} ")

