AllDays = set(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun'])

days1 = set(['mon', 'tue', 'wed'])
days2 = set(['thu', 'fri', 'sat', 'sun'])
mixed_day = set(['mon', 'fri', 'tue', 'sun'])
print("===============================")

# print sets               # unordered output will comes
print(AllDays)  # {'wed', 'sun', 'sat', 'thu', 'mon', 'fri', 'tue'}

# ===============================================================
# =========print set 1 by 1=============================

for i in AllDays:
    print(i)
print("===============================")

# ==============================================

# adding items
mixed_day.add('holiday')
print(mixed_day) # {'holiday', 'sun', 'mon', 'fri', 'tue'}
print(mixed_day) # {'holiday', 'sun', 'mon', 'fri', 'tue'}
print("===============================")

# removing items
mixed_day.discard('holiday')
print(mixed_day) # {'sun', 'mon', 'fri', 'tue'}
print(mixed_day) # {'sun', 'mon', 'fri', 'tue'}
print("===============================")

# union set
fullDay = days1 | days2
print(fullDay)     # {'sun', 'thu', 'sat', 'fri', 'mon', 'wed', 'tue'}
print("===============================")

# intersection
fullDay = days2 & mixed_day
print(fullDay)   # {'fri', 'sun'}

print("===============================")
# Difference
fullDay = days1 - mixed_day
print(fullDay)          # {'wed'}
fullDay = mixed_day - days1
print(fullDay)          # {'fri', 'sun'}

#comprehension