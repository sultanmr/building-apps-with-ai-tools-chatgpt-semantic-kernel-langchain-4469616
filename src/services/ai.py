import os
import openai
from dotenv import load_dotenv
load_dotenv()


def generate_review(review):
    openai.api_key = os.getenv('OPENAI_API_KEY')
    openai.api_base = "https://openrouter.ai/api/v1"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a sentiment classification bot, print out if the user is happy or sad. Only print out happy or sad."},
            {"role": "user", "content": review}
        ],
        temperature=0.7,
        max_tokens=150,
    )

    response_message = response["choices"][0]["message"]["content"]
    if response_message == "happy":    
        return "Thanks for shopping with us! We're glad to hear that you're happy with your purchase."
   
    return "Sorry to hear that you're not satisfied with your purchase. Please let us know how we can improve your experience."
