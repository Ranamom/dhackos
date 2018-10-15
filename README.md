Hacker Simulator 2
=============
[Hacker Simulator 2][1] - Reincarnation of [Hacker Simulator 1](https://github.com/dimankiev/hacker_sim)

Written using Python 3.6.

Bots, subnets, interesting hacking process, miners, and a lot of interesting things included in this game.

Installation (Android)
-----------------------
1. Download and install the [Termux app][2].

2. Don't forget to give [Termux][2] the "Data/SD/Memory access" rights (If your Android version >= 5.0).

3. Launch [Termux][2].

4. Use `pkg install python` command to install Python (It's needed to launch the game)

5. Install required modules by commands below:
   ```
   pip install colorama
   pip install progressbar2
   pip install hashlib
   ```
6. Use `git clone https://github.com/dimankiev/hacker_sim_2.git` command to download the game

7. Use `cd hacker_sim_2` and `python dhackos.py` commands to start the game

8. Game will say you which modules is not installed if you doesn't installed them.

9. Have a good time :D

Installation (Windows)
-----------------------
1. Download and install (with administrator rights) the [Python][3] (Python version must be >= 3.6).

2. Install required modules by commands below:
   ```
   pip install colorama
   pip install progressbar2
   pip install hashlib
   ```
3. Download the game archive [HERE][4] and unzip it to any folder (Example: `C:\Games\dHackOS`)

4. Install required modules by commands below:
   ```
   pip install colorama
   pip install progressbar2
   pip install hashlib
   ```

5. Open cmd and use the commands below to launch the game:
   ```
   cd {FOLDER_WHERE_YOU_EXTRACTED_THE_GAME_ARCHIVE}\hacker_sim_2
   python dhackos.py
   ```
6. Game will say you which modules is not installed if you doesn't installed them.

7. Have a good time :D

Getting started
----------------
1. Create a dHackOS account at start of the game of load the previous game
   - Password can't be less than 6 symbols
   - Please don't forget the password, because it will be used to load saves
   - When you shutting down the dHackOS (game), you can save it
   - Don't try to edit the save, because you can corrupt it

2. Commands:
   ```
    apps - list of installed apps + levels
    help - list of console commands
    shutdown - shutdown dHackOS
    scan - scan subnet and search for vulnerable servers
    balance - opens Bitcoin wallet where you can see your Bitcoin balance
    load_list - shows you targets list
    dhackosf - start the dHackOS exploitation framework
    upgrade - launch dHackOS programs upgrade CLI
    stats - shows your stats
    change_ip_v - move from IPv4 (old IP version) to IPv6 (new IP version) (Can't be undone)
    version - version of dHackOS
    update_ip - replacing your ip with new one
    miner - show last 10 mined blocks (short log)
    rescan_subnet - rescans subnet to find new targets
   ```

3. Use scan to find first targets.

4. Then, select and IP and remember it.

5. Launch dHackOS Exploitation Framework by `dhackosf` command, then enter IP that you remembered

6. Don't forget to upgrade your apps

7. You can see your statistics by `stats` command

Requirements
----------------------

1. Python version >= 3.6

2. Install required modules by commands below:
   ```
   pip install colorama
   pip install progressbar2
   pip install hashlib
   ```

Links
----------
- [dimankiev (Telegram)](https://t.me/dimankiev)
- [aaa114-project](http://aaa114-project.tk)
- [dimankiev (E-Mail)](mailto:dimankiev@gmail.com)

Alpha-testers
-------------------
- [Taptrue(Telegram)](https://t.me/taptrue)

License
---------
Hacker Simulator is GNU GPL v.3 Licensed  
Copyright © 2018 dimankiev (http://aaa114-project.tk)

[1]: https://github.com/dimankiev/hacker_sim_2
[2]: https://termux.com/
[3]: https://www.python.org/downloads/windows/
[4]: https://github.com/dimankiev/hacker_sim_2/archive/master.zip
