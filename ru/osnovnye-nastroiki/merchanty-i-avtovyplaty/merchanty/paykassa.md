# PayKassa

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию/авторизацию в системе [PayKassa.pro](https://paykassa.pro/).

Перейдите в раздел "**Мерчанты**" и нажмите кнопку "**Добавить мерчант**"

<figure><img src="../../../.gitbook/assets/image (815).png" alt=""><figcaption></figcaption></figure>

Заполните открывшуюся форму:

<figure><img src="../../../.gitbook/assets/image (816).png" alt="" width="355"><figcaption></figcaption></figure>

**Название** - любое подходящее название

**Домен (без http:// или https://)** - ваш домен (пример: `premiumexchanger.com`)

**E-mail поддержки вашего мерчанта (публичная информация)** - ваш публичный e-mail

**Merchant Password** - пароль для авторизации в модуле мерчанта

**URL уведомлений об оплате инвойса \[sci\_confirm\_order]** - `http(s)://`**`ваш_домен`**`/merchant-paykassa_status.html`

**URL страницы с сообщением об успешной оплате \[redirect]** - `http(s)://`**`ваш_домен`**`/merchant-paykassa_success.html`

**URL страницы с сообщением о сбое при оплате \[redirect]** - `http(s)://`**`ваш_домен`**`/merchant-paykassa_fail.html`

**URL обработчика транзакций криптовалют(необязательное \[sci\_confirm\_transaction\_notification]** - `http(s)://`**`ваш_домен`**`/merchant-paykassa_status.html`

Вместо "**ваш\_домен**" укажите имя домена вашего обменного пункта.

В настройках созданного мерчанта вы увидите "**Merchant ID**"

<figure><img src="../../../.gitbook/assets/image (820).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" -> "**Мерчанты"** нажмите кнопку "**Добавить**" и выберите PayKassa.

<figure><img src="../../../.gitbook/assets/image (818).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (821).png" alt=""><figcaption></figcaption></figure>

**ID магазина** - Merchant ID из личного кабинета PayKassa

**Секретный ключ магазина** - пароль, сгенерированный Paykassa при создании мерчанта (Merchant Password)

## Особые поля

<figure><img src="../../../.gitbook/assets/image (809).png" alt=""><figcaption></figcaption></figure>

**Показать QR код на странице оплаты** - будет отображаться QR-код для быстрого перехода к оплате для клиента

**Способ оплаты** - выбор валюты/сети для приема средств

<figure><img src="../../../.gitbook/assets/image (812).png" alt=""><figcaption></figcaption></figure>

[**Требуемое количество подтверждений транзакции**](#user-content-fn-1)[^1] - подтвержденная транзакция означает то, что она включена в блок и, следовательно, в цепочку блоков. Она проверена и зарегистрирована, платеж обработан, его нельзя изменить или отменить. Чтобы стать законной, операция должна получить определенное количество подтверждений. Каждое новое подтверждение в геометрической прогрессии снижает риск отмены самой транзакции.

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

[^1]: 6 подтверждений – стандарт для большинства транзакций, которые считаются безопасными
