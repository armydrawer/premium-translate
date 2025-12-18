# "Raffle" Page

The "Raffle" module allows the administrator to set up and manage the promotional section of the contest on the currency exchange website. This section encourages users to leave feedback about the service while participating in weekly prize draws.

{% hint style="info" %}
How to use the module:

1. **Activate the section**: Set the raffle display to "show"
2. **Basic settings**: Fill in the title, description, and configure the participation button
3. **Set the timer**: Specify the end date for the current raffle
4. **Statistics**: Update the number of reviews and the total prize pool
5. **Rules**: Edit the HTML content with detailed participation conditions
6. **Platforms**: Configure the list of recommended sites for reviews
7. **Save**: Click the "Save" button after making changes
{% endhint %}

To configure the text for the banner, go to "**Appearance**" ➔ "**Homepage**" ➔ "**Banners**".

<figure><img src="../../.gitbook/assets/image (2042).png" alt="" width="563"><figcaption></figcaption></figure>

In the settings for the "**Raffle**" page under the "**Pages**" section, make sure to select the appropriate template (Promo page template) for proper page display.

<figure><img src="../../.gitbook/assets/image (2125).png" alt="" width="253"><figcaption></figcaption></figure>

To set up the text on the Raffle page (`https://your_domain/promo/`), go to "**Appearance**" ➔ "**Raffle**".

<figure><img src="../../.gitbook/assets/image (2207).png" alt="" width="563"><figcaption></figcaption></figure>

### **Displaying the Raffle**

* **Function**: Enable/disable the raffle section on the public website
* **Options**: `hide` / `show`
* **Action**: Select the desired option and click the **Save** button

### **Configuring Raffle Content**

**Raffle Title**

* Field for bilingual input (Russian/English)
* Example: "Leave a Review"
* Displays as the main call to action

**Raffle Description**

* Brief description of participation conditions
* Example: "Join the raffle every week!"
* Supports both Russian and English languages

**Participation Button**

* **Button Link**: URL to the feedback form
* **Button Text**: Text on the button (Russian/English)
* **Image**: Path to the image for visual design
  * Format: `/wp-content/themes/newexchanger2.0/images/promo/promo.svg`

### **Timer Settings**

**Timer Title**

* Text above the countdown
* Example: "Until the contest ends"
* Bilingual support

**End Date**

* Input format: `DD.MM.YYYY`
* Example: `16.11.2024`
* Automatic countdown to the specified date

### **Review Statistics Block**

**"Reviews" Block Title**

* Name of the section with statistics
* Example: "Reviews"

**Number of Reviews**

* Numeric field to display the current count
* Format: `00000` (five-digit number with leading zeros)

### **Prize Pool Block**

**"Bank" Block Title**

* Name of the section with prize information
* Example: "Contest Bank"

**Total Prize Money**

* Displays the total amount of prizes
* Format: `00000 ₽` (with currency indication)

### Advanced Settings

### **Raffle Rules**

Block with an HTML editor for detailed description of participation conditions:

**Available HTML Tags**:

* `div`, `span`, `br`, `p` - structural elements
* `a` - links
* `img` - images
* `b`, `i`, `u`, `del` - text formatting
* `ul`, `ol`, `li` - lists
* `H2`, `H3` - headings

**Special Variables**:

* Anti-spam
* Text color
* Year
* Registration link
* Login link
* Image

**Example of Rules Structure**:

```
<h2>Winning money is very easy</h2>
<ul>
  <li><span>Make an exchange on our site</span> <a href="">Exchange</a></li>
  <li><span>Leave a review about our service, including your application number</span> <a href="" class="review">Leave a Review</a></li>
  <li><span>Check your email, open the message from BestChange, and activate your review by following the link</span></li>
</ul>
<p>You can check the raffle results <a href="">on our Telegram channel</a>. You can participate in the raffle an unlimited number of times! Good luck!</p>
<div>
  <p>Last week's winner</p>
  <p class="user_mail">p****rii@gmail.com</p>
</div>
```

### **List of Review Platforms**

HTML block with a list of recommended sites for posting reviews:

**Categories of Platforms**:

1. **Review Sites**:
   * mywot.com
   * trustpilot.com
   * webproverka.com
2. **Forums**:
   * mmgp.com
   * forum.bits.media
   * bitcointalk.org
3. **Monitoring Sites**:
   * kurs.expert
   * pro-obmen.ru

**List Structure**:

```
<h2>List of Platforms for Posting Reviews</h2>
<ul>
  <h3>Review Sites:</h3>
  <li><span>mywot.com</span><a href="domain">Leave a Review</a></li>
  <li><span>trustpilot.com</span><a href="domain">Leave a Review</a></li>
</ul>
```

Links should be inserted according to HTML markup rules in the [A](https://htmlbook.ru/html/A) tag within quotes.

```
Example:  <a href="https://your_domain/">Exchange</a>
```

<figure><img src="../../.gitbook/assets/image (2124).png" alt="" width="563"><figcaption></figcaption></figure>

Also, don't forget to add the English translation text.

<figure><img src="../../.gitbook/assets/image (2045).png" alt="" width="563"><figcaption></figcaption></figure>