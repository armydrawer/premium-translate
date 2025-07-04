#!/bin/bash

echo -e "\nСоздание директорий..."
mkdir -p electrum_in/Electrum-4.4.6/electrum_data/wallets electrum_out/Electrum-4.4.6/electrum_data/wallets

echo -e "\nСкачивание Electrum..."
wget --inet4-only https://download.electrum.org/4.4.6/Electrum-4.4.6.tar.gz

echo "Извлечение файлов из архива..."
tar -xzf Electrum-4.4.6.tar.gz --directory electrum_in
tar -xzf Electrum-4.4.6.tar.gz --directory electrum_out
rm Electrum-4.4.6.tar.gz

echo "Копирование крипто кошельков..."
cp default_wallet_in electrum_in/Electrum-4.4.6/electrum_data/wallets/default_wallet
cp default_wallet_out electrum_out/Electrum-4.4.6/electrum_data/wallets/default_wallet

echo -e "\nНастройки Electrum..."
ELECTRUM_PORT_IN=$(shuf -i 25000-34999 -n 1)
echo -e "electrum_in присвоен порт:  \c"
./electrum_in/Electrum-4.4.6/run_electrum setconfig rpcport $ELECTRUM_PORT_IN -P --offline

ELECTRUM_PORT_OUT=$(shuf -i 35000-45000 -n 1)
echo -e "electrum_out присвоен порт:  \c"
./electrum_out/Electrum-4.4.6/run_electrum setconfig rpcport $ELECTRUM_PORT_OUT -P --offline

source start_or_restart_electrum_daemon2.sh
# bash start_or_restart_electrum_daemon2.sh


echo -e "\n*** Данные для мерчанта Electrum на прием: ***"
echo "Login: user"
echo -e "Password: \c"
./electrum_in/Electrum-4.4.6/run_electrum getconfig rpcpassword -P --offline
echo "Api port: $ELECTRUM_PORT_IN"

echo -e "\n*** Данные для мерчанта Electrum на выплату ***"
echo "Login: user"
echo -e "Password: \c"
./electrum_out/Electrum-4.4.6/run_electrum getconfig rpcpassword -P --offline
echo "Api port: $ELECTRUM_PORT_OUT"
#echo "Wallet password: пароль от кошелька на выплату"
echo "Wallet password: " $WALLET_PASSWORD_OUT

echo -e "\nДобавьте в крон задание от имени пользователя с запуском каждые 30 минут:"
echo -e "sleep 15 && bash $(pwd)/start_or_restart_electrum_daemon2.sh"

echo -e "\nДобавьте в крон задание от имени пользователя с запуском после перезагрузки:"
echo -e "sleep 200 && bash $(pwd)/start_or_restart_electrum_daemon2.sh"