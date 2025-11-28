# Website Functionality During Non-Working Hours

The vast majority of exchange services operate on a schedule, as they need to respond to user requests, manually process transactions, verify applications, and so on. This requires an operator to monitor incoming requests.

To ensure that some or all user sections are disabled during non-working hours and that certain functions are unavailable to users, you need to configure the "**Operational Status**" and "**Maintenance Mode**" sections.

## Operational Status Section

{% hint style="warning" %}
Settings in this section only affect the display of the operator's status on the website pages; automatic exchanges (involving merchant transactions) will function regardless of these settings.
{% endhint %}

### Settings

In the "**Settings**" subsection, you can configure the operational modes of the website.

**Status Determination Principle:**\
• **Manual** — the status must be switched manually in the "**Manual Mode Settings**" block.\
• **Automatic** —\
• **Schedule** — the status will automatically change according to a pre-set schedule.

**Operator Button:**

• **Left** — the button will be "pinned" to the left edge of the website.\
• **Right** — the button will be "pinned" to the right edge of the website.\
• **Hide Button** — the button will not be displayed.

**"Offline" Text** — the text displayed on the button when the operator is offline.

**"Offline" Link** — the link to the page that will be accessed when the button is clicked while the operator is offline.

**"Online" Text** — the text displayed on the button when the operator is online.

**"Online" Link** — the link to the page that will be accessed when the button is clicked while the operator is online.

**Status** — manual status switching (works in conjunction with the **"Status Determination Principle"** — "**Manual**")\
• **Offline**\
• **Online**

### Adding a Schedule

**Status** — the status the exchange service will have on the specified dates and times below.\
• **Offline**\
• **Online**

**Working Hours** — the interval (hh:mm - hh:mm) for the start and end of the status.

**Working Days** — the days on which the status will be active.

### Operator Schedule

If necessary, you can create multiple schedules for the website for different statuses:

## Maintenance Mode

{% hint style="warning" %}
When maintenance mode is enabled, creating new requests on the website will be prohibited.
{% endhint %}

### Settings

**How to Switch Maintenance Mode:**\
• **Manually** — the mode must be switched manually.\
• **Based on Operator Status** — the mode will switch according to the operator's status.

**Maintenance Mode** — previously created modes will be displayed in the dropdown list.

### Adding a Mode

**Name for the Website** — the name of the mode that will be displayed in the dropdown list in the "**Maintenance Mode**" settings.

**Text for Clients** — the text that will be displayed on the exchange service pages when the option "**Do not hide and display text**" is selected for the blocks below.

For the parameters:\
• **Exchange Direction Selection Table on the Main Page**\
• **Exchange Form**\
• **API**\
• **Rate Files for Monitoring**\
• **Rates**\
• **HTML Sitemap**\
• **XML Sitemap**

the following options are available:\
• **Do not hide** — the block will be displayed on the page when the selected mode is active.\
• **Do not hide and display text** — the block will be displayed on the page when the selected mode is active, and the text from the "**Text for Clients**" field will be shown above the block.\
• **Hide** — the block will not be displayed on the page when the selected mode is active.

**Activate Mode When Operator Status Is** — select the operator status that will activate this mode.\
• **Offline**\
• **Online**

**Apply Mode:**\
• **For Users and Administrators** — the mode will apply to all users, regardless of role and status.\
• **For Users Only** — the mode will apply only to exchange service users.

### **Maintenance Mode**

If necessary, you can create multiple modes:
