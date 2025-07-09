# How to Password-Protect a Website

### Creating a File with Username and Password

Log in to the ISPmanager Shell client as the <mark style="color:red;">root user</mark>.

<figure><img src="../../.gitbook/assets/image (1) (1).png" alt=""><figcaption></figcaption></figure>

Run the following command, replacing the username with your desired one (in this example, the username is `sysadmin`):  
```sh
sh -c "echo -n 'sysadmin:' >> /etc/nginx/.htpasswd"
```

<figure><img src="../../.gitbook/assets/image (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Next, run this command to encrypt the password:  
```sh
sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"
```

<figure><img src="../../.gitbook/assets/image (2) (1).png" alt=""><figcaption></figcaption></figure>

**After running this command, you will be prompted to enter and confirm the password — type your desired password.**

The username and password file setup is now complete.

### Configuring the nginx Configuration File:

As the root user, go to the "Sites" tab and select "Configuration files" from the menu.

<figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

In the configuration file, locate the `location` block inside the `server ssl` block (usually near the end of the file), and add the following lines:

```
allow 123.123.123.123;
deny all;

auth_basic "Restricted Access";
auth_basic_user_file /etc/nginx/.htpasswd;

satisfy any;
```

<figure><img src="../../.gitbook/assets/image (2178).png" alt=""><figcaption></figcaption></figure>

**Note: The IP address `123.123.123.123` is the IP of your web server — replace it with your actual server IP!**

Save the changes and reload the server.

<figure><img src="../../.gitbook/assets/image (2177).png" alt=""><figcaption></figcaption></figure>

To disable password protection on the site, remove the above lines (the ones you added), save the file, and reload the server.