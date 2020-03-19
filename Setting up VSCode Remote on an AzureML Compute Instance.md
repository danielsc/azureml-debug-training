# Setting up VSCode Remote on an AzureML Compute Instance

## 0. Prerequisite (Windows only)
Install an OpenSSH compatible SSH client (https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client) if one is not already present.
Note: PuTTY is not supported on Windows since the ssh command must be in the path.

## 1. Generate Public/Private SSH keys on local computer
Linux:

Follow guide here: https://www.maketecheasier.com/generate-public-private-ssh-key/

Open the file manager and navigate to the .ssh directory. You should see two files: id_rsa and id_rsa.pub.
The **id_rsa.pub** will contain the public key
The **id_rsa** will contain the private key

Windows:

Follow guide on creating SSH Keys here: https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows

![](img/putty_key_gen_public.png)

The **public** key will look somewhat like this

    ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEA302l3JxEsI+Z6zCgCuNggWsAMMnIeGnZUlzUCQg8sMjfzvZGIU1xHgyd+iENJxbD+ZRoux1N5oQGyGTDtQuxQigR2ajsIr9NcQRIvIwmv4auaM/c3aSKi4zSeTIt9jlb1zOGCa5aNJJ8PiHAVws6y352DYPGT8j5yzSuxNZngYd9yvVyzXjAAwYPJ2u1a3bcOtXABFTSxofJjwtEBfBwA7Y1+Rtr/zSGdfUcmJny/QYtYqnFM2jTjmCuBckeLFNoNoruQd54qFz1ScLtz+6HavtlsBYseQgZjAGXLe2+eBhRJM7D8uSheAfHxZcDomp88JAPFiG6HT8GZ1M39nzvaw== rsa-key-20200318

The **private** key will look somewhat like this
Make sure you use the OpenSSH Format for Private Keys.
If you use PuttyGen export you keys in OpenSSH by clicking the Conversion Menu and export as OpenSSH.
![](img/putty_key_gen.png)

    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAr99EPm0P4CaTPT2KtBt+kpN3rmsNNE5dS0vmGWxIXq4vAWXD
    .....
    ewMtLnDgXWYJo0IyQ91ynOdxbFoVOuuGNdDoBykUZPQfeHDONy2Raw==
    -----END RSA PRIVATE KEY-----



Remember where you saved this **Public Key** you will be using it in the next step.

Remember where you saved this **Private Key** you will be using it in Step 4.

## 2. Create Compute Instance with Public Key
When creating Compute Instance, enable SSH and paste the Public Key you generated prior
![](img/enable_ssh.png)

## 3. Find Compute Instance access information
-  Go to https://ml.azure.com/, Click **Compute** and Click the SSH link. You should see a **SSH Details** pop out. 
![](img/vm_compute_ssh.png)

- Save the login details under **Login using local account**. We will use later

## 4. (Option 1) Create SSH config file with a script

1. Download the [script](https://raw.githubusercontent.com/danielsc/azureml-debug-training/master/src/create_ssh_config.py) and run the script on your local machine with `python create_ssh_config.py`
2. For your **IP Address**: 
    -  Go to https://ml.azure.com/, Click **Compute** and Click the SSH link. You should see a **SSH Details** pop out. 
    ![](img/vm_compute_ssh.png)
3. For your **Private Key**: 
    -  Find the private key you generate ([Follow steps abive](#1.-Generate-Public/Private-SSH-keys-on-local-computer)), it was generated when you created an SSH key for your Compute Instance.
    -  Copy the RSA Key "Private key" for that VM 
    -  Paste value in the terminal
    -  Press `Ctrl+z` and Enter(Windows) or `Ctrl+d` and Enter(Mac/Linux) to confirm Private Key
3. Skip to the **Install VS Code and connect to the Notebook VM** section of this document. Your VM should appear in VSCode with the IP address as the name.

## 4. (Option 2) Create SSH config file manually
### 1. Save Private SSH Keys in SSH config folder 

Save private key generated in **Generate Public/Private SSH keys on local computer** section of this document to the ~/.ssh/ directory on your local computer; for instance open an editor for a new file and paste the key in:

Linux:

    vi ~/.ssh/id_<host-name>_rsa 

Windows:

    notepad C:\Users\<username>\.ssh\id_<host-name>_rsa

The private key will look somewhat like this
    
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAr99EPm0P4CaTPT2KtBt+kpN3rmsNNE5dS0vmGWxIXq4vAWXD
    .....
    ewMtLnDgXWYJo0IyQ91ynOdxbFoVOuuGNdDoBykUZPQfeHDONy2Raw==
    -----END RSA PRIVATE KEY-----

Change permissions on file to make sure only you can read the file (not sure if this is needed on Windows)

    chmod 600 ~/.ssh/id_<host-name>_rsa  

### 2. Add the Notebook VM as a host
Open the file ~/.ssh/config (C:\Users\<username>\.ssh\config on Windows) in an editor and add a new entry:

    Host <host-name>
        HostName <IP-Address>
        Port 50000
        User azureuser
        IdentityFile ~/.ssh/id_<host-name>_rsa  
   
Here some details on the fields:

- `Host`: use whatever shorthand you like for the VM
- `HostName`: This is the IP address of the VM pulled from the above configuration page
- `Port`: This is the port shown on the above configuration page.
- `User`: this needs to be `azureuser`
- `IdentityFile`: should point to the file where you saved the privat key

Now you should be able to ssh to your Notebook VM using the shorthand you used above.

```
    MININT-LI90F99:git danielsc$ ssh mynotebookvm
    Welcome to Ubuntu 16.04.6 LTS (GNU/Linux 4.15.0-1041-azure x86_64)

    94 packages can be updated.
    0 updates are security updates.

    New release '18.04.2 LTS' available.
    Run 'do-release-upgrade' to upgrade to it.


    *** System restart required ***
    **********************************************************************
    * Welcome to the Linux Data Science Virtual Machine on Azure!        *
    *                                                                    *
    * For more information on available tools and features,              *
    * visit http://aka.ms/dsvm/discover.                                 *
    **********************************************************************

    Last login: Sun Jun 16 18:03:28 2019 from 172.58.43.244
    azureuser@danielsctestc7e12521ac:~$ 
```

## 4. Install VS Code and connect to the Compute Instance
Next install VS Code from here: https://code.visualstudio.com/ and then install the Remote SSH Extension from here: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh.

- Now, click on the Remote Explorer icon on the left
- Select SSH Targets from the Remote Explorer Dropdown
- Click the "+" sign
- Paste the login details from Compute Instance copied in Step 3

![](img/remote_debug_ssh.png)

From here on, you are entirely working on the Notebook VM and you can now edit, debug, use git, use extensions, etc. -- just like you can with your local VSCode. Notebook VM files are stored in `/home/azureuser/cloudfiles/code` and `/home/azureuser/R` for R related files

**Note:** You have to re-install Python Extension (https://marketplace.visualstudio.com/items?itemName=ms-python.python) to render an .ipynb Notebook in the VSCode Remote Session.

Have fun!

![](img/vscode_connect.gif)
