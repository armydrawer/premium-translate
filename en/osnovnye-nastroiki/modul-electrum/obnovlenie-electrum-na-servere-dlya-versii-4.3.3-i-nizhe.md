# Updating Electrum on the Server (for version 4.3.3 and earlier)

{% hint style="danger" %}
The latest supported version of Electrum as of now is **4.4.6**.

If you already have this version installed, this guide is not relevant for you.
{% endhint %}

1. In the ISP Manager control panel, go to the "**Sites**" section, select the desired site by clicking on it, and then click **"Log in as owner"**. You will be logged in as the <mark style="color:green;">user created for the site.</mark>

    <figure><img src="../../.gitbook/assets/изображение (184).png" alt=""><figcaption></figcaption></figure>

2. Open the "**File Manager**" section.

    <figure><img src="../../.gitbook/assets/изображение (98).png" alt="" width="330"><figcaption></figcaption></figure>

3. Navigate to the folder `/Electrum/Electrum-X.X.X/`, where `X.X.X` represents the version number of Electrum installed on the server at the time.

    <figure><img src="../../.gitbook/assets/image (1362).png" alt=""><figcaption></figcaption></figure>

4. Download Electrum version 4.4.6 from the [official website](https://download.electrum.org/4.4.6/).

5. Upload the contents of the downloaded archive to the server in the directory mentioned in step 3, replacing the existing files.

{% hint style="warning" %}
Make sure to upload the files and folders to the server exactly as shown in the screenshot below.
{% endhint %}

    <figure><img src="../../.gitbook/assets/image (1363).png" alt=""><figcaption></figcaption></figure>

When prompted about file conflicts, confirm the replacement of the existing files.

    <figure><img src="../../.gitbook/assets/image (1364).png" alt=""><figcaption></figcaption></figure>

6. **Make sure** to restart the server after updating the files.