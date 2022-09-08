from ..base_email import *
from imaplib import IMAP4_SSL
import email
from datetime import datetime
from typing import List, Tuple
from contextlib import contextmanager
import os
from datetime import datetime

'''Instructions:
1. create app password
https://support.google.com/accounts/answer/185833
'''

@contextmanager
def IMAP4_conn_manager(
    host: str = None,
    account_email: str = None, 
    app_password: str = None
    ):
    try:
        _conn = IMAP4_SSL(host)
        _conn.login(account_email, app_password)
        # _conn.select()# default is INBOX'
        yield _conn
    finally:
        _conn.close()


class EmailAcct:

    def __init__(
        self, 
        account_email: str = None,
        app_password: str = None, 
        default_mailbox: str = 'INBOX',
        host: str = 'imap.gmail.com'):

        with IMAP4_conn_manager(
            host=host,
            account_email=account_email, 
            app_password=app_password) as conn:
            conn.select()
            self.conn = conn
            self.mail = self.conn


    @classmethod
    def from_gmail(cls, app_password, default_mailbox):
        return cls('imap.gmail.com', app_password, default_mailbox)

    @property
    def list_inboxes(self) -> Tuple[str, List[bytes]]:
        return self.conn.list()

    @property
    def conn_logout(self):
        try:
            self.conn.logout()
        except IMAP4_SSL.error as err:
            raise Exception(f'Logout Error: {err}')

    @property
    def parse_inbox_names(self):
        inbox_name = []
        for item in self.list_inboxes[1]:
            text = item.decode('utf8')
            inbox_name.append(text)
        return inbox_name

    @property
    def get_namespace(self):
        return self.conn.namespace()

    def list_mail(self):
        self.mail.list()
        # list of "folders" aka labels in gmail.
        # self.mail.select("[Gmail]/Trash") # connect to inbox.
        self.mail.select("inbox") # connect to inbox.
        # result: 'OK'
        # data: [b'1, 2, 3, ..., 1282'] index of all emails in all folders
        result, data = self.mail.search(None, "ALL")
        ids = data[0] # data is a list.
        id_list = ids.split() # ids is a space separated string
        # fetch the email body (RFC822) for the given ID
        for i in id_list:
            # print(i)
            result, data = self.mail.fetch(i, "(RFC822)")
            email_message = email.message_from_bytes(data[0][1])
            print(email_message['From'], email_message['Subject'], email_message['Date'])
            # print(email_message['From'], email_message['Subject'], email_message['Date'], email_message['To'], email_message['Cc'], email_message['Bcc'], email_message['Message-ID'], email_message['In-Reply-To'], email_message['References'], email_message['X-GM-THRID'], email_message['X-Gmail-Labels'], email_message['X-GM-MSGID'], email_message['X-GM-LABELS'])

        # result, data = self.mail.fetch(latest_email_id, "(RFC822)") 
        # raw_email = data[0][1].decode("utf-8")
        # email_message = email.message_from_string(raw_email)
        # return email_message.as_string()
        # return email_message.get_payload()
        # return email_message.get_all('Subject', [])

        # for item in email_message.walk():
            # i = item.values()
            # i = item.items()
            # print(i)
            # print(item.get_params())
            # filename = item.get_filename()


    def get_recent(self):
        # Prompt server for an update. 
        # Returned data is None if no new messages, 
        # else value of RECENT response.
        new_emails = self.conn.recent()
        return new_emails

    def create_new_mailbox(self, new_mailbox_name):
        '''
        Create new mailbox by name.
        If mailbox exists will fail.

        on failure: ('NO', [b'[ALREADYEXISTS] Duplicate folder name text_mailbox (Failure)'])
        '''
        m = self.conn.create(new_mailbox_name)
        return m

    def _search_params(self, params):
        try:
            typ, msgnums = self.conn.search(None, params)
            if typ == 'OK':
                return msgnums[0]
            raise Exception('Search Error')
        except Exception as err:
            return err

    def get_raw_email(self, ids):
        id_list = ids.split()# ids is a space separated string
        latest_email_id = id_list[-1] # get the latest
        # fetch the email body (RFC822)
        result, data = self.conn.fetch(latest_email_id, "(RFC822)")
        raw_email = data[0][1].decode("utf-8")
        return raw_email

    def search_emails(self, search_term: str):
        self.conn.select()
        email_ids = self._search_params(search_term)
        # logger.info(f'search ids: {email_ids}')
        raw_email = self.get_raw_email(email_ids)
        return raw_email


    def save_as_local(self, filename, payload):
        save_path = os.path.join(f'{os.getcwd()}', f'{datetime.now()}_{filename}')
        fp = open(save_path, 'wb')
        fp.write(payload.get_payload(decode=True))
        fp.close()
        # logger.info(f'filename: {filename}')
        return 'Success'

    def return_attachment_bytes(self, raw_email):
        email_message = email.message_from_string(raw_email)
        for item in email_message.walk():
            filename = item.get_filename()
            # logger.info(f'filename: {filename}')
            if filename:
                file_bytes = item.get_payload(decode=True)
                return file_bytes

    def save_attachment_local(self, raw_email):
        email_message = email.message_from_string(raw_email)
        for item in email_message.walk():
            filename = item.get_filename()
            # logger.info(f'filename: {filename}')
            if filename:
                self.save_as_local(filename, item)


    def get_all_attachments(self, raw_email, as_bytes=True):
        email_message = email.message_from_string(raw_email)
        try:
            for item in email_message.walk():
                filename = item.get_filename()
                # logger.info(f'filename: {filename}')
                if filename:
                    if as_bytes:
                        file_bytes = item.get_payload(decode=True)
                        return file_bytes
                    else:
                        return self.save_as_local(filename, item)
        except Exception as err:
            # logger.info(f'err: {err}')
            return err


