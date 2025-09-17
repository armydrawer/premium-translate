# License Renewal

Follow the steps below to extend the validity of your license.

{% hint style="danger" %}
After purchasing a new license, it is **mandatory** to upload the updated license archive from [this link](https://premiumexchanger.com/ulicense/) to your server **using the user account created specifically for the website** (not the <mark style="color:red;">**root**</mark> user!). Overwrite the existing license files with the new ones. If this step is skipped, the previous license will remain active for the website.  

Please note that you must **always** upload license files that match the version of the script installed on your server. The script version can be found on almost every page of the admin panel in the top-left corner above the logo.  
![](<../../.gitbook/assets/image (1934).png>)

If you do not have access to the admin panel, open the file located at `wp-content\plugins\premiumbox\premiumbox.php` on your server. The script version will be indicated in the first few lines of the file.  

![](<../../.gitbook/assets/image (2005).png>)
{% endhint %}

{% hint style="danger" %}
If you upload license files for a different script version, the website will stop functioning until the correct archive is uploaded.
{% endhint %}

## Purchasing (Renewing) a License

1. Go to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section.
2. Under the domain name for which you want to renew the license, click the "**Renew**" button.

{% hint style="info" %}
The domain name associated with the license can only be changed at least one day before the current license period expires.
{% endhint %}

<figure><img src="../../.gitbook/assets/Screenshot_11 (1).png" alt="" width="514"><figcaption></figcaption></figure>

3. Select the number of months for which you want to extend the license.  

    <figure><img src="../../.gitbook/assets/изображение (96).png" alt=""><figcaption></figcaption></figure>
4. Proceed to payment and complete the transaction.
5. Go back to the "[**Your Licenses**](https://premiumexchanger.com/ulicense/)" section. Click the "**Download for version X.X**" button, where X.X is the version of your script. You can find the current version of your script in the website's admin panel under the "**Plugins**" section or by checking the file `/wp-content/plugins/premiumbox/premiumbox.php`.  
   _(The archive `license.zip` will be downloaded to your computer.)_  

    <figure><img src="../../.gitbook/assets/изображение (51).png" alt=""><figcaption></figcaption></figure>
6. Upload the downloaded `license.zip` archive to the root folder of your website (this is usually `public_html`, `www`, or `docs`) and make sure to extract the archive.

## Uploading the `license.zip` Archive to the Website's Root Folder on a Server Managed by ISP Manager

{% embed url="https://youtu.be/s1j_8mhjmrM" %}

1. Log in to your server in ISP Manager using the <mark style="color:green;">user account created for the website</mark>.  
   You can do this in two ways:

* **Option 1** — Log in directly as the <mark style="color:green;">user created for the website</mark>.  
  ![](<../../.gitbook/assets/image (512).png>)
* **Option 2** — Log in as the <mark style="color:red;">root</mark> user, then go to the "**Sites**" section, select the desired website, and click the "**Log in as owner**" button.  
  After this, you will be logged in as the <mark style="color:green;">user created for the website</mark>.

<figure><img src="../../.gitbook/assets/image (998).png" alt=""><figcaption></figcaption></figure>

2. In the "**File Manager**" section, open your website's directory: `https://`_`your_domain_name/`_ and click the "**Upload**" icon. Wait for the file to finish uploading.

<figure><img src="../../.gitbook/assets/image (903).png" alt=""><figcaption></figcaption></figure>

3. Click the "**Choose File**" button. Locate the previously downloaded `license.zip` archive on your computer and click "**OK**".

<figure><img src="../../.gitbook/assets/image (1197).png" alt=""><figcaption></figcaption></figure>

4. Select the `license.zip` archive and extract it by clicking the "**Extract**" icon.

<figure><img src="../../.gitbook/assets/image (985).png" alt=""><figcaption></figcaption></figure>