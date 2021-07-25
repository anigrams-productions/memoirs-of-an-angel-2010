# Story A
# Chapter 03: Facing the Consequences
label allchp4AA:
    $ show_button_game_menu = False
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    play music "Audio/Music/Errigal.ogg"
    scene bg mountains sunset
    with fade
      
    if choice == "Chael":
        "It had been some time since we left the City of Jarconia, and we were half-way to our destination."
        "Chael hadn't changed at all since before that night we spent stargazing together; when I woke up the next morning, he was just as cold and silent as ever as he watched over the camp."
        "When he was like that, he kind of reminded me of a guard dog. I smiled at the thought."
        
    else:
        "It had been some time since we left the City of Jarconia, and we were half-way to our destination."

    show chael 2 at left
    with dissolve
    c "It's getting late. Let's set up camp here for now."
    
    show kirile sad at right
    with dissolve
    k "Shouldn't we try to get a little further before true dark sets in? There’s still a bit of light…"
    
    show chael angry2 at left
    "Chael frowned and looked at me. I blushed a little, realizing that he was stopping for my sake."
    "It was true that I was tired; these last several days had been particularly hard on me."
    "I wasn't used to such tough terrain, or traveling at all for that matter, much less for long periods of time."
    "I knew it was starting to take its toll on me, but I had been doing my best to hide my fatigue. Was my act that transparent?"
    
    c "We're stopping here, and that's final."
    show chael 2 at left
    show kirile at right
    "Kirile nodded and the three of us began setting up camp."
    
    stop music fadeout 2.0
    
    show kirile angry2 at right
    show chael angry at left
    
    "But as I went to start making the fire, Chael and Kirile suddenly became tense."
    
    "I could hear Kirile’s low growling on the other side of me." 
    "Something was definitely wrong.\nI grabbed a small knife I carried with me and readied myself, just in case."
    play music "Audio/Music/News of Sorrow (Battle with Duren).ogg"
    "Soon, the reason for their suddenly defensive behavior revealed itself: a group of soldiers, carrying the purple and gold flag of the Neffronian Empire, was marching towards us."
    "...We had been found."
    "But what worried me more than the soldiers, was who marched with them...it was a face I knew all too well."
    
    hide chael
    hide kirile
    with dissolve
    
    show duren with dissolve
    
    "It was none other than the young Prince Duren, a dear friend I never actually expected to meet again, and certainly not so soon."
    d "Zuleika…I've finally found you. I'm so glad you're alright."
    "As he looked at my companions, his expression became one of shock."
    show duren angry
    d "Lord Chael...is that...? Can it really be...? But why?"
    "He couldn’t believe it; the man who had kidnapped his dearest friend, the man who he traveled across the country to kill, was, in fact, the very man who had taught him everything he knew: his beloved mentor, Chael the Wise."
    hide duren with dissolve
    show chael angry2 with dissolve
    c "This was my choice, Duren, just as it was hers."
    hide chael with dissolve
    show duren sad with dissolve
    d "Is that true, Zuleika? Was this your choice?"
    "I nodded silently."
    show duren sad
    with Pause(.5)
    scene duren hand mountains with dissolve
    "The blue-haired man looked very sad for a moment, then held out his hand to me."
    d "Please, Zuleika, come back with me. Your people need you…{i}I{/i} need you."
    
    menu:
        "\"I'm sorry, but I can't.\"":
            $ CAffection += 20
            $ KAffection += 20
            jump allmountainsfightA
        "Take his hand":
            play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
            "I looked at Duren, then at my companions, then back at Duren again...and finally, I took his hand."
            scene bg mountains sunset with dissolve
            
            show chael angry2 at left
            show kirile sad at right
            with dissolve
            
            show wzuleika sad hidden
            z "I'm sorry...Chael...Kirile..."
            z "You've done so much for me; I am truly thankful to both of you. However...this must come to an end."
            
            "I {i}had{/i} felt a little guilty about running around the country while poor Duren was left to deal with Nefferon on his own."
            "I was supposed to be his friend, after all, and yet I had left him there, alone..."
            "This was my only chance to make things right, even if it meant leaving the two companions I had grown so close to." 

            k "But, Zuleika -"
            show chael sad2 at left
            c "Do what you need to do, Princess."
            
            hide chael
            hide kirile
            with dissolve 
            
            show duren with dissolve

            "I turned away as the tears started flowing down my cheeks."
            show wzuleika angry hidden
            z "Let's go, Duren."
            
            hide duren with dissolve

            "Thus, we went our separate ways, never to meet again."
            
            jump epilogue
            
