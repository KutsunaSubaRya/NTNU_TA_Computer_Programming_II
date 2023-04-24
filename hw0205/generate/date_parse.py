# Mon Nov 7 00:05:03 2022 +0800

monthDict = {"Jan": "01", "Feb": "02", 
            "Mar": "03", "Apr": "04", 
            "May": "05", "Jun": "06", 
            "Jul": "07", "Aug": "08", 
            "Sep": "09", "Oct": "10", 
            "Nov": "11", "Dec": "12"}

dayDict = {"1": "01", "2": "02", 
            "3": "03", "4": "04", 
            "5": "05", "6": "06", 
            "7": "07", "8": "08", 
            "9": "09"}

def parseGitLogDateToTargetString(gitLogDate: str):
    tokens = gitLogDate.split()
    ret = ""
    date = ""
    if len(tokens[2])<2:
        date = dayDict[tokens[2]]
    else:
        date = tokens[2]
    ret += tokens[4]+"/"+ monthDict[tokens[1]] + "/" + date + "/" + tokens[3]
    # print("Date you query: ", ret)
    return ret

def parseMonth(gitLogDate: str):
    tokens = gitLogDate.split()
    return tokens[1]
