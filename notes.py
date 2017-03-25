#!/usr/bin/env python

from datetime import datetime
from optparse import OptionParser
import os
import sys

def main():

	usage = "usage: %prog [options] note_content"
	description=' Simple project notes manager.'
	parser = OptionParser(usage=usage, description=description)
	parser.add_option("-i","--install", action="store_true", dest="install", help="copy script to the /usr/local/bin dir")
	parser.add_option("-d","--date", action="store_true", dest="date", help="add date of creation at the end of the note_content")


	options, args = parser.parse_args()

	if options.install:
		os.system('cp notes.py /usr/local/bin/notes.py')
		return True

	file = '.notes/'+args[0]
	note_text = "- [ ] "+' '.join(args[1:])
	if options.date:
		note_text += '\t// added '+datetime.now().strftime('%d.%m.%Y at %H:%M')
	note_text += '\n\n'

	os.makedirs('.notes', exist_ok=True)

	short = [file for file in os.listdir('.notes') if file.startswith(args[0])]
	try:
		assert(len(short)<2)
		if len(short)==1:
			file = '.notes/' + short[0]
		else:
			note_text = '# NOTES\n\n' + note_text
	except AssertionError:
		print('-ERROR-\nNote not saved: the name of the notes_file is ambigous.')
		return

	with open(file,"a+") as f:
		f.write(note_text)

if __name__ == '__main__':
	main()