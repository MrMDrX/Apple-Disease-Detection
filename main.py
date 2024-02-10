from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import io

app = Flask(__name__)
model = load_model('models/model.h5')  # Load your saved model

@app.route('/')
def home():
    return render_template('index.html')


class_names = ['Blotch Apple', 'Normal Apple', 'Rotten Apple', 'Scab Apple']

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        img = request.files['image']
        img_bytes = img.read()
        img = image.load_img(io.BytesIO(img_bytes), target_size=(224, 224))  
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x /= 255.0

        predictions = model.predict(x)
        predicted_class_idx = np.argmax(predictions)
        predicted_class = class_names[predicted_class_idx]
        confidence = np.max(predictions)

        return f"This Looks like a <b>{predicted_class}</b>, with {confidence*100:.2f} % confidence"

if __name__ == '__main__':
    app.run(debug=True ,port=3000)
