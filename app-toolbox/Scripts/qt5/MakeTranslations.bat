:: -------------------------------------------------------------------
<<<<<<< HEAD:app-toolbox/Scripts/qt5/MakeTranslations.bat
:: Copyright (c) 2010-2017 Denis Machard
=======
:: Copyright (c) 2010-2018 Denis Machard
>>>>>>> 45df48b948e3efe1667629a2b66a7a857a6f5945:app-toolbox/Scripts/qt5/MakeTranslations.bat
:: This file is part of the extensive testing project
::
:: This library is free software; you can redistribute it and/or
:: modify it under the terms of the GNU Lesser General Public
:: License as published by the Free Software Foundation; either
:: version 2.1 of the License, or (at your option) any later version.
::
:: This library is distributed in the hope that it will be useful,
:: but WITHOUT ANY WARRANTY; without even the implied warranty of
:: MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
:: Lesser General Public License for more details.
::
:: You should have received a copy of the GNU Lesser General Public
:: License along with this library; if not, write to the Free Software
:: Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
:: MA 02110-1301 USA
:: -------------------------------------------------------------------

@echo off

set Project=%~dp0..\..\

set PythonVersion=36
set PythonPath=C:\Python%PythonVersion%\

:: convert xml translations files
REM C:\Qt\5.8\mingw53_32\bin\lrelease.exe "%Project%\Translations\us_US.ts"
REM C:\Qt\5.8\mingw53_32\bin\lrelease.exe "%Project%\Translations\fr_FR.ts"

:: build resources
echo Building translations resources...
%PythonPath%\python.exe -m PyQt5.pyrcc_main -o "%Project%\Translations\Translations.py" "%Project%\Translations\__resources.qrc"

pause