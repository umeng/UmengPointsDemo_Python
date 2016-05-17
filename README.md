# UmengPointsDemo_Python

##使用方法
<pre><code>
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

</code></pre>
