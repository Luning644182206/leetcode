class Solution:
    def corpFlightBookings(self, bookings, n):
        result = []
        if not bookings:
            return result
        
        result = [0]*n
        for item in bookings:
            start_index = item[0] - 1
            end_index = item[1]
            book_num = item[2]
            for i in range(start_index, end_index):
                # print(i, result)
                result[i] += book_num
        
        return result

if __name__ == '__main__':
    # bookings = [[1,2,10],[2,3,20],[2,5,25]]
    # n = 5
    # a = Solution()
    # print(a.corpFlightBookings(bookings, n))
    
    a = [0,0,0]
    b = [1,1]
    a[1:3] = [a+b for a, b in zip(a[1:3],b)]
    print(a)