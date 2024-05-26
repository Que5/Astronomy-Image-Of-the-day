import requests
import json


API_KEY = "BIb0sPZEF4jfKgv5Ugr3AjV9eyXMVWiyGXRvukUt"

url = "https://api.nasa.gov/planetary/apod&count=1" \
      "&apiKey=" + API_KEY


# Make the request
response = requests.get(url)

# Check for successful response before parsing data
if response.status_code == 200:
  try:
    data = json.loads(response.text)
    print(data)
  except json.JSONDecodeError:
    print("Error: Invalid JSON data received from API.")
else:
  print("Error: API request failed. Status code:", response.status_code)




# import requests



# API_KEY = "BIb0sPZEF4jfKgv5Ugr3AjV9eyXMVWiyGXRvukUt"

# url = "https://api.nasa.gov/planetary/apod&count=3" \
#       "&apiKey=BIb0sPZEF4jfKgv5Ugr3AjV9eyXMVWiyGXRvukUt"


# # Make the request
# response = requests.get(url)

# data = response.json()

# print(data)


# title = data["title"]
# image_url = data["url"]
# explanation = data["explanation"]

# image_filepath = "img.png"
# response1 = requests.get(image_url)
# with open(image_filepath, 'wb') as file:
#     file.write(response1.content)