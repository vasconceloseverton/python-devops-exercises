import psutil
import requests
import json

def post_system_info(url):
    data = {
        "cpu": psutil.cpu_percent(),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage('/').percent
    }
    res = requests.post(url, json=data)
    print(res.status_code, res.text)