label allmountainsfightA:
    scene bg mountains sunset with dissolve
    show duren sad
    "He didn't seem surprised by my refusal, but it upset him nonetheless."
    d "Very well. I'm afraid I have no choice..."
    show duren angry
    d "I'm sorry, Zuleika...but if you won't come of your own volition, then we'll just have to take you back by force."
    hide duren with dissolve
    
    show kirile angry2 at right
    show chael angry at left
    with dissolve
    "As Duren shot the first arrow, the soldiers behind him raised their swords and began to charge."
    scene bg black with fade
    "In an instant, Kirile grabbed my hand and started running as I watched Chael stay behind to hold off the enemy forces."
    "I knew that both Chael and Duren were excellent fighters, and I shivered to think of the two of them, mentor and student, fighting one another, but I didn't have the time to dwell on it."
    "Two soldiers were closing in fast behind us as we made our escape."
    "Without hesitation, knowing that these soldiers were now my enemies, I threw my small knife into the throat of one while Kirile took out the other."
    "It was clear to me, at this point more than any other, that there could be no turning back."
    stop music
    scene bg cave with fade
    play music "Audio/Sound/Nighttime.ogg"
    
    "The two of us finally made our way to a mountain cave, out of sight of our pursuers."
    "It was late and the night was cold; I shivered, both from the cold and from thinking about what could have happened to Chael, who still hadn't returned."
    
    show kirile
    with dissolve
    show wzuleika sad hidden
    z "Do you think he's okay?"
    k "Oi, cheer up! I'm sure he's fine. He's a strong guy who can take care of himself."
    show kirile happy
    k "He's a legend, you know, even in Pyralis."
    
    show kirile
    
    "I tried to smile back, but I also knew Duren's strength and skill, which were not to be underestimated."
    "I couldn't shake the fear that something bad had happened to Chael, and if so…"
    
    k "I'll keep watch outside for a while, so you can get some sleep."
    z "Thank you."
    
    if choice == "Chael":
    
        scene bg inside cave with fade
        play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
    
        "I sat inside the cave for what seemed like hours, waiting for Chael to get back and fearing the worst."
        "Suddenly, I heard some noises outside." 
        show chael sad with dissolve
        "A moment later, Kirile came in, supporting Chael, who was covered in wounds."
        "Chael tried to motion me away, but I insisted on staying by his side and immediately started dressing his wounds with what little materials I had."
        "Chael stopped me, taking my hand in his, and the two of us looked at each other for several minutes."
    
        show chael
        c "There's no need to worry about me, Princess. I'll be fine soon enough…Nalani heal more quickly than humans."
    
        show wzuleika angry hidden
        z "Who says I’m worried about you?"
        z "I'm {i}angry{/i} at you for being such an {i}idiot{/i}. Did you seriously think you could take on all of them by yourself without getting hurt?"
    
        show chael angry
        c "Of course I didn't, but I had to protect you somehow…"
    
        show wzuleika angry hidden
        z "For your information, I don't need {i}anyone{/i} to protect me."
        z "Believe it or not, I'm a fully capable woman and I can take care of myself."
        $ CAffection += 20
        show chael happy
        "...Was he actually smiling?"
    
        scene chael cave with dissolve
        $ persistent.chaelcave = True
        "He suddenly grabbed me and pulled me close to him, holding me in a tight embrace."
        c "Princess, since I met you, I have felt and experienced so many new things…pain, anger, even happiness."
        c "Before that day, I was lifeless…I felt nothing, not pleasure nor pain; I did whatever I was told and thought nothing of it."
        c "But you…you've given me life, and for the first time, I feel truly {i}alive{/i}."
    
        c "It's a wonderful feeling. I wish I could hold onto it forever…"
    
        show wzuleika normalblush hidden
        z "You can...\nI'll stay by your side...and I'll remind you of what it means to feel."
    
        c "Thank you, Zuleika."
    
        jump allmountaincamp3
        
    else:
        scene bg black with fade
        "I stayed up as long as I could, but eventually, I drifted off into an uneasy sleep."
        "However, I was soon woken by the sound of Chael returning. I was relieved to see that though he had a few scratches, he seemed to be fine."
        
        jump allmountaincamp3
    
