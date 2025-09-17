# Notifications on the Website

The website allows you to display three types of notifications, which can be configured in the "**Notifications**" section:

## Display Options on the Website

{% tabs %}
{% tab title="Website Header" %}
<figure><img src="../../.gitbook/assets/изображение (109).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Popup Window" %}
<figure><img src="../../.gitbook/assets/изображение (83).png" alt=""><figcaption></figcaption></figure>
{% endtab %}

{% tab title="Notification Window" %}
<figure><img src="../../.gitbook/assets/изображение (127).png" alt=""><figcaption></figcaption></figure>
{% endtab %}
{% endtabs %}

All created notifications are displayed in the "Notifications" section.

<figure><img src="../../.gitbook/assets/изображение (141).png" alt=""><figcaption></figcaption></figure>

## Notification Settings

<figure><img src="../../.gitbook/assets/изображение (5).png" alt=""><figcaption></figcaption></figure>

**Notification Type** — choose the intervals for displaying the notification.

| By Time Period                                                                                   | By Schedule                                      |
| ------------------------------------------------------------------------------------------------- | ------------------------------------------------ |
| <p></p><p><img src="../../.gitbook/assets/изображение (187).png" alt="" data-size="original"></p> | ![](<../../.gitbook/assets/изображение (64).png>) |

**Operator Status** — the status under which the notification will be displayed:  
• **Any status**  
• **Offline**  
• **Online**

**Link** — a link that will be displayed below the notification text.

**Duration (days)** — the period for which the notification will be active.

**Text** — the text displayed in the notification.

**Status:**  
• **Published** — the notification is active and will be displayed during the selected time interval.  
• **Under Moderation** — the notification is inactive.

## Additional Options for Notifications

### **Website Header**

**CSS Class** — specify any class (without the dot) that has a defined `background` parameter in the `style.css` file of your theme. The background color of the selected class will be applied to the notification.

![](<../../.gitbook/assets/image (2099).png>)![](<../../.gitbook/assets/image (2100).png>)

{% hint style="info" %}
Alternatively, you can specify the desired [RGB code](https://colorscheme.ru/) for the background in the `wp-content/themes/your_theme_name/style.css` file for an **existing** class `.wclosearea` (find the class using Ctrl+F). Then, [clear the cache in the Cloudflare dashboard](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sbrosit-kesh-v-cloudflare) (no server restart is required) to see the changes immediately.

In this case, the "**CSS Class**" field in the admin panel does not need to be filled out.

<img src="../../.gitbook/assets/image (1631).png" alt="" data-size="original">
{% endhint %}

### **Popup Window, Notification Window**

**Button Text** — the text for the button that hides the notification.

## Notification Sorting

Notifications can be sorted by priority for display on the website.

<figure><img src="../../.gitbook/assets/изображение (130).png" alt=""><figcaption></figcaption></figure>