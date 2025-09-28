import os
os.chdir(r'C:\Users\sevug\Desktop\New folder\pantech_solutions\simple_images\Tiger')
i=1
for file in os.listdir():
    src=file
    dst=str(i) +".jpg"
    os.rename(src,dst)
    i+=1

