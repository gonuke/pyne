"""this method compare two columns of results and errors, return
   ture if the two columns have the same results otherwise return
   false. Also return the list of absolute difference btw these 
   two columns"""
def compare(mode,file1,file2):
    return_type = True
    diff = []
    lines1 = file1.readlines()
    lines2 = file2.readlines()
    # assume the size  of file1 and file2 are the same
    for i in range(0,len(lines1)):
          list1 = lines1[i].strip().split()
          list1 = [float(item) for item in list1]
          list2 = lines2[i].strip().split()      
          list2 = [float(item) for item in list2]
    # compare the results only
          if (mode==1):  
            if(list1[0]!=list2[0]): 
              return_type = False
          
    # compare result1 and error1 with result2     
          if mode==2: 
            if list1[0]+list1[1] >=  list2[0] >= list1[1]-list1[0]:
               pass
            else: return_type=False
     
    
     
          if mode == 3:
               pass   
         
          diff.append(abs(list1[0]-list2[0]))

    return return_type, diff



