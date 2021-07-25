# Story B
# Chapter 01: Meeting the Emperor
label allchp1B:
    $ show_button_game_menu = False
    if zuleika_type == 'all':
        $ energy = 5
    else:
        $ energy = 3
    stop music
    scene bg castle hall with fade
    
    "The next morning, I requested to have an audience with the ruler of the new Neffronian Empire, Emperor Nefferon himself."
    "Though my decision was firm, I couldn't help but feel uneasy about the meeting."
    "This was the man who supposedly killed his own brother for the throne, and he had an unnerving reputation as a cruel, manipulative man."
    "I was determined not to let this stop me, however, and I forced myself to put on my bravest smile before entering the throne room."
    
    scene bg throne
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    with fade
    
    show nef with dissolve
    n "Good morning, Princess. Did you sleep well?"
    
    "I bowed, remembering my new, lowly status."
    show zuleika normal hidden
    z "...Yes, Your Majesty. I slept...wonderfully."

    n "I'm glad to hear it, but please, there is no need for you to bow your humble head to me."
    n "In your stunning presence, I am but an average man."
    n "...I assume that this is about my offer, yes?"
    "I nodded silently."
    n "Then, what do you say, little princess?\nWill you stay by my side?"
    
    menu:
        "\"Yes, Your Majesty.\"":
            $ NAffection += 20
            jump allyesmajesty
        "\"What would happen if I said no?\"":
            "Even as I tried to stand firm and look defiant, I knew it was a daring move to ask such a question."
            "One didn't say \"no\" to the emperor lightly."
            "Rather than getting angry as I expected, Nefferon kept his composure and merely smiled."
            show nef happy
            n "I believe we both know what will happen if you refuse my offer." 
            show nef
            n "Osirus is dead, the High Court has abandoned you, and with a word, I could have you killed right here and now without anyone knowing."
            n "No one would search for you, a mere angel, fallen without her dear master."

            "It was all true, and we both knew it." 
            "If I valued my life at all, I had no other choice but to accept the emperor's offer."
            
            show zuleika sad hidden
            z "Yes, Your Majesty."
            
label allyesmajesty:
    "Fear slowly crept up my spine."
    "There was no telling what he may order me to do, and my mind immediately leapt to the worst possible scenarios, but there was no turning back now."
    show nef happy
    n "Good, I'm glad."
    show nef
    n "For your first assignment, I would like you to...sing for me. It doesn't matter what you sing; I just want to hear your voice."

    "I stood there for a moment, puzzled."
    "This was not what I expected from a man known for his cruelty. Was he messing with me?"

    n "Please, little princess, sing a song for me, any song."
    stop music
    
    play music "Audio/Music/Private Reflection.ogg"
    "Not knowing what else to do or what to expect, I did as the emperor asked…"
    with Pause(2)
    "...I sang."
    scene bg black with fade
    with Pause(1)
    stop music
    
    scene bg castle hallway with fade
    play music "Audio/Music/Skye Cuillin.ogg"
    
    show zuleika normal hidden
    z "Now that I'm done with my service to the emperor for the day, I have some free time before nightfall."
    z "I can talk to Duren to earn Charm or ask him to train me for Strength."
    z "If I really want to, I can even talk to Nefferon to earn Charm or discuss politics for Intelligence."
    z "If I'm in a helpful mood, I can tidy up around the castle and earn Kindness points."
    z "I can even go outside and look around the garden."
    z "When I'm ready to move on, I can rest."
    
    if zuleika_type == 'all' or zuleika_type == 'kind':
        $ search4_done = False
    $ durenchat1_done = False
    $ nefchat1_done = False
    if zuleika_type == 'all' or zuleika_type == 'intelligent':
        $ confront_done = False
    
