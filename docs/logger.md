
# CustomFormatter Class Documentation

## Overview
The `CustomFormatter` class in the provided script extends the `logging.Formatter` class to create a custom formatter for informative logging. This formatter adds color to log messages based on their severity level.

## Class Details

### Class CustomFormatter(logging.Formatter)
A custom logging formatter that adds color to log messages.

#### Attributes
- `grey`: Grey color code for DEBUG level messages.
- `violet`: Violet color code for INFO level messages.
- `yellow`: Yellow color code for WARNING level messages.
- `red`: Red color code for ERROR level messages.
- `bold_red`: Bold red color code for CRITICAL level messages.
- `reset`: Reset color code.
- `format`: String format for log messages.
- `FORMATS`: Dictionary mapping logging levels to their respective color formats.

#### Method `format(self, record)`
Formats the log record with color based on the severity level.

##### Parameters:
- `record`: The log record.

##### Returns:
- Formatted (colored) log message.

## Example Usage
The following example demonstrates how to use the `CustomFormatter` class:

```python
import logging
import os

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

logger.debug("debug message")
logger.info("Warning: Email has not been sent......")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
```

This example sets up a logger with the custom formatter and logs messages of various severity levels.
