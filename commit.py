"""
Ideal way to run the script

python commit.py -u rishabh -t "9/5/2017 17:54:13" -m "this is some commit message"

1. -u will be a key in the COMMITERS dict
2. -t will be the time in format: "dd/mm/yyyy hh:mm:ss"
3. -m will be the commit message
"""



# -- coding: utf-8 --
from __future__ import unicode_literals
import os, datetime, random

# list of people who can commit to zohem
COMMITERS = {
    "rishabh": {
        "name": "Rishabh Verma",
        "email": "me@rishabhverma.me"
    },
    "mukul": {
        "name": "Mukul Jain",
        "email": "mukuljainagro@gmail.com"
    },
    "abhishekg": {
        "name": "Abhishek Gupta",
        "email": "abhishekgupta.iitd@gmail.com"
    },
    "abhishekb": {
        "name": "Abhishek Bhattacharya",
        "email": "abhishek.bhattachrya@zohem.com"
    },
    "rahul": {
        "name": "Rahul Something",
        "email": "rahul@darwinlabs.io"
    }
}

# key of user in `COMMITERS` dict who will be commiting
user = "abhishekg"

# commit message from the args
commit_message = "This is some commit message"

# date time parsing
_date_time = "9/5/2017 17:54:13"
date, time = _date_time.split(" ")
month, day, year = date.split("/")
hour, minute, second = time.split(":")

# convert to integer
month = int(month)
day = int(day)
year = int(year)
hour = int(hour)
minute = int(minute)
second = int(second)

commit_time = datetime.datetime(year, month, day, hour, minute, second, random.randint(0, 80000))

# setting the profile
os.system( 'git config --global user.name "{0}"'.format(COMMITERS[user]['name']) )
os.system( 'git config --global user.email "{0}"'.format(COMMITERS[user]['email']) )

# set the actual date & time
git_date_string = '{year}-{month}-{day} {hour}:{minute}:{second} +0530'.format(
    year = commit_time.year,
    month = commit_time.month,
    day = commit_time.day,
    hour = commit_time.hour,
    minute = commit_time.minute,
    second = commit_time.second
)
os.system( 'export GIT_COMMITTER_DATE="{0}"'.format(git_date_string) )
os.system( 'export GIT_AUTHOR_DATE="{0}"'.format(git_date_string) )

# do the final commit
os.system( 'git commit -m "{0}"'.format(commit_message) )