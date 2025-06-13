import os
import shutil

def deploy_symlink(current, new):
    if os.path.islink(current) or os.path.exists(current):
        os.remove(current)
    os.symlink(new, current)
    print(f"Linked {current} -> {new}")
