# KVIRIN Email Secure Analiser

Kvirin Behavior Analyzer

Накапливание данных пользователя в процессе авторизации:
- Логин пользователя;
- IP-адрес;
- Разрешение экрана;
- Видеокарта;
- User-agent;
- Операционная система;
- Токен пользователя;
- Страна;
- Город;
- Область;
- Край.

Осуществляет сверку данных с данными предыдущих авторизаций при каждом подключении.
Если в ходе авторизации процент совпадения меньше 70, то модуль оповещает об этом. 
В будущем можно произвести усовершенствование модуля и через него осуществлять запуск почтового клиента и его блокировку, если  процент совпадений меньше установленного минимума.


Модули проверки в папке Parser:
- Virus_total - Проверка хэшей файлов на заражение
- Parser_pwned_passwd - проверяем учетные записи на наличие в скомпрометированных БД
- Cisco Talos  - для проверки репутации почтовых и ip-адресов
 
 Модули необходимы для интеграции с Kvirin Email Secure Analiser.
