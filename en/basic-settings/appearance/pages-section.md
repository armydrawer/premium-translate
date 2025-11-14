# Pages Section

## Basic Pages

In this section, you can create and edit the pages you want to display on your website. By default, most standard pages for the exchange platform are already created. You can edit these existing pages or add new ones as needed. Various formatting options can be applied to the text on the created pages.

Here’s a list of all the default pages:

<figure><img src="../../.gitbook/assets/image (1227)_eng.png" alt=""><figcaption></figcaption></figure>

Please note that the content of the basic pages on the site cannot be edited through the admin panel. The text for these pages is loaded from the source code using the specified shortcode in the "**Text**" field. For these pages, you can only add additional text through this same field or edit the text directly in the code:

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5_eng.png" alt=""><figcaption></figcaption></figure>

<details>

<summary>List of all basic pages and their shortcodes</summary>

* Login — \[login\_page]
* Your Operations — \[userxch]
* Your Wallets — \[userwallets]
* Account Verification — \[userverify]
* Wallet Verification — \[walletsverify]
* Internal Account — \[domacc\_page]
* Password Recovery — \[lostpass\_page]
* Partner Payouts — \[payouts\_page]
* Home — \[home]
* Sitemap — \[sitemap]
* Contacts — \[contact\_form]
* Personal Account — \[account\_page]
* Security Settings — \[security\_page]
* Exchange — \[exchange]
* Exchange Steps — \[exchangestep]
* Reviews — \[reviews\_page]
* Partner Exchanges — \[pexch\_page]
* Partner Links — \[plinks\_page]
* Partner Account — \[paccount\_page]
* Registration — \[register\_page]
* Promotional Materials — \[promotional\_page]
* Referrals — \[preferals\_page]
* Tariffs — \[tarifs]
* API — \[user\_api]

</details>

## Editing a Page

Here’s what a page looks like in edit mode:

<figure><img src="../../../ru/.gitbook/assets/image (653) (1).png" alt=""><figcaption></figcaption></figure>

Examples of text formatting on the page:

{% tabs %}
{% tab title="Visual Mode" %}
<figure><img src="../../../ru/.gitbook/assets/image (654) (1).png" alt="" width="289"><figcaption></figcaption></figure>

<figure><img src="../../../ru/.gitbook/assets/image (846) (1).png" alt=""><figcaption></figcaption></figure>

* Bold text — click the **B** icon while highlighting the text:\
  **Bold text**
* Italics — click the _**I**_ icon while highlighting the text:\
  \&#xNAN;_Italic text_
* Underlined text — click the **U** icon while highlighting the text:\
  T̲e̲x̲t̲ ̲w̲i̲t̲h̲ ̲u̲n̲d̲e̲r̲l̲i̲n̲i̲n̲g̲
* Quoting text — click the ❝ icon while highlighting the text:

> quoted text

* Hidden content block:\
  \[`toggle title="Why rent a script when you can buy it from you?"`]Indeed, buying it once is cheaper than paying rent every month. However, the amount needed for a one-time purchase is quite substantial.\[/toggle]\`

<details>

<summary>Why rent a script when you can buy it from you?</summary>

Indeed, buying it once is cheaper than paying rent every month. However, the amount needed for a one-time purchase is quite substantial.

</details>
{% endtab %}

{% tab title="Text Mode" %}
<figure><img src="../../../ru/.gitbook/assets/image (563) (1).png" alt="" width="206"><figcaption></figcaption></figure>

<figure><img src="../../../ru/.gitbook/assets/image (564) (1).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

To ensure the pages display correctly on the site, you need to select the appropriate attributes for them:

<figure><img src="../../../ru/.gitbook/assets/image (566) (1).png" alt="" width="440"><figcaption></figcaption></figure>

{% hint style="warning" %}
We recommend not changing technical pages for basic pages, as this may disrupt the proper display of pages on the site.

The two main technical pages — "**Home**" and "**News**" — should not be edited; use them as they are.

<img src="../../../ru/.gitbook/assets/image (656) (1).png" alt="" data-size="original"><img src="../../.gitbook/assets/image (1600)_eng.png" alt="" data-size="original">
{% endhint %}

**Parent** — this is the page under which the edited page will be "nested." The parent page is at the top level, while child pages are nested at subsequent levels.

For example, you can make the **Currencies** page a parent page, with **Ethereum** and **Bitcoin** pages underneath it. Under the **Bitcoin** page, you might have another page called **Wrapped Bitcoin**. The URLs could look like this:

* https://exchanger.com/currencies/
* https://exchanger.com/currencies/eth/
* https://exchanger.com/currencies/btc/
* https://exchanger.com/currencies/btc/wbtc/

More detailed settings for this option are described in the [official WordPress documentation](https://wordpress.com/ru/support/pages/page-options/).

If you do not plan to use a nested structure, select the "**No Parent**" option.

<figure><img src="../../../ru/.gitbook/assets/image (156) (1).png" alt="" width="236"><figcaption></figcaption></figure>

**Template:**

<figure><img src="../../../ru/.gitbook/assets/image (565) (1).png" alt="" width="241"><figcaption></figcaption></figure>

* **Default Template** — the optimal choice for displaying most pages on the site.
* **Home Page Template** — used **only** for the main page of the site (when this option is selected, the specified page in the general list of pages will be marked as "**Home Page**," and a table with exchange directions will be displayed on the page itself, regardless of the shortcode or text specified in the page settings).

<figure><img src="../../../ru/.gitbook/assets/image (568) (1).png" alt="" width="330"><figcaption></figcaption></figure>

* **Page Template Without Sidebar** — displays the page without a sidebar for the personal account.

<figure><img src="../../../ru/.gitbook/assets/image (569) (1).png" alt="" width="563"><figcaption></figcaption></figure>

* **Plugin Page Template** — displays the page with a sidebar.

<figure><img src="../../../ru/.gitbook/assets/image (570) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../ru/.gitbook/assets/image (567) (1).png" alt="" width="456"><figcaption></figcaption></figure>

**Technical Page** — select from the dropdown list the basic page that will be used for the editable page, and the link that will be displayed in the list of pages in the personal account.

The number of technical pages is limited to the list, and only one site page can be attached to a technical page.

<details>

<summary>Example of Using Technical Pages</summary>

Using a technical page for an appropriate page (the link name is taken from the title of the editable page)

<img src="../../../ru/.gitbook/assets/image (571) (1).png" alt="" data-size="original">

Using a technical page for an inappropriate page

![](<../../../ru/.gitbook/assets/image (654) (1).png>)

Technical page not used

![](<../../../ru/.gitbook/assets/image (573) (1).png>)

</details>

You can also change the URLs of all pages, **except for the main page**:

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(147)_eng.png" alt=""><figcaption></figcaption></figure>
