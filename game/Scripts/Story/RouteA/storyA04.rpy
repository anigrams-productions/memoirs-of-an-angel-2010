# Story A
# Chapter 04: The Hunt Begins
label allchp5A:
    
    call status from _call_status_5    
 
    $ show_button_game_menu = False
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    scene bg faraway village day with fade
    play music "Audio/Music/Skye Cuillin.ogg"
    "Some time had passed since the attack, and we were approaching another village on the way to our destination." 
    "Though we hadn't run into any more pursuers, I was sure there were more to come, and if the three of us were to be discovered in the city…I shuddered to think what would happen to us."

    "Chael apparently sensed my unease and moved closer to me."
    show chael with dissolve
    c "Stay close to me, Princess."
    c "If anyone tries to come after us, I'll strike them down."
    hide chael with dissolve
    "I smiled; his assurance, as strange as it was, made me feel better."
    show kirile with dissolve
    k "Yeah, don't worry, lass."
    show kirile happy
    k "We'll protect ya from those guys, whatever it takes."

    show wzuleika happy hidden
    z "Thanks, Kirile."

    stop music
    scene bg black with fade
    "This light-hearted mood didn't last long...\nAs soon as we reached the city, what we saw made my stomach turn."
    
    scene bg rundown village with fade
    play music "Audio/Music/Myst (Dark Village Theme).ogg"
    
    "The once lively city was now an impoverished ghost town. Buildings lay in ruins everywhere, and the villagers looked no better off."
    "Was this a result of the war? No, it looked more recent than that, but surely it couldn't have been the bandits Chael mentioned before…a few bandits couldn't have done all of this damage."

    show lchael angry
    c "Let's take a look around.\nWe need to find out what happened here."
    
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    scene bg dark corridor with fade
    
    m "Stop, please...I...I don't know where she is, I swear!"
    play sound "Audio/Sound/whipcrack.ogg"
    so "Tell me where she is!"
    play sound "Audio/Sound/whipcrack.ogg"
    m "I don't know...I don't know..."
    
    c "I think that's enough."
    "When the soldier saw Chael's sword at the ready, he left in a hurry."
    
    play music "Audio/Music/Myst (Dark Village Theme).ogg"
    show vboya sad at right
    show lchael 2 at left
    with dissolve
    
    c "Are you okay, sir?"
    m "I'm fine now, thanks to you."
    
    show lchael angry2 at left
    c "Who is it that he was looking for?"
    
    show vboya nervous at right
    m "...A woman. The former princess...Zuleika."
    
    c "...I see. Thank you for the information.\nI hope you stay out of trouble."
    
    hide vboya
    hide lchael
    with dissolve
    
    play music "Audio/Music/Lone Harvest.ogg"
    "I could feel a knot forming in my chest as I realized that I was responsible for all of this."
    "That's what happened to this town...the emperor's men destroyed it while looking for me, and now they were hurting these innocent people..."
    
    show lchael angry with dissolve
    
    c "I was afraid that something like this would happen...but I must admit that I didn't expect them to get here so soon."
    
    show wlzuleika sad hidden
    z "What are we going to do?"
    
    hide lchael
    show lkirile with dissolve
    k "Personally, I think we should stick around for a while."
    k "Since people from this country won't recognize us, Chael and I will take a look around town and see what we can find out."
    k "As for you...as long as you stay low and don't do anything suspicious, I'm sure you'll be fine."
    
    z "But..."
    hide lkirile
    show lchael with dissolve
    c "I hate to admit it, but the Pyralin's right. If we can get to the bottom of this, then maybe we can help these people."
    show lchael angry
    c "I know that the situation looks bad, but if we act rashly, it'll only get worse."
    
    z "I suppose you're right..."
    
    show lchael
    c "We'll meet up with you at the inn when we're done."
    c "Until then, Princess, try to stay out of trouble."
    
    scene bg rundown village with fade
    play music "Audio/Music/Myst (Dark Village Theme).ogg"
    show wlzuleika normal hidden
    z "Well, since we're here...I may not be able to help with the investigation, but I can at least help gather supplies."
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        $ competition2_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament2_done = False
    
