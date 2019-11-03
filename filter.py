import re
import random


class Filter:
    regex = ''
    words = []
    black_list = 'blacklist.txt'
    blocks = ['❗️', '❕', ' 🚫', ' 🔞']

    def __init__(self):
        self.load()
        self.set_regex()

    @staticmethod
    def preprocess(text):
        return re.sub(r'(.)\1+', r'\1', text.lower())

    def load(self):
        with open(self.black_list, 'r') as lines:
            self.words = '|'.join([line.rstrip('\n') for line in lines])

    def set_regex(self):
        self.regex = r'(\b)+({})+(\b)'.format(self.words)

    def replace(self, text):
        replace_text = random.choice(self.blocks)
        return re.sub(self.regex, replace_text, self.preprocess(text))

    def detect(self, text):
        if re.search(self.regex, self.preprocess(text)):
            return None

        return text
