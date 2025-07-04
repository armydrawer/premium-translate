# Раздел "Заявки"

Раздел "Заявки" в панели администратора предназначен для управления заявками на покупку и продажу валют. В этом разделе вы можете просмотреть и управлять всеми заявками, которые были созданы клиентами на вашем сайте.

Для каждой заявки вы можете просмотреть информацию о клиенте, такую как его имя, email, телефон, имя криптовалюты, сумму обмен, курс валют и другие данные. Вы также можете изменить статус заявки, отклонить или подтвердить заявку, а также отправить клиенту комментарий, который будет отображаться в заявке.

<figure><img src="../../.gitbook/assets/image (1611).png" alt=""><figcaption></figcaption></figure>

Рассмотрим параметры конкретной заявки.

<figure><img src="../../.gitbook/assets/image (1612).png" alt=""><figcaption></figcaption></figure>

Данные над окном заявки:

* **Окно для галочки** — необходимо отметить, если вы хотите сменить статус у конкретной заявки (также можно отмечать сразу несколько заявок) или удалить её.

Также вы можете добавить реквизиты клиента из заявки в черный список, выбрав пункт "Добавить в черный список" — после этого все реквизиты клиента (e-mail, номер счета/карты/кошелька из "Отдаю" и/или "Получаю", IP-адрес, Skype будут добавлены в разделе "Черный список")

<div><figure><img src="../../.gitbook/assets/image (1619).png" alt="" width="425"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/image (1621).png" alt="" width="381"><figcaption></figcaption></figure></div>

* **ID заявки** — идентификатор заявки, присвоенный скриптом автоматически

{% hint style="info" %}
Вы можете изменить начальный ID, активировав модуль "**Установка начального ID заявки**" в разделе "**Модули**" (после изменения начального ID, последущие создаваемые заявки будут вести отсчет с указанного числа)

![](<../../.gitbook/assets/image (1613).png>)
{% endhint %}

