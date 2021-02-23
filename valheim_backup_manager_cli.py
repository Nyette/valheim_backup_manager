from pathlib import Path
import platform
import schedule
import shutil
import sys
import time

def backup():
    config = {
        'Windows': Path.home() / 'AppData' / 'LocalLow' / 'IronGate' / 'Valheim'
    }
    current_os = platform.system()
    src = config[current_os]
    if src.exists():
        worlds_path = src / 'worlds'
        if worlds_path.exists():
            paths = list(worlds_path.iterdir())
            if len(paths) > 0:
                big_db_paths = [path for path in paths if str(path).endswith('.db') and path.stat().st_size >= 1000]
                if len(big_db_paths) > 0:
                    dst = Path.home() / 'valheim_backup'
                    shutil.copytree(src, dst, dirs_exist_ok = True)
                    print(f"Copied data at {src} to {dst}")
                    time_stamp = time.ctime()
                    print(f"Created backup on {time_stamp}")
                    print("Press [Ctrl] and [C] to stop backup and exit\n")
                    return 0
                else:
                    print("Your world db files are either missing or not yet big enough to backup")
                    return 1
            else:
                print("The worlds directory is empty")
                return 1
        else:
            print("The worlds directory does not exist")
            return 1
    else:
        print("Install Valheim first")
        return 1

def main():
    status = backup()
    if status == 0:
        schedule.every(5).minutes.do(backup)
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

if __name__ == '__main__':
    main()