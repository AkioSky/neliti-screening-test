import requests
from html.parser import HTMLParser
from io import StringIO
from collections import Counter


class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = StringIO()

    def handle_data(self, data):
        self.text.write(data)

    def get_data(self):
        return self.text.getvalue()


def word_frequencies(url='https://www.djangoproject.com/'):
    """
    Downloads the content from the given URL and returns a dict {word -> frequency}
    giving the count of each word on the page. Ignores HTML tags in the response.
    :param url: Full URL of HTML page
    :return: dict {word -> frequency}
    """
    r = requests.get(url)
    s = MLStripper()
    s.feed(r.text)
    text = s.get_data()
    wordlist = text.split()
    counts = Counter(wordlist)
    return dict(counts)


print(word_frequencies())
