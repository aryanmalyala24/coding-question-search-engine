import regex as re
import os

path = os.path.join("scrapping", "leetcode_problem_links.txt")
with open (path,'r') as f:
    text = f.readlines()
    with open(path,'w') as file:
        for line in text:
            if '/solution' not in line:
                file.write(line)