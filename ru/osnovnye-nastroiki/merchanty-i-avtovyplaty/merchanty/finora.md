# Finora

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)

<mark style="color:red;">Обратите внимание, что при обновлении модуля необходимо настроить его повторно по инструкции ниже, так как после обновления файлов все поля и настройки модуля будут сброшены к состоянию по умолчанию.</mark>
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/Exe_PMx).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

{% hint style="warning" %}
Обращаем ваше внимание, что при использовании модуля на прием средств Finora фактическая сумма выплаты всегда округляется до четырех знаков после запятой на стороне сервиса.
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Finora в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="345"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (251).png" alt="" width="421"><figcaption></figcaption></figure>

**API ключ** — ключ, переданный вам менеджером Finora для конкретного метода на прием средств (уточните информацию у менеджера)

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**Тип мерчанта** (выбранный пункт закрепляется за модулем, изменить его в дальнейшем не получится):

* **Payment Link** — возвращает в заявке ссылку для оплаты по QR-коду, опция работает совместно с выбранным способом оплаты
* **Requisites** — возвращает карту или телефон для перевода средств в самой заявке через шорткод \[to\_account]

<figure><img src="../../../.gitbook/assets/изображение (192).png" alt=""><figcaption></figcaption></figure>

**Способ оплаты** — выберите подходящий метод из списка или укажите вручную свой вариант в поле "**Добавить**" (допустимые варианты уточняйте у менеджера Finora).

<figure><img src="../../../.gitbook/assets/изображение (188).png" alt=""><figcaption></figcaption></figure>

**Банк** — выберите подходящий банк из списка или укажите вручную свой вариант в поле "**Добавить**" (допустимые варианты уточняйте у менеджера Finora).

{% hint style="danger" %}
Выбирайте конкретный банк только если вы ранее выбрали формат работы **Payment Link**, при работе с форматом **Requisites** оставьте пункт по умолчанию (банк не выбран)**.**
{% endhint %}

<figure><img src="../../../.gitbook/assets/изображение (191).png" alt=""><figcaption></figcaption></figure>

{% hint style="danger" %}
При выборе конкретного банка в настройках модуля, вашему клиент нужно будет производить оплату именно с карты этого банка (в случае оплаты с другого банка платеж может быть не зачислен, в том числе и через апелляцию).
{% endhint %}

{% hint style="danger" %}
Обращаем ваше внимание, что для каждого метода необходимо создавать отдельную копию модуля мерчанта.
{% endhint %}

Для работы модуля на прием средств без использования [задания cron](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere), укажите ссылку из настроек модуля

<figure><img src="https://premium.gitbook.io/main/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252F6nSFLEEezB9OcBzt8DhE%252F%25D0%25B8%25D0%25B7%25D0%25BE%25D0%25B1%25D1%2580%25D0%25B0%25D0%25B6%25D0%25B5%25D0%25BD%25D0%25B8%25D0%25B5.png%3Falt%3Dmedia%26token%3D0c2df531-cd7a-4ff8-9fdc-dcf940e9eb68&#x26;width=768&#x26;dpr=3&#x26;quality=100&#x26;sign=d422910b&#x26;sv=2" alt=""><figcaption></figcaption></figure>

в ЛК Finora в поле **PayIn Webhook**:

<figure><img src="../../../.gitbook/assets/изображение (2) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
