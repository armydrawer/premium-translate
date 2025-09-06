# Payeer

## Настройки в личном кабинете мерчанта

1. Пройдите регистрацию/авторизацию в системе [Payeer](https://payeer.com/).
2. Пройдите верификацию аккаунта в разделе "**Профиль и верификация**" для использования API.
3. Перейдите в раздел "**API**" и нажмите кнопку "**Добавить**". Заполните указанные поля и нажмите "**Добавить мерчант**".

<figure><img src="../../../.gitbook/assets/image (1594).png" alt=""><figcaption></figcaption></figure>

Пройдите процедуру подтверждения вашего домена.

<figure><img src="../../../.gitbook/assets/image (1013).png" alt="" width="524"><figcaption></figcaption></figure>

Заполните открывшуюся форму.

<figure><img src="../../../.gitbook/assets/image (902).png" alt="" width="459"><figcaption></figcaption></figure>

* **URL успешной оплаты (SUCCESS URL)** — `https://ВАШ_ДОМЕН/merchant-payeer_success.html`
* **URL неуспешной оплаты (FAIL URL)** — `https://ВАШ_ДОМЕН/merchant-payeer_fail.html`
* **URL обработчика (RETURN URL)** — `https://ВАШ_ДОМЕН/merchant-payeer_status.html`

Вместо **`ВАШ_ДОМЕН`** укажите имя домена вашего обменного пункта. Если вы добавили хэш для **URL обработчика (RETURN URL)** в настройках модуля мерчанта, то укажите URL с хэшем.

<figure><img src="../../../.gitbook/assets/image (1595).png" alt=""><figcaption></figcaption></figure>

Отправьте магазин на модерацию, чтобы он смог принимать платежи.

## Настройки модуля

В панели администратора в разделе "**Мерчанты**" -> "**Мерчанты"** нажмите кнопку "**Добавить**" и выберите Payeer.

<figure><img src="../../../.gitbook/assets/image (1596).png" alt="" width="466"><figcaption></figcaption></figure>

Заполните указанные авторизационные поля.

<figure><img src="../../../.gitbook/assets/image (1597).png" alt="" width="450"><figcaption></figcaption></figure>

**Секретный ключ** — ключ, указанный в личном кабинете Payeer при создании магазина

**ID магазина** — ID магазина из личного кабинета Payeer&#x20;

## Продолжение настройки

Далее произведите настройку мерчанта следуя [общей инструкции по настройке](https://premium.gitbook.io/rukovodstvo-polzovatelya/osnovnye-nastroiki/merchanty-i-avtovyplaty/merchanty/obshie-nastroiki-merchantov).
