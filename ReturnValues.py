def allowed_dating_age(my_age):
    girls_age = my_age/2 + 7
    return girls_age
buckys_limit = allowed_dating_age(27)
raghus_limit = allowed_dating_age(20)
print("Bucky can date girls", buckys_limit, "or older")
print("Raghu can date girls", raghus_limit, "or older")