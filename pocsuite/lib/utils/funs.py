#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2014-2015 pocsuite developers (http://sebug.net)
See the file 'docs/COPYING' for copying permission
"""

from socket import gethostbyname
from urlparse import urlsplit
from lib.core.data import logger
from lib.core.enums import CUSTOM_LOGGING


def url2ip(url):
    """
    works like turning 'http://baidu.com' => '180.149.132.47'
    """
    iport = urlsplit(url)[1].split(':')
    if len(iport) > 1:
        return gethostbyname(iport[0]), iport[1]
    return gethostbyname(iport[0])


def warningLog(Msg):
    logger.log(CUSTOM_LOGGING.WARNING, Msg)
    pass


def infoLog(Msg):
    logger.log(CUSTOM_LOGGING.SYSINFO, Msg)
    pass


def sucLog(Msg):
    logger.log(CUSTOM_LOGGING.SUCCESS, Msg)
    pass


def errLog(Msg):
    logger.log(CUSTOM_LOGGING.ERROR, Msg)
    pass
