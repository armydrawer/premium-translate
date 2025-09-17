# Removing Electrum from the Server

1. In the ISP Manager control panel, go to the **"Sites"** section. Select the desired site by clicking on it, then click **"Log in as owner"**.

    <figure><img src="../../.gitbook/assets/изображение (89).png" alt=""><figcaption></figcaption></figure>

2. Open the **"File Manager"** section.

    <figure><img src="../../.gitbook/assets/изображение (166).png" alt="" width="330"><figcaption></figcaption></figure>

3. Delete the **Electrum** folder.

    <figure><img src="../../.gitbook/assets/изображение (91).png" alt="" width="375"><figcaption></figcaption></figure>

4. Open the **"Cron Scheduler"** section.

    <figure><img src="../../.gitbook/assets/изображение (148).png" alt="" width="305"><figcaption></figcaption></figure>

5. Delete any cron jobs created for Electrum.

    <figure><img src="../../.gitbook/assets/image (1450).png" alt=""><figcaption></figcaption></figure>

6. <mark style="color:red;">Make sure to restart the server.</mark>