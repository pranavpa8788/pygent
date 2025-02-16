import requests
import json
import logging

from pygent import logger
from pygent.api import models

class LLM:
	def __init__(self, model: models.LLM_Model) -> None:
		self.MODEL = model

		logger.info(f"Initializing class for model: {self.MODEL.NAME}")

		self.URL = "https://openrouter.ai/api/v1/chat/completions"
		self.HEADERS = {
			"Authorization": "Bearer {API_KEY}".format(API_KEY = self.MODEL.API_KEY),
		}

		logger.info(f"Finished initializing class for model: {self.MODEL.NAME}")

	
	def query(self, prompt: str) -> requests.Response:
		logger.info("Initializing data for query")

		DATA = json.dumps({
			"model": self.MODEL.TAG,
			"messages": [{
				"role": self.MODEL.ROLE,
				"content": prompt
			}]
		})

		logger.info(f"Beginning POST request to model: {self.MODEL.NAME}")

		for i in range(self.MODEL.RETRIES):
			response = requests.post(url = self.URL, headers = self.HEADERS, data = DATA)

			if (self.MODEL.check_response_status(response)):
				logger.info(f"Got response: {response}")

				logger.info(self.MODEL.get_message_from_response(response))
				logger.info(f"JSON response: {response.json()}")
				break
			else:
				logger.info(f"Got response status: {response.status_code}, retrying ({i}/{self.MODEL.RETRIES})")


if __name__ == "__main__":
	llm = LLM(models.DEEPSEEK_R1)
	# llm.query("My name is Tony Shark")
	# llm.query("Do you remember my name?")