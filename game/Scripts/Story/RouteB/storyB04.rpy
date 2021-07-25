# Story B
# Chapter 04: A New Enemy
label allnefferonmissing:
    call status from _call_status_12

    $ show_button_game_menu = False
    stop music
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    
    scene bg castle hallway
    play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
    with fade
    
    "It had been some time since Nefferon called me in to meet with him, but my mind kept turning returning to the events of that day."
    "The man frightened me, and yet...there was something else, something more to him."
    "A deep sadness, perhaps?"
    "I had heard Osirus mention it before, that his younger brother had had an exceptionally rough childhood."
    "Their parents favored Osirus heavily, often ignoring Nefferon completely as they celebrated his brother’s accomplishments instead."
    "Thus, Osirus had felt sorry for him, which is why he had allowed his brother to stay in the castle with him after it was built."
    "To think that a brother’s sympathy would lead to his downfall…"
    
    scene bg throne with fade
    "When I reached the throne room, I was shocked to find that the emperor was not there, nor was he in any of the other places I looked."
    "This didn't seem right…he couldn't have just disappeared."
    "Asking around, I discovered that he hadn't been seen at all that day."
    "Something was definitely wrong, and I was starting to get worried."
        
    menu:
        "Go and find him":
            $ NAffection += 20
            scene bg castle hallway with fade
            "Filled with worry, I left immediately to go find the emperor."
            "Along the way, I passed a familiar face: it was Prince Duren."
            play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
            show duren
            d "Oh, hello, Zuleika."
            show duren sad
            d "Is something wrong?"
            show zuleika sad hidden
            z "Duren, do you happen to know if there's anything wrong with Nef- I mean, His Majesty?"
            show duren
            d "Hmm…no, I don't know of anything in particular."
            d "I know that he's locked himself up in his room all day, but other than that…"
            show duren sad
            d "Why do you ask? Have you heard something?"
            
            z "No, I don't know any more than you, but I'm going to go visit him now."
            
            d "Good luck, then...and be careful."
            hide duren
            stop music
            jump allnefchambers

        "Leave him alone":
            scene bg castle hallway with fade
            "Even though I was a bit worried about him, I decided it wasn't my place to get all worked up over him."
            "He had a whole court of nobles to worry about him, after all..."

            "And if that weren't reason enough to leave him alone, this was quite possibly the man who killed my master.\nWouldn't we all be better off if something did happen to him?"

            u "Oh, there you are, Zuleika."
            play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
            show duren
            "I turned around, surprised, to see my friend, the young Prince Duren."
            show duren sad
            d "I was sent to find you...His Majesty wishes to see you."
            show zuleika sad hidden
            z "Thank you, Duren. I'll go see him right away."
            z "(So much for letting someone else worry about him…)"
            hide duren
            
