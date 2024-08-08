import logging
from typing import Dict, Any

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)

logger = logging.getLogger(__name__)

def log_exception(exception: Exception, message: str):
    logger.error(f"{message}: {exception}")