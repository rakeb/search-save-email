"""

__author__ = "Md Mazharul Islam Rakeb"
__email__ = "mislam7@uncc.edu"
__date__ = 10/21/20

"""

import argparse
import getpass
import imaplib


def open_connection(username, password):
    hostname = 'imap.gmail.com'
    port = 993
    connection = imaplib.IMAP4_SSL(hostname, port)

    connection.login(username, password)
    return connection


def search(key, value, con):
    result, data = con.search(None, key, '"{}"'.format(value))
    return data


def start_updated():
    des = '''
        Save searched emails as .eml files into local folder.\n\n 
        This is only tested for Gmail and has the following prerequisites:\n\n 
        1. Allow IMAP Access in your Gmail setting: https://mail.google.com/mail/u/0/#settings/fwdandpop\n\n 
        2. Allow Less secure app access by turning on Allow less secure apps: ON : https://myaccount.google.com/u/4/lesssecureapps\n\n 
    '''

    argparser = argparse.ArgumentParser(description=des)

    argparser.add_argument('-u', dest='username', help="Your email address", required=True)
    argparser.add_argument('-r', dest='remote_folder', help="Folder where to search for emails, such as INBOX",
                           default='INBOX')
    argparser.add_argument('-l', dest='local_folder',
                           help="Local folder where to save search results in .eml format. Default: Current directory",
                           default='.')
    argparser.add_argument('-e', dest='searched_email', help="The email address you want to search", required=True)
    argparser.add_argument('-c', dest='criteria', help="Search criteria, e.g. FROM, TO etc. Default: FROM",
                           default='FROM')
    argparser.add_argument('-s', dest='host', help="[Optional] IMAP host, like imap.gmail.com",
                           default='imap.gmail.com')
    argparser.add_argument('-p', dest='port', help="[Optional] IMAP port, like: 993", default=993)
    args = argparser.parse_args()

    gmail = imaplib.IMAP4_SSL(args.host, args.port)
    gmail.login(args.username, getpass.getpass())
    gmail.select(args.remote_folder)
    data = search(args.criteria, args.searched_email, gmail)
    for num in data[0].split():
        typ, data = gmail.fetch(num, '(RFC822)')
        f = open('%s/%s.eml' % (args.local_folder, str(num, 'utf-8')), 'w')
        print(str(data[0][1], 'utf-8'), file=f)
    gmail.close()
    gmail.logout()


if __name__ == '__main__':
    start_updated()
