from __future__ import print_function
import sys
import json
import urllib.request as urllib2



if __name__=='__main__':
	url = ('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(sys.argv[1], sys.argv[2]))
	request = urllib2.urlopen(url)
	jsondata = json.loads(request.read())
	jsondata1 = (jsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
	Buslinenumber = sys.argv[2]
	print ('Bus name : %s' % (Buslinenumber))
	buscoordinate = []
	for i in jsondata1:
		buscoordinate.append(i['MonitoredVehicleJourney']['VehicleLocation'])
	BusNumber = len(buscoordinate)
	print ('Number of Active Buses : %i' % BusNumber)
	for j in range(BusNumber):
		print ('Bus %d is at latitude %f and longitude %f' % (j, buscoordinate[j]['Latitude'], buscoordinate[j]['Longitude']))

