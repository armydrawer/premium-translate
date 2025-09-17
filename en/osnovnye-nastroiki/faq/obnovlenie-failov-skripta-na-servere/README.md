# Updating Script Files on the Server

When dealing with complex and hard-to-diagnose errors, a quick and effective solution is to update the script files on the server to the latest version.

{% hint style="danger" %}
Script files must always be uploaded and extracted on the server under the user account created specifically for the website <mark style="color:red;">**(not root)**</mark>!
{% endhint %}

Here’s what you need to do:

1. Create a [backup of all website files on the server](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita).
2. Download the [**update distribution package**](https://premiumexchanger.com/uscripts/) **for your script version** (the PHP version doesn’t matter — you can choose any of the available distributions).

![](<../../../.gitbook/assets/image (294).png>)

3. Upload the distribution archive to the root folder of your website and extract it, replacing the existing files.
4. Check if the issue has been resolved.