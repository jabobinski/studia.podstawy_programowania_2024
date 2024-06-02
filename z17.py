class PairFinder:
    def find_pair_indices(self, numbers, target):
        num_index_map = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in num_index_map:
                return [num_index_map[complement], i]
            num_index_map[num] = i
        return None

pair_finder = PairFinder()
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
print(pair_finder.find_pair_indices(numbers, target))