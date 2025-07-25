# Quixfer

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/quixfer).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

[Зарегистрируйтесь](https://quixfer.cc/#contacts) на сервисе Quixfer, авторизуйтесь в личном кабинете и перейдите в раздел "**Settings**" ➔ "**Security**".

<figure><img src="../../../.gitbook/assets/image (4).png" alt="" width="563"><figcaption></figcaption></figure>

Сгенерируйте API-ключи и сохраните их в текстовый файл.

<figure><img src="../../../.gitbook/assets/image (5).png" alt="" width="563"><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите Quixfer в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image.png" alt="" width="486"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1).png" alt="" width="460"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — Public Key из личного кабинета Quixfer, скопированный ранее

**Секретный ключ** — Private Key из личного кабинета Quixfer, скопированный ранее

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Способ оплаты** — выберите необходимый способ оплаты для приема средств или пункт "**Автоматически**" — в этом случае реквизиты будут запрашиваться согласно xml-коду валюты из направления обмена, где подключен мерчант (список методов будет отображаться только после указания корректного API-ключа для авторизации в модуле).

### Дополнительные поля

Для корректного получения реквизитов для валюты на прием, где используется Quixfer, необходимо добавить в форму обмена <mark style="color:red;">**обязательные**</mark> доп. поля. Под полем "**Способ оплаты**" отображается подсказка по необходимым полям для каждого метода оплаты.

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).\
