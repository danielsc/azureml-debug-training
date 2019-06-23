# Setting up VSCode Remote on an AzureML Notebook VM

## 0. Prerequisite (Windows only)
Install an OpenSSH compatible SSH client (https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client) if one is not already present.
Note: PuTTY is not supported on Windows since the ssh command must be in the path.

## 1. Save the Notebook VM access information
In the AzureML Workspace in the Azure Portal, go to configuration page of the compute target associated with your Notebook VM and find the IP Adress, ssh port, and ssh private key at the bottom: 
![](img/vm_ssh_config.png)

Save private key to the ~/.ssh/ directory on your local computer; for instance open an editor for a new file and paste the key in:

    vi ~/.ssh/id_danielsctest_rsa 
    
    C:\Users\<username>\.ssh\id_danielsctest_rsa (Windows)

The private key will look somewhat like this
    
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAr99EPm0P4CaTPT2KtBt+kpN3rmsNNE5dS0vmGWxIXq4vAWXD
    .....
    ewMtLnDgXWYJo0IyQ91ynOdxbFoVOuuGNdDoBykUZPQfeHDONy2Raw==
    -----END RSA PRIVATE KEY-----

Change permissions on file to make sure only you can read the file (not sure if this is needed on Windows)

    chmod 600 ~/.ssh/id_danielsctest_rsa  

## 2. Add the Notebook VM as a host
Open the file ~/.ssh/config (C:\Users\<username>\.ssh\config on Windows) in an editor and add a new entry:

    Host danielsctest2
        HostName 13.69.56.51
        Port 22
        User azureuser
        IdentityFile ~/.ssh/id_danielsctest_rsa  
   
Here some details on the fields:

- `Host`: use whatever shorthand you like for the VM
- `HostName`: This is the IP address of the VM pulled from the above configuration page
- `Port`: This is the port shown on the above configuration page.
- `User`: this needs to be `azureuser`
- `IdentityFile`: should point to the file where you saved the privat key

Now you should be able to ssh to your Notebook VM using the shorthand you used above.

```
    MININT-LI90F99:git danielsc$ ssh danielsctest2
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

## 3. Install VS Code and connect to the Notebook VM
Next install VS Code from here: https://code.visualstudio.com/ (Insiders is no longer required) and then install the Remote SSH Extension from here: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh.

Now, click on the Remote-SSH icon on the left to show your SSH configurations, then right-click on the SSH host configuration you just created, and select 'Connect to Host in current Window'.

From here on, you are entirely working on the Notebook VM and you can now edit, debug, use git, use extensions, etc. -- just like you can with your local VSCode.

Have fun!

![](img/vscode_connect.gif)
