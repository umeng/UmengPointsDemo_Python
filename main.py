# -*- coding: utf-8 -*-
import requests
import hashlib
import time
import json
import copy
import base64
from wsq_encrypto import prpcrypt
from helper import check_request

from HExceptions import parametersTypWrongException

host = 'api.wsq.umeng.com'
def post_data(url_path, ak, secret, encrypted_data, header=None, need_params=None):
    params_data = {"ak":ak,"encrypted_data":encrypted_data}

    try:
        if not isinstance(need_params, (dict, type(None))):
            raise parametersTypWrongException()
    except Exception as e:
        print str(e)

    if need_params:
        params_data.update(need_params)

    url_params = sorted(params_data.iteritems(), key=lambda d:d[0])
    url_params = [ (item[0], item[1].encode('utf-8')) if isinstance(item[1], unicode) else item for item in url_params]
    url_params = [ item[0]+"="+str(item[1]) for item in url_params]
    url_params = "&".join(url_params)

    # md5 signature
    m = hashlib.md5()
    t = int(time.time())
    info = "POST:%s:%d:%s:%s" %(url_path,t, url_params, secret)
    print info
    m.update(info)
    signdata = m.hexdigest()

    url =  "https://%s%s?ak=%s&_t_=%d&_s_=%s&_e_=%s&sdkv=2.5.0" %(host, url_path, ak, t, signdata, "md5")
    print url
    r = requests.post(url, data = params_data, headers=header)
    check_request(r)

    return json.loads(r.text)


def get_data(url_path, ak, secret, header=None, need_params=None):
    m = hashlib.md5()
    t = int(time.time())
    info = "GET:%s:%d:%s" %(url_path,t, secret)
    m.update(info)
    signdata = m.hexdigest()

    params_data = {"ak":ak, "_t_":t, "_s_":signdata,"_e_":"md5", "sdkv":"2.5.0"}

    if not isinstance(need_params, (dict, type(None))):
        raise parametersTypWrongException

    if need_params:
        params_data.update(need_params)

    url_params = sorted(params_data.iteritems(), key=lambda d:d[0])
    url_params = [ (item[0], item[1].encode('utf-8')) if isinstance(item[1], unicode) else item for item in url_params]
    url_params = [ item[0]+"="+str(item[1]) for item in url_params]
    url_params = "&".join(url_params)

    url =  "https://%s%s?%s" %(host,url_path, url_params)
    r = requests.get(url,headers=header)
    check_request(r)
    return json.loads(r.text)


def get_token(ak, secret):
    info = json.dumps({"ak":ak})
    print info
    data = prpcrypt(secret).encrypt(info)
    url_path = "/v2/user/token"
    # decode
    encrypted_data = base64.b64encode(data)
    print encrypted_data

    r = post_data(url_path, ak, secret, encrypted_data)
    access_token = r.get('access_token')

    expire = r.get("expire")
    return access_token, expire


def currencyOp(ak, secret, access_token, **kwargs):
    point_op_params = kwargs
    point_op_params.update({'ak':ak})
    encrpyt_data = json.dumps(copy.deepcopy(point_op_params))
    data = prpcrypt(secret).encrypt(encrpyt_data)
    # decode
    encrypted_data = base64.b64encode(data)

    url_path = "/v2/pointbank/currency/op/"
    ret = post_data(url_path, ak, secret, encrypted_data, {"accesstoken":access_token}, need_params=point_op_params)
    return ret


if __name__ == "__main__":
    ak = "54d19091fd98c55a19000406"
    community_id = "54d19014ee785020801f83c4"
    secret = "cd8ca533bdea02230cdbd9719aedfe7c"

    accesstoken, expire = get_token(ak, secret)
    print accesstoken

    import pprint

    currencyOpParams = {"fuid":"5715f7057019c9506727e5ec", "community_id":community_id, "currency":20,
                        "desc":u"中文测试", "identity":"lo23512"}
    ret = currencyOp(ak, secret, accesstoken, **currencyOpParams)
    pprint.pprint(ret)

