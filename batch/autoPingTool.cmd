@echo off

color 3e

setlocal enabledelayedexpansion

@echo off
if not defined flg set flg= && start /min "" %0& exit

set /a IP=1
::IP address
set /a cnt=1
::count the unable pinged numbers

echo 日付：%date%>>IPlog.txt
echo 時刻：%time%>>IPlog.txt
echo=>>IPlog.txt

:loop
ping -n 1 10.194.152.%IP%|findstr "out"&&(
echo No%cnt%→10.194.152.%IP%>>IPlog.txt
set /a cnt=!cnt!+1
)
set /a IP=%IP%+1
if %IP% LEQ 126 goto loop
set /a cnt=%cnt%-1
echo=>>IPlog.txt
echo %cnt%台pingできない>>IPlog.txt
echo 時刻:%time%>>IPlog.txt
echo=-------------------------------------->>IPlog.txt
echo=-------------------------------------->>IPlog.txt
echo=>>IPlog.txt
echo=>>IPlog.txt
IPlog.txt
exit