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
    SEARCH_BY_SUBJECT =  '(SUBJECT "Stone699")'
    SEARCH_BY_SUBJECT_2 =  '(SUBJECT "Email Attachment")'
    SEARCH_BY_EMAIL =  '(FROM "IQalerts@questrade.com")'
    M1 = '"[Gmail]/Starred"'
    M2 = 'politics'

    CONN = EmailAcct(
        account_email=settings.TEST_EMAIL,
        app_password=settings.GMAIL_APP_PASSWORD)

    async def test_move_email(self):
        emails = self.CONN.move_email()

    # async def test_delete_emails(self):
        # emails = self.CONN.delete_emails(email_address=self.SEARCH_BY_EMAIL)

    # async def test_list_boxes(self):
        # box_bytes = self.CONN.list_inboxes
        # assert len(box_bytes) > 0
        # print(box_bytes)

    # async def test_email_count(self):
        # c = self.CONN.total_emails
        # print(c)

    # async def test_get_namespace(self):
    #     print(self.CONN.get_namespace)
    #     emails = e.get_recent()


    # async def test_email(self):
    #     emails = self.CONN.get_unique_sender_emails(
    #         neg_list=['<Fari.Hamzei@HamzeiAnalytics.com>'],
    #         which_mailbox=self.M1
    #         )
    #     print(emails)


    # async def test_search_email(self):
        # raw_email = self.CONN.search_emails(self.SEARCH_BY_EMAIL)
        # print(raw_email)




# from .conftest import *

# @pytest.mark.asyncio
# class Test_Mailbox_CRUD:

#     SEARCH_BY_FROM_AND_SUBJECT =  '(FROM "anjali sinha" SUBJECT "test")'
#     SEARCH_BY_SUBJECT =  '(SUBJECT "Stone699")'
#     SEARCH_BY_SUBJECT_2 =  '(SUBJECT "Email Attachment")'

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


























