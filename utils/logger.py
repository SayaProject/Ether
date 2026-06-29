import logging
import os
from config.config import Config

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "ether.log")


def setup_logger() -> None:
    os.makedirs(LOG_DIR, exist_ok=True)
    
    log_level = logging.DEBUG if Config.DEBUG else logging.INFO
    
    # Root logger configuration
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(LOG_FILE, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )
    
    # Reduce noise from libraries
    logging.getLogger("telethon").setLevel(logging.WARNING)
    logging.getLogger("aiogram").setLevel(logging.WARNING)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the given name."""
    return logging.getLogger(name)