# Python script to create M3U8 file from excell (xlsx)
print('Python script to create M3U8 file from excell (xlsx)')

'''
PyInstaller Quickstart
Install PyInstaller from PyPI:
pip install pyinstaller
Go to your program’s directory and run:
pyinstaller yourprogram.py
This will generate the bundle in a subdirectory called dist.
'''
# Install openpyxl package
import os
os.system('pip install openpyxl')

# Written by dexter 20090826
import os

# Check current working directory.
current_python_working_directory = os.getcwd()
print("Current python working directory" + str(current_python_working_directory))

# Create a folder for the input excell file
os.chdir("../")
current_working_directory = os.getcwd()
print("Current working directory: " + str(current_working_directory))

input_directory_name = "Input"
if not os.path.exists(str(input_directory_name)):
    os.makedirs(input_directory_name)

os.chdir(str(input_directory_name))
# Check input directory path:
input_directory_path = os.getcwd()
print("Current input directory path: " + str(input_directory_path))

# Create a folder for the M3U and JSON files
os.chdir("../")
output_directory = "Output"

if not os.path.exists(str(output_directory)):
    os.makedirs(output_directory)

output_directory_name = "Output"
os.chdir(str(output_directory_name))

# Check input directory path:
output_directory_path = os.getcwd()
print("Current output directory path: " + str(output_directory_path))





import datetime

current_dateandtime = datetime.datetime.now()
print('Current day and time: ' + str(current_dateandtime))

import codecs
# UTF8

# Import openpyxl
# Openpyxl homepage: http://openpyxl.readthedocs.org/
# Documentation https://openpyxl.readthedocs.io/en/stable/
# Command to install openpyxl: pip install openpyxl
import openpyxl

# Give the location of the file
current_excel_filename = 'Webradio.xlsx'
print('Current excel file name: ' + current_excel_filename)
os.chdir(str(input_directory_path))


# To open the workbook
# workbook object is created
workbook = openpyxl.load_workbook(current_excel_filename)

# Get workbook active current_sheet object
# from the active attribute
current_sheet = workbook.active

# Cell object is created by using
# current_sheet object's cell() method.

current_raw = 2
m3u_file_extension = '.m3u'
m3u_output_folder = 'Output\\'
m3u_extinf_content = 'EXTINF:0,'
current_json_file = 'Webradio.txt'
current_json_filename = m3u_output_folder + current_json_file

last_raw = 119

'''
Read the excel file and create M3U files
'''
import codecs
import os





print('Last raw in the excell file: ' + str(last_raw))

os.chdir(str(output_directory_path))

while True:
    webradio_name = current_sheet.cell(row=current_raw, column=1)
    webradio_stream = current_sheet.cell(row=current_raw, column=2)
    # Print value of cell object
    # using the value attribute

    current_m3u_extinf = str(m3u_extinf_content) + str(webradio_name.value) + str('\n')
    current_m3u_stream = str(webradio_stream.value)
    current_m3u_filename = str(webradio_name.value) + str(m3u_file_extension)

    # print(current_m3u_extinf)
    # print(current_m3u_stream)
    # print(current_m3u_filename)
    # Open the file

    m3u_file = codecs.open(str(current_m3u_filename), "w", "utf-8")
    m3u_file.write(u'\ufeff')
    m3u_file.write("#EXTM3U\n")
    m3u_file.write(current_m3u_extinf)
    m3u_file.write(current_m3u_stream)
    m3u_file.write("\n")

    # Close the file
    m3u_file.close()

    # Increment the loop iterator then break at the end
    current_raw += 1
    if current_raw >= last_raw:
        break

'''
End of read the excel file and create M3U files
'''

'''
Read the excel file and create JSON filet to Ka-Radio
'''

import json
import codecs
import urllib.parse

# Set the iterator to 2 because the first row does not contain any data
current_raw = 2

# Open the json file as UTF-8
json_file = codecs.open("Webradio.txt", "w", "utf-8")
json_file.write(u'\ufeff')

while True:

    # Read the excell file
    current_json_name = current_sheet.cell(row=current_raw, column=1)
    current_json_stream = current_sheet.cell(row=current_raw, column=2)
    current_json_volume = current_sheet.cell(row=current_raw, column=3)

    # print the actual row
    print('excel line: ' + str(current_raw) + '\n')

    # print the actual radio station name
    print('radio station name: ' + str(current_json_name.value) + '\n')

    # print the actual url
    print('url: ' + str(current_json_stream.value) + '\n')

    # parse the actual url then print its parts
    from urllib.parse import urlparse

    current_url = urlparse(str(current_json_stream.value))
    print('scheme: ' + str(current_url.scheme) + '\n')
    print('hostname: ' + str(current_url.hostname) + '\n')
    print('path: ' + str(current_url.path) + '\n')

    # if no port found then set 80
    parsed_port = str(current_url.port)
    substring = "None"
    if substring in parsed_port:
        parsed_port = '80'

    # Print the port
    print("port: " + str(parsed_port) + "\n")

    # give values to python string
    current_python_string = {
        "Name": current_json_name.value,
        "URL": str(current_url.hostname),
        "File": str(current_url.path),
        "Port": parsed_port,
        "ovol": str(current_json_volume.value)
    }

    # Print the python string
    print("python string: " + str(current_python_string) + "\n")

    # Convert python string into JSON string with separators , and :
    current_json_string = json.dumps(current_python_string, ensure_ascii=False, separators=(","":"))

    # Print the JSON string
    print("JSON string: " + str(current_json_string) + "\n")

    # Write the JSON string into file
    json_file.write(str(current_json_string) + '\n')

    # Increment the loop iterator then break at the end
    current_raw += 1
    if current_raw >= last_raw:
        break

# Close the json file
json_file.close()

'''
End of read the excel file and create JSON filet to Ka-Radio
'''
import time
time.sleep(1)  # pause for 1 seconds



























