# Dynamic motd

The aim of this project is to give users useful information on the system, when logging into a server via SSH.

Example:

```
        _,met$$$$$gg.                                                           
     ,g$$$$$$$$$$$$$$$P.                                                        
   ,g$$P""       """Y$$.".                                                      
  ,$$P'              `$$$.                                                      
',$$P       ,ggs.     `$$b:                                                     
`d$$'     ,$P"'   .    $$$                               ,#.                    
 $$P      d$'     ,    $$P      ##:          :##        :###:                   
 $$:      $$.   -    ,d$$'      ##'          `##         `#'                    
 $$;      Y$b._   _,d$P'    __  ##     __     ##  __      _     __          _   
 Y$$.    `.`"Y$$$$P"'     ,####:##  ,######.  ##.#####. :### ,######. ###.####: 
 `$$b      "-.__         ,##' `###  ##:  :##  ###' `###  ##' #:   `## `###' `##:
  `Y$$b                  ##    `##  ##    ##  ##'   `##  ##    ___,##  ##:   `##
   `Y$$.                 ##     ##  #######:  ##     ##  ##  .#######  ##'    ##
     `$$b.               ##     ##  ##'       ##     ##  ##  ##'  `##  ##     ##
       `Y$$b.            ##.   ,##  ##        ##    ,##  ##  ##    ##  ##     ##
         `"Y$b._         :#:._,###  ##:__,##  ##:__,##' ,##. ##.__:##. ##     ##
             `""""       `:#### ###  ######'  `######'  #### `#####"## ##     ##

                          Debian GNU/Linux 10 (buster)
                       Kernel Version 5.7.0-2-cloud-amd64
                               Uptime 50 minutes


  System information as of Thu Apr  9 20:03:57 2020

  System load:  0.05                 Processes:           90
  Memory usage: 62%                  Users logged in:     1
  Swap usage:   ---
  Disk Usage:
    Usage of /                       : 65.7% of 24.58GB    
    Usage of /snap/amass/774         : 100.0% of 0.01GB    
    Usage of /snap/amass/776         : 100.0% of 0.01GB    
    Usage of /snap/core/8689         : 100.0% of 0.09GB    
    Usage of /snap/core/8935         : 100.0% of 0.09GB    

  Logged in users:
  user       from laptop.example.org          at Thu Apr  9 18:41:23 2020

0 updates to install.
0 are security updates.


No mail.
Last login: Thu Apr  9 18:41:23 2020 from laptop.example.org
```

**Warning:** This is designed for Debian and Debian-related distributions only.

## Dependencies

You need to install some packages:

```
sudo apt-get install figlet lsb-release python-utmp bc needrestart linuxlogo python-apt
```

iYou can optionally install `debian-goodies` which provides `checkrestart`, which will be used to warn you about services that need to be restarted. While `needrestart` already does this, many people prefer the way `checkrestart` works/looks.

## Installation

```
cp -r update-motd.d/ /etc
chmod 755 /etc/update-motd.d/
chmod 644 /etc/update-motd.d/colors /etc/update-motd.d/sysinfo.py
mv /etc/motd /etc/motd.bak
ln -s /var/run/motd /etc/motd
```

## Changes

This repo was forked from https://github.com/ldidry/dynamic-motd. Abiding by the conditions of the GPLv2 License, below is a list of all the **major** changes made to the original code/project:

* Everything relating to salting (i.e., `init.sls`, etc.) as well as `00-figlet` have been removed.
* Almost all the files have been renamed and/or modified.

## License

GPLv2. Have a look at the [LICENSE file](LICENSE).

## Acknowledments

* Dustin Kirkland, the guy behind the Ubuntu dynamic motd
  * https://github.com/nickcharlton/dynamic-motd/ for some of the files used or modified
* https://github.com/ldidry/dynamic-motd (forked from this repo)
