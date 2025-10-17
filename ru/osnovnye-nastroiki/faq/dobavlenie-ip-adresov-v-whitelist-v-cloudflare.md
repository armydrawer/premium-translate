# Добавление IP-адресов в whitelist в Cloudflare

1. Зайдите в личный кабинет [Cloudflare](https://dash.cloudflare.com/).
2. В разделе "**Account Home**" кликните по названию домена, для которого хотите создать белый список (whitelist) IP-адресов.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

3. Перейдите в раздел "**Security"** ➔ **"Security rules"** ➔ кнопка **"Create rule"** ➔ "**IP access rules**".

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Укажите конкретный IP-адрес/диапазон адресов/страну, к которой относятся IP-адреса или [ASN (**autonomous system number**)](https://blog.browserscan.net/ru/docs/what-is-an-asn) (когда речь идет о конкретной организации) и выберите действие, которое будет применяться к объекту - блокировать/разрешать доступ или создавать капчу, которая будет отображаться при доступе с IP-адреса из диапазона. Далее выберите ваш сайт в поле "**Zone**" и сохраните правило по кнопке "**Create**".

<figure><img src="../../.gitbook/assets/image (3) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Созданное правило будет отображаться в списке всех правил.

<figure><img src="../../.gitbook/assets/image (4) (1).png" alt=""><figcaption></figcaption></figure>

## Использование ASN

При добавлении по **ASN** вместо диапазона IP-адресов (в примере ниже это Telegram) используйте поиск по IP-адресу, относящемуся к искомой ASN. Для этого нужно найти ASN (их может быть несколько) по IP-адресам (к примеру, по 91.108.6.73) через [сервис Radar от Cloudflare](https://radar.cloudflare.com/ip).

<figure><img src="../../.gitbook/assets/image (5) (1).png" alt=""><figcaption></figcaption></figure>

**ASN** для Telegra&#x6D;**: AS44907, AS59930,** **AS62014, AS62041, AS211157** — их нужно добавить отдельными правилами в разделе "**Security"** ➔ **"Security rules":**

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

Созданные правила будут отображаться в разделе.

<figure><img src="../../.gitbook/assets/image (2233).png" alt=""><figcaption></figcaption></figure>
