# Story B
# Chapter 02: Trip to Town
label allchp2B:
    
    call status from _call_status_10
    $ nef_in_party = True

label allgardens1:
    stop music
    $ show_button_game_menu = False
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    scene bg garden with fade
    play music "Audio/Music/Long Road Ahead B.ogg"
    "It had been a few weeks since I accepted the emperor’s offer to remain in the castle."
    "Nefferon’s requests were always simple, not at all what I would have expected from him."
    "Every time I visited him, he would ask me to sing for him and shower me with compliments of my beauty."
    "What a strange man…"

    "Having just left the throne room after \"entertaining\" him, I decided to get a breath of fresh air in the castle gardens."
    "I loved to go there whenever I was feeling upset or stressed; it was such a peaceful place."

    "But to my surprise, I saw the young prince Duren standing at the other edge of the garden, looking beyond the outlining stone fence to the world outside."
    "He seemed troubled…"
    menu:
        "Approach him and ask what's wrong":
            $ DAffection += 20
            play music "Audio/Music/Lasting Hope (Sad Duren Theme).ogg"
            jump allgardensduren
        "Leave him alone":
            jump allgardensnefferon
            
label allgardensduren:
    show duren sad2 with dissolve
    show zuleika sad hidden
    z "What’s wrong, Duren?"

    show duren angry
    "My sudden presence startled him and he turned quickly, instinctively reaching for his bow."
    show duren
    "He looked relieved to see that it was only me."
    d "Oh, Zuleika, it's you…I'm sorry, my mind was just wandering a bit."

    z "Want to talk about it?\nYou know I can be a good listener."
    show duren sad
    d "It’s nothing much, I guess."
    d "I just…feel like there's more to life than this."
    d "During the war, I was constantly wishing for the fighting to end, but now that it's over, I'm just sitting here wasting my time away..."
    show duren angry
    d "...and by {i}his{/i} side, no less.\nHe's gotten even worse since he took the throne, always putting me down, telling me how pathetic I am…I'm so sick of it."
    show duren sad
    "He paused for a moment and looked at me, seemingly looking for something." 
    d "He hasn’t hurt you, has he, Zuleika?"
    show duren angry
    d "If he has…"
    show duren sad

    z "No, he hasn't done anything."
    z "I'm fine, but your condition worries me. There has to be something we can do to make you feel better."
    
    "I thought for a moment, then smiled."
    show zuleika normal hidden
    z "I know! Let's get out of the castle for a while, walk around the city, maybe visit with some of the villagers."
    show zuleika happy hidden
    z "It'll be fun, I promise."

    "He seemed puzzled, but he agreed nonetheless."
    show duren
    d "Alright, but if we're going to town, you'll need this."
    
    stop music
    scene bg black with fade
    "Received 500 Gold."
    $ gold += 500
    
    scene bg castle town with fade
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    $ town = "Duren"
    
    show duren with dissolve
    d "While we're here, I have some errands to run for the emperor."
    d "In the meantime, why don't you have a look around town?"
    d "I'll meet up with you back at the castle when you're done."
    hide duren with moveoutleft
    
    jump allcastletown1
    
