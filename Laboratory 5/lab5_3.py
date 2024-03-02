import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger(__name__)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

debug_handler = logging.StreamHandler(sys.stdout)
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)

info_handler = logging.StreamHandler(sys.stdout)
info_handler.setLevel(logging.INFO)
info_handler.setFormatter(formatter)

warning_handler = logging.StreamHandler(sys.stdout)
warning_handler.setLevel(logging.WARNING)
warning_handler.setFormatter(formatter)

error_handler = logging.StreamHandler(sys.stderr)
error_handler.setLevel(logging.ERROR)
error_handler.setFormatter(formatter)

critical_handler = logging.StreamHandler(sys.stderr)
critical_handler.setLevel(logging.CRITICAL)
critical_handler.setFormatter(formatter)


def show_line(line):
    logger.addHandler(debug_handler)
    logger.addHandler(info_handler)
    logger.addHandler(warning_handler)
    logger.addHandler(error_handler)
    logger.addHandler(critical_handler)


    regex_pattern_info = r'Accepted|Connection closed|Disconnecting'
    regex_pattern_warning = r'Failed password|Unknown user'
    regex_pattern_error = r'error: \w+'
    regex_pattern_critical = r'POSSIBLE BREAK-IN ATTEMPT'


    logger.debug("Size: " + str(len(line.encode('utf-8'))))
    if re.search(regex_pattern_info, line):
        logger.info(line)
    elif re.search(regex_pattern_warning, line):
        logger.warning(line)
    elif re.search(regex_pattern_error, line):
        logger.error(line)
    elif re.search(regex_pattern_critical, line):
        logger.critical(line)
