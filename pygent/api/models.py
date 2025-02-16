import json
import pprint
from requests import Response
from abc import ABC, abstractmethod

from pygent import API_KEYS

class LLM_Model(ABC):
	NAME = None
	TAG = None
	ROLE = None

	API_KEY = None

	TIMEOUT = None
	RETRIES = None

	@abstractmethod
	def get_message_from_response(response: Response):
		pass

class DEEPSEEK_R1(LLM_Model):
	NAME = "DeepSeek R1"
	TAG = "deepseek/deepseek-r1:free"
	ROLE = "user"

	API_KEY = API_KEYS["DEEPSEEK_R1"]

	# In seconds
	TIMEOUT = 90
	RETRIES = 10

	@staticmethod
	def check_response_status(response: Response) -> bool:
		json_response = response.json()
		try:
			json_response["error"]
			return False
		except KeyError:
			try:
				json_response["choices"]
				return True
			except KeyError:
				return False

	@staticmethod
	def get_message_from_response(response: Response):
		json_response = response.json()
		pprint.pprint(json_response)
		return json_response["choices"][0]["message"]["content"]
