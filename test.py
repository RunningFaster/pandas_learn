import requests

a = ["0606",
     "0611",
     "0612",
     "0613",
     "0614",
     "0601",
     "0602",
     "0616",
     "0607",
     "0603",
     "0604",
     "0605",
     "0615",
     "0617"]


def get_info(path):
    for i in a:
        res = method_name(path)
        print(res)


def method_name(path):
    res = requests.post(
        "http://12.113.230.128:8080/streetapp/" + path, json={"start": 1, "limit": 2, "streetId": ""},
        headers={'Authorization': "20200a279601"}).json()
    return res


get_info("jointlawenforcement/list")
