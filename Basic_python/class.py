#coding: utf-8

class Dog:
    # property : 変数に近いもの
    name = ""

    # method : 関数(引数=self)
    def bark(self):
        # methodの中で，propertyにアクセスする場合は，self.property_nameと書く.
        m = self.name + ": Bow-wow!"

        print(m)

# インスタンスを定義することで，class Dogの中のproperty や method を利用できる
pochi = Dog()
pochi.name = "Pochi"
pochi.bark()


hachi = Dog()
hachi.name = "Hachi"
hachi.bark()

