from pygent import logger
from pygent.tools.loader import LOADER

TOOLS_STRING = """
TOOLS:
"""

# Iterate through all modules present in tools directory

def load_tools():
	TOOL_MODULES = LOADER.load_modules()

	logger.debug("pygent.tools __init__.py")
	# print(f"tool modules: {TOOL_MODULES}")
	TOOLS_STRING = ""
	# for tool_module in TOOL_MODULES:

	# 	TOOLS_STRING += f""

	# 	logger.info(tool_module.TOOL_CLASSES)

	# 	for module in tool_module.TOOL_CLASSES:
	# 		module_name = f"tools.{tool_module}.{module}"
	# 		module_description = module.__doc__