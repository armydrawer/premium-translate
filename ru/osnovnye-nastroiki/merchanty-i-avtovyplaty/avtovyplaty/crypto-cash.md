# Crypto-Cash

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что модуль автовыплаты технический и **не производит** саму выплату — [модуль на приём Crypto-Cash (фиат)](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/crypto-cash#crypto-cash-fiatnye-valyuty) производит выплату криптовалюты сразу же после поступления средств от клиента, а модуль автовыплаты только подтверждает выплату средств для изменения статуса заявки на "**Выполненная**".

Использовать модуль автовыплаты Crypto-Cash (фиат) **всегда необходимо** в паре с [фиатным модулем на приём средств](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/quickex).

Также необходимо учитывать, что выплата средств **всегда** производится по курсу самого сервиса, поэтому крайне желательно использовать [парсер](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/kursy-valyut/parser-kursov-valyut-parsery-2.0) Crypto-Cash для курса в направлении обмена, где используется Crypto-Cash, а также включить [пересчет заявок по курсу обмена](https://premium.gitbook.io/main/osnovnye-nastroiki/valyuty-i-napravleniya-obmena/sozdanie-novogo-napravleniya#pereschet-po-kursu-obmena) для совпадения фактически выплачиваемой суммы с суммой из заявки.
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий работы свяжитесь с [представителем сервиса](https://t.me/CCW_Admin).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на сервисе Crypto-Cash](https://account.crypto-cash.world/registration) и авторизуйтесь в личном кабинете.

{% tabs %}
{% tab title="Crypto-Cash (фиатные валюты)" %}
Перейдите в [раздел с настройками мерчанта](https://account.crypto-cash.world/overview). Выпустите API-ключи по кнопке "**Сгенерировать API ключ**".

<figure><img src="../../../.gitbook/assets/image (592).png" alt=""><figcaption></figcaption></figure>

Выберите подходящие методы для выплаты средств и скопируйте секретный и публичный ключи в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (810).png" alt="" width="425"><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Crypto-Cash Crypto (криптовалюты)" %}
Перейдите в [раздел с настройками мерчанта](https://account.crypto-cash.world/overview). Выпустите API-ключи по кнопке "**Сгенерировать API ключ**".

<figure><img src="../../../.gitbook/assets/image (610).png" alt=""><figcaption></figcaption></figure>

Скопируйте секретный и публичный ключи в буфер обмена или текстовый файл.

<figure><img src="../../../.gitbook/assets/image (655).png" alt="" width="455"><figcaption></figcaption></figure>

При использовании мерчанта для выплаты отметьте endpoint "**Вывод**". Укажите в поле "**URL вебхука**" ссылку из настроек модуля автовыплаты.

<figure><img src="../../../.gitbook/assets/image (658).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

{% hint style="warning" %}
При выпуске API-ключей запомните или запишите тип ключа, который вы выбрали (выбирайте **ED25519**, так как Legacy-вариант будет отключен в скором времени) — вам потребуется выбрать тот же тип ключей в модуле на прием средств при настройке модуля автовыплаты.

![](<../../../.gitbook/assets/image (584).png>)![](<../../../.gitbook/assets/image (585).png>)
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите подходящий модуль в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

{% tabs %}
{% tab title="Crypto-Cash (фиатные валюты)" %}
<figure><img src="../../../.gitbook/assets/image (671).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="437"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Публичный ключ** — публичный ключ, скопированный ранее в ЛК Crypto-Cash

**Секретный ключ** — секретный ключ, скопированный ранее в ЛК Crypto-Cash
{% endtab %}

{% tab title="Crypto-Cash Crypto (криптовалюты)" %}
<figure><img src="../../../.gitbook/assets/image (3) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="490"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="437"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**Публичный ключ** — публичный ключ, скопированный ранее в ЛК Crypto-Cash

**Секретный ключ** — секретный ключ, скопированный ранее в ЛК Crypto-Cash
{% endtab %}
{% endtabs %}

## Особые поля

{% tabs %}
{% tab title="Crypto-Cash (фиатные валюты)" %}
<img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FOuxo4YJ8qDici97y8NpD%252Fimage.png%3Falt%3Dmedia%26token%3Db5944848-fd29-4600-8f8b-c7855fe2a32f&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=967ec67d&#x26;sv=2" alt="" height="99" width="388">

**API key type** — выберите тип ключей согласно ранее выбранному типу при создании ключей в ЛК Crypto-Cash
{% endtab %}

{% tab title="Crypto-Cash Crypto (криптовалюты)" %}


<img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FOuxo4YJ8qDici97y8NpD%252Fimage.png%3Falt%3Dmedia%26token%3Db5944848-fd29-4600-8f8b-c7855fe2a32f&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=967ec67d&#x26;sv=2" alt="" height="99" width="388">

**API key type** — выберите тип ключей согласно ранее выбранному типу при создании ключей в ЛК Crypto-Cash

<figure><img src="../../../.gitbook/assets/image (2217).png" alt="" width="437"><figcaption></figcaption></figure>

**Валюта** — выбор валюты для автовыплаты (при выборе пункта "**Автоматически**" будет использоваться код валюты "**Получаю**")

* **Добавить** — добавление своего кода валюты
{% endtab %}
{% endtabs %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
