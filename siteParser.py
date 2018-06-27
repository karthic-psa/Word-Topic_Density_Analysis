import urllib2


class URLparser:

    def __init__(self, url=None):
        self.__url = url

    def site_parser(self):
        url_site = self.__url
        head = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}

        send_request = urllib2.Request(url_site, headers=head)

        try:
            url_page = urllib2.urlopen(send_request)
        except urllib2.HTTPError, e:
            print e.fp.read()
            raise Exception('Enter a valid URL for analysis')

        page_content = url_page.read()

        return page_content
