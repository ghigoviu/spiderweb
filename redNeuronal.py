#Se hace la red nauronal en este producto

import numpy as np  # linear algebra
import os
from time import time
from keras.preprocessing.image import ImageDataGenerator, img_to_array, image
from keras.utils import np_utils
import json
from PIL import Image
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, \
    GlobalAveragePooling2D
from keras.applications.resnet import ResNet50
from keras.models import Model
from tensorflow.keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

def entrenamiento():
    # # When to save the model
    checkpointer = ModelCheckpoint(filepath='model.weights.best.hdf5',
                            verbose=1,
                            save_best_only=True)

    # # Reduce learning rate when loss doesn't improve after n epochs
    scheduler = ReduceLROnPlateau(monitor='val_loss', factor=0.1,
                          patience=5, min_lr=1e-8, verbose=1)

    # # Stop early if model doesn't improve after n epochs
    early_stopper = EarlyStopping(monitor='val_loss', patience=10,
                          verbose=0, restore_best_weights=True)
    # # Train the model
    #Cambiar de fit_generator(...*) a fit(...*)
    history = model.fit_generator(train_generator,
                          steps_per_epoch=num_train // batch_size,
                          epochs=5,
                          verbose=1,
                          callbacks=[checkpointer, scheduler],
                          validation_data=valid_generator,
                          validation_steps=num_valid // batch_size)

    model.save('model3.h5')

def get_prediction(img, real_label):
    img = img_to_array(img) / 255

    # normalise image
    mean = [0.485, 0.456, 0.406]
    std = [0.229, 0.224, 0.225]
    img = (img - mean) / std

    img_expand = np.expand_dims(img, axis=0)

    prediction = model.predict(img_expand)
    prediction_int = np.argmax(prediction)
    print(prediction, "      ", prediction_int)

    dir_int = int_to_dir[prediction_int]
    label_name = cat_2_name[str(dir_int)]
    print(label_name, "*****" )#, real_label)

    #print("Predicted: {}\nReal:      {}".format(label_name, cat_2_name[str(real_label)]))
    print()


#Comenzar entrenamiento de red neuronal
data_dir = "Spiderweb_kb"

data_train_path = data_dir + '/train'
data_valid_path = data_dir + '/valid'
data_test_path = data_dir + '/test'

print(os.listdir(data_dir))
with open('spiders.json', 'r') as json_file:
    cat_2_name = json.load(json_file)

# print(cat_2_name['200'])
batch_size = 10

# Transforms
datagen_train = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=40,
    width_shift_range=0.1,  # randomly shift images horizontally
    height_shift_range=0.1,  # randomly shift images vertically
    horizontal_flip=True,
    featurewise_std_normalization=True,  # Normalize images
    samplewise_std_normalization=True)

datagen_valid = ImageDataGenerator(
    rescale=1. / 255,
    rotation_range=40,
    width_shift_range=0.1,  # randomly shift images horizontally
    height_shift_range=0.1,  # randomly shift images vertically
    horizontal_flip=True,
    featurewise_std_normalization=True,
    samplewise_std_normalization=True)

datagen_test = ImageDataGenerator(
    rescale=1. / 255,
    featurewise_std_normalization=True,
    samplewise_std_normalization=True)

print("Split datagen and generators")

