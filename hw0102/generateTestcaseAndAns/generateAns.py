import string
import mmap


def strInsert(str1, str2, pos):
    return str1[:pos] + str2 + str1[pos:]

# sunny case generate ans

# def generateSunnyAns():
#     sunnyPos = [99, 41, 38, 78, 22, 39]
#     for i in range(1, 7):
#         str1 = ""
#         str2 = ""
#         file_name1 = "sunnyCase" + str(i) + "str1.txt"
#         file_name2 = "sunnyCase" + str(i) + "str2.txt"
#         with open(file_name1, "r") as fp:
#             mm = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)
#             str1 = mm.readline().decode("utf-8")
#             mm.close()
#         with open(file_name2, "r") as fp:
#             mm = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)
#             str2 = mm.readline().decode("utf-8")
#             mm.close()
#         print(str1)
#         print(str2)
#         ansStr = strInsert(str1, str2, sunnyPos[i-1])
#         ans_file_name = "./ans/ans" + str(i) + ".txt"
#         with open(ans_file_name, "w") as fp:
#             fp.write(ansStr)

# other case generate ans
def generateOtherAns():
    otherPos = [2075752, 14199144, 6903595, 18798873]
    for i in range(1, 5):
        str1 = ""
        str2 = ""
        file_name1 = "./otherCase/otherCase" + str(i) + "str1.txt"
        file_name2 = "./otherCase/otherCase" + str(i) + "str2.txt"
        with open(file_name1, "r") as fp:
            mm = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)
            str1 = mm.readline().decode("utf-8")
            mm.close()
        with open(file_name2, "r") as fp:
            mm = mmap.mmap(fp.fileno(), 0, access=mmap.ACCESS_READ)
            str2 = mm.readline().decode("utf-8")
            mm.close()
        ansStr = strInsert(str1, str2, otherPos[i-1])
        ans_file_name = "./ans/ans" + str(i+6) + ".txt"
        with open(ans_file_name, "w") as fp:
            fp.write(ansStr)

if __name__ == '__main__':
    # generateSunnyAns()
    generateOtherAns()