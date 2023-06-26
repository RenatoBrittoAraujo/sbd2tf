import tensorflow as tf
import random
import numpy as np
print("TensorFlow version:", tf.__version__)

size_x = 10000
size_y = 10000
vec_size = 100
range_p = (1, 1000)
x = np.array([random.sample(range(range_p[0], range_p[1]), vec_size)
             for i in range(size_x+size_y)])
y = np.array([sorted(v)[len(v)//2] for v in x])

x_train, x_test = x[:size_x], x[size_x:]
y_train, y_test = y[:size_y], y[size_y:]

print(x_train.shape, y_train.shape)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape=x_train.shape[1:]),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(range_p[1])
])

predictions = model(x_train).numpy()

# The tf.nn.softmax function converts these logits to probabilities for each class:

tf.nn.softmax(predictions).numpy()

# Note: It is possible to bake the tf.nn.softmax function into the activation function for the last layer of the network. While this can make the model output more directly interpretable, this approach is discouraged as it's impossible to provide an exact and numerically stable loss calculation for all models when using a softmax output.

# Define a loss function for training using losses.SparseCategoricalCrossentropy:

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# The loss function takes a vector of ground truth values and a vector of logits and returns a scalar loss for each example. This loss is equal to the negative log probability of the true class: The loss is zero if the model is sure of the correct class .

# This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to - tf.math.log(1/10) ~ = 2.3.

loss_fn(y_train, predictions).numpy()


# Before you start training, configure and compile the model using Keras Model.compile. Set the optimizer class to adam, set the loss to the loss_fn function you defined earlier, and specify a metric to be evaluated for the model by setting the metrics parameter to accuracy.

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])

# Train and evaluate your model
# Use the Model.fit method to adjust your model parameters and minimize the loss:
min_iter = 0
iterc = 0
min_acc = 0.8
history = None
while history is None or history.history['accuracy'][-1:][0] < min_acc or iterc < min_iter:
    history = model.fit(x_train, y_train, epochs=5)
    print("last acc:", history.history['accuracy'][-1:][0])
    iterc += 1

# The Model.evaluate method checks the model's performance, usually on a validation set or test set.

model.evaluate(x_test,  y_test, verbose=2)

# The image classifier is now trained to ~98 % accuracy on this dataset. To learn more, read the TensorFlow tutorials.
# If you want your model to return a probability, you can wrap the trained model, and attach the softmax to it:

for i in range(100):
    target_arr = random.sample(range(range_p[0], range_p[1]), vec_size)
    prediction = model.predict(np.array([target_arr])).argmax()
    actual = sorted(target_arr)[len(target_arr)//2]
    print('target_arr:', target_arr)
    print('actual: ', actual)
    print('prediction: ', prediction)
    print("error: ", abs(actual-prediction), prediction/actual*100, "%")


probability_model = tf.keras.Sequential([
    model,
    tf.keras.layers.Softmax()
])
