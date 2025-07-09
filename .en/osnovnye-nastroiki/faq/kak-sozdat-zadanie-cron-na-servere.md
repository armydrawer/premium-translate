# How to Create a Cron Job on the Server

{% hint style="info" %}
Cron jobs are set up on the server to perform regular tasks automatically. For example, checking payment statuses, updating currency rates for a parser, and so on.
{% endhint %}

If you are using the ISP Manager control panel, follow these steps:

1. Copy the cron URL from the section where you want to automate actions (such as payment checks, rate parsing, etc.).
2. In ISP Manager, go to the "**CRON Scheduler**" section and click the "**Create Job**" button:

{% hint style="danger" %}
All cron jobs must be created under the user account assigned to the website (do **not** create them as the root user).
{% endhint %}

<figure><img src="../../.gitbook/assets/изображение (124).png" alt="" width="563"><figcaption></figcaption></figure>

3. On the new page, fill in the details for the cron job:

<figure><img src="../../.gitbook/assets/image (1314).png" alt="" width="473"><figcaption></figcaption></figure>

- **Email address** — specify the email where error reports for the job execution will be sent (this option works only if outgoing mail is configured in ISP Manager under "**Settings** -> **Notifications**").
- **Command** — the full command to execute (see example below).
- **Description** — a brief description of the job (optional).
- **Enabled checkbox** — the job’s active status.
- **Schedule** — select "Expert mode" and set all the fields below to "\*" (asterisk) to run the job every minute.
- **"Do not send report to email" checkbox** — uncheck this box if you want to receive emails about the job’s execution and errors.

{% hint style="warning" %}
Please note that the exact command format may vary depending on your server, but in most cases, the following format works:

**`/usr/bin/wget -t 1 -O - --no-check-certificate "your_URL"`**

For example, if your URL is **`https://site.com/cron-bestchangeapi_upload_data.html`**, the command should be:

**`/usr/bin/wget -t 1 -O - --no-check-certificate "https://site.com/cron-bestchangeapi_upload_data.html"`**

Cron job URLs can be found in the relevant sections (a few examples):

* Parsers 2.0 — Settings

![](<../../.gitbook/assets/image (1944).png>)

* Bestchange parser — Settings



The text translates to:

- module of merchants and automatic payouts