label allchp4AB:
    $ show_button_game_menu = False
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    play music "Audio/Music/Errigal.ogg"
    scene bg mountains sunset
    with fade
    
    "It had been some time since we left the City of Jarconia, and we had already stopped at a couple of different small villages along the Pyralin border."
    "Since that night, Kirile had been acting particularly affectionate towards me, and much to my surprise, Chael no longer reprimanded him for it."

    show chael 2 at left
    c "It's getting late. Let's set up camp here for now."
    
    show kirile sad at right
    k "Shouldn't we try to get a little further before true dark sets in? There’s still a bit of light…"
    
    show chael angry2 at left
    c "It's important to rest; we need our strength for the trek tomorrow."
    "I realized that he was covering for me and smiled despite myself."
    "It was true that I was tired; these last several days had been particularly hard on me."
    "I wasn't used to such tough terrain, or traveling at all for that matter, much less for long periods of time."
    "I knew it was starting to take its toll on me, but I had been doing my best to hide my fatigue."
    "Kirile had been fooled, it seemed – he was probably too excited about the trip to notice – but I couldn't deceive a Nalani."
    
    show chael 2 at left
    show kirile at right
    "Kirile nodded, taking the hint, and the three of us began setting up camp."
    
    stop music fadeout 2.0
    
    show kirile angry2 at right
    show chael angry at left
    stop music
    "But as I went to start making the fire, Chael and Kirile suddenly became tense."
    
    "I could hear Kirile’s low growling on the other side of me." 
    "Something was definitely wrong.\nI grabbed a small knife I carried with me and readied myself, just in case."
    play music "Audio/Music/News of Sorrow (Battle with Duren).ogg"
    "Soon, the reason for their suddenly defensive behavior revealed itself: a group of soldiers, carrying the purple and gold flag of the Neffronian Empire, was marching towards us."
    "...We had been found."
    "But what worried me more than the soldiers, was who marched with them...it was a face I knew all too well."
    
    hide chael
    hide kirile
    with dissolve
    
    show duren with dissolve
    
    "It was none other than the young Prince Duren, a dear friend I never actually expected to meet again, and certainly not so soon."
    d "Zuleika…I've finally found you. I'm so glad you're alright."
    "As he looked at my companions, his expression became one of shock."
    show duren angry
    d "Lord Chael...is that...? Can it really be...? But why?"
    "He couldn’t believe it; the man who had kidnapped his dearest friend, the man who he traveled across the country to kill, was, in fact, the very man who had taught him everything he knew: his beloved mentor, Chael the Wise."
    hide duren with dissolve
    show chael angry2 with dissolve
    c "This was my choice, Duren, just as it was hers."
    hide chael with dissolve
    show duren sad with dissolve
    d "Is that true, Zuleika? Was this your choice?"
    "I nodded silently."
    show duren sad
    with Pause(.5)
    scene duren hand mountains with dissolve
    $ persistent.durenhandmountains = True
    "The blue-haired man looked very sad for a moment, then held out his hand to me."
    d "Please, Zuleika, come back with me. Your people need you…{i}I{/i} need you."
    
    menu:
        "\"I'm sorry, but I can't.\"":
            jump allmountainsfightB
        "Take his hand":
            play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
            "I looked at Duren, then at my companions, then back at Duren again…and finally, I took his hand."
            scene bg mountains sunset with dissolve
            
            show chael angry2 at left
            show kirile sad at right
            with dissolve
            
            show wzuleika sad hidden
            z "I'm sorry...Chael...Kirile..."
            z "You’ve done so much for me; I am truly thankful to both of you. However…this must come to an end."
            
            "I {i}had{/i} felt a little guilty about running around the country while poor Duren was left to deal with Nefferon on his own."
            "I was supposed to be his friend, after all, and yet I had left him there, alone…"
            "This was my only chance to make things right, even if it meant leaving the two companions I had grown so close to." 

            k "But, Zuleika -"
            show chael sad2 at left
            c "Do what you need to do, Princess."
            
            hide chael
            hide kirile
            with dissolve 
            
            show duren with dissolve

            "I turned away as the tears started flowing down my cheeks."
            show wzuleika angry hidden
            z "Let's go, Duren."
            
            hide duren with dissolve

            "Thus, we went our separate ways, never to meet again."
            
            jump epilogue
            
