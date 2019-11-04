Profanity Blocking
----------

![homepage](/images/stop.jpg)

Installation and Usage
----------

1.  First of all, you need to copy the repository.

    ```bash
    $ git clone https://github.com/egemenzeytinci/kufur-blok.git
    ```

2.  You do not need to do anything for installation.
All libraries used are native libraries of the Python language.

3.  Examples are available below.

    ```bash
    >>> from filter import Filter
    >>> app = Filter()
    >>> app.replace('pipi bok')
    🔞  🔞
    ```
    or
    ```bash
    >>> from filter import Filter
    >>> app = Filter()
    >>> sentences = ['pipi bok', 'güzel kitap']
    >>> for sentence in sentences:
    ...   result = app.detect(sentence)
    ...   if result:
    ...     print(result)
    ... 
    güzel kitap
    ```

References
----------
The file ``blacklist.txt`` is taken from @ooguz. See:
* [Blacklist](https://github.com/ooguz/turkce-kufur-karaliste)
