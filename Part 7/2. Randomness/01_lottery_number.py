import random 

def lottery_numbers(amount, lower, upper):
    list1 = [i for i in range(lower, upper+1)]
    random.shuffle(list1)
    final_list = list1[:amount]
    final_list.sort()
    return final_list

if __name__ == "__main__":
    print(lottery_numbers(4, 10, 20))