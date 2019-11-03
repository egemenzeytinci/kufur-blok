from tests.test_emoji import TestEmoji
from tests.test_deletion import TestDeletion


def main():
    te = TestEmoji()
    te.test_emoji()

    td = TestDeletion()
    td.test_deletion()


if __name__ == '__main__':
    main()
