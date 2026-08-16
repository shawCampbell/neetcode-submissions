class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #                0
        #               0 1
        #              0 1 2
        #             0 1 2 3
        #            0 1 2 3 4

        # prev = [1]
        # for l in range(2, rowIndex+2):
        #     temp = [0]*l
        #     for x in range(len(temp)):
        #         if x == 0:
        #             temp[x] = 1
        #         elif x == len(temp)-1:
        #             temp[x] = 1
        #         else:
        #             temp[x] = prev[x] + prev[x-1]
        #     prev = temp
        # return prev

        def getRow(n):
            if (n == 1):
                return [0,1,0]
            row = [0]*(n+2)
            prev = getRow(n-1)
            print(prev)
            for i in range(1, len(row)-1):
                row[i] = prev[i] + prev[i-1]
            # row.append(0)
            return row

        return getRow(rowIndex+1)[1:rowIndex+2]



