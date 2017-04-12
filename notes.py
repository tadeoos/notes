#!/usr/bin/env python

from datetime import datetime
from optparse import OptionParser
import os
import sys


def main():

	usage = "usage: %prog [options] note_content"
	description=' Simple project notes manager.'
	parser = OptionParser(usage=usage, description=description)
	parser.add_option("-i","--install", action="store_true", dest="install",
		help="copy script to the /usr/local/bin dir")
	parser.add_option("-d","--date", action="store_true", dest="date",
		help="add date of creation at the end of the note_content")
	parser.add_option("-s","--show", action="store_true", dest="show",
		help="print the contents of the .notes file")
	parser.add_option("-f", "--file",
				  action="store", type="string", dest="filename", default='.notes.md',
				  help="specify the name of the notes_file, default is '.notes.md'")
	parser.add_option("-t", "--title",
				  action="store", type="string", dest="title", default='# NOTES',
				  help="specify the first line of a new notes_file, deafult is '# NOTES'")

	options, args = parser.parse_args()

	if options.install:
		os.system('cp notes.py /usr/local/bin/notes.py')
		return True

	file = options.filename

	if os.path.exists('.gitignore'):
		if file not in open('.gitignore').read():
			with open('.gitignore', 'a') as gitignore:
				gitignore.write('\n{}\n'.format(file))
			

	

	if len(args)>0:
		check_if_first = options.filename not in os.listdir('.')
		add_title = options.title+'\n\n' if check_if_first else ''
		add_date = '\t// '+datetime.now().strftime('%d.%m.%Y at %H:%M') if options.date else ''
		note_text = add_title+"- [ ] "+' '.join(args) + add_date + '\n\n'

		with open(file, "a+") as f:
			f.write(note_text)

	if options.show:
		os.system("cat {}".format(file))

if __name__ == '__main__':
	main()