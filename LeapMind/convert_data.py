# coding: utf-8
import numpy as np

def convert_CSV(image, label, output, dim):
    with open(image, 'rb') as image_file, open(label, 'rb') as labels, open(output, 'w') as writer:
        image_file.read(16)     
        labels.read(8)
        
        images = []
        for i in range(dim):
            image = [ord(labels.read(1))] #str -> integer (code point), label
            for j in range(28*28):
                image.append(ord(image_file.read(1)))
            images.append(image)
                
        for image in images:
            # print(image)
            writer.write(",".join(str(pixel) for pixel in image)+"\n")

if __name__ == '__main__':
    convert_CSV("./dataset/train-images-idx3-ubyte", "./dataset/train-labels-idx1-ubyte",
                "mnist_train_100.csv", 100) # dim = 60000
    
    convert_CSV("./dataset/t10k-images-idx3-ubyte", "./dataset/t10k-labels-idx1-ubyte",
                "mnist_test_10.csv", 10) # dim = 10000

