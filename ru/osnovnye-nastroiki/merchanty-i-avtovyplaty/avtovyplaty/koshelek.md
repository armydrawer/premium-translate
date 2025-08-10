# Koshelek

{% hint style="danger" %}
<mark style="color:red;">Перед настройкой автовыплат обязательно прочитайте</mark> [<mark style="color:blue;">предупреждение о рисках</mark>](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)<mark style="color:blue;">!</mark>
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию и верификацию в сервисе [Koshelek](https://koshelek.ru/). Перейдите на [страницу **"API ключи"**](https://koshelek.ru/account/keysApi) и нажмите кнопку "**Создать API ключ**".

<figure><img src="../../../.gitbook/assets/image (1757).png" alt=""><figcaption></figcaption></figure>

В открывшемся окне укажите произвольное название ключа и выберите методы для работы с API (для выплаты средств выберите "**Депозит**", "**Вывод**" и "**Чтение**"). Нажмите на кнопку "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1761).png" alt="" width="467"><figcaption></figcaption></figure>

В открывшемся окне скопируйте сгенерированные ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1760).png" alt="" width="474"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Автовыплаты**" -> "**Добавить автовыплату".**

Выберите Koshelek в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1750).png" alt="" width="419"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1753).png" alt="" width="426"><figcaption></figcaption></figure>

**Публичный ключ** — **публичный ID**, сгенерированный в ЛК Koshelek

**Секретный ключ** — **секретный ключ**, сгенерированный в ЛК Koshelek

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1754).png" alt="" width="302"><figcaption></figcaption></figure>

**Сеть** — укажите сеть валюты для корректной работы автовыплаты

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/obshie-nastroiki-merchantov-avtovyplat).
