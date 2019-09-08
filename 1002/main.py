# coding=-utf8

class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        char_hash = {}
        output = []
        if len(A) > 0:
            for one_string in A:
                # 统计每个字母出现的次数
                one_char_hash = {}
                for one_char in one_string:
                    if one_char not in one_char_hash.keys():
                        one_char_hash[one_char] = 0
                    one_char_hash[one_char] += 1

                for item in one_char_hash.keys():
                    if item not in char_hash.keys():
                        char_hash[item] = []
                    char_hash[item].append(one_char_hash[item])

            for item in char_hash.keys():
                min_count = 0
                if len(char_hash[item]) == len(A):
                    min_count = min(char_hash[item])

                for i in range(min_count):
                    output.append(item)
        return output
                
           
if __name__ == '__main__':
    a = ["cool","lock","cook"]
    b = Solution()
    print(b.commonChars(a))
