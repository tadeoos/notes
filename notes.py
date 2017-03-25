#!/usr/bin/env python

from datetime import datetime
import os
import sys

def main():
	if sys.argv[1] == '-i':
		os.system('cp notes.py /usr/local/bin/notes.py')
		return

	args = sys.argv[1:]

	file = '.notes/'+args[0]
	note_text = "- [ ] "+' '.join(args[1:])+'\t// added '+datetime.now().strftime('%d.%m.%Y at %H:%M')+'\n\n'

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