# -*- coding: utf-8 -*-
import datetime
from django.test import TestCase
from player.models import *


class FeedTest(TestCase):
    def setUp(self):
        self.feed = Feed.objects.create(url="http://fuuu/")
        self.feed_title1 = "PapoTech - Podcast de Tecnologia"
        self.feed_link1 = "http://www.papotech.com.br/blog"
        self.feed_description1 = "PapoTech - Podcast sobre tecnologia, por JR Gandara e Vinicius Lobo"
        self.feed_pubdate1 = "Thu, 02 Jun 2011 02:30:51 +0000"
        self.feed_title2 = "RapaduraCast"
        self.feed_link2 = "http://www.rapaduracast.com.br"
        self.feed_description2 = u"O RapaduraCast \xe9 o podcast do portal Cinema Com Rapadura! De uma forma descontra\xedda, o RapaduraCast traz o conte\xfado do site que ser\xe1 discutido, al\xe9m de algumas novidades e quadros engra\xe7ad\xedssimos. Aqui, n\xe3o iremos medir as palavras ou fazer m\xe9dia, afinal, antes de tudo, somos meros cin\xe9filos mortais como voc\xeas leitores."
        self.feed_pubdate2 = "Wed, 31 Aug 2011 05:30:18 -0300"
        self.feed_pubdate_iso2 = "2011-08-31T05:30:18"
        self.feed_fake_xml1 = open("feeds/_teste1","r").read()
        self.feed_fake_xml2 = open("feeds/_teste2","r").read()

    def tearDown(self):
        pass

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
        #import pdb; pdb.set_trace()
        description = self.feed_description1
        self.feed._get_description = lambda: description
        self.feed._save_description()
        feed_test = Feed.objects.latest('id')
        self.assertEquals(feed_test.description, self.feed_description1)

    def test_save_pubdate(self):
        #pubdate = self.feed_pubdate2
        self.feed._rfc2datetime = datetime(2011, 8, 31, 5, 30,18)
        self.feed._save_pubdate()
        feed_test = Feed.objects.latest('id')
        self.assertEquals(feed_test.pubdate.isoformat(), self.feed_pubdate_iso2)

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