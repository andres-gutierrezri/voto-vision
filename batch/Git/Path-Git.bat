@echo off
setlocal
chcp 65001 > nul

echo ------------------------------------------
echo Script para Agregar Git al PATH de Windows
echo ------------------------------------------

REM Ingresar al Directorio del Proyecto
REM Regresar a la carpeta raíz del proyecto subiendo en los directorios

REM Definir el nombre del archivo marcador que existe en la raíz del proyecto
set "marker=.env"

REM Inicializar la variable para guardar la ruta raíz
set "root_dir="

REM Comenzar desde el directorio actual
set "current_dir=%cd%"

:search_root
REM Verificar si el archivo marcador existe en el directorio actual
if exist "%current_dir%\%marker%" (
    set "root_dir=%current_dir%"
    goto :found
)

REM Subir un nivel en el directorio
cd ..

REM Verificar si estamos en la raíz del sistema (no se puede subir más)
if "%cd%"=="%current_dir%" (
    goto :not_found
)

REM Actualizar current_dir y continuar la búsqueda
set "current_dir=%cd%"
goto :search_root

:found
echo Carpeta raiz encontrada en: %root_dir%
cd /d "%root_dir%"
goto :end

:not_found
echo No se pudo encontrar la carpeta raiz del proyecto.
goto :end

:end

REM Leer variables del archivo .env
REM Establecer la ruta al archivo .env
set ENV_FILE=.env

REM Activar expansión retardada de variables
setlocal enabledelayedexpansion

REM Verificar si el archivo .env existe
if not exist %ENV_FILE% (
    echo El archivo %ENV_FILE% no existe.
    exit /b 1
)

REM Establecer la variable de entorno para el Path de MySQL
for /f "tokens=1,2 delims==" %%a in (%ENV_FILE%) do (
    if "%%a"=="GIT_PATH" (
        REM Guardar el valor de la variable
        set "GIT_PATH=%%b"

        REM Eliminar comillas dobles si existen
        set "GIT_PATH=!GIT_PATH:"=!"
        
        REM Eliminar comillas simples si existen
        set "GIT_PATH=!GIT_PATH:'=!"

        REM Asignar la variable sin comillas
        set %%a=!GIT_PATH!
    )
)

REM Verifica si la ruta ya está en el PATH

echo %PATH% | find /I "%GIT_PATH%" >nul
if %ERRORLEVEL%==0 (
    echo La ruta de Git ya esta en el PATH del sistema.
) else (
    REM Agregar la ruta al PATH
    setx /M PATH "%PATH%;%GIT_PATH%"
    echo La ruta de Git ha sido agregada al PATH del sistema.
)

echo.
echo PARA SALIR PRESIONA UNA TECLA.
endlocal
pause > nul
exit