# -*- coding: utf-8 -*-
class People:
    # 基本变量
    __num = 0

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        People.__num += 1
        # print('People')

    def __str__(self):
        return '编号:{},\t姓名:{},\t性别:{}'.format(People.__num, self.name, self.gender)


class Student(People):
    __num = 0

    def __init__(self, name, gender, grade):
        super().__init__(name, gender)
        self.grade = grade
        Student.__num += 1

    def __str__(self):
        return super().__str__() + ",\t在读{}年级, 学生编号:{}.".format(self.grade, Student.__num)


class Staff(People):
    __num = 0

    def __init__(self, name, gender, company):
        super().__init__(name, gender)
        self.company = company
        Staff.__num += 1

    def __str__(self):
        return super().__str__()+',\t公司为{}.'.format(Staff.__num)


if __name__ == "__main__":
    name = ['A', "B", "C", "D"]
    gender = ['W', 'W', 'M', 'M']
    people = []
    for i in range(4):
        new_people = People(name[i], gender[i])
        people.append(new_people)
        print(new_people)
        # print(new_people.__num)

    stu_name = ['E', "F", "G", "H"]
    stu_gender = ['W', 'W', 'M', 'M']
    stu_grade = [1, 2, 3, 4]
    student = []
    for i in range(4):
        new_student = Student(stu_name[i], stu_gender[i], stu_grade[i])
        student.append(new_student)
        people.append(new_student)
        print(new_student)
