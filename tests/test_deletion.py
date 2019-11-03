from filter import Filter
import unittest


class TestDeletion(unittest.TestCase):
    def test_deletion(self):
        app = Filter()

        sentences = [
            'orospu çocuğu yarak gibi kitap',
            'orrrrrooooossssspuuuu evladı',
            'am gibi kitap',
            'sik gibi kitap',
            'Sikimi ye Booooookkkk gibi kitap',
            'güzel kitap çok sevdim',
            'resmen mükemmel',
        ]

        results = [
            'güzel kitap çok sevdim',
            'resmen mükemmel',
        ]

        news = []

        for sentence in sentences:
            result = app.detect(sentence)

            if result:
                news.append(result)

        self.assertEqual(news, results)
