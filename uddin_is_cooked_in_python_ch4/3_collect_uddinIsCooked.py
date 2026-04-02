#list
my_list1=[1,2,'a',"Hello"]
my_list2=[1,'a',3,67]
#index 0 1 2 3
my_list1[1]=67
my_list2.append(69)
print(my_list2)

#tuple
my_t1=('Arnold', 1984)
my_t23=(1991,2003)
print(my_t23[0])
my_t23=(100,1000)

#dictionary
my_dic={"name":"Aaron",
        "list":"my_list1",
        "tup":(1,2,3)}
my_dic['tup']=(1,4,5)
my_dic['name']="brian"

#set
set1={1,2,'a',"Jello"}
set2={2,3,'b',"Jello"}
union_set=set1|set2
intersection_set=set1&set2
difference_set=set1-set2
sym_diff_set=set1^set2

print('u:',union_set)
print('i:',intersection_set)
print('d:',difference_set)
print('sd:',sym_diff_set)