label allrundownvillage_choice:
    scene bg rundown village
    play music "Audio/Music/Myst (Dark Village Theme).ogg"
    
    if energy == 0:
        jump allrundownvillageinn
    else:
        "What should I do?"
        menu:
            "Visit the Shop":
                jump allshop_menu4
            "Go to the Library":
                jump alllibrary_menu4
            "Practice at the Training Hall":
                jump alltraining_menu4
            "Volunteer at the Church":
                jump allchurch_menu4
            "Enter Martial Arts Tournament" if zuleika_type == 'all' and tournament2_done == False or zuleika_type == 'strong' and tournament2_done == False:
                jump alltournament2
            "Enter Dancing Competition" if zuleika_type == 'all' and competition2_done == False or zuleika_type == 'charming' and competition2_done == False:
                jump allcompetition2
            "Rest at the Inn":
                stop music
                jump allrundownvillageinn
            
label allshop_menu4:
    $ location = 'allshop4'
    scene bg shop
    play music "Audio/Music/Nothing Broken (Shop).ogg"
    with fade
    show vgirla nervous with dissolve
    
    s "You look like that princess everyone is looking for..."
    show vgirla sad
    s "You're not her, right? 'Cause if you are..."
    show wlzuleika sad hidden
    z "No, no, I'm not her."
    show vgirla normal
    s "If you say so..."

    menu:
        "Buy":
            s "You have %(gold)d Gold remaining. What would you like to buy?"
            jump allbuy_menu4
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
            jump allrundownvillage_choice
        "Return to town":
            stop music
            jump allrundownvillage_choice
            
