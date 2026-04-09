# MEXC

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках!</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь на бирже MEXC](https://www.mexc.com/ru-RU/register), авторизуйтесь в личном кабинете и перейдите в раздел "**Управление API**".

<figure><img src="../../../.gitbook/assets/изображение (215).png" alt=""><figcaption></figcaption></figure>

Выпустите API-ключи с правами доступа, отмеченными на скриншоте.

<figure><img src="../../../.gitbook/assets/1000088955.jpg" alt=""><figcaption></figcaption></figure>

Пройдите проверку безопасности при выпуске ключей.

<figure><img src="../../../.gitbook/assets/изображение (217).png" alt=""><figcaption></figcaption></figure>

Скопируйте выпущенные ключи в буфер обмена или в текстовый файл.

<figure><img src="../../../.gitbook/assets/изображение (218).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите MEXC в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/изображение (219).png" alt="" width="357"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/изображение (220).png" alt="" width="380"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — Access Key, скопированный ранее в ЛК MEXC

**Секретный ключ** — Secret Key, скопированный ранее в ЛК MEXC

## Особые поля

<figure><img src="../../../.gitbook/assets/изображение (214).png" alt="" width="563"><figcaption></figcaption></figure>

**Способ оплаты** — выбор криптовалюты для автовыплаты

* **Добавить** — добавление своего кода валюты

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