label allnefchambers:
    scene bg bedroom day
    play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
    with fade
    
    "When I arrived in his chambers, I realized that my worry had been well-deserved."
    show nef sad with dissolve
    "The man before me looked very sick and weak, and was resting in bed. This was completely different from the usual strong, menacing presence of the proud emperor, the one that made my skin crawl."
    "For once, he actually seemed…human, like a normal person. Could this truly be the same man?"
    show nef
    n "My dear Zuleika...I'm so happy to see you."

    show zuleika sad hidden
    z "What happened?\nAre you sick? Do you need a doctor?"
    show nef sad2
    n "This is…punishment."
    show nef
    n "But don't worry yourself, little princess. I've already taken the antidote, so I'll be fine in a few hours."

    z "Antidote…?"
    show zuleika angry hidden
    z "You mean you were poisoned?!"
    show zuleika sad hidden
    z "You said this was punishment…punishment for what?"

    show nef sad2
    "He frowned and averted his gaze, staying like that for several minutes."
    show nef sad
    "Then he looked back at me, staring intently into my eyes."
    n "I'm going to tell you something I haven't told anyone else. You must promise to keep this a secret at all costs, or else both of our lives will be in danger."

    menu:
        "\"I promise.\"":
            $ NAffection += 20
            play music "Audio/Music/Ominous Intro.ogg"
            n "There is a group of gods which controls not only this nation, but the entire continent."

            z "You mean the Great Council?"
            show nef angry
            n "If that were the case, there wouldn't be any suffering in this world."
            show nef sad
            n "No, I'm talking about another group, one which manipulates everything from the shadows."
            n "They are the gods who have been cast out of the Great Council for being too wicked and corrupt, and they are known only as \"The Order.\""
            show nef angry
            n "They are…the incarnation of evil itself."
            play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
            show nef sad
            n "Unfortunately, I've been swept up in their game...a game in which they make all the rules."
            n "Recently, they told me to raise the taxes throughout Tyraca. I tried to tell them that the people couldn't afford to pay anymore, not after all the damage suffered by the war, and…well, you see the result."

            z "That’s horrible."
            show zuleika angry hidden
            z "We have to do something about this. We can't let them keep using you like this, especially at the expense of the people. We have to stop them!"
            
            show nef
            "He looked at me and smiled."
            
            n "Thank you for worrying about me, Princess, but I'm afraid this is one battle we can't win."
            z "We'll find a way to stop them, I swear, for the people…and for you. There has to be a way."

            "I sat there thinking for several minutes, then came up with an idea."
            show zuleika normal hidden
            z "You've been dealing with them for a while, right? Do you know who they are?"
            show nef sad
            n "Yes, for the most part. Why?"

            z "We just have to lure them to the castle, catch them by surprise, and take them out so that they can't hurt anyone else."

            show nef
            n "You are truly amazing, Princess."
            n "You don't even know what you're up against, yet you're determined to fight and defeat them. I can see why they call you \"The Courageous.\""

            "I smiled back, glad to see that his mood had improved."
            show zuleika happy hidden
            z "We {i}will{/i} defeat them, I'm sure of it."
            jump allcastle3

        "\"What could possibly pose a threat to {i}you{/i}?\"":
            show nef angry
            n "Believe it or not, I'm not the one calling the shots here."
            n "...I'm merely a puppet in a much larger scheme, orchestrated by a group much more powerful than I."
            show nef sad
            n "They are...the incarnation of evil itself."
            
            show zuleika angry hidden
            z "More evil than you, even? Wow, that's a shock."
            
            show nef angry
            n "I'm serious, Princess, and if we don't stop them soon, they're going to destroy us all."

            show zuleika sad hidden
            z "I suppose that {i}is{/i} something to worry about..."
            
            "I sat there thinking for several minutes, then came up with an idea."
            show zuleika normal hidden
            z "You've been dealing with them for a while, right? Do you know who they are?"
            show nef sad
            n "Yes, for the most part. Why?"

            z "We just have to lure them to the castle, catch them by surprise, and take them out so that they can't hurt anyone else."

            show nef
            n "You don't even know what you're up against, yet you're determined to fight and defeat them. I can see why they call you \"The Courageous.\""

            show zuleika happy hidden
            z "We {i}will{/i} defeat them, I'm sure of it."
            
label allcastle3:
    if zuleika_type == 'all' or zuleika_type == 'kind':
        $ search6_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament7_done = False
    $ durenchat3_done = False
    $ nefchat3_done = False
    if zuleika_type == 'all' or zuleika_type == 'intelligent':
        $ investigate3_done = False
    
    scene bg castle hallway with fade
    play music "Audio/Music/Skye Cuillin.ogg"
    show zuleika normal hidden
    z "It sounds like Nefferon is feeling better and everything at the castle is back to normal, so I have some free time to spend."

