import os

class File:
    '''Gets extension, path, etc.'''

    def __init__(self, full_file_path_name, extension=None, file_name=None, new_file_name = '', destination_path=''):
        self.full_file_path_name = full_file_path_name
        self.extension = extension
        self.file_name = file_name
        self.new_file_name = new_file_name
        self.destination_path = destination_path

        #Gets the extension and non-extension part of text, if they exist.
        file_only = os.path.basename(self.full_file_path_name)
        file_split = file_only.split('.')

        #Get the filename and extension seperated into different attributes.
        self.file_name = file_split[0]
        self.extension = file_split[1]

    def move(self):
        #...and join to extension
        new_name_with_ext = str(self.new_file_name + '.' + self.extension)

        #Now join to destination path
        full_new_file_path = os.path.join(self.destination_path, new_name_with_ext)

        #Check to see if this file name already exists. Number it if so.
        if os.path.exists(full_new_file_path):
            numbered_file_name = self.underscore_number_file(self.new_file_name)
            new_name_with_ext = str(numbered_file_name + '.' + self.extension)
            full_new_file_path = os.path.join(self.destination_path, new_name_with_ext)
        else:
            pass

        os.rename(self.full_file_path_name, full_new_file_path)

    def underscore_number_file(self, text, padding=2):
        '''Takes an input file-name and figures out where to add a string'''
        for x in range(0, 100):
            ending = str('_' + str(x).zfill(padding))
            new_ending = str('_' + str(x + 1).zfill(padding))

            if text.endswith(ending):
                return_text = text.replace(ending, new_ending)
            else:
                return_text = str(text + '_' + str(1).zfill(padding))

        return return_text

class RootDirectory:
    '''Manages all things related to files and folders.'''
    def __init__(self, src_path, dest_path, files=[]):
        self.src_path = src_path
        self.dest_path = dest_path
        self.files = files

    def recursive_search(self, pattern, path=None):
        '''Searches recursively from root directory for a filename of a given pattern.'''
        if path:
            root_path = path

        else:
            root_path = self.src_path

            #If it's a new search, results are probably old.
            self.search_results = []

        dir_listing = os.listdir(root_path)

        #Check each file/directory for the pattern
        for anything in dir_listing:
            full_filepathname = os.path.join(root_path, anything)

            file_name = str(pattern)

            if file_name in anything:
                file_name = File(full_filepathname)
                self.files.append(file_name)

            #If the item is a directory, recursively call this function on it.
            elif os.path.isdir(full_filepathname):
                self.recursive_search(pattern, path=full_filepathname)

            else:
                pass

    def create_dir(self, dir_name):
        '''Creates directory within destination folder.'''

        #First check if destination folder exists, if not make it.
        if os.path.exists(self.dest_path):
            pass
        else:
            os.mkdir(self.dest_path)

        #Now create tentative directory within destination folder for file
        new_file_path = os.path.join(self.dest_path, dir_name)

        #Check to see if path exists first
        if os.path.exists(new_file_path):
            pass
        else:
            os.mkdir(new_file_path)
