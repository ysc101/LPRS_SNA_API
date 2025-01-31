import requests
import json
import datetime
def test_GetAllGISDataByGPOrDPCode():
    url="http://192.168.0.162:8064/api/GISTag/GetAllGISDataByGPOrDPCode"
    params={"Gpcode":908,
"Dpancode":3,
"ProjectId":"01"
}
    response=requests.get(url,params=params)
    assert response.status_code==200 ,f"Expected Response 200 but got {response.status_code}"
    if response.status_code==200:
        try:
            data=response.json()
            print("Response data: ",data)
            with open("GetAllGISDataByGPOrDPCode_Response.json","w")as jsonfile:
                json.dump(data,jsonfile,indent=4)
        except requests.exceptions.JSONDecodeError:
            print("Response not in JSON")
    else:
        print("Response Code: ",response.status_code)
        print(response.text)