label allmountainsfightB:
    scene bg mountains sunset with dissolve
    show duren sad with dissolve
    "He didn't seem surprised by my refusal, but it upset him nonetheless."
    d "Very well. I'm afraid I have no choice..."
    show duren angry
    d "I'm sorry, Zuleika...but if you won't come of your own volition, then we'll just have to take you back by force."
    hide duren with dissolve
    
    show kirile angry2 at right
    show chael angry at left
    with dissolve
    "As Duren shot the first arrow, the soldiers behind him raised their swords and began to charge."
    scene bg black with fade
    "In an instant, Chael grabbed my hand and started running as I watched Kirile stay behind to hold off the enemy forces."
    "I knew that both Kirile and Duren were excellent fighters, and I shivered to think of the two of them fighting one another, pitting Duren's skill and agility against Kirile's raw strength, but I didn't have the time to dwell on it."
    "Two soldiers were closing in fast behind us as we made our escape."
    "Without hesitation, knowing that these soldiers were now my enemies, I threw my small knife into the throat of one while Chael took out the other."
    "It was clear to me, at this point more than any other, that there could be no turning back."
    stop music
    scene bg cave with fade
    play music "Audio/Sound/Nighttime.ogg"
    
    "The two of us finally made our way to a mountain cave, out of sight of our pursuers."
    "It was late and the night was cold; I shivered, both from the cold and from thinking about what could have happened to Kirile, who still hadn't returned."
    
    show chael
    show wzuleika sad hidden
    z "Do you think he's okay?"
    c "I wouldn't worry about him."
    c "If nothing else, that one knows how to handle himself in a fight. I'm sure he'll be fine."
    
    "I tried to force myself to smile, as I knew Kirile would in this situation, but I also knew Duren's strength and skill, which were not to be underestimated."
    "I couldn't shake the fear that something bad had happened to Kirile, and if so…"
    
    c "Get some rest. I'll keep watch outside."
    z "Thank you."
    
    scene bg inside cave with fade
    play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
    
    "I sat inside the cave for what seemed like hours, waiting for Kirile and fearing the worst."
    "Suddenly, I heard some noises outside." 
    show kirile sad
    with dissolve
    "A moment later, Chael came in, supporting Kirile, who was covered in wounds."
    "As Chael slipped out silently to resume his watch, I began dressing Kirile's wounds with whatever materials I could find."
    show kirile
    "He simply watched me for a while with a curious expression."

    k "You don't have to worry about me, you know. This is nothing compared to -"
    
    show kirile sad
    show wzuleika angry hidden
    z "Who says I’m worried about you?"
    z "I'm {i}angry{/i} at you for being such an {i}idiot{/i}. Did you seriously think you could take on all of them on your own without getting hurt?"
    
    show kirile angry
    k "I could have if it weren't for that blue-haired kid..."
    
    show wzuleika sad hidden
    z "That 'blue-haired kid' is legendary for his skill. You're lucky to have escaped with your life!"
    
    show kirile
    k "Pft…The day I'm defeated by some {i}kid{/i} is the day the fire pits of Pyralis freeze over."
    
    z "That over-confidence will get you killed some day, you know."
    $ KAffection += 20
    scene kirile cave with dissolve
    $ persistent.kirilecave = True
    "He smiled suddenly and grabbed me, pulling me into a tight embrace."
    k "That’s why I need you here to bring me back around." 
    k "As long as I have you around, I have a reason to survive and live on."
    "I smiled and blushed as my previous anger melted away."
    show wzuleika normalblush hidden
    z "Don't worry. I'll be here...so don't you die on me, okay?"

    k "Okay, I won't."
    
    jump allmountaincamp3
    
