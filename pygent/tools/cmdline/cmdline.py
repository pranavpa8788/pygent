import os
from pathlib import Path

from pygent.tools import tool_class

@tool_class
class CMDLINE:
	'''
	The CMDLINE class provides static methods to interact with the cmdline of the OS.
	'''

	@staticmethod
	def ls() -> list[str]:
		'''
		Description: List all the files and directories in the current directory
		Parameters: None
		Retuns: String
		Example: ls()
		'''

		return os.listdir()

	@staticmethod
	def cwd() -> str:
		'''
		Description: Get the current working directory's full path
		Parameters: None
		Returns: String
		Example: cwd()
		'''

		return os.getcwd()

	@staticmethod
	# TODO: perform path validation and return more verbose log
	def cd(path: str) -> str:
		'''
		Description: Change directory into the given path
		Parameters: String - Path to cd into
		Returns: String - information regarding the success/failure of command execution
		Example: cd("./bin/")
		'''
		os.chdir(path)
		return cwd()

	@staticmethod
	# TODO: perform path validation and return more verbose log
	def mkdir(dir_name: str):
		'''
		Description: Create a new directory with the given directory name in the current working directory path
		Parameters: String - Name of directory to create
		Returns: String - information regarding the success/failure of command execution
		Example: mkdir("./tests/")
		'''
		os.mkdir(dir_name)
		return dir_name

	@staticmethod
	# TODO: perform path validation and return more verbose log
	def mkfile(file_name: str):
		'''
		Description: Create a new file in the current working directory path
		Parameters: String - Name of file to create
		Returns: String - information regarding the success/failure of command execution
		Example: mkfile("./log.txt")
		'''
		Path(file_name).touch()
		return file_name

	@staticmethod
	def validate_path() -> bool:
		pass

@tool_class
class SOMETHING:

	def __init__(self):
		...