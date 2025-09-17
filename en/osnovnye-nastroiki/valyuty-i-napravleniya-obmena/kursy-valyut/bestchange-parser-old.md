# BestChange Parser (Old Version)

{% hint style="danger" %}
To enable automatic currency rate updates, it is **mandatory** to create a [Cron job](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) on your server using the link provided in the "**BestChange Parser**" → "**Settings**" section.

![](<../../../.gitbook/assets/image (1482).png>)
{% endhint %}

{% hint style="info" %}
For the module to function correctly, the PHP extension **zip** is required.
{% endhint %}

{% hint style="warning" %}
Please note that using the BestChange parser does not guarantee your exchanger will appear in the BestChange list at the position you specify in the parser settings.

The module is available to all exchangers using the Premium Exchanger script — meaning your competitors can configure the parser just like you. As a result, all exchangers using the parser will compete for the specified position (most often the 1st position) in the selected exchange direction.

The only guaranteed way to secure the top position is through **constant undercutting**.

Additionally, you can configure minimum and maximum rates using the provided instructions to avoid accidental losses if another exchanger decides to undercut (this could pull your rates down if you’ve tied them to the top position and haven’t set min/max rate limits).
{% endhint %}

{% hint style="warning" %}
The hash for the Cron job link is set in the file **`wp-content/plugins/premiumbox/userdata.php`**.

![](<../../../.gitbook/assets/image (1520).png>)![](<../../../.gitbook/assets/image (1521).png>)
{% endhint %}

{% hint style="danger" %}
The BestChange parser will only work for active exchange directions. When configuring the parser, make sure to activate the desired exchange direction before proceeding.

<img src="../../../.gitbook/assets/image (733).png" alt="" data-size="original">
{% endhint %}

{% embed url="https://www.youtube.com/watch?v=epK0sO_84zc" %}

### Step-by-Step Instructions:

1. In the "**Modules**" → "**Modules**" section, activate the "**BestChange Parser**" module. To activate, hover over the merchant name and click the "**Activate**" link.

2. In the "**BestChange Parser**" → "**Settings**" section, enter the ID of your exchanger (provided by BestChange) in the "**Blacklist exchanger IDs (comma-separated)**" field. If your exchanger is not listed on BestChange, leave this field empty and save the changes. Then, in the same section, follow the link labeled "**Cron URL for updating rates in the BestChange Parser module**."

<figure><img src="../../../.gitbook/assets/image (897).png" alt=""><figcaption></figcaption></figure>

<details>
<summary>How to find your exchanger ID?</summary>

Click the image below to see how to locate your exchanger ID on the BestChange website.

<img src="../../../.gitbook/assets/Clip2net_230726151417.png" alt="" data-size="original">
</details>

If needed, you can specify exchanger IDs to include in the "**Whitelist exchanger IDs (comma-separated)**" field. Only these exchangers will be considered when parsing rates. If left empty, rates from all exchangers will be considered.

3. In the "**BestChange Parser**" → "**Settings**" section of the admin panel, refresh the page to see the list of available currencies. Check the currencies you plan to use and save the changes.

<figure><img src="../../../.gitbook/assets/image (1034).png" alt=""><figcaption></figcaption></figure>

4. In the "**Exchange Directions**" → "**Exchange Directions**" section of the admin panel, edit the desired exchange direction.

5. In the "**Rate Auto-Adjustment**" tab, disable any active rate auto-adjustments before configuring the BestChange parser.

<figure><img src="../../../.gitbook/assets/image (1215).png" alt=""><figcaption></figcaption></figure>

In the "**BestChange Parser**" tab, you’ll find the configuration block. Complete the necessary settings:

<figure><img src="../../../.gitbook/assets/image (1044).png" alt=""><figcaption></figcaption></figure>

- Use the "**Enable Parser**" option to activate the parser (the parser will only work if currencies are selected in the next step).
- In the "**Currencies (You Give)**" and "**Currencies (You Receive)**" dropdown menus, select the exchange direction you want to use as the source for parsing.
- In the "**Position**" field, specify the monitoring position number you want your rate to match.

{% hint style="info" %}
For example, you can specify **1-6**, which will calculate the average rate of the top 6 positions.
{% endhint %}

- In the "**Min. Reserve for Position**" field, specify the minimum reserve value for the position (currency "**You Receive**"). Exchangers with reserves below this value will be ignored by the module.
- In the "**Step**" field, specify the value (e.g., 0.0001) by which the rate will be adjusted. By default, the system always makes your rate more favorable than the specified position’s rate. You can also set the step as a percentage (e.g., 3%). A negative step value will make your rate less favorable (e.g., -0.00001 or -3%). Multiplication and division are also supported (e.g., \*2 or /2, \*3% or /3%).
- Use the "**Min. Rate**" and "**Max. Rate**" fields to set the range within which the position-based rate adjustment will operate. If the competitor’s rate for the specified position falls outside this range, the module will reset your rate to the standard rate. Min. and max. rates can also be tied to the rate source. The "**Add to Rate**" field allows you to adjust the rate from the source (e.g., add 3% or subtract -3%).
- The "**Reset to Standard Rate**" option allows you to reset to the standard rate when necessary. This reset occurs when the competitor’s rate reaches the specified minimum or maximum value.
- In the "**Standard Rate**" field, specify the standard rate to which the system will reset.
- In the "**Rate Auto-Adjustment**" field, you can configure auto-adjustments for the standard rate to ensure it remains up-to-date for the exchange direction.
- The "**Add to Rate**" field can also be used to adjust the rate from the source (e.g., add 3% or subtract -3%).

Similar settings for exchange directions can also be configured in the "**BestChange Parser**" → "**Add Adjustment**" section of the admin panel.

<figure><img src="../../../.gitbook/assets/image (852).png" alt=""><figcaption></figcaption></figure>

6. Add a Cron job in the [task scheduler](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-sozdat-zadanie-cron-na-servere) to update currency rates. The script can be set to run every minute. Below is an example of a Unix-format command for the ISP Manager control panel:

<figure><img src="../../../.gitbook/assets/image (1339).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
The command format may vary depending on your server. The differences typically involve the **`/usr/bin/wget -t 1 -O - --no-check-certificate`** part of the command.

You can contact your hosting provider’s technical support to confirm the correct command for your server.
{% endhint %}