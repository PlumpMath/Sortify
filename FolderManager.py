import os

class RootDirectory:
    '''Manages all things related to files and folders.'''
    def __init__(self, path, search_results=[]):
        self.path = path
        self.search_results = search_results

    def recursive_search(self, pattern, path=None):
        '''Searches recursively from root directory for a filename of a given pattern.'''
        if path:
            root_path = path

        else:
            root_path = self.path

            #If it's a new search, results are probably old.
            self.search_results = []

        dir_listing = os.listdir(root_path)

        #Check each file/directory for the pattern
        for anything in dir_listing:
            full_filepathname = os.path.join(root_path, anything)

            if str(pattern) in anything:
                self.search_results.append(full_filepathname)

            #If the item is a directory, recursively call this function on it.
            elif os.path.isdir(full_filepathname):
                self.recursive_search(pattern, path=full_filepathname)

            else:
                pass
