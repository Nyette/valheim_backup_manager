# Valheim Backup Manager

Automatically backup your Valheim data every 5 minutes.

I made this because friends were experiencing the [world-destroying bug](https://www.pcgamer.com/valheim-backup-world-character/).

It will save a copy of the Valheim directory at [the default location](https://www.pcgamingwiki.com/wiki/Valheim#Save_game_data_location) to `C:\Users\User\valheim_backup` every 5 minutes, if the size of at least one world `db` file is greater than a kilobyte. This condition exists because you don't want to backup older/smaller world(s) by mistake.

Additional features are on the way!