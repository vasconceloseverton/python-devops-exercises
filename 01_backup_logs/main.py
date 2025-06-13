import os
import shutil
from datetime import datetime

def backup_logs(source_folder, backup_folder_base):
    if not os.path.exists(source_folder):
        print("Source folder doesn't exist.")
        return

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_folder = os.path.join(backup_folder_base, f"backup_{timestamp}")
    os.makedirs(backup_folder, exist_ok=True)

    for file in os.listdir(source_folder):
        if file.endswith(".log"):
            shutil.copy2(os.path.join(source_folder, file), backup_folder)
    print(f"Backup completed in {backup_folder}")