label allcastlemenu1:    
    if energy == 0:
        jump allchp2B
        
    else:
        scene bg castle hallway
        play music "Audio/Music/Skye Cuillin.ogg"
        "What should I do?"
        menu:
            "Visit Duren":
                play music "Audio/Music/Skye Cuillin.ogg"
                $ DAffection += 15
                jump allduren_menu1
            "Visit Nefferon":
                play music "Audio/Music/Skye Cuillin.ogg"
                $ NAffection += 15
                jump allnefferon_menu1
            "Tidy up":
                scene bg castle hallway
                play music "Audio/Music/Skye Cuillin.ogg"
                $ increase_kindness(25)
                $ energy -= 1
                show zuleika angry hidden
                z "I hate it when the maids give me a hard time about helping out around the castle."
                z "\"You're a princess; you're not supposed to work!\""
                if zuleika_type == 'charming':
                    show zuleika sad hidden
                    z "...Now that I've actually tried, I believe them."
                else:
                    show zuleika normal hidden
                    z "Regardless, it was good for me."
                    z "There's nothing like a bit of manual labor to help clear your head."
                jump allcastlemenu1
            "Visit Garden" if zuleika_type == 'all' and search4_done == False or zuleika_type == 'kind' and search4_done == False:
                $ energy -= 1
                $ search4_done = True
                scene bg garden
                play music "Audio/Music/Skye Cuillin.ogg"
                show zuleika happy hidden
                z "Look at these flowers...they're beautiful!"
                menu:
                    "Pick them up":
                        $ item_flowers += 1
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch4_2
                            "Go back inside":
                                jump allcastlemenu1
                    "Leave them":
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch4_2
                            "Go back inside":
                                jump allcastlemenu1
            "Rest":
                jump allchp2B
                
label allsearch4_2:
    show zuleika happy hidden
    z "This fruit looks delicious!"
    menu:
        "Pick it up":
            $ item_fruit += 1
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch4_3
                "Go back inside":
                    jump allcastlemenu1
        "Leave it":
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch4_3
                "Go back inside":
                    jump allcastlemenu1
                    
label allsearch4_3:
    show zuleika normal hidden
    z "Oh hey, I found a gold coin. I doubt I could use this to pay with, though."
    menu:
        "Pick it up":
            $ item_coin += 1
            z "I think that's enough searching for today. It's time to head back inside."
            jump allcastlemenu1
        "Leave it":
            z "I think that's enough searching for today. It's time to head back inside."
            jump allcastlemenu1
            
label allduren_menu1:
    scene bg castle hallway
    show duren with dissolve
    d "Hello, Zuleika. How are you today?"
    menu:
        "Talk" if durenchat1_done == False:
            $ increase_charm(20)
            $ durenchat1_done = True
            $ energy -= 1
            play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
            jump alldurenchat1
        "Ask to train":
            $ increase_strength(30)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
            $ energy -= 1
            if zuleika_type == 'intelligent':
                show duren sad
                d "Um...Zuleika?"
                show zuleika angry hidden
                z "What is it, Duren?\nI'm a bit busy here with these sword exercises..."
                d "It's just that...well...don't take this the wrong way..."
                z "Yes?"
                z "(*grumble* Dang sword...cut the stupid wood already!)"
                d "...You're supposed to take the sword out of its sheath first."
                show zuleika sad hidden
                z "Oh..."
                show zuleika angry hidden
                z "Why didn't you say that earlier?"
                d "...Sorry."
            else:
                show duren
                d "Oh, so you swing the sword like this...?"
                d "That's a pretty interesting technique."
                show zuleika happy hidden
                z "I know, right?"
                show zuleika normal hidden
                z "I can't wait to try it out sometime."
                d "I feel sorry for whoever happens to be on the other end."
            hide duren
            stop music
            jump allcastlemenu1
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ DAffection += 10
                    $ item_bouquet -= 1
                    show duren happy
                    d "These are really beautiful. Thank you, Zuleika."
                    jump allduren_menu1
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ DAffection -= 5
                    $ item_makeup -= 1
                    show duren angry
                    d "Why are you giving this to me?"
                    jump allduren_menu1
                "Miraculous Moonshine" if item_liquor > 0:
                    $ DAffection -= 5
                    $ item_liquor -= 1
                    show duren sad
                    d "I don't like this..."
                    jump allduren_menu1
                "Secret Stealth Knives" if item_knives > 0:
                    $ DAffection += 5
                    $ item_knives -= 1
                    show duren happy
                    d "These might come in handy. Thanks, Zuleika."
                    jump allduren_menu1
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ DAffection += 1
                    $ item_spellbook -= 1
                    show duren
                    d "This is...interesting. Thanks."
                    jump allduren_menu1
                "Elegant Earrings" if item_earrings > 0:
                    $ DAffection += 1
                    $ item_earrings -= 1
                    show duren
                    d "These are nice. Thanks."
                    jump allduren_menu1
                "Wild flowers" if item_flowers > 0:
                    $ DAffection += 5
                    $ item_flowers -= 1
                    show duren happy
                    d "These are pretty. Thanks, Zuleika."
                    jump allduren_menu1
                "Turtle shell" if item_shell > 0:
                    $ DAffection += 10
                    $ item_shell -= 1
                    show duren happy
                    d "This is really cool. Thank you, Zuleika."
                    jump allduren_menu1
                "Herbs" if item_herbs > 0:
                    $ DAffection += 5
                    $ item_herbs -= 1
                    show duren happy
                    d "These might come in handy. Thanks, Zuleika."
                    jump allduren_menu1
                "Stone arrowhead" if item_arrowhead > 0:
                    $ DAffection += 10
                    $ item_arrowhead -= 1
                    show duren happy
                    d "This is really cool. Thank you, Zuleika."
                    jump allduren_menu1
                "Fruit" if item_fruit > 0:
                    $ DAffection += 1
                    $ item_fruit -= 1
                    show duren
                    d "This is nice. Thanks."
                    jump allduren_menu1
                "Gold coin" if item_coin > 0:
                    $ DAffection += 5
                    $ item_coin -= 1
                    show duren happy
                    d "This might come in handy. Thanks, Zuleika."
                    jump allduren_menu1
                "Nevermind":
                    jump allduren_menu1
        "Nevermind":
            jump allcastlemenu1
            
