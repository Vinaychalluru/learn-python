
# def digital_root(str_num):
#     if int(str_num) < 10 :
#         return str_num
#     else :
#         while int(str_num) > 10:
#             s = 0
#             s = s + int(str_num[0]) + int(digital_root(str_num[1:]))
#             return str(s)
#         else:
#             return str_num
    
# print(digital_root("123456"))

def write_data(filename, words):
    try:
        with open(filename, "r") as f_output:
            f_output.write('\t'.join(words) + '\n')
    except:
        return False
    else:
        return True

print(write_data("sample.txt",['alpha','beta','gamma']))