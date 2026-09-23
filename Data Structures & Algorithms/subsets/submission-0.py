class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.vector = []
        self.all_vectors = []

        def gen_subsets(i):
            nonlocal nums
            # base case to process subset
            if i == len(nums):
                self.all_vectors.append(self.vector.copy())
                # print(self.vector)
            else:
                # first call, i not appended
                gen_subsets(i+1)
                self.vector.append(nums[i])
                # second call, i appended
                gen_subsets(i+1)
                # lastly, pop last element
                self.vector.pop()

        gen_subsets(0)
        return self.all_vectors

        
        