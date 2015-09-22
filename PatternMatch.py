import os
import fileinput
from sys import argv

class Pattern:
    '''Does pattern matching for text processing.'''
    def __init__(self, text):
        self.text = text
        self.chunks = []

        #seperates any text seperated by a delimiter and puts them into chunks.
    def chunkify(self, delimiters):
        '''Takes in a list of delimiters and creates a list split by them.'''

        replaced_text = self.text

        for delimiter in delimiters:
            replaced_text = replaced_text.replace(delimiter, '%*%')

        self.chunks = replaced_text.split('%*%')

        #Also remove formatting
        self.chunks = self.remove_formatting(self.chunks)

        #Remove any zero-length chunks
        self.chunks = self.remove_empties(self.chunks)

    def remove_formatting(self, input_list):
        '''Remove any newlines and uppercase.'''
        return_list = []

        for x in input_list:
            return_x = x.lower()
            return_x = return_x.rstrip()
            return_list.append(return_x)

        return return_list

    def remove_empties(self, input_list):
        '''Removes any empty strings from a list'''
        return_list = []

        for x in input_list:
            char = str(x)

            if len(char) > 0:
                return_list.append(char)
            else:
                pass

        return return_list

    def match(self, pattern_query):
        '''Determines if there's a match in search to both the chunks and the
        settings of the Pattern.'''

        self_set = set(self.remove_formatting(self.chunks))
        query_set = set(self.remove_formatting(pattern_query.chunks))

        possible_match = list(self_set.intersection(query_set))

        if len(possible_match) > 0:
            result = possible_match
        else:
            result = None

        return result

class TextRead:
    '''Reads text file line by line and loads patterns.'''
    def __init__(self, text_file_path, delimiters = []):
        self.text_file_path = text_file_path
        self.delimiters = delimiters
        self.raw_text = []
        self.patterns = []

##        #Load text file
        for each_line in fileinput.input(self.text_file_path):
            line_text = str(each_line)
            #Now strip the newlines, they're just annoying
            line_text = line_text.rstrip()

            self.raw_text.append(line_text)

        fileinput.close()

        #Sort the raw_text just for some sanity.

        self.raw_text.sort()

        #Now go through the raw text and create patterns based on each of them.
        for raw in self.raw_text:
            name = str(raw)
            line_name = Pattern(name)

            #Make sure to chunk them
            line_name.chunkify(self.delimiters)

            #Add them to global list of patterns
            self.patterns.append(line_name)

    def lookup(self, pattern_query, threshold, keep_match=True):
        #First compare what's in the patterns against a Pattern string query, and return
        #any matches if the list of matches is larger than the threshold number.  By default
        #Any matching pattern will remain in the patterns, unless keep_match set to False.

        #First filter out any pattern queries that don't have enough chunks to be considered a match.
        if len(pattern_query.chunks) < threshold:
            pass

        else:

            for pattern in self.patterns:
                #Create variable of potential match
                possible_match = pattern.match(pattern_query)

                if len(possible_match) >= threshold:
                    match = pattern.text

                    if keep_match == False:
                        self.patterns.remove(pattern)

                    return match
                else:
                    pass
