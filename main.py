import json
from date_parse import parseGitLogDateToTargetString as pS

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

with open('jsonLog.json') as f:
    data = json.load(f)

def findAllAuthorList():
    authorList = []
    for i in data["frontend-git-log-file"]:
        if i["author"] not in authorList:
            authorList.append(i["author"])
    authorList.sort()
    print(authorList)

def checkExistandDuplicate(val):
    num = int(0)
    deter = int(0) # 0: not found, 1: exist at least one
    for item in data["frontend-git-log-file"]:
        if val == item["commit"][0:8]:
            deter = int(1)
            num += int(1)
    # return 0: not exist
    # return 1: exist one
    # return 2: duplicate
    if not deter:
        return 0
    elif deter == 1 and num == 1:
        return 1
    return 2

def searchCommitInformationByHashVal(val):
    deter = checkExistandDuplicate(val)
    if deter == 0:
        print("("+val+") Not found")
        return
    elif deter == 2:
        print("("+val+") More than two search results")
        return
    try:
        # trigger merge operate cannot found stats -- only for TA testing, not for HW0205 judging
        fullState["stats"] 
        # ---------------------------------------------------------------------------------------
        fullState = next(item for item in data["frontend-git-log-file"] if val == item["commit"][0:8])
        print("(" + val + ")")
        print("- ", fullState["author"])
        print("    - ", fullState["author_email"])
        print("    - ", pS(fullState["date"]))
        print("    - ", fullState["stats"]["files_changed"], "file changed")
        print("    - ", fullState["stats"]["insertions"], "insertions")
        print("    - ", fullState["stats"]["deletions"], "deletions")
        print()
    except:
        print()
        print(bcolors.WARNING + "--- Hey !!!---")
        print(bcolors.WARNING + "(" + val + ")")
        print(bcolors.WARNING + "This is merge operate OwO. Not found stats")
        print("--------------")
        print()
        pass
if __name__ == "__main__":
    findAllAuthorList()
    searchCommitInformationByHashVal("6e5b87ed")