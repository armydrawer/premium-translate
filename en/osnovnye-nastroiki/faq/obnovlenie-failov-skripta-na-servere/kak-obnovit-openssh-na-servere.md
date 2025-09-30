# How to Update OpenSSH on a Server?

{% hint style="danger" %}
On July 1, 2024, cybersecurity experts from Qualys disclosed a critical vulnerability in OpenSSH (affecting versions >= 8.5 and < 4.4), identified as CVE-2024-6387, also known as "regreSSHion." This vulnerability allows remote code execution with root privileges on servers and personal computers using the standard Glib library.
{% endhint %}

## Updating the Module

{% hint style="danger" %}
Make sure to update the module to the latest version — this will significantly enhance your server's security!
{% endhint %}

In your server's console or via the Shell client in the ISP Manager control panel, execute the following command as <mark style="color:red;">**root**</mark>:

```bash
apt update && apt install --only-upgrade openssh-client openssh-server openssh-sftp-server -y
```

<figure><img src="../../../.gitbook/assets/image (1786)_eng.png" alt=""><figcaption></figcaption></figure>

Once you've completed these steps, the module will be successfully updated.