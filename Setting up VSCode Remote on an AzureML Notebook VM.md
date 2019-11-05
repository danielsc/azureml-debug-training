# Setting up VSCode Remote on an AzureML Notebook VM

## 0. Prerequisite (Windows only)
Install an OpenSSH compatible SSH client (https://code.visualstudio.com/docs/remote/troubleshooting#_installing-a-supported-ssh-client) if one is not already present.
Note: PuTTY is not supported on Windows since the ssh command must be in the path.

## 1. Save the Notebook VM access information

Note: this step needs to be updated since the Azure ML Portal UX has changed. Currently, you have to 
1. find the VM that is backing your Notebook VM in the resource group where your workspace is located
2. "Reset Password" for that VM 
3. enable "Boot Diagnostics" for that VM
4. log in through the "Serial Console" using the username and password you had used
5. execute `sudo vi /home/azureuser/.ssh/authorized_keys` and add your public ssh key from your local machine to the end of the file
6. From "Overview" remember the IP address of the VM


With the release of "Compute Instance" in late November 2019, this process will be simplified to a UI-based configuration in the Azure ML studio


## 2. Add the Notebook VM as a host
Open the file ~/.ssh/config (C:\Users\<username>\.ssh\config on Windows) on your local machine in an editor and add a new entry:

    Host mynotebookvm
        HostName <IP of the VM>
        User azureuser
   
Here some details on the fields:

- `Host`: use whatever shorthand you like for the VM
- `HostName`: This is the IP address of the VM pulled from the above configuration page
- `User`: this needs to be `azureuser`

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

## 3. Install VS Code and connect to the Notebook VM
Next install VS Code from here: https://code.visualstudio.com/ and then install the Remote SSH Extension from here: https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh.

Now, click on the Remote-SSH icon on the left to show your SSH configurations, then right-click on the SSH host configuration you just created, and select 'Connect to Host in current Window'.

From here on, you are entirely working on the Notebook VM and you can now edit, debug, use git, use extensions, etc. -- just like you can with your local VSCode.

Have fun!

![](img/vscode_connect.gif)
