# twit_app/services/basilica_service.py

import os
import basilica
from dotenv import load_dotenv

load_dotenv()

# key in .env 
BASILICA_API_KEY = os.getenv('BASILICA_API_KEY')

# connection
connection = basilica.Connection(BASILICA_API_KEY)
print(type(connection))

if __name__ == "__main__":
    # words
    sentences = ["Hello world!", "How are you?"]
    embeddings = connection.embed_sentences(sentences)
    print(list(embeddings)) # [[0.8556405305862427, ...], ...]
