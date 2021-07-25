# Story A
# Chapter 02: At a Standstill
label allchp3A:
    $ show_button_game_menu = False
    scene bg path
    play music "Audio/Music/Firesong.ogg"
    with fade
    
    "It had been a week since Kirile joined Chael and I on our travels, but we didn't get far before the boys' clashing ideas put us at a stand-still."
    "Chael and Kirile, being from two rival nations that have been bitter enemies for centuries, refused to get along with each other."
    "Any little thing could set them off, from a slightly overcooked meal to something Chael interpreted as \"suggestive\" aimed at me."
    "This time, the fight was about where we should go next."
 
    show chael 2 at left
    show kirile at right
    with dissolve
    
    c "We should head north towards Duggary Village."
    c "I heard that they’ve been having problems with bandits there lately. If we can take them out, we can probably earn some sort of payment as well as find valuable allies."
    
    k "No way, man. I say we head south along the border."
    k "The demons around there can be really rowdy, and there are many small villages around there that could use our help."
    
    show chael angry2 at left
    c "That would take us too close to the Pyralin capital; it’s too dangerous."
    c "We should go north, as I said."
    
    show kirile angry at right
    k "We would be {i}fine{/i}. I know this area like the back of my hand."
    k "I could get us past the capital without a problem, so we should go south, like I told ya."
    
    "The two angels glared fiercely at each other, growling, as if daring the other to attack."
    "Then they suddenly turned to me and waited for my input."
    
    menu:
        "Agree with Chael":
            play music "Audio/Music/Errigal.ogg"
            $ CAffection += 20
            $ destination = "Duggary"
            show chael happy2 at left
            show kirile sad at right
            
            show wzuleika sad hidden
            z "Sorry, Kirile, but I'm going to have to agree with Chael on this one."
            "Chael nodded approvingly, obviously satisfied with my decision."
            "Was that even the hint of a smile I saw?"
            
            show kirile at right
            show chael 2 at left
            k "Well, if the lady wants to go north, then we’ll go north."
            
            hide kirile
            hide chael
            with dissolve 
            
            jump allmountaincamp1
            
        "Agree with Kirile":
            play music "Audio/Music/Errigal.ogg"
            $ KAffection += 20
            $ destination = "sealine village"
            show chael angry2 at left
            show kirile at right
            
            show wzuleika sad hidden
            z "…I'm sorry, Chael, but in this case, I think Kirile is right."
            z "We should go south and help the people along the border, as he said."
            
            "The angel frowned, obviously disappointed, but he accepted my decision."
            
            show kirile at right
            k "I'm glad you see things my way. And see? I told you we'd make a good team."
            show kirile happy at right
            k "Now then, let's go kick some evil ass!"
            
            jump allmountaincamp1
            
        "Play a game to decide the winner":
            $ destination = "Duggary"
            show chael angry2 at left
            show kirile angry at right
            
            "I simply couldn't choose between them; they both seemed like perfectly reasonable options, and more importantly, I didn't want to disappoint either of them."
            show wzuleika normal hidden
            z "I know! Let's decide with a coin toss. What'll it be, gentlemen?"

            c "Heads."
            k "Hey, no fair. You answered so fast I didn't even get a chance..."
            c "That's certainly not my fault."

            show wzuleika angry hidden
            z "Boys, please..."
            stop music
            "As the two young men watched intently, each hoping to win, I carefully flipped the coin up into the air and let it fall onto the back of my hand."

            "I then revealed the coin: it was lying face-up, meaning that Chael had won."
            play music "Audio/Music/Errigal.ogg"
            show chael happy2 at left
            show kirile sad at right
            
            show wzuleika normal hidden
            z "I guess that settles it, then."
            
            show chael 2 at left
            show kirile at right
            "Though Kirile looked disappointed at first, it wasn't long before he wore his usual grin again."
            k "Well, looks like I lost fair and square. North it is."

            "Having finally made a decision, we prepared to begin the trek north to Duggary Village, one of the main commercial centers of the Neffronian Empire."

            
