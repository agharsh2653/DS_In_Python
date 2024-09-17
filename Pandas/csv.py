import pandas as pd
dis = {'a':[1,2,3,4,5,6],'b':[7,8,9,10,11,12], 'c':[13,14,15,16,17,20]}
d = pd.DataFrame(dis)
d
#d.to_csv("Test_new2.csv") #it will create csv means excel file 
#d.to_csv("Test_new1.csv",index=False) #it will remove the index value of d
d.to_csv("Test_new2.csv",index=False,header=[1,2,3]) #in this we set the header(column) value 
