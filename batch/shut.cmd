@echo off
title Lane at NEU
COLOR 3E

set t=1
for /f "tokens=3" %%i in ('reg query "HKCU\Control Panel\International" /v "sLanguage"') do (
    set reg_localevar=%%i
)

if %reg_localevar% == CHS goto Chinese
goto English

:Chinese
echo -------------------------------------------------------------------------------
echo ��Ϊ����������Ͼ֮�������Զ��ػ�����,���Է�������һЩ�¡�
echo �������ϷŸ�30���Ӱ�������Ȼ���Զ��ػ�֮��ġ�^^_^^�Ǻǡ�
echo -------------------------------------------------------------------------------
echo �������߳��νӴ������ղ����߳���������Щbug�������½⣡
echo ע�⣺�����������֣�1~315360000����������ĸ��Ч��������0~~
echo -------------------------------------------------------------------------------
echo �������� 0 ����ȡ����ǰ�ػ��ƻ����˳�����(û�мƻ���ֱ���˳�)
echo -------------------------------------------------------------------------------
set /p time=������ػ�����ʱʱ�䣨��λ��min)��
set /a s=time*60
if "%s%"=="0" (shutdown -a&cls&echo.&echo ȡ���ɹ���ллʹ�ã�&&echo.&goto end1)
shutdown -a
ping -n 2 127.1>nul
shutdown -s -t "%s%"
echo -------------------------------------------------------------------------------
echo ���ļ��������%time%���Ӻ�ر�...
echo -------------------------------------------------------------------------------
cls
echo -------------------------------------------------------------------------------
echo ��Ҫ��ʱȡ���Զ��ػ�������0��Ȼ��س����رճ�����ֱ�Ӱ��س�����
echo (����رպ󵹼�ʱ��������������...)
echo -------------------------------------------------------------------------------
echo.
set /p t=
echo.
cls
if "%t%"=="0" (shutdown -a && echo. && echo ȡ���ɹ�,ллʹ�ã�)
goto end1

:English
echo -------------------------------------------------------------------------------
echo This app was created in author's leisure time, could make something easier.
echo For example after 30 minutes music then shut down your PC, ^^_^^.
echo -------------------------------------------------------------------------------
echo It is the first time author writes a batch file, there may be several bugs.
echo Note: should input numbers (1~315360000). Charecters input means 0 ~~
echo -------------------------------------------------------------------------------
echo Input number 0 can cancel the current shut down plan.
echo -------------------------------------------------------------------------------
set /p time=Input time (Unit: min):
set /a s=time*60
if "%s%"=="0" (shutdown -a&cls&echo.&echo Cancelled successfully, thank you!&&echo.&goto end1)
shutdown -a
ping -n 2 127.1 > nul
shutdown -s -t "%s%"
echo -------------------------------------------------------------------------------
echo Your PC will be shouted down in %time% mins...
echo -------------------------------------------------------------------------------
cls
echo -------------------------------------------------------------------------------
echo If you want to cancel, please input 0, otherwise input Enter instead!
echo (Shut down countdown will continue after close...)
echo -------------------------------------------------------------------------------
echo.
set /p t=
echo.
cls
if "%t%"=="0" (shutdown -a && echo. && echo Cancelled successfully, thank you!)


:end1
echo -------------------------------------------------------------------------------
echo.
echo                                                     Powered by Lane at NEU
echo.
echo -------------------------------------------------------------------------------
if "%t%"=="1" goto end2
if not "%t%"=="0" echo Thank you!!
:end2
echo Press any key to quit...
echo.
pause>nul