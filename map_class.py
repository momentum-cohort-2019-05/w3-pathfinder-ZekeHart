import re
from PIL import Image, ImageDraw

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
        return self.ints_to_rgb(list_lines_ints)

    def ints_to_rgb(self, list_list_of_ints):
        max_value = self.getMax(list_list_of_ints)
        min_value = self.getMin(list_list_of_ints)
        ele_diff = max_value - min_value
        rgb_ints = []
        for line in list_list_of_ints:
            line_list = []
            for elev  in line:
                line_list.append(int((elev - min_value)/(ele_diff / 255)))
            rgb_ints.append(line_list)
        return self.draw_map_from_ints(rgb_ints)

    def getMax(self, list_list_of_ints):
        max_list = []
        for line in list_list_of_ints:
            max_list.append(max(line))
        return max(max_list)

    def getMin(self, list_list_of_ints):
        min_list = []
        for line in list_list_of_ints:
            min_list.append(min(line))
        return min(min_list)

    def draw_map_from_ints(self, list_of_list_of_ints):
        blank_map = Image.new('RGB', (600, 600), 'white')
        blank_map.save('test_map.png')
        draw_test = ImageDraw.Draw(blank_map)
        y = 0
        for line in list_of_list_of_ints:
            x = 0
            for _int in line: 
                draw_test.point((x,y),fill=(_int, _int, _int))
                x += 1
            y += 1
        blank_map.show()
