# CRLF
20 Points

>Statement
>
>Inject false data in the journalisation log.

���� � ������ ��� �����������. ������� �����. �� ���������� � �����, ��� ����� ���� ��� ������� ��������������. �� ��������� ������������, ��� ��� �����, ����� � ���� ���� "admin authenticated.". ��� ����� �������� ������, ��� � ��������� username ������ ������� ����� ������ cr � lf. � URI-��������� ��� �������� ��� %0d%0a. �������� ��� �������: 

```
GET /web-serveur/ch14/?username=admin+authenticated.%0d%0aguest
```

![](image1.png)

��� �� �������� ����!