# encoding utf-8
import tensorflow as tf

def x2_plus_b(x, b):
    _x = tf.constant(x)
    _b = tf.constant(b)
    result = tf.square(_x)
    result = tf.add(result, _b)
    return result

with tf.Session() as sess:
    result = sess.run([x2_plus_b(2., 3.)])
    print(result)
    
