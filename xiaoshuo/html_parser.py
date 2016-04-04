# coding:utf8
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlPaser(object):
    def _get_new_urls(self, url, soup):
        new_urls=set()
        links =soup.find_all('a',href=re.compile(r"jokehtml/\w+/\d+\.htm"))
        for link in links:
            new_url=link['href']
            new_full_url=urlparse.urljoin(url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self, url, soup):
        res_data={}
        res_data['url']=url
        #<dd class="lemmaWgt-lemmaTitle-title">
        # <h1>Python</h1>
        #title_node=soup.find('div',id='bgtop').find('h1')
        #res_data['title']=title_node.get_text()
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('span',id='text110')
        res_data['summary']=summary_node.get_text()
        return res_data

    def parse(self, url, cont):
        if url is None or cont is None:
            return
        soup = BeautifulSoup(cont, 'html.parser',from_encoding='utf-8')
        new_urls = self._get_new_urls(url,soup)
        new_data = self._get_new_data(url,soup)

        return new_urls,new_data



