# Story A
# Chapter 06: Destination
label allchp7A:
    call status from _call_status_7

    $ show_button_game_menu = False
    
    scene bg duggary with fade
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    "When we finally arrived at our destination, we were surprisingly welcome...well, in comparison."
    "Rather than the hostility offered to us at other villages, we were instead met with mere indifference."
    "What could have changed? Did Nefferon finally pull his forces out of the area?"
    
    show vgirlc nervous with dissolve
    
    w "Um...excuse me. Are you Princess Zuleika?"
    show wlzuleika sad hidden
    z "No, I'm - "
    
    show vgirlc nervous at right with move
    
    show lchael 2 at left with dissolve
    
    c "Yes, she is."
    
    show wlzuleika angry hidden
    z "Chael!"
    show lchael angry2 at left
    c "It's alright, Princess...I can tell that she means us no harm."
    show lchael 2 at left
    
    show vgirlc sad at right
    w "I have a message for you...from His Majesty, the Emperor."
    show wlzuleika sad hidden
    z "A message?"
    
    scene bg black with fade
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    "\"It's been a while, hasn't it, Princess?\nThe castle has been quite lonely without you.\""
    "\"For whatever it was that caused you to leave, I would like to make amends.\""
    "\"I am holding a royal ball at the castle in one month's time.\""
    "\"I would be truly honored if the beautiful princess would make an appearance.\""
    "\"...We'll be awaiting your arrival, Princess.\""
    stop music
    
    scene bg duggary with fade
    play music "Audio/Music/News of Sorrow (Battle with Duren).ogg"
    
    show lchael angry2 at left
    show lkirile at right
    with dissolve
    c "Hmm...this sounds like a trap."
    k "Maybe so, but this could also be a perfect opportunity."
    
    show wlzuleika sad hidden
    z "A perfect opportunity for what exactly?"
    c "Princess...over the last few months, we've seen first-hand what has happened to your nation as a result of that man's rule."
    c "If you truly care for your people as much as I believe you do, then I'm afraid there's only one way to help them..."
    show lkirile sad at right
    k "...We have to dethrone him."
    z "You guys...you would actually be willing to do something like that? This isn't even your nation..."
    
    show lkirile at right
    show lchael 2 at left
    c "Through our travels with you, Princess, this land has become like a second home to us."
    k "That's right, and we want to see it thrive, not crumble under the rule of a crazy monarch."
    show lkirile sad at right
    k "We all know what happened last time we failed to act in a case like this...there's no way we could all withstand another continental war."
    
    z "...I need to think about this for a while."
    z "I'll meet up with you guys later..."
    
    show lchael angry2 at left
    c "Very well, Princess. Do what you need to do."
    
    hide lchael
    hide lkirile
    stop music
    
    z "In my heart, I guess I always knew it would come to this...I just hoped that I would be able to spend a bit more time with my friends first."
    show wlzuleika normal hidden
    z "I'll wander around town a bit to clear my head and think about it later, after I've had some time to relax."
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        $ competition3_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament3_done = False
        
label allduggary_choice:
    scene bg duggary
    play music "Audio/Music/Thatched Villagers (Village).ogg"
    
    if energy == 0:
        jump allduggaryinn1
        
    else:
        "What should I do?"
    
        menu:
            "Visit the Shop":
                jump allshop_menu5
            "Go to the Library":
                jump alllibrary_menu5
            "Practice at the Training Hall":
                jump alltraining_menu5
            "Volunteer at the Church":
                jump allchurch_menu5
            "Enter Martial Arts Tournament" if zuleika_type == 'all' and tournament3_done == False or zuleika_type == 'strong' and tournament3_done == False:
                jump alltournament3
            "Enter Dancing Competition" if zuleika_type == 'all' and competition3_done == False or zuleika_type == 'charming' and competition3_done == False:
                jump allcompetition3
            "Rest at the Inn":
                stop music
                jump allduggaryinn1
            
label allshop_menu5:
    $ location = 'allshop5'
    scene bg shop
    play music "Audio/Music/Nothing Broken (Shop).ogg"
    with fade
    show vgirla normal with dissolve
    
    s "Hello! How may I help you today?"

    menu:
        "Buy":
            s "You have %(gold)d Gold remaining. What would you like to buy?"
            jump allbuy_menu5
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
            jump allduggary_choice
        "Return to town":
            stop music
            jump allduggary_choice
            
