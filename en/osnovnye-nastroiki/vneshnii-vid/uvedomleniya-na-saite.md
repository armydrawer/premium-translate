# Website Notifications

The website supports three types of notifications, which can be configured in the "**Notifications**" section:

## Display on the Website

{% tabs %}
{% tab title="Site Header" %}
<figure><img src="../../.gitbook/assets/изображение (109).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Popup Window" %}
<figure><img src="../../.gitbook/assets/изображение (83).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Notification Window" %}
<figure><img src="../../.gitbook/assets/изображение (127).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

All created notifications are listed in the "Notifications" section.

<figure><img src="../../.gitbook/assets/изображение (141).png" alt=""><figcaption></figcaption></figure>

## Notification Settings

<figure><img src="../../.gitbook/assets/изображение (5).png" alt=""><figcaption></figcaption></figure>

**Notification Type** — choose the display interval for the notification

| By time period                                                                                   | By schedule                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------ |
| <p></p><p><img src="../../.gitbook/assets/изображение (187).png" alt="" data-size="original"></p> | ![](<../../.gitbook/assets/изображение (64).png>) |

**Operator Status** — the status that must be met for the notification to appear:  
• **Any status**  
• **offline**  
• **online**

**Link** — a URL that will be shown below the notification text

**Duration (days)** — the length of time the notification will remain active

**Text** — the message displayed in the notification

**Status:**  
• **Published** — the notification is active and will display during the selected time interval  
• **Under moderation** — the notification is inactive

## Additional Options for Notifications

### **Site Header**

**CSS Class** — enter any class name (without the dot) that has a defined `background` property in your theme’s `style.css` file. The background color of that class will be applied to the notification.

![](<../../.gitbook/assets/image (2099).png>)![](<../../.gitbook/assets/image (2100).png>)

{% hint style="info" %}
Alternatively, you can specify the desired [RGB background color code](https://colorscheme.ru/) directly in the `style.css` file located at `wp-content/themes/your_theme_name/style.css` for the **existing** `.wclosearea` class (search for this class using Ctrl+F). After making changes, clear the cache in your Cloudflare dashboard ([how to clear cache in Cloudflare](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sbrosit-kesh-v-cloudflare)) — no server restart is needed — so the changes take effect immediately.

In this case, you do **not** need to fill in the "**CSS Class**" field in the admin panel.
{% endhint %}

### Popup Window, Notification Window

**Button Text** — the text on the button used to dismiss the notification

## Sorting Notifications

Notifications can be sorted by display priority on the website

<figure><img src="../../.gitbook/assets/изображение (130).png" alt=""><figcaption></figcaption></figure>