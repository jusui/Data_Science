# coding: utf-8
"""
7.[テンプレートによる文生成]
引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．
"""
def generate_sentence(x, y, z):
    # x:時間，y:文字列, z:気温[°]
    return u"{x}時の{y}は{z}°".format(x = x, y = y, z = z)

if __name__ == '__main__':
    print(generate_sentence(12, "気温", 22.4))
