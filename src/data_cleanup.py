#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import shutil
import os
from src.logger import logger


logger.info("[DATA-CLEANUP]- Start data folder deletion")

if __name__ == "__main__":
    if os.path.exists("data/"):
        logger.info("[DATA-CLEANUP]- Data folder exists")
        shutil.rmtree("data/")
    else:
        logger.info("[DATA-CLEANUP]- Data folder does not exists. Skip.")

logger.info("[DATA-CLEANUP]- Data folder deletion finished")
