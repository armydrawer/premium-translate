---
hidden: true
noIndex: true
noRobotsIndex: true
---

# Payin-Payout (неактивно)

{% hint style="info" %}
Если вам необходимо обновить модуль на сервере — воспользуйтесь [инструкцией](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-obnovit-faily-na-servere#moduli-merchantov)
{% endhint %}

## Настройки в личном кабинете мерчанта

{% hint style="warning" %}
Для обсуждения условий и подключения, свяжитесь с [представитлем сервиса](https://t.me/Payin_payoutt).

**Дисклеймер**: при подключении вашего сайта к тому или иному сервису, самостоятельно пожалуйста оценивайте возможные риски сотрудничества.
{% endhint %}

Для настройки модуля требуется [создать магазин в ЛК мерчанта](https://lk.payin-payout.net/app/#/shops/add). Укажите имя магазина, выберите пункт "**Онлайн магазин**" и нажмите на кнопку "**Создать магазин**".

<figure><img src="../../../.gitbook/assets/image (519).png" alt="" width="563"><figcaption></figcaption></figure>

Заполните данные магазина и сохраните их. Пройдите верификацию аккаунта и созданного магазина.

<figure><img src="../../../.gitbook/assets/image (520).png" alt="" width="563"><figcaption></figcaption></figure>

После создания магазина скопируйте данные из строк "**AgentId**" и "**Ключ**".

<figure><img src="../../../.gitbook/assets/image (516).png" alt=""><figcaption></figcaption></figure>

## Настройки модуля

В панели администратора создайте нового мерчанта в разделе "**Мерчанты**" -> "**Добавить мерчант".**

Выберите Payin-Payout в выпадающем списке в поле "**Модуль**", укажите название для модуля и нажмите "**Сохранить**".

<figure><img src="../../../.gitbook/assets/image (1858).png" alt="" width="426"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1859).png" alt="" width="425"><figcaption></figcaption></figure>

**Agent ID** — ID, отображающийся на карточке магазина

**Ключ** — ключ, отображающийся на карточке магазина

{% hint style="warning" %}
**Обязательно** укажите URL из строки "**Callback URL**" из настроек модуля:

![](<../../../.gitbook/assets/image (518).png>)

в настройках магазина в ЛК мерчанта:\
![](<../../../.gitbook/assets/image (522).png>)\
![](<../../../.gitbook/assets/image (523).png>)\
Также необходимо добавить IP-адрес мерчанта в вайтлист в ЛК Cloudflare/DDos-Guard или другого используемого вами сервиса (IP-адрес запрашивается непосредственно у мерчанта).
{% endhint %}

## Особые поля

**Способ оплаты** — выберите из выпадающего списка подходящий способ оплаты

<figure><img src="../../../.gitbook/assets/image (1896).png" alt="" width="468"><figcaption></figcaption></figure>

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).<br>
