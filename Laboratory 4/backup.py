import time
from subprocess import run
import shutil
import sys
from pathlib import Path
import os
import csv

def backup(path):

    current_time = time.strftime('%Y-%m-%d-%H-%M-%S')

    dir_name = os.path.basename(path)
    name = f"{current_time} - {dir_name}"

    user_dir = os.path.expanduser("~")
    backups_dir = os.path.join(user_dir, "backups")

    # backups_dir = os.getenv('BACKUPS_DIR', os.path.expanduser("~/backups"))
    # backups_dir = os.path.expanduser(backups_dir)

    shutil.make_archive(name, 'zip', path)

    if os.path.exists(backups_dir):
        shutil.move(f"{name}.zip", os.path.join(backups_dir, f"{name}.zip"))
    else:
        os.makedirs(backups_dir)
        shutil.move(f"{name}.zip", os.path.join(backups_dir, name))

    history = os.path.join(backups_dir, 'history.csv')
    his_data = {'date': current_time, 'directory': dir_name, "name": name}

    if os.path.exists(history):

        with open(history, mode='a') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'directory', 'name'])
            writer.writerow(his_data)
    else:
        with open(history, mode='w') as file:
            writer = csv.DictWriter(file, fieldnames=['date', 'directory', 'name'])
            writer.writeheader()
            writer.writerow(his_data)

if __name__ == '__main__':
    backup(Path(sys.argv[1]))
