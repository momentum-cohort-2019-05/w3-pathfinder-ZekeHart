import re

class MapData:

    def __init__(self, file):
        self.file = file
        # self.int_list = read_file(self.file)

    def read_file(self):
        """
        opens the file the map object was instantiated with, 
        sends it to be cleaned and converted into ints, and then returns the list of ints
        """
        with open(self.file) as initial:
            one_file = initial.read()
            return self.clean_file(one_file)
    
    def clean_file(self, raw_file):
        """
        cleans the file of all non space or number characters and replaces them with spaces (so as to not mess up newlines)
        """
        clean_file = raw_file.strip()
        cleaner_file = re.sub(r'[^0-9 ]', ' ', clean_file) 
        stripped_file = cleaner_file.split(' ')
        return self.to_numbers(stripped_file)

    def to_numbers(self, clean_file):
        """
        given a cleaned up file, returns it as a list of ints
        """
        int_list = []
        for x in clean_file:
            int_list.append(int(x))
        return int_list

    def readlines_file(self):
        with open(self.file) as initial:
            one_file = initial.readlines()
        return self.clean_lines(one_file)

    def clean_lines(self, raw_lines):
        clean_lines = []
        for line in raw_lines:
            # clean_line = re.sub(r'[^0-9 ]', ' ', line).split(' ') 
            clean_line = line.strip().split()
            clean_lines.append(clean_line)
        return self.lines_to_ints(clean_lines)

    def lines_to_ints(self, clean_lines):
        list_lines_ints = []
        for line in clean_lines:
            line_ints = []
            for _ in line:
                line_ints.append(int(_))
            list_lines_ints.append(line_ints)
        return list_lines_ints
