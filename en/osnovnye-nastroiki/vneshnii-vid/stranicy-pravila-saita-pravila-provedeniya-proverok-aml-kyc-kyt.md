# Pages "Site Rules" and "AML/KYC/KYT Verification Rules"

## Settings for v2.4

### "Site Rules" Page

The "Site Rules" page is available out of the box and is typically located at _https://your\_domain/**tos**_. If needed, the page URL can be changed by clicking the **"Edit"** button in the **"Pages"** section.

The content of the page, as well as other settings (SEO text, keywords, title), can be edited via the admin panel in the **"Pages"** section or directly on the page itself by clicking the **"Edit Page"** button.

<figure><img src="../../.gitbook/assets/image (1191).png" alt=""><figcaption><p>The "<strong>Pages</strong>" section</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1055).png" alt=""><figcaption><p>Exchange page</p></figcaption></figure>

### "AML/KYC/KYT Verification Rules" Page

This page needs to be created manually and filled with content of your choice. Be sure to specify the page URL, as it will be required later.

<figure><img src="../../.gitbook/assets/image (969).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you are using version 2.4, you need to download and extract the module into the `wp-content/plugins/premiumbox/moduls` folder.
{% endhint %}

{% file src="../../.gitbook/assets/additionalrules.zip" %}
Module for download
{% endfile %}

In the **"Modules"** -> **"Modules"** section, activate the **"Additional Rules"** module.

<figure><img src="../../.gitbook/assets/image (1132).png" alt=""><figcaption></figcaption></figure>

To create the page, go to the **"Pages"** section and create a new page with the AML/KYC/KYT rules.

Then, navigate to **"Exchange Settings"** -> **"General Settings"** and compose the text for agreeing to the rules, as well as the error message if the rules are not accepted.

<figure><img src="../../.gitbook/assets/image (1058).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Replace the word **/aml/** with the URL of the page you created.
{% endhint %}

## Settings for v2.5 and Above

Go to **"Exchange Settings"** -> **"General Settings"** and in the field **"Checkbox text for accepting rules before creating a request"**, enter the following text:

```
I have read and agree to the <a href="/tos/" target="_blank">exchange terms</a> and the <a href="/aml/" target="_blank">AML verification rules</a>.
```

<figure><img src="../../.gitbook/assets/image (1035).png" alt=""><figcaption></figcaption></figure>

## Display Settings

You can choose the step at which the rules text and acceptance checkbox will be displayed. In **"Exchange Settings"** -> **"General Settings"**, find the option **"Use exchange step #2, where the user confirms their details"**.

<figure><img src="../../.gitbook/assets/изображение (81).png" alt=""><figcaption></figcaption></figure>

If "No" is selected, the text will be displayed directly on the exchange page:

<figure><img src="../../.gitbook/assets/изображение (135).png" alt=""><figcaption></figcaption></figure>

If "Yes" is selected, the text will appear on the next step, after the request details have been filled in:

<figure><img src="../../.gitbook/assets/изображение (140).png" alt=""><figcaption></figcaption></figure>