label allcastlemenu3:    
    if energy == 0:
        jump allcastle4
        
    else:
        scene bg castle hallway
        play music "Audio/Music/Skye Cuillin.ogg"
        "What should I do?"
        menu:
            "Visit Duren":
                $ DAffection += 15
                jump allduren_menu3
            "Visit Nefferon":
                $ NAffection += 15
                jump allnefferon_menu3
            "Tidy up":
                scene bg castle hallway
                $ increase_kindness(25)
                $ energy -= 1
                if zuleika_type == 'charming':
                    show zuleika angry hidden
                    z "I tried to clean up my room today, but I think I just made it worse."
                    show zuleika normal hidden
                    z "Guess I'll just have to rely on the maids as usual."
                else:
                    show zuleika normal hidden
                    z "I finally got around to cleaning my room up a bit."
                    show zuleika happy hidden
                    z "I'm sure the maids will appreciate not having to pick up my dirty laundry today."
                jump allcastlemenu3
            "Visit Garden" if zuleika_type == 'all' and search6_done == False or zuleika_type == 'kind' and search6_done == False:
                $ energy -= 1
                $ search6_done = True
                scene bg garden
                play music "Audio/Music/Skye Cuillin.ogg"
                show zuleika happy hidden
                z "This fruit looks delicious!"
                menu:
                    "Pick it up":
                        $ item_fruit += 1
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch6_2
                            "Go back inside":
                                jump allcastlemenu3
                    "Leave it":
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch6_2
                            "Return to castle":
                                jump allcastlemenu3
            "Enter Tournament" if zuleika_type == 'all' and tournament7_done == False or zuleika_type == 'strong' and tournament7_done == False:
                jump alltournament7
            "Search for clues" if zuleika_type == 'all' and investigate3_done == False or zuleika_type == 'intelligent' and investigate3_done == False:
                $ investigative_skill += 50
                $ investigate3_done = True
                $ energy -= 1
                scene bg castle hall with fade
                show zuleika normal hidden
                z "I decided to check out the scene of the crime - Osirus' bedroom - to see what more I could discover."
                show zuleika angry hidden
                z "...What's this?"
                z "It looks like a nasty death threat sent by Lord Dietrich Von Houser..."
                show zuleika sad hidden
                z "If I remember correctly, Osirus had been threatening to revoke Von Houser's lordship if he refused to release his Nalani slaves."
                z "But since Nefferon took the throne, he repealed the law forbidding the use of Nalani slaves, which means that Von Houser was let off the hook..."
                show zuleika angry hidden
                z "In other words, he would have had a lot to gain from taking out Osirus."
                z "And in addition, I do believe that his weapon of choice is a large axe, which may count as a \"large, heavy blade.\""
                show zuleika sad hidden
                z "I'm not sure that he would have had the skill to sneak into the castle, though, let alone have the power to overcome Osirus..."
                jump allcastlemenu3
            "Rest":
                jump allcastle4
                
label allsearch6_2:
    show zuleika happy hidden
    z "Look at these flowers...they're beautiful!"
    menu:
        "Pick them up":
            $ item_flowers += 1
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch6_3
                "Go back inside":
                    jump allcastlemenu3
        "Leave them":
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch6_3
                "Go back inside":
                    jump allcastlemenu3
                    
label allsearch6_3:
    show wzuleika normal hidden
    z "Hey, I found a stone arrowhead. This might come in handy."
    menu:
        "Pick it up":
            $ item_arrowhead += 1
            z "I think that's enough searching for today. It's time to head back inside."
            if durenspecial_done == False:
                jump alldurenspecial2
            else:
                jump allcastlemenu3
        "Leave it":
            z "I think that's enough searching for today. It's time to head back inside."
            if durenspecial_done == False:
                jump alldurenspecial2
            else:
                jump allcastlemenu3
                
