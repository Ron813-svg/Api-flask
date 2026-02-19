import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
fahrenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

ocult1 = tf.keras.layers.Dense(units=5, input_shape=[1])
ocult2 = tf.keras.layers.Dense(units=6)
exitIA = tf.keras.layers.Dense(units=1)

modelo = tf.keras.Sequential([ocult1, ocult2, exitIA])
modelo.compile(loss='mean_squared_error', optimizer=tf.keras.optimizers.Adam(0.1))
modelo.fit(celsius, fahrenheit, epochs=2000, verbose=False)
