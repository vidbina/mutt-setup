# Setup

 - Symlink ```.muttrc``` to the ```muttrc``` in this repository
 - Create a ```accounts``` directory within this project's root
 - Add a file for every mail account you need setup, below I have an example for the account settings necessary
 - Encrypt your password into a appropriately named .gpg file

## Account setup

```muttrc
color status brightyellow black
set from="foo@example.com"
set realname="Kwame Foo"

set my_foo_pass="`gpg --quiet --for-your-eyes-only -d ~/.mutt/accounts/foos_encrypted_password.gpg`"
set imap_user="foo@example.com"
set imap_pass=$my_foo_pass
set smtp_url="smtp://foo@example.com@smtp.gmail.com:587/"
set smtp_pass=$my_foo_pass

set folder="imaps://imap.gmail.com:993"
set spoolfile="~/.mutt/mail/foo/INBOX" # local dirs because I use offlineimap
set record="~/.mutt/mail/foo/Sent"
set postponed="+[Gmail]/Drafts"
```

# Troubleshooting
Problem: ```/Users/X/.mbox: No such file or directory (errno = 2)```
Solution: created ```~/.mbox``` because mutt complained 

Problem: ```/Users/david/.mbox: No such file or directory (errno = 2)```
Solution: send mail to self ```echo "text" | mail $USER``` which 
creates ```/var/spool/mail/USER```
didn't quite work :-/

Problem: [Error sending message, child exited 127 (Exec error.).][err-sending-mutt]
Solution: check path to sendmail variable... it must be valid

Problem: Login failed
If you are quite sure that the encrypted password is correct make sure to use
double quotes in mutt to encapsulate the password. I've noticed that encrypting
passwords like ```This is just a sentence.``` does not work well with mutt if
not entered within double quotes. If your password is to be stored as the 
variable ```my_foo_pass``` confirm that the contents are correct by running
```set ?my_foo_pass``` in mutt which should print the data that Mutt has 
registered as the password :wink:.
