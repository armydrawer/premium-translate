# Rapira Crypto



{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

Пройдите регистрацию в сервисе [Rapira](https://rapira.net/). В личном кабинете обязательно включите двухэтапную аутентификацию в разделе "**Настройки**" → "**Безопасность**" → "**GoogleAuth**" (это обязательное условия для выпуска API-ключей)

Перейдите в раздел "**Настройки**" → "**API-ключи**" и нажмите кнопку "**Создать API-ключ**".

<figure><img src="../../../.gitbook/assets/image (1844).png" alt=""><figcaption></figcaption></figure>

В настройках API-ключа обязательно поставьте галочку для пункта "**Withdraw**" для разрешения вывода средств с помощью этого ключа.

<figure><img src="../../../.gitbook/assets/image (1887).png" alt="" width="375"><figcaption></figcaption></figure>

Скопируйте ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1849).png" alt="" width="342"><figcaption></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Rapira в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1842).png" alt="" width="419"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1840).png" alt="" width="422"><figcaption></figcaption></figure>

**Prviate Key** — **Приватный ключ**, сгенерированный в ЛК Rapira

**UID** — **UID**, сгенерированный в ЛК Rapira

**Host** — выберите любой из вариантов (rapira.net или rapira.org)

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1843).png" alt=""><figcaption></figcaption></figure>

**XML-код валюты** — заполнять <mark style="color:red;">**не требуется**</mark>, если вы используете [стандартные коды валют Bestchange](https://www.bestchange.ru/wiki/rates.html), в таком случае можно использовать одну копию модуля для выплаты всех криптовалют.

{% hint style="warning" %}
Если же XML-код валюты отличается от стандарта Bestchange, тогда может потребоваться заполнение этого поля. Проверить XML-коды валют можно в разделе "**Валюты**" → редактировать валюту → вкладка "**Основные настройки**" → поле "**Обозначение для XML"**.
{% endhint %}

**Валюта для конвертации** — укажите валюту, с баланса которой в ЛК мерчанта будет производиться конвертация в валюту для выплаты (чаще всего это USDT или RUB).

<figure><img src="../../../.gitbook/assets/image (1851).png" alt="" width="191"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку модуля следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
