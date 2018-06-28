from siteParser import URLparser
from stopwords import stop_filter
from bs4 import BeautifulSoup
import re


class Filter(object, URLparser):

    stopped_word = stop_filter()
    __cleaned_dataf = {}
    __cleaned_datat = {}

    def __init__(self, urllink=None):
        super(Filter, self).__init__()
        self._urllink = urllink

    def make_map(self, temp_list):
        __sent_data = []
        __sent_data2 = []
        str_comb = ''
        str_comb1= ''
        cnt = 0
        # print(temp_list)
        for words in temp_list:
            # print('1')
            if words != 'None':
                try:
                    word = words.lower()
                    # print word
                    # if word.isalnum():
                    if word in self.stopped_word:

                        # __sent_data2.append(str_comb)
                        if cnt == 0 and len(str_comb)>0:
                            str_comb += ','
                            cnt += 1
                        continue
                    elif words in self.__cleaned_dataf:
                        # print(words)
                        self.__cleaned_dataf[words] += 1
                        __sent_data.append(words)
                        str_comb += words + ' '
                        cnt = 0
                    else:
                        self.__cleaned_dataf[words] = 1
                        __sent_data.append(words)
                        str_comb += words + ' '
                        cnt = 0
                    # else:
                    #     continue
                except:
                    continue
            # for temp_sent in __sent_data:
        # print(__sent_data)
        if len(str_comb)>0:
            sent_data2 = str_comb.split(',')
            for topic in sent_data2:
                if topic in self.__cleaned_datat:
                    self.__cleaned_datat[topic] += 1
                else:
                    self.__cleaned_datat[topic] = 1
        # print(self.__cleaned_datat)
        return self.__cleaned_dataf, ' '.join(__sent_data)


    def filter_data(self):
        url_data = super(Filter, self).site_parser(self._urllink)
        # print url_data[0]
        __remove_tags = re.compile(r'<[^>]+>')
        __tags_cleaned = __remove_tags.sub('', url_data[0]).split()
        # __tags_cleaned = url_data[0].split()
        # print(__tags_cleaned)
        __cleaned_data = {}
        __cleaned_topice = {}
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
        # print(__cleaned_data)
        not_needed = ['script', 'div', 'style', 'img', 'span', 'input', 'option', 'li']
        for top_tags in url_data[1].find_all(True):
            if top_tags.name not in not_needed:
                if top_tags.name and top_tags.name:
                    if 'h' in top_tags.name:
                        # content_here = ''
                        # sent_here = ''
                        try:
                            content_here = str(top_tags.string).split()
                            # print(content_here)
                            # print('1')
                            if content_here:
                                # print('2')
                                temp = self.make_map(content_here)
                                # print('3')
                                # print(temp[1])
                        except:
                            pass


        print(self.__cleaned_datat)
        # print __cleaned_topice
        return __cleaned_data


