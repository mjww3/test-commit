from __future__ import unicode_literals
import os
import ConfigParser

print "Enter date of format 2017-07-09"
date = raw_input()

print "Enter the time of format 20:11:11"
time = raw_input()

print "Enter your name"
name = raw_input()
if(name=="Mukul Jain"):
	email = "mukuljainagro@gmail.com"

print "Enter commit message"
m = raw_input()
os.system("git config --global user.name" +name)
os.system("git config --global user.email" +email)

final = date+" "+time
aas = 'export GIT_COMMITTER_DATE='+'"'+final+'"'
aaas = 'export GIT_AUTHOR_DATE='+'"'+final+'"'
print aas
print aaas
os.system(aas)
os.system(aaas)
os.system('git add .')
os.system("git commit -am "+"'"+m+"'")
os.system('git push -u origin master')

###########################################