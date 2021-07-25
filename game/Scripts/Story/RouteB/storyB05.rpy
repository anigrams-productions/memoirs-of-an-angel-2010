# Story B
# Chapter 05: Having a Plan
label allchp5B:
    call status from _call_status_13

    $ show_button_game_menu = False
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    stop music
    
    scene bg castle hall with fade
    "Shortly after, Emperor Nefferon once again called me in to meet with him."
    scene bg throne with fade
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    show nef
    n "Thank you for meeting with me like this, Princess."
    n "I called you here to inform you that I've come up with the perfect plan to lure the Order here."
    show zuleika happy hidden
    z "You have? That's great!"
    show zuleika normal hidden
    z "What's the plan?"
    n "We're going to host a ball at the castle."
    show zuleika sad hidden
    z "...A {i}what{/i}?"
    n "A formal ball, as in a social event that involves dancing."
    show nef sad
    n "As a princess, I'd think you would be familiar with the term."
    z "I {i}am{/i} familiar with the term..."
    show nef
    n "Why the surprise, then?"
    z "That's just not the kind of master plan I had in mind. Couldn't you just call them in for a meeting or something?"
    show nef happy
    n "I could, but this way is much more fun, wouldn't you agree?"
    show nef
    z "...I guess..."
    n "The ball is scheduled for a week from today. You should take this time to prepare."
    hide nef with dissolve
    stop music
    z "(Speaking of preparing, what am I going to do about finding a dance partner?)"
    z "(I think I need some air...)"
    
    scene bg castle town with fade
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    "I decided to get out of the castle for a bit and head into town."
        
    if zuleika_type == 'all' or zuleika_type == 'charming':
        $ competition6_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament8_done = False
    
label allcastletown_choice2:
    if energy == 0:
        jump allcastle5
        
    else:
        scene bg castle town
        play music "Audio/Music/Thatched Villagers (Village).ogg"
        "What should I do?"
    
        menu:
            "Visit the Shop":
                jump allshop_menu3
            "Go to the Library":
                jump alllibrary_menu3
            "Practice at the Training Hall":
                jump alltraining_menu3
            "Volunteer at the Church":
                jump allchurch_menu3
            "Enter Martial Arts Tournament" if zuleika_type == 'all' and tournament8_done == False or zuleika_type == 'strong' and tournament8_done == False:
                jump alltournament8
            "Enter Dancing Competition" if zuleika_type == 'all' and competition6_done == False or zuleika_type == 'charming' and competition6_done == False:
                jump allcompetition6
            "Return to the Castle":
                stop music
                jump allcastle5
            
label allshop_menu3:
    $ location = 'allshop3'
    scene bg shop
    play music "Audio/Music/Nothing Broken (Shop).ogg"
    show vgirla normal with dissolve
    
    s "Hello! How may I help you today?"

    menu:
        "Buy":
            s "You have %(gold)d Gold remaining. What would you like to buy?"
            jump allbuy_menu3
        "Work as a sales clerk":
            hide vgirla
            show zuleika normal hidden
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
            jump allcastletown_choice2
        "Return to town":
            stop music
            jump allcastletown_choice2
            
