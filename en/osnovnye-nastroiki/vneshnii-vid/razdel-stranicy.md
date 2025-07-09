# "Pages" Section

## Basic Pages

In this section, you create and edit the pages you want to display on your website. By default, most of the standard pages for the exchanger are already created — you can edit these if you wish or add new pages. Various formatting options can be applied to the text on the pages you create.

Here is a list of all the default pages created:

<figure><img src="../../.gitbook/assets/image (1227).png" alt=""><figcaption></figcaption></figure>

Please note that the content of the site’s basic pages is not edited through the admin panel. The text for these pages is loaded from the source code via the shortcode specified in the "**Text**" field. For these pages, you can only add additional text through this field or edit the text directly in the code:

<figure><img src="../../.gitbook/assets/изображение.png" alt=""><figcaption></figcaption></figure>

<details>

<summary>List of all basic pages and their shortcodes</summary>

- Authorization — \[login_page]
- Your Transactions — \[userxch]
- Your Wallets — \[userwallets]
- Account Verification — \[userverify]
- Wallet Verification — \[walletsverify]
- Internal Account — \[domacc_page]
- Password Recovery — \[lostpass_page]
- Partner Payouts — \[payouts_page]
- Home — \[home]
- Sitemap — \[sitemap]
- Contacts — \[contact_form]
- Personal Account — \[account_page]
- Security Settings — \[security_page]
- Exchange — \[exchange]
- Exchange Steps — \[exchangestep]
- Reviews — \[reviews_page]
- Partner Exchanges — \[pexch_page]
- Partner Referrals — \[plinks_page]
- Partner Account — \[paccount_page]
- Registration — \[register_page]
- Promotional Materials — \[promotional_page]
- Referrals — \[preferals_page]
- Rates — \[tarifs]
- API — \[user_api]

</details>

## Editing a Page

Page in edit mode:

<figure><img src="../../.gitbook/assets/image (1596).png" alt=""><figcaption></figcaption></figure>

Examples of text formatting on a page:

{% tabs %}
{% tab title="Visual Mode" %}
<figure><img src="../../.gitbook/assets/image (1597).png" alt="" width="289"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (846).png" alt=""><figcaption></figcaption></figure>

Here is a natural English translation of the provided text:

---

* Bold text — click the **B** icon when the text is selected:  
  **Bold text**

* Italic — click the _**I**_ icon when the text is selected:  
  _Italic text_

* Underlined text — click the **U** icon when the text is selected:  
  T̲e̲x̲t̲ ̲w̲i̲t̲h̲ ̲u̲n̲d̲e̲r̲l̲i̲n̲e̲

* Quoting text — click the ❝ icon when the text is selected:

> quoted text

* Collapsible content block:  
  \[`toggle title="Why rent a script if I can buy it from you?"]Indeed, buying once is cheaper than paying rent every month. However, the upfront cost when purchasing is quite high.[/toggle]`

<details>

<summary>Why rent a script if I can buy it from you?</summary>

Indeed, buying once is cheaper than paying rent every month. However, the upfront cost when purchasing is quite high.

</details>
{% endtab %}

{% tab title="Mode: "Text"" %}
<figure><img src="../../.gitbook/assets/image (563).png" alt="" width="206"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (564).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

To ensure pages display correctly on the website, you need to assign the appropriate attributes to them:

<figure><img src="../../.gitbook/assets/image (566).png" alt="" width="440"><figcaption></figcaption></figure>

{% hint style="warning" %}
We recommend not changing the technical pages for the basic pages — doing so may cause pages to display incorrectly on the site.

The two main technical pages — "**Home**" and "**News**" — should not be edited; it’s best to use them as they are.

&#x20;![](<../../.gitbook/assets/image (1599).png>)![](<../../.gitbook/assets/image (1600).png>)
{% endhint %}

**Parent** — the page under which the page you are editing will be "nested." The parent page is at the top level, and child pages are nested beneath it at subsequent levels.

For example, you can make the **Currencies** page a parent page, with **Ethereum** and **Bitcoin** as child pages beneath it. Under the **Bitcoin** page, you could have another page called **Wrapped Bitcoin**. The URLs might look like this:

* https://exchanger.com/currencies/  
* https://exchanger.com/currencies/eth/  
* https://exchanger.com/currencies/btc/  
* https://exchanger.com/currencies/btc/wbtc/

---

If you need the translation adapted for a specific style or audience, just let me know!

Here is a natural English translation of the provided text:

---

A more detailed explanation of this option can be found in the [official WordPress documentation](https://wordpress.com/ru/support/pages/page-options/).

If you do not plan to use a nested page structure, select "**No Parent**."

<figure><img src="../../.gitbook/assets/image (156).png" alt="" width="236"><figcaption></figcaption></figure>

**Template:**

<figure><img src="../../.gitbook/assets/image (565).png" alt="" width="241"><figcaption></figcaption></figure>

* **Default Template** — the optimal choice for displaying most pages on the site.
* **Home Page Template** — used **only** for the site’s homepage (when this option is selected, the page will be marked as "**Homepage**" in the general pages list, and on the live site, the page will display a table of exchange directions regardless of any shortcode or text set in the page settings).

<figure><img src="../../.gitbook/assets/image (568).png" alt="" width="330"><figcaption></figcaption></figure>

* **Page Template Without Sidebar** — displays the page without a sidebar for the user account area.

<figure><img src="../../.gitbook/assets/image (569).png" alt="" width="563"><figcaption></figcaption></figure>

* **Plugin Page Template** — displays the page with a sidebar.

<figure><img src="../../.gitbook/assets/image (570).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (567).png" alt="" width="456"><figcaption></figcaption></figure>

**Technical Page** — select from the dropdown the base page that will be used for the page you are editing, and the link that will appear in the pages list within the user account area.

The number of technical pages is limited to the list provided. Only one site page can be assigned to each technical page.

<details>

<summary>Example of Using Technical Pages</summary>

Using a technical page for a suitable page (the link name is taken from the title of the edited page):

<img src="../../.gitbook/assets/image (571).png" alt="" data-size="original">

Using a technical page for an unsuitable page:

![](<../../.gitbook/assets/image (1598).png>)

Technical page not used:

![](<../../.gitbook/assets/image (574).png>)

</details>

If needed, you can also change the URLs of all pages **except the homepage**:

<figure><img src="../../.gitbook/assets/изображение (147).png" alt=""><figcaption></figcaption></figure>

---

Let me know if you need the images’ captions or any additional context adapted!