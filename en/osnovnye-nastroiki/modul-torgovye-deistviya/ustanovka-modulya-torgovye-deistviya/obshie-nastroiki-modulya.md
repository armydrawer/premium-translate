# General Module Settings

The module has settings that only need to be configured once to ensure proper operation going forward.

Go to the "**Trading Actions** -> **Settings**" section and set the options as shown in the screenshot below.

<figure><img src="../../../.gitbook/assets/image (377).png" alt=""><figcaption></figcaption></figure>

**Hash for cron files** — Setting a hash makes the cron URL more unique, which enhances security. We recommend using a hash at least 20 characters long, containing Latin letters and numbers. Example hash: `ImYkwGsq2fjhuWypiasq2fNasq2fdQJzVvCpiasq2fdQJzVvCpis8umbxs8umbx`

**Number of actions per run** — the maximum number of actions that will be executed in a single task

**Number of requests per action** — the maximum number of requests that will be processed within one action

**Log trading actions** — enable logging of trading action executions  
• **Yes**  
• **No**

**Log trading scripts** — enable logging of API requests to the exchange and their responses  
• **Yes**  
• **No**

**Execute action immediately:**  
• **Yes** — the action will trigger **when the request status is changed manually in the admin panel or by the merchant upon acceptance/auto-payout**  
• **No** — the action will trigger **via the cron job**  
• **Yes, if not in admin panel** — the action will trigger **when the request status is changed by the merchant upon acceptance/auto-payout, but not when changed in the admin panel**

**Save trading information** — save data about trading actions after they are executed  
• **Yes**  
• **No**

{% hint style="warning" %}
Be sure to create [cron jobs](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on your server for the statuses where you plan to use trading actions.

![](<../../../.gitbook/assets/image (1512).png>)
{% endhint %}