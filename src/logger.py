import logging 

logging.basicConfig(
    filename='app.log',
    level = logging.INFO,
    format = "%(asctime)s - %(levelname) - %(message)s"
)

def log_message(message):
    logging.info(message)

def log_message(error):
    logging.error(error)


