import requests
from bs4 import BeautifulSoup
from PIL import Image

# Setting the URL of the CCTV camera's web interface
url = "http://example.com/camera"

# Setting the login credentials
username = "username"
password = "password"

# Making a GET request to the login page
login_url = url + "/login"
session = requests.Session()
login_page = session.get(login_url)

# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(login_page.text, 'html.parser')
form = soup.find('form')
csrf_token = form.find('input', {'name': '_csrf'})['value']

# Setting the login data and making a POST request to the login page
login_data = {'username': username, 'password': password, '_csrf': csrf_token}
session.post(login_url, data=login_data)

# Making a GET request to the live view page
live_view_url = url + "/liveview"
live_view_page = session.get(live_view_url)

# Parse the HTML response with BeautifulSoup
soup = BeautifulSoup(live_view_page.text, 'html.parser')
img_url = soup.find('img')['src']

# Making a GET request to the image URL and save the image
img_data = session.get(img_url).content
with open('image.jpg', 'wb') as f:
    f.write(img_data)

# Display the image using PIL
img = Image.open('image.jpg')
img.show()
