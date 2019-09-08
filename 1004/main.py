# coding=-utf8

class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        var_hash = {
            0: {
                num:
            },
            1:
        }



           
if __name__ == '__main__':
    a = 'cababc'
    b = Solution()
    
    print(b.isValid(a))
    
class Solution {
public:
    std::vector<int> psum;
    int cal(int l, int r) {
      if (!l) return psum[r];
      else return psum[r] - psum[l-1];
    }
    int longestOnes(vector<int>& A, int K) {
      if (A[0]) psum.push_back(0);
      else psum.push_back(1);
      for (int i = 1; i < A.size(); ++i) psum.push_back(psum.back() + 1-A[i]);
      int ret = 0;
      for (int i = 0; i < A.size(); ++i) {
        int low = i, high = A.size()-1, ans = -1;
        while (low <= high) {
          int mid = (low + high) >> 1;
          int cnt = cal(i, mid);
          if (cnt <= K) {
            ans = mid - i + 1;
            low = mid + 1;
          } else high = mid - 1;
        }
        ret = max(ret, ans);
      }
      return ret;
    }
};