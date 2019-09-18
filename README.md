# Webradio-Stations-Tool

The tool is capable to read an excel file that stores the list of radio stations and generates a JSON file that can be uploaded to the webradio via web interface.

See an ESP8266 based webradio project at GitHub.
Link to the project: https://github.com/karawin/Ka-Radio

Description:

Collect the stations related information into an excel file. The first column shall contain the name of the station to have a friendly name of your favourite channe. The second is the location of the webstream, the tool has an internal parser to figure out the server, port, and file location, therefore you do not need to care about it, just insert the stream. The third column to store the volume settings, you can insert zero if no additional volume settings required. Save the list of stations to an excel file named Webradio.xlsx.

Run the tool and it generates an output folder with the JSON file and additional M3U files that can be played by your computer.


Plans for the future:
- Add GUI
- Check the last filled row in the excell
- Multi platfom
