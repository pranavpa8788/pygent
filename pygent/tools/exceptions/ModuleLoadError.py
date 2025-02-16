class ModuleLoadError(Exception):
	def __init__(self, module_name: str, message: str):
		self.module_name = module_name
		self.message = message
		super().__init__(self.message)

	def __str__(self):
		return f"Error while loading module {self.module_name} - {self.message}"

class ModuleDocNotFoundError(ModuleLoadError):
	def __init__(self, module_name: str):
		message = f"Unable to find docstring for module"
		super().__init__(module_name, message)
