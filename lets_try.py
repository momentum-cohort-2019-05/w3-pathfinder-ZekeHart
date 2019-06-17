from PIL import Image, ImageDraw
from map_class import MapData
from makeMap import stats
# import re
# map_file = MapData("elevation_small.txt").read_file()
# # print(max(map_file))
# total_diff = stats(map_file)
# ele_range = total_diff.get_range()
# print(ele_range)
# print(min(map_file))


map_lines_file = MapData("elevation_large.txt").readlines_file()

# print(len(map_lines_file))



# fill_value_list = []
# for line in map_lines_file:
#     fill_value_line = []
#     for _value in line:
#         fill_value_line.append(_value - 3139)
#     fill_value_list.append(fill_value_line)


# divided_list = []
# for line in fill_value_list:
#     divided_line = []
#     for _value in line:
#         # breakpoint()
#         divided_line.append(int((_value / 2509)*255))
#     divided_list.append(divided_line)

# print(divided_list)

# max_list = []
# min_list = []
# for line in divided_list:
#     max_list.append(max(line))
#     min_list.append(min(line))
# # print(divided_list)

# # print(max(max_list))
# # print(min(min_list))

# cooler way to find min or max in list of lists, don't need to make it one file or do for loops, add this version to
# min([min(row) for row in self.elevations])

# _int = 4561
# print(((_int - min(map_file))//(ele_range/256)))

# ______
# blank_map = Image.new('RGBA', (600, 600), 'white')
# blank_map.save('test_map.png')
# draw_test = ImageDraw.Draw(blank_map)
# y = 0
# for line in map_lines_file:
#     x = 0
#     for _int in line:
#         draw_test.point((x,y),fill=(int((_int - min(map_file))//(ele_range/255))))
#         x += 1
#     y += 1
# blank_map.show()
# print("done")

# _____


# blank_map = Image.new('RGBA', (600, 600), 'white')
# blank_map.save('test_map.png')
# draw_test = ImageDraw.Draw(blank_map)
# y = 0
# for line in divided_list:
#     x = 0
#     for _int in line:
       
#         draw_test.point((x,y),fill=(_int, _int, _int))
#         x += 1
#     y += 1
# # breakpoint()
# blank_map.show()
# print("done")


# # this one _______

# blank_map = Image.new('RGB', (600, 600), 'white')
# blank_map.save('test_map.png')
# draw_test = ImageDraw.Draw(blank_map)
# y = 0
# for line in divided_list:
#     x = 0
#     for _int in line: 
#         draw_test.point((x,y),fill=(_int))
#         x += 1
#     y += 1

# # ________________
# # breakpoint()

# # a = 0
# # b = 200
# # total_elevation_change = 0
# # for a in range(600):
# #     empty_list = []
# #     empty_list.append(abs(divided_list[a][b] - divided_list[a+1][b-1]))
# #     empty_list.append(abs(divided_list[a][b] - divided_list[a+1][b]))
# #     empty_list.append(abs(divided_list[a][b] - divided_list[a+1][b+1]))
# #     if empty_list.index(min(empty_list)) == 0:
# #         b += 1
# #         total_elevation_change += empty_list[0]
# #     if empty_list.index(min(empty_list)) == 1:
# #         total_elevation_change += empty_list[1]
# #     if empty_list.index(min(empty_list)) == 2:
# #         b -= 1
# #         total_elevation_change += empty_list[2]
# #     draw_test.point((a,b),fill=(0,255,255))
    
# list_of_ele_changes = []
# for b in range(600):    
#     a = 0
#     total_elevation_change = 0
#     for a in range(600):
#         empty_list = []
#         empty_list.append(abs(divided_list[a][b] - divided_list[a+1][b-1]))
#         empty_list.append(abs(divided_list[a][b] - divided_list[a+1][b]))
#         empty_list.append(abs(divided_list[a][b] - divided_list[a+1][b+1]))
#         if empty_list.index(min(empty_list)) == 0:
#             b += 1
#             total_elevation_change += empty_list[0]
#         if empty_list.index(min(empty_list)) == 1:
#             total_elevation_change += empty_list[1]
#         if empty_list.index(min(empty_list)) == 2:
#             b -= 1
#             total_elevation_change += empty_list[2]
#         draw_test.point((a,b),fill=(0,255,255))
#     list_of_ele_changes.append(total_elevation_change)

# blank_map.show()
# best_path = list_of_ele_changes.index(min(list_of_ele_changes))
# print (best_path, list_of_ele_changes[best_path])
# # print(f"your total elevation change was {total_elevation_change} meters. Tired yet?")
# print("done")




# for line in map_lines_file:
#     x = 0
#     for _int in line:
#         draw_test.point((x,y),fill=(int((_int - 3139)//(9.8))))
#         x += 1
#         print(x,y)
#     y += 1

# for _ in range(600):
#     draw_test.point((20,x),fill=(120))
#     x += 1

# for line in range(600):
#     for _ in range(600):
#         draw_test.point((x,y),fill=(120))
#         x += 1
#     y += 1


# _int = 5000
# draw_test.point((5,5),fill=(int((_int - 3139)//(9.8))))
# draw_test.point((5,6),fill=(int((_int - 3139)//(9.8))))
# draw_test.point((5,7),fill=(int((_int - 3139)//(9.8))))
# draw_test.point((5,8),fill=(int((_int - 3139)//(9.8))))
# draw_test.point((5,9),fill=(int((_int - 3139)//(9.8))))
# blank_map.show()

# x=0
# y= 0
# for y in range(600)
#     for x in range(600)
#         (y,x) list[x] * color 


# blank_map = Image.new('RGBA', (600, 600), 'white')
# blank_map.save('test_map.png')
# draw_test = ImageDraw.Draw(blank_map)
# # blank_map.ImageDraw,Draw.point((1,1) fill=160)
# draw_test.point((200,150),fill=160)

# 



# def get_numbers_from_file(map_file):
#     with open(map_file) as initial:
#         one_file = initial.read()
#         return one_file


# unclean_file = get_numbers_from_file(map_file)
# clean_file = unclean_file.strip()
# cleaner_file = re.sub(r'[^0-9 ]', ' ', clean_file) 
# # print(clean_file)
# stripped_file = cleaner_file.split(' ')
# # print(stripped_file)

# new_int_list = []
# for x in stripped_file:
#     new_int_list.append(int(x))


# print(new_int_list.count(3969))
# map_min = min(new_int_list)
# map_max = max(new_int_list)
# min_max_diff = map_max - map_min
# print(min_max_diff)
# print(min(new_int_list))





    # initial_file = initial.readlines()
    # 
    

# stripped_lines = [line.strip() for line in initial_file]


# print(one_file)
# stripped_file = one_file.strip()
# # print(stripped_file)
# # file_max = max(stripped_file)
# # print(file_max)
# smushed_file = " ".join(stripped_file)
# print(smushed_file)
# split_lines = stripped_lines.split()

# def make_coord_pairs(stripped_lines):
#     line_list = []
#     x = False
#     for line in stripped_lines:
#         for _int in line:
#             if not x:
#                 int_pair = []
#                 int_pair.append(_int)
#                 x = True
#             else:
#                 int_pair.append(_int)
#                 line_list.append(int_pair)
#                 x = not x
#     return line_list


# list_of_coords = make_coord_pairs(stripped_lines)
# print(list_of_coords)


# print(stripped_lines)