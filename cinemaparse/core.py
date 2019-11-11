import requests
import bs4
class CinemaParser:
    def __init__(self, city = 'msk'):
        self.city = city
        self.content = ''
    def extract_raw_content(self):
        if self.city == 'spb':
            self.content = requests.get('https://spb.subscity.ru')
        if self.city == 'msk':
            self.content = requests.get('https://msk.subscity.ru')
            return self.content.text
    def print_raw_content(self):
        self.soup = bs4.BeautifulSoup(self.content.text, 'html.parser')
        print(self.soup.prettify())