label alldurenspecial2:
    $ durenspecial_done = True
    scene bg garden
    play music "Audio/Music/Dreamy Flashback.ogg"
    
    show duren with dissolve
    show zuleika normal hidden
    z "Oh, hey, Duren. I wasn't expecting to see you here."
    show zuleika sad hidden
    z "Is there something wrong?"
    d "No, nothing's wrong. I was just taking a stroll and admiring the flowers."
    d "Which ones are your favorite, Zuleika?"
    
    menu:
        "\"Roses\"":
            $ DAffection += 10
            d "Ah, yes, those can be very beautiful."
            show zuleika happy hidden
            z "Indeed...they're so romantic, don't you think?"
            show duren happy
            d "Of course."
            show duren
            d "Next time I'm in town, I'll buy a bouquet of roses for you."
            z "I'd love that, Duren. Thank you!"
            hide duren
            jump allcastlemenu3
        "\"Irises\"":
            $ DAffection += 20
            show duren happy
            d "Really? Those are my favorite, too."
            show duren
            d "I love the way the petals fall down, like a waterfall...they're so beautiful."
            show zuleika normal hidden
            z "I've never really thought of it that way, but yes, it is a lot like that."
            show duren happy
            d "If I ever find an iris as beautiful as you, I'll be sure to give it to you."
            show zuleika happy hidden
            z "Aww...thank you, Duren. I would love that."
            hide duren
            jump allcastlemenu3
        "\"I don't really like flowers.\"":
            show zuleika angry hidden
            z "That's kind of a girly thing for you to be interested in, anyway, isn't it?"
            z "I keep telling you that you need to man up a bit."
            show duren sad
            d "I know..."
            show duren
            d "But my old mentor liked flowers, too, and he was manly."
            show duren sad
            d "Well...by his culture's standards, anyway..."
            show duren
            d "You should really stop and take a look at them sometime. I find the flowers here to be quite soothing."
            show zuleika normal hidden
            z "...I'll consider it."
            hide duren
            jump allcastlemenu3
            
label allduren_menu3:
    scene bg castle hallway
    show duren with dissolve
    d "Oh, hey. What brings you here?"
    menu:
        "Talk" if durenchat3_done == False:
            $ increase_charm(20)
            $ durenchat3_done = True
            $ energy -= 1
            play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
            jump alldurenchat3
        "Ask to train":
            $ increase_strength(30)
            $ energy -= 1
            hide duren
            if zuleika_type == 'intelligent':
                show zuleika normal hidden
                z "It's a good thing Duren is so patient with me."
                show zuleika angry hidden
                z "I swear I'll get the hang of this whole combat thing eventually..."
                show zuleika sad hidden
                z "...just not today, it seems."
            else:
                show zuleika normal hidden
                z "I had a great time training with Duren today."
                show zuleika happy hidden
                z "He sure is a fun sparring partner."
            jump allcastlemenu3
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ DAffection += 10
                    $ item_bouquet -= 1
                    show duren happy
                    d "These are really beautiful. Thank you, Zuleika."
                    jump allduren_menu3
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ DAffection -= 5
                    $ item_makeup -= 1
                    show duren angry
                    d "Why are you giving this to me?"
                    jump allduren_menu3
                "Miraculous Moonshine" if item_liquor > 0:
                    $ DAffection -= 5
                    $ item_liquor -= 1
                    show duren sad
                    d "I don't like this..."
                    jump allduren_menu3
                "Secret Stealth Knives" if item_knives > 0:
                    $ DAffection += 5
                    $ item_knives -= 1
                    show duren happy
                    d "These might come in handy. Thanks, Zuleika."
                    jump allduren_menu3
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ DAffection += 1
                    $ item_spellbook -= 1
                    show duren
                    d "This is...interesting. Thanks."
                    jump allduren_menu3
                "Elegant Earrings" if item_earrings > 0:
                    $ DAffection += 1
                    $ item_earrings -= 1
                    show duren
                    d "These are nice. Thanks."
                    jump allduren_menu3
                "Wild flowers" if item_flowers > 0:
                    $ DAffection += 5
                    $ item_flowers -= 1
                    show duren happy
                    d "These are pretty. Thanks, Zuleika."
                    jump allduren_menu3
                "Turtle shell" if item_shell > 0:
                    $ DAffection += 10
                    $ item_shell -= 1
                    show duren happy
                    d "This is really cool. Thank you, Zuleika."
                    jump allduren_menu3
                "Herbs" if item_herbs > 0:
                    $ DAffection += 5
                    $ item_herbs -= 1
                    show duren happy
                    d "These might come in handy. Thanks, Zuleika."
                    jump allduren_menu3
                "Stone arrowhead" if item_arrowhead > 0:
                    $ DAffection += 10
                    $ item_arrowhead -= 1
                    show duren happy
                    d "This is really cool. Thank you, Zuleika."
                    jump allduren_menu3
                "Fruit" if item_fruit > 0:
                    $ DAffection += 1
                    $ item_fruit -= 1
                    show duren
                    d "This is nice. Thanks."
                    jump allduren_menu3
                "Gold coin" if item_coin > 0:
                    $ DAffection += 5
                    $ item_coin -= 1
                    show duren happy
                    d "This might come in handy. Thanks, Zuleika."
                    jump allduren_menu3
                "Nevermind":
                    jump allduren_menu3
        "Nevermind":
            jump allcastlemenu3
            
