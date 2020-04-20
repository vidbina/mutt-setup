# (Neo)Mutt Setup

[neomuttrc]: https://neomutt.org/man/neomuttrc

1. Symlink `~/.muttrc` to the [muttrc](./muttrc) in this repository
2. Symlink `~/.offlineimaprc` to [offlineimap](./offlineimap) in this
   repository
3. Create a "accounts" directory within this project's root
4. [Configure an account](#account-setup) within the previously created
   "accounts" directory for every mail account you need setup
5. Encrypt your password into a appropriately named gpg file

## Account setup

In our [muttrc](./muttrc), we source accounts/setup.muttrc which sets the
shared configuration parameters between all accounts (e.g.: settings such as
`realname` and `forward_format` are more or less global settings) and then
sources the account-specific configuration for every account.

```muttrc
# ~/.mutt/accounts/setup.muttrc
set realname="David Asabina"

set fcc_attach
unset mime_forward
set forward_format = "Fwd: %s"
set include
set forward_quote

# Load the configuration for a given account, e.g.: vidbina in this case
source "~/.mutt/accounts/ACCOUNT_A.muttrc"
folder-hook $folder '~/.mutt/accounts/ACCOUNT_A.muttrc'
```

For every separate account, we go ahead to define an associated configuration
within the accounts directory. The following snippet provides an indication of
what this configuration may look like. Note that one would need to provide the
correct key id to the `pgp_sign_as` setting.

```muttrc
# ~/.mutt/accounts/ACCOUNT_A.muttrc
color status brightyellow black
set from="foo@example.com"
set realname="Kwame Foo"

set use_from=yes
set use_envelope_from=yes

set folder="~/.mutt/mail/account-a"
set spoolfile="+INBOX"
set postponed="+[Gmail]/Drafts"

set folder="imaps://imap.gmail.com:993"
set spoolfile="~/.mutt/mail/foo/INBOX" # local dirs because I use offlineimap
set record="~/.mutt/mail/foo/Sent"
set postponed="+[Gmail]/Drafts"

set sort=threads
set editor=nvim

set header_cache="~/.mutt/hdrs"
set message_cachedir="~/.mutt/msgs"

# Copied from https://pbrisbin.com/posts/mutt_gmail_offlineimap/

## main options
#set realname   = "Real Name"
#set from       = "user@gmail.com"
#set mail_check = 0
#set envelope_from
#
#unset move           # gmail does that
#set delete           # don't ask, just do
#unset confirmappend  # don't ask, just do!
#set quit             # don't ask, just do!!
#unset mark_old       # read/new is good enough for me

# sort/threading
set sort     = threads
set sort_aux = reverse-last-date-received
set sort_re

# look and feel
set pager_index_lines = 8
set pager_context     = 5
set pager_stop
set menu_scroll
set smart_wrap
set tilde
unset markers

# composing
set fcc_attach
unset mime_forward
set forward_format = "Fwd: %s"
set include
set forward_quote

#set pgp_autosign=yes
set crypt_use_gpgme=yes
set postpone_encrypt = yes
set pgp_self_encrypt = yes
set crypt_use_pka = no
set crypt_autosign = no
set crypt_autoencrypt = no
set crypt_autopgp = yes
set pgp_sign_as=0xXXXXXXXXXXXXXXXX
```

# Troubleshooting

> :warning: DISCLAIMER: These problem/solution pairs stems from my OSX days
> which are likely very dated.

Problem: `/Users/X/.mbox: No such file or directory (errno = 2)`
Solution: created `~/.mbox` because mutt complained

Problem: `/Users/david/.mbox: No such file or directory (errno = 2)`
Solution: send mail to self `echo "text" | mail $USER` which creates
`/var/spool/mail/USER`
didn't quite work :-/

Problem: [Error sending message, child exited 127 (Exec error.).][err-sending-mutt]
Solution: check path to sendmail variable... it must be valid

Problem: Login failed
If you are quite sure that the encrypted password is correct make sure to use
double quotes in mutt to encapsulate the password. I've noticed that encrypting
passwords like `This is just a sentence.` does not work well with mutt if not
entered within double quotes. If your password is to be stored as the variable
`my_foo_pass` confirm that the contents are correct by running `set
?my_foo_pass` in mutt which should print the data that Mutt has registered as
the password :wink:.
