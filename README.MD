
#  Image Classification API

A fast and lightweight Machine Learning REST API built with [FastAPI](https://fastapi.tiangolo.com/) and Hugging Face Transformers[cite: 151, 152]. This service accepts an image URL and returns a predicted class along with a confidence score using a pre-trained Vision Transformer (ViT) model.

---

##  Prerequisites

Before you begin, ensure you have the following installed on your machine:
* **Python 3.8+**
* **Git** (for version control) 
* **ngrok** (for exposing the local server to the internet) 
* **Postman** (optional, for testing endpoints) 

---

## ️ Installation & Setup

**1. Clone the repository**
Download the project to your local machine:
```bash
git clone [https://github.com/ananacik-455/danit_56_api.git](https://github.com/ananacik-455/danit_56_api.git)
cd your-repo-name

```

**2. Create a virtual environment (Recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

**3. Install dependencies**
Install all required Python libraries from the requirements file:

```bash
pip install -r requirements.txt

```

*(Note: Ensure your `requirements.txt` includes `fastapi`, `uvicorn`, `pydantic`, `transformers`, `torch`, `torchvision`, `pillow`, and `requests`)*.

---

##  Running the API Locally

Start the FastAPI server using Uvicorn with auto-reload enabled:

```bash
uvicorn transformer_api:app --reload

```

Your API is now running locally at: **http://127.0.0.1:8000**.

### Testing Locally via Swagger UI

FastAPI automatically generates an interactive documentation page. You can test the API directly in your browser without any extra tools:

1. Open your browser and navigate to http://127.0.0.1:8000/docs.


2. Click on the `POST /predict` endpoint.


3. Click **"Try it out"** and input a test JSON payload.

---

##  Exposing the API to the Internet

To allow external clients, front-end developers, or mobile apps to communicate with your local server, use **ngrok**.

1. Leave your FastAPI server running in its terminal window.


2. Open a **new** terminal window.


3. Run the following command to create a secure tunnel to port 8000:



```bash
ngrok http 8000

```

4. Look for the `Forwarding` URL in the green text (e.g., `https://a1b2-34-56-78-90.ngrok-free.app`). This is your new public API address!



---

##  Testing with Postman

You can test your newly public API using Postman:

1. Open Postman and create a **New -> HTTP Request**.


2. Set the HTTP method to **POST**.


3. Enter your ngrok URL followed by the `/predict` endpoint (e.g., `https://a1b2-34-56-78-90.ngrok-free.app/predict`).


4. Go to the **Body** tab, select **raw**, and choose **JSON** from the dropdown.


5. Paste the following JSON payload containing an image link:



```json
{
  "image_link": "[https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80](https://images.unsplash.com/photo-1543466835-00a7907e9de1?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80)"
}

```

6. Click **Send**.



**Expected Response:**

```json
{
  "predicted_class": "beagle",
  "confidence_score": 0.9852
}

```
