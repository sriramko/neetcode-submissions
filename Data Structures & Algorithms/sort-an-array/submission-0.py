class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def recurse(part: List[int]) -> List[int]:
            if len(part) < 2:
                return part
            middle = len(part) // 2
            f = part[:middle]
            l = part[middle:]
            start = recurse(f)
            end = recurse(l)
            i = j = 0
            ret = []
            while True:
                if start[i] < end[j]:
                    ret.append(start[i])
                    i += 1
                else:
                    ret.append(end[j])
                    j += 1
                if i == len(start):
                    ret.extend(end[j:])
                    break
                if j == len(end):
                    ret.extend(start[i:])
                    break
            return ret
        return recurse(nums)
            
            