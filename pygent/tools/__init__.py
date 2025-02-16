
from pygent import logger

from pygent.tools.loader import LOADER

def tool_class(cls):
	setattr(cls, "TOOL_CLASS", True)
	return cls

def tool_method(func):
	setattr(func, "TOOL_METHOD", True)
	return func

LOADER.load_modules()

logger.debug("pygent.tools __init__.py")

# Iterate through all modules present in tools directory
from .tools import *