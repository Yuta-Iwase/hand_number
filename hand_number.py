import tensorflow.keras as keras
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import RMSprop

from PIL import Image
import numpy as np
# データ加工の関数があったのでインポート
import tensorflow.keras.utils

test_x = []
test_y = []

path = 'image.png'
im = np.array(Image.open(path))
im = im[:, :, 0:3]
im = im / 255.0
test_x.append(im.tolist())
test_y.append(2)

path = 'image.png'
im = np.array(Image.open(path))
im = im[:, :, 0:3]
im = im / 255.0
test_x.append(im.tolist())
test_y.append(1)

path = 'image.png'
im = np.array(Image.open(path))
im = im[:, :, 0:3]
im = im / 255.0
test_x.append(im.tolist())
test_y.append(0)

test_x = np.array(test_x)
test_y = np.array(test_y)

from tensorflow.keras.models import load_model	

model = load_model('model.h5')

predict_classes = model.predict_classes(test_x)
print('正解:')
print(test_y)
print('推論:')
print(predict_classes)