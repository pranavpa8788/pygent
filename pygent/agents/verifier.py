from pygent.api.llm import LLM
from pygent.api import models
from pygent.utils import prompts

class Verifier(LLM):
	def __init__(self, model_name: str) -> None:
		super().__init__(self, model_name)

		self.MAIN_PROMPT = prompts.OUTPUT_GENERATOR_AGENT_PROMPT
	
	def query(self, prompt: str) -> None: