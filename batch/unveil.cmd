@echo off
setlocal enabledelayedexpansion

set /a cnt=1
set /a max=1

echo ����������ʾ���б����ص��ļ����ļ���.
echo=
echo ��Ѹ��ļ������ƶ�Ӳ�̸�Ŀ¼���ٲ���,
echo ������ڸ�Ŀ¼�£��������������������ر�...
pause>nul

cls
dir /b /a:d > log.dat

for /f %%i in (log.dat) do (
set /a cnt=!cnt!+1
)
set /a max=%cnt%
set /a cnt=1

for /f %%i in (log.dat) do (
cls
echo ��ǰ������ȣ� !cnt!/!max!
echo ��ǰ�����ļ��У�%%i
echo=
echo=
echo �����У����Ե�...
attrib /d /s -a -r -s -h %%i
set /a cnt=!cnt!+1
)
del log.dat

cls
echo ������ɣ�������˳�...
pause>nul