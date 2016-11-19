# coding=utf-8
import urllib
import learn.re


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html


def getCity(html):
    reg = r'<title>【(.+?)天气】.+?</title>'
    getlist = learn.re.findall(reg, html)
    return getlist[0]


html = getHtml("http://www.weather.com.cn/weather/101010100.shtml")
print getCity(html)

# <title>【北京天气】北京天气预报,蓝天,蓝天预报,雾霾,雾霾消散,天气预报一周,天气预报15天查询</title>

# 北京

# 这里简单介绍一下什么意思，r开头表示对后面字符串不进行转义，保持原样，输入正则表达式时基本都要加。
# 说说正则表达式里面的内容吧，前后的标示<title>和</title>和html中的保持一致，就是要匹配的字符串，主要用于确定所在的位置。
#
# 说说.+?的含义吧，.代表任意字符，+表示重复前面的类型1次或多次，所以.+合在一起表示长度大于等于2的任意字符，而.+?表示的是能够成功匹配的情况下返回最短情况的意思。
# 说了半天，举个例子，对于字符串“aaaaaabb”如果正则表达式是“a.+?b”那么应该返回aaaaaab，如果是“a.+”匹配就是aaaaaabb。
#
# 所以其实聪明的你已经发现，要想找到我们要的那行字符串，正则表示式只需要
# reg = r'<title>.+?</title>'
# 就能找到了，那中间写那么多东西岂不是多此一举？其实也不是，在这里的正则表达式中，用()括起来的区域可以作为返回值，也就是我们可以用括号()把城市所在位置表示出来，括号里是要的城市，我们用（.+?）即可表示，然后把括号前后信息补充好就成了如下
# reg = r'<title>【(.+?)天气】.+?</title>'
# 这样我们就能找到对应的行，并且返回出我们想要的城市信息了。