class Gmail:

    def __init__(self):
        self.mail = IMAP4_SSL('imap.gmail.com')
        self.mail.login('email@gmail.com', GMAIL_APP_PASSWORD)
        self.save_dir = '/path/to/dir'

    def save_as_local(self, filename, payload):
        att_path = os.path.join(self.save_dir, f'{datetime.now()}_{filename}')
        fp = open(att_path, 'wb')
        fp.write(payload.get_payload(decode=True))
        fp.close()
        print('Downloaded file:', filename)

    def save_as_bytes(self, email_message):
        for item in email_message.walk():
            filename = item.get_filename()
            # logger.info(f'filename: {filename}')
            if filename:
                file_bytes = item.get_payload(decode=True)
                return file_bytes


    def save_attachment(self, email_message):
        for item in email_message.walk():
            filename = item.get_filename()
            # logger.info(f'filename: {filename}')
            if filename:
                self.save_as_local(filename, item)


    def search_mail(self):
        self.mail.list()
        # logger.info(f'list: {self.mail.list()}')
        
        # list of "folders" aka labels in gmail.
        # self.mail.select("[Gmail]/Trash") # connect to inbox.
        self.mail.select("inbox") # connect to inbox.
        
        # result: 'OK'
        # data: [b'1, 2, 3, ..., 1282'] index of all emails in all folders
        # result, data = self.mail.search(None, "ALL")
        # logger.info(data)


    def list_mail(self):
        self.mail.list()
        # logger.info(f'list: {self.mail.list()}')
        
        # list of "folders" aka labels in gmail.
        # self.mail.select("[Gmail]/Trash") # connect to inbox.
        self.mail.select("inbox") # connect to inbox.
        
        # result: 'OK'
        # data: [b'1, 2, 3, ..., 1282'] index of all emails in all folders
        result, data = self.mail.search(None, "ALL")

        ids = data[0] # data is a list.
        # logger.info(f'ids: {data}')

        id_list = ids.split() # ids is a space separated string
        # logger.info(f'id_list: {id_list}')
        
        latest_email_id = id_list[-1] # get the latest
        # logger.info(f'latest_email_id: {latest_email_id}')

        # fetch the email body (RFC822) for the given ID
        result, data = self.mail.fetch(latest_email_id, "(RFC822)") 
        # logger.info(f'data:      {data}')

        raw_email = data[0][1].decode("utf-8")

        email_message = email.message_from_string(raw_email)
        # logger.info(f'email_message: \n\n{email_message}')

        # logger.info(f'email payload: {email_message.keys()}')
        # self.save_attachment(email_message)
        # bts = self.save_as_bytes(email_message)
        # return bts
        return email_message

    def get_attachment_as_bytes(self, email_message):
        # logger.info(f'email payload: {email_message.keys()}')
        bts = self.save_as_bytes(email_message)
        return bts



# def gmail_1():
#     mail = imaplib.IMAP4_SSL('imap.gmail.com')
#     mail.login('email@gmail.com', GMAIL_APP_PASSWORD)
#     mail.list()
#     # Out: list of "folders" aka labels in gmail.
#     mail.select("inbox") # connect to inbox.
#     result, data = mail.search(None, "ALL")
#     ids = data[0] # data is a list.
#     id_list = ids.split() # ids is a space separated string
#     latest_email_id = id_list[-1] # get the latest
#     # fetch the email body (RFC822) for the given ID
#     result, data = mail.fetch(latest_email_id, "(RFC822)") 
#     raw_email = data[0][1] # here's the body, which is raw text of the whole email
#     # including headers and alternate payloads
#     return raw_email

