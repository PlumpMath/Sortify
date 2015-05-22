import os
from sys import argv

class Pattern:
    '''Does pattern matching for text processing.'''
    def __init__(self, text, chunks=[]):
        self.text = text
        self.chunks = chunks

        #seperates any text seperated by a delimiter and puts them into chunks.
    def chunkify(self, delimiters):
        '''Takes in a list of delimiters and creates a list split by them.'''

        replaced_text = self.text

        for delimiter in delimiters:
            replaced_text = replaced_text.replace(delimiter, '%*%')

        self.chunks = replaced_text.split('%*%')

        #Also remove formatting
        self.chunks = self.remove_formatting(self.chunks)

    def remove_formatting(self, input_list):
        '''Remove any newlines and uppercase.'''
        return_list = []

        for x in input_list:
            return_x = x.lower()
            return_x = return_x.rstrip()
            return_list.append(return_x)

        return return_list

    def match(self, pattern_query):
        '''Determines if there's a match in search to both the chunks and the
        settings of the Pattern.'''
        self_set = set(self.remove_formatting(self.chunks))
        query_set = set(self.remove_formatting(pattern_query.chunks))

        return list(self_set.intersection(query_set))

class TextRead:
    '''Reads text file line by line and loads patterns.'''
    def __init__(self, text_file_path, text_list=None, delimiters = [], patterns=[]):
        self.text_file_path = text_file_path
        self.text_list = text_list
        self.delimiters = delimiters
        self.patterns = patterns

        #Load text file
        self.text_list = open(text_file_path, 'r')

        for number, each_line in enumerate(self.text_list):
            line_number = str(number)
            line_text = str(each_line)
            #Now strip the newlines, they're just annoying
            line_text = line_text.rstrip()

            #Combine them to prepare them for new Pattern instance.
            line_name = str(line_number + line_text)

            line_name = Pattern(str(line_text))

            #Make sure to chunk them
            line_name.chunkify(self.delimiters)

            #Add them to global list of patterns
            self.patterns.append(line_name)

    def lookup(self, pattern_query, threshold):
        #First compare what's in the patterns against a Pattern string query, and return
        #any matches if the list of matches is larger than the threshold number.
        return_list = []

        for pattern in self.patterns:
            #Create variable of potential match
            possible_match = pattern.match(pattern_query)

            if len(possible_match) > threshold:
                return pattern.text
