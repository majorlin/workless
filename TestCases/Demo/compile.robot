*** Settings ***
Library           OperatingSystem
Library           WorkLessLibrary
Library           BuiltIn

*** Variables ***
${SDK_PATH}       %{MSDK_PATH}
${DEMOS}          ${SDK_PATH}/demos/YTM32B1ME0
${UART_PORT}      /dev/ttyUSB0

*** Test Cases ***
TestHelloWorld
    [Documentation]     Run hello world demo
    [Tags]    demo
    Compile Module      ${DEMOS}/hello_world    Hello world!

TestWDG
    [Documentation]     Run WDG demo
    [Tags]    demo
    Compile Module      ${DEMOS}/wdg        Watch dog reset happens

*** Keywords ***
Compile Module
    [Arguments]     ${module}           ${echo}
                    Uart Open           ${UART_PORT}    baudrate=115200
    ${result}       Compile GCC         ${module}
    Should Be Equal As Integers         ${result}       0
    ${result}       Download Firmware   ${module}/GCC/FLASH/flash.srec
    Should Be Equal As Integers         ${result}       0
    BuiltIn.Sleep   1s
    ${read}         UART READ
    Should Contain  ${read}             ${echo}

