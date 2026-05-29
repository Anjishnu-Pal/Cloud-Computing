import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras import layers, models
import json

(x_train,y_train),(x_test,y_test)=mnist.load_data()

x_train=x_train[:30000]/255.0
y_train=y_train[:30000]

model=models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(128,activation='relu'),
    layers.Dense(10,activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

print("VM1 Training Started")

model.fit(x_train,y_train,epochs=2,batch_size=128)

loss,acc=model.evaluate(x_test/255.0,y_test)

with open("vm1_result.txt","w") as f:
    f.write(str(acc))

print("VM1 Accuracy:",acc)