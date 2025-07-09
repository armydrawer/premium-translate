# How to Update OpenSSH on Your Server

{% hint style="danger" %}
On July 1, 2024, cybersecurity experts from Qualys disclosed a critical vulnerability in OpenSSH (versions >= 8.5 and < 9.4) identified as CVE-2024-6387, nicknamed regreSSHion. This flaw allows remote code execution with root privileges on servers and user PCs using the standard Glibc library.
{% endhint %}

## Module Update

{% hint style="danger" %}
Be sure to update the module to the latest version — this will significantly improve your server’s security!
{% endhint %}

In your server console or the ISP Manager control panel’s shell client, run the following command as <mark style="color:red;">**root**</mark>:

```bash
apt update && apt install --only-upgrade openssh-client openssh-server openssh-sftp-server -y
```

<figure><img src="../../.gitbook/assets/image (1786).png" alt=""><figcaption></figcaption></figure>

After completing these steps, the OpenSSH module will be updated.