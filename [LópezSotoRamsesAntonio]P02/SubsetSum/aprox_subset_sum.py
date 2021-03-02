
class AproxSS():
    """
    Class to show the Aprox-Subset-Sum Algorithm
    """

    def aprox_subset_sum(self, s, t, e):
        """
        Returns an aproximation to a target number

            Params:
                s (list): list of integer numbers
                t (int): target number
                e (double): approximation ratio

            Returns:
                m (int): the appox number
        """
        n = len(s)
        l = [0]
        for i in range(0, n):
            l2 = []
            for j in range(0, len(l)):
                l2.append(l[j] + s[i])
            l = self.merge_list(l2,l)
            l = self.trim(l, e / (2 * n))
            for k in range(0, len(l)):
                if l[k] > t:
                    l.pop(k)
        l.reverse()
        m = l[0]
        app = (m * 100) / t
        print ("accunrancy: {0:.2f}%".format(app))
        return m

    def trim(self, list_l, d):
        """
        Trims a list

            Parameters:
                list_l (list): list of elements
                d (double): trimming parameter
            
            Returns:
                l (list): trimed list
        """
        m = len(list_l)
        l = [list_l[0]]
        last = list_l[0]
        for i in range(1, m):
            if list_l[i] > last * (1 + d):
                l.append(list_l[i])
                last = list_l[i]
        return l

    def merge_list(self, l1, l2):
        """
        Merges two lists

            Parameters:
                l1 (list): list number one
                l2 (list): list number two

            Returns:
                l (int): merged list
        """
        l = l1 + l2
        list(set(l))
        l.sort()
        return l

if __name__ == "__main__":
    apss = AproxSS()
    print("Choose an instance")
    in1 = "S = [104, 102, 201, 101, 22, 98, 25, 20, 55, 71]    t = 908     e = 0.04" 
    in2 = "S = [23, 9, 34, 112, 43, 54, 123, 90, 34, 11]    t = 590     e = 0.4"
    in3 = "S = [12, 43, 65, 9, 17, 36, 54, 66, 14, 48]    t = 395     e = 0.2"
    in4 = "S = [102, 122, 105, 136, 123, 76, 52, 23, 9, 11]    t = 666     e = 0.8"
    in5 = "S = [245, 148, 20, 12, 78, 25, 32, 76, 43, 222]    t = 1050     e = 0.4"
    print("1. " + in1 + "\n2. " + in2 + "\n3. " + in3 + "\n4. " + in4 + "\n5. " + in5)

    while True:
       choose = input("\ninput a number> ")
       try:
           choose = int(choose)
           break
       except ValueError:
           print ("\nwrong input D:")
    
    if choose == 1:
        print("\n" + in1)
        e1 = apss.aprox_subset_sum([104, 102, 201, 101, 22, 98, 25, 20, 55, 71], 908, 0.04)
        print("approx: "+ str(e1))
    elif choose == 2:
        print("\n" + in2)
        e2 = apss.aprox_subset_sum([23, 9, 34, 112, 43, 54, 123, 90, 34, 11], 590, 0.4)
        print("approx: "+ str(e2))
    elif choose == 3:
        print("\n" + in3)
        e3 = apss.aprox_subset_sum([12, 43, 65, 9, 17, 36, 54, 66, 14, 48], 395, 0.2)
        print("approx: " + str(e3))
    elif choose == 4:
        print("\n" + in4)
        e4 = apss.aprox_subset_sum([102, 122, 105, 136, 123, 76, 52, 23, 9, 11], 666, 0.8)
        print("approx: " + str(e4))
    elif choose == 5:
        print("\n" + in5)
        e5 = apss.aprox_subset_sum([245, 148, 20, 12, 78, 25, 32, 76, 43, 222], 1050, 0.4)
        print("approx: " + str(e5))
    else:
        print("\ninvalid number :(")