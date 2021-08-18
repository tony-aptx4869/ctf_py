#!/usr/bin/python3
# -*- coding: UTF-8 -*-

def rsa_moder(n):
    base = 2
    while base < n:
        if n % base == 0:
            return base, n // base
        base += 1


# 求欧拉函数f(n)
def rsa_get_euler(prime1, prime2):
    return (prime1 - 1) * (prime2 - 1)


# 求私钥
def rsa_get_key(e, euler):
    k = 1
    while True:
        if (((euler * k) + 1) % e) == 0:
            return (euler * k + 1) // e
        k += 1


# 根据n,e计算d(或根据n,d计算e)
def get_rsa_e_d(n, e=None, d=None):
    if e is None and d is None:
        return

    arg = e
    if arg is None:
        arg = d

    primes = rsa_moder(n)
    p = primes[0]
    q = primes[1]

    d = rsa_get_key(arg, rsa_get_euler(p, q))

    return d


def test():
    str_fmt = 'n: {:<10} e: {:<10} d: {:<10}'

    # 导入rsa库
    import rsa as rsa
    key = rsa.newkeys(24)

    # 产生rsa密钥对
    if isinstance(key[1], rsa.PrivateKey):
        print(str_fmt.format(key[1].n, key[1].e, key[1].d))

    # 解密
    n = 14666299
    d = 2101153
    e = get_rsa_e_d(n, None, d)
    print(str_fmt.format(n, e, d))

    n = 12748507
    e = 65537
    d = get_rsa_e_d(n, e, None)
    print(str_fmt.format(n, e, d))


if __name__ == '__main__':
    # test()
    e = 65537
    euler = 15293032452367350153165488019040591774681947461806846211394110253205642263473409036704430501788674488200851282278984725917912759352314609076680106465146927987185897175378916654731151435950320195255522494291583988536029296991596619423707257925682257185042246028065776839633921182038513220548394723908052221984662464436997205150633282305927029392525099540708495780571249882489695973963632971183382777042356347551064066905696276285731788272303683511385482977782637450227421451201918293810767333044827440010656954584157537245294463744706911890881303916957823546888317663596809518986423759580164973515874335313890183844107 - 247692304124525245667211985038807577149526498494620587227372131956797094691024123744042981854305983726197861602632106839535018310683933498643676609810589875918586417866386869064768090338701012890559718753173049383323496502184441436691424048763065870187602889642817121344647370355274568061468019226498216956532 + 1
    key = rsa_get_key(e, euler)
    print(key)
