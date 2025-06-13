# if you dont use pipenv uncomment the following:
from dotenv import load_dotenv
load_dotenv()

#Step1: Setup GROQ API key
import os

GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

#Step2: Convert image to required format
import base64

def encode_image(image_path):   
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

#Step3: Setup Multimodal LLM 
from groq import Groq

query="Is there something wrong with my face?"
# Use a vision-capable model
model = "llama-3.2-11b-vision-preview"  # This supports vision
# Alternative: model = "llama-3.2-90b-vision-preview"

def analyze_image_with_query(query, model, encoded_image):
    client = Groq(api_key=GROQ_API_KEY)  # Pass API key explicitly
    
    # Check if the model supports vision
    vision_models = [
        "llama-3.2-11b-vision-preview", 
        "llama-3.2-90b-vision-preview"
    ]
    
    if model in vision_models:
        # Vision model - use multimodal format
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text", 
                        "text": query
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{encoded_image}",
                        },
                    },
                ],
            }
        ]
    else:
        # Text-only model - use string format (image will be ignored)
        messages = [
            {
                "role": "user",
                "content": query  # Simple string format
            }
        ]
        print(f"Warning: {model} doesn't support vision. Image will be ignored.")
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=1000,
            temperature=0.7
        )
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"

# Alternative function for text-only queries
def analyze_text_query(query, model="llama3-8b-8192"):
    client = Groq(api_key=GROQ_API_KEY)
    
    messages = [
        {
            "role": "user",
            "content": query
        }
    ]
    
    try:
        chat_completion = client.chat.completions.create(
            messages=messages,
            model=model,
            max_tokens=1000,
            temperature=0.7
        )
        return chat_completion.choices[0].message.content
    
    except Exception as e:
        return f"Error: {str(e)}"