label allnefferon_menu1:
    scene bg throne with fade
    show nef with dissolve
    n "Back so soon, Princess?"
    menu:
        "Talk" if nefchat1_done == False:
            $ increase_charm(20)
            $ nefchat1_done = True
            $ energy -= 1
            play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
            jump allnefferonchat1
        "Discuss politics":
            $ increase_intelligence(30)
            $ energy -= 1
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
            jump allcastlemenu1
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ NAffection -= 5
                    $ item_bouquet -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu1
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ NAffection += 10
                    $ item_makeup -= 1
                    show nef happy
                    n "This will be very useful to me. Thank you, Princess."
                    jump allnefferon_menu1
                "Miraculous Moonshine" if item_liquor > 0:
                    $ NAffection += 5
                    $ item_liquor -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu1
                "Secret Stealth Knives" if item_knives > 0:
                    $ NAffection += 1
                    $ item_knives -= 1
                    show nef
                    n "I don't have much use for these, but thank you."
                    jump allnefferon_menu1
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ NAffection += 5
                    $ item_spellbook -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu1
                "Elegant Earrings" if item_earrings > 0:
                    $ NAffection += 10
                    $ item_earrings -= 1
                    show nef happy
                    n "This will be very useful to me. Thank you, Princess."
                    jump allnefferon_menu1
                "Wild flowers" if item_flowers > 0:
                    $ NAffection -= 5
                    $ item_flowers -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu1
                "Turtle shell" if item_shell > 0:
                    $ NAffection -= 5
                    $ item_shell -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu1
                "Herbs" if item_herbs > 0:
                    $ NAffection += 1
                    $ item_knives -= 1
                    show nef
                    n "I don't have much use for these, but thank you."
                    jump allnefferon_menu1
                "Stone arrowhead" if item_arrowhead > 0:
                    $ NAffection -= 5
                    $ item_arrowhead -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu1
                "Fruit" if item_fruit > 0:
                    $ NAffection += 5
                    $ item_fruit -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu1
                "Gold coin" if item_coin > 0:
                    $ NAffection += 10
                    $ item_coin -= 1
                    show nef happy
                    n "Gold never loses its value; this is an excellent gift. Thank you, Princess."
                    jump allnefferon_menu1
                "Nevermind":
                    jump allnefferon_menu1
        "Confront about Osirus" if zuleika_type == 'all' and confront_done == False or zuleika_type == 'intelligent' and confront_done == False:
            play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"
            $ investigative_skill += 50
            $ confront_done = True
            $ energy -= 1
            jump allmystery1
        "Nevermind":
            jump allcastlemenu1
    