label allbuy_menu4:
    show vgirla normal
    menu:
        "\"A Gift of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'intelligent' or zuleika_type == 'strong' or zuleika_type == 'charming':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "No":
                    jump allbuy_menu4
        "\"A Bouquet of Fanciful Flowers\" - 15 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "They're pretty, aren't they? And they make such wonderful gifts, too. I bet you have someone in mind, don't you? "
            if gold < 15:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 15
                    $ increase_kindness(10)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "Buy as a gift":
                    $ gold -= 15
                    $ item_bouquet += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "Don't buy":
                    jump allbuy_menu4
        "\"Penniless Princess' Travel Kit\" - 45 Gold":
            s "Ah, what a great item! After all, young beauties like ourselves need to look good, even on the go. "
            if gold < 45:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "Buy as a gift":
                        $ gold -= 45
                        $ item_makeup += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "Don't buy":
                        jump allbuy_menu4
            else:
                menu:
                    "Yes":
                        $ gold -= 45
                        $ increase_charm(15)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "No":
                        jump allbuy_menu4
        "\"Miraculous Moonshine\" - 50 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Let go and enjoy yourself with this intoxicating drink. Just don't go overboard."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 50
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "Buy as a gift":
                    $ gold -= 50
                    $ item_liquor += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "Don't buy":
                    jump allbuy_menu4
        "\"Secret Stealth Knives\" - 80 Gold":
            s "When you're in a pinch, it helps to have something to defend yourself with. Oh, but please, don't use them in the store. "
            if gold < 80:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "Buy as a gift":
                        $ gold -= 80
                        $ item_knives += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "Don't buy":
                        jump allbuy_menu4
            else:
                menu:
                    "Yes":
                        $ gold -= 80
                        $ increase_strength(20)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "No":
                        jump allbuy_menu4
        "\"Sinister Spellbook for Beginners\" - 100 Gold":
            s "Excellent choice! I just hope you don't plan to use any of those spells on me... "
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            if zuleika_type == 'all' or zuleika_type == 'kind':
                menu:
                    "Buy for self":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "Buy as a gift":
                        $ gold -= 100
                        $ item_spellbook += 1
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "Don't buy":
                        jump allbuy_menu4
            else:
                menu:
                    "Yes":
                        $ gold -= 100
                        $ increase_intelligence(25)
                        s "You now have %(gold)d Gold. "
                        jump allbuy_menu4
                    "No":
                        jump allbuy_menu4
        "\"Elegant Earrings\" - 150 Gold" if zuleika_type == 'all' or zuleika_type == 'kind':
            s "Adorning yourself with jewelry has long been a way to show off your wealth...er...I mean...make yourself look pretty."
            if gold < 150:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Buy for self":
                    $ gold -= 150
                    $ increase_charm(25)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "Buy as a gift":
                    $ gold -= 150
                    $ item_earrings += 1
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "Don't buy":
                    jump allbuy_menu4
        "\"Pristine Princess Potion\" (Charm Booster) - 500 Gold":
            s "Even the gaudiest pauper can look like a beautiful princess with this potion. Speaking of which, has anyone ever told you that you look just like Princess Zuleika?"
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_charm(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "No":
                    jump allbuy_menu4
        "\"Potent Puissance Potion (Strength Booster)\" - 500 Gold":
            s "Bulking up, huh? You know, too much of that will give you wrinkles. Not that that should stop you, of course... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_strength(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "No":
                    jump allbuy_menu4
        "\"Brain Boosting Book\" - 500 Gold":
            s "Supposedly, this stuff will make you smarter instantly. I wonder if I should try some... "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_intelligence(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "No":
                    jump allbuy_menu4
        "\"Concentrated Compassion Concoction\" - 500 Gold":
            s "Aww, how kind of you...but wait, you didn't actually do anything! "
            if gold < 500:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 500
                    $ increase_kindness(100)
                    s "You now have %(gold)d Gold. "
                    jump allbuy_menu4
                "No":
                    jump allbuy_menu4
        "\"Magical Map\" - 50 Gold":
            s "This is a basic world map with a few major cities marked (like this one). It may be useful if you want to know where you are."
            if gold < 50:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
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
                    z "To the west is the nation of Pyralis, home of the demons, where Kirile is from."
                    show nation map at truecenter
                    with dissolve
                    z "I'm currently in a small run-down village on the Tyracan-Pyralin border."
                    scene bg shop with fade
                    show vgirla normal
                    s "You now have %(gold)d Gold."
                    jump allbuy_menu4
                "No":
                    jump allbuy_menu4
        "\"Wondrous Wardrobe Modifier\" - 100 Gold":
            s "It's always fun to try on new, cool-looking outfits, isn't it?"
            if gold < 100:
                show vgirla sad
                s "Oops, it doesn't look like you can afford this item!"
                jump allbuy_menu4
            "Should I buy this item?"
            menu:
                "Yes":
                    $ gold -= 100
                    hide vgirla with dissolve
                    jump change_clothes
                "No":
                    jump allbuy_menu4
        "Nevermind":
            jump allshop_menu4
            
label alllibrary_menu4:
    scene bg library
    play music "Audio/Music/Comfortable Mystery 4 (Library).ogg"
    with fade
    show vgirle normal with dissolve
    l "Welcome to the Library, the center for useful information."
    show vgirle nervous
    l "Come to think of it, you look an awful lot like Princess Zuleika..."
    show wlzuleika happy hidden
    z "What, me? No way!"
    show vgirle normal
    l "Alright, if you insist..."
    
    menu:
        "Do some research":
            hide vgirle
            show wlzuleika normal hidden
            z "I was a bit curious about Pyralis after meeting Kirile, so I did some research. "
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
            jump allrundownvillage_choice
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
            jump allrundownvillage_choice
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
            jump allrundownvillage_choice
        "Return to town":
            stop music
            jump allrundownvillage_choice
            
label alltraining_menu4: 
    scene bg training
    play music "Audio/Music/Cartoon Battle (Training Hall).ogg"
    with fade
    show vboyd normal with dissolve
    
    t "Yo! Looking for some action? You've come to the right place!"
    show vboyd nervous
    t "...Wait a second. You're not that princess chick, are you?"
    show wlzuleika sad hidden
    z "Er...no, no, of course not."
    show vboyd normal
    t "Just checkin'."
    
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
            jump allrundownvillage_choice
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
            jump allrundownvillage_choice
        "Spar with a partner":
            hide vboyd
            show wlzuleika angry hidden
            z "The partner I ended up sparring with was twice my size and obviously had nothing against hitting a girl."
            if zuleika_type == 'intelligent':
                show wlzuleika normal hidden
                z "I bet Kirile would beat him up if I asked him to...but then we'd both get in trouble."
            else:
                show wlzuleika happy hidden
                z "I'd much rather spar with someone like Kirile...he's so fun to fight with."
            $ increase_strength(25)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            stop music
            jump allrundownvillage_choice
        "Return to town":
            stop music
            jump allrundownvillage_choice
            
label allchurch_menu4:
    scene bg church
    play music "Audio/Music/Halls of the Undead (Church Theme).ogg"
    with fade
    show vboyf normal with dissolve
    
    p "Welcome, welcome. We can really use your help."
    show vboyf sad
    p "Though...you remind me a lot of that fugitive princess..."
    p "I'm afraid we can't let you in if that's the case. We can't afford any more trouble, you see."
    show wlzuleika sad hidden
    z "Oh, um...I'm not her, I'm really not."
    show vboyf normal
    p "Very well. I'm sorry I doubted you, miss."
    
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
            jump allrundownvillage_choice
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
            jump allrundownvillage_choice
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
            jump allrundownvillage_choice
        "Return to town":
            stop music
            jump allrundownvillage_choice
            
label alltournament2:
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
            $ zcritical = 0
            $ kcritical = 0
            stop music
            scene bg black with fade
            with Pause(.5)
            
            scene bg courtyard with fade
            an "The second match will be..."
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSZuleika at left
            with moveinleft
            an "On this side, the former Princess Zuleika, known for her courage and conquests in battle,"
            
            play sound "Audio/Sound/SciFi_Power_Down_Metal_SE.ogg"
            show VSKirile at right
            with moveinright
            an "and on this one, we have Kirile the Powerful from the demon nation of Pyralis."
            an "Which of these legendary fighters will win? Let's find out!"
            
            hide VSKirile with moveoutright
            hide VSZuleika with moveoutleft
            
            scene bg courtyard
            play music "Audio/Music/Freddys Menagerie (Tournament - Kirile).ogg"
            
            show battlezuleika normal at left
            with dissolve
            
            show HPL at topleft
            with moveinleft
            
            zb "Come on, let's go!"
            
            show kirile at right
            with dissolve
            
            show HPR at topright
            with moveinright
            
            kb "I bet this'll be one hell of a fight."
            
            jump alltournament2_choice
            
        "How to Play":
            an "New to the tournament? Don't worry, it's easy to play!"
            an "Each round, you are given three choices: Attack, Defend, or Forfeit."
            an "Attack means that you throw an offensive attack at your enemy, but be careful because they'll attack you back with the same amount of force!"
            an "Defend means that you let the enemy attack first, but they do much less damage than they normally would. Then you get a chance to counterattack, but with less power than a normal attack."
            an "Forfeit means quitting the battle. You're advised to do so if you're about to lose."
            an "The more battles you fight in the tournament, the more battle skill you'll gain, so make sure to enter at every opportunity!"
            
            jump alltournament2
            
        "Return to town":
            stop music
            jump allrundownvillage_choice
            
label alltournament2_choice:
    menu:
        "Attack":
            
            show battlezuleika angry at left
            zb "Take this!"
            
            with flash
            
            if battle_skill > 49:
                $ zattack = renpy.random.randint(1,100)

                if zattack <= 35:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 15

                elif zattack > 35 and zattack <= 65:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 20

                elif zattack > 65 and zattack <= 85:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 25
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"

                else:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 30
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"
                    
            else:
                $ zattack = renpy.random.randint(1,100)

                if zattack <= 5:
                    show kirile happy at right
                    show battlezuleika sad at left
                    zb "Oh no! I missed!"

                elif zattack > 5 and zattack <= 35:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 15

                elif zattack > 35 and zattack <= 65:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 20

                elif zattack > 65 and zattack <= 85:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 25
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"

                else:
                    show kirile sad at right
                    with sshake
                    $ EHP -= 30
                
                    show battlezuleika happy at left
                    zb "Yes! Critical hit!"
                
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPL
                hide HPR
                jump alltournament2win
                
            else:
                show battlezuleika normal at left
                show kirile at right
                with Pause(1.5)
            
            show kirile angry at right
            kb "Let me show you how it's really done."
            
            with flash
            
            $ kattack = renpy.random.randint(1,100)

            if kattack <= 5:
                show kirile sad at right
                show battlezuleika happy at left
                kb "Crap, I missed..."

            elif kattack > 5 and kattack <= 50:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 15

            elif kattack > 50 and kattack <= 75:
                show battlezuleika sad at left
                with sshake
                $ ZHP -= 20

            elif kattack > 75 and kattack <= 90:
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
                jump alltournament2lose
                
            else:
                show battlezuleika normal at left
                show kirile at right
                
            jump alltournament2_choice
            
        "Defend":
            show battlezuleika angry at left
            
            zb "Go ahead, come at me."
            
            show kirile angry at right
            kb "Be careful what you ask for, lass."
            
            with flash
            
            $ kattack = renpy.random.randint(1,100)

            if kattack <= 5:
                show kirile sad at right
                show battlezuleika happy at left
                kb "Crap, I missed..."

            elif kattack > 5 and kattack <= 45:
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
                jump alltournament2lose
            
            else:
                show battlezuleika normal at left
                show kirile at right
                with Pause(1.5)
            
            show battlezuleika angry at left
            zb "Time to counter!"
            
            with flash
            
            $ zattack = renpy.random.randint(1,100)

            if zattack <= 35:
                show kirile sad at right
                with sshake
                $ EHP -= 5

            else:
                show kirile sad at right
                with sshake
                $ EHP -= 10
            
            if EHP < 1:
                show battlezuleika happy at left
                zb "Yay, I won!"
                hide HPR
                hide HPL
                jump alltournament2win
                
            else:
                show battlezuleika normal at left
                show kirile at right
                
            jump alltournament2_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    jump alltournament2
                "No":
                    jump alltournament2_choice
                    
label alltournament2win:
    stop music
    scene bg black with fade
    $ energy -= 1
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb happy with dissolve
    an "Congratulations on winning the second round!\nYour prize is 500 Gold!"
    $ gold += 500
    show vboyb normal
    an "That's all for today, but don't forget that the tournament is being held across the nation, so you can compete in any town."
    an "Good luck!"
    
    $ battle_skill += 50
    $ tournament2_done = True
    stop music
    hide vboyb
    jump allrundownvillage_choice
    
label alltournament2lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament2
            
        "Return to town":
            jump allrundownvillage_choice
            
label allcompetition2:
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
                    
                    jump allcompetition2_round1
                    
                "Chael":
                    $ partner = "Chael"
                    $ CAffection += 5
                    
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
                    
                    jump allcompetition2_round1
                    
                "Kirile":
                    $ partner = "Kirile"
                    $ KAffection += 5
                    
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
                    
                    jump allcompetition2_round1
                    
        "How to Play":
            an "New to the competiton? Don't worry, it's easy to play!"
            an "First, choose a partner. When you dance (and succeed) with a boy, you'll earn affection with him, so choose your partner wisely."
            an "Second, watch the step pattern that appears on the screen and try to memorize it."
            an "Finally, put your memory to the test and choose the correct combination from the choices given."
            an "If you get it right, you'll move on to the next round. If you get it wrong, you'll have to do it over again."
            an "Reach the end with as few wrong answers as possible to win!"
            
            jump allcompetition2
                    
        "Return to town":
            stop music
            jump allrundownvillage_choice
            
label allcompetition2_round1:
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
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
            
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
            
            jump allcompetition2_round2
            
        "{image=GUI/Dance/Dance - FiveChoice1B.png}":
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
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition2_round1
            
label allcompetition2_round2:
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
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition2_round2
            
        "{image=GUI/Dance/Dance - FiveChoice2B.png}":
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
            
            jump allcompetition2_round3
            
label allcompetition2_round3:
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
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition2_round3
            
        "{image=GUI/Dance/Dance - FiveChoice3B.png}":
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
                kb "You have some really great moves. Keep it up!"
                show dancezuleika normal at left
                show kirile at right
                zb "On to the next one."
            
            jump allcompetition2_round4
            
label allcompetition2_round4:
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
                
            elif partner == "Chael":
                show dancezuleika happy at left
                show chael happy at right
                
            elif partner == "Kirile":
                show dancezuleika happy at left
                show kirile happy at right
            
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
            
            jump allcompetition2_round5
            
        "{image=GUI/Dance/Dance - FiveChoice4B.png}":
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
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition2_round4
            
label allcompetition2_round5:
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
                
            show dancezuleika normal at left
            zb "Let's try that again."
            
            jump allcompetition2_round5
            
        "{image=GUI/Dance/Dance - FiveChoice5B.png}":
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
            
            $ HP += 20
            
            zb "Perfect!"
            
            if partner == "Duren":
                db "That was fantastic, Zuleika."
                
            elif partner == "Chael":
                cb "Wonderful, as expected from you."
                
            elif partner == "Kirile":
                kb "I've never seen anyone dance as well as you."
            
            jump allcompetition2win
            
label allcompetition2win:
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
            
        elif partner == "Chael":
            $ CAffection += 10
            
        elif partner == "Kirile":
            $ KAffection += 10
        
    elif miss < 3:
        show vgirlf happy
        an "Congratulations on winning Second Place in the second round!\nYour prize is 250 Gold!"
        $ gold += 250
        
        if partner == "Duren":
            $ DAffection += 5
            
        elif partner == "Chael":
            $ CAffection += 5
            
        elif partner == "Kirile":
            $ KAffection += 5
        
    else:
        show vgirlf sad
        an "Ouch, sorry that you lost..."
        an "Better luck next time."
        
    show vgirlf normal
    an "That's all for today, but don't forget that the competition is being held across the nation, so you can compete in any town."
    an "Good luck!"
    
    $ dancing_skill += 50
    $ competition2_done = True
    stop music
    hide vgirlf
    jump allrundownvillage_choice
            
label allrundownvillageinn:
    
    if zuleika_type == 'all' and tournament2_done == True or zuleika_type == 'strong' and tournament2_done == True:
        scene bg rundown village
        play music "Audio/Music/Happy Boy End Theme.ogg"
        
        u "Hey, wait up!"
        
        show lkirile with dissolve
        k "You were really something back there at the tournament."
        show lkirile happy
        k "I can't believe you beat me."
        
        show wlzuleika normal hidden
        z "I have a feeling it wasn't all my doing. You were holding back, weren't you?"
        
        show lkirile
        k "You noticed, huh?"
        
        menu:
            "\"Thanks for going easy on me.\"":
                k "No problem."
                show lkirile sad
                k "After all, Chael would've been angry if you'd gotten hurt..."
                z "He's just a bit protective, that's all."
                show lkirile
                z "Anyway, I'm glad you had a good time."
                show wlzuleika angry hidden
                z "Next time I'll beat you for real."
                k "I'm counting on it, lass."
                
                stop music
                jump allrundownvillageinn2
            "\"You didn't need to do that.\"":
                $ KAffection += 20
                show wlzuleika angry hidden
                z "I said it before and I'll say it again: I'm a strong woman, and I can take care of myself."
                z "I don't need you to hold back your punches for me."
                show lkirile sad
                k ". . ."
                show lkirile happy
                k "You've got quite the fighting spirit, don't you, lass? I love it!"
                show lkirile
                k "Next time we get a chance to spar, let's really go all-out."
                show lkirile happy
                k "If it's with you, I'm sure it'll be a blast."
                show wlzuleika happy hidden
                z "Sounds like a plan."
                
                stop music
                jump allrundownvillageinn2
    else:
        jump allrundownvillageinn2
      
label allrundownvillageinn2:
    scene bg inn night with fade
    play music "Audio/Sound/Nighttime.ogg"
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    "When I returned to the inn that night, Chael and Kirile were already there waiting for me."
    show lchael angry2 at left
    show lkirile sad at right
    with dissolve
    
    show wlzuleika sad hidden
    z "So...what did you find out?"
    
    c "Emperor Nefferon has sent search parties out to villages all throughout Tyraca."
    c "Their orders are to capture you alive...and to do whatever it takes to find you."
    
    k "We managed to find the leader of the search party in this town and \"convinced\" him to leave, but there are many others out there."
    
    show wlzuleika angry hidden
    z "That Nefferon...I really hate him."
    show wlzuleika sad hidden
    z "I guess the only thing we can do at this point is to continue on our way, and hopefully chase away some soldiers in the process."
    
    "The other two angels nodded, but the solemn looks on their faces remained."
    hide lchael with moveoutleft
    hide lkirile with moveoutright
    "After a moment, they each went their own ways; Chael remained in the room while Kirile went outside."
    "It seemed that I wasn't the only one with something to think about..."
    
    $ chaelinn_done = False
    $ kirileinn_done = False
    
label allrundownvillageinn_choice:
    scene bg inn night
    play music "Audio/Sound/Nighttime.ogg"
    
    menu:
        "Talk to Chael" if chaelinn_done == False:
            scene bg inn night
            play music "Audio/Music/Wounded.ogg"
            $ chaelinn_done = True
            $ CAffection += 20
            show lchael sad with dissolve
            show wlzuleika sad hidden
            z "Is something wrong?"
            c "It's just...seeing that man being whipped today brought back some painful memories."
            z "Were you...whipped?"
            show lchael sad2
            c "That was a long time ago..."
            z "But it obviously still hurts you, even now."
            show lchael angry2
            c "Yes...it's all about the pain."
            show lchael sad2
            c "When I was first created, I was filled with an overwhelming sense of grief."
            c "I didn't know why or where it came from...but it was as if I had lost something I didn't even know I had."
            show lchael angry2
            c "Menorrhi said that it was because I was too weak, that I had strayed from the light."
            c "...That's when the \"lessons\" started."
            scene bg black with fade
            c "She taught me to withstand physical and emotional pain by subjecting me to it, day after day, night after night."
            c "Pain became my world...the pain I felt, the pain given to me, the pain I gave to others..."
            c "Eventually, even the pain didn't matter anymore. Nothing did."
            scene bg inn night with fade
            show lchael angry with dissolve
            show wlzuleika sad hidden
            z "That sounds horrible, Chael. It's no wonder you don't want to go home..."
            show wlzuleika angry hidden
            z "No one should have the right to treat you that way."
            
            stop music
            c ". . ."
            c "You should get some sleep, Princess."
            hide lchael with moveoutleft
            
            if kirileinn_done == False:
                jump allrundownvillageinn_choice
                
            else:
                jump allchp6A
            
        "Talk to Kirile" if kirileinn_done == False:
            scene bg rundown village night with fade
            play music "Audio/Music/Wounded.ogg"
            $ kirileinn_done = True
            $ KAffection += 20
            
            show lkirile sad2 with dissolve
            show wlzuleika sad hidden
            z "Kirile? Are you alright?"
            
            show lkirile
            k "Of course. I'm just fine."
            
            z "You certainly didn't look \"just fine\" a minute ago."
            
            k "I suppose I can't fool a smart lass like you, huh?"
            show lkirile sad
            k "That whole mess with your friend a while back...it brought back some bad memories that I haven't been able to get out of my head."
            z "Do you want to talk about it?"
            
            show lkirile
            k "I may have mentioned before that I didn't have many friends back in Pyralis...but I did have one."
            k "He was my second-in-command, and he was also my best friend."
            show wlzuleika normal hidden
            z "Was he like you?"
            show lkirile happy
            k "He was very much like me. We'd play jokes on each other all the time; it was great."
            show lkirile
            k "We were very close, and I trusted him with my life."
            show lkirile sad
            k "...But as it turned out, we weren't as good of friends as I thought."
            k "The day before the last big battle of the war, the Tyracan army offered us a large bribe if we agreed to surrender."
            k "Many of my men were tired of fighting and would have happily taken the money, but I knew that the honor of our nation was at stake, so I refused."
            
            scene bg black with fade
            k "That night, I was met with a mutiny...led by none other than my best friend."
            k "Our swords clashed, but I held back. I didn't want to hurt him."
            k "In a moment, he told me that he was sorry, that he didn't want to fight me anymore, and I believed him..."
            k "As soon as I put away my sword, that's when he swung his, right across my face."
            
            scene bg rundown village night with fade
            show lkirile sad
            k "After that, he and the rest of the army left me for dead, leaving behind scars that will never heal..."
            
            show wlzuleika sad hidden
            z "Oh, Kirile...that's so sad. I had no idea..."
            
            stop music
            k "...I better go. See you tomorrow."
            hide lkirile with moveoutleft
            
            scene bg inn night with fade
            
            if chaelinn_done == False:
                jump allrundownvillageinn_choice
                
            else:
                jump allchp6A
            
        "Go to bed":
            jump allchp6A