# Electrum

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

{% hint style="danger" %}
Electrum позволяет отменять транзакции и подменять их, что может привести к потере средств обменником, если нижеуказанные настройки не установлены в вашем обменнике и этой спецификой Electrum захочет воспользоваться мошенник. Если вы используете модуль для работы с Electrum — **обязательно** выполните следующую настройку.

При использовании мерчантов на приём средств необходимо [пересчитывать сумму заявки](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya/sozdanie-novogo-napravleniya-obmena#pereschet-po-summe-oplaty) как минимум для статуса "**Оплаченная заявка**" в настройках направления обмена

![](<../../../.gitbook/assets/image (329).png>)

Также необходимо настроить автоматический перевод заявок в статус "**На проверке**", если фактическая сумма платежа меньше чем изначальная (опция в настройках модулей мерчантов на приём средств в разделе "**Мерчанты**").

<img src="../../../.gitbook/assets/image (328).png" alt="" data-size="original">
{% endhint %}

{% hint style="warning" %}
На прием средств и для автовыплаты **рекомендуется** использовать [разные Electrum-кошельки](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum/sozdanie-dopolnitelnogo-koshelka) — это позволит создать независимые контуры для приема и вывода BTC.

Такая мера необходима для предотвращения вывода "грязных" BTC. Если принимать и выплачивать всё на один кошелек, то есть вероятность, что вместе с чистыми средствами будет выведен и "грязный" BTC.
{% endhint %}

## Установка и настройка модуля

Выполните установку Electrum на сервер по [инструкции](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/modul-electrum/ustanovka-i-nastroika-electrum).

Обязательно сохраните в текстовый файл номер порта для подключения, адрес сервера (опционально), логин и пароль для подключения кошелька.

<figure><img src="../../../.gitbook/assets/image (1443).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Electrum в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1444).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1446).png" alt=""><figcaption></figcaption></figure>

* **Количество подтверждения платежа, чтобы считать его выполненным** — оставьте поле пустым для работы со стандартным значением, которое использует Electrum
* **Login** — данные из строки "**Пользователь для подключения**"
* **Password** — данные из строки "**Пароль пользователя для подключения**"
* **Api server** — поле заполняется только если модуль Electrum установлен на сервер, отличный от того, где установлен скрипт Premium Exchanger. Укажите IP-адрес в формате `111.111.111.111` (без указания протокола `http/https`).

{% hint style="warning" %}
Если модуль Electrum установлен на одном сервере со скриптом Premium Exchanger — оставьте поле пустым.
{% endhint %}

* **Api port** — данные из строки "**Порт для подключения**"

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
