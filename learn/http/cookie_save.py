import cookielib
import urllib2

filename = 'cookie.txt'

cookie = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)

opener = urllib2.build_opener(handler)

respone = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True,ignore_expires=True)

