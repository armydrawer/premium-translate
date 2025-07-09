# BestChange Parser (Old)

{% hint style="danger" %}
To automatically update currency rates, it is **essential** to create a [Cron job](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link found in the "**BestChange Parser**" — "**Settings**" section.

![](<../../../.gitbook/assets/image (1482).png>)
{% endhint %}

{% hint style="info" %}
The module requires the PHP zip extension to function correctly.
{% endhint %}

{% hint style="warning" %}
Please note that using the BestChange parser does **not** guarantee you a spot in the exchanger list on BestChange at the position you specify in the parser settings.

This module is available to all exchangers using the Premium Exchanger script — your competitors can configure the parser just like you. Therefore, all exchangers using the parser will be competing for the same position (usually the 1st place) in the selected exchange direction.

The only way to guarantee the top spot is through **constant undercutting** (price dumping).

You can also set minimum and maximum rates following this guide to avoid accidentally going into a loss if another exchanger starts dumping prices (this will pull your rates down if you have chosen to tie your rates to the first place and haven’t set min/max rate limits).
{% endhint %}

{% hint style="warning" %}
The hash for the Cron job link is set in the file **`wp-content/plugins/premiumbox/userdata.php`**

![](<../../../.gitbook/assets/image (1520).png>)![](<../../../.gitbook/assets/image (1521).png>)
{% endhint %}

{% hint style="danger" %}
The BestChange parser will only work for an active exchange direction — be sure to activate the exchange direction before configuring the parser.
  
<img src="../../../.gitbook/assets/image (733).png" alt="" data-size="original">
{% endhint %}

{% embed url="https://www.youtube.com/watch?v=epK0sO_84zc" %}

Here is a natural, fluent English translation of the provided text:

---

1. In the "**Modules → Modules**" section, activate the "**BestChange parser**" module. To activate it, hover over the merchant’s name and click the "**Activate**" link.

2. In the "**BestChange parser → Settings**" section, enter the ID of your exchanger (as provided by the BestChange service) into the "**Blacklist of exchanger IDs (comma-separated)**" field. If your exchanger is not listed on BestChange, leave the "**Blacklist of exchanger IDs (comma-separated)**" field empty and save the changes. Then, in the same section, click the link "**Cron URL to update rates in the BestChange parser module**".

<figure><img src="../../../.gitbook/assets/image (897).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>How to find your exchanger ID?</summary>

Click the image below to see how to find your exchanger ID on the BestChange website.

<img src="../../../.gitbook/assets/Clip2net_230726151417.png" alt="" data-size="original">

</details>

If needed, you can specify exchanger IDs in the "**Whitelist of exchanger IDs (comma-separated)**" field on the BestChange website that should be considered when parsing rates. All other exchangers will be ignored. If this field is left empty, rates from all exchangers will be included during parsing.

3. In the control panel, under "**BestChange parser → Settings**," refresh the page to see the list of available currencies. Check the boxes next to the currencies you plan to use. Save your changes.

<figure><img src="../../../.gitbook/assets/image (1034).png" alt=""><figcaption></figcaption></figure>

4. In the control panel, go to "**Exchange Directions → Exchange Directions**" and open the exchange direction you want to edit.

5. On the "**Auto rate adjustment**" tab, before configuring the BestChange parser, disable any active auto rate adjustments if they are currently enabled.

<figure><img src="../../../.gitbook/assets/image (1215).png" alt=""><figcaption></figcaption></figure>

On the "**BestChange parser**" tab, you will see the settings block. Configure the necessary options:

<figure><img src="../../../.gitbook/assets/image (1044).png" alt=""><figcaption></figcaption></figure>

---

If you need any further help or clarification, feel free to ask!

* Use the "**Enable parser**" option to activate the parser (the parser will only work if currencies are selected in the next step).  
* Use the dropdown menus "**Currencies (You give)**" and "**Currencies (You receive)**" to select the exchange direction you want to use as the source for parsing.  
* In the "**Position**" field, specify the position number in the monitoring list to which you want to link your rate.

{% hint style="info" %}
You can also specify a range, for example, **1-6** — this will mean the average value among the first 6 positions.  
{% endhint %}

Here is a natural, fluent English translation of the provided text:

---

* In the "**Min. reserve for position**" field, you can specify the minimum reserve amount for the position (currency "**You receive**"). Exchange services with reserves below this value will be ignored by the module.  
* In the "**Step**" field, enter the value by which the rate will be adjusted (for example, 0.0001). By default, the system always sets your rate to be more favorable than the rate of the specified position. You can also specify the step as a percentage (for example, 3%). A negative step value will make your rate less favorable than the specified position’s rate (e.g., -0.00001 or -3%). Multiplication and division can also be used (e.g., *2 or /2, *3% or /3%).  
* In the "**Min. rate**" and "**Max. rate**" fields, you can set the minimum and maximum rate limits within which the position binding will operate. If a competitor’s rate for the specified position goes beyond these limits, the module will reset your rate to the standard rate. The min. and max. rates can be linked to a rate source. Using the "**Add to rate**" field, you can adjust the rate obtained from the source (for example, add 3% or subtract 3%).  
* The "**Reset to standard rate**" option allows you to reset to the standard rate when necessary. This reset occurs if the rate on your site reaches the specified minimum or maximum limit.  
* In the "**Standard rate**" field, specify the standard rate value to which the rate will be reset.  
* The "**Auto-correct rate**" option lets you set automatic adjustments for the standard rate, ensuring the standard rate is always up to date for the exchange direction.  
* Using the "**Add to rate**" field, you can fine-tune the rate obtained from the source (for example, add 3% or subtract 3%).  

Similar settings for the exchange direction can also be configured in the control panel under "**BestChange parser** → **Add adjustment**".

---

If you need the image caption or any additional formatting, please let me know!

6. Add a cron job in the [task scheduler](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) to update the currency exchange rates. The script can be set to run every minute. Here is an example of a Unix-format command for the ISP Manager control panel:

<figure><img src="../../../.gitbook/assets/image (1339).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The command may vary for different servers, especially the part **`/usr/bin/wget -t 1 -O - --no-check-certificate`**.

Please check with your hosting provider’s technical support to get the correct command for your server.
{% endhint %}