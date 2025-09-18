# Server Error Log

## Option 1

In the ISP Manager panel, go to the "Websites" section and follow the steps shown in the screenshot:

<figure><img src="../../../.gitbook/assets/image (781).png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../../.gitbook/assets/image (782).png" alt=""><figcaption></figcaption></figure>

## Option 2

In the ISP Manager panel, navigate to the specified folder:

<figure><img src="../../../.gitbook/assets/image (803).png" alt=""><figcaption></figcaption></figure>

Look for the file **`your_domain.error.log`** in the list and open it.

<figure><img src="../../../.gitbook/assets/image (783).png" alt="" width="397"><figcaption></figcaption></figure>

{% hint style="info" %}
The log directory may be located in a different path on your server.

If you can't find the logs at the specified path, use the search function:\
\
In the root folder, click "Search"\
![](<../../../.gitbook/assets/изображение (54).png>)

In the window that opens, enter **logs** in the "Name Mask" field, check the box for "**Search in subdirectories**," and click "**Find**":\
![](<../../../.gitbook/assets/изображение (79).png>)

In the search results window, open the folder containing the logs:\
![](<../../../.gitbook/assets/изображение (154).png>)
{% endhint %}

## Configuring Log Output

If the log file is missing or the file is empty, enable error reporting in your PHP settings (select the version your site is running on):

<figure><img src="../../../.gitbook/assets/image (799).png" alt=""><figcaption></figcaption></figure>

It is also recommended to enable error reporting in the `wp-config.php` file located in the root folder of your site:

<figure><img src="../../../.gitbook/assets/image (800).png" alt=""><figcaption></figcaption></figure>

Open the file, [replace **false** with **true**](#user-content-fn-1)[^1] in the specified location, and save your changes.

<figure><img src="../../../.gitbook/assets/image (801).png" alt=""><figcaption></figcaption></figure>

[^1]: If it was originally set to true, error logging was already enabled, and no changes to the file are necessary.