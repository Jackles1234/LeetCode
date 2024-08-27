class Solution(object):
    def minOperations(self, logs):
        operations = 0
        for i in range(len(logs)):
            if logs[i] == "../":
                if operations == 0:
                    continue
                else:
                    operations-=1
            elif logs[i] == "./":
                continue
            else:
                operations+=1

        return operations

#Correct
#Easy