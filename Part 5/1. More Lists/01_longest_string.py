def longest(items: list):

    longest_item = ""
    for i in items:
        if len(i) > len(longest_item):
            longest_item = i 
    
    return longest_item 


if __name__ == "__main__":
    
    my_list = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(my_list))