@echo off
Title Linn ��·��ѡ����
Color 3E
echo -------------------------------------------------------------------------------
echo     �˹��߿��԰�����ѡ������ʱ��·�ɣ���������ͨ����Ҳ������У԰����������
echo     ����һ����������Ȼ���Լ�������ߡ���ʣ�µľ��Ǳ����ߵ��¶��ˡ�
echo.
echo				@ ����1��ʹ��������ͨ������~~
echo				@ ����2��ʹ������У԰������~~
echo				@ ����3��ʹ��˫����ͬʱ����~~
echo				@ ����4���鿴��ǰ��ipv4·�����~~
echo -------------------------------------------------------------------------------
set /p ch=���������ѡ��:
set /a choice=ch
if "%choice%"=="1" (goto ch1)
if "%choice%"=="2" (goto ch2)
if "%choice%"=="3" (goto ch3)
if "%choice%"=="4" (goto ch4)
if "%choice%"=="0" (echo did nothing && goto end)
goto end

:ch1
route delete 0.0.0.0 mask 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 192.168.1.1 metric 1
route add 0.0.0.0 mask 0.0.0.0 192.168.1.253 metric 2
route delete 202.118.0.0 mask 255.255.0.0 58.154.234.254
route delete 219.216.0.0 mask 255.255.0.0 58.154.234.254
route delete 202.199.0.0 mask 255.255.0.0 58.154.234.254
route delete 58.154.0.0 mask 255.255.0.0 58.154.234.254
route delete 118.202.0.0 mask 255.255.0.0 58.154.234.254
cls
goto end

:ch2
route delete 0.0.0.0 mask 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 58.154.234.254 metric 1
route delete 202.118.0.0 mask 255.255.0.0 58.154.234.254
route delete 219.216.0.0 mask 255.255.0.0 58.154.234.254
route delete 202.199.0.0 mask 255.255.0.0 58.154.234.254
route delete 58.154.0.0 mask 255.255.0.0 58.154.234.254
route delete 118.202.0.0 mask 255.255.0.0 58.154.234.254
cls
goto end

:ch3
route delete 0.0.0.0 mask 0.0.0.0
route add 0.0.0.0 mask 0.0.0.0 192.168.1.1 metric 1
route add 0.0.0.0 mask 0.0.0.0 192.168.1.253 metric 2
route add 0.0.0.0 mask 0.0.0.0 58.154.234.254 metric 100
route add 202.118.0.0 mask 255.255.0.0 58.154.234.254
route add 219.216.0.0 mask 255.255.0.0 58.154.234.254
route add 202.199.0.0 mask 255.255.0.0 58.154.234.254
route add 58.154.0.0 mask 255.255.0.0 58.154.234.254
route add 118.202.0.0 mask 255.255.0.0 58.154.234.254
cls
goto end

:ch4
cls
route print -4
pause
exit

:end
echo -------------------------------------------------------------------------------
echo.
echo    �����ɹ�������
echo.
echo                                                     Powered by Linn at NEU
echo.
echo -------------------------------------------------------------------------------
echo �밴������˳�����...
echo.
pause>nul
