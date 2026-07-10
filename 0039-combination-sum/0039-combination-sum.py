class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []

        def backtrack(start, target, path):
            # If target becomes 0, we found a valid combination
            if target == 0:
                result.append(path[:])
                return

            # If target becomes negative, stop exploring
            if target < 0:
                return

            # Try each candidate starting from 'start'
            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # Reuse the same number, so pass i (not i+1)
                backtrack(i, target - candidates[i], path)

                # Backtrack
                path.pop()

        backtrack(0, target, [])
        return result
        