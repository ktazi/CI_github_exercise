from tensorflow import keras
import pandas as pd
from keras.callbacks import EarlyStopping
import sys

#create the model
model = keras.Sequential([keras.layers.Flatten(input_shape=(28,28)),
                        keras.layers.Dense(128, activation='relu', input_shape=(28,28)), 
                        keras.layers.Dense(10, activation='softmax')])
model.compile(loss='binary_crossentropy', optimizer="adam", metrics=['accuracy'])
print(model.summary())
#import train dataset
df = pd.read_csv(sys.argv[0])
df[df.columns[1:]] = df[df.columns[1:]] / 255 # normalization
X = df[df.columns[1:]].values.reshape((14999, 28,28))
Y = keras.utils.to_categorical(df["label"].values)
print(X.shape,Y.shape)
es = EarlyStopping(monitor='accuracy', mode='auto', verbose=1, patience=20)
model.fit(X,Y, epochs=70,batch_size=800, verbose=1,callbacks=[es])
model.save("model.h5")