label allbuy_menu5:
    show vgirla normal
    menu:
        "\"A Gift of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'intelligent' or zuleika_type == 'strong' or zuleika_type == 'charming':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "No":
                    jump allbuy_menu5
        "\"A Bouquet of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "Buy as a gift":
                    $ gold -= 15
                    $ item_bouquet += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "Don't buy":
                    jump allbuy_menu5
        "\"Penniless Princess' Travel Kit\" - 45 Gold":
            s "Ah, what a great item! After all, young beauties like ourselves need to look good, even on the go. "
            if gold < 45:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "Buy as a gift":
                        $ gold -= 45
                        $ item_makeup += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "Don't buy":
                        jump allbuy_menu5
            else:
                menu:
                    "Yes":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "No":
                        jump allbuy_menu5
        "\"Miraculous Moonshine\" - 50 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Let go and enjoy yourself with this intoxicating drink. Just don't go overboard."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 50
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "Buy as a gift":
                    $ gold -= 50
                    $ item_liquor += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "Don't buy":
                    jump allbuy_menu5
        "\"Secret Stealth Knives\" - 80 Gold":
            s "When you're in a pinch, it helps to have something to defend yourself with. Oh, but please, don't use them in the store. "
            if gold < 80:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "Buy as a gift":
                        $ gold -= 80
                        $ item_knives += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "Don't buy":
                        jump allbuy_menu5
            else:
                menu:
                    "Yes":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "No":
                        jump allbuy_menu5
        "\"Sinister Spellbook for Beginners\" - 100 Gold":
            s "Excellent choice! I just hope you don't plan to use any of those spells on me... "
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "Buy as a gift":
                        $ gold -= 100
                        $ item_spellbook += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "Don't buy":
                        jump allbuy_menu5
            else:
                menu:
                    "Yes":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu5
                    "No":
                        jump allbuy_menu5
        "\"Elegant Earrings\" - 150 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Adorning yourself with jewelry has long been a way to show off your wealth...er...I mean...make yourself look pretty."
            if gold < 150:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 150
                    $ increase_charm(25)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "Buy as a gift":
                    $ gold -= 150
                    $ item_earrings += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "Don't buy":
                    jump allbuy_menu5
        "\"Pristine Princess Potion\" (Charm Booster) - 500 Gold":
            s "Even the gaudiest pauper can look like a beautiful princess with this potion. Speaking of which, has anyone ever told you that you look just like Princess Zuleika?"
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_charm(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "No":
                    jump allbuy_menu5
        "\"Potent Puissance Potion (Strength Booster)\" - 500 Gold":
            s "Bulking up, huh? You know, too much of that will give you wrinkles. Not that that should stop you, of course... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_strength(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "No":
                    jump allbuy_menu5
        "\"Brain Boosting Book\" - 500 Gold":
            s "Supposedly, this stuff will make you smarter instantly. I wonder if I should try some... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_intelligence(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "No":
                    jump allbuy_menu5
        "\"Concentrated Compassion Concoction\" - 500 Gold":
            s "Aww, how kind of you...but wait, you didn't actually do anything! "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_kindness(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu5
                "No":
                    jump allbuy_menu5
        "\"Magical Map\" - 50 Gold":
            s "This is a basic world map with a few major cities marked (like this one). It may be useful if you want to know where you are."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
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
                    z "I'm currently in a large city by the sea."
                    scene bg shop with fade
                    show vgirla normal
                    s "You now have %(gold)d Gold."
                    jump allbuy_menu5
                "No":
                    jump allbuy_menu5
        "\"Wondrous Wardrobe Modifier\" - 100 Gold":
            s "It's always fun to try on new, cool-looking outfits, isn't it?"
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu5
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 100
                    hide vgirla with dissolve
                    jump change_clothes
                "No":
                    jump allbuy_menu5
        "Nevermind":
            jump allshop_menu5
            
label alllibrary_menu5:
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
                show wlzuleika normal hidden
                z "To prepare for the ball, I decided to find some books on dancing."
                show wlzuleika angry hidden
                z "...What are all of these little pictures supposed to mean? I don't get it."
            else:
                show wlzuleika sad hidden
                z "I'm really unprepared for this ball."
                show wlzuleika normal hidden
                z "But maybe these books on how to dance will help."
            $ increase_intelligence(25)
            $ energy -= 1
            stop music
            jump allduggary_choice
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
            jump allduggary_choice
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
            jump allduggary_choice
        "Return to town":
            stop music
            jump allduggary_choice
            
label alltraining_menu5: 
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
            jump allduggary_choice
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
            jump allduggary_choice
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
            jump allduggary_choice
        "Return to town":
            stop music
            jump allduggary_choice
            
label allchurch_menu5:
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
                z "The woman even gave me a nice reward for helping her: 50 Gold! "
                $ gold += 50
            $ increase_kindness(25)
            $ energy -= 1
            stop music
            jump allduggary_choice
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
            jump allduggary_choice
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
            jump allduggary_choice
        "Return to town":
            stop music
            jump allduggary_choice
            
label alltournament3:
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
            an "The third match will be..."
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSZuleika at left
            with moveinleft
            an "On this side, the former Princess Zuleika, known for her courage and conquests in battle,"
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSChael at right
            with moveinright
            an "and on this one, we have Prince Chael of Nalan, known far and wide for his incredible speed and deadly accuracy."
            an "Which of these legendary fighters will win? Let's find out!"
            
            hide VSChael with moveoutright
            hide VSZuleika with moveoutleft
            
            scene bg courtyard
            play music "Audio/Music/Exotic Battle (Tournament - Chael).ogg"
            
            show battlezuleika normal at left
            with dissolve
            
            show HPL at topleft
            with moveinleft
            
            zb "This is it! I can't back down now."
            
            show chael at right
            with dissolve
            
            show HPR at topright
            with moveinright
            
            cb "I would prefer not to take up arms against one such as you, but if I must, then so be it."
            
            jump alltournament3_choice
            
        "Return to town":
            stop music
            jump allduggary_choice
            
label alltournament3_choice:
    menu:
        "Attack":
            show battlezuleika angry at left
            zb "Take this!"
            
            with flash
            
            if battle_skill > 49:
                $ zattack = renpy.random.randint(1,100)

                if zattack <= 35:
                    show chael sad at right
                    with sshake
                    $ EHP -= 15

                elif zattack > 35 and zattack <= 65:
                    show chael sad at right
                    with sshake
                    $ EHP -= 20

                elif zattack > 65 and zattack <= 85:
                    show chael sad at right
                    with sshake
                    $ EHP -= 25
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"

                else:
                    show chael sad at right
                    with sshake
                    $ EHP -= 30
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"
                    
            else:
                $ zattack = renpy.random.randint(1,100)

                if zattack <= 5:
                    show chael happy at right
                    show battlezuleika sad at left
                    zb "Oh no! I missed!"

                elif zattack > 5 and zattack <= 35:
                    show chael sad at right
                    with sshake
                    $ EHP -= 15

                elif zattack > 35 and zattack <= 65:
                    show chael sad at right
                    with sshake
                    $ EHP -= 20

                elif zattack > 65 and zattack <= 85:
                    show chael sad at right
                    with sshake
                    $ EHP -= 25
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"

                else:
                    show chael sad at right
                    with sshake
                    $ EHP -= 30
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"
                
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPL
                hide HPR
                jump alltournament3win
                
            else:
                show battlezuleika normal at left
                show chael at right
                with Pause(1.5)
            
            show chael angry at right
            cb "What a bother..."
            
            with flash
            
            $ cattack = renpy.random.randint(1,100)

            if cattack <= 5:
                show chael sad at right
                show battlezuleika happy at left
                cb "Crap, I missed..."

            elif cattack > 5 and cattack <= 45:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 15

            elif cattack > 45 and cattack <= 70:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 20

            elif cattack > 70 and cattack <= 85:
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
                jump alltournament3lose
                
            else:
                show battlezuleika normal at left
                show chael at right
                
            jump alltournament3_choice
            
        "Defend":
            show battlezuleika angry at left
            
            zb "Go ahead, come at me."
            
            show chael angry at right
            cb "As you wish, Princess."
            
            with flash
            
            $ cattack = renpy.random.randint(1,100)

            if cattack <= 30:
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
                jump alltournament3lose
            
            else:
                show battlezuleika normal at left
                show chael at right
                with Pause(1.5)
            
            show battlezuleika angry at left
            zb "Time to counter!"
            
            with flash
            
            $ zattack = renpy.random.randint(1,100)

            if zattack <= 35:
                show chael sad at right
                with sshake
                $ EHP -= 5

            else:
                show chael sad at right
                with sshake
                $ EHP -= 10
            
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPR
                hide HPL
                jump alltournament3win
                
            else:
                show battlezuleika normal at left
                show chael at right
                
            jump alltournament3_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    jump alltournament3
                "No":
                    jump alltournament3_choice
                    
label alltournament3win:
    stop music
    scene bg black with fade
    $ energy -= 1
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb happy with dissolve
    an "Congratulations on winning the third round!\nYour prize is 1000 Gold!"
    $ gold += 1000
    show vboyb normal
    an "Thank you for participating. We hope to see you again next year!"
    
    $ battle_skill += 50
    $ tournament3_done = True
    stop music
    hide vboyb
    jump allduggary_choice
    
label alltournament3lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament3
            
        "Return to town":
            jump allduggary_choice
            
label allcompetition3:
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
                    
                    an "The third dance will be..."
            
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
                    
                    jump allcompetition3_round1
                    
                "Chael":
                    $ partner = "Chael"
                    $ CAffection += 5
                    
                    stop music
                    scene bg black with fade
                    with Pause(.5)
                    
                    scene bg dancehall with fade
                    
                    an "The third dance will be..."
            
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
                    
                    jump allcompetition3_round1
                    
                "Kirile":
                    $ partner = "Kirile"
                    $ KAffection += 5
                    
                    stop music
                    scene bg black with fade
                    with Pause(.5)
                    
                    scene bg dancehall with fade
                    
                    an "The third dance will be..."
            
                    play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
                    show VSBZuleika at left
                    with moveinleft
                    an "The former Princess Zuleika, known for her courage and golden tongue,"
            
                    play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
                    show VSKirile at right
                    with moveinright
                    an "dancing with the cheerful Prince Kirile of Pyralis!"
                    
                    hide VSKirile with moveoutright
                    hide VSBZuleika with moveoutleft
                    
                    scene bg dancehall
                                                    
                    show dancezuleika normal at left
                    with dissolve
                    
                    zb "Alright, let's do this!"
            
                    show kirile at right
                    with dissolve
                    
                    kb "Whatever happens, let's just have fun."
                    
                    show HP at top
                    with moveinleft
                    
                    jump allcompetition3_round1
                
                "Nefferon":
                    $ partner = "Nefferon"
                    $ NAffection += 5
                    
                    stop music
                    scene bg black with fade
                    with Pause(.5)
                    
                    scene bg dancehall with fade
                    
                    an "The third dance will be..."
            
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
                    
                    jump allcompetition3_round1
                    
        "How to Play":
            an "New to the competiton? Don't worry, it's easy to play!"
            an "First, choose a partner. When you dance (and succeed) with a boy, you'll earn affection with him, so choose your partner wisely."
            an "Second, watch the step pattern that appears on the screen and try to memorize it."
            an "Finally, put your memory to the test and choose the correct combination from the choices given."
            an "If you get it right, you'll move on to the next round. If you get it wrong, you'll have to do it over again."
            an "Reach the end with as few wrong answers as possible to win!"
            
            jump allcompetition3
                    
        "Return to town":
            stop music
            jump allduggary_choice
            
label allcompetition3_round1:
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
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            elif partner == "Kirile":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show kirile sad at right
                zb "Oops, sorry, Kirile. I missed a few steps there..."
                
                show kirile at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition3_round1
            
        "{image=GUI/Dance/Dance - SixChoice1B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
                
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
                
            elif partner == "Chael":
                cb "Well done, Princess."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
                
            elif partner == "Kirile":
                kb "That was great!"
                show dancezuleika normal at left
                show kirile at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "Well done, Princess"
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition3_round2
            
label allcompetition3_round2:
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
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
                
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
                
            elif partner == "Chael":
                cb "Your moves are as graceful as ever."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
                
            elif partner == "Kirile":
                kb "Yes, you're doing it!"
                show dancezuleika normal at left
                show kirile at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "Truly splendid."
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition3_round3
            
        "{image=GUI/Dance/Dance - SixChoice2B.png}":
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
                
            elif partner == "Kirile":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show kirile sad at right
                zb "Oops, sorry, Kirile. I missed a few steps there..."
                
                show kirile at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition3_round2
            
label allcompetition3_round3:
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
                
            elif partner == "Chael":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show chael sad at right
                zb "Oops, sorry, Chael. I missed a few steps there..."
                
                show chael at right
                
            elif partner == "Kirile":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show kirile sad at right
                zb "Oops, sorry, Kirile. I missed a few steps there..."
                
                show kirile at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition3_round3
            
        "{image=GUI/Dance/Dance - SixChoice3B.png}":
            play music "Audio/Music/Circus Waltz FX (Dancehall).ogg"
            
            if partner == "Duren":
                show dancezuleika happy at left
                show duren happy at right
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
                
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
                
            elif partner == "Chael":
                cb "You're doing very well, Princess."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
                
            elif partner == "Kirile":
                kb "You've got some really great moves. Keep it up!"
                show dancezuleika normal at left
                show kirile at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "You're doing very well, Princess."
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition3_round4
            
label allcompetition3_round4:
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
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
                
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
                
            elif partner == "Chael":
                cb "Well done, Princess."
                show dancezuleika normal at left
                show chael at right
                zb "On to the next one."
                
            elif partner == "Kirile":
                kb "That was great!"
                show dancezuleika normal at left
                show kirile at right
                zb "On to the next one."
                
            elif partner == "Nefferon":
                nb "Well done, Princess"
                show dancezuleika normal at left
                show nef at right
                zb "On to the next one."
            
            jump allcompetition3_round5
            
        "{image=GUI/Dance/Dance - SixChoice4B.png}":
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
                
            elif partner == "Kirile":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show kirile sad at right
                zb "Oops, sorry, Kirile. I missed a few steps there..."
                
                show kirile at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition3_round4
            
label allcompetition3_round5:
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
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
                
            elif partner == "Nefferon":
                show dancezuleika happy at left
                show nef happy at right
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That was fantastic, Zuleika."
                                
            elif partner == "Chael":
                cb "Wonderful, as expected from you."
                                
            elif partner == "Kirile":
                kb "I've never seen anyone dance as well as you."
                
            elif partner == "Nefferon":
                nb "As I thought, you're a remarkable dancer."
                            
            jump allcompetition3win
            
        "{image=GUI/Dance/Dance - SixChoice5B.png}":
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
                
            elif partner == "Kirile":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show kirile sad at right
                zb "Oops, sorry, Kirile. I missed a few steps there..."
                
                show kirile at right
                
            elif partner == "Nefferon":
                
                zb ". . ."
                
                show dancezuleika sad at left
                show nef sad at right
                zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
                show nef at right
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition3_round5
            
label allcompetition3win:
    scene bg black with fade
    $ energy -= 1
    
    scene bg dancehall with fade
    show vgirlf normal with dissolve
        
    if miss == 0:
        show vgirlf happy
        an "Congratulations on winning First Place in the third round!\nYour prize is 1000 Gold!"
        $ gold += 1000

        if partner == "Duren":
            $ DAffection += 10
            
        elif partner == "Chael":
            $ CAffection += 10
            
        elif partner == "Kirile":
            $ KAffection += 10
            
        elif partner == "Nefferon":
            $ NAffection += 10
        
    elif miss < 3:
        show vgirlf happy
        an "Congratulations on winning Second Place in the third round!\nYour prize is 500 Gold!"
        $ gold += 500
        
        if partner == "Duren":
            $ DAffection += 5
            
        elif partner == "Chael":
            $ CAffection += 5
            
        elif partner == "Kirile":
            $ KAffection += 5
            
        elif partner == "Nefferon":
            $ NAffection += 5
        
    else:
        show vgirlf sad
        an "Ouch, sorry that you lost..."
        an "Better luck next time."
        
    show vgirlf normal
    an "Thank you for participating. We hope to see you again next year!"
    
    $ dancing_skill += 50
    $ competition3_done = True
    stop music
    hide vgirlf
    jump allduggary_choice
            
label allduggaryinn1:
    
    scene bg inn night with fade
    play music "Audio/Sound/Nighttime.ogg"
    
    show lchael with dissolve
    "When I arrived at the inn that night, I found only Chael waiting for me."
    c "What have you decided, Princess?"
    show wlzuleika sad hidden
    z "You guys were right..."
    show wlzuleika angry hidden
    z "The only way Tyraca will ever be able to rebuild itself to its former glory is if a good, reliable king is on the throne...and Nefferon definitely doesn't fit that description."
    show lchael angry
    c "No, he definitely does not."
    show lchael sad
    c "There's...something else we need to discuss, as well."
    show wlzuleika sad hidden
    z "What is it, Chael?"
    c "All three of us going to the ball is...too risky."
    show lchael angry
    c "Not only would it be more difficult to get in, but if something were to go wrong, at least one of us needs to survive in order to carry on the mission."
    z "So, you're saying that I can only choose one of you to go with me..."
    show lchael sad
    c "Yes, Princess, I'm afraid so."
    z "...I understand. I'll...think about it."
    show lchael
    c "Please do. In the meantime, sleep well."
    hide lchael with dissolve
    "I doubted that I would be able to sleep well that night, not with so much running through my head..."
    
    if NAffection > max(CAffection, KAffection, DAffection):
        scene bg duggary
        play music "Audio/Music/Thatched Villagers (Village).ogg"
        "As we headed out the next morning, I was stopped by one of the villagers."
        show vboye nervous with dissolve
        m "Wait, before you go, this message came for you from the emperor."
        show wlzuleika sad hidden
        z "Another message?"
        hide vboye
        scene bg black with fade
        play music "Audio/Music/Dreamy Flashback.ogg"
        "\"Dear Princess...\""
        "\"I know that we have our differences, but ever since I first saw those beautiful emerald eyes of yours, I was in love.\""
        "\"I have kept my feelings hidden for all these years for fear of what my brother Osirus would do if he found out...\""
        "\"Now that he is gone, I can express my love freely...and my dear Zuleika, you are the only one for me.\""
        "\"Please, allow me to be your escort for the royal ball. Nothing in this world could ever make me happier.\""
        "\"I promise to make it worth your while.\""
        show wlzuleika sad hidden
        z "What an odd letter..."
        show wlzuleika normal hidden
        z "Even though he's my enemy, I'm touched by his heart-felt words. I think I'll take him up on his offer."
        $ ball = "Nefferon"
        $ NAffection += 400
        stop music
        jump allballnefferonA
        
    if DAffection > max(CAffection, KAffection, NAffection):
        scene bg duggary
        play music "Audio/Music/Thatched Villagers (Village).ogg"
        "As we headed out the next morning, I was stopped by one of the villagers."
        show vboye nervous with dissolve
        m "Wait, before you go, this message came for you from Prince Duren."
        show wlzuleika sad hidden
        z "Another message?"
        hide vboye
        scene bg black with fade
        play music "Audio/Music/Dreamy Flashback.ogg"
        "\"Dear Zuleika...\""
        "\"I have missed you so much these past few months.\""
        "\"It must be true what they say, that you never know what you have until it's gone...\""
        "\"I love you, Zuleika, my friend, my princess...I always have, and I always will.\""
        "\"I know that I screwed up, but please, allow me to make things right again.\""
        "\"This time...I'll do the right thing. I'll fix this, Zuleika, I swear.\""
        "\"So please, allow me to take you to the royal ball. I won't let you down.\""
        show wlzuleika sad hidden
        z "Oh, Duren...I've missed you, too."
        show wlzuleika normal hidden
        z "I think I'll take him up on his offer."
        $ ball = "Duren"
        $ DAffection += 400
        stop music
        jump allballdurenA
        
    else:
        jump allchp8A