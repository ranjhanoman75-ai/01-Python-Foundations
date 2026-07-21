print("===========Logging Info=================")
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("Debug")
logging.info("Info")
logging.error("Error")
logging.warning("warning")
logging.critical("critical error")

print("=======Logging save to file=========")
import logging 
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG
)
logging.info("Application started")
logging.warning("Low memory")
logging.error("Database connection failed")