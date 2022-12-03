#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Copyright (c) 2022 YTMicro
# ******************************************************************************
# File: JLinkLibrary.py
# Created Date: Saturday, December 3rd 2022, 9:09:12 am
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
class JLinkLibrary:
    def __init__(self, sn=None, por=False, device="YTM32B1ME0"):
        self.por = por
        self.sn = sn
        self.device = device
        pass

    def download_srec(self, srec_file):
        # create temp file
        script_file = "temp.jlink"
        with open(script_file, "w") as f:
            if self.por:
                f.write("power on\n")
            f.write("loadfile {}\n".format(srec_file))
            if self.por:
                f.write("power off\n")
                f.write("sleep 500\n")
                f.write("power on\n")
            else:
                f.write("r\n")
                f.write("g\n")
            f.write("qc\n")
        # run script
        cmd = "JLinkExe -device {} -if swd -speed 4000 -autoconnect 1 -CommanderScript {}".format(self.device, script_file)
        if self.sn:
            cmd += " -SelectEmuBySN {}".format(self.sn)
        os.system(cmd)

    def read_memory(self, addr, size):
        # create temp file
        script_file = "temp.jlink"
        with open(script_file, "w") as f:
            f.write("r\n")
            f.write("mem32 0x{:08X} 0x{:08X}\n".format(addr, size))
            f.write("qc\n")
        # run script
        cmd = "JLinkExe -device {} -if swd -speed 4000 -autoconnect 1 -CommanderScript {}".format(self.device, script_file)
        if self.sn:
            cmd += " -SelectEmuBySN {}".format(self.sn)
        os.system(cmd)

    def get_library(self):
        return "JLinkLibrary"

    def get_version(self):
        return "1.0.0"

    def get_author(self):
        return "Major Lin"
