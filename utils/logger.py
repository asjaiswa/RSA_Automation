import logging
import os


def get_logger(name: str = __name__, log_level=logging.INFO, report_dir: str = None):
    """Return a logger instance with console and file handler"""

    logger = logging.getLogger(name)
    logger.setLevel(log_level)

    if not logger.handlers:
        if report_dir is None:
            report_dir = "Reports"
        os.makedirs(report_dir, exist_ok=True)
        log_file = os.path.join(report_dir, "test.log")  # store directly in report_dir

        # File handler
        fh = logging.FileHandler(log_file)
        fh.setLevel(log_level)

        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(log_level)

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # Add handlers
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