label allmountaincamp1:
    scene bg path
    show chael with dissolve
    c "We'll pack up and head out first thing tomorrow morning."
    c "Until then, feel free to wander around the area."
    hide chael with moveoutleft
            
    show wzuleika normal hidden
    z "It looks like I have some free time to spend around camp."
    z "I can visit Chael to chat and earn Charm or have a discussion to increase my Intelligence."
    z "Or I can visit Kirile to chat or ask him to train me to increase my Strength."
    z "If I'm in a helpful mood, I can help out around camp and earn Kindness points."
    if zuleika_type == 'all' or zuleika_type == 'kind':
        z "I can even search the area to find things that I can pick up."
    z "When I'm ready to move on, I can rest."
    
    if zuleika_type == 'all' or zuleika_type == 'kind':
        $ search1_done = False
    $ chaelchat1_done = False
    $ kirilechat1_done = False
    if zuleika_type == 'all' or zuleika_type == 'intelligent':
        $ nalan_done = False
    
label allcampmenu1:    
    scene bg path
    play music "Audio/Music/Errigal.ogg"
    
    if energy == 0:
        jump allmountaincamp2
        
    else:
        "What should I do?"
        menu:
            "Visit Chael":
                $ CAffection += 15
                jump allchael_menu1
            "Visit Kirile":
                $ KAffection += 15
                jump allkirile_menu1
            "Help out around camp":
                $ increase_kindness(30)
                $ energy -= 1
                scene bg black with fade
                with Pause(0.5)
                scene bg path with fade
                play music "Audio/Music/Errigal.ogg"
                show wzuleika angry hidden
                z "Whew, that was hard work!"
                show wzuleika normal hidden
                z "But at least we're all set for tonight now."
                z "I made sure to collect plenty of firewood and gathered some delicious looking fruit for dessert."
                jump allcampmenu1
            "Search area" if zuleika_type == 'all' and search1_done == False or zuleika_type == 'kind' and search1_done == False:
                $ energy -= 1
                $ search1_done = True
                play music "Audio/Music/Errigal.ogg"
                show wzuleika happy hidden
                z "Look at these flowers...they're beautiful!"
                menu:
                    "Pick them up":
                        $ item_flowers += 1
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch1_2
                            "Return to camp":
                                jump allcampmenu1
                    "Leave them":
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch1_2
                            "Return to camp":
                                jump allcampmenu1
            "Rest":
                jump allmountaincamp2
                
label allsearch1_2:
    show wzuleika happy hidden
    z "This fruit looks delicious!"
    menu:
        "Pick it up":
            $ item_fruit += 1
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch1_3
                "Return to camp":
                    jump allcampmenu1
        "Leave it":
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch1_3
                "Return to camp":
                    jump allcampmenu1
                    
label allsearch1_3:
    show wzuleika normal hidden
    z "Oh hey, I found a stone arrowhead. This might come in handy."
    menu:
        "Pick it up":
            $ item_arrowhead += 1
            z "I think that's enough searching for today. It's time to head back to camp."
            jump allcampmenu1
        "Leave it":
            z "I think that's enough searching for today. It's time to head back to camp."
            jump allcampmenu1
            
