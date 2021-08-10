import json
import requests
from .credentials import headers


def get_json_content(response):
    try:
        content = response.json()
    except json.JSONDecodeError:
        print("Wrong content format", response.text)
    else:
        return content


def get_initial_data():
    base_url = "https://www.googleapis.com/books/v1/volumes?q=Harry"
    response = requests.get(base_url, headers=headers)
    return get_json_content(response)


def get_query_response(intitle="", inauthor="", inpublisher="", startIndex=0, lang="en", order_by="relevance"):
    base_url = "https://www.googleapis.com/books/v1/volumes?q=Harry"
    params = {
        "intitle": intitle,
        "inauthor": inauthor,
        "inpublisher": inpublisher,
        "maxResults": 10,
        "startIndex": startIndex,
        "langRestrict": lang,
        "orderBy": order_by
    }

    response = requests.get(base_url, headers=headers, params=params)
    return get_json_content(response)


def get_single_volume(volume_id):
    base_url = f"https://www.googleapis.com/books/v1/volumes/{volume_id}"

    response = requests.get(base_url, headers=headers)
    return get_json_content(response)
