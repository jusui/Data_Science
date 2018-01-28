#! /bin/bash

wget https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
wget https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
wget https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
gzip -dc https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz >train-images-idx3-ubyte
gzip -dc https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz >train-labels-idx1-ubyte
gzip -dc https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz >t10k-images-idx3-ubyte
gzip -dc https://web.archive.org/web/20150910141412/http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz >t10k-labels-idx1-ubyte

