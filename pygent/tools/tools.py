from pygent.tools import TOOL_MODULES
from pygent import logger

TOOLS_STRING = """
TOOLS:
"""

def load_tools():
	# print(f"tool modules: {TOOL_MODULES}")
	TOOLS_STRING = ""
	for tool_module in TOOL_MODULES:

		TOOLS_STRING += f""

		logger.info(tool_module.TOOL_CLASSES)

		for module in tool_module.TOOL_CLASSES:
			module_name = f"tools.{tool_module}.{module}"
			module_description = module.__doc__
