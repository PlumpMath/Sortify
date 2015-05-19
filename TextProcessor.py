import os

class TextProcess:
    '''Handles all text processing for names, file-names, etc.'''

    def __init__(self, input_text, extension=None, name=None, full_name=None):
        self.input_text = input_text
        self.extension = extension
        self.name = name
        self.full_name = full_name

        '''Gets the extension and non-extension part of text, if they exist.'''
        file_split = self.input_text.split('.')

        #If the '.' isn't there, then they both don't exist.
        if len(file_split) > 1:
            self.extension = file_split[1]
            self.full_name = file_split[0]
            self.name = os.path.basename(file_split[0])
