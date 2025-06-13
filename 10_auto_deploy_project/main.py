import subprocess
import logging
import time
import os

logging.basicConfig(filename='deploy.log', level=logging.INFO)

def auto_deploy(repo_dir):
    try:
        logging.info("[START] Deploy at %s", time.ctime())
        subprocess.run(["git", "-C", repo_dir, "pull"], check=True)
        subprocess.run(["docker-compose", "-f", os.path.join(repo_dir, "docker-compose.yml"), "down"], check=True)
        subprocess.run(["docker-compose", "-f", os.path.join(repo_dir, "docker-compose.yml"), "build"], check=True)
        subprocess.run(["docker-compose", "-f", os.path.join(repo_dir, "docker-compose.yml"), "up", "-d"], check=True)
        logging.info("[END] Success at %s", time.ctime())
    except Exception as e:
        logging.error("[ERROR] %s", str(e))
