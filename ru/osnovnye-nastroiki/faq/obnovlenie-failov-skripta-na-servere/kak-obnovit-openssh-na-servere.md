# Как обновить OpenSSH на сервере?

{% hint style="danger" %}
1 июля 2024 года эксперты по ИБ из Qualys опубликовали информацию, что в OpenSSH (с версии >= 8.5 и < 4.4) обнаружена критическая уязвимость CVE-2024-6387 под названием regreSSHion. Она позволяет удалённо выполнить код с правами root на серверах и пользовательских ПК со стандартной библиотекой Glib.
{% endhint %}

## Обновление модуля

{% hint style="danger" %}
Обязательно обновите модуль до актуальной версии — это повысит уровень защиты сервера!
{% endhint %}

В консоли сервера или в Shell-клиенте панели управления сервером ISP Manager из-под <mark style="color:red;">**root**</mark> выполните следующую команду:

`apt update && apt install --only-upgrade openssh-client openssh-server openssh-sftp-server -y`

<figure><img src="../../../.gitbook/assets/image (1786).png" alt=""><figcaption></figcaption></figure>

После этих действий модуль будет обновлен.
