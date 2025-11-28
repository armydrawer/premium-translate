# General Module Settings

The module includes settings that only need to be configured once to ensure proper operation moving forward.

Go to the "**Trading Actions" -> "Settings"** section and configure the settings as shown in the screenshot below.

### **Hash for cron files**

Setting a hash makes the cron URL more unique, which enhances security. We recommend using a hash that is at least 20 characters long and includes Latin letters and numbers. Example hash:\
`ImYkwGsq2fjhuWypiasq2fNasq2fdQJzVvCpiasq2fdQJzVvCpis8umbxs8umbx`

### **Number of actions per run**

The maximum number of actions that will be executed in a single task.

### **Number of requests per action**

The maximum number of requests that will be processed in a single action.

### **Logging trading actions**

Logs the execution of trading actions:\
• **Yes**\
• **No**

### **Logging trading scripts**

Logs API requests to the exchange and their responses:\
• **Yes**\
• **No**

### **Execute action immediately:**

• **Yes** — The action will trigger **when the request status is manually changed in the admin panel or by the merchant to "accepted" or "auto-payout."**\
• **No** — The action will trigger **via a cron job.**\
• **Yes, if not in the admin panel** — The action will trigger **when the request status is changed by the merchant to "accepted" or "auto-payout."**

### **Save trading information**

Saves data about trading actions after they are executed:\
• **Yes**\
• **No**

{% hint style="warning" %}
Make sure to create [cron jobs](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere) on the server for the statuses where you plan to use trading actions.

<img src="../../../.gitbook/assets/image (569) (1).png" alt="" data-size="original">
{% endhint %}
