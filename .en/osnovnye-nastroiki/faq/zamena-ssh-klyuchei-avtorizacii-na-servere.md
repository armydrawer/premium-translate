# Replacing SSH Authorization Keys on the Server

The commands below should be executed through the ISP Manager control panel as the root user. This guide will help you replace the SSH keys used for SSH/SFTP authentication on your server.

1. Log in to the ISP Manager control panel as the root user.
2. Navigate to **Administration -> Shell Client**.

<figure><img src="../../.gitbook/assets/spaces_m9kqZXsNykrN6VyxxXBO_uploads_3rinLIMnpcghlMNMVkFk_изображение.webp" alt=""><figcaption></figcaption></figure>

3. Right-click on the blank terminal screen and select **Paste from browser** from the context menu.

<figure><img src="../../.gitbook/assets/spaces_m9kqZXsNykrN6VyxxXBO_uploads_9M75rlvamo44ybnN49r0_изображение.webp" alt=""><figcaption></figcaption></figure>

4. Enter the command in the window that appears and click **OK**. Then press **Enter** to execute the command.
5. Repeat steps 3 and 4 for each command listed below, executing them one by one.
6. The list of commands to run (you can use the copy icon on the right when hovering over a command):

```bash
rm ~/.ssh/authorized_keys
```

```bash
ssh-keygen -m PEM -t rsa -b 2048 -f ~/PRIVATE_SSH_KEY -q -N ""
```

```bash
puttygen ~/PRIVATE_SSH_KEY -o ~/PRIVATE_SSH_KEY.ppk -O private
```

```bash
touch ~/.ssh/authorized_keys
```

```bash
cat ~/PRIVATE_SSH_KEY.pub >> ~/.ssh/authorized_keys
```

```bash
rm -f ~/PRIVATE_SSH_KEY.pub
```

7. Go to the **File Manager** section and open the **root** folder.

<figure><img src="../../.gitbook/assets/Clip2net_230629214730.png" alt=""><figcaption></figcaption></figure>

8. Download the two SSH key files to your computer:

- `PRIVATE_SSH_KEY` — use this for macOS/Linux  
- `PRIVATE_SSH_KEY.ppk` — use this for Windows

<figure><img src="../../.gitbook/assets/Clip2net_230629214819.png" alt=""><figcaption></figcaption></figure>

9. After downloading, delete the key files from the server.

<figure><img src="../../.gitbook/assets/Clip2net_230629214845.png" alt=""><figcaption></figcaption></figure>

10. Test your SSH/SFTP connection using the new keys to confirm everything is working correctly.