label allbuy_menu3:
    show vgirla normal
    menu:
        "\"A Gift of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'intelligent' or zuleika_type == 'strong' or zuleika_type == 'charming':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "No":
                    jump allbuy_menu3
        "\"A Bouquet of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "Buy as a gift":
                    $ gold -= 15
                    $ item_bouquet += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "Don't buy":
                    jump allbuy_menu3
        "\"Penniless Princess' Travel Kit\" - 45 Gold":
            s "Ah, what a great item! After all, young beauties like ourselves need to look good, even on the go. "
            if gold < 45:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "Buy as a gift":
                        $ gold -= 45
                        $ item_makeup += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "Don't buy":
                        jump allbuy_menu3
            else:
                menu:
                    "Yes":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "No":
                        jump allbuy_menu3
        "\"Miraculous Moonshine\" - 50 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Let go and enjoy yourself with this intoxicating drink. Just don't go overboard."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 50
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "Buy as a gift":
                    $ gold -= 50
                    $ item_liquor += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "Don't buy":
                    jump allbuy_menu3
        "\"Secret Stealth Knives\" - 80 Gold":
            s "When you're in a pinch, it helps to have something to defend yourself with. Oh, but please, don't use them in the store. "
            if gold < 80:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "Buy as a gift":
                        $ gold -= 80
                        $ item_knives += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "Don't buy":
                        jump allbuy_menu3
            else:
                menu:
                    "Yes":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "No":
                        jump allbuy_menu3
        "\"Sinister Spellbook for Beginners\" - 100 Gold":
            s "Excellent choice! I just hope you don't plan to use any of those spells on me... "
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "Buy as a gift":
                        $ gold -= 100
                        $ item_spellbook += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "Don't buy":
                        jump allbuy_menu3
            else:
                menu:
                    "Yes":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu3
                    "No":
                        jump allbuy_menu3
        "\"Elegant Earrings\" - 150 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Adorning yourself with jewelry has long been a way to show off your wealth...er...I mean...make yourself look pretty."
            if gold < 150:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 150
                    $ increase_charm(25)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "Buy as a gift":
                    $ gold -= 150
                    $ item_earrings += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "Don't buy":
                    jump allbuy_menu3
        "\"Pristine Princess Potion\" (Charm Booster) - 500 Gold":
            s "Even the gaudiest pauper can look like a beautiful princess with this potion. Then again, I guess you're already a princess..."
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_charm(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "No":
                    jump allbuy_menu3
        "\"Potent Puissance Potion (Strength Booster)\" - 500 Gold":
            s "Bulking up, huh? You know, too much of that will give you wrinkles. Not that that should stop you, of course... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_strength(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "No":
                    jump allbuy_menu3
        "\"Brain Boosting Book\" - 500 Gold":
            s "Supposedly, this stuff will make you smarter instantly. I wonder if I should try some... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_intelligence(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "No":
                    jump allbuy_menu3
        "\"Concentrated Compassion Concoction\" - 500 Gold":
            s "Aww, how kind of you...but wait, you didn't actually do anything! "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_kindness(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu3
                "No":
                    jump allbuy_menu3
        "\"Magical Map\" - 50 Gold":
            s "This is a basic world map with a few major cities marked (like this one). It may be useful if you want to know where you are."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
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
                    jump allbuy_menu3
                "No":
                    jump allbuy_menu3
        "\"Wondrous Wardrobe Modifier\" - 100 Gold":
            s "It's always fun to try on new, cool-looking outfits, isn't it?"
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu3
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 100
                    hide vgirla with dissolve
                    jump change_clothes
                "No":
                    jump allbuy_menu3
        "Nevermind":
            jump allshop_menu3
            
label alllibrary_menu3:
    scene bg library
    play music "Audio/Music/Comfortable Mystery 4 (Library).ogg"
    with fade
    show vgirle normal with dissolve
    l "Welcome to the Library, the center for useful information. "
    l "What would you like to do?"
    
    menu:
        "Do some research":
            hide vgirle
            if zuleika_type == 'strong':
                show zuleika normal hidden
                z "To prepare for the ball, I decided to find some books on dancing."
                show zuleika angry hidden
                z "...What are all of these little pictures supposed to mean? I don't get it."
            else:
                show zuleika sad hidden
                z "I'm really unprepared for this ball."
                show zuleika normal hidden
                z "But maybe these books on how to dance will help."
            $ increase_intelligence(25)
            $ energy -= 1
            stop music
            jump allcastletown_choice2
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
            jump allcastletown_choice2
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
            jump allcastletown_choice2
        "Return to town":
            stop music
            jump allcastletown_choice2
            
label alltraining_menu3: 
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
            jump allcastletown_choice2
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
            jump allcastletown_choice2
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
            jump allcastletown_choice2
        "Return to town":
            stop music
            jump allcastletown_choice2
            
label allchurch_menu3:
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
                z "The woman even gave me a nice reward for helping her: 50 Gold! "
                $ gold += 50
            $ increase_kindness(25)
            $ energy -= 1
            stop music
            jump allcastletown_choice2
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
            jump allcastletown_choice2
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
            jump allcastletown_choice2
        "Return to town":
            stop music
            jump allcastletown_choice2
            
label alltournament8:
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
            an "The final match will be..."
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSZuleika at left
            with moveinleft
            an "On this side, the former Princess Zuleika, fighting to save the kingdom and regain her honor,"
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSNefferon at right
            with moveinright
            an "and on this one, we have the one and only Emperor Nefferon, who refuses to give up his seat of power."
            an "Which of these legendary fighters will win? Let's find out!"
            
            hide VSNefferon with moveoutright
            hide VSZuleika with moveoutleft
            
            scene bg courtyard
            play music "Audio/Music/Dangerous (Boss Battle).ogg"
            
            show battlezuleika normal at left
            with dissolve
            
            show HPL at topleft
            with moveinleft
            
            zb "For the sake of my people, I must win this fight!"
            
            show nef at right
            with dissolve
            
            show HPR at topright
            with moveinright
            
            nb "I love that determined look in your eyes, little princess...I'm going to enjoy making you scream."
            
            jump alltournament8_choice
            
        "How to Play":
            an "New to the tournament? Don't worry, it's easy to play!"
            an "Each round, you are given three choices: Attack, Defend, or Forfeit."
            an "Attack means that you throw an offensive attack at your enemy, but be careful because they'll attack you back with the same amount of force!"
            an "Defend means that you let the enemy attack first, but they do much less damage than they normally would. Then you get a chance to counterattack, but with less power than a normal attack."
            an "Forfeit means quitting the battle. You're advised to do so if you're about to lose."
            an "The more battles you fight in the tournament, the more battle skill you'll gain, so make sure to enter at every opportunity!"
            
            jump alltournament8
            
        "Return to town":
            stop music
            jump allcastletown_choice2
            
label alltournament8_choice:
    menu:
        "Attack":
            show battlezuleika angry at left
            zb "Take this!"
            
            with flash
            
            if battle_skill > 99:
                $ zattack = renpy.random.randint(1,100)

                if zattack <= 5:
                    show nef happy at right
                    show battlezuleika sad at left
                    zb "Oh no! I missed!"

                elif zattack > 5 and zattack <= 35:
                    show nef sad at right
                    with sshake
                    $ EHP -= 15

                elif zattack > 35 and zattack <= 65:
                    show nef sad at right
                    with sshake
                    $ EHP -= 20

                elif zattack > 65 and zattack <= 85:
                    show nef sad at right
                    with sshake
                    $ EHP -= 25
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"

                else:
                    show nef sad at right
                    with sshake
                    $ EHP -= 30
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"
                    
            else:             
                if zattack <= 10:
                    show nef happy at right
                    show battlezuleika sad at left
                    zb "Oh no! I missed!"

                elif zattack > 10 and zattack <= 40:
                    show nef sad at right
                    with sshake
                    $ EHP -= 15

                elif zattack > 40 and zattack <= 90:
                    show nef sad at right
                    with sshake
                    $ EHP -= 20

                else:
                    show nef happy at right
                    show battlezuleika sad at left
                    zb "Crap, he blocked it!"
                
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPL
                hide HPR
                jump alltournament4win
                
            else:
                show battlezuleika normal at left
                show nef at right
                with Pause(1.5)
            
            show nef angry at right
            nb "That was pathetic!"
            
            with flash
            
            if battle_skill > 99:
                $ nattack = renpy.random.randint(1,100)

                if nattack <= 10:
                    show nef sad at right
                    show battlezuleika happy at left
                    nb "Crap, I missed..."

                elif nattack > 10 and nattack <= 60:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 15

                elif nattack > 60 and nattack <= 90:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 20

                else:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 25
                
                    zb "Oh no, it was a critical hit..."
            else:
                $ nattack = renpy.random.randint(1,100)

                if nattack <= 10:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 15

                elif nattack > 10 and nattack <= 30:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 20

                elif nattack > 30 and nattack <= 60:
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
                hide HPR
                hide HPL
                jump alltournament4lose
                
            else:
                show battlezuleika normal at left
                show nef at right
                
            jump alltournament8_choice
            
        "Defend":
            show battlezuleika angry at left
            
            zb "Go ahead, come at me."
            
            show nef angry at right
            nb "Gladly!"
            
            with flash
            
            if battle_skill > 99:
                $ nattack = renpy.random.randint(1,100)

                if nattack <= 10:
                    show nef sad at right
                    show battlezuleika happy at left
                    nb "Crap, I missed..."

                elif nattack > 10 and nattack <= 80:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 5

                else:
                    show battlezuleika sad at left
                    with sshake
                    $ ZHP -= 10
            else:
                $ nattack = renpy.random.randint(1,100)

                if nattack <= 10:
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
                hide HPR
                hide HPL
                jump alltournament4lose
            
            else:
                show battlezuleika normal at left
                show nef at right
                with Pause(1.5)
            
            show battlezuleika angry at left
            zb "Time to counter!"
            
            with flash
            
            $ zattack = renpy.random.randint(1,100)

            if zattack <= 35:
                show nef sad at right
                with sshake
                $ EHP -= 5

            else:
                show nef sad at right
                with sshake
                $ EHP -= 10
            
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPR
                hide HPL
                jump alltournament4win
                
            else:
                show battlezuleika normal at left
                show nef at right
                
            jump alltournament8_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    jump alltournament8
                "No":
                    jump alltournament8_choice
                    
label alltournament8win:
    stop music
    scene bg black with fade
    $ energy -= 1
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb happy with dissolve
    an "Congratulations on winning the final round!\nYour prize is 1000 Gold!"
    $ gold += 1000
    show vboyb normal
    an "Thank you for participating. We hope to see you again next year!"
    
    $ battle_skill += 50
    $ tournament8_done = True
    stop music
    hide vboyb
    jump allcastletown_choice2
    
label alltournament8lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament8
            
        "Return to town":
            jump allcastletown_choice2
            
label allcompetition6:
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
                    
                    an "The second dance will be..."
            
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
                    
                    jump allcompetition6_round1
                    
                "Nefferon":
                    $ partner = "Nefferon"
                    $ NAffection += 5
                    
                    stop music
                    scene bg black with fade
                    with Pause(.5)
                    
                    scene bg dancehall with fade
                    
                    an "The second dance will be..."
            
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
                    
                    jump allcompetition6_round1
                    
        "How to Play":
            an "New to the competiton? Don't worry, it's easy to play!"
            an "First, choose a partner. When you dance (and succeed) with a boy, you'll earn affection with him, so choose your partner wisely."
            an "Second, watch the step pattern that appears on the screen and try to memorize it."
            an "Finally, put your memory to the test and choose the correct combination from the choices given."
            an "If you get it right, you'll move on to the next round. If you get it wrong, you'll have to do it over again."
            an "Reach the end with as few wrong answers as possible to win!"
            
            jump allcompetition6
                    
        "Return to town":
            stop music
            jump allcastletown_choice2
            
label allcompetition6_round1:
    stop music

    show arrowup at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
      
    show arrowdown at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowup at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowup at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowright at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
      
    show arrowdown at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowup at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SixChoice1A.png}":
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
            
            jump allcompetition6_round1
            
        "{image=GUI/Dance/Dance - SixChoice1B.png}":
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
                nb "Well done, Princess"
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition6_round2
            
label allcompetition6_round2:
    stop music

    show arrowdown at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
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
    
    show arrowright at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
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
    
    show arrowright at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SixChoice2A.png}":
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
            
            jump allcompetition6_round3
            
        "{image=GUI/Dance/Dance - SixChoice2B.png}":
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
            
            jump allcompetition6_round2
            
