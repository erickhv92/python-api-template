import json
import logging
import sys
from datetime import datetime

from application.params import get_settings


settings = get_settings()


class JsonFormatter(logging.Formatter):
    """JSON formatter for structured logging."""
    
    def format(self, record):
        log_record = {
            "timestamp": datetime.utcnow().isoformat(),
            "level": record.levelname,
            "message": record.getMessage(),
            "module": record.module,
            "function": record.funcName,
            "line": record.lineno,
            "environment": settings.environment,
        }
        
        if hasattr(record, "props"):
            log_record.update(record.props)
            
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
            
        return json.dumps(log_record)


def setup_logging(name: str = None) -> logging.Logger:
    """Set up and return a logger instance."""
    logger = logging.getLogger(name or __name__)
    
    # Only configure if not already configured
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        
        if settings.environment == "production":
            handler.setFormatter(JsonFormatter())
        else:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
        
        logger.addHandler(handler)
        
        # Set log level based on environment
        if settings.environment == "development":
            logger.setLevel(logging.DEBUG)
        else:
            logger.setLevel(logging.INFO)
        
    return logger