# AI Image Detector

A Streamlit application that uses Google's Gemini 2.5 Flash AI model to generate detailed descriptions of uploaded images.

## Features

- Simple and intuitive user interface
- Support for multiple image formats (JPG, JPEG, PNG)
- Real-time image description generation
- Responsive image display
- Error handling for API and upload issues

## Prerequisites

Before running this application, make sure you have:

1. Python 3.x installed
2. A Google Gemini API key (Get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Satvikshaurya3/AI-image-detector.git
cd AI-image-detector
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Create a `.streamlit/secrets.toml` file in the project directory and add your Gemini API key:
```toml
GOOGLE_API_KEY = "your-api-key-here"
```

## Required Packages

The following Python packages are required:
- streamlit
- google-generativeai
- Pillow (PIL)

These can be installed using the requirements.txt file included in the repository.

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (typically http://localhost:8501)

3. Use the application:
   - Click the "Choose an image..." button to upload an image
   - View your uploaded image
   - Click "Describe Image" to generate a description
   - Wait for the AI to analyze and describe the image
   - View the generated description below the image

## Technical Details

- Model: Gemini 2.5 Flash (Updated from Gemini Pro Vision)
- Image formats supported: JPG, JPEG, PNG
- Interface: Streamlit web application
- API: Google Generative AI

## File Structure

```
AI-image-detector/
├── .streamlit/
│   └── secrets.toml
├── app.py
├── requirements.txt
└── README.md
```

## Error Handling

The application includes error handling for:
- Missing API key
- Invalid image uploads
- API connection issues
- Image processing errors

## Troubleshooting

1. If you see an API key error:
   - Check that your `.streamlit/secrets.toml` file exists and contains the correct API key
   - Verify that your API key is active and valid

2. If the image upload fails:
   - Ensure the image is in a supported format (JPG, JPEG, or PNG)
   - Check that the file size is reasonable

3. If the description generation fails:
   - Check your internet connection
   - Verify that your API key has sufficient quota remaining

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Google Generative AI for providing the Gemini model
- Streamlit for the web application framework

## Contact

For any queries or issues, please open an issue on the GitHub repository.