# How to Update Files on the Server?

From time to time, it’s necessary to replace module files on the server due to the release of a new module version, bug fixes in the current module, or other reasons.

{% hint style="danger" %}
Before making any changes to the files on the server, we strongly recommend creating a backup of the root folder on your computer:

<img src="../../../.gitbook/assets/image (1269)_eng.png" alt="" data-size="original">

\
All file operations should be performed via the ISP Manager panel under the <mark style="color:green;">**user account created for the website**</mark> (**not** <mark style="color:red;">**root**</mark>).
{% endhint %}

{% hint style="info" %}
To locate the path to the root folder of your website on the server, refer to this [guide](https://premium.gitbook.io/main/en/basic-settings/faq/kak-naiti-kornevuyu-papku-saita-na-servere).
{% endhint %}

{% hint style="danger" %}
Please note that modules are not compatible across different script versions. For example, if you are using script version 2.7, all modules must also be version 2.7.\*.

Installing an incompatible module will result in an error (the website will not load), and you will need to upload compatible modules again.
{% endhint %}

***

## Script Modules

1. Download the **update archive** for your script version from the [**"Your Scripts"**](https://premiumexchanger.com/uscripts/) page. Choose the appropriate PHP version and your script version, then extract the archive on your computer.

<figure><img src="../../../.gitbook/assets/image (2019)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

2. **Make sure** to deactivate the modules you plan to update in the "**Modules**" section.

<figure><img src="../../../.gitbook/assets/image (2020)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

3. Navigate to the directory path shown in the screenshot: `/wp-content/plugins/premiumbox/moduls/`

<figure><img src="../../../.gitbook/assets/image (657) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. Select **one or more required modules** and drag them into the ISP Manager window, placing them in the corresponding directory on the server.
5. At the bottom of the page, a window will appear showing the destination folder (the "**moduls**" folder).
6. If a file conflict window appears, overwrite the files by clicking "**Replace**."
7. Reactivate the updated modules in the "**Modules**" section.

After completing these steps, the modules will be updated, and no further actions are required.

***

## Merchant and Auto-Payout Modules

{% hint style="danger" %}
Ensure that you download the module specifically for the script version installed on your server. The script version can be found, for example, on the "**Requests**" page.

<img src="../../../.gitbook/assets/image (2021)_eng.png" alt="" data-size="original">
{% endhint %}

{% tabs %}
{% tab title="For Version 2.7" %}
In your account, go to the **"Your Scripts"** section and download the merchant module for the required payment system from the "**Additional Modules**" block.

<figure><img src="../../../.gitbook/assets/image (2022)_eng.png" alt=""><figcaption></figcaption></figure>

Upload the contents of the module archive to the server in the `/wp-content/plugins/premiumbox/merchants` directory (for payment acceptance) or `/wp-content/plugins/premiumbox/paymerchants` directory (for auto-payouts), and extract the files. If a file conflict window appears, overwrite the files.
{% endtab %}

{% tab title="For Version 2.6 and Below" %}
Download the updated module distribution (any archive compatible with **your script version**) from the ["**Your Scripts**"](https://premiumexchanger.com/uscripts/) section in your account.

<figure><img src="../../../.gitbook/assets/image (2025)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

Extract the downloaded archive on your computer and locate the folder containing the required merchant module:

<figure><img src="../../../.gitbook/assets/image (674) (1).png" alt="" width="563"><figcaption></figcaption></figure>

or auto-payout module:

<figure><img src="../../../.gitbook/assets/image (695) (1).png" alt="" width="563"><figcaption></figcaption></figure>

Upload the contents of the module archive to the server in the `/wp-content/plugins/premiumbox/merchants` directory (for payment acceptance) or `/wp-content/plugins/premiumbox/paymerchants` directory (for auto-payouts). If a file conflict window appears, overwrite the files.
{% endtab %}
{% endtabs %}

***

## Default Script Design Files

1. Download the **update archive** for your script version from the [**"Your Scripts"**](https://premiumexchanger.com/uscripts/) page. Choose the appropriate PHP version and your script version, then extract the archive on your computer.

<figure><img src="../../../.gitbook/assets/image (2032)_eng.png" alt="" width="563"><figcaption></figcaption></figure>

2. Navigate to the directory path shown in the screenshot: `/wp-content/themes/`

<figure><img src="../../../.gitbook/assets/image (677) (1).png" alt="" width="563"><figcaption></figcaption></figure>

4. Select the required design folder (`newexchanger2.0` — the new standard design for 2024) and drag it into the ISP Manager window, placing it in the corresponding directory.
5. If a file conflict window appears, overwrite the files by clicking "**Replace**."
6. Activate the uploaded design in the website control panel under "**Appearance -> Themes**."
7. Additional appearance settings may be required if you activate a new design on the site. The main design settings can be found in the "**Appearance**" section.

***

## Script Files

1. Download the **update archive** for your script version from the [**"Your Scripts"**](https://premiumexchanger.com/uscripts/) page. Choose the appropriate PHP version and your script version, then extract the archive on your computer.

<figure><img src="../../../.gitbook/assets/image (2019)_eng (1).png" alt="" width="563"><figcaption></figcaption></figure>

2. Navigate to the directory path shown in the screenshot: `/wp-content/plugins/premiumbox/`

<figure><img src="../../../.gitbook/assets/image (676) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. Select **one or more required directories** and drag them into the ISP Manager window, placing them in the corresponding directory.
4. If a file conflict window appears, overwrite the files by clicking "**Replace**."
