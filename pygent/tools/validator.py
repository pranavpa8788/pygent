from types import ModuleType

from pygent.tools import exceptions

from pygent import logger

class VALIDATOR:

	@staticmethod
	def validate_module_docstring(module: ModuleType):
		logger.debug(f"module: {module.__name__}, doc: {module.__doc__}")
		if not (module.__doc__ and module.__doc__.strip()):
			raise exceptions.ModuleDocNotFoundError(module.__name__)