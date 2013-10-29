import json
import urllib

def getLocationInfo(ipAddr):
    if ipAddr is not None:
        try:
            locationString = urllib.urlopen("http://api.hostip.info/get_json.php?ip=%s&position=true" % ipAddr).read()
            return json.loads(locationString)
        except:
            pass

    return 'Unknown Location'
