#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import sys

sys.path.append("./")

from cml_layman_brothers.src.main.utils import logger

logger = logger.setup_custom_logger("root")

import shutil
import os

logger.info("[DATA-CLEANUP]- Start data folder deletion")


if os.path.exists("cml_layman_brothers/data/"):
    logger.info("[DATA-CLEANUP]- Data folder exists")
    shutil.rmtree("cml_layman_brothers/data/")
else:
    logger.info("[DATA-CLEANUP]- Data folder does not exists. Skip.")

logger.info("[DATA-CLEANUP]- Data folder deletion finished")
