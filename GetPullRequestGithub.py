import requests
respone = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
complete_details = respone.json()
print(complete_details[0]["users"]["login"])
