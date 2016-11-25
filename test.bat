chcp 1251

REM without parameters
triangle.exe
@IF ERRORLEVEL 0 GOTO err
echo ERRORLEVEL

REM incorrect parameters count
triangle.exe 1231234 123 12312312345 18
@IF ERRORLEVEL 0 GOTO err

REM parameters is not numbers
triangle.exe 12 1231a2312345 18
@IF ERRORLEVEL 0 GOTO err

REM negative parameters
triangle.exe -12 12312312345 18
@IF ERRORLEVEL 0 GOTO err

REM correct replacing 1231234 in 12312312345
lab1.exe test/input.txt test/output1231234-paul.txt 1231234 paul
@IF NOT ERRORLEVEL 0 GOTO err
@FC /B test\output1231234-paul.txt test\1231234-paul.txt
@IF ERRORLEVEL 1 GOTO err



ECHO Program testing succeeded :-)
@PAUSE
EXIT

:err
ECHO Program testing failed :-(
@PAUSE
EXIT
