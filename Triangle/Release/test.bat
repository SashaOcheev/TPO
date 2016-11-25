@chcp 1251

REM without parameters
triangle.exe
@IF NOT ERRORLEVEL 1 GOTO err

REM incorrect parameters count
triangle.exe 2 2 2 2
@IF NOT ERRORLEVEL 1 GOTO err

REM parameters is not numbers 1
triangle.exe 12 1a5 18
@IF NOT ERRORLEVEL 2 GOTO err

REM parameters is not numbers 2
triangle.exe 12 1231.2312345. 18
@IF NOT ERRORLEVEL 2 GOTO err

REM parameters is not numbers 3
triangle.exe 12 .5 18
@IF NOT ERRORLEVEL 2 GOTO err

REM parameters is not numbers 4
triangle.exe 12 5. 18
@IF NOT ERRORLEVEL 2 GOTO err

REM zero parameters
triangle.exe 1 0 1
@IF NOT ERRORLEVEL 3 GOTO err

REM negative parameters
triangle.exe -12 15 18
@IF NOT ERRORLEVEL 3 GOTO err

REM not triangle
triangle.exe 7 2 3 >> output/1.txt
@IF NOT ERRORLEVEL 0 GOTO err
FC output/1.txt expected/1.txt
IF NOT ERRORLEVEL 0 GOTO err

REM not triangle where a + b == c
triangle.exe 1 2 3 >> output/2.txt
@IF NOT ERRORLEVEL 0 GOTO err
FC output/2.txt expected/2.txt
IF NOT ERRORLEVEL 0 GOTO err

REM not triangle with two equils
triangle.exe 3 6 3 >> output/3.txt
@IF NOT ERRORLEVEL 0 GOTO err
FC output/3.txt expected/3.txt
IF NOT ERRORLEVEL 0 GOTO err

REM ordinary
triangle.exe 3 4 5 >> output/4.txt
@IF NOT ERRORLEVEL 0 GOTO err
@IF NOT ERRORLEVEL 0 GOTO err
FC output/4.txt expected/4.txt
IF NOT ERRORLEVEL 0 GOTO err

REM equilateral
triangle.exe 10 10 10 >> output/5.txt
@IF NOT ERRORLEVEL 0 GOTO err
@IF NOT ERRORLEVEL 0 GOTO err
FC output/5.txt expected/5.txt
IF NOT ERRORLEVEL 0 GOTO err

REM isosceles 1
triangle.exe 3 3 5 >> output/6.txt
@IF NOT ERRORLEVEL 0 GOTO err
@IF NOT ERRORLEVEL 0 GOTO err
FC output/6.txt expected/6.txt
IF NOT ERRORLEVEL 0 GOTO err

REM isosceles 2
triangle.exe 3 5 3 >> output/7.txt
@IF NOT ERRORLEVEL 0 GOTO err
@IF NOT ERRORLEVEL 0 GOTO err
FC output/7.txt expected/7.txt
IF NOT ERRORLEVEL 0 GOTO err

REM isosceles 3
triangle.exe 5 3 3 >> output/8.txt
@IF NOT ERRORLEVEL 0 GOTO err
@IF NOT ERRORLEVEL 0 GOTO err
FC output/8.txt expected/8.txt
IF NOT ERRORLEVEL 0 GOTO err

REM float
triangle.exe 1.2 1.3 1.4 >> output/9.txt
@IF NOT ERRORLEVEL 0 GOTO err
@IF NOT ERRORLEVEL 0 GOTO err
FC output/9.txt expected/9.txt
IF NOT ERRORLEVEL 0 GOTO err


@ECHO Program testing succeeded :-)
@PAUSE
EXIT

:err
@ECHO Program testing failed :-(
@PAUSE
EXIT

