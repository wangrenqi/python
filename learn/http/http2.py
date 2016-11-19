import urllib2

request = urllib2.Request('http://blog.csdn.com/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError, e:
    print e.reason
    print e.code
