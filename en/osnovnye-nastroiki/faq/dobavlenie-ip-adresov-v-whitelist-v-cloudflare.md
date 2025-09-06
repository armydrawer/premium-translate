# Добавление IP-адресов в Whitelist в Cloudflare

1. Зайдите в личный кабинет [Cloudflare](https://dash.cloudflare.com/).
2. В разделе "**Websites**" кликните по названию домена, для которого хотите создать белый список (whitelist) IP-адресов.

<figure><img src="../../.gitbook/assets/Clip2net_230810205217.png" alt=""><figcaption></figcaption></figure>

3. Перейдите в раздел **Security -> WAF ->** вкладка **"Custom rules" ->** кнопка **"Create rule"**

<figure><img src="../../.gitbook/assets/Clip2net_230810205421.png" alt=""><figcaption></figcaption></figure>

4. Чтобы разрешить IP-адресу или диапазону IP-адресов доступ к вашему сайту без каких-либо ограничений со стороны Cloudflare, то **в точности задайте такие же настройки**, как указано на скриншоте ниже:

{% hint style="warning" %}
В поле "**Value**" кликайте именно по строке, которая появляется при вводе значения, чтобы это значение выбралось и применилось!

<img src="../../.gitbook/assets/Clip2net_230810204224.png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../.gitbook/assets/Clip2net_230810203657.png" alt=""><figcaption><p>Пример добавление в Whitelist пула IP адресов Telegram</p></figcaption></figure>

Также можно добавить **ASN (autonomous system number)** внешнего сервиса (в нашем примере это Telegram) вместо диапазона IP-адресов. Для этого нужно найти ASN (их может быть несколько) по IP-адресам (к примеру, 91.108.6.73), принадлежащим сервису, через раздел **Security Center** -> **Investigate.**

<figure><img src="../../.gitbook/assets/image (1309).png" alt=""><figcaption></figcaption></figure>

**ASN** для Telegra&#x6D;**: 62041, 211157** — их нужно добавить отдельными правилами в разделе **WAF -> Tools -> IP Access Rules:**

<figure><img src="../../.gitbook/assets/image (1312).png" alt=""><figcaption></figcaption></figure>

Созданные правила будут отображаться в разделе.

<figure><img src="../../.gitbook/assets/image (1311).png" alt=""><figcaption></figcaption></figure>