label allchael_menu1:
    play music "Audio/Music/Errigal.ogg"
    show chael angry with dissolve
    c "Don't you have somewhere better to be, Princess?"
    menu:
        "Talk" if chaelchat1_done == False:
            $ increase_charm(20)
            $ chaelchat1_done = True
            $ energy -= 1
            play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
            show chael
            jump allchaelchat1
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
            jump allcampmenu1
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ CAffection += 1
                    $ item_bouquet -= 1
                    show chael
                    c "This is nice. Thank you."
                    jump allchael_menu1
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ CAffection += 1
                    $ item_makeup -= 1
                    show chael
                    c "This is nice. Thank you."
                    jump allchael_menu1
                "Miraculous Moonshine" if item_liquor > 0:
                    $ CAffection -= 5
                    $ item_liquor -= 1
                    show chael angry
                    c "Only humans would come up with such a disgusting substance."
                    jump allchael_menu1
                "Secret Stealth Knives" if item_knives > 0:
                    $ CAffection -= 5
                    $ item_knives -= 1
                    show chael angry
                    c "Why are you giving these to me?"
                    jump allchael_menu1
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ CAffection += 10
                    $ item_spellbook -= 1
                    show chael happy
                    c "This will be very useful to me. Thank you, Princess."
                    jump allchael_menu1
                "Elegant Earrings" if item_earrings > 0:
                    $ CAffection += 5
                    $ item_earrings -= 1
                    show chael happy
                    c "These are quite beautiful. Thank you, Princess."
                    jump allchael_menu1
                "Wild flowers" if item_flowers > 0:
                    $ CAffection += 10
                    $ item_flowers -= 1
                    show chael happy
                    c "These are really quite beautiful. Thank you, Princess."
                    jump allchael_menu1
                "Turtle shell" if item_shell > 0:
                    $ CAffection += 5
                    $ item_shell -= 1
                    show chael happy
                    c "This looks interesting. Thank you, Princess."
                    jump allchael_menu1
                "Herbs" if item_herbs > 0:
                    $ CAffection += 10
                    $ item_herbs -= 1
                    show chael happy
                    c "These will be very useful to me. Thank you, Princess."
                    jump allchael_menu1
                "Stone arrowhead" if item_arrowhead > 0:
                    $ CAffection += 1
                    $ item_arrowhead -= 1
                    show chael
                    c "This looks...interesting. Thank you."
                    jump allchael_menu1
                "Fruit" if item_fruit > 0:
                    $ CAffection += 5
                    $ item_fruit -= 1
                    show chael happy
                    c "I'm sure this will be delicious. Thank you, Princess."
                    jump allchael_menu1
                "Gold coin" if item_coin > 0:
                    $ CAffection += 1
                    $ item_coin -= 1
                    show chael
                    c "This looks...interesting. Thank you."
                    jump allchael_menu1
                "Nevermind":
                    jump allchael_menu1
        "Ask about Nalan" if zuleika_type == 'all' and nalan_done == False or zuleika_type == 'intelligent' and nalan_done == False:
            play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
            $ investigative_skill += 50
            $ nalan_done = True
            $ energy -= 1
            jump allnalan1
        "Nevermind":
            jump allcampmenu1
            
