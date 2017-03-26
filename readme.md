# NOTES

A simple script to create short notes while developing a project.

## INSTALATION

- download `notes.py` file and save it wherever you please

## USAGE

first time run (assuming you are in the directory where `notes.py` is stored):

`python notes.py -i`

this will copy the script into /usr/local/bin directory.  
Assuming you have it in your path you can now run:

`notes.py notes_content`

from wherever on your computer.

This will create (or append if it exist) a `.notes.md` file with 'notes_content' on a new line and the date of creation.

### Example output:

`notes.py -d mail to admin` produces the following in .notes.md:
```
# NOTES

- [ ] mail to admin   // 25.03.2017 at 17:38
```