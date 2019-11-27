#!/usr/bin/env python
# coding: utf-8

#get_ipython().run_line_magic('matplotlib', 'inline')
import keras_bugprediction
import time

projects = ['Math', 'Closure', 'Lang', 'Time', 'Chart']
lastVersions = [106, 133, 65, 27, 26]
fromVersion = [41, 41, 21, 11, 11]
toVersion = [50, 50, 33, 14, 13]


file = open("../../WTP-data/bugprediction_exectime.txt","w")
for index, project in enumerate(projects):
	print('*** Project: %s ***' % project)
	lastVersion = lastVersions[index]
	start_time = time.time()
	for version in range(fromVersion[index], toVersion[index]+1):
		print('Version: %d' % version)
		keras_bugprediction.kerasBugPrediction(project, version, lastVersion)
	elapsed_time = time.time() - start_time
	print("elapsed_time: ", elapsed_time)
	meanElapsedTime = elapsed_time/(toVersion[index]-fromVersion[index]+1)
	file.write("%s,%f\n" % (project, meanElapsedTime))
file.close()