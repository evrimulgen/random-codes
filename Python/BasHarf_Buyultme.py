cumle = "the mirkan Kastamonulu was added successfully. You may edit it again below."
x=0
for i in cumle:
    if i is ' ':
        list1 = list(cumle)
        list1[x+1] = list1[x+1].upper()
        list1[0] = list1[0].upper()
        cumle = ''.join(list1)
    x += 1

print(cumle)

# cumle2 = "the mirkan Kastamonulu was added successfully. You may edit it again below."
# cumle2 = cumle2.replace('t', 'T', 1)
# print(cumle2)

# cumle3 = "the mirkan Kastamonulu was added successfully. You may edit it again below."
# cumle3 = cumle3.capitalize()
# print(cumle3)

# cumle4 = "the mirkan Kastamonulu was added successfully. You may edit it again below."
# cumle4 = cumle4.title()
# print(cumle4)

# import time
# for i in range(25,2500):
# 	'mal-beran'.upper().center(i, '-')
# 	time.sleep(0.01)
