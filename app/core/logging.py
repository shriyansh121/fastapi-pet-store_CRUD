import logging
import os

def setup_logger():
    logger = logging.getLogger("app")
    logger.setLevel(logging.DEBUG)

    # Prevent duplicate handlers
    if logger.handlers:
        return logger

    # -------- Console Handler --------
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    console_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    console_handler.setFormatter(console_formatter)

    # -------- File Handler --------
    os.makedirs("logs", exist_ok=True)

    file_handler = logging.FileHandler("logs/app.log")
    file_handler.setLevel(logging.DEBUG)

    file_formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )
    file_handler.setFormatter(file_formatter)

    # -------- Add Handlers --------
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
