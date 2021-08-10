import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_BOOKS_API_KEY")

headers = {
    "x-api-key": api_key
}
