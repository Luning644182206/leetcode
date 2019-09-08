# coding= -utf8
# 两地调度

class Solution:
    # def twoCitySchedCost(self, costs: List[List[int]]) -> int:
    #     costA_inB = []
    #     costB_inA = []
    #     costA_all = []
    #     costB_all = []
    #     for item in costs:
    #         cost_A = item[0]
    #         cost_B = item[1]
    #         if cost_A >= cost_B:
    #             costB_all.append(cost_B)
    #             costB_inA.append(cost_A)
    #         else:
    #             costA_all.append(cost_A)
    #             costA_inB.append(cost_B)
    #     half_len_costs = len(costs)/2
    #     if len(costA_all) != half_len_costs or len(costB_all) != half_len_costs:
    #         if len(costA_all) > len(costB_all):
    #             num_pop = len(costA_all) - half_len_costs
    #             while num_pop:
    #                 min_cost_A_inB = min(costA_inB)
    #                 min_cost_A_inB_index = costA_inB.index(min_cost_A_inB)
    #                 costB_all.append(costA_inB[min_cost_A_inB_index])
    #                 costA_inB[min_cost_A_inB_index] = 1001
    #                 costA_all[min_cost_A_inB_index] = 0
    #                 num_pop -= 1
                
    #         elif len(costA_all) < len(costB_all):
    #             num_pop = len(costB_all) - half_len_costs
    #             while num_pop:
    #                 min_cost_B_inA = min(costB_inA)
    #                 min_cost_B_inA_index = costB_inA.index(min_cost_B_inA)
    #                 costA_all.append(costB_inA[min_cost_B_inA_index])
    #                 costB_inA[min_cost_B_inA_index] = 1001
    #                 costB_all[min_cost_B_inA_index] = 0
    #                 num_pop -= 1
    #     return sum(costA_all) + sum(costB_all)
    
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:


























