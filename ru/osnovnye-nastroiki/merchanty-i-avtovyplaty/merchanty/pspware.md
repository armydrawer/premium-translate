---
hidden: true
noIndex: true
---

# PSPWare

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/obnovlenie-failov-skripta-na-servere/kak-obnovit-faily-na-servere#moduli-merchantov-i-avtovyplat)
{% endhint %}

{% hint style="warning" %}
Для обсуждения условий и подключения свяжитесь с [представителем сервиса](https://t.me/pspware_ceo)

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" ➔ "**Добавить мерчант".**

Выберите PSPWare в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (2157).png" alt="" width="410"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (2154).png" alt="" width="464"><figcaption></figcaption></figure>

**Домен** — оставьте поле пустым

**ID мерчанта** — ID, выданный вам представителем PSPWare

**API ключ** — ключ, выданный вам представителем PSPWare

## Особые поля

<figure><img src="../../../.gitbook/assets/image (2155).png" alt=""><figcaption></figcaption></figure>

**СБП** — выдача номера телефона для оплаты через СБП вместо реквизитов карты в заявках

{% hint style="warning" %}
Обратите внимание, что вам также необходимо переслать URL для работы Webhook из настроек модуля представителю сервиса с просьбой установить его для вас. Без установки указанного URL заявки с недоплатой/переплатой **не будут менять свои статусы**!

<img src="../../../.gitbook/assets/image (2156).png" alt="" data-size="original">
{% endhint %}

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
