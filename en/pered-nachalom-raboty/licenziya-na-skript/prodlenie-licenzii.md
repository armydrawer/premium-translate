# License Renewal

Follow these steps to renew your license.

{% hint style="danger" %}
After purchasing a new license, **make sure** to upload the updated archive with the [license](https://premiumexchanger.com/ulicense/) to the server using the <mark style="color:green;">**user created for the site**</mark> (not <mark style="color:red;">**root**</mark>!) over the existing license files. Without this step, the previous license will remain active for the site.\
\
Please note that the license files must **always** match the version of the script installed on your server (the script version is displayed on almost every page in the admin panel at the top left corner above the logo).\
![](<../../.gitbook/assets/image (1934)_eng.png>)

If you do not have access to the admin panel, you can check the script version by opening the file located at `wp-content\plugins\premiumbox\premiumbox.php` on the server; the version will be indicated in the first few lines.

![](<../../.gitbook/assets/image (2005)_eng.png>)
{% endhint %}

{% hint style="danger" %}
If you upload license files from a different version of the script, the site will stop working until the correct archive is uploaded.
{% endhint %}

## Purchasing (Renewing) a License

1. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section.
2. Under the domain name for which you want to renew the license, click the "**Renew**" button.

{% hint style="info" %}
You can change the domain name in the license no earlier than 24 hours before the current rental period expires.
{% endhint %}

<figure><img src="../../.gitbook/assets/Screenshot_11 (1)_eng.png" alt="" width="514"><figcaption></figcaption></figure>

3. Select the number of months for the license renewal.\

    <figure><img src="../../.gitbook/assets/изображение (96)_eng.png" alt=""><figcaption></figcaption></figure>
4. Proceed to payment and complete your order.
5. Return to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section. Click the "**Download for version X.X**" button, where X.X is your script version. You can find the current version of your script in the site management panel under the "**Plugins**" section or through the file manager in the file `/wp-content/plugins/premiumbox/premiumbox.php` _(&#x43D;_&#x430; your computer will download the archive `license.zip`_)_\

    <figure><img src="../../.gitbook/assets/изображение (51)_eng.png" alt=""><figcaption></figcaption></figure>
6. Upload the downloaded archive _`license.zip`_ to the root folder of your site (usually the folders `public_html`, `www`, or `docs`) and make sure to extract the archive.

## Uploading the license.zip Archive to the Root Folder of the Site on a Server Managed by ISP Manager

{% embed url="https://youtu.be/s1j_8mhjmrM" %}

1. Log in to your server in ISP Manager using the <mark style="color:green;">user created for the site</mark>. \
   You can do this in two ways:

* **Option 1** — log in directly as the <mark style="color:green;">user created for the site</mark>\
  ![](<../../.gitbook/assets/image (512)_eng.png>)
* **Option 2** — log in as the <mark style="color:red;">root</mark> user, then go to the "**Sites**" section, select the necessary site, and click the "**Log in as Owner**" button.\
  After these steps, you will be logged in as the <mark style="color:green;">user created for the site</mark>.

<figure><img src="../../.gitbook/assets/image (998)_eng.png" alt=""><figcaption></figcaption></figure>

2. In the "**File Manager**" section, open your site's directory: `https://`_`your_domain_name/`_ and click the "**Upload**" icon. Wait for the file to upload.

<figure><img src="../../.gitbook/assets/image (903)_eng.png" alt=""><figcaption></figcaption></figure>

3. Click the "**Select File**" button. Locate the previously downloaded archive `license.zip` on your computer and click the "**OK**" button.

<figure><img src="../../.gitbook/assets/image (1197)_eng.png" alt=""><figcaption></figcaption></figure>

4. Select the `license.zip` archive and extract it by clicking the "**Extract**" icon.

<figure><img src="../../.gitbook/assets/image (985)_eng.png" alt=""><figcaption></figcaption></figure>