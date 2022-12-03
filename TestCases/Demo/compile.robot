*** Settings ***
Library           OperatingSystem
Library           WorkLessLibrary

*** Variables ***
${SDK_PATH}       %{MSDK_PATH}
${DEMOS}          ${SDK_PATH}/demos/YTM32B1ME0

*** Test Cases ***
TestHelloWorld
    [Documentation]    Run hello world demo
    [Tags]    demo
    Compile Module    ${DEMOS}/hello_world

TestWDG
    [Documentation]    Run WDG demo
    [Tags]    demo
    Compile Module    ${DEMOS}/wdg

*** Keywords ***
Compile Module
    [Arguments]     ${module}
    ${result}       Compile GCC    ${module}
    Should Be Equal As Integers     ${result}       0

