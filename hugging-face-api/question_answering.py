import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

# .env dosyasındaki çevresel değişkeni yükle
load_dotenv()

# API Key'ini çevresel değişkenden al
api_key = os.getenv("HF_TOKEN")

# InferenceClient ile bağlantı
client = InferenceClient(
    provider="hf-inference",
    api_key=api_key,
)

# Modeli kullanarak soru-cevap işlemi
answer = client.question_answering(
    question="What is my name?",
    context="My name is Clara and I live in Berkeley.",
    model="distilbert/distilbert-base-cased-distilled-squad",
)
print(answer)
