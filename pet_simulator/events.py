# MH 1st event functions

# NEEDS:
# 3-5 events

# FOR ALL:
# prints what happened in the event and returns stat changes

def invasion(name):
    print(f"{name} points out to you that aliens seem to be invading. You take shelter in a bunker and bond while the apocalyps happens. + Hapiness + Energy")
    source = "hapiness/energy"
    return 3, 5, source

def local_crazy_crashout(name):
    print(f"The local crazy guy gets mad at {name} for stealing his sushi, and chases you and {name} all the way to london. You have to fly back in a very crowded plane. - Energy")
    source = "energy"
    return -5, source

def rabies_dad(name):
    print(f"{name} gives your dad rabies and you have to console him with baseball. - Sleep - Energy")
    source = "sleep/energy"
    return -5, -3, source

def lotion_release(name):
    print(f"A new pet lotion releases that cures the giant red warts that are commonly found on animals (y'know). You get a free sample and all of {name}'s previously unmentioned terrible skin conditions dissapear... This seems fishy. + Hapiness")
    source = "hapiness"
    return 7, source

def bank_robbery(name):
    print(f"The news reports on a bank robbery with a cctv footage showing the robber to look INCREBIBLY similar to {name}... You decide it's best to ignore it and keep the cash you found in the fridge. You get 100 glorps. + Cash I guess? + On the LAM status?")
    source = "cash money baby"
    return 100

