# "Giveaway" Page

The "Giveaway" module allows administrators to configure and manage the promotional block for a contest on the currency exchange website. This block encourages users to leave reviews about the service by participating in weekly prize giveaways.

{% hint style="info" %}
**How the module works:**

1. **Activate the block**: Set the giveaway display option to "show."
2. **Basic setup**: Fill in the title, description, and configure the participation button.
3. **Set the timer**: Specify the end date for the current giveaway.
4. **Statistics**: Update the number of reviews and the prize pool amount.
5. **Rules**: Edit the HTML content with detailed participation terms.
6. **Platforms**: Configure the list of recommended websites for reviews.
7. **Save changes**: Click the "Save" button after making adjustments.
{% endhint %}

The banner text settings can be found in the "**Appearance**" ➔ "**Homepage**" ➔ "**Banners**" section.

<figure><img src="../../.gitbook/assets/image (2042).png" alt="" width="563"><figcaption></figcaption></figure>

In the "**Giveaway**" page settings under the "**Pages**" section, make sure to select the appropriate template (Promo page template) for the page to display correctly.

<figure><img src="../../.gitbook/assets/image (2125).png" alt="" width="253"><figcaption></figcaption></figure>

The text settings for the Giveaway page (`https://your_domain/promo/`) are located in the "**Appearance**" ➔ "**Giveaway**" section.

<figure><img src="../../.gitbook/assets/image (2207).png" alt="" width="563"><figcaption></figcaption></figure>

---

### **Giveaway Display**

* **Function**: Enable/disable the giveaway block on the public website.
* **Options**: `hide` / `show`
* **Action**: Select the desired option and click the **Save** button.

---

### **Giveaway Content Settings**

**Giveaway Title**

* A field for bilingual input (Russian/English).
* Example: "Leave a Review."
* Displayed as the main call-to-action.

**Giveaway Description**

* A brief description of the participation terms.
* Example: "Participate in weekly giveaways!"
* Supports both Russian and English.

**Participation Button**

* **Button Link**: The URL leading to the review form.
* **Button Text**: The text displayed on the button (Russian/English).
* **Image**: Path to the image for visual design.
  * Format: `/wp-content/themes/newexchanger2.0/images/promo/promo.svg`

---

### **Timer Settings**

**Timer Title**

* Text displayed above the countdown timer.
* Example: "Time Left Until the Contest Ends."
* Supports bilingual input.

**End Date**

* Input format: `DD.MM.YYYY`
* Example: `16.11.2024`
* Automatically counts down to the specified date.

---

### **Review Statistics Block**

**"Reviews" Block Title**

* The name of the section displaying statistics.
* Example: "Reviews."

**Number of Reviews**

* A numeric field to display the current count.
* Format: `00000` (a five-digit number with leading zeros).

---

### **Prize Pool Block**

**"Prize Pool" Block Title**

* The name of the section displaying prize information.
* Example: "Contest Prize Pool."

**Prize Amount**

* Displays the total prize amount.
* Format: `00000 ₽` (with currency specified).

---

### Advanced Settings

### **Giveaway Rules**

A block with an HTML editor for detailed participation terms:

**Available HTML Tags**:

* `div`, `span`, `br`, `p` - structural elements.
* `a` - links.
* `img` - images.
* `b`, `i`, `u`, `del` - text formatting.
* `ul`, `ol`, `li` - lists.
* `H2`, `H3` - headings.

**Special Variables**:

* Anti-spam.
* Text color.
* Year.
* Registration link.
* Login link.
* Image.

**Example Rules Structure**:

```html
<h2>Winning Money is Easy</h2>
<ul>
  <li><span>Make an exchange on our website</span> <a href="">Exchange</a></li>
  <li><span>Leave a review about our service, including your order number</span> <a href="" class="review">Leave a Review</a></li>
  <li><span>Check your email, open the message from BestChange, and activate your review by clicking the link</span></li>
</ul>
<p>You can check the giveaway results <a href="">on our Telegram channel</a>. You can participate in the giveaway as many times as you like! Good luck!</p>
<div>
  <p>Last week's winner:</p>
  <p class="user_mail">p****rii@gmail.com</p>
</div>
```

---

### **List of Review Platforms**

An HTML block with a list of recommended websites for posting reviews:

**Platform Categories**:

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

```html
<h2>Recommended Platforms for Posting Reviews</h2>
<ul>
  <h3>Review Sites:</h3>
  <li><span>mywot.com</span><a href="domain">Leave a Review</a></li>
  <li><span>trustpilot.com</span><a href="domain">Leave a Review</a></li>
</ul>
```

Links are inserted according to HTML markup rules within the [A](https://htmlbook.ru/html/A) tag between quotation marks.

```html
Example: <a href="https://your_domain/">Exchange</a>
```

<figure><img src="../../.gitbook/assets/image (2124).png" alt="" width="563"><figcaption></figcaption></figure>

Don't forget to add the English translation for the text as well.

<figure><img src="../../.gitbook/assets/image (2045).png" alt="" width="563"><figcaption></figcaption></figure>