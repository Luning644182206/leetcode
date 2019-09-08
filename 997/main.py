# coding=-utf8

class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        trust_hash = {}
        have_trust = -1
        someone_list = []
        if len(trust) > 0:
            for item in trust:
                someone = item[0]
                trustone = item[1]
                if trustone not in trust_hash:
                    trust_hash[trustone] = 0
                trust_hash[trustone] += 1
                if someone not in someone_list:
                    someone_list.append(someone)

            for item in trust_hash.keys():
                if trust_hash[item] == (N-1) and item not in someone_list:
                    have_trust = item
        else:
            have_trust = 1
        return have_trust
                
           
if __name__ == '__main__':
    a = [[1,3],[2,3],[3,1]]
    b = Solution()
    print(b.findJudge(3, a))
    