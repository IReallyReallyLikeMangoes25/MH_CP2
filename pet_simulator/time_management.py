# MH 1st time management functions

# NEEDS:
# Update time function

# update time function, takes in current day:
def update_time(current_day):
    return current_day + 1
    # returns +1 day

def update_age(pets, current_day):
    for pet in pets:
        pet["age"] = int(pet["age"])
        pet["level"] = int(pet["level"])
        pet["age"] = f"{current_day} days."
        if pet["age"]/10 is int:
            pet["level"] += 1
        return pets