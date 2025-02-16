from types import ModuleType

from pygent.tools import exceptions

class VALIDATOR:

	@staticmethod
	def validate_module_docstring(module: ModuleType):
		if not (module.__doc__ and module.__doc__.strip()):
			raise exceptions.ModuleDocNotFoundError(module.__name__)