label allnefferon_menu3:
    scene bg throne with fade
    show nef with dissolve
    n "Your presence always brightens my day, Princess."
    menu:
        "Talk" if nefchat3_done == False:
            $ increase_charm(20)
            $ nefchat3_done = True
            $ energy -= 1
            play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
            jump allnefferonchat3
        "Discuss politics":
            $ increase_intelligence(30)
            $ energy -= 1
            play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
            hide nef
            if zuleika_type == 'strong':
                show zuleika sad hidden
                z "I never knew that peace treaties were so complicated..."
                show zuleika angry hidden
                z "Why can't everyone just get along?"
            else:
                show zuleika sad hidden
                z "I never knew that peace treaties were so complicated and difficult to maintain."
                show zuleika angry hidden
                z "When each party has its own interests in mind, it's hard to come to a compromise and to convice the other parties to keep their promises..."
                show zuleika sad hidden
                z "I suppose that's why treaties are sometimes broken, as unfortunate as it is."
                z "Why can't we all just get along?"
            jump allcastlemenu3
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ NAffection -= 5
                    $ item_bouquet -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu3
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ NAffection += 10
                    $ item_makeup -= 1
                    show nef happy
                    n "This will be very useful to me. Thank you, Princess."
                    jump allnefferon_menu3
                "Miraculous Moonshine" if item_liquor > 0:
                    $ NAffection += 5
                    $ item_liquor -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu3
                "Secret Stealth Knives" if item_knives > 0:
                    $ NAffection += 1
                    $ item_knives -= 1
                    show nef
                    n "I don't have much use for these, but thank you."
                    jump allnefferon_menu3
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ NAffection += 5
                    $ item_spellbook -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu3
                "Elegant Earrings" if item_earrings > 0:
                    $ NAffection += 10
                    $ item_earrings -= 1
                    show nef happy
                    n "This will be very useful to me. Thank you, Princess."
                    jump allnefferon_menu3
                "Wild flowers" if item_flowers > 0:
                    $ NAffection -= 5
                    $ item_flowers -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu3
                "Turtle shell" if item_shell > 0:
                    $ NAffection -= 5
                    $ item_shell -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu3
                "Herbs" if item_herbs > 0:
                    $ NAffection += 1
                    $ item_knives -= 1
                    show nef
                    n "I don't have much use for these, but thank you."
                    jump allnefferon_menu3
                "Stone arrowhead" if item_arrowhead > 0:
                    $ NAffection -= 5
                    $ item_arrowhead -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu3
                "Fruit" if item_fruit > 0:
                    $ NAffection += 5
                    $ item_fruit -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu3
                "Gold coin" if item_coin > 0:
                    $ NAffection += 10
                    $ item_coin -= 1
                    show nef happy
                    n "Gold never loses its value; this is an excellent gift. Thank you, Princess."
                    jump allnefferon_menu3
                "Nevermind":
                    jump allnefferon_menu3
        "Nevermind":
            jump allcastlemenu3
            
label alldurenchat3:
    show duren
    d "You know, Zuleika, you're not like the other girls. You're more like a guy."
    show duren sad
    d "Wait...no, that's not what I mean."
    show duren
    d "I mean that I can talk to you freely as if you're not a girl."
    show duren sad
    d "Wait...that didn't come out right, either."
    d "What I mean is..."
    show zuleika happy hidden
    z "It's alright, Duren, I think I know what you're trying to say."
    show duren sad
    d "You do?"
    menu:
        "\"Of course!\"":
            $ DAffection += 20
            show zuleika normal hidden
            z "I'm glad that you feel so comfortable around me."
            show zuleika happy hidden
            z "I feel the same way around you."
            show duren happy
            d "I'm so happy to hear that."
            show duren
            d "I hope our friendship continues for a long time to come."
            show zuleika normal hidden
            z "I'm sure it will."
            hide duren
            jump allcastlemenu3
        "\"Yeah, I like boys, too.\"":
            show zuleika happy hidden
            z "I didn't know you swung that way, though. Good for you."
            show duren sad
            d "But I...uh...that's not..."
            d "...Oh, nevermind."
            hide duren with moveoutleft
            jump allcastlemenu3
            
