class ModuleDocNotFoundError(ModuleLoadError):

	def __init__(self, module_name: str):
		self.module_name = module_name
		self.message = f"Unable to find docstring for module: {self.module_name}"
		super().__init__(self.message)

	def __str__(self):
		return f"{super().__str__()}.{self.__class__.__name__}: {self.message}"

	def __repr__(self):
		return f"{super().__str__()}.{self.__class__.__name__}: {self.message}"