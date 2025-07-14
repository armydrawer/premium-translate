# Beribit

## Beribit

We recommend keeping a small reserve of each cryptocurrency involved in trading. This helps cover shortfalls caused by rounding during calculations and transfers between accounts, and also allows for quick response to sudden changes in withdrawal fees. It’s important to keep in mind that having a small buffer can be useful in case of unexpected situations.

### Settings in Your Exchange Account <a href="#settings-in-exchange-account" id="settings-in-exchange-account"></a>

Register or log in to the [Beribit exchange](https://web.archive.org/web/20240522164757mp_/https://beribit.com/).

Go to the "**My Profile**" section and complete the account verification process.

Fill out the form that appears:

![](https://web.archive.org/web/20240522164757im_/https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FuGxORuTq49PMqzpxwvDv%252Fimage.png%3Falt%3Dmedia%26token%3D9a9cdc3e-af1a-4733-9f2a-bb917ef7f2a0\&width=768\&dpr=4\&quality=100\&sign=82b3cc4b6be606803480fb3adf7dd31a7f3fa808a9e566e8adcddec005859e7f)

After your account is verified, contact [customer support](https://web.archive.org/web/20240522164757mp_/https://t.me/beribitbot) on Telegram to receive your API access keys.

### Trading Actions Module Settings <a href="#trading-actions-module-settings" id="trading-actions-module-settings"></a>

Go to "**Trading Actions -> Add Action**," enter a name for the trading action in the "**Title**" field, select Beribit from the "**Module**" dropdown menu, leave the status as "**Active Action**," and click "**Save**."

![](https://web.archive.org/web/20240522164757im_/https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252Fgq8ZQmrhbqB84ihn5NOm%252Fimage.png%3Falt%3Dmedia%26token%3D29f8aec8-97ba-4f05-8aa9-5511fd3fc378\&width=768\&dpr=4\&quality=100\&sign=938eef1442b82f3236b7db432f4c16cc10e3c05ff2e020611ec91ef50869e259)

Fill in the authorization fields with the data provided by the exchange’s support team.

Here is a natural, fluent English translation of the provided text:

---

# General Instructions for Configuring Trading Action Parameters

In this module, you can create one of two actions — "**Sell**" or "**Buy**."

---

### "**Sell**" Action Settings

![Sell Action Settings](https://web.archive.org/web/20240522164757im_/https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FlREukg3VB3tb8RdZaUl2%252Fimage.png%3Falt%3Dmedia%26token%3D05efbb3e-eb8f-4858-8859-84e413b3d8dd&width=768&dpr=4&quality=100&sign=84c045573632ad6f362164160d68454b561dbe342e2c15bd48fd5f538dcb3d29)

---

### "**Buy**" Action Settings

![Buy Action Settings](https://web.archive.org/web/20240522164757im_/https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FihuX5GSKIGu9uqItuDGY%252Fimage.png%3Falt%3Dmedia%26token%3D88ff681c-f1df-493a-92bc-5b95a36f16f7&width=768&dpr=4&quality=100&sign=48be5f781cbf30468c3f6c60b6a9987ef53987221fd5bffc2d9f110255e9502d)

---

* The "**Sell**" action is suitable when you want to convert the currency received from a client’s order into the stablecoin USDT (or another currency you find appropriate). To receive funds from the client directly on Beribit, you can use the [Beribit Receiving Module](https://web.archive.org/web/20240522164757mp_/https://premium.gitbook.io/main/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/beribit).

* The "**Buy**" action is suitable when you do not want to keep a reserve of the payout currency in your exchange accounts and plan to purchase the currency for payout only when a client places an order to buy that currency from your exchange.

For the action to work correctly, it is essential to select the currencies you intend to work with in the "**Currency Code**" and "**Trading Currency Code**" fields.

---

If you need the link or additional context translated, just let me know!

Here is a natural English translation of the provided text:

---

* **Currency Code** — the currency that:  
  • will be sold in the "**Sell**" action (to buy the currency specified in the **"Trading Currency Code"** field)  
  • will be bought in the "**Buy**" action (to sell the currency specified in the **"Trading Currency Code"** field)

* **Trading Currency Code** — the currency that:  
  • will be bought in the "**Sell**" action (when selling the currency specified in the **"Currency Code"** field)  
  • will be sold in the "**Buy**" action (to buy the currency specified in the **"Currency Code"** field)

The list of currency pairs available for trading is provided on the [page](https://web.archive.org/web/20240522164757mp_/https://api.beribit.com/markets).

---

List of pairs: **USDT/RUB and vice versa, ETH/USDT and vice versa, BTC/USDT and vice versa, BNB/USDT and vice versa, TRX/USDT and vice versa**

If you select currencies that do not form a pair from the list above, the trading action will definitely return an error (No trade pairs XXX_YYY or YYY_XXX in api) when attempting to execute.

---

#### Example 1 — "Sell" action <a href="#primer-1-deistvie-prodat" id="primer-1-deistvie-prodat"></a>

Suppose you want to exchange TRX for BTC. You want to automatically sell incoming TRX from a client for USDT.

To do this, create a "**Sell**" trading action and activate it for the TRX - BTC direction. Set the action to trigger "After status 'Paid order'" and check the box for the TRX - BTC exchange direction.

---

If you need any further clarification or adjustments, feel free to ask!

Here is a natural English translation of the provided text:

---

With these settings, the value will be taken from the "**You Give**" amount (the actual payment amount from the client) and sold for USDT on the Beribit exchange after the order status changes to "**Paid**."

#### Example 2 – Action "**Buy**" <a href="#example-2-action-buy" id="example-2-action-buy"></a>

Suppose you have an exchange direction TRX → BTC. You want to automatically buy BTC either to pay the client or to hedge using the USDT balance available in your account.

To do this, you need to create a trading action "**Buy**" and activate it for the TRX → BTC direction. Then select the trigger "After order status changes to 'Paid'" and check the box for the TRX → BTC exchange direction.

---

Let me know if you want me to translate or adapt anything else!

With these settings, the amount specified in the "**You Receive**" field will be used to purchase the corresponding amount of BTC with USDT on the Beribit exchange once the order status changes to "**Paid**."

![](https://web.archive.org/web/20240522164757im_/https://premium.gitbook.io/~gitbook/image?url=https%3A%2F%2F2574066779-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fm9kqZXsNykrN6VyxxXBO%252Fuploads%252FerTQuhVccG1JwSiAULWX%252Fimage.png%3Falt%3Dmedia%26token%3D86e996d7-7359-4452-94c5-13782c2af6f7&width=768&dpr=4&quality=100&sign=387da92272cdd16dd0e07d43ae4d358f958f9dedc6339fb875fc8fc3725204cc)