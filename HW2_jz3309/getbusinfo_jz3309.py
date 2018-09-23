
import sys
import json
import urllib.request as urllib2
import csv
#import urllib is not available in pyhton3.

if __name__=='__main__':
	url = ('http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1],sys.argv[2]))
	
	request = urllib2.urlopen(url)
	busjsondata = json.loads(request.read())
	busdata = busjsondata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
	with open(sys.argv[3], "w") as buscsvfile:
		filewriter = csv.writer(buscsvfile, delimiter = ',')
		filewriter.writerow(('Latitude','Longitude','StopName','StopStatus'))


		for i in range(len(busdata)):
			Latitude = busdata[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
			Longitude = busdata[i]["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]

			busdata2 = busdata[i]["MonitoredVehicleJourney"]["OnwardCalls"]["OnwardCall"]
			if busdata[i]['MonitoredVehicleJourney']['OnwardCalls'] != {}:
				for j in range(len(busdata2)):
					StopName = busdata2[j]["StopPointName"]
					StopStatus = busdata2[j]["Extensions"]["Distances"]["PresentableDistance"]
					filewriter.writerow((Latitude, Longitude, StopName, StopStatus))
				else:
					filewriter.writerow((Latitude, Longitude, "N/A", "N/A"))
	print('Bus information csv file has printed. Informaiton is on the next stop location of the given busline.')

			

