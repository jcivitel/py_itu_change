from urllib.request import urlopen
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attr):
        print("Found td Tag", tag)


url = "https://www.itu.int/oth/T0202.aspx?parent=T0202"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")

parser = MyHTMLParser()
parser.feed(html)
