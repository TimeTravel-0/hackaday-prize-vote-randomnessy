#!/usr/bin/env python

import csv
from operator import itemgetter


with open("nessy-2015-06-30-tail.txt") as infile:
	reader = csv.reader(infile, delimiter=';', quotechar='"')
	
	histo = dict()
	items = []
	itemsum = 0
	
	for item in reader:
		# create histo:
		try:
			histo[item[1]]+=1
		except:
			histo[item[1]]=1
			
		itemsum+=float(item[1])
		items.append([item[0],float(item[1])])

	
	print itemsum
	# sort
	s = sorted(items, key=itemgetter(1))
	
	for row in s:
		print row, row[1]/itemsum*100


	print "-"*80
	for key, value in histo.iteritems() :
		print '%f;%i'%(float(key)/itemsum*100,value)