'''
{'"=?UTF-8?Q?Bell?=" <info@e.bell.ca>',
 '"Afrin Siddiqui" <afrin.s@quantinsti.com>',
 '"Al Bentley" <al.bentley@simplywallst.com>',
 '"Alex Melikhov" <a.melikhov@changelly.com>',
 '"Alex Slessor (via Google Drive)" <theeconomicspecialist@gmail.com>',
 '"Alex from BitClave" <alex.bessonov@bitclave.intercom-mail.com>',
 '"Alexander Slessor (via Google Sheets)" <alexjslessor@gmail.com>',
 '"Alexey from Play2Live" <info@play2live.io>',
 '"Alfa Distribution" <admin@normarh.qc.ca>',
 '"Alfa Distribution" <tracking@shipstation.com>',
 '"Amazon.ca" <auto-confirm@amazon.ca>',
 '"Amazon.ca" <shipment-tracking@amazon.ca>',
 '"Becker @ Market Hero" <ab@markethero.io>',
 '"Becker @ Market Hero" <alexbecker@markethero.io>',
 '"Becker @ Market Hero" <mail@markethero.io>',
 '"Becker @ Market Hero" <webinarinfo@webinarjam.net>',
 '"Becker @ Market" <mail@markethero.io>',
 '"Becker, Alex" <mail@markethero.io>',
 '"Bell" <noreply@bell.ca>',
 '"CANEX.ca" <help@canex.ca>',
 '"CTLS Support / Support SSCDL (HC/SC)" <hc.ctls-sscdl.sc@canada.ca>',
 '"Capital One" <capitalone@message.capitalone.com>',
 '"Capital One" <capitalone@notification.capitalone.com>',
 '"Christopher from Kaggle" <christopher.crawford@kaggle.intercom-mail.com>',
 '"CodePen" <verify@codepen.io>',
 '"Codementor Community" <community@codementor.io>',
 '"Codementor" <support@codementor.io>',
 '"Credit Score Increase @ Borrowell.com" <info@borrowell.com>',
 '"Credit Score Update @ Borrowell" <info@borrowell.com>',
 '"Credit Score Update @ Borrowell.com" <info@borrowell.com>',
 '"Crypto Tickets" <support@crypto.tickets>',
 '"Dan from Kaggle" <dan.becker@kaggle.intercom-mail.com>',
 '"Daphne from Codementor" <daphne@codementor.io>',
 '"Dawood (Meetup)" <Blockchain-Business-Startups-Meetup-announce@meetup.com>',
 '"Dolan, Michael" <michael.dolan@Wabtec.com>',
 '"Dragos Ionel (Meetup)" <meetup-group-aigeeks-announce@meetup.com>',
 '"Du, Judy" <Du.Judy@cfmws.com>',
 '"Egor from crypto.tickets" <egor@ticketscloud.org>',
 '"Eventbrite" <ebhelp@eventbrite.com>',
 '"Eventbrite" <orders@eventbrite.com>',
 '"Facebook" <security@facebookmail.com>',
 '"Fari Hamzei" <Fari.Hamzei@HamzeiAnalytics.com>',
 '"Fillip from CEX.IO" <p.lunhu@wnb.com.ua>',
 '"Glassdoor Jobs" <noreply@glassdoor.com>',
 '"Grant Mac (via Google Maps)" <noreply-location-sharing+1a45c883@google.com>',
 '"HA Admin" <Admin@HamzeiAnalytics.com>',
 '"Hamilton Machine Learning and Computing Research"\r\n'
 ' <noreply@eventbrite.com>',
 '"Hamzei Analytics (via Google Sheets)" <hamzeianalytics@gmail.com>',
 '"Hamzei Analytics Customer Support" <support@hamzeianalytics.com>',
 '"Hamzei Analytics Subscription Services" <Subscriptions@HamzeiAnalytics.com>',
 '"Harknett, Kerry" <Harknett.Kerry@cfmws.com>',
 '"Houston, James" <james.houston@Wabtec.com>',
 '"JVZoo" <support@jvzoo.com>',
 '"James P.Smith (Meetup)" '
 '<Toronto-Chapter-TDWI-The-Data-Warehousing-Institute-announce@meetup.com>',
 '"Kasthy from DataCamp" <support@datacamp.com>',
 '"Khan Academy" <no-reply@khanacademy.org>',
 '"Kickstarter" <no-reply@kickstarter.com>',
 '"Koodo" <koodobilling@mailing.koodomobile.com>',
 '"Koodo" <koodoservice@mail.koodomobile.com>',
 '"Leggat Chevrolet Cadillac Buick GMC Service"\r\n'
 ' <1170leggservice11@dealermineinc.com>',
 '"Leggat Chevrolet Cadillac Buick GMC" <noreply@wedrivesales.ca>',
 '"Mark Esposito" <Mark@HamzeiAnalytics.com>',
 '"Mark Esposito" <mark@hamzeianalytics.com>',
 '"Mark from Kaggle" <mark.mcdonald@kaggle.intercom-mail.com>',
 '"Martijn from DataCamp" <team@datacamp.com>',
 '"McDonough, Liz" <mcdonou@mcmaster.ca>',
 '"Mike from BitClave" <mike.t@bitclave.intercom-mail.com>',
 '"Millaire, Carole" <Millaire.Carole@cfmws.com>',
 '"NSLSC/CSNPE" <info@msfaa-emafe.cibletudes-canlearn.ca>',
 '"Neal, Malia" <Malia_Neal@reyrey.com>',
 '"Newegg.ca" <info@newegg.ca>',
 '"PC Financial" <info@e.pcfinancial.ca>',
 '"PC Optimum" <noreply@e.pcoptimum.ca>',
 '"Paul from Kaggle" <paul.mooney@kaggle.intercom-mail.com>',
 '"Phil from Kaggle" <phil.culliton@kaggle.intercom-mail.com>',
 '"QuadrigaCX" <no_reply@quadrigacx.com>',
 '"QuantInsti" <contact@quantinsti.com>',
 '"Quantra QuantInsti" <quantra@quantinsti.com>',
 '"Quantra" <quantra@quantinsti.com>',
 '"Scotiabank Prepaid VISA" <noreply@visaprepaidprocessing.com>',
 '"Shopify" <shopify@email.shopify.com>',
 '"SkyWatch" <noreply@eventbrite.com>',
 '"Slack" <feedback@slack.com>',
 '"Slack" <no-reply@email.slack-core.com>',
 '"Slack" <no-reply@slack.com>',
 '"Sohier from Kaggle" <sohier.dane@kaggle.intercom-mail.com>',
 '"Sunny Ray (Meetup)" <CanadaBitcoin-announce@meetup.com>',
 '"Sushant" <sushant.r@quantinsti.com>',
 '"Suzanne Mckenzie" <Suzanne@hamzeianalytics.com>',
 '"Team Alpha Vantage" <admin@alphavantage.co>',
 '"Tefera, Yidnek" <ntefera@Wabtec.com>',
 '"The DataCamp Team" <team@datacamp.com>',
 '"Toronto Public Library" <notifications@torontopubliclibrary.ca>',
 '"Uber" <uber-us@uber.com>',
 '"Udemy" <no-reply@e.udemymail.com>',
 '"Vasily from BitClave" <vasily.trofimchuk@bitclave.intercom-mail.com>',
 '"Walter from Kaggle" <walter.reade@kaggle.intercom-mail.com>',
 '"Weiting from Codementor" <jobs@codementor.io>',
 '"Wendy from Kaggle" <wendy.kan@kaggle.intercom-mail.com>',
 '"adidas Canada Online Store" <adidas@account.adidas.com>',
 '"adidas Canada Online Store" <adidas@adidas-news.adidas.com>',
 '"eBay Canada" <eBay@reply.ebay.ca>',
 '"info@newegg.ca" <info@newegg.ca>',
 '"ontariocolleges.ca | collegesdelontario.ca"\r\n'
 ' <noreply@ontariocolleges.ca>',
 '"service@intl.paypal.com" <service@intl.paypal.com>',
 '"support@cex.io" <support@cex.io>',
 '"xda-developers" <webmaster@xda-developers.com>',
 '-Alex Becker- <alexbecker@markethero.io>',
 '-Alex Becker- <mail@markethero.io>',
 '1170leggservice11@dealermineinc.com',
 '<Admin@HamzeiAnalytics.com>',
 '<Alexander.Slessor@forces.gc.ca>',
 '<CityofHamilton@hamilton.ca>',
 '<David.Hommersen@forces.gc.ca>',
 '<Fari.Hamzei@HamzeiAnalytics.com>',
 '<GARY.ARCHER@forces.gc.ca>',
 '<Izzat.Jaff@ttc.ca>',
 '<JEFFREY.CLARKE2@forces.gc.ca>',
 '<Joanne.BRUMWELL@forces.gc.ca>',
 '<Liviu.Antonescu@ttc.ca>',
 '<TYLER.HOMER@forces.gc.ca>',
 '<VALLERIE.GRIESE@forces.gc.ca>',
 '<creditplan@canex.ca>',
 '<noreply@bnc.ca>',
 '<npf_statement@cfmws.com>',
 '<osapwebmaster@ontario.ca>',
 '<ricoh_MFD_scan2_email@transport.bombardier.com>',
 '<stephen.green@ttc.ca>',
 '=?UTF-8?B?QW5kcsOpIFZvcmJhY2g=?= <notifications@github.com>',
 '=?UTF-8?B?VWRlbXk=?= <udemy@email.udemy.com>',
 '=?utf-8?Q?CEX.IO?= <support@cex.io>',
 '=?utf-8?Q?Customer=20Service=20Fj=C3=A4llr=C3=A4ven=20Canada?= '
 '<customerservice@fjallravencanada.com>',
 '=?utf-8?Q?Egor=20from=20crypto.tickets?= <info@crypto.tickets>',
 '=?utf-8?Q?Gemini=20Exchange?= <hello@gemini.com>',
 '=?utf-8?Q?Gemini?= <hello@gemini.com>',
 '=?utf-8?Q?GitHub?= <support@github.com>',
 '=?utf-8?Q?Kaggle=20Team?= <team@kaggle.com>',
 '=?utf-8?Q?Maeve=20=40=20Borrowell.com?= <info@borrowell.com>',
 '=?utf-8?Q?SkipTheDishes=20Team?= <couriers@skipthedishes.com>',
 '=?utf-8?Q?Stephen=20at=20Mi=20PC?= <hi@mipcworld.com>',
 '=?utf-8?Q?Stephen=20at=20Mini=20PC?= <hi@mipcworld.com>',
 '=?utf-8?q?ARToken?= <info@cappasity.com>',
 '=?utf-8?q?Cappasity_CAPP_Team?= <info@cappasity.com>',
 '=?utf-8?q?Cappasity_Team?= <info@cappasity.com>',
 '=?utf-8?q?Jenny_Herz?= <info@cappasity.com>',
 '?? Alex Becker ?? <mail@markethero.io>',
 'ALEXANDER SLESSOR <slessoa@mcmaster.ca>',
 'Adobe <message@adobe.com>',
 'Adobe Systems Incorporated <storemanager@adobe.com>',
 'Akash Kumar <akashk@cadretransit.com>',
 'Alex <alexjslessor@gmail.com>',
 'Alex Becker <alex@beckermailing.com>',
 'Alex Becker <alex@konker.io>',
 'Alex Becker <mail@markethero.io>',
 'Alex Becker <support@konker.io>',
 'Alex Slessor <theeconomicspecialist@gmail.com>',
 'Alexander Slessor <alexjslessor@gmail.com>',
 'Alexander Slessor <catch@payments.interac.ca>',
 'Alexander Slessor <ext.alexander.slessor@rail.bombardier.com>',
 'Alexander Slessor <notify@payments.interac.ca>',
 'Alstom Recruiting Team <system@successfactors.eu>',
 'Alver Emad <alveremad2000@gmail.com>',
 'Alver Koro <alver.koro@rail.bombardier.com>',
 'Amazon <account-update@amazon.com>',
 'Amrit Chahal <amrit@kanecapitalgroup.com>',
 'Anaconda Cloud <server@anaconda.org>',
 'Analytics Vidhya <kunal.jain@analyticsvidhya.com>',
 'AngelList <team@angel.co>',
 'AngelList Talent <talent@angel.co>',
 'Ayoub DARDORY <notifications@github.com>',
 'Ayush <ayushsingh244617@gmail.com>',
 'BRUCE NARBAITZ <catch@payments.interac.ca>',
 'Becker <mail@markethero.io>',
 'Becker Alex <mail@markethero.io>',
 'Bell <confirmation@bell.ca>',
 'Bell <ebill@bell.ca>',
 'Bell <noreply@bell.ca>',
 'Bitstamp <noreply@bitstamp.net>',
 'Borrowell Inc <info@borrowell.com>',
 'Brandon Hurst <brandon.hurst@rail.bombardier.com>',
 'CFMWS Member Care <help@canex.ca>',
 'Capital One <capitalone@experience.capitalone.com>',
 'Christopher Winchester <cwinchester@rogers.com>',
 'CoinGate Support <support@coingate.com>',
 'CoinGate Team <info@coingate.com>',
 'Coinbase <contact@coinbase.com>',
 'Coinbase <no-reply@coinbase.com>',
 'Coinbase <no-reply@updates.coinbase.com>',
 'Coinbase Support <support@coinbase.com>',
 'Coinigy Alerts <alerts@coinigy.com>',
 'Damiano Spina <notifications@github.com>',
 'Daniel Gross <team@pioneer.app>',
 'Databricks <billing@databricks.com>',
 'Databricks Team <no-reply@databricks.com>',
 'Dataquest <hello@dataquest.io>',
 'Dave Scharbach <Toronto-Machine-Learning-Meetup-announce@meetup.com>',
 'Dawood <Blockchain-Business-Startups-Meetup-announce@meetup.com>',
 'Discord <noreply@discordapp.com>',
 'Discord <notifications@discordapp.com>',
 'Dragos Ionel <meetup-group-aigeeks-announce@meetup.com>',
 'EMAA Pay Website <no-reply-EMAA-Pay-Website@forces.gc.ca>',
 'Elastic DevRel Team <meetup-group-dEvREeHj-announce@meetup.com>',
 'Ethan Wilding <Ethereum-Developers-announce@meetup.com>',
 'Fabian Fingerle <notifications@github.com>',
 'Fari Hamzei  <customercare@gotowebinar.com>',
 'Fari Hamzei via Dropbox <no-reply@dropbox.com>',
 'Fari via Dropbox <no-reply@dropbox.com>',
 'Fari via Dropbox <no-reply@dropboxmail.com>',
 'Filip Schouwenaars <filip.s@datacamp.com>',
 'GBA+ Team Status of Women Canada <cfc.acs-gba.swc@cfc-swc.gc.ca>',
 'GRANT MAC NEIL <catch@payments.interac.ca>',
 'Gary Archer <g-archer@live.ca>',
 'GitHub <noreply@github.com>',
 'Google <no-reply@accounts.google.com>',
 'Google <privacy-noreply@policies.google.com>',
 'Google AdWords <adwords-noreply@google.com>',
 'Google Ads <ads-noreply@google.com>',
 'Google Alerts <googlealerts-noreply@google.com>',
 'Google Cloud Platform <CloudPlatform-noreply@google.com>',
 'Google Download Your Data <noreply@google.com>',
 'Google Location Sharing <noreply-location-sharing@google.com>',
 'Google Maps Platform <google-maps-platform-noreply@google.com>',
 'Google News <googlenews-noreply@google.com>',
 'Google Payments <payments-noreply@google.com>',
 'Google Play <googleplay-noreply@google.com>',
 'Google Search Console Team <sc-noreply@google.com>',
 'Grace Barker <cognitiveclass-Toronto-announce@meetup.com>',
 'Graham Wilson <Grahamw@cadrestaff.com>',
 'Groupon <notify@r.groupon.com>',
 'Heroku <communications@heroku.com>',
 'Heroku <no-reply@heroku.com>',
 'Heroku <noreply@heroku.com>',
 'IQalerts@questrade.com',
 'Introduction to Mobile Application Development using Android '
 '<courses@edx.org>',
 'Jannis Redmann <notifications@github.com>',
 'Jeffrey Clarke <jeffreyjohnclarke@gmail.com>',
 'Joana Nunes <joana.N@hotmail.ca>',
 'Joana Nunes <joana.n@hotmail.ca>',
 'Johnny Vestergaard <notifications@github.com>',
 'Jonathan Greechan <Toronto-Startup-Founder-101-announce@meetup.com>',
 'Kickstarter <no-reply@kickstarter.com>',
 'Konker <no-reply@konker.io>',
 'LakeBTC <help@lakebtc.com>',
 'Liam McAuley <liam_mcauley@msn.com>',
 'Linda Duncliffe <Lindad@cadrestaff.com>',
 'Livecoin <sponsored@livecoin.net>',
 'Lutfi Dragusha <TARGETBMS@hotmail.com>',
 'MELANIE CHAI <catch@payments.interac.ca>',
 'Mail Delivery Subsystem <mailer-daemon@googlemail.com>',
 'Make It Happen <makeithappen@uwaterloo.ca>',
 'Marco Ochse <notifications@github.com>',
 'Martijn Theuwissen <martijn.theuwissen@datacamp.com>',
 'Mary Loubele <Intersections-KW-announce@meetup.com>',
 'Max Haroon <SIPmeetup-announce@meetup.com>',
 'Megan Risdal <surveys@google.com>',
 'Michelle Grant <michelle.grant@rail.bombardier.com>',
 'Microsoft account team\r\n'
 '\t<account-security-noreply@accountprotection.microsoft.com>',
 'Mode <noreply@modeanalytics.com>',
 'Muhammad Usman Khalid <muhammad_usman.khalid@rail.bombardier.com>',
 'NVIDIA <news@nvidia.com>',
 'NVIDIA Accelerated Computing Developer Newsletter <news@nvidia.com>',
 'NVIDIA Developer <noreply@nvidiadeveloper.com>',
 'Navjyot Khatra <navjyotk@cadretransit.com>',
 'Netflix <info@mailer.netflix.com>',
 'Nick Meiremans <notifications@github.com>',
 'Nicole Carter <contact@valleycentreforcounselling.com>',
 'PH-MN3 Agent 075 <roger.s@google.com>',
 'Peter Ewinger <peter.ewinger@gmail.com>',
 'Philip Alfaro <philip.alfaro@rail.bombardier.com>',
 'Pioneer <team@pioneer.app>',
 'Plotly Forum <plot@discoursemail.com>',
 'Plotly Forum summary <plot@discoursemail.com>',
 'Pluralsight <admin@pluralsight.com>',
 'Poloniex <do-not-reply@poloniex.com>',
 'Quantopian <no-reply@quantopian.com>',
 'Questrade client services <support@questrade.com>',
 'Questrade no-reply <no-reply@questrade.com>',
 'Quincy Larson <quincy@freecodecamp.org>',
 'Read the Docs <readthedocs@readthedocs.org>',
 'Richard Paddon <sportsguy_70@hotmail.com>',
 'Rinzin Norbu <rnorbu33@gmail.com>',
 'Rob Prouse <CoderCampHamilton-announce@meetup.com>',
 'Salvatore Delle Palme <meetup-group-aKsiZtZm-announce@meetup.com>',
 'Sanjeeb Das Gupta <sanjeeb@juliacomputing.com>',
 'Sayesha Bhardwaj1 <sayesha.bhardwaj1@rail.bombardier.com>',
 'Scotiabank <catch@payments.interac.ca>',
 'Scott McAuley <smcauley440@gmail.com>',
 'Skip Team <support@skipthedishes.com>',
 'Skype <noreply@alerts.skype.com>',
 'Soumyadeep Ganguly <soumyadeep.ganguly@rail.bombardier.com>',
 'Sphere <recruiting@sphere.ms>',
 'Sunny Ray <CanadaBitcoin-announce@meetup.com>',
 'Sunny Ray <meetup-group-BwdxeTwh-announce@meetup.com>',
 'Sunny Ray <meetup-group-gXdNmZMY-announce@meetup.com>',
 'Support <support@datacamp.com>',
 'TTC Employment Services <system@successfactors.com>',
 'Taiga.io <no-reply@taiga.io>',
 'Tangerine <donotreply@tangerine.ca>',
 'Team Coinbase <support+emiua2018@updates.coinbase.com>',
 'Tej Gandhi via LinkedIn <messaging-digest-noreply@linkedin.com>',
 'The DataCamp Team <support@datacamp.com>',
 'The DataCamp Team <team@datacamp.com>',
 'The Khan Academy team <hello@khanacademy.org>',
 'The Personal <noreply@thepersonal.com>',
 'The Personal Insurance Company <noreply@ThePersonal.com>',
 'TokenDesk Team <justinas@tokendesk.io>',
 'Troy Do <notifications@github.com>',
 'Tyler Homer <tylerghomer@gmail.com>',
 'Udemy Support <support@udemy.com>',
 'Valentin Barbat <valentin.barbat@rail.bombardier.com>',
 'Veken Bakrad <vbakrad@gmail.com>',
 'Vikas Ramrakha <SIPmeetup-announce@meetup.com>',
 'Wade Slaughter <wade.slaughter@rail.bombardier.com>',
 'Wade Slaughter <wades@cadretransit.com>',
 'Wade Slaughter <wadeslaughter22@gmail.com>',
 'WeCloudData <toronto-data-science-announce@meetup.com>',
 'Wendy from Kaggle <wendy.kan@kaggle.intercom-mail.com>',
 'Westdale 3D Printing <westdale3dprinting@gmail.com>',
 'WordPress <wordpress@thebayesian.com>',
 'account-noreply@adobe.com',
 'activation.no.reply.tm@koodo.com',
 'adsense-noreply@google.com',
 'alex slessor <slessoa@yahoo.ca>',
 'cPanel on nytrologistics.com <cpanel@nytrologistics.com>',
 'cody leonard <codyl2@hotmail.com>',
 'customerservice@koodomobile.com',
 'david hommersen <davidhommersen@hotmail.com>',
 'do-not-reply@rcmp-grc.gc.ca',
 'dwasss <notifications@github.com>',
 'edX <activate@edx.org>',
 'halekan <notifications@github.com>',
 'iamtodor <notifications@github.com>',
 'info@datacamp.com',
 'info@therocktrading.com',
 'inoue yoshitaka <notifications@github.com>',
 'internetsupport <internetsupport@bell.ca>',
 'jacob Nussbaum <jacob.nussbaum123@gmail.com>',
 'makeithappen@uwaterloo.ca',
 'mark esposito <dpmm55@gmail.com>',
 'noreply-analytics@google.com',
 'noreply@koodomobile.com',
 'quantra@quantinsti.com',
 'support@exodus.io',
 'teacher IT <teacherit1992@gmail.com>',
 'tsepayroll@staffedge.com'}
'''