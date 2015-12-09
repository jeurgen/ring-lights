#/usr/bin/python

import sys
import requests
import time
import array
import threading



# This path has to adjusted to suit your environment; see http://www.developers.meethue.com/documentation/getting-started
 
lightPath = "http://Philips-hue.fritz.box/api/md5-like-username-of-authorized-user/lights/" # base path without id

lightAction = lightPath + '/state'


# my hue light IDs:

# 1 table down
# 2 Kitchen Spot
# 3 Desk
# 4 Bloom
# 5 table up


# insert the light IDs you want to ring
myLights=['1','2','3','4','5']



#determine if a given lights is on
def light_is_on(lightId):
    # Code to determine if lights are on
    r = requests.get(lightPath+lightId)
    if r.json['state']['on'] == True:
#	print 'lights are on'
        return True

#    print 'lights are off'
    return False


def switch_on_off(lightId):
        payload = '{"on": true}'
        r = requests.put(lightPath+lightId+'/state', data=payload)
        time.sleep(0.5)

	payload = '{"on": false}'
        r = requests.put(lightPath+lightId+'/state', data=payload)


def switch_off_on(lightId):
        payload = '{"on": false}'
        r = requests.put(lightPath+lightId+'/state', data=payload)
	time.sleep(0.5)       
 
	payload = '{"on": true}'
        r = requests.put(lightPath+lightId+'/state', data=payload)



def lightRing(lightId):
		while True:
			if (light_is_on(lightId)):
				switch_off_on(lightId)
				switch_off_on(lightId)
				break
			else:
				switch_on_off(lightId)
				switch_on_off(lightId)
				break



threads=[]
while True:
    line = sys.stdin.readline()
    if not line: break # EOF

    if "Receiving new incoming call" in line:
	for lightId in myLights:
        	t = threading.Thread(target=lightRing,  args=(lightId,))
    		threads.append(t)
    		t.start()
		
		#lightRing(lightId)
