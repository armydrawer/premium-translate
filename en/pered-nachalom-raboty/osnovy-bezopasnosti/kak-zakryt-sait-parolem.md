# How to Password Protect a Website

### Creating a File with Username and Password

Log into the Shell client in ISPmanager as the <mark style="color:red;">root user</mark>.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Run the following command, specifying the username (in this example, we'll use the username sysadmin):\
`sh -c "echo -n 'sysadmin:' >> /etc/nginx/.htpasswd"`

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Next, run the command to encrypt the access password:\
`sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"`

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**After this, the system will prompt you to enter and confirm the password—please provide them.**

The setup for the username and password file is complete.

### Configuring the Nginx Configuration File:

As the root user, go to the "Sites" tab and select "Configuration files" from the menu.

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

In the configuration file, locate the location block within the server ssl block (at the end of the file) and insert the following lines:

```
allow 123.123.123.123;
deny all;

auth_basic "Restricted Access";
auth_basic_user_file /etc/nginx/.htpasswd;

satisfy any;
```

<figure><img src="../../.gitbook/assets/image (2178).png" alt=""><figcaption></figcaption></figure>

**The IP address 123.123.123.123 is the server's address (web); it will be different in your case!**

After that, save the changes and reload the server.

<figure><img src="../../.gitbook/assets/image (2177).png" alt=""><figcaption></figcaption></figure>

To disable the password protection for the website, remove the lines (2), save the changes, and reload the server.