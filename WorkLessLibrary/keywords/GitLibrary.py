#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Copyright (c) 2022 YTMicro
# ******************************************************************************
# File: GitLibrary.py
# Created Date: Saturday, December 3rd 2022, 10:13:43 am
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
class GitLibrary(object, repo=None):
    def __init__(self):
        self.repo = repo
        os.chdir(self.repo)

    def git_checkout(self, branch):
        # checkout and update branch
        cmd = "git checkout {}".format(branch)
        os.system(cmd)
        cmd = "git pull"
        os.system(cmd)
