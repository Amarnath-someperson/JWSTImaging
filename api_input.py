import requests
import json


# Allow changing the page to view all images
def generate_json(page, results):
    try:
        url = "https://api.jwstapi.com/all/type/jpg?page=" + page + "&perPage=" + results

        payload = {}
        headers = {
            'X-API-KEY': '44858ca7-8346-4f1b-b47c-843555aaa270'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        response = response.json()
        json_ = json.dumps(response, indent=2)
        with open("raw/imagedetails.json", "w") as outfile:
            outfile.write(json_)
    except:
        print('An error occured. Check your input and try again')
