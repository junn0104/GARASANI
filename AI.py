import tensorflow as tf
import keras


commands = ['deepvoice', 'human']

norm_layer = keras.layers.Normalization()
input_shape = (624, 129, 1)
num_labels = len(commands)

imported = keras.models.Sequential([
    keras.layers.Input(shape=input_shape),
    keras.layers.Resizing(32, 32),
    norm_layer,
    keras.layers.Conv2D(32, 3, activation='relu'),
    keras.layers.Conv2D(64, 3, activation='relu'),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.25),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.5),
    keras.layers.Dense(num_labels),
])

imported.load_weights('model.weights.h5')

def get_spectrogram(waveform):
    spectrogram = tf.signal.stft(waveform, frame_length=255, frame_step=128)
    spectrogram = tf.abs(spectrogram)
    spectrogram = spectrogram[..., tf.newaxis]
    return spectrogram

def predict(file_path):
    x = file_path
    x = tf.io.read_file(str(x))
    x, sample_rate = tf.audio.decode_wav(x, desired_channels=1, desired_samples=16000*5,)
    x = tf.squeeze(x, axis=-1)
    x = get_spectrogram(x)
    x = x[tf.newaxis,...]

    prediction = imported(x)

    if prediction[0][0] > prediction[0][1]:
        return "deepvoice"
    else:
        return "human"
