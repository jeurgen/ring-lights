# ring-lights
Make your Philips Hue lights notify you of incoming calls.

## Motivation
* Problem: Sleeping baby -> disabled ringtones -> incoming calls are missed
* Solution: Blink the Hue lights at incoming calls


## Preconditions
* PBX allows setup of additional VOIP Phone
* A server system running the new phone and the lights control script is available. This might be a raspberry pi or the PBX itself.
* linphonec is installed on the server system and configured for your PBX
* A Philips hue system including the hue bridge is available

*Tested in a scenario with AVM Fritz Box, Raspbian Linux on a Raspberry Pi and Philips Hue White Startet Set*


## Run
* Adjust the parameters in the Python Script. Path to your hue bridge, "key" and light-ids are required. 
* linphonec | python lightring.py
