# How to Protect a Website with a Password

### Creating a File with a Username and Password

Log in to the Shell client in **ISPmanager** as the <mark style="color:red;">root user</mark>.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Run the following command, specifying the username (in this example, we’ll use `sysadmin`):  
`sh -c "echo -n 'sysadmin:' >> /etc/nginx/.htpasswd"`

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

Next, execute the command to encrypt the password:  
`sh -c "openssl passwd -apr1 >> /etc/nginx/.htpasswd"`

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

**The system will then prompt you to enter and confirm the password — provide the desired password.**

The username and password file setup is now complete.

---

### Configuring the Nginx Configuration File

Log in as the root user, navigate to the **"Sites"** section, and select **"Configuration files"** from the menu.

<figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>

In the configuration file, locate the `location` block inside the `server ssl` block (usually at the end of the file). Add the following lines:

```
allow 123.123.123.123;
deny all;

auth_basic "Restricted Access";
auth_basic_user_file /etc/nginx/.htpasswd;

satisfy any;
```

<figure><img src="../../.gitbook/assets/image (2178).png" alt=""><figcaption></figcaption></figure>

**Note:** Replace `123.123.123.123` with the actual IP address of your server (this will vary in your case).  

Save the changes and restart the server.

<figure><img src="../../.gitbook/assets/image (2177).png" alt=""><figcaption></figcaption></figure>

---

### Disabling Password Protection

To disable password protection for the website, simply remove the lines related to authentication (lines 2–5 in the example above), save the changes, and restart the server.