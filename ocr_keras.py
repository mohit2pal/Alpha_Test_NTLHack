import keras_ocr
import cv2
from matplotlib import pyplot as plt

pipeline = keras_ocr.pipeline.Pipeline()

# img = cv2.imread('Sample.jpg')

img = [
    keras_ocr.tools.read(images) for images in [
        'Sample.jpg',
    ]
]

prediction_groups = pipeline.recognize(img)

for i in prediction_groups:
    for y in i:
        print(y[0], "")