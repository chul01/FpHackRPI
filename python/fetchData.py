import urllib2
import urllib
import requests;
request = requests.get('http://api.tripadvisor.com/api/partner/2.0/location/258705?key=193e8c94-8953-49b0-82aa-925202d810f6');

print(request.json());