# coding=utf-8
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    page.close()
    return html


def getCity(html):
    ref = r'<title>【(.+?)天气】.+?</title>'
    result = re.findall(ref, html)
    if len(result) > 0:
        return result[0]
    else:
        return 'error : 没City'


html = getHtml("http://www.weather.com.cn/weather/101010100.shtml")

print getCity(html)


def get_start(html):
    reg = r'<h1>.+?（今天.+?</h1>'
    get_list = re.findall(reg, html)
    if len(get_list) > 0:
        return get_list[0]
    else:
        return 'get start =0'


# <h1>19日（今天）</h1>
# def get_start(html):
#     reg=r'<h1>.+?（今天.+?</h1>'
#     get_list = re.findall(reg,html)
#     if len(get_list)>0:
#         return get_list[0]
#     else:
#         return "无数据"
#


def get_end(html):
    reg = r'<h1>.+?（明天.+?</h1>'
    get_list = re.findall(reg, html)
    if len(get_list) > 0:
        return get_list[0]
    else:
        return 'get end = 0'


# <h1>20日（明天）</h1>

# def get_end(html):
#     reg=r'<h1>.+?（明天.+?</h1>'
#     get_list = re.findall(reg,html)
#     if len(get_list)>0:
#         return get_list[0]
#     else:
#         return "无数据"




def get_block(html):
    start = html.find(get_start(html))
    end = html.find(get_end(html))
    block = html[start:end]
    return block


# def get_block(html):
#     start=html.find(get_start(html))
#     end=html.find(get_end(html))
#     block=html[start:end]
#     return block



# <h1>19日（今天）</h1>
# <big class="png40"></big>
# <big class="png40 n07"></big>
# <p class="wea" title="中度霾（南部地区重度霾）或雾转小雨">中度霾（南部地区重度霾）或雾转小雨</p>
# <p class="tem">
# <span>22℃</span>
# <i>13℃</i>
# </p>
# <p class="win">
# <em>
# <span title="无持续风向" class=""></span>
# </em>
# <i>微风</i>
# </p>
# <div class="slid"></div>
# </li>
# <li class="sky skyid lv3">
# <h1>20日（明天）</h1>



# <h1>19日（今天）</h1>

def get_block_date(block):
    reg = r'<h1>(.+?)（今天.+?</h1>'
    get_list = re.findall(reg, block)
    if len(get_list) > 0:
        return get_list[0]
    else:
        return 'get block date = null'

        # def get_block_date(block):
        #     reg=r'<h1>(.+?)（今天.+?</h1>'
        #     get_list = re.findall(reg,block)
        #     if len(get_list)>0:
        #         return get_list[0]
        #     else:
        #         return "无数据"
        #



        # <p class="wea" title="中度霾（南部地区重度霾）或雾转小雨">中度霾（南部地区重度霾）或雾转小雨</p>


def get_block_air(block):
    reg = r'p class="wea" title="(.+?)".+?'
    get_list = re.findall(reg, block)
    if len(get_list) > 0:
        return get_list[0]
    else:
        return 'get block air = null...'

        # def get_block_air(block):


#     reg=r'p class="wea" title="(.+?)".+?'
#     get_list = re.findall(reg,block)
#     if len(get_list)>0:
#         return get_list[0]
#     else:
#         return "无数据"




def get_block_day_tem(block):
    reg = r'<span>([0-9]+).+?</span>'
    get_lsit = re.findall(reg, block)
    if len(get_lsit) > 0:
        return get_lsit[0]
    else:
        return 'get block day tem = null'
        # <span>22℃</span>


# def get_block_day_tmp(block):
#     reg=r'<span>([0-9]+).+?</span>'
#     get_list = re.findall(reg,block)
#     if len(get_list)>0:
#         return get_list[0]
#     else:
#         return "无数据"






def get_block_night_temp(block):
    reg = r'<i>([0-9]+).+?</i>'
    get_list = re.findall(reg, block)
    if len(get_list) > 0:
        return get_list[0]
    else:
        return 'get block night temp = 0'

        # <i>微风</i>
        #


# def get_block_night_tmp(block):
#     reg=r'<i>([0-9]+).+?</i>'
#     get_list = re.findall(reg,block)
#     if len(get_list)>0:
#         return get_list[0]
#     else:
#         return "无数据"







def get_block_wind(block):
    reg = r'<i>([^0-9]+)</i>'
    get_list = re.findall(reg, block)
    if len(get_list) > 0:
        return get_list[0]
    else:
        return 'get block wind = 0'

        # <i>微风</i>
        #
        # def get_block_wind(block):
        #     reg=r'<i>([^0-9]+)</i>'
        #     get_list = re.findall(reg,block)
        #     if len(get_list)>0:
        #         return get_list[0]
        #     else:
        #         return "无数据"


block = get_block(html)
print block

print "所在城市:" + getCity(html)
print "查询日期:" + get_block_date(block)
print "天气情况:" + get_block_air(block)
print "日间温度:" + get_block_day_tem(block)
print "夜间温度:" + get_block_night_temp(block)
print "风力指数:" + get_block_wind(block)


# 北京
# <h1>19日（今天）</h1>
# <big class="png40"></big>
# <big class="png40 n07"></big>
# <p class="wea" title="多云转阴，有轻度霾，后半夜有零星小雨或雨夹雪">多云转阴，有轻度霾，后半夜有零星小雨或雨夹雪</p>
# <p class="tem">
# <i>3℃</i>
# </p>
# <p class="win">
# <em>
# <span title="无持续风向" class=""></span>
# </em>
# <i>微风</i>
# </p>
# <div class="slid"></div>
# </li>
# <li class="sky skyid lv3">
#
# 所在城市:北京
# 查询日期:19日
# 天气情况:多云转阴，有轻度霾，后半夜有零星小雨或雨夹雪
# 日间温度:get block day tem = null
# 夜间温度:3
# 风力指数:微风
