import csv
import subprocess

def create_users_from_csv(csv_file):
    with open(csv_file, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            username = row[0]
            subprocess.run(["sudo", "useradd", "-m", username])
