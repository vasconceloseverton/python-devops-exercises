import subprocess
import os

def deploy(repo_url, folder):
    if not os.path.exists(folder):
        subprocess.run(["git", "clone", repo_url, folder])
    else:
        subprocess.run(["git", "-C", folder, "pull"])
    subprocess.run(["docker-compose", "-f", os.path.join(folder, "docker-compose.yml"), "up", "-d"])