label allnefferonchat3:
    show zuleika normal hidden
    z "I must admit...you're not what I expected."
    show nef
    n "Oh? How so?"
    menu:
        "\"You're not such a bad guy after all, Neffy.\"":
            play music "Audio/Music/One-Eyed Maestro (Nefferon Theme).ogg"
            $ NAffection += 20
            n "...\"Neffy\"?"
            show zuleika happy hidden
            z "\"Nefferon\" sounds too...sinister, so I'll call you \"Neffy\" instead."
            n "I'm honored to receive such a cute pet name from you, Princess..."
            show nef angry
            n "...but never call me that again."
            show zuleika sad hidden
            z "Aww...you're no fun."
            hide nef
            jump allcastlemenu3
        "\"You're even more of a villain than I thought.\"":
            play music "Audio/Music/Crisis (Nefferon Theme).ogg"
            $ NAffection -= 50
            show nef angry
            n "As I've explained -"
            show zuleika angry hidden
            z "You actually expect me to feel sorry for you?"
            z "Regardless of who's on top, you're still responsible for your actions..."
            show zuleika sad hidden
            z "...just as I am responsible for the lives {i}I{/i} helped destroy, even though I was only following orders."
            show zuleika angry hidden
            z "If you're really as \"innocent\" in all of this as you claim, then step up and do something to stop it."
            z "Otherwise...you're just as bad as the Order themselves."
            n "I think that's enough of your insubordinance for today. Get out."
            z "Gladly."
            hide nef
            jump allcastlemenu3
            
label alltournament7:
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
            
            jump alltournament7_choice
            
        "How to Play":
            an "New to the tournament? Don't worry, it's easy to play!"
            an "Each round, you are given three choices: Attack, Defend, or Forfeit."
            an "Attack means that you throw an offensive attack at your enemy, but be careful because they'll attack you back with the same amount of force!"
            an "Defend means that you let the enemy attack first, but they do much less damage than they normally would. Then you get a chance to counterattack, but with less power than a normal attack."
            an "Forfeit means quitting the battle. You're advised to do so if you're about to lose."
            an "The more battles you fight in the tournament, the more battle skill you'll gain, so make sure to enter at every opportunity!"
            
            jump alltournament7
            
        "Return to Castle":
            stop music
            jump allcastlemenu3
            
label alltournament7_choice:
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
                
            jump alltournament7_choice
            
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
                
            jump alltournament7_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    jump alltournament7
                "No":
                    jump alltournament7_choice
                    
label alltournament7win:
    stop music
    scene bg black with fade
    $ energy -= 1
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb happy with dissolve
    an "Congratulations on winning the third round!\nYour prize is 750 Gold!"
    $ gold += 750
    show vboyb normal
    an "That's all for today, but don't forget that the tournament is being held across the nation, so you can compete in any town."
    an "Good luck!"
    
    $ battle_skill += 50
    $ tournament7_done = True
    stop music
    hide vboyb
    jump allcastlemenu3
    
label alltournament7lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament7
            
        "Return to Castle":
            jump allcastlemenu3
            
