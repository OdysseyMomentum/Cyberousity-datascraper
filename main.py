# Developed by Daniel Skala 11.14.2020

import ahocorasick
from bs4 import BeautifulSoup
import requests
import sys

class KeywordExtractor:
    """
    KeywordExtractor class is responsible for extracting crime-related keywords from a given website
    We use the aho-corasick algorithm for parallel search in text
    """

    Keywords = ahocorasick.Automaton()  # Tree of streets to search in

    histogram = dict()

    def __init__(self):
        PATH_GENERAL = r"C:\Users\danko\PycharmProjects\CyberParser"
        KEYWORDS_PATH = PATH_GENERAL + r"\Keywords"

        # Initialize the two automatons with data
        with open(KEYWORDS_PATH, encoding="utf-8", mode="r") as street_file:
            self.init_dictionary(street_file)


    def init_dictionary(self, keywords):
        """
        Build two distinct automatons: one for streets and one for cities
        :param streets: a .txt file of streets
        :param cities: a .txt file of cities
        """
        for i, line in enumerate(keywords):
            self.Keywords.add_word(line.strip('\n'), (i, line.strip('\n')))

        # Parallelize automatons
        self.Keywords.make_automaton()

    def get_tokens(self, html_string: str) -> int:
        """
        Function to return the amount of tokens in a website
        :param html_string: String to process
        :return: Amount of tokens obtained by a split
        """
        return len(html_string.split())


    def get_keywords(self, html_string: str) -> (list, set):
        """
        The main function to extract the cyber-crime related keywords from a website
        :param html_string: String to scrape from
        :return: Pair of a set and a list of the found keywords
        """

        list_of_keywords_idx = list()
        list_of_keywords = list()
        set_of_keywords = set()

        # Get all indices of keywords and append them to the list
        for end_index, (insert_order, original_value) in self.Keywords.iter(html_string):
            start_index = end_index - len(original_value) + 1
            list_of_keywords_idx.append((start_index, end_index))
            assert html_string[start_index:start_index + len(original_value)] == original_value

        # Fill in the list and set of founds keywords
        for pair in list_of_keywords_idx:
            start = pair[0]
            end = pair[1]
            word = html_string[start:end+1]
            set_of_keywords.add(word)
            list_of_keywords.append(word)

        # Build up the histogram
        for item in list_of_keywords:
            if item in self.histogram:
                self.histogram[item] += 1
            else:
                self.histogram[item] = 1

        return (set_of_keywords, list_of_keywords)


    def to_JSON(self) -> str:
        """
        Convert the histogram into a JSON format
        :return: string
        """

        hist_string = str()

        sorted_x = sorted(keyword_extractor.histogram.items(), key=lambda kv: kv[1], reverse=True)
        hist_string += "["

        for idx, item in enumerate(sorted_x[:10]):
            hist_string += "{"
            hist_string += '"word": ' + '"' + str(item[0]) + '", '
            hist_string += '"count": ' + str(item[1])
            if idx == len(sorted_x[:10])-1:
                hist_string += "}"
            else:
                hist_string += "}, "
        hist_string += "]"

        return hist_string

if __name__ == '__main__':

    HIST_SIZE = 10

    keyword_extractor = KeywordExtractor() # Instantiate the class

    url = requests.get(url=sys.argv[1])
    soup = BeautifulSoup(url.content, 'lxml').text
    soup = soup.replace("\n\n", "").lower()

    tokens = keyword_extractor.get_tokens(soup)

    key_list, key_set = keyword_extractor.get_keywords(soup)

    with open("out.txt", mode="w", encoding="utf-8") as output_file:
        output_file.write('{ "histogram": ' + keyword_extractor.to_JSON() + ', "percentage": ' + str(round(len(key_list)/tokens*100, 3)) + '}')

