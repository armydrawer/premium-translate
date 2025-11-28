# How to Update ionCube Loader

1. Install PHP 8.1 on your server via the ISP Manager control panel under the **root user** in the "**Settings -> Software Configuration**" section.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_22_13 (1).png" alt=""><figcaption></figcaption></figure>

2. Download the latest version of [ionCube Loader](https://www.ioncube.com/loaders.php) to your computer and extract the archive.

<figure><img src="../../../../.gitbook/assets/image (673) (1).png" alt="" width="563"><figcaption></figcaption></figure>

3. Log in to the ISP Manager control panel as the **root user** and open the file manager.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-01_22_06_12 (1).png" alt=""><figcaption></figcaption></figure>

4. Using the file manager, navigate to the directory `/opt/php81/lib/php/modules/` (the path on your server may differ — if it does, contact your hosting provider's support team to confirm the correct path). Upload the **ioncube\_loader\_lin\_8.1.so** file from the extracted archive to the server, replacing the existing file.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_18_28 (1).png" alt=""><figcaption></figcaption></figure>

5. Go to the "**Settings -> PHP Settings**" section and open "**PHP Core Settings**" for version 8.1.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_27_58 (1).png" alt=""><figcaption></figcaption></figure>

6. Configure the settings as shown in the screenshot below and save them.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_28_32.png" alt=""><figcaption></figcaption></figure>

7. Open the "**Extension Management**" section for PHP 8.1.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_31_07 (1).png" alt=""><figcaption></figcaption></figure>

8. Make sure to disable and then re-enable the ionCube module to properly activate the new version.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_31_54.png" alt=""><figcaption></figcaption></figure>

9. In the "**Sites**" section, activate PHP 8.1 for your website.

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_39_14 (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/Clip2net_2023-04-02_20_39_43.png" alt=""><figcaption></figcaption></figure>
