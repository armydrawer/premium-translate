# Pages "Site Rules," "AML/KYC/KYT Verification Rules"

## Settings for v2.4

### "Site Rules" Page

The site rules page is included by default and is typically located at _https://your\_domain/**tos**_ (you can change the page address if needed using the **"Edit"** button in the **"Pages"** section).

You can edit the text of the page and other settings (SEO text, keywords, title) through the admin panel in the **"Pages"** section or directly on the page using the **"Edit Page"** button.

<figure><img src="../../.gitbook/assets/image (1191)_eng.png" alt=""><figcaption><p>Section "<strong>Pages</strong>"</p></figcaption></figure>

<figure><img src="../../.gitbook/assets/image (1055)_eng.png" alt=""><figcaption><p>Exchange Page</p></figcaption></figure>

### "AML/KYC/KYT Verification Rules" Page

You need to create this page manually and fill it with text as you see fit. Be sure to note the page address, as you will need it later.

<figure><img src="../../.gitbook/assets/image (969) (1).png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
If you are using version 2.4, you need to upload and unpack the module into the `wp-content/plugins/premiumbox/moduls` folder.
{% endhint %}

{% file src="../../.gitbook/assets/additionalrules.zip" %}
Download Module
{% endfile %}

In the **"Modules"** -> **"Modules"** section, you need to activate the **"Additional Rules"** module.

<figure><img src="../../.gitbook/assets/image (1132)_eng.png" alt=""><figcaption></figcaption></figure>

To create the page, go to the **"Pages"** section and create a new page for the AML/KYC/KYT rules.

Then, navigate to the **"Exchange Settings"** -> **"General Settings"** section and draft the text for agreeing to the rules, as well as the error message if the rules are not accepted.

<figure><img src="../../.gitbook/assets/image (1058)_eng.png" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Replace the word **/aml/** with the address of the page you created.
{% endhint %}

## Settings for v2.5 and Above

Go to the **"Exchange Settings"** -> **"General Settings"** section and enter the following text in the **"Text for agreeing to the rules before submitting a request"** field:

```
I have read and agree to the <a href="/tos/" target="_blank">exchange terms</a> and the <a href="/aml/" target="_blank">AML verification rules</a>.
```

<figure><img src="../../.gitbook/assets/image (1035)_eng.png" alt=""><figcaption></figcaption></figure>

## Display Settings

You can choose the step at which the rules text and the acceptance checkbox will be displayed. In the **"Exchange Settings"** -> **"General Settings"** section, find the option **"Use exchange step #2, where the user confirms their details."**

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(81)_eng.png" alt=""><figcaption></figcaption></figure>

If "No" is selected, the text will be displayed immediately on the exchange page:

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(135)_eng.png" alt=""><figcaption></figcaption></figure>

If "Yes" is selected, the text will be displayed on the next step, after the application details have been filled out:

<figure><img src="../../.gitbook/assets/%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5%20(140)_eng.png" alt=""><figcaption></figcaption></figure>
