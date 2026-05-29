Overview
Harvestify is an AI-powered agriculture application that leverages Deep Learning and Computer Vision to detect plant diseases from leaf images. The system helps farmers and agricultural enthusiasts identify diseases quickly and provides treatment recommendations, fertilizer suggestions, and preventive measures.
In addition, Harvestify includes a crop recommendation module that suggests suitable crops based on soil type and temperature conditions.
Features
🌿 Plant disease detection from leaf images
🤖 Deep Learning-based image classification
📊 Confidence score generation for predictions
💊 Disease treatment recommendations
🌱 Fertilizer suggestions
⚠️ Precautionary measures for disease prevention
🌾 Crop recommendation based on soil and temperature
⚡ FastAPI-powered REST API for real-time predictions
Tech Stack
Backend
Python
FastAPI
AI & Machine Learning
TensorFlow
Keras
NumPy
Image Processing
Pillow (PIL)
Frontend
HTML
CSS
JavaScript
Dataset
The model is trained to classify plant diseases across 38 categories, including:
Apple
Corn (Maize)
Grape
Orange
Peach
Pepper
Potato
Strawberry
Tomato
Soybean
Raspberry
Squash
and healthy plant classes.
Project Workflow
User uploads a leaf image.
Image is preprocessed and resized to 224×224 pixels.
TensorFlow model performs disease classification.
The system calculates prediction confidence.
Disease-specific information is retrieved.
Treatment, fertilizer, and precaution recommendations are returned to the user.
Sample API Response
{
  "disease": "Tomato Late Blight",
  "confidence": "96.84%",
  "treatment": "Use Copper fungicide",
  "fertilizer": "Use potassium rich fertilizer",
  "precautions": "Remove infected leaves"
}
Crop Recommendation Module
The application also includes a crop recommendation feature that suggests crops based on:
Soil Type
Temperature
Example:
Loamy Soil + Temperature > 20°C → Wheat
Sandy Soil → Groundnut
Other Conditions → Rice
Future Enhancements
Machine Learning-based crop recommendation
Database integration for prediction history
Cloud deployment
User authentication
Mobile application support
Expanded disease knowledge base
