```
# ML-with-chatGPT
Using ChatGPT to build an end-to-end project of Machine Learning using the Google app store dataset.

# Google Play Store Apps Sentiment and Rating Predictor

## Overview

This project involves the development of a machine learning model to predict the sentiment and rating of Google Play Store apps based on various features. The model is integrated into a Gradio web app for easy interaction.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Gradio Web App](#gradio-web-app)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Installation

To get started, clone the repository to your local machine:

```bash```
git clone https://github.com/your-username/google-play-store-sentiment-predictor.git
cd google-play-store-sentiment-predictor
```

Create a virtual environment and install the dependencies:
```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

Usage
Train the Model
Run the Jupyter notebook train_model.ipynb to train the machine learning model on the provided Google Play Store Apps dataset.

The trained model will be saved to the models/ directory.

Run the Gradio Web App
Ensure your virtual environment is activated.

Run the Gradio app script:

```python gradio_app.py```


Open the provided link in your browser to interact with the app.
Model Training
The model is trained using scikit-learn's RandomForestRegressor for predicting app ratings and sentiment analysis based on user reviews.

Gradio Web App
The Gradio web app allows users to input values for app features, and the model will predict the sentiment and rating.

Gradio Web App

Dependencies
gr==0.9.0
gradio==2.3.6
numpy==1.21.2
scikit-learn==0.24.2
Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

License
This project is licensed under me and is free to use, improve or any.

```
This template covers the essential sections such as installation instructions, usage guidelines, information about model training, details on the Gradio web app, dependencies, contribution guidelines, and licensing information. Update the sections based on the specifics of your project. Additionally, you may want to include images or other resources to enhance your README.
```
