# Adding IP Addresses to the Whitelist in Cloudflare

1. Log in to your [Cloudflare dashboard](https://dash.cloudflare.com/).
2. In the "**Account Home**" section, click on the domain name for which you want to create an IP address whitelist.

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

3. Navigate to "**Security**" ➔ **"Security rules"** ➔ click the **"Create rule"** button ➔ select "**IP access rules**."

<figure><img src="../../.gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

4. Specify the IP address, range of addresses, country, or [ASN (**Autonomous System Number**)](https://blog.browserscan.net/ru/docs/what-is-an-asn) (used for specific organizations) that you want to whitelist. Then, choose the action to apply to the specified object—allow access, block access, or display a CAPTCHA for requests from the specified IP range. Next, select your site in the "**Zone**" field and save the rule by clicking the "**Create**" button.

<figure><img src="../../.gitbook/assets/image (3).png" alt=""><figcaption></figcaption></figure>

The created rule will appear in the list of all rules.

<figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>

## Using ASN

When adding rules by **ASN** instead of an IP address range (for example, in the case of Telegram), you can search for the ASN associated with the desired IP address. To do this, find the ASN (there may be several) associated with the IP address (e.g., 91.108.6.73) using [Cloudflare's Radar service](https://radar.cloudflare.com/ip).

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

**Telegram's ASN**: **AS44907, AS59930, AS62014, AS62041, AS211157** — these need to be added as separate rules in the "**Security**" ➔ **"Security rules"** section:

<figure><img src="../../.gitbook/assets/image (6).png" alt=""><figcaption></figcaption></figure>

The created rules will be displayed in the list of rules.

<figure><img src="../../.gitbook/assets/image (2233).png" alt=""><figcaption></figcaption></figure>