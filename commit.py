# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
for i in range(100):
	f = open('test1.html','a')
	f.write('mukul')
	os.system('export GIT_COMMITTER_DATE="2017-05-28 20:11:11"')
	os.system('export GIT_AUTHOR_DATE="2017-06-28 20:11:11"')
	os.system('git add .')
	os.system("git commit -am 'Commit Message Here ascassadas'")
	os.system('git push -u origin master')
	f.close()
