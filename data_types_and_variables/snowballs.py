snowballs_count = int(input())
new_snowball = 0
best_snowball = False

for balls in range(1, snowballs_count + 1):

    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())


    snowball_prep = int(snowball_weight / snowball_time)
    old_snowball = snowball_prep ** snowball_quality



    if new_snowball < old_snowball:
        new_snowball = old_snowball
        best_snowball = True

    else:
        best_snowball = False

    if best_snowball == True:
        best_snowball_weight = snowball_weight
        best_snowball_time = snowball_time
        best_snowball_quality = snowball_quality

print(f"{best_snowball_weight} : {best_snowball_time} = {new_snowball} ({best_snowball_quality})")
