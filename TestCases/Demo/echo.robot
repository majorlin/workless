#
#Copyright (c) 2022 YTMicro
#******************************************************************************
#File: echo.robot
#Created Date: Saturday, December 3rd 2022, 9:03:28 am
#Author: Major Lin
#-----
#Last Modified: 
#Modified By: 
#-----
#
#-----
#HISTORY:
#Date      	By           	Comments
#----------	-------------	----------------------------------------------------------
#******************************************************************************
#

*** Settings ***
Documentation     A test suite with a single test.


*** Variables ***
${TEST NAME}     echo

*** Test Cases ***
Hello World
    [Documentation]    A test case with a single keyword.
    Log    Hello World!