label allmountaincamp3:
    play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
    scene bg inside cave
    with fade

    show wzuleika normal hidden
    z "Now that all the commotion is over, I have some free time before we head off again in the morning."
    
    if zuleika_type == 'all' or zuleika_type == 'kind':
        $ search2_done = False
    $ chaelchat2_done = False
    $ kirilechat2_done = False
    
label allcampmenu2:    
    scene bg inside cave
    play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
    
    if energy == 0:
        jump allchp5A
        
    else:
        "What should I do?"
        menu:
            "Visit Chael":
                $ CAffection += 15
                jump allchael_menu2
            "Visit Kirile":
                $ KAffection += 15
                jump allkirile_menu2
            "Help out around camp":
                $ increase_kindness(30)
                $ energy -= 1
                play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
                show wzuleika angry hidden
                z "There's not much I can do to make this damp cave any more comfortable..."
                z "Oh well, these leaf beds I made will just have to do."
                jump allcampmenu2
            "Search area" if zuleika_type == 'all' and search2_done == False or zuleika_type == 'kind' and search2_done == False:
                $ energy -= 1
                $ search2_done = True
                scene bg cave
                play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
                show wzuleika normal hidden
                z "I managed to find some good-looking herbs growing near the cave."
                menu:
                    "Pick them up":
                        $ item_herbs += 1
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch2_2
                            "Return to camp":
                                jump allcampmenu2
                    "Leave them":
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch2_2
                            "Return to camp":
                                jump allcampmenu2
            "Rest":
                jump allchp5A
                
label allsearch2_2:
    show wzuleika normal hidden
    z "This turtle shell looks like it hasn't been inhabited for a long time."
    menu:
        "Pick it up":
            $ item_shell += 1
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch2_3
                "Return to camp":
                    jump allcampmenu2
        "Leave it":
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch2_3
                "Return to camp":
                    jump allcampmenu2
                    
label allsearch2_3:
    show wzuleika normal hidden
    z "Oh hey, I found a stone arrowhead. This might come in handy."
    menu:
        "Pick it up":
            $ item_arrowhead += 1
            z "I think that's enough searching for today. It's time to head back to camp."
            jump allcampmenu2
        "Leave it":
            z "I think that's enough searching for today. It's time to head back to camp."
            jump allcampmenu2
            
