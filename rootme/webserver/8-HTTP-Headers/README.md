# HTTP Headers

15 Points
HTTP response give informations

> Statement
>
> Get an administrator access to the webpage.

Переходим на страницу таска. Нам говорят, что содержимое это не только то, что рендерит браузер. Смотрим хедеры через Burp.

![](image1.png)

Видим нестандартный заголовок Header-RootMe-Admin со значением none. Попробуем через Repeater отправить тот же запрос, но с заголовком Header-RootMe-Admin: yes.

![](image2.png)

Ура! Мы получили флаг.