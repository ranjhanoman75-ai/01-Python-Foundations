from pathlib import Path
import logging

LOG_FILE = Path(__file__).parent / "app.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True          # <-- Important
)

logging.info("Application Started")
logging.error("Database Failed")

logging.shutdown()      # Flush logs to disk