# Directory traversal

25 Points
Photo gallery v 0.01

> Statement
>
> Find the hidden section of the photo galery.

Перейдем на любую вкладку. Пусть это будет apps. URL этой страницы: challenge01.root-me.org/web-serveur/ch15/ch15.php?galerie=apps. Смотрим на html-код.

![](image1.png)

Видим, что параметр galarie указывает директорию, содержимое которой нужно вывести. Попробуем вывести содержимое самой папки galarie (ch15.php?galarie=./)

![](image2.png)

Наше внимание привлекла папка 86hwnX2r (полное название можно найти в html-коде). Смотрим, что в ней

![](image3.png)

В ней находится файла password.txt. Для того, чтобы его открыть перейдем по адресу challenge01.root-me.org/web-serveur/ch15/galerie/86hwnX2r/password.txt.