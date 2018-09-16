# Question 44

# 1. Given three text files as input. The first text file contains the text Content1 . The second contains Content2 and the third Content3.

# 2. You should create a Python script that generates a new text file which should contain the content of all three text files.
# So the generated file should have this content:

# Content1 
# Content2 
# Content3 

# In other words, your Python script should merge the three text files. 

# 3. Also, the name of the output file should be the current timestamp. Example:2017-11-01-13-57-39-170965.txt 

from datetime import datetime
import glob2

now = datetime.now()
out_file = ("../assets/qn44/%s.txt" % now.strftime("%Y-%m-%d-%H-%M-%S-%f"))

myfiles = glob2.glob("../assets/qn44/file*.txt")

with open(out_file, "w") as out_file_obj:
    for f in myfiles:
        with open(f,"r") as f_obj :
            out_file_obj.write(f_obj.read() + "\n")
