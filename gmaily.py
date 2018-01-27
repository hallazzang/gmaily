import email
import email.header
import email.utils
import email.parser
import email.policy
import email.iterators
import imaplib

class Gmaily:
    @property
    def client(self):
        if not hasattr(self, '_client'):
            self._client = imaplib.IMAP4_SSL('imap.gmail.com')
        return self._client

    def login(self, user_email, user_pw):
        try:
            r = self.client.login(user_email, user_pw)
        except imaplib.IMAP4.error:
            return False
        return True

    def inbox(self):
        return SearchQuery('INBOX', self.client)

    def logout(self):
        self._client.logout()

class SearchQuery:
    def __init__(self, mailbox, client):
        self._mailbox = mailbox
        self._client = client
        self._criterias = ['ALL']

    def all(self):
        # Terminal method of method chaining
        self._client.select(self._mailbox, readonly=True)
        status, data = self._client.uid('SEARCH', *self._criterias)
        if status != 'OK':
            raise RuntimeError()

        return [Message(int(uid), self._client) for uid in data[0].split()]

    def before(self, date):
        if not hasattr(date, 'strftime'):
            raise TypeError()
        self._criterias.extend(['BEFORE', date.strftime('%d-%b-%Y')])
        return self

    def body(self, string):
        self._criterias.extend(['BODY', string])
        return self

    def from_(self, sender):
        self._criterias.extend(['FROM', sender])
        return self

    def by(self, sender):
        # Shortcut for from_
        return self.from_(sender)

    def header(self, field, value):
        self._criterias.extend(['HEADER', field, value])
        return self

    def since(self, date):
        if not hasattr(date, 'strftime'):
            raise TypeError()
        self._criterias.extend(['SENTSINCE', date.strftime('%d-%b-%Y')])
        return self

    def after(self, date):
        # Shortcut for since
        return self.since(date)

    def subject(self, subject):
        self._criterias.extend(['SUBJECT', subject])
        return self

    def text(self, text):
        self._criterias.extend(['TEXT', text])
        return self

    def __repr__(self):
        return '<SearchQuery %r>' % self._criterias

class Message:
    def __init__(self, uid, client):
        self._uid = uid
        self._client = client

    @property
    def uid(self):
        return self._uid

    @property
    def _body(self):
        if not hasattr(self, '_raw_body'):
            status, data = self._client.uid('FETCH', str(self.uid),
                '(BODY.PEEK[])')
            if status != 'OK':
                raise RuntimeError()

            parser = email.parser.BytesParser(policy=email.policy.default)
            self._raw_body = parser.parsebytes(data[0][1])

        return self._raw_body

    @property
    def text(self):
        if not hasattr(self, '_text'):
            self._text = ''.join(
                x.get_payload(decode=True).decode(x.get_content_charset())
                for x in email.iterators.typed_subpart_iterator(self._body,
                    'text')
            )

        return self._text

    @property
    def attachments(self):
        if not hasattr(self, '_attachments'):
            self._attachments = [
                Attachment(x)
                for x in email.iterators.typed_subpart_iterator(self._body,
                    'application')
            ]

        return self._attachments

    @property
    def subject(self):
        return self._body['subject']

    @property
    def sender(self):
        return self._body['from']

    @property
    def date(self):
        return email.utils.parsedate_to_datetime(self._body['date'])

    def __repr__(self):
        return '<Message %d>' % self.uid

class Attachment:
    def __init__(self, msg):
        self._msg = msg

    @property
    def name(self):
        return self._msg.get_filename()

    @property
    def payload(self):
        return self._msg.get_payload(decode=True)

    def __repr__(self):
        return '<Attachment %s>' % self.name
