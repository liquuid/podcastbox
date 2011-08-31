"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase
from player.models import *

class FeedTest(TestCase):
    def setUp(self):
        self.feed = Feed.objects.create(url="http://fuuu/")
        self.feed_title = "Los mano"
        self.feed_link = "http://fuuu/"
        self.feed_description = "#### mi mi mi ####"
        self.feed_pubdate = "Thu, 02 Jun 2011 02:30:51 +0000"
        self.feed_fake_xml = """
        <?xml version="1.0" encoding="UTF-8"?>
        <!-- generator="wordpress/2.2" -->
        <rss version="2.0"
                xmlns:content="http://purl.org/rss/1.0/modules/content/"
                xmlns:wfw="http://wellformedweb.org/CommentAPI/"
                xmlns:dc="http://purl.org/dc/elements/1.1/"
                >
        
        <channel>
                <title>%s<title>
                <link>%s</link>
                <description>%s</description>
                <pubDate>%s</pubDate>
                <generator>http://wordpress.org/?v=2.2</generator>
                <language>en</language>
                                <item>
                        <title>Episodio #1</title>
                        <link>http://fuuu/1</link>
                        <comments>http://fuuu/1#comments</comments>
                        <pubDate>Thu, 02 Jun 2011 02:22:38 +0000</pubDate>
                        <dc:creator>liquuid</dc:creator>
                        
                        <category><![CDATA[Podcasts]]></category>
        
                        <category><![CDATA[Teste]]></category>
        
                        <guid isPermaLink="false">http://fuuu/</guid>
                        <description><![CDATA[mimimimimi mimimi  ]]></description>
                                <content:encoded><![CDATA[mememememememe emmememem ]]></content:encoded>
        <enclosure url="http://fuuuu/123.mp3" length="39295336" type="audio/mpeg" />
               </item>
               <item>
                        <title>Episodio #2</title>
                        <link>http://fuuu/1</link>
                        <comments>http://fuuu/2#comments</comments>
                        <pubDate>Thu, 02 Jun 2011 03:22:38 +0000</pubDate>
                        <dc:creator>liquuid</dc:creator>
                        
                        <category><![CDATA[Podcasts]]></category>
        
                        <category><![CDATA[Teste]]></category>
        
                        <guid isPermaLink="false">http://fuuu/</guid>
                        <description><![CDATA[mimimimimi mimimi  ]]></description>
                                <content:encoded><![CDATA[mememememememe emmememem ]]></content:encoded>
                        <enclosure url="http://fuuuu/123.mp3" length="39295336" type="audio/mpeg" />
              </item>
 </channel>
        </rss>
        """ % (self.feed_title, self.feed_link, self.feed_description, self.feed_pubdate )

    def tearDown(self):
        pass

    def test_get_title(self):
        self.assertEquals(self.get_title(), self.feed_title)

    def test_get_link(self):
        self.assertEquals(self.get_link(), self.feed_link)

    def test_get_description(self):
        self.feed.raw_feed = self.feed_fake_xml
        self.assertEquals(self.feed.get_description(), self.feed_description)

    def test_get_pubdate(self):
        self.assertEquals(self.get_pubdate(), self.feed_pubdate)

    def test_save_title(self):
        title = self.feed.title
        self.feed.title = self.feed_title
        self.feed.save_title()
        self.assertEquals(self.title, self.feed_title)

    def test_save_link(self):
        link = self.feed.link
        self.feed.link = self.feed_link
        self.feed.save_link()
        self.assertEquals(self.link, self.feed_link)

    def test_save_description(self):
        description = self.feed.description
        self.feed.description = self.feed_description
        self.feed.save_description()
        self.assertEquals(self.description, self.feed_description)

    def test_save_pubdate(self):
        pubdate = self.feed.pubdate
        self.feed.pubdate = self.feed_pubdate
        self.feed.save_pubdate()
        self.assertEquals(self.pubdate, self.feed_pubdate)

    def test_url(self):
        self.assertEquals(self.feed.url, "http://fuuu/")

    def test_string_name(self):
        self.feed.title = None
        self.assertEquals(self.feed.__str__(), self.feed.url)
        self.feed.title = "Name"
        self.assertEquals(self.feed.__str__(), self.feed.title)

