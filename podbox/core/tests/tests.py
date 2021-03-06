import datetime

from django.shortcuts import resolve_url
from django.test import Client
from django.test import RequestFactory
from django.test import TestCase

from podbox.core.models import *


class HomeLoggedInUserTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get(resolve_url('home'))
        self.user = User.objects.create_user(
            username='liquuid',
            email='liquuid@…',
            password='top_secret')
        self.user.save()
        c = Client()
        c.login(username='liquuid', password='top_secret')
        self.response = c.get(resolve_url('home'), follow=True)

    def test_template(self):
        """Must use index.html"""
        self.assertTemplateUsed(self.response, 'index.html')

    def test_login(self):
        self.assertEqual(self.response.status_code, 200)


class HomeNonLoggedInUserTest(TestCase):
    def setUp(self):
        self.response = self.client.get(resolve_url('home'), follow=True)

    def test_home_for_non_logged_users(self):
        self.assertContains(self.response, 'Log in')


class EpisodeTest(TestCase):
    def setUp(self):
        self.title = "Episodio1"
        self.url = "http://"
        self.updated = datetime.datetime.now()
        self.summary = "yadayadayadayadayada"
        self.feeds = Feed()

    def tearDown(self):
        pass

    """
        def _parse_data(self, data):
            self.title = data['title']
            self.url = data["links"][1]["href"]
            self.updated = datetime.strptime(data['updated'][:25].strip(), "%a, %d %b %Y %H:%M:%S")
            self.summary = data['summary']

        def __str__(self):
            return "%s" % (self.title)
    """


class FeedTest(TestCase):
    def setUp(self):
        self.category = Category()
        self.category.name = 'teste'
        self.category.save()
        self.feed = Feed.objects.create(url="http://fuuu/", category=self.category)
        self.feed_title1 = "PapoTech - Podcast de Tecnologia"
        self.feed_link1 = "http://www.papotech.com.br/blog"
        self.feed_description1 = "PapoTech - Podcast sobre tecnologia, por JR Gandara e Vinicius Lobo"
        self.feed_pubdate1 = "Thu, 02 Jun 2011 02:30:51 +0000"
        self.feed_title2 = "RapaduraCast"
        self.feed_link2 = "http://www.rapaduracast.com.br"
        self.feed_description2 = u"O RapaduraCast \xe9 o podcast do portal Cinema Com Rapadura! De uma forma descontra\xedda, o RapaduraCast traz o conte\xfado do site que ser\xe1 discutido, al\xe9m de algumas novidades e quadros engra\xe7ad\xedssimos. Aqui, n\xe3o iremos medir as palavras ou fazer m\xe9dia, afinal, antes de tudo, somos meros cin\xe9filos mortais como voc\xeas leitores."
        self.feed_pubdate2 = "Wed, 31 Aug 2011 05:30:18 -0300"
        self.feed_pubdate_iso2 = "2011-08-31T05:30:18"
        self.feed_fake_xml1 = open("feeds/_teste1", "r", encoding='utf-8').read()
        self.feed_fake_xml2 = open("feeds/_teste2", "r", encoding='latin-1').read()

    def test_get_title(self):
        self.feed._raw_feed = self.feed_fake_xml1
        self.assertEquals(self.feed._get_title(), self.feed_title1)
        self.feed._raw_feed = self.feed_fake_xml2
        self.assertEquals(self.feed._get_title(), self.feed_title2)

    def test_get_link(self):
        self.feed._raw_feed = self.feed_fake_xml1
        self.assertEquals(self.feed._get_link(), self.feed_link1)
        self.feed._raw_feed = self.feed_fake_xml2
        self.assertEquals(self.feed._get_link(), self.feed_link2)

    def test_get_description(self):
        self.feed._raw_feed = self.feed_fake_xml1
        self.assertEquals(self.feed._get_description(), self.feed_description1)
        self.feed._raw_feed = self.feed_fake_xml2
        self.assertEquals(self.feed._get_description(), self.feed_description2)

    def test_get_pubdate(self):
        self.feed._raw_feed = self.feed_fake_xml1
        self.assertEquals(self.feed._get_pubdate(), self.feed_pubdate1)
        self.feed._raw_feed = self.feed_fake_xml2
        self.assertEquals(self.feed._get_pubdate(), self.feed_pubdate2)

    def test_save_title(self):
        title = self.feed_title1
        self.feed._get_title = lambda: title
        self.feed._save_title()
        feed_test = Feed.objects.latest('id')
        self.assertEquals(feed_test.title, self.feed_title1)

    def test_save_link(self):
        link = self.feed_link1
        self.feed._get_link = lambda: link
        self.feed._save_link()
        feed_test = Feed.objects.latest('id')
        self.assertEquals(feed_test.link, self.feed_link1)

    def test_save_description(self):
        description = self.feed_description1
        self.feed._get_description = lambda: description
        self.feed._save_description()
        feed_test = Feed.objects.latest('id')
        self.assertEquals(feed_test.description, self.feed_description1)

    def test_save_pubdate(self):
        self.feed._rfc2datetime = lambda: datetime(2011, 8, 31, 5, 30, 18)
        self.feed._save_pubdate()
        feed_test = Feed.objects.latest('id')
        self.assertEquals(feed_test.pubdate.isoformat(), self.feed_pubdate_iso2 + "+00:00")

    def test_url(self):
        self.assertEquals(self.feed.url, "http://fuuu/")

    def test_string_name(self):
        self.feed.title = None
        self.assertEquals(self.feed.__str__(), self.feed.url)
        self.feed.title = "Name"
        self.assertEquals(self.feed.__str__(), self.feed.title)

    def test_rfc2datetime(self):
        self.feed._get_pubdate = lambda: self.feed_pubdate2
        self.assertEquals(self.feed._rfc2datetime().isoformat(), self.feed_pubdate_iso2)
