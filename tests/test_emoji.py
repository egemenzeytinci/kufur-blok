from filter import Filter
import unittest


class TestEmoji(unittest.TestCase):
    def test_emoji(self):
        app = Filter()
        app.blocks = ['🚫']

        sentences = [
            'orospu çocuğu yarak gibi kitap',
            'orrrrrooooossssspuuuu evladı',
            'am gibi kitap',
            'sik gibi kitap',
            'Sikimi ye Booooookkkk gibi kitap',
        ]

        results = [
            '🚫 çocuğu 🚫 gibi kitap',
            '🚫 evladı',
            '🚫 gibi kitap',
            '🚫 gibi kitap',
            '🚫 ye 🚫 gibi kitap',
        ]

        news = []

        for sentence in sentences:
            news.append(app.replace(sentence))

        self.assertEqual(news, results)
