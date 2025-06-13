import time
import requests
import subprocess

def health_check_loop(url, container_name):
    while True:
        try:
            res = requests.get(url)
            if res.status_code != 200:
                raise Exception("Not healthy")
        except:
            print("Service down, restarting container...")
            subprocess.run(["docker", "restart", container_name])
        time.sleep(30)
