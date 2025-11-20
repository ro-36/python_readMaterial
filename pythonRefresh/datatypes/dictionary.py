# # # dict = {10:100,20:200,30:300,40:400}

# # # # for i in dict:
# # # #     print(dict[i])

# # # for i in dict.values():
# # #     print(i)


# # # help(dict)


# # d1 = {10:100,20:200,30:300}
# # d2 = {40:400,50:500,60:600}

# # for i in d2:
# #     d1[i] = d2[i]

# # print(d1)

# arr = [1,1,1,2,2,2,3,3,4,4,4,4,5,5]
# d = {}

# for i in arr:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1

# print(d)


d1 = {10:100,20:200,40:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    if i in d1.keys():
        d1[i]+=d2[i]
    else:
        d1[i]=d2[i]

print(d1)
