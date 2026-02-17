import random
# import my_module


# test_value: int = random.randint(20,39)
#
# print(test_value)

# print(my_module.my_fav_no)


# random_number_0_to_1 = random.random() * 10
# print(random_number_0_to_1)

# random_float = random.uniform(1,10)
# print(random_float)


# coin_face_decider = random.randint(1,2)

# if coin_face_decider ==1:
#     print("Heads")
# elif coin_face_decider ==2:
#     print("Tails")

i = 50
heads_counter = 0
tails_counter = 0
while i!=0:
    coin_face_decider = random.randint(1, 2)
    if coin_face_decider == 1:
        heads_counter+=1
        i-=1
    elif coin_face_decider == 2:
        tails_counter+=1
        i-=1
print(f"There were {heads_counter} heads and {tails_counter} tails seen in the 50 flips")

