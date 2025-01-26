from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the trained model
model = load_model("best_model.h5")

# Load and preprocess the test image
# Match the size used during training
img = load_img("pcb_data/3ymxgu5dewzd1.jpeg", target_size=(128, 128))
img_array = img_to_array(img) / 255.0  # Normalize pixel values to [0, 1]
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension

# Make a prediction
prediction = model.predict(img_array)
print("Good PCB" if prediction[0][0] > 0.5 else "Bad PCB")
