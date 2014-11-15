Problem: ```/Users/X/.mbox: No such file or directory (errno = 2)```
Solution: created ```~/.mbox``` because mutt complained 

Problem: ```/Users/david/.mbox: No such file or directory (errno = 2)```
Solution: send mail to self ```echo "text" | mail $USER``` which 
creates ```/var/spool/mail/USER```
didn't quite work :-/

Problem: [Error sending message, child exited 127 (Exec error.).][err-sending-mutt]
Solution: check path to sendmail variable... it must be valid

