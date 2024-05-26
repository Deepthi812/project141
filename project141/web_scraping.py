import requests
from bs4 import BeautifulSoup
import csv

START_URL = "https://en.wikipedia.org/wiki/Lists_of_stars" 
HEADERS = ["Name", "Distance", "Mass", "Radius"]
stars_data = []