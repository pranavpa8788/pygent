from pygent import logger
from pygent.api.llm import LLM
from pygent.api import models
from pygent.utils import prompts
from pygent.tools import tools

class Agent(LLM):
	def __init__(self, model: models.LLM_Model) -> None:
		super().__init__(model)

		self.BASE_PROMPT = prompts.AGENT_BASE_PROMPT

	def query(self, prompt: str) -> None:
		# self.BASE_PROMPT = self.BASE_PROMPT.replace("\n", "")
		# self.BASE_PROMPT = self.BASE_PROMPT.replace("\t", "")
		print(logger.hasHandlers())
		logger.info(f"BASE PROMPT: ${repr(self.BASE_PROMPT)}")
		PARSED_PROMPT = self.BASE_PROMPT.format(TOOLS_PROMPT = "", INPUT_PROMPT = prompt)

		super().query(PARSED_PROMPT)
	
if __name__ == "__main__":
	agent = Agent(models.DEEPSEEK_R1)
	# agent.query("How to detect validity of json in python?")