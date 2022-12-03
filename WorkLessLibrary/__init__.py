#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Copyright (c) 2022 YTMicro
# ******************************************************************************
# File: __init__.py
# Created Date: Saturday, December 3rd 2022, 10:34:53 am
# Author: Major Lin
# -----
# Last Modified: Sat Dec 03 2022
# Modified By: Major Lin
# -----
# 
# -----
# HISTORY:
# Date      	By           	Comments
# ----------	-------------	----------------------------------------------------------
# ******************************************************************************
###
import os
import sys

from WorkLessLibrary.keywords import CompileKeywords, JLinkKeywords

__version___ = "0.2.0"


class WorkLessLibrary(CompileKeywords, JLinkKeywords):
    __version__ = __version___

    ROBOT_LIBRARY_SCOPE = "GLOBAL"