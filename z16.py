class SubsetGenerator:
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [curr + [num] for curr in result]
        return result

b = SubsetGenerator()
abc = [4, 5, 6]
print(b.subsets(abc))