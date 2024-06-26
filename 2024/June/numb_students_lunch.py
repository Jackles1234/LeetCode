class Solution(object):
    def countStudents(self, students, sandwiches):
        student_count = 0
        while student_count < len(students):
            if students[student_count] == sandwiches[0]:
                students.pop(student_count)
                sandwiches.pop(0)
                student_count = 0
            else:
                student_count+=1
        return(len(students))
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        

#### CORRECT ####
#https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/