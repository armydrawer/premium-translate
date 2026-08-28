# Casha.pro

{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с представителем сервиса.

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Свяжитесь с представителем сервиса для подключения и получения данных от аккаунта.

С полученными данными [войдите в личный кабинет на стороне сервиса](https://casha.pro/).

В разделе "API ключи" создайте создайте ключи для подключения модуля.

<figure><img src="../../../.gitbook/assets/image (1096).png" alt=""><figcaption></figcaption></figure>

Вы получите API ключ и секретный ключ. Сохраните их в отдельном текстовом файле.

{% hint style="warning" %}
Мерчант использует для выплат общий баланс в USDT и конвертирует сумму выплаты по внутреннему курсу.&#x20;

Уточните у представителя сервиса включена ли для вашего аккаунта возможность такой автоматической конвертации.
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите **Casha** в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1105).png" alt=""><figcaption></figcaption></figure>

Заполните указанные поля авторизации в настройках модуля.

<figure><img src="../../../.gitbook/assets/image (1111).png" alt=""><figcaption></figcaption></figure>

**Домен** — не заполняйте поле, оставьте его пустым.

**API ключ** —  API ключ, сгенерированный на стороне Casha.

**Секретный ключ** — Секретный ключ, сгенерированный на стороне Casha.

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1117).png" alt=""><figcaption></figcaption></figure>

**Код валюты** (для выплаты)**:**

* **Доп. поля (Заявка)** — использование кода валюты из заявки (выберите **\[Получаете] Код валюты**)
* **Доп. поля (Валюты)** — использование [доп.поля валюты](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-valyuty) "**Получаю**"
* **Доп. поля (Направления)** — использование [доп.поля направления обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/dopolnitelnye-polya#dopolnitelnye-polya-dlya-napravleniya-obmena)
* **Код валюты** — ручной явный выбор валюты выплаты.

<figure><img src="../../../.gitbook/assets/image (1120).png" alt=""><figcaption></figcaption></figure>

Счет — Выберите поле в котором клиент указывает счет для выплаты.

{% hint style="warning" %}
**Если используете стандартное поле "На счет", в опции выберите значение \[Получаете] Счет**.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1122).png" alt=""><figcaption></figcaption></figure>

Способ оплаты — Явно укажите желаемый способ выплаты для этой копии модуля.

{% hint style="info" %}
Способ оплаты должен соответствовать реквизитам которые вы запрашиваете у клиента для выплаты, так для метода **Card** должен запрашиваться номер карты, \
а для **SBP** или **Mobile** - номер телефона.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1125).png" alt=""><figcaption></figcaption></figure>

**Банк —** Можно выбрать банк для выплаты явно или указать автоматическое значение. В таком случае банк будет определяться по указанным реквизитам, если это возможно.

{% hint style="info" %}
Например по номеру карты определить банк можно, по номеру телефона - нельзя.&#x20;
{% endhint %}

**Cron-файл -** [создайте задание](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) с такой ссылкой на сервер&#x435;**.**

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
