# Reserve from File

The script includes functionality to retrieve the reserve value for a currency from a file. You can create a text file where you store the reserve values, and this file will be used to display the reserve for the currency on the website.

---

### Steps to Set Up Reserve from a File:

1. **Activate the Module**  
   In the website's admin panel, go to **"Modules" → "Modules"**, and activate the module called **"Reserve Parser from File"**.

   <figure><img src="../../../.gitbook/assets/image (1008).png" alt=""><figcaption></figcaption></figure>

2. **Create a TXT File**  
   Create a `.txt` file and define the currency reserves in it. Enter each reserve value on a new line. Then, upload the `.txt` file to your server.  
   Example of file content:  
   ```
   Reserv 1 = 100000  
   Reserv 2 = 5000  
   Reserv 3 = 14000  
   ```

3. **Specify the File URL**  
   In the admin panel, go to **"Modules" → "Reserve from File"**, and specify the URL of the uploaded `.txt` file.

   <figure><img src="../../../.gitbook/assets/image (1073).png" alt=""><figcaption></figcaption></figure>

4. **Assign Reserve Values to Currencies**  
   - In the admin panel, navigate to **"Currencies"**, edit the desired currency, and for the **"Currency Reserve"** parameter, select the corresponding line number from the file. Save the changes.  
     <figure><img src="../../../.gitbook/assets/image (909).png" alt=""><figcaption></figcaption></figure>
   - Alternatively, in the **"Exchange Directions"** section, go to the **"Reserve"** tab and select the corresponding line number from the file. This allows you to set individual reserve values for each exchange direction.  
     <figure><img src="../../../.gitbook/assets/image (906).png" alt=""><figcaption></figcaption></figure>

5. **Set Up a Cron Job**  
   Configure a cron job to periodically fetch the reserve value from the file and update it on the website. The script can be run every minute.  
   Example of a cron command in Unix format for the ISP Manager control panel:  
   ```
   /usr/bin/wget -t 1 -O - http(s)://your_domain/request-fres.html
   ```

   {% hint style="info" %}
   The exact command may vary depending on your server. The part `/usr/bin/wget -t 1 -O -` might need to be adjusted. Contact your hosting provider's technical support for the correct command.
   {% endhint %}

   <figure><img src="../../../.gitbook/assets/image (1102).png" alt="" width="563"><figcaption></figcaption></figure>

---

Now, the reserve value for the currency on your website will always be fetched from the `.txt` file automatically.