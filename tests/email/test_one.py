from osint_tools.api.email.gmail.deps import EmailAcct
from ..conftest import *

@pytest.mark.asyncio
class Test_Dependancies:
    '''
    ('OK',
     [b'(\\HasNoChildren) "/" "Deleted Messages"',
      b'(\\HasNoChildren) "/" "INBOX"',
      b'(\\HasChildren \\Noselect) "/" "[Gmail]"',
      b'(\\All \\HasNoChildren) "/" "[Gmail]/All Mail"',
      b'(\\Drafts \\HasNoChildren) "/" "[Gmail]/Drafts"',
      b'(\\HasNoChildren \\Important) "/" "[Gmail]/Important"',
      b'(\\HasNoChildren \\Sent) "/" "[Gmail]/Sent Mail"',
      b'(\\HasNoChildren \\Junk) "/" "[Gmail]/Spam"',
      b'(\\Flagged \\HasNoChildren) "/" "[Gmail]/Starred"',
      b'(\\HasNoChildren \\Trash) "/" "[Gmail]/Trash"',
      b'(\\HasNoChildren) "/" "politics"']
    )
    '''
    SEARCH_BY_FROM_AND_SUBJECT =  '(FROM "anjali sinha" SUBJECT "test")'
    SEARCH_BY_SUBJECT_2 =  '(SUBJECT "Email Attachment")'
    FROM_YOUTUBE = '(FROM "no-reply@youtube.com")'
    s1 = 'no-reply@youtube.com'
    s2 = 'notification@service.tiktok.com'
    M1 = '"[Gmail]/Starred"'
    M2 = 'politics'
    CONN = EmailAcct(
        account_email=settings.TEST_EMAIL,
        app_password=settings.GMAIL_APP_PASSWORD)

    async def test_list_boxes(self):
        box_bytes = self.CONN.list_inboxes
        print(box_bytes)
        assert len(box_bytes) > 0

    async def test_get_namespace(self):
        print(self.CONN.get_namespace)
        # emails = e.get_recent()

    async def test_email_count(self):
        count = self.CONN.total_emails
        print(count)
        assert count > 100

    # async def test_move_by_addr(self):
        # raw_email = self.CONN.move_by_email_addr(self.s2, 'tiktok_label')
        # print(raw_email)

    # async def test_search_email(self):
    #     raw_email = self.CONN.search_emails(self.s1)
    #     print(raw_email)


    # async def test_delete_emails(self):
        # emails = self.CONN.delete_emails(email_address=self.s1)
        
    # async def test_unique_sender_emails(self):
        # uniq_email_set = self.CONN.get_unique_sender_emails()
        # print(uniq_email_set)


    # async def test_move_email(self):
        # emails = self.CONN.move_email()

    # async def test_email(self):
    #     emails = self.CONN.get_unique_sender_emails(
    #         neg_list=[''],
    #         which_mailbox=self.M1
    #         )
    #     print(emails)









# @pytest.mark.asyncio
# class Test_Mailbox_CRUD:

#     async def test_get_attachment_bytes(self):
#         g = EmailAcct()
#         raw_email = g.search_emails(self.SEARCH_BY_SUBJECT_2)
#         # print(raw_email)
#         _save = g.return_attachment_bytes(raw_email)
#         assert isinstance(_save, bytes)
#         g.conn_logout

#     async def test_download_attachment(self):
#         g = EmailAcct()
#         raw_email = g.search_emails(self.SEARCH_BY_SUBJECT_2)
#         _save = g.save_attachment_local(raw_email)
#         g.conn_logout


#     async def test_create_mailbox(self):
#         g = EmailAcct()
#         a = g.create_new_mailbox('text_mailbox')
#         g.conn_logout


#     async def test_search_mail(self):
#         g = EmailAcct()
#         a = g.list_inboxes
#         print(a)
#         print(type(a))

#         for item in a[1]:
#             print(item.decode('utf8'))

#         print(g.get_namespace)
#         print(g.get_recent())
#         print(g.parse_inbox_names)


