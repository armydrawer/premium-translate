# Section "Pages"

## Basic Pages

In this section, you can create and edit the pages you want to display on your website. By default, most of the standard pages for an exchange platform are already created — you can edit them as needed or add new pages. You can apply various formatting options to the text on the pages you create.

Here is a list of all the default pages:

<figure><img src="../../.gitbook/assets/image (1227).png" alt=""><figcaption></figcaption></figure>

Please note that the content of the website's basic pages cannot be edited directly through the admin panel. The text for such pages is loaded from the source code using a specific shortcode in the "**Text**" field. For these pages, you can only add additional text via the same field or edit the text directly in the code:

<figure><img src="../../.gitbook/assets/изображение.png" alt=""><figcaption></figcaption></figure>

<details>

<summary>List of all basic pages and their shortcodes</summary>

- Authorization — \[login\_page]  
- Your Transactions — \[userxch]  
- Your Wallets — \[userwallets]  
- Account Verification — \[userverify]  
- Wallet Verification — \[walletsverify]  
- Internal Account — \[domacc\_page]  
- Password Recovery — \[lostpass\_page]  
- Affiliate Withdrawals — \[payouts\_page]  
- Home — \[home]  
- Sitemap — \[sitemap]  
- Contacts — \[contact\_form]  
- Personal Account — \[account\_page]  
- Security Settings — \[security\_page]  
- Exchange — \[exchange]  
- Exchange Steps — \[exchangestep]  
- Reviews — \[reviews\_page]  
- Affiliate Exchanges — \[pexch\_page]  
- Affiliate Links — \[plinks\_page]  
- Affiliate Account — \[paccount\_page]  
- Registration — \[register\_page]  
- Promotional Materials — \[promotional\_page]  
- Referrals — \[preferals\_page]  
- Rates — \[tarifs]  
- API — \[user\_api]  

</details>

## Editing a Page

A page in editing mode looks like this:

<figure><img src="../../.gitbook/assets/image (1596).png" alt=""><figcaption></figcaption></figure>

### Examples of text formatting on a page:

{% tabs %}
{% tab title="Mode: 'Visual'" %}
<figure><img src="../../.gitbook/assets/image (1597).png" alt="" width="289"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (846).png" alt=""><figcaption></figcaption></figure>

- **Bold text** — click the **B** icon while the text is selected:  
  **Bold text**  
- *Italic text* — click the _**I**_ icon while the text is selected:  
  *Italic text*  
- Underlined text — click the **U** icon while the text is selected:  
  U̲n̲d̲e̲r̲l̲i̲n̲e̲d̲ ̲t̲e̲x̲t̲  
- Quoting text — click the ❝ icon while the text is selected:  

> Quoted text  

- Hidden content block:  
  \[`toggle title="Why rent a script when you can buy it from you?"]It's true that buying it once is cheaper than paying rent every month. However, the upfront cost of purchasing is quite high.[/toggle]`

<details>

<summary>Why rent a script when you can buy it from you?</summary>

It's true that buying it once is cheaper than paying rent every month. However, the upfront cost of purchasing is quite high.

</details>
{% endtab %}

{% tab title="Mode: 'Text'" %}
<figure><img src="../../.gitbook/assets/image (563).png" alt="" width="206"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (564).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

### Setting Attributes for Proper Page Display

To ensure pages display correctly on the website, you need to assign the appropriate attributes:

<figure><img src="../../.gitbook/assets/image (566).png" alt="" width="440"><figcaption></figcaption></figure>

{% hint style="warning" %}
We recommend not altering the technical pages for basic pages, as this may disrupt their proper display on the website.

The two main technical pages — "**Home**" and "**News**" — should ideally remain unchanged. Use them as they are.

&#x20;![](<../../.gitbook/assets/image (1599).png>)![](<../../.gitbook/assets/image (1600).png>)
{% endhint %}

- **Parent** — the page under which the edited page will be nested. A parent page is at the top level, while child pages are nested under it.  

For example, you can set the **Currencies** page as the parent, and place **Ethereum** and **Bitcoin** pages under it. Under the **Bitcoin** page, you could add another page called **Wrapped Bitcoin**. The URLs might look like this:  

  - https://exchanger.com/currencies/  
  - https://exchanger.com/currencies/eth/  
  - https://exchanger.com/currencies/btc/  
  - https://exchanger.com/currencies/btc/wbtc/  

For more details on setting this option, refer to the [official WordPress guide](https://wordpress.com/ru/support/pages/page-options/).  

If you don't plan to use a nested structure, select "**No Parent**".  

<figure><img src="../../.gitbook/assets/image (156).png" alt="" width="236"><figcaption></figcaption></figure>

- **Template:**

<figure><img src="../../.gitbook/assets/image (565).png" alt="" width="241"><figcaption></figcaption></figure>

  - **Default Template** — the optimal choice for displaying most pages on the website.  
  - **Home Page Template** — used **only** for the website's home page. When this option is selected, the page will appear in the general list of pages with the label "**Home Page**," and on the website itself, a table with exchange directions will be displayed, regardless of the shortcode or text specified in the page settings.  

<figure><img src="../../.gitbook/assets/image (568).png" alt="" width="330"><figcaption></figcaption></figure>

  - **Page Template Without Sidebar** — displays the page without a sidebar for the personal account section.  

<figure><img src="../../.gitbook/assets/image (569).png" alt="" width="563"><figcaption></figcaption></figure>

  - **Plugin Page Template** — displays the page with a sidebar.  

<figure><img src="../../.gitbook/assets/image (570).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (567).png" alt="" width="456"><figcaption></figcaption></figure>

- **Technical Page** — select a basic page from the dropdown list to be used for the edited page. The link to this page will appear in the list of pages in the personal account section.  

The number of technical pages is limited to the list provided, and only one website page can be attached to a technical page.  

<details>

<summary>Example of Using Technical Pages</summary>

Using a technical page for a suitable page (the link name is taken from the title of the edited page):  

<img src="../../.gitbook/assets/image (571).png" alt="" data-size="original">

Using a technical page for an unsuitable page:  

![](<../../.gitbook/assets/image (1598).png>)

When a technical page is not used:  

![](<../../.gitbook/assets/image (574).png>)

</details>

Additionally, if necessary, you can change the URL of all pages, **except for the home page**:

<figure><img src="../../.gitbook/assets/изображение (147).png" alt=""><figcaption></figcaption></figure>