# Dynamic motd

[![Project Tracker](https://img.shields.io/badge/repo%20status-Project%20Tracker-lightgrey)](https://randomserver.xyz/project-tracker.html)
[![Style Guide](https://img.shields.io/badge/code%20style-Style%20Guide-blueviolet)](https://github.com/StrangeRanger/bash-style-guide)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![CodeFactor](https://www.codefactor.io/repository/github/strangeranger/dynamic-motd/badge)](https://www.codefactor.io/repository/github/strangeranger/dynamic-motd)

The aim of this project is to give users useful information on the system, when logging into a server via SSH.

Example:

``` txt
               .-. 
        .-'``(|||) 
     ,`\ \    `-`.                 88                         88 
    /   \ '``-.   `                88                         88 
  .-.  ,       `___:      88   88  88,888,  88   88  ,88888, 88888  88   88 
 (:::) :        ___       88   88  88   88  88   88  88   88  88    88   88 
  `-`  `       ,   :      88   88  88   88  88   88  88   88  88    88   88 
    \   / ,..-`   ,       88   88  88   88  88   88  88   88  88    88   88 
     `./ /    .-.`        '88888'  '88888'  '88888'  88   88  '8888 '88888' 
        `-..-(   ) 
              `-` 


                               Ubuntu 20.04.2 LTS
                        Kernel Version 5.4.0-73-generic
                        Uptime 9 days 8 hours 56 minutes


  System information as of Tue Jun  1 17:57:33 2021

  CPU usage:    xxxxxx                         Users logged in: xxxxxx
  Memory Usage: 1.16GiB / 1.9GiB (61.05%)
  Disk Usage:   29.57GiB / 48.85GiB (60.53%)

9 updates to install.
0 are security updates.


Last login: Tue Jun  1 09:56:43 2021 from laptop.example.org
```

**Warning:** This is designed for Debian (11 and later), Ubuntu (20.04 and later), and other Debian-related distributions only. For Debian 10 and below, and Ubuntu 18.04 and below, please visit the [old branch](https://github.com/StrangeRanger/dynamic-motd/tree/old).

## Getting Started

### Prerequisites

You need to install some packages:

```
sudo apt-get install figlet lsb-release python3-utmp bc needrestart linuxlogo python3-apt
```

iYou can optionally install `debian-goodies` which provides `checkrestart`, which will be used to warn you about services that need to be restarted. While `needrestart` already does this, many people prefer the way `checkrestart` works/looks.

### Installation

```
sudo rm -rf /etc/update-motd.d/
sudo cp -r update-motd.d/ /etc
sudo chmod 755 /etc/update-motd.d/
sudo chmod 644 /etc/update-motd.d/colors /etc/update-motd.d/sysinfo.py
sudo mv /etc/motd /etc/motd.bak
sudo ln -s /var/run/motd /etc/motd
```

## Tested On

......

## Changes

This repo was forked from https://github.com/ldidry/dynamic-motd. Abiding by the conditions of the GPLv2 License, below is a list of all the **major** changes made to the original code/project:

- Everything relating to salting (i.e., `init.sls`, etc.) as well as `00-figlet` have been removed.
- All scripts using python2 have been upgraded to python3.
- Every file has either been renamed, rewritten, or modified.

## License

GPLv2. Have a look at the [LICENSE file](LICENSE).

## Acknowledments

- Dustin Kirkland, the guy behind the Ubuntu dynamic motd
  - https://github.com/nickcharlton/dynamic-motd/ for some of the files used or modified
- https://github.com/ldidry/dynamic-motd (forked from this repo)