label allgardensnefferon:
    "I decided it was best to leave him to his thoughts and continue on my way."
    "It wasn't long, however, before I ran into yet another unexpected face in the gardens: the emperor himself."
    
    show nef
    play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
    n "Taking a nice stroll through the gardens, are we?"
    show zuleika normal hidden
    z "I didn't expect to see you here, Your Majesty..."
    show nef sad
    n "Is that a problem?"
    z "No, no, of course not. I'm just surprised."
    show nef
    n "I actually came here hoping to find you, Princess."
    n "I'm going to town for a bit to take care of some...personal business. Would you care to join me?"
    
    menu:
        "\"I would be honored to, Your Majesty.\"":
            play music "Audio/Music/One-Eyed Maestro (Nefferon Theme).ogg"
            show nef happy
            n "I'm so glad to hear that, little princess."
            show nef
            n "Oh, but before we go, here's a small token of my thanks."
            
            stop music
            scene bg black with fade
            "Received 500 Gold."
            $ gold += 500
    
            scene bg castle town with fade
            play music "Audio/Music/Thatched Villagers (Village).ogg"
            $ town = "Nefferon"
            
            show nef with dissolve
            n "As much as I would love to have a beautiful woman on my arm as I prance through town, I'm afraid this is some business that I must do alone."
            n "But please, Princess, feel free to have a look around town in the meantime."
            n "I'll meet up with you back at the castle when you're done."
            hide nef with moveoutleft
            
            jump allcastletown1
            
        "\"Er...no, thanks.\"":
            show nef angry
            show zuleika angry hidden
            z "Why do you want {i}me{/i} to go with you?"
            z "If anyone, you should ask Duren, but you should at least ask a guard or something. I'm not exactly escort material..."
            n "If I had wanted to ask one of them to go with me, I would have."
            n "No, I asked you."
            show nef
            n "It's not as if you have much of a choice in the matter, remember?"
            n "I am the emperor, after all. If I say that you are to go with me, then you will."
            show nef sad
            n "I thought that was an easy enough concept to understand, but it seems I was mistaken."
            show zuleika sad hidden
            z "I...understand, Your Majesty."
            show nef
            n "Good. That's much better."
            n "Oh, and before we go, here's a small gift. Spend it wisely."
            
            stop music
            scene bg black with fade
            "Received 500 Gold."
            $ gold += 500
    
            scene bg castle town with fade
            play music "Audio/Music/Thatched Villagers (Village).ogg"
            $ town = "Nefferon"
            
            show nef with dissolve
            n "As much as I would love to have a beautiful woman on my arm as I prance through town, I'm afraid this is some business that I must do alone."
            n "But please, Princess, feel free to have a look around town in the meantime."
            n "I'll meet up with you back at the castle when you're done."
            hide nef with moveoutleft
            
            jump allcastletown1

    
label allcastletown1:
    show zuleika normal hidden
    z "Well, since I have some time, I might as well go exploring. There's a lot to do in town."
    z "The Shop is a great place to buy items or work in order to earn money and Charm."
    z "At the Library, I can brush up on my reading or teach a class to increase my Intelligence."
    z "The Training Hall provides a place where I can prepare for combat and work on my Strength."
    z "The Church is always looking for volunteers, which can increase my Kindness level."
    if zuleika_type == 'all':
        z "I heard that there's also both a nationwide martial arts tournament and a dancing competition going on where I can test my skills."
    elif zuleika_type == 'strong':
        z "I heard that there's also a nationwide martial arts tournament going on where I can test my battle skills."
    elif zuleika_type == 'charming':
        z "I heard there's even a nationwide dancing competition going on where I can test my skills."
    z "When I'm ready to move on, I can return to the castle."
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        $ competition5_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament5_done = False
    
label allcastletown_choice1:
    if energy == 0:
        jump allcastle1
        
    else:
        scene bg castle town
        play music "Audio/Music/Thatched Villagers (Village).ogg"
        "What should I do?"
    
        menu:
            "Visit the Shop":
                jump allshop_menu2
            "Go to the Library":
                jump alllibrary_menu2
            "Practice at the Training Hall":
                jump alltraining_menu2
            "Volunteer at the Church":
                jump allchurch_menu2
            "Enter Martial Arts Tournament" if zuleika_type == 'all' and tournament5_done == False or zuleika_type == 'strong' and tournament5_done == False:
                jump alltournament5
            "Enter Dancing Competition" if zuleika_type == 'all' and competition5_done == False or zuleika_type == 'charming' and competition5_done == False:
                jump allcompetition5
            "Return to the Castle":
                stop music
                jump allcastle1
            
label allshop_menu2:
    $ location = 'allshop2'
    scene bg shop
    play music "Audio/Music/Nothing Broken (Shop).ogg"
    with fade
    show vgirla normal with dissolve
    
    s "Hello! How may I help you today?"

    menu:
        "Buy":
            s "You have %(gold)d Gold remaining. What would you like to buy?"
            jump allbuy_menu2
        "Work as a sales clerk":
            hide vgirla
            if zuleika_type == 'kind':
                show zuleika sad hidden
                z "I spent several hours manning the counter, but I was too shy to attract many customers..."
                show zuleika normal hidden
                z "It's a good thing I wasn't being paid on commission. I made 85 Gold! "
            else:
                show zuleika normal hidden
                z "I spent several hours manning the counter, giving suggestions, and chatting with customers. "
                z "While it was tiring work, it was well worth it. I made 85 Gold! "
            $ gold += 85
            $ increase_charm(25)
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Return to town":
            stop music
            jump allcastletown_choice1
            
