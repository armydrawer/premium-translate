# BestChange Parser (Old)

{% hint style="danger" %}
To automatically update currency rates, **make sure to create a** [**Cron job**](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link from the "**BestChange Parser**" section — "**Settings**".

<img src="../../../.gitbook/assets/image (1482)_eng.png" alt="" data-size="original">
{% endhint %}

{% hint style="info" %}
The module requires the PHP extension: zip for proper functionality.
{% endhint %}

{% hint style="warning" %}
Please note that using the BestChange parser does not guarantee you a spot in the list of exchangers on BestChange as specified in the parser settings.

The module is available to all exchangers using the Premium Exchanger script — your competitors can set up the parser just like you, so all exchangers using the parser will compete for the specified position (usually the top spot) in the chosen exchange direction.

The only guaranteed way to secure the top position is through **constant undercutting**.

You can also configure minimum and maximum rates according to this guide to avoid going into the negative if another exchanger decides to undercut (this will pull you along if you have set the binding to the first position and haven't configured the min/max rates).
{% endhint %}

{% hint style="warning" %}
The hash for the Cron job link is set in the file **`wp-content/plugins/premiumbox/userdata.php`**.

<img src="../../../.gitbook/assets/image (577) (1).png" alt="" data-size="original"><img src="../../../.gitbook/assets/image (578) (1).png" alt="" data-size="original">
{% endhint %}

{% hint style="danger" %}
The BestChange parser will only work in the active exchange direction — make sure to set the direction to active before starting the parser configuration.

<img src="../../../.gitbook/assets/image (733) (1).png" alt="" data-size="original">
{% endhint %}

{% embed url="https://www.youtube.com/watch?v=epK0sO_84zc" %}

1. In the "**Modules" → "Modules"** section, activate the "**BestChange Parser**" module. To activate it, hover over the merchant's name and click the "**Activate**" link.
2. In the "**BestChange Parser" → "Settings"** section, enter your exchanger's ID provided by BestChange in the "**Blacklist of Exchanger IDs (comma-separated)**" field. If your exchanger is not listed on BestChange, leave the "**Blacklist of Exchanger IDs (comma-separated)**" field empty and save the changes. Then, in the same section, follow the link "**Cron URL for updating rates in the BestChange Parser module**".

<figure><img src="../../../.gitbook/assets/image (897) (1).png" alt=""><figcaption></figcaption></figure>

<details>

<summary>How to find the Exchanger ID?</summary>

Click on the image below to see how to find the Exchanger ID on the BestChange website.

<img src="../../../.gitbook/assets/Clip2net_230726151417 (1).png" alt="" data-size="original">

</details>

If necessary, in the "**Whitelist of Exchanger IDs (comma-separated)**" field, specify the IDs of the exchange points on the BestChange website that should be considered when parsing rates. Other exchange points will be ignored. If you leave this field empty, rates from all exchange points will be considered during parsing.

3. In the control panel under "**BestChange Parser" → "Settings"**, refresh the page to see the list of available currencies. Check the boxes for the currencies you plan to use. Save the changes.

<figure><img src="../../../.gitbook/assets/image (1034)_eng.png" alt=""><figcaption></figcaption></figure>

4. In the control panel under "**Exchange Directions" → "Exchange Directions"**, go to edit the exchange direction.
5. On the "**Auto-Correction of Rate**" tab, before starting the BestChange parser configuration, disable any active rate auto-corrections if such settings are in use.

<figure><img src="../../../.gitbook/assets/image (1215)_eng.png" alt=""><figcaption></figcaption></figure>

On the "**BestChange Parser**" tab, you will see a settings block. Make the necessary configurations:

<figure><img src="../../../.gitbook/assets/image (1044)_eng.png" alt=""><figcaption></figcaption></figure>

* Use the "**Enable Parser**" option to allow the parser to work (the parser will only function if currencies are selected in the next step).
* From the drop-down menus "**Currencies (You Give)**" and "**Currencies (You Receive)**", select the exchange direction you want to use as the source for parsing.
* In the "**Position**" field, specify the position number in the monitoring system to which you want to tie your rate.

{% hint style="info" %}
You can also specify, for example, **1-6** — this will mean the average value among the first 6 positions.
{% endhint %}

* In the "**Min. Reserve for Position**" field, you can specify the minimum reserve value for the position (currency "**You Receive**"). Exchangers with reserves below the specified value will be ignored by the module.
* In the "**Step**" field, specify a value (e.g., 0.0001) by which the rate will change. The system will always make your rate more favorable than the specified position's rate by default. You can also set the step as a percentage (e.g., 3%). A negative step value will make your rate less favorable than the specified position's rate (-0.00001 or -3%), and you can also use multiplication and division (\*2 or /2, \*3% or /3%).
* In the "**Min. Rate**" and "**Max. Rate**" fields, you can set the limits within which the binding to the position will operate. If a competitor for the specified position exceeds the minimum or maximum rate, the module will reset your rate to the standard one. The min. and max. rates can be tied to the source rates. The "**Add to Rate**" field can be used to adjust the rate obtained from the source (e.g., add 3% or subtract -3%).
* With the "**Reset to Standard Rate**" option, you can reset to the standard rate if necessary. The reset to the standard rate occurs when the specified minimum or maximum rate is reached on your site.
* In the "**Standard Rate**" field, specify the value of the standard rate to which the reset will occur.
* In the "**Auto-Correction of Rate**" field for the standard rate, you can set auto-correction to always have an up-to-date standard rate in the exchange direction.
* The "**Add to Rate**" field can also be used to adjust the rate obtained from the source (e.g., add 3% or subtract -3%).

Similar settings for the exchange direction can also be configured in the control panel under "**BestChange Parser" → "Add Adjustment"**.

<figure><img src="../../../.gitbook/assets/image (852) (1).png" alt=""><figcaption></figcaption></figure>

6. Add a cron job in the [task scheduler](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sozdat-zadanie-cron-na-servere) that will update the currency rates. The script can be run every minute. Here’s an example command for the task scheduler in Unix format for the ISP Manager control panel:

<figure><img src="../../../.gitbook/assets/image (544) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The command from the example may look different for each server. The changes pertain to the part of the command **`/usr/bin/wget -t 1 -O - --no-check-certificate`**.

You can confirm the correct command with your hosting provider's technical support.
{% endhint %}
