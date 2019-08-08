import js2py

data = open('js_encode.js', 'r', encoding='utf8').read()
encode = js2py.eval_js(data)


def get_ret(keyword):
    aaa = encode(keyword)
    bbb = encode("qwer*") + aaa + encode("*asdf")
    bb = encode(bbb)
    return bb

# if __name__ == '__main__':
#     get_ret('黑龙江绿色食品')