label allkirile_menu1:
    play music "Audio/Music/Errigal.ogg"
    show kirile with dissolve
    k "Hey, Zuleika. What's up?"
    menu:
        "Talk" if kirilechat1_done == False:
            $ increase_charm(20)
            $ kirilechat1_done = True
            $ energy -= 1
            play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
            jump allkirilechat1
        "Ask to train":
            $ increase_strength(30)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
            if zuleika_type == 'intelligent':
                show kirile happy
                k "You really suck at this, don't you?"
                show wzuleika angry hidden
                z "For the last time, I'm a princess, not a warrior."
                show wzuleika normal hidden
                z "I prefer to fight with my words, not my fists."
                show kirile
                k "Yeah, right. You're just mad that you lost."
                show wzuleika angry hidden
                z "Shut up, jerk."
            else:
                show kirile
                k "I figured you'd be really bad at this kind of thing, but you're actually quite strong."
                show kirile happy
                k "I'm quite impressed. Maybe next time {i}you{/i} should teach {i}me{/i}."
                show kirile
                show wzuleika normal hidden
                z "You're quite strong yourself, and you've got some interesting moves I've never seen before."
                z "I think you have plenty to teach me."
                show kirile happy
                k "Next time, then, I'll come up with something really cool to show you."
                show wzuleika happy hidden
                z "I'm looking forward to it."
            hide kirile
            stop music
            jump allcampmenu1
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ KAffection -= 5
                    $ item_bouquet -= 1
                    show kirile sad
                    k "Why are you giving these to me?"
                    jump allkirile_menu1
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ KAffection -= 5
                    $ item_makeup -= 1
                    show kirile sad
                    k "Why are you giving this to me?"
                    jump allkirile_menu1
                "Miraculous Moonshine" if item_liquor > 0:
                    $ KAffection += 10
                    $ item_liquor -= 1
                    show kirile happy
                    k "Just what I needed. Thanks, lass."
                    jump allkirile_menu1
                "Secret Stealth Knives" if item_knives > 0:
                    $ KAffection += 10
                    $ item_knives -= 1
                    show kirile happy
                    k "These will definitely come in handy. Thanks, lass."
                    jump allkirile_menu1
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ KAffection -= 5
                    $ item_spellbook -= 1
                    show kirile angry
                    k "Only Nalani use magic. Pyralins such as myself have no need for cheap tricks like that."
                    jump allkirile_menu1
                "Elegant Earrings" if item_earrings > 0:
                    $ KAffection += 1
                    $ item_earrings -= 1
                    show kirile
                    k "These are nice. Thanks"
                    jump allkirile_menu1
                "Wild flowers" if item_flowers > 0:
                    $ KAffection -= 5
                    $ item_flowers -= 1
                    show kirile sad
                    k "Why are you giving these to me?"
                    jump allkirile_menu1
                "Turtle shell" if item_shell > 0:
                    $ KAffection += 5
                    $ item_shell -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu1
                "Herbs" if item_herbs > 0:
                    $ KAffection += 1
                    $ item_herbs -= 1
                    show kirile
                    k "These are nice. Thanks"
                    jump allkirile_menu1
                "Stone arrowhead" if item_arrowhead > 0:
                    $ KAffection += 5
                    $ item_arrowhead -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu1
                "Fruit" if item_fruit > 0:
                    $ KAffection += 10
                    $ item_fruit -= 1
                    show kirile happy
                    k "Wow, this looks really delicious! Thanks, lass."
                    jump allkirile_menu1
                "Gold coin" if item_coin > 0:
                    $ KAffection += 5
                    $ item_coin -= 1
                    show kirile happy
                    k "This looks cool. Thanks, lass."
                    jump allkirile_menu1
                "Nevermind":
                    jump allkirile_menu1
        "Nevermind":
            jump allcampmenu1
            
label allchaelchat1:
    show wzuleika sad hidden
    z "I'm sorry that I ended up dragging you into this mess..."
    show chael angry
    c "There's nothing for you to apologize for, Princess. This was my choice."
    z "Do you...regret it?"
    show chael
    c "Not at all. For the first time in my life, I feel like a person rather than that woman's pet. It's a liberating feeling."
    z "But don't you miss your home?"
    c "Of course I do, but I still stick by my decision."
    show chael angry
    c "And what about you, Princess? Do you regret coming with me?"
    
    menu:
        "\"Not at all!\"":
            $ CAffection += 20
            show wzuleika normal hidden
            show chael
            z "Before this, I had only been out of the castle once or twice; the rest of the time, Osirus kept me locked away in the castle."
            z "I've seen so many new and interesting things while traveling with you, and I, too, have felt the wonderful feeling of liberation."
            z "I do miss my home, of course, and I miss Duren, too...but I think it was time for me to leave, and I'm glad that I did."
            show chael happy
            c "I'm happy to hear that, Princess. I'm glad you did, too."
    
            hide chael
            stop music
    
            jump allcampmenu1
            
        "\"Maybe a little...\"":
            show chael sad
            show wzuleika sad hidden
            z "I feel like I'm shirking my responsibilities by being out here..."
            z "Even if I'm technically not the princess anymore, I still care deeply about my people."
            z "Plus, I feel bad for leaving Duren there...\nNefferon is so cruel to him."
            c "I'm sorry you feel that way..."
            show chael angry
            c "It wasn't my intention to force you into leaving the castle, though looking back, I'm sure it seemed that way."
            show chael sad
            c "I hope you don't think ill of me, Princess."
            show wzuleika normal hidden
            z "You just did what you thought was right, Chael.\nI can't blame you for that."
            c ". . ."
            hide chael
            stop music
            jump allcampmenu1
    