label allchael_menu2:
    play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
    scene bg night2
    show chael
    with dissolve
    c "...Yes, Princess?"
    menu:
        "Talk" if chaelchat2_done == False:
            $ increase_charm(20)
            $ chaelchat2_done = True
            $ energy -= 1
            play music "Audio/Music/Unpromised (Sad Chael Theme).ogg"
            jump allchaelchat2
        "Discuss strategy":
            $ increase_intelligence(30)
            $ energy -= 1
            play music "Audio/Music/Unpromised (Sad Chael Theme).ogg"
            c "I don't believe that Duren's attack was meant to be an ambush, but if it were, what were some of the flaws in his technique?"
            show wzuleika sad hidden
            z "Well, it wasn't much of an ambush..."
            show wzuleika normal hidden
            z "He had so many soldiers with him that we could tell he was coming from a mile away. That gave us time to prepare ourselves so that we weren't caught off-guard."
            c "Exactly. Even if we weren't angels, we still would have been alerted to his presence in advance. Anything else?"
            z "Hmm...\nOh, I know!"
            z "He didn't know who the enemy was. Otherwise, he would have been prepared to face you."
            c "That's right. Failing to know your enemy beforehand can be a fatal mistake."
            show chael angry
            c "If it had been anyone else, he'd probably be dead..."
            show chael sad
            c "Excuse me. We'll continue this later."
            hide chael
            jump allcampmenu2
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ CAffection += 1
                    $ item_bouquet -= 1
                    show chael
                    c "This is nice. Thank you."
                    jump allchael_menu2
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ CAffection += 1
                    $ item_makeup -= 1
                    show chael
                    c "This is nice. Thank you."
                    jump allchael_menu2
                "Miraculous Moonshine" if item_liquor > 0:
                    $ CAffection -= 5
                    $ item_liquor -= 1
                    show chael angry
                    c "Only humans would come up with such a disgusting substance."
                    jump allchael_menu2
                "Secret Stealth Knives" if item_knives > 0:
                    $ CAffection -= 5
                    $ item_knives -= 1
                    show chael angry
                    c "Why are you giving these to me?"
                    jump allchael_menu2
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ CAffection += 10
                    $ item_spellbook -= 1
                    show chael happy
                    c "This will be very useful to me. Thank you, Princess."
                    jump allchael_menu2
                "Elegant Earrings" if item_earrings > 0:
                    $ CAffection += 5
                    $ item_earrings -= 1
                    show chael happy
                    c "These are quite beautiful. Thank you, Princess."
                    jump allchael_menu2
                "Wild flowers" if item_flowers > 0:
                    $ CAffection += 10
                    $ item_flowers -= 1
                    show chael happy
                    c "These are really quite beautiful. Thank you, Princess."
                    jump allchael_menu2
                "Turtle shell" if item_shell > 0:
                    $ CAffection += 5
                    $ item_shell -= 1
                    show chael happy
                    c "This looks interesting. Thank you, Princess."
                    jump allchael_menu2
                "Herbs" if item_herbs > 0:
                    $ CAffection += 10
                    $ item_herbs -= 1
                    show chael happy
                    c "These will be very useful to me. Thank you, Princess."
                    jump allchael_menu2
                "Stone arrowhead" if item_arrowhead > 0:
                    $ CAffection += 1
                    $ item_arrowhead -= 1
                    show chael
                    c "This looks...interesting. Thank you."
                    jump allchael_menu2
                "Fruit" if item_fruit > 0:
                    $ CAffection += 5
                    $ item_fruit -= 1
                    show chael happy
                    c "I'm sure this will be delicious. Thank you, Princess."
                    jump allchael_menu2
                "Gold coin" if item_coin > 0:
                    $ CAffection += 1
                    $ item_coin -= 1
                    show chael
                    c "This looks...interesting. Thank you."
                    jump allchael_menu2
                "Nevermind":
                    jump allchael_menu2
        "Nevermind":
            jump allcampmenu2
            
