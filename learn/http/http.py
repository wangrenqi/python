import urllib2
import urllib

url = 'http://www.server.com/login'
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT'
values = {'username' : 'cqc', 'password' : 'XXXX'}
headers = { 'User-Agent' : 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)' ,
            'Referer': 'http://www.zhihu.com/articles' }
data = urllib.urlencode(values)
request =urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

# response = urllib2.urlopen("http://www.baidu.com")
# print response.read()