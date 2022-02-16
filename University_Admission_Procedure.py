class Students:
    def __init__(self):
        self.all = []
        self.Biotech = []
        self.Chemistry = []
        self.Engineering = []
        self.Mathematics = []
        self.Physics = []

    def start(self):
        n = int(input())
        index = 3

        file = open('students.txt', 'r')
        for line in file:
            self.all.append(list(line.split(" ")))

        self.all = sorted(self.all, key=lambda x: (x[2], x[3], x[4], x[5], x[0], x[1]))
        self.all.reverse()

        return self.casting(n, index)

    def printing(self):
        print("\nBiotech")
        for i in self.Biotech:
            print(i[0], i[1], i[2])
        print("\nChemistry")
        for i in self.Chemistry:
            print(i[0], i[1], i[2])
        print("\nEngineering")
        for i in self.Engineering:
            print(i[0], i[1], i[2])
        print("\nMathematics")
        for i in self.Mathematics:
            print(i[0], i[1], i[2])
        print("\nPhysics")
        for i in self.Physics:
            print(i[0], i[1], i[2])

    def casting(self, n, index):
        for i in range(3):
            len_ = len(self.all)
            for abt in range(len_):
                try:
                    if self.all[abt][index] == "Biotech" and len(self.Biotech) < n:
                        self.Biotech.append(self.all[abt])
                        self.all[abt] = [0]
                    elif self.all[abt][index] == "Chemistry" and len(self.Chemistry) < n:
                        self.Chemistry.append(self.all[abt])
                        self.all[abt] = [0]
                    elif self.all[abt][index] == "Engineering" and len(self.Engineering) < n:
                        self.Engineering.append(self.all[abt])
                        self.all[abt] = [0]
                    elif self.all[abt][index] == "Mathematics" and len(self.Mathematics) < n:
                        self.Mathematics.append(self.all[abt])
                        self.all[abt] = [0]
                    elif self.all[abt][index] == "Physics" and len(self.Physics) < n:
                        self.Physics.append(self.all[abt])
                        self.all[abt] = [0]
                except IndexError:
                    pass

            index += 1
            if index >= 6:
                break

        return self.printing()


student = Students()
print(student.start())
