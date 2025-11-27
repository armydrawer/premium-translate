# Paycore

{% hint style="danger" %}
Перед настройкой автовыплат обязательно прочитайте [предупреждение о рисках!](https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/avtovyplaty/preduprezhdenie-o-riskakh)
{% endhint %}

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представителем сервиса](https://t.me/Paycore_pw).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, пожалуйста, самостоятельно оценивайте возможные риски сотрудничества.
{% endhint %}

Зарегистрируйтесь на сервисе [Paycore](https://paycore.pw/) с помощью [представителя сервиса](https://t.me/Paycore_pw).

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить автовыплату".**

Выберите Paycore в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2245).png" alt=""><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**API ключ** — API ключ, выданный вам представителем Paycore

## Особые поля

В инструкции в модуле автовыплаты обязательно добавьте шорткод "**Ссылка на оплату**" — это необходимо для отображения ссылки в заявке, по которой будет переходить клиент для выбора метода получения им средств и банка на платежной странице сервиса.

<figure><img src="../../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

Также обязательно отметьте статус "**Ожидание подтверждения от модуля автовыплат**" в разделе "**Настройки обменника**" ➔ "**Настройки статуса**" — это необходимо для корректной работы модуля автовыплаты (если раздел не отображается в боковой панели — активируйте модуль "**Профессиональная настройка статусов**" в разделе "**Модули**", а затем проведите указанную настройку).

<figure><img src="../../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
