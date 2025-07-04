# Payscrow

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premiumexchanger.com/wiki/preduprezhdenie-auto/)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта <a href="#nastroiki-v-lichnom-kabinete-merchanta" id="nastroiki-v-lichnom-kabinete-merchanta"></a>

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/Payscrow).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь и авторизуйтесь в ЛК мерчанта. В разделе "**Профиль**" ➔ "**Настройки API**" скопируйте API-ключ и ключ подписи для авторизации в модуле автовыплаты.

<figure><img src="../../../../.gitbook/assets/image (126).png" alt=""><figcaption></figcaption></figure>

В поле "**Статус продажи**" позже укажите URL из настроек модуля автовыплаты (Webhook)

<figure><img src="../../../../.gitbook/assets/image (127).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля <a href="#nastroiki-modulya" id="nastroiki-modulya"></a>

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" ➔ "**Добавить автовыплату".**

Выберите Payscrow в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../../.gitbook/assets/image (124).png" alt="" width="444"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../../.gitbook/assets/image (125).png" alt="" width="451"><figcaption></figcaption></figure>

**Домен** — URL, присланный вам представителем мерчанта

**API ключ** — API ключ, скопированный в ЛК мерчанта

**Ключ подписи**  — ключ подписи, скопированный в ЛК мерчанта

## Особые поля

<figure><img src="../../../../.gitbook/assets/image (128).png" alt="" width="516"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ для выплаты средств

**Кто платит комиссию:**

* мерчант — комиссию сервиса оплачивает обменник (сумма комиссии будет списана с вашего баланса)
* пользователь — комиссию сервиса оплачивает клиент (в этом случае клиент получит на 5% меньше, чем изначальная сумма из заявки)

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
