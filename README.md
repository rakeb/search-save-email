Copy searched emails to .eml files. This is only tested for Gmail and has the
following prerequisites: 
1. Allow IMAP Access in your Gmail setting: https://mail.google.com/mail/u/0/#settings/fwdandpop 
2. Allow Less secure app access by turning on Allow less secure apps: ON :
https://myaccount.google.com/u/4/lesssecureapps

optional arguments:
  -h, --help         show this help message and exit
  
  -u USERNAME        Your email address
  
  -r REMOTE_FOLDER   Folder where to search for emails, such as INBOX
  
  -l LOCAL_FOLDER    Local folder where to save search results in .eml format.
                     Default: Current directory
                     
  -e SEARCHED_EMAIL  The email address you want to search
  
  -c CRITERIA        Search criteria, e.g. FROM, TO etc. Default: FROM
  
  -s HOST            [Optional] IMAP host, like imap.gmail.com
  
  -p PORT            [Optional] IMAP port, like: 993