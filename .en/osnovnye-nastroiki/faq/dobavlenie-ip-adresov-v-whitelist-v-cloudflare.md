# Adding IP Addresses to the Whitelist in Cloudflare

1. Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/).
2. Under the **Websites** section, click on the domain name for which you want to create an IP whitelist.

<figure><img src="../../.gitbook/assets/Clip2net_230810205217.png" alt=""><figcaption></figcaption></figure>

3. Navigate to **Security -> WAF ->** the **"Custom rules"** tab, then click the **"Create rule"** button.

<figure><img src="../../.gitbook/assets/Clip2net_230810205421.png" alt=""><figcaption></figcaption></figure>

4. To allow an IP address or a range of IP addresses unrestricted access to your site (bypassing Cloudflare’s restrictions), configure the settings exactly as shown in the screenshot below:

{% hint style="warning" %}
In the "**Value**" field, be sure to click on the suggestion that appears as you type to select and apply the value correctly!

<img src="../../.gitbook/assets/Clip2net_230810204224.png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../.gitbook/assets/Clip2net_230810203657.png" alt=""><figcaption><p>Example of adding Telegram’s IP address range to the whitelist</p></figcaption></figure>

You can also add an **ASN (Autonomous System Number)** of an external service (in this example, Telegram) instead of specifying IP ranges. To find the ASN(s) associated with the service’s IP addresses (for example, 91.108.6.73), use the **Security Center** -> **Investigate** section.

<figure><img src="../../.gitbook/assets/image (1250).png" alt=""><figcaption></figcaption></figure>

**Telegram’s ASNs:** 62041, 211157 — these should be added as separate rules under **WAF -> Tools -> IP Access Rules:**

<figure><img src="../../.gitbook/assets/image (1253).png" alt=""><figcaption></figcaption></figure>

The created rules will then be displayed in this section.

<figure><img src="../../.gitbook/assets/image (1252).png" alt=""><figcaption></figcaption></figure>