# SSH-Login-Notice



A very simple method of recieving a message upon SSH login.

## Example

```
SSH login attempt successful at USERNAME:HOSTNAME -  1-15-22 23:00. If you do not recognize this login, please take action ASAP.
```


## Tutorial

First, a telegram bot must be made by messaging the "BotFather" on telegram and going through the interactive setup. Here you will recieve your API token.


Second, to find your ChatID, simply message the "UserInfoBot" to get your user account's chat ID.


Finally, input these values into the script and copy both the RC file and the ssh-notice.py script into the user's ~/.ssh folder. If this folder does not exist, run the `ssh-keygen` command to generate public and private keys for the user account and create the ~/.ssh folder. 


Now every time a user authenticates to the host, a Telegram message is recieved indicating who logged-in and where. 



