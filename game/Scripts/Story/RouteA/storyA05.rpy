# Story A
# Chapter 05: Getting Closer
label allchp6A:
    call status from _call_status_6    

    $ show_button_game_menu = False
    
    stop music
    scene bg meadow with fade
    play music "Audio/Music/Errigal.ogg"
    "Some time had passed since we left the village."
    "Each village we stopped at was more and more hostile towards us..."
    "It had gotten to the point where we had to stay away from heavily traveled paths for fear of being seen."
    "For a while, I was afraid that Chael or Kirile might turn me in, but it seemed that they were loyal companions after all. I was so thankful to have them by my side..."
    
    show chael with dissolve
    c "Let's stop here for now."
    c "We're almost there, and we don't want to get too close to the city until we have to."
    "Kirile and I nodded in agreement, and we began setting up camp."
    
    scene bg black with fade
    
    scene bg meadow with fade
    show wzuleika normal hidden
    z "Well, it looks like I have some free time to spend around camp before nightfall."
    
    if zuleika_type == 'all' or zuleika_type == 'kind':
        $ search3_done = False
    $ chaelchat3_done = False
    $ kirilechat3_done = False
    if zuleika_type == 'all' or zuleika_type == 'intelligent':
        $ pyralis_done = False
    
label allcampmenu3:    
    if energy == 0:
        jump allchp7A
        
    else:
        scene bg meadow
        play music "Audio/Music/Errigal.ogg"
        "What should I do?"
        menu:
            "Visit Chael":
                $ CAffection += 15
                jump allchael_menu3
            "Visit Kirile":
                $ KAffection += 15
                jump allkirile_menu3
            "Help out around camp":
                $ increase_kindness(30)
                $ energy -= 1
                scene bg black with fade
                with Pause(1.0)
                scene bg meadow with fade
                play music "Audio/Music/Errigal.ogg"
                show wzuleika angry hidden
                z "Whew, that was hard work!"
                show wzuleika normal hidden
                z "But at least we're all set for tonight now."
                z "I made sure to collect plenty of firewood and gathered some delicious looking fruit for dessert."
                jump allcampmenu3
            "Search area" if zuleika_type == 'all' and search3_done == False or zuleika_type == 'kind' and search3_done == False:
                $ energy -= 1
                $ search3_done = True
                play music "Audio/Music/Errigal.ogg"
                show wzuleika happy hidden
                z "This fruit looks delicious!"
                menu:
                    "Pick it up":
                        $ item_fruit += 1
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch3_2
                            "Return to camp":
                                jump allcampmenu3
                    "Leave it":
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch3_2
                            "Return to camp":
                                jump allcampmenu3
            "Rest":
                jump allchp7A
                
label allsearch3_2:
    show wzuleika happy hidden
    z "Look at these flowers...they're beautiful!"
    menu:
        "Pick them up":
            $ item_flowers += 1
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch3_3
                "Return to camp":
                    jump allcampmenu3
        "Leave them":
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch3_3
                "Return to camp":
                    jump allcampmenu3
                    
label allsearch3_3:
    show wzuleika normal hidden
    z "Oh hey, I found a gold coin. I doubt I could use this to pay with, though."
    menu:
        "Pick it up":
            $ item_coin += 1
            z "I think that's enough searching for today. It's time to head back to camp."
            jump allcampmenu3
        "Leave it":
            z "I think that's enough searching for today. It's time to head back to camp."
            jump allcampmenu3
            
