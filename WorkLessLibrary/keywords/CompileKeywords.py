#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Copyright (c) 2022 YTMicro
# ******************************************************************************
# File: CompileLibrary.py
# Created Date: Saturday, December 3rd 2022, 10:17:37 am
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
from WorkLessLibrary.WorkLessUtil import run_cmd
from robot.api.deco import keyword

class CompileKeywords(object):
    def __init__(self):
        pass
    
    @keyword("Compile GCC")
    def compile_gcc(self, project_path, make_args=""):
        # generate makefile
        cmd = "progen.py proj.yaml -t GCC -p GCC"
        run_cmd(cmd, path=project_path)
        # compile
        cmd = "make clean"
        run_cmd(cmd, path=project_path + "/GCC")
        cmd = "make {}".format(make_args)
        return run_cmd(cmd, path=project_path + "/GCC")
