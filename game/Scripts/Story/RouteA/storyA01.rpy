# Story A
# Chapter 01: An Unexpected Meeting
label allchp2A:
    stop music
    $ show_button_game_menu = False
    scene bg jarconia with fade
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    
    "Several weeks later, we were at our destination, the City of Jarconia. "
    "It was a large, bustling city full of rushed travelers and merchants advertising their \"rare\" items for sale. "
    "With everything else going on, I was relieved to find that hardly anyone noticed us, despite our strange appearances."
    
    show lchael
    c "While here, I have some...personal business to take care of. "
    c "In the meantime, you might want to have a look around town. It is only a suggestion, of course."
    c "I will meet you at the inn when I am done. I have already reserved a room for you."
    
    hide lchael with moveoutleft
    
    show wlzuleika normal hidden
    z "Well, since I have some time, I might as well go exploring. There's a lot to do in town. "
    z "The Shop is a great place to buy items or work in order to earn money and Charm. "
    z "At the Library, I can brush up on my reading or teach a class to increase my Intelligence. "
    z "The Training Hall provides a place where I can prepare for combat and work on my Strength. "
    z "The Church is always looking for volunteers, which can increase my Kindness level. "
    if zuleika_type == 'all':
        z "I heard that there's also both a nationwide martial arts tournament and a dancing competition going on where I can test my skills."
    elif zuleika_type == 'strong':
        z "I heard that there's also a nationwide martial arts tournament going on where I can test my battle skills."
    elif zuleika_type == 'charming':
        z "I heard that there's also a nationwide dancing competition going on where I can test my skills."
    z "When I'm ready to move on, I can rest at the Inn. "
    
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        $ competition1_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament1_done = False
    
label alljarconia_choice:
    scene bg jarconia
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    
    if energy == 0:
        jump alljarconiainn1
        
    else:
        "What should I do?"
    
        menu:
            "Visit the Shop":
                jump allshop_menu1
            "Go to the Library":
                jump alllibrary_menu1
            "Practice at the Training Hall":
                jump alltraining_menu1
            "Volunteer at the Church":
                jump allchurch_menu1
            "Enter Martial Arts Tournament" if zuleika_type == 'all' and tournament1_done == False or zuleika_type == 'strong' and tournament1_done == False:
                jump alltournament1
            "Enter Dancing Competition" if zuleika_type == 'all' and competition1_done == False or zuleika_type == 'charming' and competition1_done == False:
                jump allcompetition1
            "Rest at the Inn":
                stop music
                jump alljarconiainn1
            
label allshop_menu1:
    $ location = 'allshop1'
    scene bg shop
    play music "Audio/Music/Nothing Broken (Shop).ogg"
    with fade
    show vgirla normal with dissolve
    
    s "Hello! How may I help you today?"

    menu:
        "Buy":
            s "You have %(gold)d Gold remaining. What would you like to buy?"
            jump allbuy_menu1
        "Work as a sales clerk":
            hide vgirla
            if zuleika_type == 'kind':
                show wlzuleika sad hidden
                z "I spent several hours manning the counter, but I was too shy to attract many customers..."
                show wlzuleika normal hidden
                z "It's a good thing I wasn't being paid on commission. I made 85 Gold! "
            else:
                show wlzuleika normal hidden
                z "I spent several hours manning the counter, giving suggestions, and chatting with customers. "
                z "While it was tiring work, it was well worth it. I made 85 Gold! "
            $ gold += 85
            $ increase_charm(25)
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Return to town":
            stop music
            jump alljarconia_choice
            
