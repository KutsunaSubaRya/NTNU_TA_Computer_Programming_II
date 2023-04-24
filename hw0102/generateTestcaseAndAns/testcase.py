# generate 10 testcase, 6 sunny, 4 other, one testcase 2 pts.
import secrets
import string   
import random
strSunnyLen = 100
strOtherLen = 20000000
def Upper_Lower_string(length): # define the function and pass the length as argument  
    # Print the string in Lowercase  
    result = ''.join(random.choice(string.digits + string.ascii_letters + " ,.") for x in range(length)) # run loop until the define length  
    # print(" Random string generated in Lowercase: ", result)
    return result
# generate 6 sunny case
# for i in range(1, 7):
#     file_name1 = "sunnyCase" + str(i) + "str1.txt"
#     file_name2 = "sunnyCase" + str(i) + "str2.txt"
#     with open(file_name1, "a") as fp:
#         fp.write(Upper_Lower_string(strSunnyLen))
#     with open(file_name2, "a") as fp:
#         fp.write(Upper_Lower_string(strSunnyLen))
    
# generate 4 other case
# [2075752, 14199144, 6903595, 18798873]
for i in range(1, 5):
    file_name1 = "./otherCase/otherCase" + str(i) + "str1.txt"
    file_name2 = "./otherCase/otherCase" + str(i) + "str2.txt"
    with open(file_name1, "a") as fp:
        fp.write(Upper_Lower_string(strOtherLen))
    with open(file_name2, "a") as fp:
        fp.write(Upper_Lower_string(strOtherLen))

# randomList=[]
# for i in range(4):
#    r=random.randint(1,20000000)
#    # checking whether the generated random number is not in the
#    # randomList
#    if r not in randomList:
#       # appending the random number to the resultant list, if the condition is true
#       randomList.append(r)
# # printing the resultant random numbers list
# print("non-repeating random numbers are:")
# print(randomList)
    