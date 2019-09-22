@echo off

rem Install PyInstaller from PyPI:
pip install pyinstaller

rem Create an executable from the python file by pyinstaller:
pyinstaller --onefile "Python Radio Stations Tool.py"

rem Check the directory of the script:
set current_script_directory=%cd%
echo The current work directory of the script is: %current_script_directory%

rem Go one level up in the folder structure:
cd..

rem Check the directory of the tool:
set current_tool_directory=%cd%
echo The path of the tool is: %current_tool_directory%

rem Set the name of the windows executable folder:
set windows_executable_folder_name=\Windows Executable

rem Combine the path of the tool and the name of the windows executable:
set windows_executable_folder_path="%current_tool_directory%%windows_executable_folder_name%"

rem Print the path of the windows executable:
echo The path of the Windows Executable is: %windows_executable_folder_path%


rem Check if the windows executable folder exists:
if exist %windows_executable_folder_path% (
	rmdir /Q /S %windows_executable_folder_path% 
	mkdir %windows_executable_folder_path% 
	echo The path of the Windows Executable existed but repleaced with a new one
	) else (
	mkdir %windows_executable_folder_path%
	echo The path of the Windows Executable did not exist but created a new one
	)


rem Combine the path of the tool and the name of the windows executable:
set windows_executable_source_location="%current_script_directory%\dist\Python Radio Stations Tool.exe"

rem Copy the executable file to the upper level folder:
xcopy %windows_executable_source_location% %windows_executable_folder_path%

rem print message if the script successfully completed:
echo The executable file is succesfully copied to the "Windows Executable" folder

rem Wait for a key:
pause
