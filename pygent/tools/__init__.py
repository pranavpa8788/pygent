def tool_class(cls):
	setattr(cls, "TOOL_CLASS", True)
	return cls

def tool_method(func):
	setattr(func, "TOOL_METHOD", True)
	return func