train_generator = datagen_train.flow_from_directory(
    data_train_path,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical')

valid_generator = datagen_valid.flow_from_directory(
    data_valid_path,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical')

test_generator = datagen_test.flow_from_directory(
    data_test_path,
    target_size=(224, 224),
    batch_size=batch_size,
    class_mode='categorical')

# Lets have a look at some of our images
'''
images, labels = train_generator.next()

fig = plt.figure(figsize=(20, 10))
fig.subplots_adjust(wspace=0.2, hspace=0.4)

# Lets show the first 32 images of a batch
for i, img in enumerate(images[:6]):
    ax = fig.add_subplot(2, 3, i + 1, xticks=[], yticks=[])
    ax.imshow(img)
    image_idx = np.argmax(labels[i])
'''
#Parte en la que se prepara el modelo de predicción
int_to_dir = {v: k for k, v in train_generator.class_indices.items()}

base_model = ResNet50(
    include_top=False,
    weights="imagenet"
)

# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='elu')(x)
x = Dropout(0.95)(x)
# and a logistic layer
predictions = Dense(3, activation='softmax')(x)

for layer in base_model.layers:
    layer.trainable = True

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)
print("Se ha generado el modelo")
# compile the model (should be done *after* setting layers to non-trainable)
model.compile(optimizer=Adam(lr=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])
print("Se ha compilado el modelo")

num_train = len(train_generator.filenames)
num_valid = len(valid_generator.filenames)
num_test = len(train_generator.filenames)

#entrenamiento()

print("Probando el modelo")
model.load_weights('model.weights.best.hdf5')
#score = model.evaluate_generator(test_generator, steps=num_test // 1, verbose=1)
#for sc in score:
#   print('Test accuracy: ', sc)

for i in range(10):
    random_index = np.random.randint(0, len(test_generator.filenames))
    data_dir = "Spiderweb_kb"
    #data_dir = "C:/Users/Vrick/Desktop"

    #Pruebas en conjunto
    img = test_generator.filenames[random_index]
    imgTest = image.load_img(data_dir + "/test/" + img, target_size=(224, 224))
    real_label = test_generator.filenames[random_index].split("/")[0]

    #imgName = "C:\\Users\\Vrick\\Desktop\\Prueba\\VN117.jpg"
    #imgTest = image.load_img(imgName, target_size=(224, 224))
    #real_label = "violinista" #test_generator.filenames[random_index].split("/")[0]

    #Para pruebas particulares
    #index_particular = "Violinista/6.jpg"
    #img = index_particular
    #imgTest = image.load_img(data_dir + "/test/" + img, target_size=(224, 224))
    #real_label = index_particular.split("/")[0]

    get_prediction(imgTest, real_label)


'''
import numpy as np # linear algebra
import os
from time import time
from keras.preprocessing.image import ImageDataGenerator, img_to_array, image
from keras.utils import np_utils
import json
from PIL import Image
import os
import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, Activation, BatchNormalization, GlobalAveragePooling2D
from keras.applications import ResNet50
from keras.models import Model
from keras.optimizers import Adam
from keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping
import cv2


data_dir = "coins/data3"
batch_size=5
data_train_path =  data_dir + '/train'

with open('cat_to_name.json', 'r') as json_file:
    cat_2_name = json.load(json_file)
datagen_train = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.1,  # randomly shift images horizontally 
    height_shift_range=0.1,  # randomly shift images vertically
    horizontal_flip=True,
    featurewise_std_normalization=True, # Normalize images
    samplewise_std_normalization=True)

train_generator = datagen_train.flow_from_directory(
        data_train_path,
        target_size=(224, 224),
        batch_size=batch_size,
        class_mode='categorical')

base_model = ResNet50(
    include_top=False,
    weights="imagenet"
)
int_to_dir = {v: k for k, v in train_generator.class_indices.items()}
# add a global spatial average pooling layer
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='elu')(x)
x = Dropout(0.95)(x)
# and a logistic layer
predictions = Dense(3, activation='softmax')(x)

# this is the model we will train
model = Model(inputs=base_model.input, outputs=predictions)

for layer in base_model.layers:
    layer.trainable = True
    


model.load_weights('model.weights.best.hdf5')

font = cv2.FONT_HERSHEY_SIMPLEX         
org = (50, 50) 
# fontScale
fontScale = 1
   
# Blue color in BGR
color = (0, 0, 255)
  
# Line thickness of 2 px
thickness = 2
cap = cv2.VideoCapture(1)
label_name=""
while(True):
    #   Captura video cuadro a cuadro 
    ret, img = cap.read()
    if ret == True:
       img2=img
       img2 = cv2.putText(img2, label_name, org, font,fontScale, color, thickness, cv2.LINE_AA)
       cv2.imshow("Monedas", img2)
       
       tecla=cv2.waitKey(20)
       if tecla==ord('p'):
           filename = 'savedImage.jpg'
           cv2.imwrite(filename, img)
           imDetect=image.load_img("savedImage.jpg",target_size=(224,224))
           imDetec=image.img_to_array(imDetect)/255
           mean = [0.485, 0.456, 0.406]
           std = [0.229, 0.224, 0.225]
           imDetec=(imDetec-mean)/std
           img_expand = np.expand_dims(imDetec, axis=0)
           prediction = model.predict(img_expand)
           prediction_int = np.argmax(prediction)
           print(prediction,"      ",prediction_int)
           dir_int = int_to_dir[prediction_int]
           label_name = cat_2_name[str(dir_int)]
           print("Moneda detectada",label_name)
           # Using cv2.putText() method
          
           cv2.waitKey(2000)
       else:
           if tecla==ord('s'):
               break       
           
       # Cuando todo está listo, se libera la captura        
    else:
        
      break
cap.release()
cv2.destroyAllWindows()

'''