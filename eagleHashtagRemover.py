# eagleHashtagRemover.py
#! /usr/bin/env python 3
"""Script to remove all CADSoft EAGLE .b# unnecessary files.

	Simply run: python eagleHastagRemover.py /directory/to/search/

	Does 2 things: first finds all .b# and .s# files in the directory, 
	and second removes them.
"""
import os
import sys
import fnmatch

def hastag_finder(searchDirectory):
	"""Finds location of all CADSoft EAGLE .b# files.

	Args:
		searchDirectory: Directory to search for .b# files.

	Returns:
		filesToRemove: List of locations of .b# files.
	"""
	filesToRemove = []
	for file in os.listdir(searchDirectory):
		# Look for all files in directory that match filenames *b#*, ex Eric.b#3
		if fnmatch.fnmatch(file, '*.b#*'):
			fullLocation = searchDirectory + '/' + file
			filesToRemove.append(fullLocation)
		# Look for all files in directory that match filenames *s#*, ex Eric.b#3
		if fnmatch.fnmatch(file, '*.s#*'):
			fullLocation = searchDirectory + '/' + file
			filesToRemove.append(fullLocation)

	return filesToRemove

def hashtag_remover(fileList):
	"""Deletes all found CADSoft EAGLE .b# files.

	Args:
		fileList: Directory location where the .b# and .s# files are in.

	Returns:
		Nothing.
	"""
	for file in fileList:
		print("Trying to delete: ", file)
		try:
			os.remove(file)
		except:
			print("Error while deleting file : ", file)

def main():
	hashtag_files = hastag_finder(sys.argv[1])
	hashtag_remover(hashtag_files)

if __name__ == '__main__':
	main()