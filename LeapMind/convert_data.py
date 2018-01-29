# coding: utf-8
import numpy as np

def convert_CSV(image, label, output, dim):
    image_file = open(image, 'rb')
    writer = open(output, 'w')
    labels = open(label, 'rb')

    image_file.read(16)
    print(image_file)
    labels.read(8)
    print(labels)
    
    images = []
    for i in range(dim):
        image = [ord(labels.read(1))]
        for j in range(28*28):
            image.append(ord(image_file.read(1)))
        images.append(image)

    for image in images:
        print(image)
        writer.write(",".join(str(pix) for pix in image)+"\n") 
    image_file.close()
    writer.close()
    labels.close()

if __name__ == '__main__':
    convert_CSV("train-images-idx3-ubyte", "train-labels-idx1-ubyte",
            "mnist_train_100.csv", 100) # dim = 60000
    convert_CSV("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte",
            "mnist_test_10.csv", 10) # dim = 10000

