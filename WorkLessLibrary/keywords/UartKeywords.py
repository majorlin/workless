#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# Copyright (c) 2022 YTMicro
# ******************************************************************************
# File: UartKeywords.py
# Created Date: Saturday, December 3rd 2022, 8:02:53 pm
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

import serial

class UartKeywords(object):
    def __init__(self):
        self.uart = None

    def uart_open(self, port, baudrate=115200, timeout=0.1):
        self.uart = serial.Serial(port, baudrate, timeout=timeout)

    def uart_close(self):
        self.uart.close()

    def uart_write(self, data):
        self.uart.write(data)

    def uart_read(self):
        # read all data in buffer
        return self.uart.read_all()