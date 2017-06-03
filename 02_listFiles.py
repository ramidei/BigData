import os
def rename_files():
    #(1) get file names from a folder
    file_list = os.listdir(r"C:\00_IMS_Courses\90_BigData\images\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Direstory is "+saved_path)
    os.chdir(r"C:\00_IMS_Courses\90_BigData\images\prank")
    print("Current Working Direstory is "+os.getcwd())

    #(2) for each file, rename filename
    for file_name in file_list:
        #os.rename(file_name,file_name.translate(None,"0123456789"))
        os.rename(file_name,file_name.translate(None,".jpg"))
        reverse_name = file_name[::-1]
        print (reverse_name)
        #os.rename(file_name,file_name+ ".jpg")
        #os.rename(file_name,file_name.lstrip(".jpg"))
    os.chdir(saved_path)
        #print("Current Working Direstory is "+os.getcwd())
rename_files()


        #os.rename(file_name,file_name.translate(None,"0123456789").lstrip())
        #os.rename(file_name,file_name.lstrip("0123456789"))
