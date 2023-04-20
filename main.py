import json
from date_parse import parseGitLogDateToTargetString as pS
from date_parse import parseMonth as pM

class monthlyContribution:
    def __init__(self, author, commit, fileChanged, insertions, deletions):
        self.author = author
        self.commit = commit
        self.fileChanged = fileChanged
        self.insertions = insertions
        self.deletions = deletions
    def addContributeItem(self, commit, fileChanged, insertions, deletions):
        self.commit += commit
        self.fileChanged += fileChanged
        self.insertions += insertions
        self.deletions += deletions
    def printMember(self):
        print("- ", self.author)
        print("    - ", self.commit, "commits")
        print("    - ", self.fileChanged, "file changed")
        print("    - ", self.insertions, "insertions")
        print("    - ", self.deletions, "deletions")
with open('jsonLog.json') as f:
    data = json.load(f)

def findAllAuthorList():
    authorList = []
    for i in data["frontend-git-log-file"]:
        if i["author"] not in authorList:
            authorList.append(i["author"])
    authorList.sort()
    # print(authorList)
    return authorList

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
        # fullState["stats"]
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
        print("--- Hey !!!---")
        print("(" + val + ")")
        print("This is merge operate OwO. Not found stats")
        print("--------------")
        print()
        pass

def searchMonthlyContribution(month, authorList):
    memberList = []
    for i in authorList:
        memberList.append(monthlyContribution(i,0,0,0,0)) 
    # print(memberList)
    for i in data["frontend-git-log-file"]:
        if pM(i["date"]) == month:
            for member in memberList:
                if i["author"] == member.author:
                    print("i[author]= ", i["author"])
                    print("member.author = ", member.author)
                    try:
                        i["stats"]
                        member.addContributeItem(int(1), 
                                                i["stats"]["files_changed"], 
                                                i["stats"]["insertions"],
                                                i["stats"]["deletions"])
                    except:
                        pass
    for i in memberList:
        i.printMember()
if __name__ == "__main__":
    searchCommitInformationByHashVal("b133cda7")
    searchMonthlyContribution("Sep", findAllAuthorList())