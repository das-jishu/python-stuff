import os
difficulty = input("Enter difficulty: ")
os.system("git add .")
os.system("git commit -m \"Added " + difficulty + " problem.\"")
os.system("git push -u origin master")