label allchael_menu3:
    play music "Audio/Music/Errigal.ogg"
    scene bg meadow
    show chael
    with dissolve
    c "What can I do for you, Princess?"
    menu:
        "Talk" if chaelchat3_done == False:
            $ increase_charm(20)
            $ chaelchat3_done = True
            $ energy -= 1
            play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
            jump allchaelchat3
        "Discuss strategy":
            $ increase_intelligence(30)
            $ energy -= 1
            hide chael
            show wzuleika normal hidden
            z "We talked for hours about why the Battle of Forge was such a key battle in the war, and why the Pyralin forces had such an advantage in this case."
            if zuleika_type == 'strong':
                show wzuleika sad hidden
                z "Rather, Chael talked while I listened and tried to understand. I'm pretty sure most of the lesson was lost on me..."
            else:
                z "I'll have to keep some of that in mind the next time I spar with Kirile."
            jump allcampmenu3
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ CAffection += 1
                    $ item_bouquet -= 1
                    show chael
                    c "This is nice. Thank you."
                    jump allchael_menu3
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ CAffection += 1
                    $ item_makeup -= 1
                    show chael
                    c "This is nice. Thank you."
                    jump allchael_menu3
                "Miraculous Moonshine" if item_liquor > 0:
                    $ CAffection -= 5
                    $ item_liquor -= 1
                    show chael angry
                    c "Only humans would come up with such a disgusting substance."
                    jump allchael_menu3
                "Secret Stealth Knives" if item_knives > 0:
                    $ CAffection -= 5
                    $ item_knives -= 1
                    show chael angry
                    c "Why are you giving these to me?"
                    jump allchael_menu3
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ CAffection += 10
                    $ item_spellbook -= 1
                    show chael happy
                    c "This will be very useful to me. Thank you, Princess."
                    jump allchael_menu3
                "Elegant Earrings" if item_earrings > 0:
                    $ CAffection += 5
                    $ item_earrings -= 1
                    show chael happy
                    c "These are quite beautiful. Thank you, Princess."
                    jump allchael_menu3
                "Wild flowers" if item_flowers > 0:
                    $ CAffection += 10
                    $ item_flowers -= 1
                    show chael happy
                    c "These are really quite beautiful. Thank you, Princess."
                    jump allchael_menu3
                "Turtle shell" if item_shell > 0:
                    $ CAffection += 5
                    $ item_shell -= 1
                    show chael happy
                    c "This looks interesting. Thank you, Princess."
                    jump allchael_menu3
                "Herbs" if item_herbs > 0:
                    $ CAffection += 10
                    $ item_herbs -= 1
                    show chael happy
                    c "These will be very useful to me. Thank you, Princess."
                    jump allchael_menu3
                "Stone arrowhead" if item_arrowhead > 0:
                    $ CAffection += 1
                    $ item_arrowhead -= 1
                    show chael
                    c "This looks...interesting. Thank you."
                    jump allchael_menu3
                "Fruit" if item_fruit > 0:
                    $ CAffection += 5
                    $ item_fruit -= 1
                    show chael happy
                    c "I'm sure this will be delicious. Thank you, Princess."
                    jump allchael_menu3
                "Gold coin" if item_coin > 0:
                    $ CAffection += 1
                    $ item_coin -= 1
                    show chael
                    c "This looks...interesting. Thank you."
                    jump allchael_menu3
                "Nevermind":
                    jump allchael_menu3
        "Nevermind":
            jump allcampmenu3
            
