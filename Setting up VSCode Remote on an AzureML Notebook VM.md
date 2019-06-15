# Setting up VSCode Remote on an AzureML Notebook VM


In the AzureML Workspace in the Azure Portal, go to configuration page of the compute target associated with your Notebook VM and find the IP Adress, ssh port, and ssh private key at the bottom: 
![](img/vm_ssh_config.png)

Save private key to the ~/.ssh/ directory on your local computer; for instance open and editor for a new file and paste the key in:

    vi ~/.ssh/id_danielsctest_rsa
    
The private key will look somewhat like this
    
    -----BEGIN RSA PRIVATE KEY-----
    MIIEpAIBAAKCAQEAr99EPm0P4CaTPT2KtBt+kpN3rmsNNE5dS0vmGWxIXq4vAWXD
    Pbu/nc7KR7+8QVDl00tKo9B1m7b6Kwg3G3lar5oLSOmUTq/S23b5cGjLNak4+mrb
    .....

Change permissions on file to make sure only you can read the file (not sure if this is needed on Windows)

    chmod 600 ~/.ssh/id_danielsctest_rsa
    

Open the file ~/.ssh/config in an editor and add a new entry:

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

Next install VS Code Insiders from here: https://code.visualstudio.com/insiders/ and then click on the Remote-SSH icon on the left to show your SSH configurations, then right-click on the SSH host configuration you just created, and select 'Connect to Host in current Window'.

From here on, you are entirely working on the Notebook VM and you can now edit, debug, use git, use extensions, etc. -- just like you can with your local VSCode.

![](img/vscode_connect.gif)