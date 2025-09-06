---
noIndex: true
---

# Koshelek

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

Пройдите регистрацию и верификацию в сервисе [Koshelek](https://koshelek.ru/). Перейдите на [страницу **"API ключи"**](https://koshelek.ru/account/keysApi) и нажмите кнопку "**Создать API ключ**".

<figure><img src="../../../.gitbook/assets/image (1816).png" alt=""><figcaption></figcaption></figure>

В открывшемся окне укажите произвольное название ключа и выберите методы для работы с API (для приема средств выберите "**Депозит**" и "**Чтение**"). Нажмите на кнопку "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1818).png" alt="" width="464"><figcaption></figcaption></figure>

В открывшемся окне скопируйте сгенерированные ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (1819).png" alt="" width="474"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Koshelek в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1808).png" alt="" width="422"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1810).png" alt="" width="426"><figcaption></figcaption></figure>

**Публичный ключ** — **публичный ID**, сгенерированный в ЛК Koshelek

**Секретный ключ** — **секретный ключ**, сгенерированный в ЛК Koshelek

## Особые поля

<figure><img src="../../../.gitbook/assets/image (1811).png" alt="" width="302"><figcaption></figcaption></figure>

**Сеть** — укажите сеть для корректной выдачи реквизитов в заявке при использовании мерчанта

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
