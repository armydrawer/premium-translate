# Custodex

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере - воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Так как коллбэки от Custodex могут фильтроваться Cloudflare (если он используется вами), необходимо запросить актуальные IP-адреса у Custodex и добавить их в белый список по [инструкции](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/dobavlenie-ip-adresov-v-whitelist-v-cloudflare)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию на сайте [Custodex](https://custodex.sv/). Пройдите KYB и подключите 2FA в личном кабинете в разделе "Настройки" -> "Аккаунт".

<figure><img src="../../../.gitbook/assets/image (1241).png" alt=""><figcaption></figcaption></figure>

## Получение пары ключей

В личном кабинете мерчанта перейдите в раздел "Настройки" -> "Интеграция", скопируйте приватный и публичные ключи в блокнот или в буфер обмена.&#x20;

<figure><img src="../../../.gitbook/assets/image (1244).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Custodex в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1246).png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1280).png" alt=""><figcaption></figcaption></figure>

**Private key** — приватный ключ, скопированный ранее в ЛК Custodex

**Public key** — публичный ключ, скопированный ранее в ЛК Custodex

## Продолжение настройки

## Особые поля

<figure><img src="../../../.gitbook/assets/image (504).png" alt=""><figcaption></figcaption></figure>

**Код валюты** — выберите из выпадающего списка валюту, которую будете ожидать на приём

<figure><img src="../../../.gitbook/assets/image (505).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
Для каждой валюты необходимо создать [отдельную копию модуля мерчанта](#user-content-fn-1)[^1], в которой выбрать соответствующую валюту, а затем подключить эту копию на вкладке "**Мерчанты и выплаты**" в настройках направления обмена, где в валюте "**Отдаю**" будет выбранная валюта
{% endhint %}

{% hint style="info" %}
Для совершения автовыплаты, где требуется передавать тэг назначения (destination tag для Ripple, payment ID для Monero, message для XEM и т.п.), необходимо создать дополнительное поле для соответствующих валют.

В разделе "**Валюты**" -> **"Доп. поля валют"** создайте новое дополнительное поле для валюты и в поле "**Уникальный ID**" задайте значение `dest_tag` (значение этого параметра одинаковое для любых криптовалют — Ripple, Monero, XEM и т.п.). После создания поля активируйте его в настройках валюты (вкладка "**Доп. поля**")

Созданное поле будет выводится в форме создания заявки, в котором пользователь будет должен указать тэг назначения.
{% endhint %}

**Тип адреса** — выберите подходящий тип адреса:

* **STATIC** — создает постоянный кошелек для клиента
* **SINGLE** — создает одноразовый (револьверный) кошелек для клиента

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).

[^1]: укажите индивидуальное название для каждой копии в поле "Заголовок" для удобства последующей настройки
