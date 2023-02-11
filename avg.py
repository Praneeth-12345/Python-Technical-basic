inp_lst = [12, 45, 78, 36, 45, 237.11, -1, 88]

sum_lst = sum(inp_lst)

lst_avg = sum_lst/len(inp_lst)
print("Average value of the list:\n") 
print(lst_avg) 
print("Average value of the list with precision upto 3 decimal value:\n")
print(round(lst_avg,3))   