 # MH 2nd work functions

# NEEDS:
# simple game to award in-game money
import random

# dictionary of customers, with their questions and the right answers
customers = {
    "Susan McCombs" : {
        "question" : "Hi, yes my name is Susan, unfortunate, I know. Could you direct me to the nearest teleporter to Earth?",
        "responses" : ["Earth one or two ma'am?", "Earth was recently demolished to make room for a subspace highway.", "Why? Gonna go 'Earth it up?' with some Earth chump? You chump.", "Honestly I don't even know dude... Right I guess?"],
        "correct" : "Earth one or two ma'am?",
        "incorrect" : ["Why? Gonna go 'Earth it up?' with some Earth chump? You chump."],
        "response" : "How did you find out my fathers name is 'Earth Chump'!?"
    },

    "Joshua Jermithan" : {
        "question" : "Greetings cashier... Have you any idea where an old soul could find a good mop?",
        "responses" : ["I don't know man I don't really like mops myself.", "I'll go look for one later sir.", "Of course an OLD MAN like you needs a mop. Such an old man thing to do. Want a mop I mean.", "Bro I'm not a janitor. If I was I would tell you though."],
        "correct" : "Bro I'm not a janitor. If I was I would tell you though.",
        "incorrect" : ["I don't know man I don't really like mops myself."],
        "response" : "You... don't like mops...? What HAS this generation come to?"
    },

    "Freddie Skips" : {
        "question" : "What's up bub? The names Freddie Skips and I'm in 'the business' if ya'know what I mean... Eitha' way, 'ave ya' seen a 'Wobble-Legs' fella walkin' 'round?",
        "responses" : ["Wouldn't you like to know pasta boy.", "Yeah in fact the last guy I seen 'ad some pretty wobbly legs. He went thatta-ways.", "No sorry dude, I did see a fellow with extremely ridgid legs though if that makes you feel any better.", "Why do you have that space pasta jammed into your pocket? Ew."],
        "correct" : "Yeah in fact the last guy I seen 'ad some pretty wobbly legs. He went thatta-ways.",
        "incorrect" : ["Why do you have that space pasta jammed into your pocket? Ew.", "Wouldn't you like to know pasta boy."],
        "response" : "AY! This was my mothers pasta!"
    },

    "Tania the Destroyer" : {
        "question" : "Bro... I need to destroy something... Can I destroy this place?",
        "responses" : {"Sure.", "Only if you can pay me more than my boss.", "Dude who are you?", "Actually there's a retirement home down the street which seems perfect for this very cause."},
        "correct" : "Actually there's a retirement home down the street which seems perfect for this very cause.",
        "incorrect" : ["Only if you can pay me more than my boss.", "Dude who are you?"],
        "response" : "Lord forbid a girl have hobbies."
    },

    "Mr. Egg Senior" : {
        "question" : "Yes yes it is I, Mr. Egg senior, father of the famous Edwina Egg, yes. Do you want an autograph young lad?",
        "responses" : {"Well you're a *knee slap* egghead, aren't you?", "Dude Edwina egg fell off after her first movie.", "YES PLEASE I STAN EDWINA AND YOU.", "If you want to give me one... I guess?"},
        "correct" : "YES PLEASE I STAN EDWINA AND YOU.",
        "incorrect" : ["Well you're a *knee slap* egghead, aren't you?", "Dude Edwina egg fell off after her first movie."],
        "response" : "How EXTREMELY offensive!"
    },

    "Riswalda Hicks" : {
        "question" : "My name is Riswalda and I'm here to say, I like to predict futures in a super cool way! In your future... Ah... Yes... I see a vacant seat in the poor chimney corner, and a crutch without an owner carefully preserved.",
        "responses" : {"Did you just quote 'a Christmas Carol'?", "Do you need something ma'am?", "Ok.", "I don't need a fortune teller to tell me things I already know."},
        "correct" : "Ok.",
        "incorrect" : ["Did you just quote 'a Christmas Carol'?"],
        "response" : "What? NO! What uhh, what even is, what did you say? A 'Fishnest... Barrel'?"
    },

    "Ol' Moldy Bones" : {
        "question" : "Ahhh, hello again youngun. Been too long since you and I went out for cod cassarole. Are you free at the moment?",
        "responses" : {"Who are you?", "Well not today but I'm free after the next galactic vinyl floors appreciators meeting.", "If I have to eat that one more time cod as a species WILL go extinct.", "What does it look like old man?"},
        "correct" : "Well not today but I'm free after the next galactic vinyl floors appreciators meeting.",
        "incorrect" : ["Who are you?", "If I have to eat that one more time cod as a species WILL go extinct."],
        "response" : "I thought I knew you... Turns out I was wrong..."
    },

    "That one guy who always buys choclate bars and them throws them at birds." : {
        "question" : "...... Can I buy some of these choclate bars?",
        "responses" : {"Absolutely not.", "If you start throwing them at my neighbor.", "Please just eat one choclate bar none of us even care about the birds anymore.", "I don't see why not."},
        "correct" : "I don't see why not.",
        "incorrect" : ["Absolutely not."],
        "response" : ".... Just try and look at it from my perspective."
    },

    "Dave Smith" : {
        "question" : "Hey! It's me! Dave! I sure love my job in accounting, how's your day?",
        "responses" : {"Worse than yours.", "Dave. I work in a space gas station. It's terrible like every other day you ask.", "Just get out Dave.", "Hey everyone! Look at 'accounting Dave'! Stop saying that EVERY time you see anyone!"},
        "correct" : "Good enough.",
        "incorrect" : ["Hey everyone! Look at 'accounting Dave'! Stop saying that EVERY time you see anyone!"],
        "response" : "Hey! Accounting is a noble trade! Passed down by the nights of the pie chart table to my father and my fathers father and my fathers fathers father and my-"
    },

    "Anthony Wobble-Legs" : {
        "question" : "Psst... Hey bruiser... Youz seen a guy with spaghettaboutit jammed up in 'is trousers? I'm lokin' fer a fella sorta' like that...",
        "responses" : {"Spaghettaboutwhat?", "What's it to ya'?", "I might've... And the perp might've takin' a turn down 'I don't get paid enough for this ave'.", "No."},
        "correct" : "No.",
        "incorrect" : ["I might've... And the perp might've takin' a turn down 'I don't get paid enough for this ave'."],
        "response" : "Why I outa'...."
    }
}

def work(money, customer_list):
    earnings = 0
    # random customer appears from the customer dictionary and asks their question
    customer = customer_list(random.randint(1, 10))
    customer_list.pop(customer)
    print(f"{customer}: {customer["question"]}")
    # response option are given to the user
    for i, response in customer["responses"]:
        print(f"{i}. {response}")
    while True:
        choice = input("How do you respond: ")
        if int(choice) > len(customer["responses"]):
            continue
        else:
            choice = customer["responses"][int(choice)]
            break
    # if the users response is the correct answer add + 10 to earnings
    if choice = customer["correct"]:
        money += 10
    # if the users response is the wrong answer then subtract - 10 from earnings
    elif choice in customer["incorrect"]:
        money -= 10
        print(customer["response"])
    # if the users response is a neutral answer add + 5 to earnings
    else:
        money += 5
    # returns the days earnings
    return money
    