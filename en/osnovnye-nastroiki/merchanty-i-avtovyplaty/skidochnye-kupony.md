---
layout:
  width: default
  title:
    visible: true
  description:
    visible: false
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
  metadata:
    visible: true
---

# Discount Coupons

### Feature Overview

The discount coupon editing module allows administrators to manage promotional campaigns and discount programs. This functionality provides flexible options for configuring and controlling coupon campaigns to encourage customer engagement.

<figure><img src="../../.gitbook/assets/image (2211)_eng.png" alt="" width="388"><figcaption></figcaption></figure>

### Key Coupon Parameters

Coupon Code:

* **Format:** Alphanumeric code (using Latin letters) without special characters
* **Example:** `1q2w3e4r5t!`
* **Restrictions:** Unique code for the entire system; the code cannot be changed after the coupon is created.

Discount Percentage:

* **Format:** An integer from 1 to 100. Example: `15` (corresponds to a 15% discount)

Coupon Type:

* **One-time Use** — can be used only once
* **Reusable** — can be used an unlimited number of times

Usage Status:

* **No** — the coupon has not been used yet
* **Yes** — the coupon has been activated by the customer

Publication Status:

* **Published** — the coupon is active and available for use
* **Under Review** — the coupon has been created but not activated

After creating the coupons, activate their use in the settings of each exchange direction where the coupons will be applied.

<figure><img src="../../.gitbook/assets/image (2208)_eng.png" alt="" width="551"><figcaption></figcaption></figure>

After this, an optional field will appear in the exchange form, where customers with a coupon can activate it and receive the corresponding discount.

<figure><img src="../../.gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="526"><figcaption></figcaption></figure>

If an incorrect or non-existent coupon is entered, the customer will see a warning immediately without having to submit a request.

<figure><img src="../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1) (1) (1) (1)_eng.png" alt="" width="219"><figcaption></figcaption></figure>