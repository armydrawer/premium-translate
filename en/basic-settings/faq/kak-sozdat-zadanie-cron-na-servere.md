# How to Create a Cron Job on a Server?

{% hint style="info" %}
Cron jobs are created on a server to automate recurring tasks. For example, checking payment statuses, updating exchange rates for parsers, and so on.
{% endhint %}

If you are using the ISP Manager server control panel, follow these steps:

1. Copy the cron link from the section for which you want to set up automated actions (e.g., payment checks, exchange rate parsing, etc.).
2. In the ISP Manager panel, navigate to the "**CRON Scheduler**" section and click the "**Create Job**" button:

{% hint style="danger" %}
All cron jobs must be created under the user account associated with the website **(not under the root user account)**.
{% endhint %}

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(124)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

3. On the new page, fill in the details for the cron job:

<figure><img src="../../.gitbook/assets/image%20(1314)_eng.png" alt="" width="473"><figcaption></figcaption></figure>

* **Email Address** — Enter the email address where error notifications for the job will be sent (this option works only if outgoing mail is configured in ISP Manager under "**Settings** -> **Notifications**").
* **Command** — The full command to execute (example provided below).
* **Description** — A brief description of the job (optional field).
* **"Enabled" Checkbox** — The status of the job.
* **Schedule** — Select "Expert Mode" and set all fields below to "\*" (asterisk) for the job to run every minute.
* **"Do Not Send Report to Email" Checkbox** — Uncheck this box if you want to receive email notifications about the job's execution and errors.

{% hint style="warning" %}
Note that the command format may vary slightly depending on the server, but in most cases, the format provided below will suffice:

**`/usr/bin/wget -t 1 -O - --no-check-certificate "your_URL"`**

For example, if your URL is **`https://site.com/cron-bestchangeapi_upload_data.html`**,\
the command should look like this:\
&#xNAN;**`/usr/bin/wget -t 1 -O - --no-check-certificate "https://site.com/cron-bestchangeapi_upload_data.html"`**

Cron job links can be found in the corresponding sections. Here are a few examples:

* Parsers 2.0 — Settings\
  ![](../../.gitbook/assets/image%20\(1944\)_eng.png)
* Bestchange Parser — Settings\
  ![](../../.gitbook/assets/image%20\(1945\)_eng.png)
* Merchant and Auto-Payout Modules\
  ![](../../.gitbook/assets/image%20\(1946\)_eng.png)
{% endhint %}
