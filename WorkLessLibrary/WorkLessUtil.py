#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Copyright (c) 2022 YTMicro
# ******************************************************************************
# File: WorkLessUtil.py
# Created Date: Saturday, December 3rd 2022, 10:20:34 am
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

import sys
import time
import subprocess

def run_cmd(cmd, path=".", dry_run=False, timeout=60):
    # run command under given path
    print("Run command: {} under {}".format(cmd, path))
    if dry_run:
        return 0
    result = subprocess.run(cmd, cwd=path, shell=True, timeout=timeout, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    # show result
    print(result.stdout.decode("utf-8"))
    print(result.stderr.decode("utf-8"))
    return result.returncode