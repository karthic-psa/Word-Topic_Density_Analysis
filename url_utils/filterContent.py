from siteParser import URLparser
from stopwords import stop_filter
from bs4 import BeautifulSoup
import re


class Filter(object, URLparser):

    stopped_word = stop_filter()
    importance = {'title_tag': 20,'header_tag': 10, 'common_tag': 1}
    __cleaned_dataf = {}
    __cleaned_datat = {}

    def __init__(self, urllink=None):
        super(Filter, self).__init__()
        self._urllink = urllink

    def make_map(self, temp_list, content_type):
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
                        self.__cleaned_dataf[words] += self.importance[content_type]
                        __sent_data.append(words)
                        str_comb += words + ' '
                        cnt = 0
                    else:
                        self.__cleaned_dataf[words] = self.importance[content_type]
                        __sent_data.append(words)
                        str_comb += words + ' '
                        cnt = 0
                    # else:
                    #     continue
                except:
                    continue
            # for temp_sent in __sent_data:
        # print(str_comb)
        if len(str_comb)>0:
            str_comb = str_comb[:len(str_comb)-1]
            # print(str_comb)
            temp_this = str_comb.split('.')
            # print(''.join(temp_this))
            sent_data2 = ''.join(temp_this).split(',')
            # print(__sent_data2)
            for topic in sent_data2:
                if topic != '' and topic != ' ':
                    if topic in self.__cleaned_datat:
                        self.__cleaned_datat[topic] += self.importance[content_type]
                    else:
                        self.__cleaned_datat[topic] = self.importance[content_type]
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
        self.data_importance(url_data[1])
        return self.__cleaned_datat

    def data_importance(self, data_got):
        not_needed = ['script', 'style', 'img', 'input', 'option']
        for top_tags in data_got.find_all(True):
            if top_tags.name not in not_needed:
                if top_tags.name and top_tags.name:
                    if 'h' in top_tags.name:
                        # content_here = ''
                        # sent_here = ''
                        try:
                            content_here = str(top_tags.string).split()
                            # print(content_here)

                            if content_here:
                                # print('1')
                                # print('2')
                                temp = self.make_map(content_here, 'header_tag')
                                # print('3')
                                # print(temp[1])
                        except:
                            pass
                    if 'title' in top_tags.name:
                        try:
                            content_here = str(top_tags.string).split()
                            if content_here:
                                # print('2')
                                temp = self.make_map(content_here, 'title_tag')
                        except:
                            pass
                    else:
                        try:
                            content_here = str(top_tags.string).split()
                            if content_here:
                                # print('2')
                                temp = self.make_map(content_here, 'common_tag')
                        except:
                            pass



        # print(self.__cleaned_datat)
        # print __cleaned_topice



