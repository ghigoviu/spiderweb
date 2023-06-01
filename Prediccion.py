import os

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

longitud, altura = 150, 150
modelo = 'model.h5'
pesos_modelo = "model.weights.best.hdf5"
print(os.getcwd())

cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

print("Modelos cargados correctamente")

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  result = cnn.predict(x)
  print("Result: ")
  print(result[0])
  answer = np.argmax(result)
  res = ""
  if answer == 0:
    print("pred: Araña de seda dorada")
    res = "Araña de seda dorada"
  elif answer == 1:
    print("pred: Araña violinista")
    res = "Araña violinista"
  elif answer == 2:
    print("pred: Viuda negra")
    res = "Viuda negra"

  return res