label allbuy_menu1:
    show vgirla normal
    menu:
        "\"A Gift of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'intelligent' or zuleika_type == 'strong' or zuleika_type == 'charming':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "No":
                    jump allbuy_menu1
        "\"A Bouquet of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "Buy as a gift":
                    $ gold -= 15
                    $ item_bouquet += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "Don't buy":
                    jump allbuy_menu1
        "\"Penniless Princess' Travel Kit\" - 45 Gold":
            s "Ah, what a great item! After all, young beauties like ourselves need to look good, even on the go. "
            if gold < 45:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "Buy as a gift":
                        $ gold -= 45
                        $ item_makeup += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "Don't buy":
                        jump allbuy_menu1
            else:
                menu:
                    "Yes":
                        $ gold -= 45
                        $ increase_charm(15)
                        $ charm += 15
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "No":
                        jump allbuy_menu1
        "\"Miraculous Moonshine\" - 50 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Let go and enjoy yourself with this intoxicating drink. Just don't go overboard."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 50
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "Buy as a gift":
                    $ gold -= 50
                    $ item_liquor += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "Don't buy":
                    jump allbuy_menu1
        "\"Secret Stealth Knives\" - 80 Gold":
            s "When you're in a pinch, it helps to have something to defend yourself with. Oh, but please, don't use them in the store. "
            if gold < 80:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "Buy as a gift":
                        $ gold -= 80
                        $ item_knives += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "Don't buy":
                        jump allbuy_menu1
            else:
                menu:
                    "Yes":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "No":
                        jump allbuy_menu1
        "\"Sinister Spellbook for Beginners\" - 100 Gold":
            s "Excellent choice! I just hope you don't plan to use any of those spells on me... "
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "Buy as a gift":
                        $ gold -= 100
                        $ item_spellbook += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "Don't buy":
                        jump allbuy_menu1
            else:
                menu:
                    "Yes":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu1
                    "No":
                        jump allbuy_menu1
        "\"Elegant Earrings\" - 150 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Adorning yourself with jewelry has long been a way to show off your wealth...er...I mean...make yourself look pretty."
            if gold < 150:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 150
                    $ increase_charm(25)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "Buy as a gift":
                    $ gold -= 150
                    $ item_earrings += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "Don't buy":
                    jump allbuy_menu1
        "\"Pristine Princess Potion\" (Charm Booster) - 500 Gold":
            s "Even the gaudiest pauper can look like a beautiful princess with this potion. Speaking of which, has anyone ever told you that you look just like Princess Zuleika?"
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_charm(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "No":
                    jump allbuy_menu1
        "\"Potent Puissance Potion (Strength Booster)\" - 500 Gold":
            s "Bulking up, huh? You know, too much of that will give you wrinkles. Not that that should stop you, of course... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_strength(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "No":
                    jump allbuy_menu1
        "\"Brain Boosting Book\" - 500 Gold":
            s "Supposedly, this stuff will make you smarter instantly. I wonder if I should try some... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_intelligence(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "No":
                    jump allbuy_menu1
        "\"Concentrated Compassion Concoction\" - 500 Gold":
            s "Aww, how kind of you...but wait, you didn't actually do anything! "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_kindness(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu1
                "No":
                    jump allbuy_menu1
        "\"Magical Map\" - 50 Gold":
            s "This is a basic world map with a few major cities marked (like this one). It may be useful if you want to know where you are."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 50
                    if zuleika_type == 'all' or zuleika_type == 'intelligent':
                        $ investigative_skill += 10
                    scene bg blank with fade
                    show nation map at truecenter
                    with dissolve
                    show wlzuleika normal hidden
                    z "This is a map of the known world."
                    show nation map tyraca at truecenter
                    with dissolve
                    z "I'm from the nation of Tyraca, which is named for the Tyracan Plains."
                    show nation map nalan at truecenter
                    with dissolve
                    z "To the southeast is the mysterious nation of Nalan, home of the elves, where Chael is from."
                    z "I wonder why there aren't any cities or towns marked..."
                    show nation map pyralis at truecenter
                    with dissolve
                    z "To the west is the nation of Pyralis, which is said to be home to many dangerous demons."
                    show nation map at truecenter
                    with dissolve
                    z "I'm currently in the City of Jarconia on the Tyracan-Pyralin border."
                    scene bg shop with fade
                    show vgirla normal
                    s "You now have %(gold)d Gold."
                    jump allbuy_menu1
                "No":
                    jump allbuy_menu1
        "\"Wondrous Wardrobe Modifier\" - 100 Gold":
            s "It's always fun to try on new, cool-looking outfits, isn't it?"
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu1
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 100
                    hide vgirla with dissolve
                    jump change_clothes
                "No":
                    jump allbuy_menu1
        "Nevermind":
            jump allshop_menu1
            
label alllibrary_menu1:
    scene bg library
    play music "Audio/Music/Comfortable Mystery 4 (Library).ogg"
    with fade
    show vgirle normal with dissolve
    l "Welcome to the Library, the center for useful information. "
    l "What would you like to do?"
    
    menu:
        "Do some research":
            hide vgirle
            show wlzuleika normal hidden
            z "I was a bit curious about Nalan after meeting Chael, so I did some research. "
            if zuleika_type == 'strong':
                show wlzuleika sad hidden
                z "Too bad none of these books make any sense to me..."
            else:
                z "I feel like I can understand him a lot better now. "
            $ increase_intelligence(25)
            if zuleika_type == 'all' or zuleika_type == 'intelligent':
                $ investigative_skill += 10
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Take a class":
            hide vgirle
            if zuleika_type == 'strong':
                show wlzuleika angry hidden
                z "...Sheesh, what a grouchy teacher. All I did was ask where the bathroom was."
                show wlzuleika normal hidden
                z "At least I learned something about manners, I guess."
            else:
                show wlzuleika angry hidden
                z "...Sheesh, what a grouchy teacher. All I did was ask for a little bit of proof, and he kicked me out. "
                z "Ah well. I learned a lot, anyway, even without help from the teacher. "
            $ increase_intelligence(15)
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Teach class":
            hide vgirle
            if zuleika_type == 'strong':
                show wlzuleika sad hidden
                $ gold += 120
                z "Er...I think my students ended up teaching me more than I taught them..."
                show wlzuleika happy hidden
                z "It's a good thing I wasn't paid based on the quality of the lesson. I managed to earn 120 Gold!"
            else:
                show wlzuleika normal hidden
                $ gold += 120
                z "Wow, that was so refreshing! My students were great and asked some really stimulating questions. "
                z "I think they ended up teaching me more than I taught them, but sometimes, that's the way it works. "
                z "I earned 120 Gold!"
            $ increase_intelligence(25)
            $ increase_charm(10)
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Return to town":
            stop music
            jump alljarconia_choice
            
label alltraining_menu1: 
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
                show wlzuleika angry hidden
                z "Oh man, I'm really not cut out for this sort of thing. "
                z "I swear I'm going to be sore for the next {i}week{/i}... "
            else:
                show wlzuleika happy hidden
                z "Wow, that was a great work out!"
                show wlzuleika normal hidden
                z "I feel prepared for anything now."
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Practice with a weapon":
            hide vboyd
            show wlzuleika normal hidden
            z "I had a great time training with my scythe today. I even learned a few new techniques."
            if zuleika_type == 'intelligent':
                show wlzuleika angry hidden
                z "It's just a shame that I hardly ever use the thing. "
            else:
                show wlzuleika happy hidden
                z "I hope I get the chance to try some of them out soon."
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Spar with a partner":
            hide vboyd
            show wlzuleika angry hidden
            z "The partner I ended up sparring with was twice my size and obviously had nothing against hitting a girl."
            show wlzuleika normal hidden
            z "I wonder what it would be like to spar against someone like Chael. I bet it would be pretty interesting. "
            if zuleika_type == 'intelligent':
                show wlzuleika angry hidden
                z "...I bet it would also be very painful. "
            else:
                show wlzuleika happy hidden
                z "What a great challenge that would be!"
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Return to town":
            stop music
            jump alljarconia_choice
            
label allchurch_menu1:
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
                show wlzuleika normal hidden
                z "I spent fifteen minutes helping  a particularly chatty woman look for her lost purse. "
                show wlzuleika angry hidden
                z "Then I got fed up with her and threatened to leave..."
                show wlzuleika happy hidden
                z "...but that's when I noticed that her purse was actually wrapped around her leg."
                show wlzuleika normal hidden
                z "I'm sure there's a valuable lesson there somewhere."
            else:
                show wlzuleika angry hidden
                z "I spent several hours helping  a particularly chatty woman look for her lost purse. "
                show wlzuleika normal hidden
                z "But while it wasn't the most amusing way to spend my time, it was well worth it. "
                show wlzuleika happy hidden
                z "The woman even gave me a generous reward for helping her: a whole 200 Gold! "
                $ gold += 200
            $ increase_kindness(25)
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Console the grieving":
            hide vboyf
            if zuleika_type == 'charming':
                show wlzuleika sad hidden
                z "I talked to a poor little girl whose dog recently passed away. "
                show wlzuleika angry hidden
                z "I told her that she needed to get over it quickly so that she could get on with her life, but she apparently didn't appreciate that advice."
                show wlzuleika sad hidden
                z "This whole kindness thing is harder than I thought..."
            else:
                show wlzuleika sad hidden
                z "I talked to a poor little girl whose dog recently passed away. "
                z "It was heartbreaking, but I hope I managed to cheer her up, if even a little. "
            $ increase_kindness(30)
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Donate to the needy":
            hide vboyf
            show wlzuleika normal hidden
            z "It wasn't much, but I donated 25 Gold to a family that was left homeless after the war. "
            if zuleika_type == 'charming':
                z "It's much easier to just give them money than to try to apologize."
            else:
                show wlzuleika sad hidden
                z "I felt it was the least I could do... "
            $ increase_kindness(50)
            $ gold -= 25
            $ energy -= 1
            stop music
            jump alljarconia_choice
        "Return to town":
            stop music
            jump alljarconia_choice
            
label alltournament1:
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
            
            jump alltournament1_choice
            
        "How to Play":
            an "New to the tournament? Don't worry, it's easy to play!"
            an "Each round, you are given three choices: Attack, Defend, or Forfeit."
            an "Attack means that you throw an offensive attack at your enemy, but be careful because they'll attack you back with the same amount of force!"
            an "Defend means that you let the enemy attack first, but they do much less damage than they normally would. Then you get a chance to counterattack, but with less power than a normal attack."
            an "Forfeit means quitting the battle. You're advised to do so if you're about to lose."
            an "The more battles you fight in the tournament, the more battle skill you'll gain, so make sure to enter at every opportunity!"
            
            jump alltournament1
            
        "Return to town":
            stop music
            jump alljarconia_choice
            
label alltournament1_choice:
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
                
            jump alltournament1_choice
            
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
                
            jump alltournament1_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    $ energy += 1
                    jump alltournament1
                "No":
                    jump alltournament1_choice
                    
label alltournament1win:
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
    $ tournament1_done = True
    stop music
    hide vboyb
    jump alljarconia_choice
    
label alltournament1lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament1
            
        "Return to town":
            jump alljarconia_choice
            
label allcompetition1:
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
                    
                    jump allcompetition1_round1
                    
                "Chael":
                    $ partner = "Chael"
                    $ CAffection += 5
                    
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
                    show VSChael at right
                    with moveinright
                    an "dancing with the mysterious Prince Chael of Nalan!"
                    
                    hide VSChael with moveoutright
                    hide VSBZuleika with moveoutleft
                    
                    scene bg dancehall
                                                    
                    show dancezuleika normal at left
                    with dissolve
                    
                    zb "Alright, let's do this!"
            
                    show chael at right
                    with dissolve
                    
                    cb "I'm ready whenever you are, Princess."
                    
                    show HP at top
                    with moveinleft
                    
                    jump allcompetition1_round1
                    
        "How to Play":
            an "New to the competiton? Don't worry, it's easy to play!"
            an "First, choose a partner. When you dance (and succeed) with a boy, you'll earn affection with him, so choose your partner wisely."
            an "Second, watch the step pattern that appears on the screen and try to memorize it."
            an "Finally, put your memory to the test and choose the correct combination from the choices given."
            an "If you get it right, you'll move on to the next round. If you get it wrong, you'll have to do it over again."
            an "Reach the end with as few wrong answers as possible to win!"
            
            jump allcompetition1
                    
        "Return to town":
            stop music
            jump alljarconia_choice
            
label allcompetition1_round1:
    
    show arrowdown at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowup at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
      
    show arrowleft at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowup at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup with dissolve
      
    show arrowleft at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
       
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FourChoice1A.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition1_round1
            
        "{image=GUI/Dance/Dance - FourChoice1B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That's the way to do it!"
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Chael":
                cb "Well done, Princess."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
            
            jump allcompetition1_round2
    
label allcompetition1_round2:
 
    stop music
    
    show arrowdown at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    hide arrowleft with dissolve
      
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
       
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FourChoice2A.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "Keep it up."
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Chael":
                cb "Your moves are as graceful as ever."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
            
            jump allcompetition1_round3
            
        "{image=GUI/Dance/Dance - FourChoice2B.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition1_round2
            
label allcompetition1_round3:
 
    stop music
    
    show arrowright at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowleft at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
      
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowright at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    hide arrowright with dissolve
    
    show arrowleft at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup with dissolve
      
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FourChoice3A.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "You're doing great!"
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Chael":
                cb "You're doing very well, Princess."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
            
            jump allcompetition1_round4
            
        "{image=GUI/Dance/Dance - FourChoice3B.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition1_round3
            
label allcompetition1_round4:
    
    stop music
    
    show arrowdown at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
      
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    hide arrowright with dissolve
      
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FourChoice4A.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition1_round4
            
        "{image=GUI/Dance/Dance - FourChoice4B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That's the way to do it!"
                show dancezuleika normal at left
                show duren at right
                zb "On to the next one."
                
            elif partner == "Chael":
                cb "Well done, Princess."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
            
            jump allcompetition1_round5
            
label allcompetition1_round5:
 
    stop music
    
    show arrowup at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
      
    show arrowleft at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowup at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    hide arrowright with dissolve
      
    show arrowleft at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - FourChoice5A.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That was fantastic, Zuleika."
                
            elif partner == "Chael":
                cb "Wonderful, as expected from you."
                
            jump allcompetition1win
            
        "{image=GUI/Dance/Dance - FourChoice5B.png}":
            $ miss += 1
            
            if partner == "Duren":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show duren sad at right
                zb "Oops, sorry, Duren. I missed a few steps there..."
                
                show duren at right
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition1_round5
            
label allcompetition1win:
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
            
        elif partner == "Chael":
            $ CAffection += 10
        
    elif miss < 3:
        show vgirlf happy
        an "Congratulations on winning Second Place in the first round!\nYour prize is 100 Gold!"
        $ gold += 100
        
        if partner == "Duren":
            $ DAffection += 5
            
        elif partner == "Chael":
            $ CAffection += 5
        
    else:
        show vgirlf sad
        an "Ouch, sorry that you lost..."
        an "Better luck next time."
    
    show vgirlf normal    
    an "That's all for today, but don't forget that the competition is being held across the nation, so you can compete in any town."
    an "Good luck!"
    
    $ dancing_skill += 50
    $ competition1_done = True
    stop music
    hide vgirlf
    jump alljarconia_choice
            
label alljarconiainn1:
    stop music
    scene bg inn sunset with fade
    
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    show wlzuleika normal hidden
    z "Whew, I'm really beat. Time to get some rest. "
    show wlzuleika sad hidden
    z "But it doesn't look like Chael is here yet, and there's still a bit of light outside... "
    show wlzuleika normal hidden
    z "Perhaps I'll get out of the city for a bit, then. I'm not used to such crowded places; the fresh air may do me some good. "
    
    scene bg faraway village
    with fade
    
    "The city looked so much more beautiful from afar, and the mountains were beautiful, too. I was glad that I decided to come out here. "
    show kirile sad2 with dissolve
    play music "Audio/Music/Dissappointment (Sad Kirile Theme).ogg"
    "But that's when I saw him...a depressed-looking man staring off into the sunset. "
    
    show wzuleika normal hidden
    z "(Those wings...he must be an angel, too, but it seems strange for there to be another one here.)"
    show wzuleika sad hidden
    z "Um...excuse me, but is something wrong? "
    
    dm "Just a little homesick, is all. Nothin' a lass like you needs to worry about. "
    
    show wzuleika angry hidden
    z "Why don’t you just go home, then? "
    z "Judging from your appearance, you're from Pyralis, right? You’re practically already there. "
    
    dm "I...can't go home. I can never go back there as long as I live. "

    "I waited for him to go on, but he stood there in silence, refusing to face me. "
    
    show wzuleika sad hidden
    z "Want to talk about it? I'm a good listener. "
    
    show kirile sad
    "The man finally turned around to face me, and I immediately noticed the dark scar across his eye and the black eye patch that tried to conceal the damage. "
    "He must have noticed my look because he pointed to it. "
    show kirile angry
    dm "When I lost my eye, I lost my pride as a warrior; I went from being the undefeated champion of my nation, to being some sort of cripple…a disgrace to my kingdom, and more importantly, a disgrace to my queen. "
    show kirile sad
    dm "When she discharged me from the very military I had devoted my life to, it was the same as condemning me to death…I have nothing left, there or anywhere."
    
    menu:
        "\"That's so sad...\"":
            show wzuleika sad hidden
            z "I can't believe your own creator would do something like that to you. That's horrible..."
            dm "Tell me about it..."
            dm "I don't know what to do anymore."
            show wzuleika normal hidden
            z "Well, I'm sure you'll figure out something. I believe in you!"
            show kirile
            dm "Thanks, lass. I'll keep that in mind."
            
            stop music
            scene bg black with fade
            with Pause(.5)
            
            if zuleika_type == 'all' or zuleika_type == 'intelligent':
                jump alljarconiainn2A
            else:
                jump alljarconiainn2B
            
        "\"Get a hold of yourself!\"":
            $ KAffection += 20
            show wzuleika angry hidden
            z "It truly is horrible what happened to you, but you're not a cripple, and your life isn't over. "
            z "I've seen soldiers who lost arms and legs, and still kept on fighting. So what if you lost an eye? You just have to learn to see better with the other to make up for it. "
            z "And so what if you were cast out of your kingdom? You just have to find a new home for yourself. "
            show wzuleika normal hidden
            z "It won't be easy, but if you were strong enough to win all those battles, I bet you're strong enough to keep fighting. "
    
            "The black-clad angel stared at me, frowning, for several moments. "
            stop music
            show kirile with dissolve
            play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
            "Then, slowly but surely, a smile spread across his face. "
    
            dm "Thank you for putting my head back on straight. "
            show kirile happy
            dm "You're right, this is no time to mope around feeling sorry. I just need to get out there and make something of myself - that'll show 'em! "
            
            show kirile
    
            "His smile was contagious, and before long, I found myself smiling back and cheering him on. "
            "I soon realized, however, that it was getting late, and I knew Chael was probably waiting for me back at the inn. "
    
            show wzuleika normal hidden
            z "I'm glad to see that you're feeling better, but I have to get back to the city before it gets too dark, or else I'll never find my way there. "
            z "Good luck! "
    
            show kirile happy
            dm "Thanks. You too! "
    
            "I laughed and waved good-bye to the odd, but friendly man, then headed back to the inn. "
            stop music
            scene bg black with fade
            with Pause(.5)
            
            if zuleika_type == 'all' or zuleika_type == 'intelligent':
                jump alljarconiainn2A
            else:
                jump alljarconiainn2B
    
label alljarconiainn2A:
        scene bg inn night
        play sound "Audio/Sound/Nighttime.ogg"
        with fade
        
        show lchael with dissolve
        
        show wlzuleika normal hidden
        z "So, Chael, how was your day? "
        
        c "It was...fine. And yours? "
        
        show wlzuleika happy hidden
        z "It was great! I did all sorts of things today. "
        show wlzuleika normal hidden
        z "I was surprised to find some interesting books on Nalan at the library. "
        z "It sounds like a really beautiful place. "
        
        stop sound
        show lchael angry
        c "...Is that all you have to say about it? "
        
        show wlzuleika sad hidden
        z "What do you mean by that? "
        
        show lchael sad
        play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
        c "Nothing...I suppose I'm just used to people being frightened by it. "
        c "They fear what they do not understand...and my world is one thing most people could never comprehend. "
        
        menu:
            "\"That's because it's so...weird.\"":
                show lchael angry
                c "Hmph. "
                c "We have a long day ahead of us tomorrow. Get some rest. "
                
                jump allkirilemeeting
        
            "\"I'm not afraid.\"":
                show lchael
                $ CAffection += 20
                z "It's a different culture from what I'm used to, yes, but that doesn't mean that it's frightening. "
                show wlzuleika normal hidden
                z "I think it's quite intriguing, really. "
               
                show lchael happy
                c "Well, I'm glad that you're so open-minded, Princess, though I'm not surprised. You look as if you have some Nalani blood yourself. "
        
                c "I can tell you more about Nalan sometime, if you would like. "
        
                show wlzuleika happy hidden
                z "I would love that. "
        
                jump allkirilemeeting
                
label alljarconiainn2B:
    scene bg inn night
    play sound "Audio/Sound/Nighttime.ogg"
    with fade
    
    show wlzuleika normal hidden
    z "Now it's {i}really{/i} time for bed. "
    z "It'll be nice to sleep in an actual bed after sleeping on the ground for the past few weeks. "
    z "I'm sure I'll get used to this traveling thing eventually, but I'm definitely not used to it yet. "
    
    stop sound
    scene bg black with fade
    with Pause(.5)
        
label allkirilemeeting:
    scene bg jarconia 
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    with fade
    
    "The next morning, we set out to leave. "
    "However, before we could get very far, I heard a familiar voice calling after us. "
    
    play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
    
    dm "Oi! Wait up! "
    show lkirile with dissolve
    
    show wlzuleika normal hidden
    z "Hey, what are you doing here? "
    z "I thought you were going to go out and \"make something of yourself.\" "
    
    show lkirile happy
    dm "I am, with you. "
    
    show wlzuleika angry hidden
    z "...Excuse me? "
    
    show lkirile
    dm "You seem like a good lass, someone who'll accomplish great things. "
    dm "I wanna help lift you up and be there when you do. I can be your bodyguard or something... "
    show lkirile sad
    "He gestured towards my frowning companion. "
    dm "…unless the position is already taken up by {i}that{/i} one. "
    
    menu:
        "\"Sure, you can join us.\"":
            $ KAffection += 20
            show lkirile happy
            dm "That’s great! I won’t let you down, I promise. "
            
            show lkirile
            "He bowed at the waist and introduced himself. "
            k "The name is Kirile the Powerful, at your service. "
            
            "The name struck me immediately; he was the prince of Pyralis, known for his incredible strength and cheerful smile. "
            "Could it be coincidence that the angels of the three Great Nations have been brought together like this? "
            "No...it had to be fate. "
            
            show wlzuleika normal hidden
            z "I'm Zuleika, and this is my friend, Chael. "
            
            show lkirile happy
            
            k "Well, Zuleika, I'm glad I met you. I've got a good feeling about this. "
            
            z "Me, too. "    
            
        "\"Sorry, I already have a bodyguard.\"":
            $ CAffection += 20
            show lkirile
            "My subtle refusal didn't seem to faze the young man; he was determined to join us no matter what. "
            
            dm "Well, I'll be your cook, then. "
            
            show wlzuleika sad hidden
            z "He does the cooking, too. So, you see, there's really no need for you to - "
            
            dm "Then I can be your navigator. "
            dm "I've traveled around this area quite a bit in my lifetime and I know where all the best places are. "
            
            z "That's really not neccessary. We'll be - "
            
            show lkirile happy
            
            dm "Oh, I know! I'll be your entertainer! "
            dm "Whenever you need a laugh, I'll provide you with all the jokes you could ever need. It'll boost morale and keep you goin' through the tough times, and I'll even do it for free. "
            
            "With a sigh, I turned and started walking, the ever-serious Chael right beside me, and obviously not taking the hint, the black-clad angel followed close behind with a triumphant smile on his face. "
            "Thus, Kirile the Powerful became the newest member of our little group. "
            
    call status from _call_status_1

    $ kirile_in_party = True
           
    jump allchp3A