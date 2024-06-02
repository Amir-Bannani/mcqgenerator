import os
import logging
from datetime import datetime


LOG_FILE = f'{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}.log'

LOG_path = os.path.join(os.getcwd(), "logs")

os.makedirs(LOG_path, exist_ok=True)
LOG_FILEPATH = os.path.join(LOG_path, LOG_FILE)


logging.basicConfig(level=logging.INFO,
        filename=LOG_FILEPATH,
        format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
)
