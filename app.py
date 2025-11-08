import streamlit as st
import google.generativeai as genai
from PIL import Image
import io

# Page configuration
st.set_page_config(page_title="Simple Image Describer", layout="wide")

# --- Initialize Gemini API ---
try:
    # Load API key from secrets
    GOOGLE_API_KEY = st.secrets["GOOGLE_API_KEY"]
    
    # Configure the Gemini API
    genai.configure(api_key=GOOGLE_API_KEY)
    
    # Initialize the model
    model = genai.GenerativeModel('gemini-2.5-flash')
except Exception as e:
    st.error("Error: Unable to initialize the Gemini API. Please check your API key in the secrets.")
    st.stop()

# --- Main App UI ---
st.title("Simple Image Describer")
st.write("Upload an image and get an AI-generated description!")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Process the uploaded image
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    
    # Create a button to trigger the description
    if st.button("Describe Image"):
        try:
            with st.spinner("Generating description..."):
                # Prepare the image for the Gemini API
                if uploaded_file.type.startswith('image/'):
                    # Get the image bytes
                    image_bytes = uploaded_file.getvalue()
                    
                    # Create the image part for the Gemini API
                    image_part = {
                        "mime_type": uploaded_file.type,
                        "data": image_bytes
                    }
                    
                    # Generate the description
                    prompt = "Describe this image in detail, focusing on the main elements, colors, composition, and any notable features."
                    response = model.generate_content([prompt, image_part])
                    
                    # Display the result
                    st.write("### Description:")
                    st.write(response.text)
                    
        except Exception as e:
            st.error(f"An error occurred while processing the image: {str(e)}")
else:
    st.info("👆 Upload an image to get started!")
