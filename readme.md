# NOTES

A simple script to create short notes while developing a project.

## USAGE

- first time run:
`python notes.py -i`
this will copy the script into /usr/local/bin directory. Assuming you have it in your path you can now run:
`notes.py notes_file notes_content`
from wherever on your computer.
This will create (or append if it exist) a `notes_file` in .notes directory with 'notes_content' on a new line and the date of creation.