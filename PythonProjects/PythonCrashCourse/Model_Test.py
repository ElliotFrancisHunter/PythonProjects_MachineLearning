from keras.datasets import cifar10
import keras.utils as utils
from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt


labels_array = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

(_, _), (x_test, y_test) = cifar10.load_data()


x_test = x_test.astype('float32') / 255.0
y_test = utils.to_categorical(y_test)

model = load_model(filepath='Image_Classifier.h5')

results = model.evaluate(x=x_test, y=y_test)
print('Test loss:', results[0])
print('Test accuracy:', results[1])

test_image_data = np.asarray([x_test[12]])  # 3 works, 5 ish, 10 works, 12

prediction = model.predict(x=test_image_data)
max_index = np.argmax(prediction[0])
print('Prediction:', labels_array[max_index])
plt.imshow(x_test[12])
plt.show()
