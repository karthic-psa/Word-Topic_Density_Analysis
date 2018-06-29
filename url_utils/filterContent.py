from siteParser import URLparser
from stopwords import stop_filter
from bs4 import BeautifulSoup
import re


class Filter(object, URLparser):

    stopped_word = stop_filter()
    importance = {'title_tag': 400, 'header_tag': 100, 'common_tag': 1}
    __cleaned_dataf = {}
    __cleaned_datap = {}
    __cleaned_datat = {}

    def __init__(self, urllink=None):
        super(Filter, self).__init__()
        self._urllink = urllink

    # Method to make dictionaries maps (key, value) pairs of all required variations of data by weight #
    # Change scope of variables in (or out of) if conditions to generate required results - words alphanumeric or not #
    # Uncomment 'isalpha()' statement if you want only words #
    def make_map(self, temp_list, content_type):
        __sent_data = []
        __str_comb = ''
        cnt = 0
        try:
            for words in temp_list:
                if words != 'None' and words != '' and words != ' ':
                    try:
                        word = words.lower()
                        if word in self.stopped_word:
                            if cnt == 0 and len(__str_comb) > 0:
                                __str_comb += ','
                                cnt += 1
                            continue
                        elif words in self.__cleaned_dataf:
                            # if words.isalpha():
                            if words.isalnum():
                                self.__cleaned_dataf[words] += self.importance[content_type]
                                __sent_data.append(words)
                                __str_comb += words + ' '
                            cnt = 0
                        else:
                            # if words.isalpha():
                            if words.isalnum():
                                self.__cleaned_dataf[words] = self.importance[content_type]
                                __sent_data.append(words)
                                __str_comb += words + ' '
                            cnt = 0

                    except Exception:
                        continue

            if len(__str_comb) > 0:
                __str_combn = __str_comb[:len(__str_comb)-1]
                __str_combn.strip()
                temp_this = __str_combn.split('.')
                sent_data2 = ''.join(temp_this).split(',')
                for topic in sent_data2:
                    if topic != '' and topic != ' ' and topic != '" ':
                        if topic in self.__cleaned_datat:
                            self.__cleaned_datat[topic] += self.importance[content_type]
                        else:
                            self.__cleaned_datat[topic] = self.importance[content_type]

            if len(__sent_data) > 0:
                temp_str = ' '.join(__sent_data)
                if temp_str in self.__cleaned_datap:
                    self.__cleaned_datap[temp_str] += self.importance[content_type]
                else:
                    self.__cleaned_datap[temp_str] = self.importance[content_type]

        except Exception:
            print('Something went wrong, please try again')

    # Gets all the pieces of code to filter various results #
    def filter_data(self):
        try:
            url_data = super(Filter, self).site_parser(self._urllink)
            word_dens_nt = self.filtered_words_nt(url_data[0])
            self.data_importance(url_data[1])
            # print(self.__cleaned_datat)
            return self.__cleaned_datap, self.__cleaned_datat, self.__cleaned_dataf, word_dens_nt

        except Exception:
            print('Something went wrong, please try again')

    # Method to get normal word density/frequency of repeated words in a page. Still in testing - remove scripts tags #
    # Still needs work - hence in a different method for unit testing #
    def filtered_words_nt(self, data_got):
        try:
            __remove_tags = re.compile(r'<[^>]+>')
            __remove_scripts = re.compile(r'#<script(.*?)>(.*?)</script>#is')
            __scripts_cleaned = __remove_scripts.sub('', data_got)
            __tags_cleaned = __remove_tags.sub('', __scripts_cleaned).split()
            __cleaned_data = {}
            for words in __tags_cleaned:
                try:
                    word = words.lower()
                    if word.isalpha():
                        if word in self.stopped_word:
                            continue
                        elif words in __cleaned_data:
                            __cleaned_data[words] += 1
                        else:
                            __cleaned_data[words] = 1
                    else:
                        continue

                except Exception:
                    continue

            return __cleaned_data

        except Exception:
            print('Something went wrong, please try again')

    # A HTML parse-tree search #
    # Classifies data from page by tags with respective importance given by weights declared above #
    # Can be scaled as per requirements by just adding or removing require tags here in list and assigning weights #
    # Also search for required tags in 'if' statements and assign weights according in the dictionary 'importance' #
    # Need to test and experiment more with this to achieve optimum results - For now just split into three parts #
    def data_importance(self, data_got):
        try:
            not_needed = ['script', 'style', 'img', 'input', 'option']
            for top_tags in data_got.find_all(True):
                if top_tags.name not in not_needed:
                    if top_tags.name and top_tags.name:
                        if 'h' in top_tags.name:
                            try:
                                content_here = str(top_tags.string).split()
                                if content_here:
                                    self.make_map(content_here, 'header_tag')
                            except Exception:
                                pass
                        if 'title' in top_tags.name:
                            try:
                                content_here = str(top_tags.string).split()
                                if content_here:
                                    self.make_map(content_here, 'title_tag')
                            except Exception:
                                pass
                        else:
                            try:
                                content_here = str(top_tags.string).split()
                                if content_here:
                                    self.make_map(content_here, 'common_tag')
                            except Exception:
                                pass
                            for under_tags in data_got.find_all(top_tags.name):
                                if under_tags.name and under_tags.string:
                                    if 'h' in under_tags.name:
                                        try:
                                            content_here = str(under_tags.string)
                                            if content_here:
                                                self.make_map(content_here, 'header_tag')
                                        except Exception:
                                            pass
                                    if 'title' in under_tags.name:
                                        try:
                                            content_here = str(under_tags.string)
                                            if content_here:
                                                self.make_map(content_here, 'title_tag')
                                        except Exception:
                                            pass
                                    else:
                                        try:
                                            content_here = str(under_tags.string).split()
                                            if content_here:
                                                self.make_map(content_here, 'common_tag')
                                        except Exception:
                                            pass
        except Exception:
            print('Something went wrong, please try again')




