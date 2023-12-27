#!/usr/bin/env python3

import os
import sys

CMD = 'wmic memphysical get maxcapacity'

def conversion(kb):
	'''converts output from Command Prompt to GB from KB'''

	gb = (int(kb) / 1024) / 1024
	return int(gb)

def proc():
	'''Gets maximum RAM capacity of computer using Windows Command Prompt'''

	output = os.popen('cmd.exe /c "wmic memphysical get maxcapacity"').read().replace("\n","").split(" ")
	
	try:
		kb = int([output[output.index(i)] for i in output if i.isnumeric()][0])
	except:
		try:
			output = output.strip()
			kb = int([output[output.index(i)] for i in output if i.isnumeric()][0])
		except Exception as e:
			print("Error occured during script execution.\n>>> %s" % e)
			sys.exit(1)

	ram = conversion(kb)
	return ram

def run():
	'''Runs script's core functions during main module execution'''

	ram = proc()
	print('Maximum RAM Capacity is %i GB' % ram)

if __name__ == '__main__':
	'''Main module execution'''
	run()