label allkirile_menu3:
    play music "Audio/Music/Errigal.ogg"
    scene bg meadow
    show kirile happy
    with dissolve
    k "I think my day just got ten times better."
    show kirile
    k "What's up?"
    menu:
        "Talk" if kirilechat3_done == False:
            $ increase_charm(20)
            $ kirilechat3_done = True
            $ energy -= 1
            play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
            jump allkirilechat3
        "Ask to train":
            $ increase_strength(30)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
            if zuleika_type == 'intelligent':
                show kirile
                k "I can't believe it - you're actually getting better!"
                show wzuleika angry hidden
                z "I better be, with all the training I've been doing."
                show kirile happy
                k "I'm sure you'll be kicking butt in no time."
            else:
                show kirile
                k "So, to do this, you move your arm like this...yes, yes, that's it."
                show wzuleika normal hidden
                z "Oh, wow, that's a really useful move. I can definitely see how that could come in handy during battle."
                show wzuleika happy hidden
                z "Thank you for showing it to me, Kirile."
                show kirile happy
                k "No problem. I hope it'll help you as much as it's helped me."
                z "I'm sure it will."
            hide kirile
            jump allcampmenu3
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ KAffection -= 5
                    $ item_bouquet -= 1
                    show kirile sad
                    k "Why are you giving these to me?"
                    jump allkirile_menu3
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ KAffection -= 5
                    $ item_makeup -= 1
                    show kirile sad
                    k "Why are you giving this to me?"
                    jump allkirile_menu3
                "Miraculous Moonshine" if item_liquor > 0:
                    $ KAffection += 10
                    $ item_liquor -= 1
                    show kirile happy
                    k "Just what I needed. Thanks, lass."
                    jump allkirile_menu3
                "Secret Stealth Knives" if item_knives > 0:
                    $ KAffection += 10
                    $ item_knives -= 1
                    show kirile happy
                    k "These will definitely come in handy. Thanks, lass."
                    jump allkirile_menu3
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ KAffection -= 5
                    $ item_spellbook -= 1
                    show kirile angry
                    k "Only Nalani use magic. Pyralins such as myself have no need for cheap tricks like that."
                    jump allkirile_menu3
                "Elegant Earrings" if item_earrings > 0:
                    $ KAffection += 1
                    $ item_earrings -= 1
                    show kirile
                    k "These are nice. Thanks"
                    jump allkirile_menu3
                "Wild flowers" if item_flowers > 0:
                    $ KAffection -= 5
                    $ item_flowers -= 1
                    show kirile sad
                    k "Why are you giving these to me?"
                    jump allkirile_menu3
                "Turtle shell" if item_shell > 0:
                    $ KAffection += 5
                    $ item_shell -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu3
                "Herbs" if item_herbs > 0:
                    $ KAffection += 1
                    $ item_herbs -= 1
                    show kirile
                    k "These are nice. Thanks"
                    jump allkirile_menu3
                "Stone arrowhead" if item_arrowhead > 0:
                    $ KAffection += 5
                    $ item_arrowhead -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu3
                "Fruit" if item_fruit > 0:
                    $ KAffection += 10
                    $ item_fruit -= 1
                    show kirile happy
                    k "Wow, this looks really delicious! Thanks, lass."
                    jump allkirile_menu3
                "Gold coin" if item_coin > 0:
                    $ KAffection += 5
                    $ item_coin -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu3
                "Nevermind":
                    jump allkirile_menu3
        "Ask about Pyralis" if zuleika_type == 'all' and pyralis_done == False or zuleika_type == 'intelligent' and pyralis_done == False:
            play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
            $ investigative_skill += 50
            $ pyralis_done = True
            $ energy -= 1
            jump allpyralis1
        "Nevermind":
            jump allcampmenu3
            
label allchaelchat3:
    show chael
    show wzuleika normal hidden
    z "Hey Chael, what do you like to do for fun?"
    show chael angry
    c "...\"Fun\"?"
    z "Yeah, you know...what do you enjoy doing? What makes you happy?"
    c "...I'm not sure. I've never thought about it before."
    show wzuleika sad hidden
    z "Don't they have games or anything in Nalan?"
    c "Oh, they do...but I was never allowed to participate in them, so I'm not sure if I would enjoy them or not."
    
    menu:
        "\"That's sad...\"":
            z "Your mistress definitely wasn't very nice to you, was she?"
            show chael sad
            c "No...she wasn't."
            show chael angry
            c "...I would prefer not to discuss this anymore. Excuse me."
            hide chael with moveoutleft
            jump allcampmenu3
        "\"Well, let's find something you do enjoy, then.\"":
            $ CAffection += 20
            show chael
            c "And what do you propose, Princess?"
            show wzuleika normal hidden
            z "Why don't we wander around the area for a bit?"
            show chael angry
            c "How will that help?"
            show wzuleika happy hidden
            z "You'll see."
            
            scene bg black with fade
            
            scene bg lake with fade
            play music "Audio/Music/Dreamy Flashback.ogg"
            show chael with dissolve
            show wzuleika normal hidden
            z "So, what do you think?"
            show chael happy
            c "I think...I enjoy life, being surrounded by nature, and...being with you."
            z "...Really? I...enjoy being with you, too."
            
            if CAffection > max(KAffection, DAffection, NAffection):
                show chael
                c "Actually, I have something I've been meaning to give to you."
                show chael blush
                c "I found it in the market of the last village we visited, and it's a very rare find outside of Nalan."
                c "Here...it's a tiara, made out of authentic elven silver."
                show chael happyblush
                c "You may not be official anymore, but you'll always be a princess to me."
                
                menu:
                    "\"Thank you so much!\"":
                        scene bg black
                        stop music
                        with fade
        
                        "Received \"Elven Tiara\"."
                        $ gift = "Tiara"
                        $ persistent.gifttiara = True
                        $ CAffection += 20
                        
                        scene bg lake with fade
                        play music "Audio/Music/Dreamy Flashback.ogg"
                        show chael happyblush with dissolve
                        
                        show wzuleika happyblush hidden
                        z "It's so beautiful, Chael."
                        show wzuleika normalblush hidden
                        z "And to tell you the truth, I kind of missed my old tiara...I just didn't feel right without it."
                        z "Just like...I wouldn't feel right if you weren't here with me."
                        c "Before I met you, I never believed in fate...but I believe that we were brought together for a reason."
                        show wzuleika happyblush hidden
                        z "I wouldn't have thought it, but you're actually quite romantic, aren't you?"
                        c "...Only with you, Princess."
                        hide chael
                        jump allcampmenu3
                    "\"I can't accept something like this...\"":
                        $ CAffection -= 100
                        play music "Audio/Music/Unpromised (Sad Chael Theme).ogg"
                        show chael angry
                        show wzuleika sad hidden
                        z "I'm sure it cost you a fortune, right?"
                        z "I couldn't possible accept something so rare and valuable..."
                        c "I wouldn't have presented it to you if I didn't want you to have it."
                        z "But still..."
                        c "Nevermind. I'm sorry to have bothered you, Princess."
                        hide chael with moveoutleft
                        z "I'm sorry, Chael..."
                        jump allcampmenu3
                        
            else:
                c "I'm glad to hear you say that, Princess."
                show chael
                c "We should probably start heading back now."
                show wzuleika normal hidden
                z "Yes, let's go."
                hide chael
                jump allcampmenu3
            