* **Графический флаг** — языковая версия сайта, на которой клиент создал заявку
* **Буквенный код страны**  — страна клиента (определяется по IP-адресу), совершившего заявку. Если вместо буквенного кода отображается N/A, это означает, что страна клиента не определена по IP-адресу (встречается при использовании клиентом [IPv6](https://ru.wikipedia.org/wiki/IPv6))

<figure><img src="../../.gitbook/assets/image (1614).png" alt="" width="396"><figcaption></figcaption></figure>

* **Имя клиента** — никнейм клиента, выбранный им при регистрации на сайте

Также над окном заявки могут отображаться различные уведомления для оператора:

<figure><img src="../../.gitbook/assets/image (549).png" alt="" width="404"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (548).png" alt="" width="323"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (551).png" alt="" width="400"><figcaption></figcaption></figure>

Под окном заявки будут отображаться различные фильтры и кнопки:

<figure><img src="../../.gitbook/assets/image (552).png" alt=""><figcaption></figcaption></figure>

* **Инфо** — по нажатию кнопки раскрывается дополнительная информация по заявке

<figure><img src="../../.gitbook/assets/image (553).png" alt="" width="563"><figcaption></figcaption></figure>

* **Похожие** — в общем списке заявок будут отфильтрованы и отображаться только те заявки, у которых тот же e-mail, skype и номер телефона, что и в заявке, под которой нажата кнопка (фильтрация по клиенту)
* **По счету "Отдаю"** — будут отфильтрованы и отображаться только заявки с тем же счетом "**Отдаю**", что и в заявке, под которой нажата кнопка
* **По счету "Получаю"** — будут отфильтрованы и отображаться только заявки с тем же счетом "**Получаю**", что и в заявке, под которой нажата кнопка
* **По e-mail** — будут отфильтрованы и отображаться только те заявки, у которых тот же e-mail, что и в заявке, под которой нажата кнопка
* **По IP** — будут отфильтрованы и отображаться только те заявки, у которых тот же IP-адрес, что и в заявке, под которой нажата кнопка
* **Редактировать** — ручное редактирование параметров заявки

<figure><img src="../../.gitbook/assets/image (554).png" alt="" width="355"><figcaption></figcaption></figure>

* **Пересчитать сумму** — будет пересчитана сумма по заявке (актуально, если клиент заплатил меньшую сумму, чем указана в заявке и не используется [автоматический пересчет суммы](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-summe-oplaty)
* **Пересчитать курс** — будет пересчитан курс по заявке (актуально, если не используется [автоматический пересчет курса обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-kursu-obmena))
* **Перевести** — в заявке по направлению обмена с подключенным модулем автовыплаты и выплатой по кнопке, будет отображаться кнопка для ручного запуска подключенной автовыплаты

<figure><img src="../../.gitbook/assets/image (1615).png" alt="" width="563"><figcaption></figcaption></figure>

При подключенном мерчанте на прием в заявке будут отображаться реквизиты мерчанта, по которым клиент выполняет оплату, тэг назначения, ID транзакции мерчанта (при обмене криптовалют) и реальная сумма оплаты (сумма, которую перевел клиент)

<figure><img src="../../.gitbook/assets/image (1616).png" alt="" width="411"><figcaption></figcaption></figure>

При подключенной автовыплате в заявке будут отображаться ID транзакции автовыплаты (при обмене криптовалют), TXID выплаты (для проверки платежа через обозреватель блокчейна — к примеру, [Blockchair](https://blockchair.com/)) и реальная сумма выплаты (сумма, которая была переведена клиенту)

<figure><img src="../../.gitbook/assets/image (1618).png" alt="" width="469"><figcaption></figcaption></figure>

При подключенной [AML-проверке](https://premium.gitbook.io/main/osnovnye-nastroiki/proverka-aml) при обмене криптовалют в заявке будет отображаться вероятность получения "грязной" валюты и кнопка "**Проверить**" для ручного запуска проверки

<figure><img src="../../.gitbook/assets/image (1617).png" alt="" width="450"><figcaption></figcaption></figure>

Рассмотрим другие параметры заявки:

<figure><img src="../../.gitbook/assets/image (542).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (543).png" alt=""><figcaption></figcaption></figure>

* **Курс** — курс при создании заявки
* Окно действий отображается при использовании платного [модуля "Торговые действия"](https://premium.gitbook.io/main/osnovnye-nastroiki/modul-torgovye-deistviya) и предназначено для запуска торговых действий по заявке

<figure><img src="../../.gitbook/assets/image (547).png" alt="" width="221"><figcaption></figcaption></figure>

* **Дата создания** — дата и время создания заявки
* **Дата изменения** — дата и время изменений в заявке (если они были)

<figure><img src="../../.gitbook/assets/image (544).png" alt=""><figcaption></figcaption></figure>

* **Отдаете** — валюта, которую отдает клиент
* **Сумма (с доп. ком.)** — сумма с учетом [комиссий обменного пункта](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (если комиссии добавлены)
* **Сумма (с доп. ком.)** — сумма с учетом комиссий обменного пункта и [комиссий платежной системы](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (если комиссии добавлены)

<figure><img src="../../.gitbook/assets/image (545).png" alt=""><figcaption></figcaption></figure>

* **Получаете** — валюта, которую получает клиент
* **Сумма (с доп. ком.)** — сумма с учетом [комиссий обменного пункта](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-obmennogo-punkta) (если комиссии добавлены)
* **Сумма (с доп. ком.)** — сумма с учетом комиссий обменного пункта и [комиссий платежной системы](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#vkladka-komissii-platezhnykh-sistem) (если комиссии добавлены)
* **На счет** — счет, указанный клиентом при создании заявки

<figure><img src="../../.gitbook/assets/image (546).png" alt=""><figcaption></figcaption></figure>

* **E-mail** — e-mail клиента, указанный им при создании заявки
* **IP-адрес** — IP-адрес клиента
* **User agent** — строка, которую браузер клиента отправляет на сервер при запросе веб-страницы, содержащая информацию о его операционной системе, браузере и его версии, а также другие данные, такие как тип устройства и язык. Веб-сервер использует эту информацию для того, чтобы предоставить оптимизированную версию веб-страницы для устройства и браузера клиента.
