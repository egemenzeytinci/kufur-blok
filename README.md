KÜFÜR BLOKLAMA
----------

![homepage](/images/stop.jpg)

Kurulum ve Kullanım
----------

1.  Her şeyden önce depoyu kopyalamanız gerekmektedir.

    ```bash
    $ git clone https://github.com/egemenzeytinci/kufur-blog.git
    ```

2.  Kurulum için herhangi bir şey yapmanıza gerek yoktur.
Kullanılan tüm kütüphaneler Python dilinin doğal kütüphaneleridir.

3.  Aşağıda örnekler mevcuttur.

    ```bash
    >>> from filter import Filter
    >>> app = Filter()
    >>> app.replace('pipi bok')
    🔞  🔞
    ```
    ya da
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

Referans
----------
``blacklist.txt`` dosyası @ooguz çalışmasından alınmıştır. Bkz:
* [Blacklist](https://github.com/ooguz/turkce-kufur-karaliste)