label allkirile_menu2:
    play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
    scene bg cave
    show kirile
    with dissolve
    k "Oh, hey, Zuleika. Did you need something?"
    menu:
        "Talk" if kirilechat2_done == False:
            $ increase_charm(20)
            $ kirilechat2_done = True
            $ energy -= 1
            play music "Audio/Music/Harlequin (Zuleika and Kirile Meeting).ogg"
            jump allkirilechat2
        "Ask to train":
            $ increase_strength(30)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            hide kirile
            show wzuleika normal hidden
            z "Since it had already been a long day, we decided to keep it to some simple strength training exercises."
            if zuleika_type == 'intelligent':
                show wzuleika angry hidden
                z "Even so, I'm afraid I'll be sore tomorrow..."
            else:
                show wzuleika angry hidden
                z "I wish I had gotten a chance to fight those soldiers earlier. That would have been a much better work out."
            jump allcampmenu2
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ KAffection -= 5
                    $ item_bouquet -= 1
                    show kirile sad
                    k "Why are you giving these to me?"
                    jump allkirile_menu2
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ KAffection -= 5
                    $ item_makeup -= 1
                    show kirile sad
                    k "Why are you giving this to me?"
                    jump allkirile_menu2
                "Miraculous Moonshine" if item_liquor > 0:
                    $ KAffection += 10
                    $ item_liquor -= 1
                    show kirile happy
                    k "Just what I needed. Thanks, lass."
                    jump allkirile_menu2
                "Secret Stealth Knives" if item_knives > 0:
                    $ KAffection += 10
                    $ item_knives -= 1
                    show kirile happy
                    k "These will definitely come in handy. Thanks, lass."
                    jump allkirile_menu2
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ KAffection -= 5
                    $ item_spellbook -= 1
                    show kirile angry
                    k "Only Nalani use magic. Pyralins such as myself have no need for cheap tricks like that."
                    jump allkirile_menu2
                "Elegant Earrings" if item_earrings > 0:
                    $ KAffection += 1
                    $ item_earrings -= 1
                    show kirile
                    k "These are nice. Thanks"
                    jump allkirile_menu2
                "Wild flowers" if item_flowers > 0:
                    $ KAffection -= 5
                    $ item_flowers -= 1
                    show kirile sad
                    k "Why are you giving these to me?"
                    jump allkirile_menu2
                "Turtle shell" if item_shell > 0:
                    $ KAffection += 5
                    $ item_shell -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu2
                "Herbs" if item_herbs > 0:
                    $ KAffection += 1
                    $ item_herbs -= 1
                    show kirile
                    k "These are nice. Thanks"
                    jump allkirile_menu2
                "Stone arrowhead" if item_arrowhead > 0:
                    $ KAffection += 5
                    $ item_arrowhead -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu2
                "Fruit" if item_fruit > 0:
                    $ KAffection += 10
                    $ item_fruit -= 1
                    show kirile happy
                    k "Wow, this looks really delicious! Thanks, lass."
                    jump allkirile_menu2
                "Gold coin" if item_coin > 0:
                    $ KAffection += 5
                    $ item_coin -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu2
                "Nevermind":
                    jump allkirile_menu2
        "Nevermind":
            jump allcampmenu2
            
label allchaelchat2:
    scene bg night2
    show chael sad
    show wzuleika sad hidden
    z "You look upset...is something wrong?"
    show chael angry
    c "There's no moon tonight..."
    c "The source of Nalani magic is light. Without a powerful light source, such as the sun or moon, I can't use my magic."
    show chael sad
    c "I feel so useless on nights like this."
    
    menu:
        "\"You're never useless, Chael.\"":
            $ CAffection += 20
            show wzuleika normal hidden
            z "Even if you can't use magic, you're still an excellent swordsman."
            z "And plus, even in your weakened state, you still managed to help save my life yet again."
    
            show chael angry
            c "Only because that Pyralin was around. If he hadn't been here..."
    
            z "Then we would have figured something else out, I'm sure."
    
            show chael
            c "I suppose you're right, Princess."
    
            show wzuleika happy hidden
            z "I usually am, or haven't you figured that out yet?"
    
            show chael happy
            c "Hmm...I don't think you want my answer to that."
    
            show wzuleika angry hidden
            z "Hey, what's that supposed to mean?"
            
            hide chael
            stop music
    
            jump allcampmenu2
            
        "\"It does help when you have your magic...\"":
            show wzuleika sad hidden
            z "But you'll be fine again tomorrow, won't you?"
            show wzuleika normal hidden
            z "We just have to wait until then."
            show chael
            c "Yes, I suppose you're right."
            c "There's no use getting upset over something I can't control."
            show wzuleika happy hidden
            z "Have you been taking lessons on optimism from Kirile?"
            show chael angry
            c "As if I would ever learn anything from {i}that{/i} guy."
            hide chael
            stop music
            jump allcampmenu2
    
