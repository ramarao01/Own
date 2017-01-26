import re

class Parsing:

    def parser(self,stdout):

        list1 = []
        stdlist = stdout.strip().split("\n")
        regex = re.compile(".*--.*")

        for i in range(len(stdlist)):
            list1.append(stdlist[i].split())
            x = len([m.group(0) for l in stdlist[i].split()
                 for m in [regex.search(l)] if m])
            if x == 0:
                list1.append(stdlist[i].split())
            else:
                z = x
        for i in list1:
            if len(i) != z:
                list1.remove(i)

        keys=list1[0]
        y=list1[1:]
        dic = {}
        for i in keys:
            dic[i] = []
        for i,key in enumerate(keys):
            for j in range(len(y)):
                dic[key].append(y[j][i])
       

        return dic