label allkirilechat3:
    show kirile
    show wzuleika normal hidden
    z "I know that you were a high ranking officer in the army during the war, but what were you before that, during the long period of peace?"
    k "Actually, even then I was involved in the military, but it was a different kind of work."
    k "You see, not all demons are strong and powerful; some tribes are actually quite weak and fragile, so they need extra protection now and then."
    show wzuleika sad hidden
    z "Protection from what?"
    show kirile sad
    k "Other tribes, mostly...or in the worst case, dragons."
    show kirile angry
    k "Those dragons are nasty little buggers. They destroy everything in sight, and wrestling with 'em certainly isn't easy."
    show wzuleika angry hidden
    z "...You didn't \"wrestle them\" with your bare hands, did you?"
    show kirile sad
    k "Of course I did. Isn't that what you're supposed to do?"
    show wzuleika sad hidden
    z "Er...well..."
    show kirile
    k "Anyway, while they were tough to beat, I usually managed to scare 'em off long enough to help out the tribe."
    show kirile happy
    k "I did manage to actually defeat one, though, and even took a souvenir: one of its claws."
    k "I made it into a necklace that I always keep with me, as a reminder of the good ol' days."
    
    if KAffection > max(CAffection, DAffection, NAffection):
        show kirile blush
        k "Zuleika, I...want you to have it."
        menu:
            "\"Thank you so much!\"":
                scene bg black
                stop music
                with fade
        
                "Received \"Dragon Claw Necklace\"."
                $ KAffection += 20
                $ gift = "Claw Necklace"
                $ persistent.giftclaw = True
                
                scene bg meadow
                play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
                show kirile blush with dissolve
                
                show wzuleika happyblush hidden
                z "Really, I'm honored to receive such a gift."
                show kirile happyblush
                k "I'm so happy you like it."
                show kirile blush
                k "Always keep it close to your heart, alright?"
                z "I will!"
                jump allcampmenu3
            "\"I can't accept something like this...\"":
                $ KAffection -= 100
                play music "Audio/Music/Dissappointment (Sad Kirile Theme).ogg"
                show kirile sad
                show wzuleika sad hidden
                z "It's too important to you...you should keep it."
                k "I {i}want{/i} you to have it, though."
                z "I'm sorry, Kirile...but I just can't accept it."
                stop music
                jump allcampmenu3
    else:
        show wzuleika happy hidden
        z "That's so cool!"
        k "Thanks."
        show kirile
        show wzuleika normal hidden
        z "Are you glad that you don't have to do that anymore?"
        k "Definitely."
        show kirile happy
        k "Though it would be pretty funny to watch Chael try to wrestle one of those dragons."
        show wzuleika happy hidden
        z "It would, wouldn't it?"
        jump allcampmenu3
        
