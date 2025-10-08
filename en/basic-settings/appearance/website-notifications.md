# Website Notifications

The website can display three types of notifications, which can be configured in the "**Notifications**" section:

## Display Options

{% tabs %}
{% tab title="Header Notification" %}
<figure><img src="../../.gitbook/assets/изображение (109)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Popup Notification" %}
<figure><img src="../../.gitbook/assets/изображение (83)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Notification Window" %}
<figure><img src="../../.gitbook/assets/изображение (127)_eng.png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

All created notifications are displayed in the "Notifications" section.

<figure><img src="../../.gitbook/assets/изображение (141)_eng.png" alt=""><figcaption></figcaption></figure>

## Notification Settings

<figure><img src="../../.gitbook/assets/изображение (5)_eng.png" alt=""><figcaption></figcaption></figure>

**Notification Type** — choose the intervals for displaying the notification.

| By Time Period                                                                                 | By Schedule                                      |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| <p></p><p><img src="../../.gitbook/assets/изображение (187)_eng.png" alt="" data-size="original"></p> | ![](<../../.gitbook/assets/изображение (64)_eng.png>) |

**Operator Status** — the status under which the notification will be displayed\
• **Any Status**\
• **offline**\
• **online**

**Link** — the link that will be displayed in the notification below the text.

**Duration (days)** - the period for which the notification will be active.

**Text** — the text displayed in the notification.

**Status:**\
• **Published** — the notification is active and will be displayed during the selected time interval.\
• **Under Review** — the notification is inactive.

## Additional Options for Notifications

### **Header Notification**

**CSS Class** — specify any class (without a dot) that has a filled `background` parameter in the `style.css` file of your theme — the background color of the selected class will be applied to the notification.

![](<../../.gitbook/assets/image (2099)_eng.png>)![](<../../.gitbook/assets/image (2100)_eng.png>)

{% hint style="info" %}
An alternative option is to specify the desired [RGB code](https://colorscheme.ru/) for the background in the `wp-content/themes/your_theme_name/style.css` file for the **existing** class `.wclosearea` (find the class using Ctrl+F) and [clear the cache in Cloudflare](https://premium.gitbook.io/main/en/basic-settings/faq/kak-sbrosit-kesh-v-cloudflare) (no server restart is required) to see the changes immediately.

In this case, you do not need to fill in the "**CSS Class**" field in the admin panel.

<img src="../../.gitbook/assets/image (1631)_eng.png" alt="" data-size="original">
{% endhint %}

### **Popup Notification, Notification Window**

**Button Text** — the text for the button to hide the notification.

## Sorting Notifications

Notifications can be sorted by their display priority on the website.

<figure><img src="../../.gitbook/assets/изображение (130)_eng.png" alt=""><figcaption></figcaption></figure>