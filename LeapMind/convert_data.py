# coding: utf-8
import numpy as np

def convert_CSV(image, label, output, dim):
    f = open(image, 'rb')
    o = open(output, 'w')
    l = open(label, 'rb')

    f.read(16)
    l.read(8)
    images = []

    for i in range(dim):
        image = [ord(l.read(1))]
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)

    for image in images:
        print(image)
        o.write(",".join(str(pix) for pix in image)+"\n") 
    f.close()
    o.close()
    l.close()

if __name__ == '__main__':
    convert_CSV("train-images-idx3-ubyte", "train-labels-idx1-ubyte",
            "mnist_train.csv", 60000)
    convert_CSV("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte",
            "mnist_test.csv", 10000)

