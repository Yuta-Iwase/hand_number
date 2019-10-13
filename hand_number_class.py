import tensorflow as tf
import tensorflow.keras as keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import RMSprop

from PIL import Image
import numpy as np
# データ加工の関数があったのでインポート
import tensorflow.keras.utils
from tensorflow.keras.models import load_model	

    

class Hand_num():
    # model = load_model('model.h5')
    test_y = []
    # global graph

    def estimate(self):
        model = load_model('model.h5')
        path = 'image.png'
        im = np.array(Image.open(path))
        im = im[:, :, 0:3]
        im = im / 255.0
        test_x = []
        test_x.append(im.tolist())
        # test_x.append(im.tolist())
        predict_classes = model.predict_classes(test_x)
        return predict_classes
    # print('正解:')
    # print(test_y)
    # print('推論:')
    # print()