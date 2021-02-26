# Valheim Backup Manager

Automatically backup your Valheim data.

I made this because friends were experiencing the [world-destroying bug](https://www.pcgamer.com/valheim-backup-world-character/).

## Customization / Options

Running `python valheim_backup_manager_cli.py` will bring about default behavior.

It will save a copy of the Valheim directory at [the default location](https://www.pcgamingwiki.com/wiki/Valheim#Save_game_data_location) to `C:/Users/User/valheim_backup` every 5 minutes, if the size of at least one world `db` file is greater than a kilobyte. This condition exists because you don't want to backup older/smaller worlds by mistake.

### Change Destination

Use the `--dst` flag. If you wanted to change the destination to the Desktop, you'd run:

`python valheim_backup_manager_cli.py --dst C:/Users/User/Desktop`

Note that you are setting the *parent* directory of the backup.

It will automatically create the `valheim_backup` directory for you, which will update with each backup.

### Change Frequency

Use the `--freq` flag. If you wanted to make the backup happen every 2 minutes, you'd run:

`python valheim_backup_manager_cli.py --freq 2`
