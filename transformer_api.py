from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from PIL import Image
from io import BytesIO
from transformers import pipeline

# 1. Create the FastAPI application [cite: 157-158]
app = FastAPI(title="Hugging Face Image Classification API")

# 2. Load the pre-trained Hugging Face model into memory
# Using the pipeline abstraction makes loading models and tokenizers very straightforward
try:
    print("Loading Hugging Face model. This might take a minute on the first run...")
    image_classifier = pipeline("image-classification", model="google/vit-base-patch16-224")
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")


# 3. Describe the data we expect to receive from the user [cite: 161-163]
class ImageRequest(BaseModel):
    image_link: str


# 4. Create the endpoint where data will be sent [cite: 168-169]
@app.post("/predict")
def predict_image_class(data: ImageRequest):
    try:
        # Step A: Download the image from the provided link
        response = requests.get(data.image_link)

        response.raise_for_status()  # Check if the download was successful

        # Step B: Open the image using PIL (Python Imaging Library)
        img = Image.open(BytesIO(response.content))

        # Step C: Make the prediction using the Hugging Face pipeline
        predictions = image_classifier(img)

        # The pipeline returns a list of dictionaries with 'score' and 'label'
        # We will extract the one with the highest confidence
        top_prediction = predictions[0]

        # 5. Return the result in JSON format [cite: 180-181]
        return {
            "predicted_class": top_prediction["label"],
            "confidence_score": round(float(top_prediction["score"]), 4)
        }

    except requests.exceptions.RequestException as e:
        # Handle errors related to downloading the image
        raise HTTPException(status_code=400, detail=f"Could not download image: {str(e)}")
    except Exception as e:
        # Handle errors related to processing or the model
        raise HTTPException(status_code=500, detail=f"Error processing image: {str(e)}")