from subprocess import Popen, PIPE
from os import path

def get_email_password(account):
  if ("%s" % account).isalpha():
    f = path.expanduser("~/.mutt/%s.gpg" % (account))
    s = "gpg --quiet --no-tty --for-your-eyes-only -d %s" % (f)
  
    p = Popen(s.split(' '), stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    return output

  else:
    return None
