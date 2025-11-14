# Nginx and PHP-FPM Configuration Using ISP Manager

Log in to the ISP Manager panel as the <mark style="color:red;">**root user**</mark> and navigate to the "**Websites**" section. Enter the settings editing mode for your website.

<figure><img src="../../../ru/.gitbook/assets/image (707) (1).png" alt=""><figcaption></figcaption></figure>

In the "**PHP Handler**" block, select the handler and the version of PHP you want to use for your website.

PHP handlers in Apache, CGI, and FastCGI have different characteristics and efficiencies, which can affect the performance and security of web applications.

**Apache Module (mod\_php):**

* This method integrates PHP directly into the Apache server, allowing Apache to handle PHP scripts. This makes it fast and efficient, as there is no additional time required to start the PHP interpreter for each request.
* However, this can lead to security and isolation issues since all PHP scripts run in the context of the Apache server.

**CGI (Common Gateway Interface):**

* CGI is an older and less efficient way of processing PHP scripts. It starts the PHP interpreter for each request, which can be very resource-intensive, especially on high-traffic sites.
* The advantage of CGI is that it provides isolation between the PHP code and the web server, which can enhance security. However, due to the high system load, this method is rarely used today [1](https://blog.layershift.com/which-php-mode-apache-vs-cgi-vs-fastcgi/).

**FastCGI:**

* FastCGI is an improved version of CGI that addresses performance issues while retaining the security benefits of CGI. It allows the PHP interpreter to remain in memory, handling multiple requests, which significantly reduces system load.
* FastCGI offers better scalability and performance compared to CGI and mod\_php, especially on high-traffic sites. However, it does not allow the use of PHP directives in .htaccess files, which can be a limitation for some scenarios [1](https://blog.layershift.com/which-php-mode-apache-vs-cgi-vs-fastcgi/).

The choice between these methods depends on the specific requirements of your web application, including performance, security, and ease of configuration. FastCGI is often considered the best choice for modern web applications due to its balance between performance and security.

{% hint style="info" %}
The PHP version must match the version specified for the archive you downloaded.

<img src="../../../ru/.gitbook/assets/image (555) (1).png" alt="" data-size="original">
{% endhint %}

<figure><img src="../../../ru/.gitbook/assets/image (708) (1).png" alt="" width="563"><figcaption></figcaption></figure>

In the "**Optimization and DDoS Protection**" block, set the specified settings (in the list of file extensions for caching, make sure to remove "**js**").

<figure><img src="../../../ru/.gitbook/assets/image (709) (1).png" alt="" width="563"><figcaption></figcaption></figure>
