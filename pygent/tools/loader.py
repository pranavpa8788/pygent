import os
import sys
import glob
import pkgutil
import inspect
import importlib

from pygent import logger

from pygent.tools.validator import VALIDATOR

class LOADER:

	@staticmethod
	def load_modules():
		TOOL_MODULES = []

		package_dir = os.path.dirname(__file__)

		for _, module_name, _ in pkgutil.iter_modules([package_dir]):
			logger.debug(f"Processing module with name: {module_name}, isdir: {os.path.isdir(os.path.join(package_dir, module_name))}")

			# Process further only if it is a directory
			if os.path.isdir(os.path.join(package_dir, module_name)):
				try:
					logger.debug(f"Importing module: {module_name}")
					module = importlib.import_module(f".{module_name}", package="pygent.tools")			
					logger.info(f"tool module type: {type(module)}")

					VALIDATOR.validate_module_docstring(module)

					LOADER.get_module_files(module)

					TOOL_MODULES.append(module)
				except ImportError as e:
					logger.error(f"Error occurred while importing tool: {module_name} in __init__.py, {e}")


	@staticmethod
	def get_module_files(module):
		module_dir = os.path.dirname(module.__file__)

		logger.info(f"module: {module}, module_dir: {module_dir}")

		for _, module_name, _ in pkgutil.iter_modules([module_dir]):
			full_module_name = f"{module.__name__}.{module_name}"

			logger.info(f"Attempting to import module: {full_module_name}")

			try:
				module = importlib.import_module(full_module_name)
			except ImportError:
				logger.info(f"ImportError {e} while attempting to import module {full_module_name}")

				return False
			
			logger.info(f"Successfully imported module: {full_module_name}, members: {inspect.getmembers(module, inspect.isclass)}")
			
			for name, cls in inspect.getmembers(module, inspect.isclass):
				if cls.__module__ == full_module_name and hasattr(cls, "TOOL_CLASS"):
					logger.info(f"module_name: {full_module_name}, class: {cls}")