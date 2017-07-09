import requests

kek = input("What is your file name(ex: pepe.exe)?: ")
params = {"apikey": "9035ff20fc58212e76ec2d447cf2b33f9cb1b63b59c96c370649989161f79705"}
files = {"file": (kek, open(kek, "rb"))}
response = requests.post("https://www.virustotal.com/vtapi/v2/file/scan", files=files, params=params)
json_response = response.json()