label allbuy_menu2:
    show vgirla normal
    menu:
        "\"A Gift of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'intelligent' or zuleika_type == 'strong' or zuleika_type == 'charming':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "No":
                    jump allbuy_menu2
        "\"A Bouquet of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "Buy as a gift":
                    $ gold -= 15
                    $ item_bouquet += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "Don't buy":
                    jump allbuy_menu2
        "\"Penniless Princess' Travel Kit\" - 45 Gold":
            s "Ah, what a great item! After all, young beauties like ourselves need to look good, even on the go. "
            if gold < 45:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "Buy as a gift":
                        $ gold -= 45
                        $ item_makeup += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "Don't buy":
                        jump allbuy_menu2
            else:
                menu:
                    "Yes":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "No":
                        jump allbuy_menu2
        "\"Miraculous Moonshine\" - 50 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Let go and enjoy yourself with this intoxicating drink. Just don't go overboard."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 50
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "Buy as a gift":
                    $ gold -= 50
                    $ item_liquor += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "Don't buy":
                    jump allbuy_menu2
        "\"Secret Stealth Knives\" - 80 Gold":
            s "When you're in a pinch, it helps to have something to defend yourself with. Oh, but please, don't use them in the store. "
            if gold < 80:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "Buy as a gift":
                        $ gold -= 80
                        $ item_knives += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "Don't buy":
                        jump allbuy_menu2
            else:
                menu:
                    "Yes":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "No":
                        jump allbuy_menu2
        "\"Sinister Spellbook for Beginners\" - 100 Gold":
            s "Excellent choice! I just hope you don't plan to use any of those spells on me... "
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "Buy as a gift":
                        $ gold -= 100
                        $ item_spellbook += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "Don't buy":
                        jump allbuy_menu2
            else:
                menu:
                    "Yes":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu2
                    "No":
                        jump allbuy_menu2
        "\"Elegant Earrings\" - 150 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Adorning yourself with jewelry has long been a way to show off your wealth...er...I mean...make yourself look pretty."
            if gold < 150:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 150
                    $ increase_charm(25)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "Buy as a gift":
                    $ gold -= 150
                    $ item_earrings += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "Don't buy":
                    jump allbuy_menu2
        "\"Pristine Princess Potion\" (Charm Booster) - 500 Gold":
            s "Even the gaudiest pauper can look like a beautiful princess with this potion. Then again, I guess you're already a princess..."
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_charm(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "No":
                    jump allbuy_menu2
        "\"Potent Puissance Potion (Strength Booster)\" - 500 Gold":
            s "Bulking up, huh? You know, too much of that will give you wrinkles. Not that that should stop you, of course... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_strength(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "No":
                    jump allbuy_menu2
        "\"Brain Boosting Book\" - 500 Gold":
            s "Supposedly, this stuff will make you smarter instantly. I wonder if I should try some... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_intelligence(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "No":
                    jump allbuy_menu2
        "\"Concentrated Compassion Concoction\" - 500 Gold":
            s "Aww, how kind of you...but wait, you didn't actually do anything! "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_kindness(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu2
                "No":
                    jump allbuy_menu2
        "\"Magical Map\" - 50 Gold":
            s "This is a basic world map with a few major cities marked (like this one). It may be useful if you want to know where you are."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 50
                    if zuleika_type == 'all' or zuleika_type == 'intelligent':
                        $ investigative_skill += 10
                    scene bg blank with fade
                    show nation map at truecenter
                    with dissolve
                    show zuleika normal hidden
                    z "This is a map of the known world."
                    show nation map tyraca at truecenter
                    with dissolve
                    z "I'm from the nation of Tyraca, which is named for the Tyracan Plains."
                    show nation map nalan at truecenter
                    with dissolve
                    z "To the southeast is the mysterious nation of Nalan, home of the elves, where that assassin was from."
                    z "I wonder why there aren't any cities or towns marked..."
                    show nation map pyralis at truecenter
                    with dissolve
                    z "To the west is the nation of Pyralis, which is said to be home to many dangerous demons."
                    show nation map at truecenter
                    with dissolve
                    z "I'm currently in the town surrounding the Palace of the High Court on the Callinia River."
                    scene bg shop with fade
                    show vgirla normal
                    s "You now have %(gold)d Gold."
                    jump allbuy_menu2
                "No":
                    jump allbuy_menu2
        "\"Wondrous Wardrobe Modifier\" - 100 Gold":
            s "It's always fun to try on new, cool-looking outfits, isn't it?"
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu2
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 100
                    hide vgirla with dissolve
                    jump change_clothes
                "No":
                    jump allbuy_menu2
        "Nevermind":
            jump allshop_menu2
            
label alllibrary_menu2:
    scene bg library
    play music "Audio/Music/Comfortable Mystery 4 (Library).ogg"
    with fade
    show vgirle normal with dissolve
    l "Welcome to the Library, the center for useful information. "
    l "What would you like to do?"
    
    menu:
        "Do some research":
            hide vgirle
            show zuleika normal hidden
            z "It recently occured to me that I didn't actually know much about Osirus or his past, so I decided to do some research."
            show zuleika sad hidden
            z "He sure managed to make a lot of enemies..."
            $ increase_intelligence(25)
            if zuleika_type == 'all' or zuleika_type == 'intelligent':
                $ investigative_skill += 10
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Take a class":
            hide vgirle
            if zuleika_type == 'strong':
                show zuleika angry hidden
                z "...Sheesh, what a grouchy teacher. All I did was ask where the bathroom was."
                show zuleika normal hidden
                z "At least I learned something about manners, I guess."
            else:
                show zuleika angry hidden
                z "...Sheesh, what a grouchy teacher. All I did was ask for a little bit of proof, and he kicked me out. "
                z "Ah well. I learned a lot, anyway, even without help from the teacher. "
            $ increase_intelligence(15)
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Teach class":
            hide vgirle
            if zuleika_type == 'strong':
                show zuleika sad hidden
                $ gold += 120
                z "Er...I think my students ended up teaching me more than I taught them..."
                show wlzuleika happy hidden
                z "It's a good thing I wasn't paid based on the quality of the lesson. I managed to earn 120 Gold!"
            else:
                show zuleika normal hidden
                $ gold += 120
                z "Wow, that was so refreshing! My students were great and asked some really stimulating questions. "
                z "I think they ended up teaching me more than I taught them, but sometimes, that's the way it works. "
                z "I earned 120 Gold!"
            $ increase_intelligence(25)
            $ increase_charm(10)
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Return to town":
            stop music
            jump allcastletown_choice1
            
label alltraining_menu2: 
    scene bg training
    play music "Audio/Music/Cartoon Battle (Training Hall).ogg"
    with fade
    show vboyd normal with dissolve
    
    t "Yo! Looking for some action? You've come to the right place! "
    t "What would you like to do?"
    
    menu:
        "Build muscle":
            hide vboyd
            if zuleika_type == 'intelligent':
                show zuleika angry hidden
                z "Oh man, I'm really not cut out for this sort of thing. "
                z "I swear I'm going to be sore for the next {i}week{/i}... "
            else:
                show zuleika happy hidden
                z "Wow, that was a great work out!"
                show zuleika normal hidden
                z "I feel prepared for anything now."
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Practice with a weapon":
            hide vboyd
            show zuleika normal hidden
            z "I had a great time training with my scythe today. I even learned a few new techniques."
            if zuleika_type == 'intelligent':
                show zuleika angry hidden
                z "It's just a shame that I hardly ever use the thing. "
            else:
                show zuleika happy hidden
                z "I hope I get the chance to try some of them out soon."
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Spar with a partner":
            hide vboyd
            show zuleika angry hidden
            z "The partner I ended up sparring with was twice my size and obviously had nothing against hitting a girl. "
            show zuleika normal hidden
            z "I guess I'm spoiled because Duren goes easy on me when we train."
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Return to town":
            stop music
            jump allcastletown_choice1
            
label allchurch_menu2:
    scene bg church
    play music "Audio/Music/Halls of the Undead (Church Theme).ogg"
    with fade
    show vboyf normal with dissolve
    
    p "Welcome, welcome. We can really use your help. "
    p "What would you like to do today?"
    
    menu:
        "Find lost item":
            hide vboyf
            if zuleika_type == 'charming':
                show zuleika normal hidden
                z "I spent fifteen minutes helping  a particularly chatty woman look for her lost purse. "
                show zuleika angry hidden
                z "Then I got fed up with her and threatened to leave..."
                show zuleika happy hidden
                z "...but that's when I noticed that her purse was actually wrapped around her leg."
                show zuleika normal hidden
                z "I'm sure there's a valuable lesson there somewhere."
            else:
                show zuleika angry hidden
                z "I spent several hours helping  a particularly chatty woman look for her lost purse. "
                show zuleika normal hidden
                z "But while it wasn't the most amusing way to spend my time, it was well worth it. "
                show zuleika happy hidden
                z "The woman even gave me a generous reward for helping her: a whole 200 Gold! "
                $ gold += 200
            $ increase_kindness(25)
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Console the grieving":
            hide vboyf
            if zuleika_type == 'charming':
                show zuleika sad hidden
                z "I talked to a poor little girl whose dog recently passed away. "
                show zuleika angry hidden
                z "I told her that she needed to get over it quickly so that she could get on with her life, but she apparently didn't appreciate that advice."
                show zuleika sad hidden
                z "This whole kindness thing is harder than I thought..."
            else:
                show zuleika sad hidden
                z "I talked to a poor little girl whose dog recently passed away. "
                z "It was heartbreaking, but I hope I managed to cheer her up, if even a little. "
            $ increase_kindness(30)
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Donate to the needy":
            hide vboyf
            show zuleika normal hidden
            z "It wasn't much, but I donated 25 Gold to a family that was left homeless after the war. "
            if zuleika_type == 'charming':
                z "It's much easier to just give them money than to try to apologize."
            else:
                show zuleika sad hidden
                z "I felt it was the least I could do... "
            $ increase_kindness(50)
            $ gold -= 25
            $ energy -= 1
            stop music
            jump allcastletown_choice1
        "Return to town":
            stop music
            jump allcastletown_choice1
            
label alltournament5:
    scene bg courtyard
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    with fade
    show vboyb normal with dissolve
    
    an "Welcome to the biggest event of the year: the 9th Annual Martial Arts Tournament."
    an "Test your skill against the best fighters in the nation!"
    
    menu:
        "Enter":
            show vboyb happy
            an "It's great to have you here. Let the tournament begin!"
            $ ZHP = 100
            $ EHP = 100
            stop music
            scene bg black with fade
            with Pause(.5)
            
            scene bg courtyard with fade
            an "The first match will be..."
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSZuleika at left
            with moveinleft
            an "On this side, the former Princess Zuleika, known for her courage and conquests in battle,"
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSDuren at right
            with moveinright
            an "and on this one, we have none other than the empire's favorite archer, the young Prince Duren!"
            an "Which of these legendary fighters will win? Let's find out!"
            
            hide VSDuren with moveoutright
            hide VSZuleika with moveoutleft
            
            scene bg courtyard
            play music "Audio/Music/El Magicia (Tournament - Duren).ogg"
            
            show battlezuleika normal at left
            with dissolve
            
            show HPL at topleft
            with moveinleft
            
            zb "Let's do this!"
            
            show duren at right
            with dissolve
            
            show HPR at topright
            with moveinright
            
            db "I won't go easy on you, Zuleika."
            
            jump alltournament5_choice
        
        "How to Play":
            an "New to the tournament? Don't worry, it's easy to play!"
            an "Each round, you are given three choices: Attack, Defend, or Forfeit."
            an "Attack means that you throw an offensive attack at your enemy, but be careful because they'll attack you back with the same amount of force!"
            an "Defend means that you let the enemy attack first, but they do much less damage than they normally would. Then you get a chance to counterattack, but with less power than a normal attack."
            an "Forfeit means quitting the battle. You're advised to do so if you're about to lose."
            an "The more battles you fight in the tournament, the more battle skill you'll gain, so make sure to enter at every opportunity!"
            
            jump alltournament5
            
        "Return to town":
            stop music
            jump allcastletown_choice1
            
label alltournament5_choice:
    menu:
        "Attack":
            show battlezuleika angry at left
            zb "Take this!"
            
            with flash

            $ zattack = renpy.random.randint(1,100)

            if zattack <= 35:
                show duren sad at right
                with sshake
                $ EHP -= 15

            elif zattack > 35 and zattack <= 65:
                show duren sad at right
                with sshake
                $ EHP -= 20

            elif zattack > 65 and zattack <= 85:
                show duren sad at right
                with sshake
                $ EHP -= 25
                
                show battlezuleika happy at left
                zb "Yes! Critical hit!"

            else:
                show duren sad at right
                with sshake
                $ EHP -= 30
                
                show battlezuleika happy at left
                zb "Yes! Critical hit!"
                
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPL
                hide HPR
                jump alltournament1win
                
            else:
                show battlezuleika normal at left
                show duren at right
                with Pause(1.5)
            
            show duren angry at right
            db "Now it's my turn."
            
            with flash

            $ dattack = renpy.random.randint(1,100)

            if dattack <= 10:
                show duren sad at right
                show battlezuleika happy at left
                db "Crap, I missed..."

            elif dattack > 10 and dattack <= 60:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 15

            elif dattack > 60 and dattack <= 85:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 20

            elif dattack > 85 and dattack <= 95:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 25
                
                zb "Oh no, it was a critical hit..."

            else:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 30
                
                zb "Oh no, it was a critical hit..."
                
            if ZHP < 1:
                show battlezuleika sad at left
                zb "Aww, I lost..."
                hide HPL
                hide HPR
                jump alltournament1lose
                
            else:
                show battlezuleika normal at left
                show duren at right
                
            jump alltournament5_choice
            
        "Defend":
            show battlezuleika angry at left
            
            zb "Go ahead, come at me."
            
            show duren angry at right
            db "As you wish..."
            
            with flash

            $ dattack = renpy.random.randint(1,100)

            if dattack <= 10:
                show duren sad at right
                show battlezuleika happy at left
                db "Crap, I missed..."

            elif dattack > 10 and dattack <= 80:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 5

            else:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 10
            
            if ZHP < 1:
                show battlezuleika sad at left
                zb "Aww, I lost..."
                hide HPL
                hide HPR
                jump alltournament1lose
            
            else:
                show battlezuleika normal at left
                show duren at right
                with Pause(1.5)
            
            show battlezuleika angry at left
            zb "Time to counter!"
            
            with flash
            
            $ zattack = renpy.random.randint(1,100)

            if zattack <= 35:
                show duren sad at right
                with sshake
                $ EHP -= 5

            else:
                show duren sad at right
                with sshake
                $ EHP -= 10
            
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPL
                hide HPR
                jump alltournament1win
                
            else:
                show battlezuleika normal at left
                show duren at right
                
            jump alltournament5_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    $ energy += 1
                    jump alltournament5
                "No":
                    jump alltournament5_choice
                    
label alltournament5win:
    stop music
    scene bg black with fade
    $ energy -= 1
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb happy with dissolve
    an "Congratulations on winning the first round!\nYour prize is 250 Gold!"
    $ gold += 250
    show vboyb normal
    an "That's all for today, but don't forget that the tournament is being held across the nation, so you can compete in any town."
    an "Good luck!"
    
    $ battle_skill += 50
    $ tournament5_done = True
    stop music
    hide vboyb
    jump allcastletown_choice1
    
label alltournament5lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament5
            
        "Return to town":
            jump allcastletown_choice1
            
label allcompetition5:
    stop music
    scene bg dancehall
    play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
    with fade
    
    show vgirlf normal
    an "Welcome to the biggest event of the year: the 9th Annual Dancing Competition."
    an "Test your skill against the best dancers in the nation!"
    
    menu:
        "Enter":
            show vgirlf happy
            an "It's great to have you here. Let the competition begin!"
            $ HP = 0
            $ miss = 0
            $ partner = "None"
            
            show vgirlf normal
            an "Please choose a dance partner."
            menu:
                "Duren":
                    $ partner = "Duren"
                    $ DAffection += 5
                    
                    stop music
                    scene bg black with fade
                    with Pause(.5)
                    
                    scene bg dancehall with fade
                    
                    an "The first dance will be..."
            
                    play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
                    show VSBZuleika at left
                    with moveinleft
                    an "The former Princess Zuleika, known for her courage and golden tongue,"
            
                    play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
                    show VSDuren at right
                    with moveinright
                    an "dancing with the young Prince Duren!"
                    
                    hide VSDuren with moveoutright
                    hide VSBZuleika with moveoutleft
                    
                    scene bg dancehall
                                
                    show dancezuleika normal at left
                    with dissolve
                    
                    zb "Alright, let's do this!"
            
                    show duren at right
                    with dissolve
                    
                    db "As long as you put your heart into it, I'm sure we'll do fine."
                    
                    show HP at top
                    with moveinleft
                    
                    jump allcompetition5_round1
                    
                "Nefferon":
                    $ partner = "Nefferon"
                    $ NAffection += 5
                    
                    stop music
                    scene bg black with fade
                    with Pause(.5)
                    
                    scene bg dancehall with fade
                    
                    an "The first dance will be..."
            
                    play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
                    show VSBZuleika at left
                    with moveinleft
                    an "The former Princess Zuleika, known for her courage and golden tongue,"
            
                    play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
                    show VSNefferon at right
                    with moveinright
                    an "dancing with none other than the infamous Emperor Nefferon!"
                    
                    hide VSNefferon with moveoutright
                    hide VSBZuleika with moveoutleft
                    
                    scene bg dancehall
                                                    
                    show dancezuleika normal at left
                    with dissolve
                    
                    zb "Alright, let's do this!"
            
                    show nef at right
                    with dissolve
                    
                    nb "To dance with a stunning beauty like you is truly an honor, Princess."
                    
                    show HP at top
                    with moveinleft
                    
                    jump allcompetition5_round1
                    
        "How to Play":
            an "New to the competiton? Don't worry, it's easy to play!"
            an "First, choose a partner. When you dance (and succeed) with a boy, you'll earn affection with him, so choose your partner wisely."
            an "Second, watch the step pattern that appears on the screen and try to memorize it."
            an "Finally, put your memory to the test and choose the correct combination from the choices given."
            an "If you get it right, you'll move on to the next round. If you get it wrong, you'll have to do it over again."
            an "Reach the end with as few wrong answers as possible to win!"
            
            jump allcompetition5
                    
        "Return to town":
            stop music
            jump allcastletown_choice1
            
label allcompetition5_round1:
    stop music
    show arrowright at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
      
    show arrowdown at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowright at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
      
    show arrowdown at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FiveChoice1A.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Nefferon":
                show dancezuleika happy at left
                show nef happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That's the way to do it!"
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "Well done, Princess."
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition5_round2
            
        "{image=GUI/Dance/Dance - FiveChoice1B.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition5_round1
            
label allcompetition5_round2:
    stop music

    show arrowleft at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowleft at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
      
    show arrowleft at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowdown at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowleft at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowleft at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
      
    show arrowleft at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowdown at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FiveChoice2A.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition5_round2
            
        "{image=GUI/Dance/Dance - FiveChoice2B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Nefferon":
                show dancezuleika happy at left
                show nef happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "Keep it up."
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "Truly splendid."
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition5_round3
            
label allcompetition5_round3:
    stop music

    show arrowdown at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowleft at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowleft at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FiveChoice3A.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition5_round3
            
        "{image=GUI/Dance/Dance - FiveChoice3B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Nefferon":
                show dancezuleika happy at left
                show nef happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "You're doing great!"
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "You're doing very well, Princess."
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition5_round4
            
label allcompetition5_round4:
    stop music

    show arrowright at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowleft at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
      
    show arrowleft at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowright at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowleft at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
      
    show arrowleft at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FiveChoice4A.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Nefferon":
                show dancezuleika happy at left
                show nef happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That's the way to do it!"
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "Well done, Princess."
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition5_round5
            
        "{image=GUI/Dance/Dance - FiveChoice4B.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition5_round4
            
label allcompetition5_round5:
    stop music

    show arrowdown at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 225, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 297, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 369, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 441, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 513, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FiveChoice5A.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition5_round5
            
        "{image=GUI/Dance/Dance - FiveChoice5B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Nefferon":
                show dancezuleika happy at left
                show nef happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That was fantastic, Zuleika."
                
            elif partner == "Nefferon":
                nb "As I thought, you're a remarkable dancer."
            
            jump allcompetition5win
            
label allcompetition5win:
    scene bg black with fade
    $ energy -= 1
    
    scene bg dancehall with fade
    show vgirlf normal with dissolve
        
    if miss == 0:
        show vgirlf happy
        an "Congratulations on winning First Place in the first round!\nYour prize is 250 Gold!"
        $ gold += 250
        
        if partner == "Duren":
            $ DAffection += 10
            
        elif partner == "Nefferon":
            $ NAffection += 10
        
    elif miss < 3:
        show vgirlf happy
        an "Congratulations on winning Second Place in the first round!\nYour prize is 100 Gold!"
        $ gold += 100
        
        if partner == "Duren":
            $ DAffection += 5
            
        elif partner == "Nefferon":
            $ NAffection += 5
        
    else:
        show vgirlf sad
        an "Ouch, sorry that you lost..."
        an "Better luck next time."
        
    show vgirlf normal
    an "That's all for today, but don't forget that the competition is being held across the nation, so you can compete in any town."
    an "Good luck!"
    
    $ dancing_skill += 50
    $ competition5_done = True
    stop music
    hide vgirlf
    jump allcastletown_choice1

label allcastle1:
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
        
    if town == "Duren":
        scene bg hallway night
        play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
        with fade
        
        "By the time we returned to the castle, it was already dark."
        show duren happy with dissolve
        d "I had a really great time today, Zuleika…thank you."
        show zuleika happy hidden
        z "I had a good time, too."
        z "Some of that stuff was really interesting; I'd never seen anything like it!"

        show zuleika normal hidden
        z "We should do it again sometime - if you're up for it, that is."

        d "I would love that, Princess. I'll be looking forward to it."
        $ gift = "None"
        
        jump allchp3B
        
    elif town == "Nefferon":
        scene bg hallway night with fade
        
        "By the time we returned to the castle, it was already dark." 
        show nef with dissolve
        play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
        n "Thank you again for going with me, Princess."
        show zuleika normal hidden
        z "You're very welcome, Your Majesty."
        show zuleika happy hidden
        z "I actually had a pretty good time. I saw all sorts of new, interesting things."
        show nef happy
        n "I'm glad that you enjoyed yourself."
        $ gift = "None"
        stop music
        
        if NAffection > 75:
            scene bg bedroom with fade
            "That night, I sat in my bedroom, contemplating the day's events."
            play sound "Audio/Sound/knocking_6.ogg"
            "Before long, I heard a knock at the door."
            "As I opened it, I was shocked to see Emperor Nefferon."
            play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"
            show nef with dissolve
            n "I apologize for arriving on such short notice, Princess, but I believe you lost this today."
            "He handed me a large, dark velvet-covered box." 
            show zuleika sad hidden

            z "But, Your Majesty, I haven't lost any –"

            n "Open it."
            $ gift = "Ruby Necklace"
            $ persistent.giftnecklace = True
            
            scene bg black with fade
            stop music
            "Received \"Ruby Necklace\"."
            
            scene bg bedroom with fade
            play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"
            
            show nef with dissolve

            "The necklace was incredibly beautiful, but at the same time, it sent shivers down my spine, as did the expression on the emperor’s face."
            
            show nef happy

            n "From now on, little princess, I want you to wear it for me. Do you understand?"
            
            show zuleika sadblush hidden
            z "Like this?"
            "I frowned as I noticed that it looked out of place on me."
            "Osirus had always adorned me with green emeralds and gold, since those were his favorite colors; I had never worn anything like this before." 

            "What struck me most about the necklace, however, was that it looked as if the rubies were drops of blood dripping down my neck, and that thought made me shiver."
            
            show nef
            n "As I thought, it looks beautiful on you."
            
            menu:
                "\"...Thank you.\"":
                    $ NAffection += 20
                    play music "Audio/Music/One-Eyed Maestro (Nefferon Theme).ogg"
                    show nef happy
                    "The man smiled when I thanked him, obviously pleased by my acceptance, real or not."
                    show nef sad
                    n "You do like it, don't you, Princess?"
                    show zuleika normal hidden
                    show nef
                    z "It's beautiful, Your Majesty, it really is, but…why did you give it to me?"
                    
                    "The emperor smirked, amused by my confusion."
                    n "I just wanted to give it to you. That’s all."
                    show nef angry
                    n "Is there something wrong with that?"
                    show zuleika sadblush hidden
                    z "No, I suppose not…"
                    show nef
                    
                    scene nef violent bedroom with dissolve
                    $ persistent.nefviolentbedroom = True
                    play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"

                    "He took my chin in his hand and forced me to look at him."
                    "I could feel my heart pounding in my chest and my cheeks becoming flushed."
                    n "You're cute, little princess. Despite myself, I think I've taken quite a liking to you."
                    
                    scene bg bedroom with dissolve
                    "With that, he let me go and disappeared from the room as quickly as he had come."
                    "I stared after him, speechless, not daring to move."
                    jump allchp3B

                "\"What are you doing here?\"":
                    show nef
                    "The man smiled, obviously amused by my question."

                    n "This is {i}my{/i} castle."
                    n "I can do whatever I wish, go wherever I wish, and…"
                    
                    scene nef violent bedroom with fade
                    $ persistent.nefviolentbedroom = True
                    "He forcefully brought me close to him with one hand and cupped my chin with the other."
                    n "...play with whoever I wish."

                    "I tried to get away, but he held me firm and pressed his mouth to my ear."
                    "I could feel his hot breath as he whispered..."
                    n "You do like the necklace, don't you, Princess?"

                    show zuleika sadblush hidden
                    z "I don't understand. Why did you give it to me?"

                    "The emperor chuckled at my confusion."
                    n "I just wanted to give it to you. That's all."
                    n "Is there something wrong with that?"

                    "I looked at him with defiance and refused to speak."
                    
                    scene bg bedroom with fade
                    show nef with dissolve
                    "After a moment, he finally released me from his grasp."
                    "I quickly ran to the other side of the room, picking up a sharp poker that was beside the fireplace."

                    "The man chuckled again, unaffected by my threatening stance."
                    n "You're cute, little princess. Despite myself, I think I've taken quite a liking to you."

                    hide nef with moveoutleft
                    
                    "With that, he disappeared from the room as quickly as he had come."
                    "I stared after him, speechless, poker still in hand."
                    jump allchp3B

        else:
            jump allchp3B