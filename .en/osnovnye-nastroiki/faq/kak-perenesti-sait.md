# How to Migrate Your Website

{% hint style="warning" %}
If you already have a live website on your main domain, you can move it to a subdomain. However, if you plan to make changes on the subdomain, you may encounter difficulties later when trying to transfer the database back to the main domain.

This happens because the main site continues to operate with up-to-date data on requests and new users, while the subdomain may have different settings. In such cases, synchronizing the data will no longer be possible.
{% endhint %}

The Premium Exchanger script license includes the option to create a test version of your website on a subdomain, which you can later transfer to your main domain.

To do this, specify your subdomain on the ["Your Licenses"](https://premiumexchanger.com/ulicense/) page:

<figure><img src="../../.gitbook/assets/изображение (142).png" alt=""><figcaption></figcaption></figure>

You can create a subdomain using the ISP Manager control panel by following this [guide](https://www.ihc.ru/articles/sozdanie-poddomenov-v-ispmanager.html).

Install the script on your subdomain according to the [installation instructions](https://premium.gitbook.io/rukovodstvo-polzovatelya/pered-nachalom-raboty/instrukciya-po-ustanovke).

{% hint style="warning" %}
Please note that the license files are updated with your subdomain information only after you specify the subdomain on the "Your Licenses" page — once you add the subdomain, you **must** update the license files on your server and upload them to the root folder of your subdomain website.
{% endhint %}

After setting up the site on your subdomain and testing its functionality, you will need to move the site to your main domain. To do this, use ISP Manager to transfer all files to the main domain’s folder, and update the site URL in the copied database (in the `_options` table — fields `siteurl` and `home`).

<figure><img src="../../.gitbook/assets/image (706).png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
If you plan to fully replace the main domain’s data with all requests and settings from the subdomain, this process should go smoothly without any issues.
{% endhint %}

However, if you want to transfer settings from a subdomain to the main domain (and the main domain already has a live website), synchronizing the two sites won’t be possible. This is because they use two separate databases that are not connected to each other.