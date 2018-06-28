from siteParser import URLparser
from stopwords import stop_filter
import re


class Filter(object, URLparser):

    stopped_word = stop_filter()

    def __init__(self, urllink=None):
        super(Filter, self).__init__()
        self._urllink = urllink

    def filter_data(self):
        url_data = super(Filter, self).site_parser(self._urllink)
        __remove_tags = re.compile(r'<[^>]+>')
        __tags_cleaned = __remove_tags.sub('', url_data).split()
        __cleaned_data = {}
        for words in __tags_cleaned:
            try:
                word = words.lower()
                if word.isalnum():
                    if word in self.stopped_word:
                        continue
                    elif words in __cleaned_data:
                        __cleaned_data[words] += 1
                    else:
                        __cleaned_data[words] = 1
                else:
                    continue
            except:
                continue
        print(__cleaned_data)
        return __cleaned_data


