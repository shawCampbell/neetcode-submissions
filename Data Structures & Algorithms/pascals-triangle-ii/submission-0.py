class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #                0
        #               0 1
        #              0 1 2
        #             0 1 2 3
        #            0 1 2 3 4

        prev = [1]
        for l in range(2, rowIndex+2):
            temp = [0]*l
            for x in range(len(temp)):
                if x == 0:
                    temp[x] = 1
                elif x == len(temp)-1:
                    temp[x] = 1
                else:
                    temp[x] = prev[x] + prev[x-1]
            prev = temp
        return prev
