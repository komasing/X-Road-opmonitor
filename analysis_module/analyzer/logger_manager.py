""" Logger Manager - Analyzer Module
"""

import logging
import json
import time
import os


def get_timestamp():
    return int(time.time())


def get_local_timestamp():
    return time.strftime('%Y-%m-%d %H:%M:%S %z', time.localtime())


class LoggerManager:

    __version__ = 'v0.9'

    def __init__(self, logger_name, module_name):
        self.logger_name = logger_name
        self.module_name = module_name

    def log_info(self, activity, msg):
        logger = logging.getLogger(self.logger_name)
        # Build Message
        data = dict()
        data['level'] = 'INFO'
        data['timestamp'] = get_timestamp()
        data['local_timestamp'] = get_local_timestamp()
        data['module'] = self.module_name
        data['activity'] = activity
        data['msg'] = msg
        data['version'] = self.__version__
        # Log to file
        logger.info(json.dumps(data))

    def log_warning(self, activity, msg):
        logger = logging.getLogger(self.logger_name)
        # Build Message
        data = dict()
        data['level'] = 'WARNING'
        data['timestamp'] = get_timestamp()
        data['local_timestamp'] = get_local_timestamp()
        data['module'] = self.module_name
        data['activity'] = activity
        data['msg'] = msg
        data['version'] = self.__version__
        # Log to file
        logger.warning(json.dumps(data))

    def log_error(self, activity, msg):
        logger = logging.getLogger(self.logger_name)
        # Build Message
        data = dict()
        data['level'] = 'ERROR'
        data['timestamp'] = get_timestamp()
        data['local_timestamp'] = get_local_timestamp()
        data['module'] = self.module_name
        data['activity'] = activity
        data['msg'] = msg
        data['version'] = self.__version__
        # Log to file
        logger.error(json.dumps(data))

    def log_heartbeat(self, msg, heartbeat_path, heartbeat_file, status=None):
        # Build Message
        data = dict()
        data['timestamp'] = get_timestamp()
        data['local_timestamp'] = get_local_timestamp()
        data['module'] = self.module_name
        data['msg'] = msg
        data['version'] = self.__version__
        data['status'] = status
        # Log to file
        if not os.path.isdir(heartbeat_path):
            os.makedirs(heartbeat_path)
        with open(os.path.join(heartbeat_path, heartbeat_file), 'w') as out_file:
            json.dump(data, out_file)
