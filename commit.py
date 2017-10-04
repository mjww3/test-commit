# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
var = 01
var = str(var)
for i in range(100):
	f = open('test1.html','a')
	f.write('mukul')
	if var<10:
		var = "0"+str(var)
	dat = "2017-07-"+ str(var)+" "+"20:11:11"
	aas = 'export GIT_COMMITTER_DATE='+'"'+dat+'"'
	aaas = 'export GIT_AUTHOR_DATE='+'"'+dat+'"'
	print aas
	print aaas
	os.system(aas)
	os.system(aaas)
	(var) = int(var)+1
	os.system('git add .')
	os.system("git commit -am 'Commit Message Here ascassadas'")
	os.system('git push -u origin master')
	f.close()
