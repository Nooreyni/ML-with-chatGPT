import gradio as gr
import numpy as np

# Function to make predictions using the trained RandomForestRegressor model
def predict_rating(reviews, size, content_rating_encoded, last_updated_year):
    # Transform input values into a NumPy array
    input_values = np.array([[reviews, size, content_rating_encoded, last_updated_year]])

    # Use the trained RandomForestRegressor model to make predictions
    prediction = rf_reg_model.predict(input_values)

    # Return the predicted rating
    return prediction[0]

# Create custom components
reviews_input = gr.components.Number()
size_input = gr.components.Number()
content_rating_encoded_input = gr.components.Number()
last_updated_year_input = gr.components.Number()
predicted_rating_output = gr.components.Textbox()

# Create Gradio interface with custom components
iface = gr.Interface(
    fn=predict_rating,
    inputs=[reviews_input, size_input, content_rating_encoded_input, last_updated_year_input],
    outputs=predicted_rating_output,
    live=True
)

# Launch the Gradio interface
iface.launch()

