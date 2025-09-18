# Email Notifications

The site can send emails using the standard phpmailer function, which is built into the WordPress CMS.

{% hint style="warning" %}
Free accounts on mail.ru and yandex.ru may not work correctly or may not send emails to recipients at all.

For reliable email delivery, we recommend using paid email accounts from services such as [360.yandex.ru](https://360.yandex.ru/), [biz.mail.ru](https://biz.mail.ru/), [Postmark](https://postmarkapp.com/), or [Zeptomail](https://www.zoho.com/zeptomail/).
{% endhint %}

{% hint style="danger" %}
Please note that the templates for **administrators** and **users** in the dropdown menu are separate entities and can be configured independently of each other (items in the dropdown menu).

![](<../../.gitbook/assets/image (785).png>)![](<../../.gitbook/assets/image (786).png>)
{% endhint %}

## Basic Settings

In the site management panel, go to the "**Messages" → "Email Templates"** section and configure the module:

<figure><img src="../../.gitbook/assets/image (1226).png" alt="" width="489"><figcaption></figcaption></figure>

* **Sender Email** — the email address from which the email will be sent. This must be an existing address within your domain, such as support@your_domain.ru. Otherwise, emails may not be sent or may end up in spam. You can create such an email address in your server's control panel.
* **Sender Name** — the name of the site from which the email will be sent. If this field is left blank, emails may not be sent or may end up in users' spam folders.
* **Administrator Email** — the email address from which emails will be sent on behalf of the administrator.

## SMTP Configuration

{% hint style="warning" %}
We highly recommend using SMTP for sending emails, as without it, the recipient will know your server's IP address, which could lead to DoS/DDoS attacks if the recipient is a malicious actor.
{% endhint %}

Set up email sending via an external SMTP service. One such service could be Yandex.Mail or another email service that provides SMTP functionality.

Configure SMTP for the module:

<figure><img src="../../.gitbook/assets/image (1183).png" alt="" width="490"><figcaption></figcaption></figure>

{% hint style="warning" %}
Do not use your server's SMTP settings — use the SMTP settings of email services like Yandex, Mail.ru, or Google.
{% endhint %}

In the "**Messages" → "Email Templates"** section, you will find the following settings:

* **Enable SMTP:**\
  • "**Yes**" — activate SMTP (all emails from the site will be sent using SMTP).\
  • "**No**" — SMTP will be disabled.
* **SMTP Connection Type** — typically, the "**SSL**" connection type is used.
* **SMTP Host** — the address of the SMTP server. Each email service has a unique address. For Yandex.Mail, the address is `smtp.yandex.ru`, and for Mail.ru, it is `smtp.mail.ru`.
* **SMTP Port** — the port of the SMTP server. Each email service has its own port. For Yandex.Mail and Mail.ru, use port 465.
* **SMTP Username** — the address of the registered email account, for example, `premiumexchanger@yandex.ru`.
* **SMTP Password** — a special password for the email account.

{% hint style="warning" %}
To use the "**SMTP Password**" option, you need to create an app password if you are using popular email services:

* [Instructions for Mail.ru](https://help.mail.ru/mail/security/protection/external)
* [Instructions for Yandex.Mail](https://yandex.ru/support/id/authorization/app-passwords.html)
* [Instructions for Zoho](https://www.zoho.com/mail/help/adminconsole/two-factor-authentication.html#alink5)
{% endhint %}

After entering the settings, click the "**Save**" button. On the page, you will find a form to send a test email to check the correctness of the email sending settings.

<figure><img src="../../.gitbook/assets/image (1098).png" alt="" width="499"><figcaption></figcaption></figure>

## Email Template Configuration

{% embed url="https://youtu.be/g_YcR3FqPi0" %}

{% hint style="warning" %}
Once again, we emphasize that the templates for **administrators** and **users** in the dropdown menu are separate entities and can be configured independently of each other (items in the dropdown menu).\
![](<../../.gitbook/assets/image (785).png>)![](<../../.gitbook/assets/image (786).png>)
{% endhint %}

After you have configured email sending, set up the necessary templates for various application statuses and other options for sending messages from the site to administrators and users:

<figure><img src="../../.gitbook/assets/image (1095).png" alt=""><figcaption></figcaption></figure>

* **Send Email:**\
  • "**Yes**" — the email will be sent.\
  • "**No**" — the email will not be sent.
* **Email Subject** — specify the subject of the email.
* **Sender Email** — the email address from which the email will be sent.
* **Sender Name** — the name of the site from which the email will be sent.
* **Administrator Email** — the administrator's email address where they want to receive this email. You can specify multiple addresses separated by commas.
* **Email Body** — the text of the email. Above the text input field, you will find a panel with \[shortcodes]. Use them in the email template to display data from the applications in the sent emails.

## Troubleshooting

If you suspect that the option is not working correctly, go to the "**Email Logs**" section and check for any potential issues.

<figure><img src="../../.gitbook/assets/image (941).png" alt=""><figcaption></figcaption></figure>

If you are experiencing issues with message delivery and there are no obvious reasons for it, we recommend taking the following steps:

* Contact your hosting provider and check if they are blocking email sending. There may be server restrictions (for example, [relay](https://korporativnaya-pochta.com/articles/smart-relay-zaschita-ot-spama-dlya-korporativnoy-pochty)) that are preventing email delivery.
* Change the subject of the email sent for the "New Application" status to something less formal. It’s possible that a filter on the SMTP server is being triggered, blocking delivery. Try using a less formal subject to avoid filtering.

If emails are only being received by some users or are going to the "Spam" folder, check for the presence of [SPF and/or DKIM records](https://neuropassenger.ru/dostavlyaemost-pisem/) for your domain and configure them if necessary.

* [Check SPF Record](https://mxtoolbox.com/spf.aspx)
* [Check DKIM Record](https://mxtoolbox.com/dkim.aspx)