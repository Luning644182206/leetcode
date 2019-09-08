# if __name__=='__main__':
#     num_prob = int(input())
#     prob_score = list(map(int, input().split(' ')))
#     prob_time = list(map(int, input().split(' ')))
#     time_all = int(input())
#     # num_prob = 5
#     # prob_score = [5,4,3,5,2]
#     # prob_time = [2,2,3,5,1]
#     # time_all = 10
    
#     _dic = {}
#     for index,item in enumerate(prob_score):
#         if item not in _dic:
#             _dic[item] = []
#         _dic[item].append(prob_time[index])
    
#     # 开始选择
#     score = []
#     times_all = [0]
#     prob_score = sorted(prob_score, reverse=True)
#     for item in prob_score:
#         min_time = min(_dic[item])
#         min_time_index = _dic[item].index(min_time)
        
#         if sum(times_all) + min_time <= time_all:
#             _dic[item][min_time_index] = 100000000
#             score.append(item)
#             times_all.append(min_time)
#     print(sum(score))

for x in[1,2,3]:print(x),