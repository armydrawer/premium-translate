# Reserve from File

The script allows you to retrieve the reserve value for a currency from a file. You can create a text file to store the reserve values, which will then be displayed on the website as the currency reserve.

1. In the website control panel, go to the "**Modules" → "Modules"** section and activate the "**Reserve Parser from File**" module.

<figure><img src="../../../.gitbook/assets/image (1008).png" alt=""><figcaption></figcaption></figure>

2. Create a txt file and specify the currency reserves in it. List each reserve value on a new line. Upload the txt file to the server. Here’s an example of how the lines in the file should look:

`Reserve 1 = 100000`

`Reserve 2 = 5000`

`Reserve 3 = 14000`

3. In the website control panel, navigate to "**Modules" → "Reserve from File"** and enter the URL of the uploaded txt file.

<figure><img src="../../../.gitbook/assets/image (1073).png" alt=""><figcaption></figcaption></figure>

4. In the control panel, go to the "**Currencies**" section, edit the currency, and select the corresponding line number from the file for the "**Currency Reserve**" parameter. Save your changes.

<figure><img src="../../../.gitbook/assets/image (909).png" alt=""><figcaption></figcaption></figure>

Alternatively, in the "**Exchange Directions**" section, under the "**Reserve**" tab, you can select the corresponding line number from the file. This way, you can set an individual reserve value for each direction.

<figure><img src="../../../.gitbook/assets/image (906).png" alt=""><figcaption></figcaption></figure>

5. Set up a cron job to retrieve the reserve value from the file and update it on the website. The script can be run every minute. Here’s an example command for a cron job in Unix format for the ISP Manager control panel:

`/usr/bin/wget -t 1 -O - http(s)://your_domain/request-fres.html`

{% hint style="info" %}
The command may vary for each server. The changes pertain to this part of the command: `/usr/bin/wget -t 1 -O —`. You can confirm the correct command with your hosting provider's technical support.
{% endhint %}

<figure><img src="../../../.gitbook/assets/image (1102).png" alt="" width="563"><figcaption></figcaption></figure>

Now, the reserve value for the currency on the website will continuously be sourced from the txt file.