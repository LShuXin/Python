import requests;
def getHTMLTEXT(url):
    try:
        r=requests.get(url,timeout=30);
        r.raise_for_status();#如果状态码不是200，会引发HTTPerror异常
        r.encoding=r.apparent_encoding;
        return t.text;
    except:
        return "产生异常";


