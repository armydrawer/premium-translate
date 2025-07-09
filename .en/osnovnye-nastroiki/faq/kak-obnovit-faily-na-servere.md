# How to Update Files on the Server

From time to time, you need to replace module files on the server due to new module versions being released, bug fixes in existing modules, or other reasons.

{% hint style="danger" %}
Before making any changes to files on the server, we strongly recommend backing up the root folder to your computer:

<img src="../../.gitbook/assets/image (1269).png" alt="" data-size="original">

\
All file operations should be performed through the ISP Manager panel logged in as the <mark style="color:green;">**user created specifically for the website**</mark> (**not** <mark style="color:red;">**root**</mark>).
{% endhint %}

{% hint style="info" %}
To find the path to your website’s root folder on the server, please refer to the [instructions here](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/faq/kak-naiti-kornevuyu-papku-saita-na-servere).
{% endhint %}

{% hint style="danger" %}
Please note that modules are not compatible across different script versions. For example, if you are using script version 2.7, all modules must also be version 2.7.*.

If you install an incompatible module, you will encounter errors (the site will not load), and you will need to upload compatible modules again.
{% endhint %}

## Script Modules

1. Download the update archive for your script from the [“Your Scripts” page](https://premiumexchanger.com/uscripts/) — choose the archive matching your PHP version and your script version — then extract it on your computer.

<figure><img src="../../.gitbook/assets/image (2019).png" alt="" width="563"><figcaption></figcaption></figure>

2. **Be sure to deactivate** the modules you plan to update in the "**Modules**" section.

<figure><img src="../../.gitbook/assets/image (2020).png" alt="" width="563"><figcaption></figcaption></figure>

3. Navigate to the modules directory shown in the screenshot: `/wp-content/plugins/premiumbox/moduls/`

<figure><img src="../../.gitbook/assets/image (1831).png" alt="" width="563"><figcaption></figcaption></figure>

4. Select one or more modules you want to update and drag them into the corresponding directory on the server using ISP Manager:

<figure><img src="../../.gitbook/assets/изображение (179).png" alt=""><figcaption></figcaption></figure>

5. At the bottom of the page, a window will appear showing the destination folder (the "**moduls**" folder).

<figure><img src="../../.gitbook/assets/изображение (80).png" alt=""><figcaption></figcaption></figure>

6. If a file conflict window appears, choose to overwrite the files by clicking "**Replace**."

<figure><img src="../../.gitbook/assets/изображение (66).png" alt=""><figcaption></figcaption></figure>

7. Activate the updated modules in the "**Modules**" section.

After completing these steps, the modules will be updated and no further action is required.

## Merchant and Auto-Payout Modules

{% hint style="danger" %}
Make sure you download the module that matches the exact version of the script installed on your server. You can check the script version, for example, on the "**Requests**" page.

![](<../../.gitbook/assets/image (2021).png>)
{% endhint %}

{% tabs %}
{% tab title="For Version 2.7" %}
In your personal account, go to the **"[Your Scripts](https://premiumexchanger.com/uscripts/)"** section and, under the "**Additional Modules**" block, download the merchant module for the required payment system.

<figure><img src="../../.gitbook/assets/image (2022).png" alt=""><figcaption></figcaption></figure>

Upload the contents of the module archive to your server in the `/wp-content/plugins/premiumbox/merchants` directory (for payment acceptance) or `/wp-content/plugins/premiumbox/paymerchants` directory (for auto-payouts), then extract the files. If prompted about file conflicts, overwrite the existing files.
{% endtab %}

{% tab title="For Version 2.6 and Below" %}
Download the distribution package with the updated module (any archive matching **your script version**) from the **"[Your Scripts](https://premiumexchanger.com/uscripts/)"** section in your personal account.

<figure><img src="../../.gitbook/assets/image (2025).png" alt="" width="563"><figcaption></figcaption></figure>

Extract the downloaded archive on your computer and locate the folder with the required merchant module at the specified path:

<figure><img src="../../.gitbook/assets/image (2023).png" alt="" width="563"><figcaption></figcaption></figure>

Or the auto-payout module:

<figure><img src="../../.gitbook/assets/image (2089).png" alt="" width="563"><figcaption></figcaption></figure>

Upload the module files to your server in the `/wp-content/plugins/premiumbox/merchants` directory (for payment acceptance) or `/wp-content/plugins/premiumbox/paymerchants` directory (for auto-payouts). If a file conflict prompt appears, overwrite the existing files.
{% endtab %}
{% endtabs %}

## Standard Script Design Files

1. Download the script archive **for updating** from the [**Your Scripts**](https://premiumexchanger.com/uscripts/) page for <mark style="color:red;">**your script version**</mark> (any PHP version) and extract it on your computer.

<figure><img src="../../.gitbook/assets/image (2032).png" alt="" width="563"><figcaption></figcaption></figure>

2. Navigate to the directory path shown in the screenshot containing the design files: `/wp-content/themes/`

<figure><img src="../../.gitbook/assets/image (2031).png" alt="" width="563"><figcaption></figcaption></figure>

4. Select the desired design folder (`newexchanger2.0` — the new standard design for 2024) and drag it into the ISP Manager window, placing it in the corresponding directory.

<figure><img src="../../.gitbook/assets/themes_240406131513.png" alt=""><figcaption></figcaption></figure>

5. If a file conflict window appears, choose to overwrite the files by clicking the "**Replace**" button.

<figure><img src="../../.gitbook/assets/изображение (66).png" alt=""><figcaption></figcaption></figure>

7. Activate the uploaded design in the website control panel under "**Appearance -> Themes**."

<figure><img src="../../.gitbook/assets/Темы ‹ Обменник — WordPress - Google Chrome_240406131708.png" alt=""><figcaption></figcaption></figure>

8. Additional appearance settings may be required after activating the new design on your site. The main design settings can be found in the subsections under "**Appearance**."

## Script Files

1. Download the script update archive from the [**"Your Scripts"** page](https://premiumexchanger.com/uscripts/) for <mark style="color:red;">**your script version**</mark> (any PHP version) and extract the archive on your computer.

<figure><img src="../../.gitbook/assets/image (2029).png" alt="" width="563"><figcaption></figcaption></figure>

2. Navigate to the directory with the modules as shown in the screenshot: `/wp-content/plugins/premiumbox/`

<figure><img src="../../.gitbook/assets/image (2030).png" alt="" width="563"><figcaption></figcaption></figure>

3. Select one or more required directories and drag them into the ISP Manager window, placing them in the corresponding directory.

<figure><img src="../../.gitbook/assets/premiumbox_240501155622.png" alt=""><figcaption></figcaption></figure>

4. If a file conflict window appears, choose to overwrite the files by clicking the "**Replace**" button.

<figure><img src="../../.gitbook/assets/изображение (66).png" alt=""><figcaption></figcaption></figure>