label allcastle4:
    if zuleika_type == 'all' and investigative_skill > 130 or zuleika_type == 'intelligent' and investigative_skill > 130:
        stop music
        scene bg hallway night with fade
        "After nightfall, I decided it was time for some additional snooping."
        "I had a good idea of who Osirus' murderer was, but I had to be sure..."
        "However, I was stopped by an unexpected visitor."
        play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
        show nef with dissolve
        n "Good evening, Princess. It's dangerous to wander around the halls unescorted at this time of night."
        show zuleika sad hidden
        z "...I was just heading back to my room, actually."
        n "Oh? But you seem to be headed in the opposite direction. Are you lost?"
        show zuleika happy hidden
        z "...Yes, yes, that must be it. It's so dark that I must have taken a wrong turn somewhere."
        play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"
        n "You're a terrible liar, little princess."
        show zuleika sad hidden
        z "What do you mean? I was just lost, really..."
        n "I know all about your little investigation into my brother's death."
        n "What, may I ask, have you uncovered?"
            
        menu:
            "\"It was you!\"":
                show nef angry
                n "How dare you make such accusations at me?"
                show zuleika angry hidden
                z "It's true, though, isn't it?"
                z "You're the only one who had the means and the access to reach Osirus' chambers, and the only one powerful enough to overtake him."
                z "In addition, Osirus was killed by a large blade, which matches the description of your Blade of Anguish perfectly."
                z "You killed your own flesh and blood, you murderer!"
                show nef happy
                
                scene nef violent hallway with dissolve
                $ persistent.nefviolenthallway = True
                "Nefferon smirked and forcefully pulled me to him."
                n "I have to admit...you surprised me, Princess. I didn't expect you to figure it out."
                n "It's been fun, but I think it's about time to shut that loud mouth of yours."
                if NAffection > 250:
                    show zuleika sad hidden
                    z "I know why you did it..."
                    scene bg hallway night with dissolve
                    show nef sad with dissolve
                    show zuleika sad hidden
                    z "Always living in the shadow of your brother...it must have been hard on you."
                    z "Your secret is safe with me, I promise."
                    n "...Thank you for understanding..."
                    "He let me go and disappeared as quickly as he had come."
                    jump allchp5B
                else:
                    show zuleika angry hidden
                    z "You can kill me if you like, but I already gave all of my findings to Duren. If you kill me now, he'll {i}know{/i} it was you."
                    n "Everyone thinks I was the one who killed Osirus, anyway, yet they haven't done a thing. Why? Because I'm the emperor; I'm untouchable."
                    show zuleika normal hidden
                    z "You said yourself that those rumors have hurt your ability to rule...let me live, and I'll tell Duren and the rest of the High Court that it was Lord Von Houser instead."
                    scene bg hallway night with dissolve
                    show nef angry with dissolve
                    n "...You would do that for me, Princess?"
                    
                    show zuleika normal hidden
                    z "I would, but I can only do so if you let me go."
                    n "...Very well, but if you betray me, I will have your head."
                    stop music
                    scene bg bedroom with fade
                    play music "Audio/Music/A Mission.ogg"
                    show duren sad with dissolve
                    d "Zuleika, where have you been? I came here looking for you, but you were nowhere to be found..."
                    show zuleika sad hidden
                    z "Duren! I need your help."
                    $ DAffection += 20
                    z "Nefferon was the one who killed Osirus, I'm sure of it."
                    d "Well, that's what the rumors say, but..."
                    show zuleika angry hidden
                    z "No, I mean that I have proof...and a confession."
                    show duren angry
                    d "Seriously? I knew it had to have been him!"
                    show zuleika angry hidden
                    z "I need you to talk to the leaders of Royal Guard and explain the situation to them, but keep all of this as quiet as possible until I say otherwise, okay?"
                    show duren
                    d "Got it."
                    z "We're going to take that man down, once and for all."
                    $ NAffection -= 50
                    jump allchp5B
                
            "\"It was Lord Von Houser!\"":
                $ NAffection += 20
                show nef angry
                n "I had a feeling it was him."
                n "I thought he was a little too happy when Osirus' death was announced..."
                show nef
                n "Thank you for the information, Princess. I'll see to it that Von Houser is properly punished for his crimes."
                show zuleika normal hidden
                z "Thank you, Your Majesty."
                jump allchp5B
                
            "\"...I don't know who it was.\"":
                show nef angry
                n "Hmph."
                n "That's probably for the best, anyway."
                show nef
                n "Next time, Princess, you should leave the detective work to professionals."
                show zuleika sad hidden
                z "...Yes, Your Majesty."
    else:
        jump allchp5B