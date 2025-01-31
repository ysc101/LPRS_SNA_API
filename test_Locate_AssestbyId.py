import requests
import json
import datetime
def test_Locate_AssetbyID():
  url="http://192.168.0.162:8064/api/GISTag/LocateAssestbyId"
  params={"RddassetCode":140780,
"Gpcode":4080,
"Dpancode":4080,
"ProjectId":"01",
"Token":"qwerty",
"ProgressStatus":"",
"SequenceNumber":""}
  response=requests.get(url,params=params)
  assert response.status_code==200, f"Expected 200 but got {response.status_code}"
  if response.status_code==200:
      try:
          data=response.json()
          print("Resposnse Data: ",data)
          with open("AssetbyID_response.json","w") as json_file:
              json.dump(data,json_file,indent=4)
      except requests.exceptions.JSONDecodeError:
          print("Response not in JSON")
  else:
      print("Response Code : ",response.status_code)
      print(f"Response text: {response.text}")