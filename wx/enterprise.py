#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cgi import parse_qs, escape
from encrypt.WXBizMsgCrypt import WXBizMsgCrypt
from urllib import unquote
import urllib, urllib2
import json
import requests

# disable warnings
import warnings
warnings.filterwarnings("ignore")

sToken          = "c8tcRUW1j"
sEncodingAESKey = "e6msYFTXeev0zxFNQpNCzq91SfzcAKBBn3CGXAJgd90"
sAppId          = "wx1c77202393c1c41d"

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])

    sReplyEchoStr = ""
    if "echostr" in environ['QUERY_STRING']:
        d = parse_qs(environ['QUERY_STRING'])

        wxDecrypt = WXBizMsgCrypt(sToken, sEncodingAESKey, sAppId)
        ret ,sReplyEchoStr = wxDecrypt.VerifyURL(d["msg_signature"][0], d["timestamp"][0], d["nonce"][0], d["echostr"][0])

    return sReplyEchoStr or "hello world"

def sendSth():
    secret = "3AhT8A1akqYHKVuLCtrcx3OvZPFHbMO03vvBaGu4xyciG8Lj6z1OGs8Zp-81ZtnE"
    url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={0}&corpsecret={1}".format(sAppId, secret)
    access_token = ""
    if not access_token:
        web = urllib.urlopen(url)
        ret = json.loads(web.read())
        access_token = ret["access_token"]
        print access_token

    params = {
        "button":[
            {    
                "name":"小工具",
                "key":"V1001_TOOL_LITE",
                "sub_button":[
                    {
                        "type":"view",
                        "name":"搜索",
                        "url":"http://www.soso.com/"
                    },
                    {
                        "type":"click",
                        "name":"Github",
                        "key":"V1001_GITHUB"
                    },
                ]
            },
            {
                "name":"关于",
                "sub_button":[
                    {
                        "type":"view",
                        "name":"主页",
                        "url":"http://zhanglintc.co/"
                    },
                    {
                        "type":"view",
                        "name":"博客",
                        "url":"http://imlane.farbox.com"
                    },
                ]
            }
        ]
    }
    params = json.dumps(params, ensure_ascii = False)
    print params

    print requests.post("https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token={0}&agentid=0".format(access_token), data = params).text

def main():
    # sendSth()
    pass

if __name__ == '__main__':
    main()