label allpyralis1:
    show kirile
    k "So, you want to know more about my home, huh?"
    
    show wzuleika normal hidden
    z "I do. What can you tell me about it?"
        
    k "Well, let's see..."
    k "Basically, it's made up of many different demon tribes, each with their own unique characteristics."
    k "All of Pyralis is ruled by the seven Sisters of Hell, who are the daughters of the Supreme God of Chaos himself."
    
    show wzuleika sad hidden
    z "\"Supreme God?\""
    
    show kirile sad
    k "All the gods who are a part of the Great Council now are only so in title...there are very few true ones left."
    show kirile
    k "The ones who are \"true\" are descended directly from the two original beings who created this world."
    k "You see..."
    
    stop music
    scene bg black with fade
    with Pause(.5)
    
    play music "Audio/Music/Arcadia.ogg"
    
    k "In the beginning, there were two powerful beings: a god and a goddess. Together, they created this world."
    
    show chaos god at truecenter
    with dissolve
    
    k "The god had the power of chaos, and created everything that is dark and evil, as some would call it."
    k "He called the land \"Pyralis\" and created strange, beast-like creatures who could withstand its harsh climates."
    k "He made each type of creature from scratch, imbuing each species with certain qualities which would allow it to survive."
    k "The most powerful of these, known as \"true bloods\" were made in his own image, and were granted the power of darkness."
    k "All of his creations, then, were granted the power of great physical strength, which allowed them to move and shape their surroundings."
    
    hide chaos god
    k "That is how the Supreme God of Chaos created Pyralis."
    
    scene bg meadow
    play music "Audio/Music/Errigal.ogg"
    
    show wzuleika normal hidden
    z "(This story sounds strangely familiar...)"
    show wzuleika angry hidden
    z "(Where have I heard something like it before?)"
    
    if investigative_skill > 99:
        show wzuleika normal hidden
        z "(Oh, I remember! It's just like the story about the creation of Nalan!)"
        z "Kirile?"
        show kirile
        k "What is it?"
        show wzuleika sad hidden
        z "The feuding between Pyralis and Nalan doesn't make sense at all."
        show kirile sad
        k "What do you mean by that?"
        z "I mean...you said that your god and a goddess created the world {i}together{/i}, right?"
        z "Have you ever thought about what happened to the goddess from the story?"
        k "...Not really. She's never really mentioned in the Story of Creation."
        show wzuleika normal hidden
        z "She is in Nalan...I think the goddess who made Nalan is the same goddess who helped create the world."
        k "...You really think so?"
        z "Come on, let's find Chael."
        
        scene bg black with fade
        
        scene bg meadow with fade
        
        show chael 2 at left
        show kirile at right
        with dissolve
        c "What is it, Princess?"
        show wzuleika normal hidden
        z "Chael, have you ever heard the Pyralin Story of Creation?"
        show chael angry2 at left
        show kirile sad at right
        c "No, of course not. I'm suprised that such idiotic creatures even - "
        show wzuleika angry hidden
        z "Hey, be nice!"
        z "Believe it or not, your story and his compliment each other perfectly."
        show wzuleika normal hidden
        z "I think that the god who made Pyralis and the goddess who made Nalan were the god and goddess who created the world...{i}together.{/i}"
        z "Don't you see what this means?"
        z "In the beginning, the Nalani and Pyralins weren't enemies...they were friends. They both had their role to play in the world, and they complimented each other."
        c ". . ."
        k ". . ."
        c "I suppose...that makes sense."
        show kirile at right
        k "But it's kind of hard to wrap your head around, isn't it? I mean...we've hated each other for so long."
        c "It does make one wonder why the hatred began in the first place."
        k "And how the other half of the story just disappeared..."
        show kirile at right
        k "Ah well, I guess there's no point in worryin' about it now."
        show kirile happy at right
        k "What do you say? Friends?"
        show chael 2 at left
        c "...Let's stick with acquaintances."
        
        hide chael
        hide kirile
        
        jump allcampmenu3
        
    else:
        jump allcampmenu3