label alldurenchat1:
    show zuleika happy hidden
    z "You're so funny, Duren."
    show duren sad
    d "Huh? Me?"
    show zuleika normal hidden
    show duren
    z "Yes, you."
    z "You're always so shy and polite...except when you're angry."
    z "Then you're strong and confident, and it's like you're a whole different person."
    show duren
    d "Managing my anger is one lesson I always failed. Lord Chael, my mentor, would scold me whenever I got like that while we were training."
    d "As a Nalani, he believed in keeping one's emotions hidden at all times. It's a way of deceiving the enemy...or so he told me."
    menu:
        "\"He sounds like a smart man.\"":
            $ DAffection += 20
            show duren happy
            d "Oh, he is."
            show duren sad
            d "It's unfortunate that we can't continue our lessons anymore."
            show zuleika sad hidden
            z "Why is that?"
            d "My master forbid it once he took the throne..."
            show duren angry
            d "Honestly, I bet it's just because he's afraid that I'll get too strong and overthrow him."
            show zuleika happy hidden
            z "There you go, losing your temper again."
            show duren sad
            d "Oops..."
            jump allcastlemenu1
        "\"That guy sounds like a total weirdo...\"":
            show duren sad
            d "Well, he's not."
            d "Contrary to popular belief, Nalani aren't that different from the rest of us."
            d "Anyway, he's a great mentor...or, at least he was before my master forbid me from seeing him again."
            show zuleika sad hidden
            z "I'm sorry to hear that, Duren."
            show zuleika normal hidden
            z "I know it's not much consolation, but I'm here to train with you whenever you like."
            show duren
            d "Thank you for the offer, Zuleika, but I think training with you would do more harm than good..."
            show zuleika angry hidden
            z "Hey, what's that supposed to mean?"
            stop music
            jump allcastlemenu1
            
label allnefferonchat1:
    show nef
    n "I heard that there was quite a commotion going on in your room last night."
    show zuleika sad hidden
    z "Yes...though I'm sure you've already heard all the reports."
    show nef angry
    n "I have, and don't worry, Princess."
    n "The useless guards who allowed that {i}vermin{/i} to get to you have been properly dealt with."
    menu:
        "\"Thank you, Your Majesty.\"":
            $ NAffection += 20
            play music "Audio/Music/One-Eyed Maestro (Nefferon Theme).ogg"
            show nef happy
            n "Your gratitude flatters me, little princess."
            show nef
            n "I {i}was{/i} going to have you pay for those window replacements yourself, but since you've been so polite, I suppose I could let you off the hook this time."
            "I bowed graciously, even though I was a little annoyed that he was even thinking of making me pay for damages that weren't my doing."
            show zuleika normal hidden
            z "You're...very kind, Your Majesty."
            n "Of course I am. Now run along before I change my mind."
            jump allcastlemenu1
        "\"Dealt with how exactly?\"":
            n "That is none of your concern."
            show nef
            n "Oh, and by the way, those windows cost 50,000 Gold each.\nI'll be expecting you to pay for the replacements since it was you, after all, that he was after."
            show zuleika angry hidden
            z "What?! You've got to be kidding me! I don't even have any money...you took it all already, remember?"
            show nef angry
            n "I never kid, Princess."
            show nef
            n "Now then, run along. I have work to do."
            stop music
            jump allcastlemenu1
            
label allmystery1:
    show nef sad
    n "It really is a shame what happened to my brother..."
    show zuleika angry hidden
    z "What are you upset about? You were the one who made it happen."
    show nef angry
    n "Don't tell me you actually believed those silly rumors."
    z ". . ."
    show nef
    n "If you stop and think about it for a moment, you'll see that I would have gained nothing from killing Osirus."
    show nef angry
    n "Even just having this rumor circulating is doing enough to damage my reputation."
    show nef sad
    n "It's true that my brother and I didn't get along, and it's also true that I wanted to take the throne for myself."
    show nef angry
    n "However, to get here in such a way would not have been my preferred course of action."
    n "I managed to bribe several nobles into supporting me, as I'm sure you've figured out, but there are more - many of whom are much more influential - who remain loyal to Osirus."
    n "Since they believe that I was the one who killed their beloved monarch, they've come to outright oppose me."
    n "The same goes for many of Osirus' soldiers and guards; they refuse to serve the man who supposedly killed their leader."
    show nef sad
    n "How am I supposed to rule effectively when my people are against me?"
    n "So, you see, I had nothing to gain from killing my brother."
    n "I may have wanted the throne, but...not like this."
    show zuleika sad hidden
    z "(Hmm...he has a point. If he didn't kill him, though, then who did?)"
    z "(I guess it's up to me to find out.)"
    stop music
    jump allcastlemenu1