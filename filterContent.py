from siteParser import URLparser


class Filter(object, URLparser):

    def __init__(self, urllink=None):
        super(Filter, self).__init__()
        self._urllink = urllink

    def filter_data(self):
        url_data = super(Filter, self).site_parser(self._urllink)
        
        return url_data
