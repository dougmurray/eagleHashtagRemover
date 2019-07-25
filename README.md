eagleHashtagRemover
===================

Script to remove unnecessary .b# files produced from CADSoft EAGLE board file edits.  

How to run
-----------

To run the script just type:

	python eagleHashtagRemover.py /path/to/search/for/bhashtagfiles

with the */path/to/search/for/bhashtagfiles* being the location of the .b# files you would like to remove.  

How it works
-------------

When editing a CADSoft EAGLE board file numerous files with the extension .b#number, example pcb.b#1, are produced.  As they accumulate over time with each edit, and have no real prupose for saving the board file, they can be removed from the directory.  This simple script looks in the path given and finds all files with the .b#number extensions and deletes them.  