# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
var = 1
for i in range(100):
	f = open('test1.html','a')
	f.write('mukul')
	if(var>=30):
		var = 1
	if (var<=9):
		aq = str(var)
		a= "0"+str(var)
	var = int(var)
	dat = "2017-07-"+ str(var)+" "+"20:11:11"
	aas = 'export GIT_COMMITTER_DATE='+'"'+dat+'"'
	aaas = 'export GIT_AUTHOR_DATE='+'"'+dat+'"'
	print aas
	print aaas
	os.system(aas)
	os.system(aaas)
	var = var+1
	os.system('git add .')
	os.system("git commit -am 'Commit Message Here ascassadas'")
	os.system('git push -u origin master')
	f.close()
