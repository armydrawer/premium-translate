# License Renewal

Follow the steps below to extend the validity of your license.

{% hint style="danger" %}
After paying for the new license, it is **essential** to upload the updated license archive from [this page](https://premiumexchanger.com/ulicense/) to your server **using the user account created specifically for the website** (do **not** use the **root** user!). Upload the new license files **over the existing ones** — otherwise, the site will continue to operate under the previous license.

Please note that the license files you upload **must always match the version of the script installed on your server**. You can find the script version displayed on almost every page in the admin panel, in the top left corner above the logo.  
![](<../../.gitbook/assets/image (1934).png>)

If you don’t have access to the admin panel, open the file located at `wp-content\plugins\premiumbox\premiumbox.php` on your server — the script version is indicated in the first few lines.  
![](<../../.gitbook/assets/image (2005).png>)
{% endhint %}

{% hint style="danger" %}
If you upload license files for a different script version, the site will stop working until the correct license archive is uploaded.
{% endhint %}

## Purchasing (Renewing) a License

1. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section.
2. Find the domain name for which you want to renew the license and click the "**Renew**" button.

{% hint style="info" %}
You can only change the domain name in the license no earlier than 24 hours before the current license expires.
{% endhint %}

<figure><img src="../../.gitbook/assets/Screenshot_11 (1).png" alt="" width="514"><figcaption></figcaption></figure>

3. Select the number of months you want to extend the license for.  
<figure><img src="../../.gitbook/assets/изображение (96).png" alt=""><figcaption></figcaption></figure>

4. Proceed to payment and complete your order.
5. After payment, return to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section. Click the "**Download for version X.X**" button, where X.X is your script version. You can check your current script version in the site’s admin panel under "**Plugins**" or by opening the file `/wp-content/plugins/premiumbox/premiumbox.php` via your file manager.  
(The license archive `license.zip` will be downloaded to your computer.)

<figure><img src="../../.gitbook/assets/изображение (51).png" alt=""><figcaption></figcaption></figure>
6. Upload the downloaded archive _`license.zip`_ to the root folder of your website (usually one of the folders named `public_html`, `www`, or `docs`) and be sure to extract the archive.

## Uploading the license.zip Archive to the Website Root Folder on a Server Running ISP Manager

{% embed url="https://youtu.be/s1j_8mhjmrM" %}

1. Log in to your server in ISP Manager using the <mark style="color:green;">user account created for your website</mark>. You can do this in one of two ways:

* **Option 1** — log in directly as the <mark style="color:green;">user created for your website</mark>.\
  ![](<../../.gitbook/assets/image (512).png>)
* **Option 2** — log in as the <mark style="color:red;">root</mark> user, then go to the "**Sites**" section, select the desired site, and click the "**Login as Owner**" button.\
  After this, you will be logged in as the <mark style="color:green;">user created for your website</mark>.

<figure><img src="../../.gitbook/assets/image (998).png" alt=""><figcaption></figcaption></figure>

2. In the "**File Manager**" section, open your website’s directory: `https://`_`your_domain_name/`_ and click the "**Upload**" icon. Wait for the file to finish uploading.

<figure><img src="../../.gitbook/assets/image (903).png" alt=""><figcaption></figcaption></figure>

3. Click the "**Choose File**" button. Locate the previously downloaded `license.zip` archive on your computer and click "**OK**".

<figure><img src="../../.gitbook/assets/image (1197).png" alt=""><figcaption></figcaption></figure>

4. Select the `license.zip` archive and extract it by clicking the "**Extract**" icon.

<figure><img src="../../.gitbook/assets/image (985).png" alt=""><figcaption></figcaption></figure>