label allcompetition6_round3:
    stop music

    show arrowleft at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
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
    
    show arrowright at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowleft at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowright at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SixChoice3A.png}":
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
            
            jump allcompetition6_round3
            
        "{image=GUI/Dance/Dance - SixChoice3B.png}":
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
            
            jump allcompetition6_round4
            
label allcompetition6_round4:
    stop music

    show arrowdown at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
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
    hide arrowleft with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
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

    hide arrowleft with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SixChoice4A.png}":
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
                nb "Well done, Princess"
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition6_round5
            
        "{image=GUI/Dance/Dance - SixChoice4B.png}":
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
            
            jump allcompetition6_round4
            
label allcompetition6_round5:
    stop music

    show arrowup at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
      
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowup at Position(xpos = 185, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 257, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 329, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
      
    show arrowright at Position(xpos = 401, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 473, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowdown at Position(xpos=545, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SixChoice5A.png}":
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
                            
            jump allcompetition6win
            
        "{image=GUI/Dance/Dance - SixChoice5B.png}":
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
            
            jump allcompetition6_round5
            
label allcompetition6win:
    scene bg black with fade
    $ energy -= 1
    
    scene bg dancehall with fade
    show vgirlf normal with dissolve
        
    if miss == 0:
        show vgirlf happy
        an "Congratulations on winning First Place in the second round!\nYour prize is 500 Gold!"
        $ gold += 500

        if partner == "Duren":
            $ DAffection += 10
            
        elif partner == "Nefferon":
            $ NAffection += 10
        
    elif miss < 3:
        show vgirlf happy
        an "Congratulations on winning Second Place in the third round!\nYour prize is 250 Gold!"
        $ gold += 250
        
        if partner == "Duren":
            $ DAffection += 5
            
        elif partner == "Nefferon":
            $ NAffection += 5
        
    else:
        show vgirlf sad
        an "Ouch, sorry that you lost..."
        an "Better luck next time."
    
    show vgirlf normal
    an "Thank you for participating. We hope to see you again next year!"
    
    $ dancing_skill += 50
    $ competition6_done = True
    stop music
    hide vgirlf
    jump allcastletown_choice2
            
label allcastle5:
    if CAffection > max(KAffection, DAffection, NAffection):
        scene bg castle town
        show vboye nervous with dissolve
        m "Wait, before you go, this message came for you."
        show zuleika sad hidden
        z "A message?"
        hide vboye
        scene bg black with fade
        play music "Audio/Music/Dreamy Flashback.ogg"
        "\"Dear Princess Zuleika...\""
        "\"You may not know of me, for I hail from the mysterious land of Nalan, but I have heard many stories of you...\""
        "\"...and I must confess that I have fallen in love with you from afar.\""
        "\"If you are as kind and gracious as the stories tell, then please allow me the honor of escorting you to your royal ball.\""
        "\"I'll meet you in your room on the night of the ball. Please wait for me.\""
        show zuleika sad hidden
        z "What an odd letter..."
        show zuleika happy hidden
        z "It's kind of romantic, though. I think I'll take him up on his offer."
        $ ball = "Chael"
        $ CAffection += 600
        stop music
        jump allchp6B
    elif KAffection > max(CAffection, DAffection, NAffection):
        scene bg castle town
        show vboye nervous with dissolve
        m "Wait, before you go, this message came for you."
        show zuleika sad hidden
        z "A message?"
        hide vboye
        scene bg black with fade
        play music "Audio/Music/Dreamy Flashback.ogg"
        "\"Dear Princess Zuleika...\""
        "\"You may not know me, since I come from the distant land of Pyralis, but I've heard so much about you...\""
        "\"...and I have to admit that I think I love you.\""
        "\"If you are as cool as the stories say you are, then please let me take you to your royal ball.\""
        "\"I'll meet you in your room on the night of the ball. Wait for me.\""
        show zuleika sad hidden
        z "What an odd letter..."
        show zuleika happy hidden
        z "It's kind of romantic, though. I think I'll take him up on his offer."
        $ KAffection += 600
        $ ball = "Kirile"
        stop music
        jump allchp6B 
        
    elif DAffection > max(CAffection, KAffection, NAffection):
        stop music
        scene bg castle hallway with fade
        "When I returned to the castle, I found Duren waiting for me."
        play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
        show duren
        show zuleika normal hidden
        z "Hey, Duren."
        show zuleika sad hidden
        z "I'm assuming you heard about the ball?"
        d "I did. That's...actually what I wanted to talk to you about."
        show zuleika happyblush hidden
        z "Oh Duren, I'd love to!"
        show duren sad
        d "Er...love to what?"
        show zuleika sadblush hidden
        z "Um...nevermind."
        z "What is that you were going to say?"
        show duren
        d "Well, I was thinking that this would be a perfect opportunity to take Nefferon out."
        show zuleika sad hidden
        z "Oh...right, of course."
        d "Since he'll be busy with the guests, it'll be the perfect time to round up the Royal Guard."
        d "Once we have the ballroom surrounded, I'll need you to distract him...and give him this."
        "He handed me a small, liquid-filled bottle."
        show zuleika angry hidden
        z "Is this...poison?"
        d "It won't kill him; it'll just knock him out long enough for us to arrest him."
        show duren happy
        d "I'm counting on you, Zuleika."
        "I nodded silently, a bit dissappointed."
        show duren sad
        d "Oh, and...um..."
        show zuleika normal hidden
        z "...Yes?"
        d "I...have something important to ask you."
        show duren blush
        "We looked into each other’s eyes, feeling the familiar bond that had been between us since childhood, a bond that was now stronger than ever."

        show duren happyblush
        "The young prince then took something out of his pocket: a small leather pouch."
        "It had a blue flower embroidered onto it, which I recognized to represent absolute loyalty, in this case to the prince."
        "I gasped as I realized what it meant."

        show duren blush
        "He kneeled on one knee as he presented it to me."
        d "Zuleika…I wish for nothing more than for you to stay by my side and for us to rule this nation together."
        d "Please, will you be my..."
        d "...royal adviser?"
        
        menu:
            "Accept":
                $ gift = "Satchel"
                $ persistent.giftsatchel = True
                $ DAffection += 50
                
                scene bg black with fade
                stop music
                "Received \"Embroidered Satchel\"."
                
                scene bg castle hallway with fade
                play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
                
                show duren blush with dissolve
                
                show zuleika happyblush hidden
                z "Of course…I accept." 
                show zuleika normalblush hidden
                z "It's truly beautiful. Thank you so much."
                show duren happyblush
                "I was surprised to see a smile spread across his face, and I smiled cheerfully in response."

                d "We'll make this nation great, I'm sure of it."
                d "With you by my side, we'll accomplish so much. We'll make this a place worth living again."

                show zuleika happyblush hidden
                z "That sounds really great, Duren, and I'm so happy that I'll get to be a part of it…that I'll get to make this nation great with you, together."
                
                show duren blush
                d "You'll go to the ball with me, too, won't you?"
                z "I would love to."
                $ ball = "Duren"
                $ ending = "Stay with Duren"
                stop music
                jump allchp6B

            "\"I'm sorry, but I can't.\"":
                show zuleika sad hidden
                z "I wish you the best of luck with everything, but I'm afraid I can't stay here to help you."
                show duren sad

                d "Why not?"
                show zuleika normal hidden
                z "This may sound silly, but…when that assassin came, he gave me the option to leave here, to start a new life and to help rebuild the kingdom with my own two hands."
                z "Ever since then, I haven't been able to get the idea out of my head…and this is my opportunity to finally get out of here and start over."

                "He looked at me intently for a moment."
                show duren
                d "I understand."
                d "If that is your wish, Zuleika, then so be it; I won't stop you."

                z "Thank you, Duren."
                
                d "Will you still go to the ball with me, for old times' sake?"
                show zuleika happy hidden
                z "Of course! That's what friends are for."
                
                $ ball = "Duren"
                $ ending = "Leave"
                stop music
                jump allchp6B
                
    elif NAffection > max(CAffection, KAffection, DAffection):
        stop music
        scene bg castle hallway with fade
        "When I returned to the castle, I found Nefferon waiting for me."
        play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
        show nef
        n "Ah, there you are, Princess."
        n "I have something I wish to...discuss with you."
        show zuleika normal hidden
        z "Yes?"
        n "I would be...honored if you would attend the ball with me."
        show zuleika happyblush hidden
        z "Really?"
        show zuleika normalblush hidden
        z "I would love to, Your Majesty."
        $ NAffection += 50
        show nef happy
        n "Please, Zuleika, when we're alone, feel free to call me by name. You have earned that right."
        z "Very well...Nefferon."
        stop music
        $ ball = "Nefferon"
        jump allchp6B