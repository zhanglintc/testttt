@ECHO OFF&TITLE ��ͼ�����ű�v1.1 CodeBy:Sylthas
MODE con COLS=55 LINES=25
color 0A
:loop
cls
echo.��ͼ�����ű� For ������http://fuliba.net CodeBy:Sylthas 
echo.
echo.Hi! %username%! Now is %date% %time%
echo.��ӭʹ�ò�ͼ�����ű�,���ű����Խ�rar�ļ����ص�ͼƬ��.
echo.
echo.��������ͼ���ļ���س���
set /p imagefile=
echo.��������rar�ļ���س���
set /p rarfile=
echo.
copy /b %imagefile% + %rarfile% %rarfile%_new.jpg
echo.
if errorlevel 1 goto errorinfo
echo.��ͼ%rarfile%_new.jpg�Ѿ�����
echo.ʹ��ʱ�뽫%rarfile%_new.jpg����Ϊxx.rar���ɴ�
echo.
goto choice
:errorinfo
echo.��������,��ͼ����ʧ��.
echo.
:choice
set /p key=�Ƿ������Q���˳�:
if /i "%key%" =="q" goto quit
goto loop
:quit
exit