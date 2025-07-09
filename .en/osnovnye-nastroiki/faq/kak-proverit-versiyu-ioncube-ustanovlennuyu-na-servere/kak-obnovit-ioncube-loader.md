# How to Update ionCube Loader

1. Install PHP 8.1 on your server via the ISP Manager control panel as the **root user** by going to **Settings -> Software Configuration**.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_22_13.png" alt=""><figcaption></figcaption></figure>

2. Download the latest version of [ionCube Loader](https://www.ioncube.com/loaders.php) to your PC and extract the archive.

<figure><img src="../../../.gitbook/assets/image (2008).png" alt="" width="563"><figcaption></figcaption></figure>

3. Log into ISP Manager as the **root user** and open the file manager.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-01_22_06_12.png" alt=""><figcaption></figcaption></figure>

4. Using the file manager, navigate to the directory `/opt/php81/lib/php/modules/` (the exact path on your server may differ—if it does, please check with your hosting support for the correct location). Upload the file **ioncube_loader_lin_8.1.so** from the extracted archive to this folder, replacing the existing file.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_18_28.png" alt=""><figcaption></figcaption></figure>

5. Go to **Settings -> PHP Settings**, then open **Basic PHP Settings** for PHP 8.1.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_27_58.png" alt=""><figcaption></figcaption></figure>

6. Configure the settings as shown in the screenshot below and save your changes.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_28_32 (1).png" alt=""><figcaption></figcaption></figure>

7. Open the **Extension Management** section for PHP 8.1.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_31_07.png" alt=""><figcaption></figcaption></figure>

8. Make sure to disable and then re-enable the ionCube module to properly activate the new version.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_31_54.png" alt=""><figcaption></figcaption></figure>

9. Finally, in the **Sites** section, enable PHP 8.1 for your website.

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_39_14.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/Clip2net_2023-04-02_20_39_43.png" alt=""><figcaption></figcaption></figure>