import argparse
from pathlib import Path
import platform
import schedule
import shutil
import sys
import time

def backup(config):
    location = {
        'Windows': Path.home() / 'AppData' / 'LocalLow' / 'IronGate' / 'Valheim'
    }
    current_os = platform.system()
    src = location[current_os]
    if src.exists():
        worlds_path = src / 'worlds'
        if worlds_path.exists():
            paths = list(worlds_path.iterdir())
            if len(paths) > 0:
                big_db_paths = [path for path in paths if str(path).endswith('.mp4') and path.stat().st_size >= 1000]
                if len(big_db_paths) > 0:
                    dst = config['dst'] / 'valheim_backup'
                    shutil.copytree(src, dst, dirs_exist_ok=True)
                    print(f"Copied data at {src} to {dst}")
                    time_stamp = time.ctime()
                    print(f"Created backup on {time_stamp}")
                    print("Press [Ctrl] and [C] to stop backup and exit\n")
                    config['status'] = 0
                    return config
                else:
                    print("Your world db files are either missing or not yet big enough to backup")
                    config['status'] = 1
                    return config
            else:
                print("The worlds directory is empty")
                config['status'] = 1
                return config
        else:
            print("The worlds directory does not exist")
            config['status'] = 1
            return config
    else:
        print("Install Valheim first")
        config['status'] = 1
        return config

def main(config):
    config = backup(config)
    if config['status'] == 0:
        schedule.every(config['freq']).minutes.do(backup, config)
        try:
            while True:
                schedule.run_pending()
                time.sleep(1)
        except KeyboardInterrupt:
            schedule.clear()
            sys.exit()
    else:
        input("Press [Enter] to exit\n")
        sys.exit()

def handle_input():
    parser = argparse.ArgumentParser(
        description="Automatically backup your Valheim data"
    )
    parser.add_argument(
        "--dst",
        type=Path,
        default=Path.home(),
        help="This is a string representing the path you'd like to save the backup to.",
    )
    parser.add_argument(
        "--freq",
        type=int,
        default=5,
        help="This is an integer representing how often the backup should happen in minutes.",
    )
    args = parser.parse_args()
    config = vars(args)
    return config

if __name__ == '__main__':
    config = handle_input()
    main(config)