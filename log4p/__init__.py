#!/usr/bin/env python3
# -*- coding: utf-8 -*-  
"""
 @Author: 郝天飞/Talen Hao (talenhao@gmail.com)
 @Site: talenhao.github.io
 @Since: 2017/12/13 11:58 AM 
"""


import logging
import logging.config
import json
import os


current_path = os.path.dirname(__file__)
config = current_path + "/log4p.json"


class GetLogger:
    def __init__(self, logger_name, logging_level="debug", config_file=config):
        self.logger_name = logger_name
        self.logging_level = logging_level
        self.config = config_file

    def get_l(self):
        # Create a logger
        agent_logger = logging.getLogger(self.logger_name)
        agent_logger.setLevel(self.logging_level)
        with open(self.config, 'r') as logging_configuration_file:
            config_dict = json.load(logging_configuration_file)
            logging.config.dictConfig(config_dict)
        return agent_logger
