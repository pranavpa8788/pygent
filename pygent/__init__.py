import json
import logging

import colorlog

print("Initializing logger")

NAME = "pygent"
logger = logging.getLogger(NAME)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

log_format = "%(asctime)s - %(filename)s %(log_color)s%(levelname)s%(reset)s - %(message)s"
date_format = "%Y-%m-%d %H:%M:%S"

formatter = colorlog.ColoredFormatter(
	log_format,
	datefmt=date_format,
	log_colors={
		"DEBUG": "cyan",
		"INFO": "blue",
		"WARNING": "yellow",
		"ERROR": "red",
		"CRITICAL": "red,bg_white"
	}
)

handler.setFormatter(formatter)
logger.addHandler(handler)

with open("secrets.json", "r") as secrets_file:
	API_KEYS = json.load(secrets_file)["API_KEYS"]