label allkirilechat1:
    k "How exactly did a pretty princess like yourself end up here with {i}that{/i} guy?"
    show kirile sad
    k "I figured you would have been crowned by now, with the emperor dead and all..."
    
    menu:
        "\"Chael saved me.\"":
            show kirile sad
            show wzuleika sad hidden
            z "It was a dark, stormy night..."
            z "There I was, locked away in the highest point of the highest tower, waiting for my Prince Charming to come and rescue me..."
            show wzuleika normal hidden
            z "Just then, a magnificent white angel burst into my room."
            z "He said, \"Come with me, Princess. I'll make you my bride and save you from this wretched place.\""
            show wzuleika happy hidden
            z "And of course, I said yes."
            k "...His bride, huh?"
            show kirile
            k "I suppose that just means I'll have to try that much harder."
            hide kirile with moveoutleft
            show wzuleika angry hidden
            z "What did he mean by that?"
            stop music
            jump allcampmenu1
        "\"The princess thing didn't exactly work out...\"":
            $ KAffection += 20
            show wzuleika sad hidden
            z "I {i}should{/i} have been crowned, but the High Court obviously didn't like that plan. They crowned his brother, Nefferon, instead."
            show wzuleika angry hidden
            z "Knowing him, he probably bribed them to do it..."
            show kirile angry
            k "That guy sounds like a total jerk."
            show wzuleika sad hidden
            z "Believe me, he is.\nThere's a reason that they call him \"The Cruel,\" you know."
            show kirile
            k "Well, if it makes you feel any better, I think you would have made a great empress."
            show wzuleika happy hidden
            z "That does make me feel better. Thanks, Kirile."
            show kirile happy
            k "No problem."
    
            hide kirile
            stop music
    
            jump allcampmenu1
    
label allnalan1:
    show wzuleika normal hidden
    c "You want to know more about Nalan?"
    z "Yes, I really do. There's so little information about it at the castle, and even what I found in the last town wasn't very descriptive."
    
    show chael
    c "Very well. In order to understand my people, you must first understand how Nalan came to be."
    c "Have you heard the Story of Creation?"
    
    show wzuleika sad hidden
    z "No...in Tyraca, everything written before Osirus' reign was destroyed."
    
    show chael angry
    c "I assumed as much. In my experience, humans prefer to live in ignorance."
    show chael
    c "That's where we'll begin our story, then."
        
    stop music
    scene bg black with fade
    with Pause(.5)
    
    play music "Audio/Music/Arcadia.ogg"
    
    c "In the beginning, there were two powerful beings: a god and a goddess. Together, they created this world."
    
    show goddess at truecenter
    with dissolve
    
    c "The goddess had the power of order, and created everything that is light and pure."
    c "She bestowed upon her world the name \"Nalan\" and created a group of wise, mysterious creatures to inhabit it."
    c "Her first gift to them was the power of light, which is the source of all life."
    c "Her second gift to them was the power to speak without words, for words can be misinterpreted; thoughts cannot."
    c "Her third gift to them was the power to change their surroundings, which allowed them to develop advanced technology. This power is what humans call \"magic.\""
    c "Finally, she gave them a lush forest to live in, where they would be free from the influence of the outside world."
    
    hide goddess with fade
    c "That is how the nation of Nalan was born."
    
    scene bg path with dissolve
    play music "Audio/Music/Errigal.ogg"
    
    show wzuleika sad hidden
    z "(I feel like part of this story is missing.\nWhat about the {i}god{/i} who helped create the world?)"
    show wzuleika normal hidden
    z "(I suppose I'll have to do some more research to find out.)"
    
    jump allcampmenu1

