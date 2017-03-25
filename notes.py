#!/Users/Tadeo/anaconda/bin/python

from datetime import datetime
import os
import sys

def main():
	if sys.argv[1] == '-i':
		os.system('cp notes.py /usr/local/bin/notes.py')
		args = sys.argv[2:]
		return
	args = sys.argv[1:]

	file = '.notes/'+args[0]
	note_text = "- "+' '.join(args[1:])+'\t/ ('+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+')\n\n'

	# os.makedirs('.notes', exist_ok=True)
	try:
		os.mkdir('.notes')
		with open(file,"w") as f:
			f.write('# NOTES\n\n')
	except FileExistsError:
		pass
	with open(file,"a+") as f:
		f.write(note_text)

if __name__ == '__main__':
	main()