label allkirilechat2:
    scene bg cave
    show kirile
    
    k "Who exactly is that 'Duren' kid?"
    show wzuleika angry hidden
    z "You don't keep up with your politics, do you?"
    show kirile sad
    k "Am I supposed to?"
    show kirile
    k "I've never seen much point in dealing with that side of things...I just focus on the battles."
    k "So, who is he?"
    
    menu: 
        "\"He's a friend.\"":
            $ KAffection += 20
            show wzuleika normal hidden
            z "Duren is Nefferon's angel, and therefore the prince of the new Neffronian Empire."
            show wzuleika sad hidden
            z "He's also been my best friend for many years...though I suppose that's all changed now."
            show kirile sad
            k "I'm sorry, lass. It must be rough to lose a friend like that."
            z "It is, but...I think it's for the best, in the long run."
            show wzuleika normal hidden
            z "What about you, Kirile? Did you have any friends back in Pyralis?"
            k "As a general, I didn't have many opportunities to make friends."
            k "Maintaining authority within an army of demons is tough. I had to scare them into obeying orders, or else they would turn on me."
            k "There's not much room for bonding there..."
            show wzuleika sad hidden
            z "No, I suppose not."
            show wzuleika happy hidden
            z "At least you have friends now, right?"
            k "...Yeah?"
            show wzuleika normal hidden
            z "Of course!"
            z "I'm your friend...and even though Chael pretends not to like you, I think he's your friend, too."
            show kirile happy
            k "You can't imagine how happy it makes me to hear that."
            show kirile
            k "Thanks, lass. You're a wonderful friend."
            hide kirile
            stop music
            jump allcampmenu2
        "\"He's no one important.\"":
            show kirile sad
            k "You sure? You two seemed pretty close..."
            show wzuleika angry hidden
            z "He's just the guy who stole my position, that's all."
            z "We used to be friends a long time ago, but not anymore."
            k "Hmm..."
            show kirile
            k "I don't think he meant to hurt you by all that. Otherwise, he wouldn't have come all this way to find you."
            k "If I had a friend like that, someone who would cross the country looking for me, I think I would hold them closer to my heart."
            show wzuleika sad hidden
            z "I guess you're right, Kirile...I shouldn't blame him for what happened. He was as much a victim in this whole situation as I was."
            k "Anyway, I was just curious. Sorry I brought it up."
            show wzuleika normal hidden
            z "Oh, no, it's fine."
            hide kirile
            stop music
            jump allcampmenu2
            
# Ending 0
label epilogue:
    stop music
    play music "Audio/Sound/pencil-1.ogg" fadein 1.0
    scene black with fade
    with Pause(1)
    
    scene bg blank with fade
    show journal with dissolve
    
    "Years later, after enduring the tyrannical emperor's reign for so long, the nation of Tyraca was in ruin."
    
    "Duren and I, having since been exiled for plotting against the emperor, did our best to try to gain outside support from the other Great Nations in order to take him down."
    "However, they had also suffered great damage, and no one was willing to do anything that might spark another continental war."
    stop music fadeout 0.5
    play music "Audio/Music/For the Fallen.ogg"
    "Our cause seemed lost."
    "In a last desperate attempt, the two of us attempted to take him on by ourselves, knowing that it would probably cost us our lives, for the sake of our beloved kingdom."
    "We almost managed to make it to the throne room, but before we could complete our task, we were captured."
    "Nefferon had the two of us publically executed as an example of what happens to those who oppose the emperor..."
    "...but the executions didn't scare the people, but rather had quite the opposite effect."

    "Spurred on by our courage and righteous sacrifice, the people rose up and revolted against the oppressive tyrant once and for all."
    "Tyraca henceforth became the first democratic nation of the known world, ruled not by corrupt and greedy monarchs and nobles, but by the average citizens who loved their nation, just as I did long ago."
    "And that...is my story.\n\n(( Ending 0 of 15 ))"
    stop music
    scene black with fade
    with Pause(.5)

    $ persistent.ending0 = True
    
    jump end