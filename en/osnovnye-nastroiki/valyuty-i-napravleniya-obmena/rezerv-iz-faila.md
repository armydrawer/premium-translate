# Reserve from a File

The script allows you to set the reserve amount for a currency by reading it from a file. You can create a text file containing the reserve values, which will then be displayed on the website as the currency reserves.

1. In the website control panel, go to **Modules → Modules** and activate the module called **Reserve Parser from File**.

<figure><img src="../../../.gitbook/assets/image (1008).png" alt=""><figcaption></figcaption></figure>

2. Create a TXT file and enter the currency reserves in it. Specify each reserve value on a new line. Upload this TXT file to your server. Example lines in the reserve file:

```
Reserv 1 = 100000
Reserv 2 = 5000
Reserv 3 = 14000
```

3. In the control panel, navigate to **Modules → Reserve from File** and enter the URL of the uploaded TXT file.

<figure><img src="../../../.gitbook/assets/image (1073).png" alt=""><figcaption></figcaption></figure>

4. In the control panel under **Currencies**, edit the desired currency and select the corresponding line number from the file for the **Currency Reserve** parameter. Save your changes.

<figure><img src="../../../.gitbook/assets/image (909).png" alt=""><figcaption></figcaption></figure>

Alternatively, in the **Exchange Directions** section on the **Reserve** tab, you can select the corresponding line number from the file. This way, you can assign individual reserve values for each exchange direction.

<figure><img src="../../../.gitbook/assets/image (906).png" alt=""><figcaption></figcaption></figure>

5. Set up a scheduled task (cron job) to fetch the reserve values from the file and update them on the website. The script can be run every minute. Here is an example command for a Unix-based scheduler using ISP Manager:

```
/usr/bin/wget -t 1 -O - http(s)://your_domain/request-fres.html
```

{% hint style="info" %}
The exact command may vary depending on your server. Changes usually affect the `/usr/bin/wget -t 1 -O -` part. Please check with your hosting provider’s technical support to get the correct command.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1102).png" alt="" width="563"><figcaption></figcaption></figure>

Now, the currency reserve value on your website will always be taken from the TXT file.