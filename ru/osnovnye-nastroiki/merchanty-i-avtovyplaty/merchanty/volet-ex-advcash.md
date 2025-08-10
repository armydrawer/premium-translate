# Volet (ex-Advcash)

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию в системе [Volet](https://account.volet.com/register) и верифицируйте ваш аккаунт для работы с API.

{% hint style="warning" %}
Для приема средств на счета мерчанта достаточно создать **SCI (shopping cart interface)** по инструкции, указанной ниже. Если вы также хотите выплачивать средства со счетов мерчанта, то дополнительно создайте новый **API (application programming interface).**
{% endhint %}

1. Перейдите в раздел "**Для разработчиков**" и нажмите кнопку "**Создать новый SCI**".

<figure><img src="../../../.gitbook/assets/image (1425).png" alt="" width="267"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1422).png" alt=""><figcaption></figcaption></figure>

Выберите платежные системы, с которыми хотите работать, и нажмите "**Продолжить**".

<figure><img src="../../../.gitbook/assets/image (677).png" alt="" width="563"><figcaption></figcaption></figure>

Заполните открывшуюся форму и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (678).png" alt="" width="550"><figcaption></figcaption></figure>

**Страница успешной транзакции** — `https://ваш_домен/merchant-advcash_success.html`

**Страница неудачной транзакции** — `https://ваш_домен/merchant-advcash_fail.html`

**Статусная страница** — `https://ваш_домен/merchant-advcash_status.html`

Вместо "**ваш\_домен**" укажите имя домена вашего обменного пункта.

{% hint style="warning" %}
Для всех пунктов выберите метод POST
{% endhint %}

2. Создайте новое API для работы с мерчантом.

Перейдите в раздел "**Для разработчиков**" и нажмите кнопку "**Создать новый API**".

<figure><img src="../../../.gitbook/assets/image (1425).png" alt="" width="267"><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (1422).png" alt=""><figcaption></figcaption></figure>

Заполните открывшуюся форму и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (679).png" alt="" width="498"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчанта".**

Выберите AdvCash в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1424).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1423).png" alt=""><figcaption></figcaption></figure>

**Email владельца счета** — **электронная почта для отображения в SCI**, указанная в личном кабинете AdvCash

**Название SCI** — **название SCI**, указанное в личном кабинете AdvCash

**Пароль от SCI** — **пароль для SCI**, указанный в личном кабинете AdvCash

**Имя API** — **название API**, указанное в личном кабинете AdvCash (заполняется в модуле автовыплаты, в модуле на прием средств можно оставить пустым)

**Пароль API** — **пароль для API**, указанный в личном кабинете AdvCash (заполняется в модуле автовыплаты, в модуле на прием средств можно оставить пустым)

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