label allmountaincamp2:
    play music "Audio/Sound/Nighttime.ogg"
    scene bg camp night
    with fade
    
    "That night, I was having a hard time sleeping."
    "I was excited about the road ahead, but I was also a little apprehensive."
    "There were a dozen things that could go wrong, and every time I closed my eyes, I started going through them in my head."
    "Since I couldn’t sleep, I decided that I might as well leave camp for a while."
    "I soon realized, however, that I wasn't the only one having trouble sleeping. My two companions had already left camp, each going their separate way."
    "This would probably be a great time to connect with them..."
    menu:
        "Stargaze with Chael":
            $ choice = "Chael"
            $ CAffection += 20
            jump allstargaze
        "Explore with Kirile":
            $ choice = "Kirile"
            $ KAffection += 20
            jump allexplore
        "Go to bed":
            $ choice = "none"
            scene bg black with fade
            with Pause(.5)
            
            call status from _call_status_2
            jump allchp4AA
            
label allstargaze:
    play music "Audio/Music/Long Road Ahead B.ogg"
    scene bg night
    with fade
    
    "The lush mountains of the Pyralin border really were beautiful, and I enjoyed looking out at the scenery."
    "Whenever I did, I felt overwhelmingly thankful that I left the castle. Otherwise, I would never have seen such beautiful sights."
    "...It was all thanks to this man.\nI smiled at the thought."
    
    show chael with dissolve
    
    c "Good evening, Princess.\nTo what do I owe this pleasure?"
    
    show wzuleika normal hidden
    z "I was just having a hard time getting to sleep, so I thought I would come out here and admire the view for a bit."
    
    show chael angry
    c "I see."
    
    show chael happy
    c "I haven't thanked you yet."
    
    show wzuleika sad hidden
    z "Thanked me for what?"
    
    c "For taking my hand...for trusting me...for not being afraid. It meant a lot to me."
    
    "I was shocked to see an actual smile – or something close – on his face."
    "It was, truly, a beautiful smile, as expected from such a beautiful man."
    
    show wzuleika normal hidden
    z "I should be the one thanking you."
    z "You risked everything to spare my life…I am truly in your debt."
    
    c "No...I am forever in yours."
    
    show chael
    
    c "In return, allow me to grant you a peaceful slumber tonight. It's the least I can do."
    c "Sweet dreams, Princess..."
    
    scene bg black with fade
    
    "Before I knew what hit me, I was in a deep, peaceful sleep, without a single nightmare to plague me."
    
    call status from _call_status_3
    jump allchp4AA
    
label allexplore:
    scene bg cave
    with fade
    
    "I decided to join Kirile, who was exploring an area near camp."
    "As I got closer, I realized that he had come across a small mountain cave." 
    "The environment around me never ceased to amaze me; everything was new and interesting."
    "The people here, too, were interesting…like Kirile.\nIt lightened my mood when I thought of him."
    
    play music "Audio/Music/Harlequin (Zuleika and Kirile Meeting).ogg"
    show kirile with dissolve
    k "Cave exploring at this time of night?"
    show kirile happy
    k "You sure are an adventurous one."
    show kirile
    
    show wzuleika normal hidden
    z "I was just having a hard time getting to sleep, so I thought I would come out here and see what you were up to."
    k "Well, as you can see, I'm not up to much. I was just thinking."
    k "I'm one real lucky guy. It’s not often that someone like me gets the chance to turn things around for himself, yet here I am, and for the first time in my life, I feel like…I’m not alone."
    show kirile happy
    k "Ya know, for a while there, I thought you and that other guy had something going on."
    show kirile
    k "I thought for sure you'd go see him instead."
    
    z "Ha! That man is like a block of ice."
    show wzuleika angry hidden
    z "I'm grateful to him for saving me, but I don't think anything could get past that thick shield of his."
    
    k "That thick {i}head{/i}, you mean."
    show kirile happy
    
    "We both laughed, and I was amazed at how easy it was to feel better around him."
    show kirile
    
    show wzuleika happy hidden
    z "You're amazing, Kirile."
    z "You always seem to know just how to cheer me up."
    
    show kirile happy
    k "Of course. That's what I'm here for, you know."
    
    scene bg black with fade
    
    "After laughing and joking for a bit, the two of us headed back to camp."
    "When I went to sleep that night, my head was full of happy, peaceful dreams."
    
    call status from _call_status_4
    jump allchp4AB