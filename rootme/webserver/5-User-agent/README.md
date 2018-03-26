#User-agent

10 Points
Admin is really dumb...

Переходим на сайт таска и видим, что нам нужно изменить хэдер User-agent.

![](Screenshot_1.png)

Сделаем это через Burp. Находим запрос в на вкладке HTTP History и отправляем его в Repeater.

![](Screenshot_2.png)

Изменим User-agent на admin и получим флаг.

![](Screenshot_3.png)