# Updating Script Files on the Server

When facing hard-to-diagnose errors, a quick and effective solution is to update the script files on the server to the latest version.

{% hint style="danger" %}
Script files should always be uploaded and unpacked on the server under the user account created specifically for the website <mark style="color:red;">**(not root)**</mark>!
{% endhint %}

You need to:

* Create a [backup of all website files on the server](https://premium.gitbook.io/main/osnovnye-nastroiki/faq/kak-sdelat-bekap-saita)
* Download the [**update** distribution package](https://premiumexchanger.com/uscripts/) **matching your script version** (PHP version does not matter — you can choose any of the available packages)

![](<../../.gitbook/assets/image (294).png>)\

* Upload the distribution archive to the website’s root folder and unpack it, overwriting the existing files
* Verify that the error has been resolved