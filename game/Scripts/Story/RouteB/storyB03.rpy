# Story B
# Chapter 03: Jealousy
label allchp3B:
    call status from _call_status_11

    $ show_button_game_menu = False
    
    stop music
    
    scene bg castle hall with fade
    "A week after my visit to the village, Nefferon called me in to have a meeting with him."

    scene bg throne with fade
    show nef angry with dissolve
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    "When I entered, I was surprised to see that the emperor's usual smirk had been replaced by a frown."
    "What could have upset him?"
    
    n "You and my pet seem very...close."
    
    "I had a bad feeling and suddenly wondered where Duren was; I hadn't seen him for several days."
    "I looked steadily at the emperor, trying to figure out what he was thinking."
    
    show zuleika sad hidden
    z "We're friends, yes, as a result of circumstance."
    
    show nef sad
    n "I see..."
    
    menu:
        "\"Where is he?!\"":
            $ DAffection += 20
            play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"
            show nef angry
            "The question, along with the anger and fear in my voice, seemed to strike an almost physical blow to the emperor."

            n "Why do you want to know?"
            n "That boy doesn’t matter; he's worthless. {i}I{/i} am the emperor, {i}I{/i} am the one with worth."
            n "Don't I matter more than him?"

            show zuleika angry hidden
            z "You may think he's worthless, but Duren is important to me, and I want to know what you've done with him!"

            "The two of us glared at each other for what seemed like hours, but Nefferon was the first to snap."
            n "Get out!"
            n "Go, get out! I don't want to look at your wretched face anymore."

            "I knew what would happen if I stayed there any longer – he would have me killed right then and there – so I ran out, determined to find Duren."
            
            stop music
            jump alldungeon

        "\"If that upsets you...\"":
            $ NAffection += 20
            show nef sad
            n "I apologize, little princess...I just get jealous easily. It's one of my worst flaws."
            show zuleika normal hidden
            z "I promise that nothing is going on between Duren and I. We're just friends."
            show nef
            n "I'm relieved to hear that."
            show zuleika sad hidden
            z "Where is he, by the way?"
            n "Oh, I sent him off to run some errands for me. He should be back later today."
            "I was secretly glad to hear that Nefferon hadn't done anything to hurt him. He was, after all, my best friend..."
            "After a moment of looking at me intently, he motioned for me to leave."
            n "You may go now, but come to my chambers tonight…I want to hear you sing again."
            
            jump allcastle2
            
label alldungeon:
    scene bg castle hallway with fade
    "After asking around, I discovered that Duren had been locked up in the dungeon."

    "Luckily, most of the guards in the castle still owed their allegiance to Osirus, and therefore his angel as well, so when I told the dungeon guards the situation, they let me pass freely."
    scene bg dungeon with fade
    
    show duren sad with dissolve
    play music "Audio/Music/Lasting Hope (Sad Duren Theme).ogg"
    "I gasped when I saw Duren; he was covered in cuts and bruises and looked like he hadn't eaten in at least a day."
    "He looked surprised to see me, but his pain and sadness were apparent."

    d "Zuleika…I'm sorry you had to see me like this."
    d "What are you doing here?"
    show zuleika sad hidden
    z "I came to save you, of course."
    z "Come on, let's get you out of here. You can hide out in my room for the time being."
    
    scene bg bedroom with fade
    play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
    show duren sad with dissolve
    "Once we arrived at my bedroom, I began dressing his wounds in silence."

    "After several minutes, I finally gathered the courage to ask the question that was plaguing my mind."
    show zuleika sad hidden
    z "Duren, what happened to you?"
    $ DAffection += 20

    show duren
    d "Oh, this…it's nothing."

    show duren sad
    z "This isn’t \"nothing,\" Duren; it's really serious."
    show zuleika angry hidden
    z "Did he…Did Nefferon do this to you?"

    show duren sad2
    "The young man looked away, avoiding my worried look."
    d "He doesn't like it when other people touch his things."
    z "(Since when did I become \"his thing?\")"

    show zuleika sad hidden
    z "We have to do something about this."
    z "I…I care about you, Duren, I really do, and I don't want to see you hurt like this."
    show zuleika angry hidden
    z "That man has no right to treat you this way."
    
    show duren happy
    "The young man suddenly smiled, surprising me."

    d "Thank you, Zuleika."
    d "Thank you for worrying about me…it means a lot."

    "Seeing him smile, even in this condition, reminded me to smile, too."
    "So I smiled, not for myself, but for the brave young man in front of me, to encourage him to keep fighting."
    
    stop music
    scene bg black with fade
    with Pause(.5)
    
label allcastle2:
    if zuleika_type == 'all' or zuleika_type == 'kind':
        $ durenspecial_done = False
        $ search5_done = False
    if zuleika_type == 'all' or zuleika_type == 'strong':
        $ tournament6_done = False
    $ durenchat2_done = False
    $ nefchat2_done = False
    if zuleika_type == 'all' or zuleika_type == 'intelligent':
        $ investigate2_done = False
    
    scene bg castle hallway
    play music "Audio/Music/Skye Cuillin.ogg"
    with fade
    
    show zuleika normal hidden
    z "Once again, I have some free time before nightfall."
    if zuleika_type == 'all' or zuleika_type == 'kind':
        z "I can either visit Duren, visit Nefferon, tidy up around the castle, or visit the garden."
    else:
        z "I can either visit Duren, visit Nefferon, or tidy up around the castle."
    if zuleika_type == 'all' or zuleika_type == 'strong':
        z "I can also sneak out of the castle and enter the Tournament in town."
    if zuleika_type == 'all' or zuleika_type == 'intelligent':
        z "Or I can even search the castle for clues."
    
label allcastlemenu2:    
    if energy == 0:
        jump allchp4B

    else:
        scene bg castle hallway
        play music "Audio/Music/Skye Cuillin.ogg"
        menu:
            "Visit Duren":
                $ DAffection += 15
                jump allduren_menu2
            "Visit Nefferon":
                $ NAffection += 15
                jump allnefferon_menu2
            "Tidy up":
                scene bg castle hallway
                $ increase_kindness(25)
                $ energy -= 1
                if zuleika_type == 'charming':
                    show zuleika normal hidden
                    z "I spent ten minutes sweeping the floors and brushing away cobwebs..."
                    show zuleika angry hidden
                    z "...and then I gave up. I have better things to do with my time."
                else:
                    show zuleika normal hidden
                    z "I spent several hours sweeping the floors and brushing away cobwebs."
                    z "Though it wasn't the easiest work, the castle looks much cleaner now."
                jump allcastlemenu2
            "Visit Garden" if zuleika_type == 'all' and search5_done == False or zuleika_type == 'kind' and search5_done == False:
                $ energy -= 1
                $ search5_done = True
                scene bg garden
                play music "Audio/Music/Skye Cuillin.ogg"
                show zuleika normal hidden
                z "I managed to find some good-looking herbs growing nearby."
                menu:
                    "Pick them up":
                        $ item_herbs += 1
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch5_2
                            "Go back inside":
                                jump allcastlemenu2
                    "Leave them":
                        "What should I do now?"
                        menu:
                            "Keep looking":
                                jump allsearch5_2
                            "Go back inside":
                                jump allcastlemenu2
            "Enter Tournament" if zuleika_type == 'all' and tournament6_done == False or zuleika_type == 'strong' and tournament6_done == False:
                jump alltournament6
            "Search for clues" if zuleika_type == 'all' and investigate2_done == False or zuleika_type == 'intelligent' and investigate2_done == False:
                $ investigative_skill += 50
                $ investigate2_done = True
                $ energy -= 1
                scene bg castle library with fade
                play music "Audio/Music/Comfortable Mystery 4 (Library).ogg"
                show zuleika normal hidden
                z "I went to the library to take a look at the investigation report regarding Osirus' death."
                show zuleika sad hidden
                z "According to this, he was cut down by a \"large, heavy blade\" while sitting in his chambers."
                show zuleika normal hidden
                z "It sounds like the murder weapon wasn't a normal sword, so that should help narrow down the list of suspects."
                z "Who do I know that uses a \"large, heavy blade\"?"
                jump allcastlemenu2
            "Rest":
                jump allchp4B
                
label allsearch5_2:
    show zuleika normal hidden
    z "This turtle shell looks like it hasn't been inhabited for a long time."
    menu:
        "Pick it up":
            $ item_shell += 1
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch5_3
                "Go back inside":
                    jump allcastlemenu2
        "Leave it":
            "What should I do now?"
            menu:
                "Keep looking":
                    jump allsearch5_3
                "Go back inside":
                    jump allcastlemenu2
                    
label allsearch5_3:
    show zuleika normal hidden
    z "Oh hey, I found a gold coin. I doubt I could use this to pay with, though."
    menu:
        "Pick it up":
            $ item_coin += 1
            z "I think that's enough searching for today. It's time to head back inside."
            if durenspecial_done == False:
                jump alldurenspecial1
            else:
                jump allcastlemenu2
        "Leave it":
            z "I think that's enough searching for today. It's time to head back inside."
            if durenspecial_done == False:
                jump alldurenspecial1
            else:
                jump allcastlemenu2
                
label alldurenspecial1:
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
            jump allcastlemenu2
        "\"Irises\"":
            $ DAffection += 20
            show duren happy
            d "Really? Those are my favorite, too."
            show duren
            d "I love the way the petals fall down, like a fountain...they're so beautiful."
            show zuleika normal hidden
            z "I've never really thought of it that way, but yes, it is a lot like that."
            show duren happy
            d "If I ever find an iris as beautiful as you, I'll be sure to give it to you."
            show zuleika happy hidden
            z "Aww...thank you, Duren. I would love that."
            hide duren
            jump allcastlemenu2
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
            jump allcastlemenu2
            
label allduren_menu2:
    scene bg castle hallway
    show duren with dissolve
    d "Hello, Zuleika. How are you today?"
    menu:
        "Talk" if durenchat2_done == False:
            $ increase_charm(20)
            $ durenchat2_done = True
            $ energy -= 1
            play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
            jump alldurenchat2
        "Ask to train":
            $ increase_strength(30)
            if zuleika_type == 'all' or zuleika_type == 'strong':
                $ battle_skill += 10
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
            jump allcastlemenu2
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ DAffection += 10
                    $ item_bouquet -= 1
                    show duren happy
                    d "These are really beautiful. Thank you, Zuleika."
                    jump allduren_menu2
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ DAffection -= 5
                    $ item_makeup -= 1
                    show duren angry
                    d "Why are you giving this to me?"
                    jump allduren_menu2
                "Miraculous Moonshine" if item_liquor > 0:
                    $ DAffection -= 5
                    $ item_liquor -= 1
                    show duren sad
                    d "I don't like this..."
                    jump allduren_menu2
                "Secret Stealth Knives" if item_knives > 0:
                    $ DAffection += 5
                    $ item_knives -= 1
                    show duren happy
                    d "These might come in handy. Thanks, Zuleika."
                    jump allduren_menu2
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ DAffection += 1
                    $ item_spellbook -= 1
                    show duren
                    d "This is...interesting. Thanks."
                    jump allduren_menu2
                "Elegant Earrings" if item_earrings > 0:
                    $ DAffection += 1
                    $ item_earrings -= 1
                    show duren
                    d "These are nice. Thanks."
                    jump allduren_menu2
                "Wild flowers" if item_flowers > 0:
                    $ DAffection += 5
                    $ item_flowers -= 1
                    show duren happy
                    d "These are pretty. Thanks, Zuleika."
                    jump allduren_menu2
                "Turtle shell" if item_shell > 0:
                    $ DAffection += 10
                    $ item_shell -= 1
                    show duren happy
                    d "This is really cool. Thank you, Zuleika."
                    jump allduren_menu2
                "Herbs" if item_herbs > 0:
                    $ DAffection += 5
                    $ item_herbs -= 1
                    show duren happy
                    d "These might come in handy. Thanks, Zuleika."
                    jump allduren_menu2
                "Stone arrowhead" if item_arrowhead > 0:
                    $ DAffection += 10
                    $ item_arrowhead -= 1
                    show duren happy
                    d "This is really cool. Thank you, Zuleika."
                    jump allduren_menu2
                "Fruit" if item_fruit > 0:
                    $ DAffection += 1
                    $ item_fruit -= 1
                    show duren
                    d "This is nice. Thanks."
                    jump allduren_menu2
                "Gold coin" if item_coin > 0:
                    $ DAffection += 5
                    $ item_coin -= 1
                    show duren happy
                    d "This might come in handy. Thanks, Zuleika."
                    jump allduren_menu2
                "Nevermind":
                    jump allduren_menu2
        "Nevermind":
            jump allcastlemenu2
            
label allnefferon_menu2:
    scene bg throne with fade
    show nef with dissolve
    n "When are you going to sing for me again, I wonder?"
    menu:
        "Talk" if nefchat2_done == False:
            $ increase_charm(20)
            $ nefchat2_done = True
            $ energy -= 1
            play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
            jump allnefferonchat2
        "Discuss politics":
            $ increase_intelligence(30)
            $ energy -= 1
            play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
            show nef
            if zuleika_type == 'strong':
                show zuleika sad hidden
                z "Are you sure it's such a good idea to have an alliance with Menorrhi the Witch?"
                z "Not that I understand all of this political stuff, but it just seems a bit odd..."
                n "There are certain motives behind this alliance...you wouldn't understand."
                show zuleika angry hidden
                z "Then teach me. That's why I came to you in the first place."
                n "Perhaps another time, Princess."
            else:
                show zuleika sad hidden
                z "Are you sure it's such a good idea to have an alliance with Menorrhi the Witch?"
                z "For most of your subjects, Nalan is considered to be a terrifying place..."
                z "All the people I've talked to seem to dislike the idea of being allied with such a nation."
                n "While you may care greatly what the people have to say, little princess, I do not."
                n "There are certain motives behind this alliance...you wouldn't understand."
                show zuleika angry hidden
                z "Then teach me. That's why I came to you in the first place."
                n "Perhaps another time, Princess."
            stop music
            jump allcastlemenu2
        "Give a gift" if zuleika_type == 'all' or zuleika_type == 'kind':
            "What should I give him?"
            menu:
                "Bouquet of Fanciful Flowers" if item_bouquet > 0:
                    $ NAffection -= 5
                    $ item_bouquet -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu2
                "Peniless Princess Travel Kit" if item_makeup > 0:
                    $ NAffection += 10
                    $ item_makeup -= 1
                    show nef happy
                    n "This will be very useful to me. Thank you, Princess."
                    jump allnefferon_menu2
                "Miraculous Moonshine" if item_liquor > 0:
                    $ NAffection += 5
                    $ item_liquor -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu2
                "Secret Stealth Knives" if item_knives > 0:
                    $ NAffection += 1
                    $ item_knives -= 1
                    show nef
                    n "I don't have much use for these, but thank you."
                    jump allnefferon_menu2
                "Sinister Spellbook for Beginners" if item_spellbook > 0:
                    $ NAffection += 5
                    $ item_spellbook -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu2
                "Elegant Earrings" if item_earrings > 0:
                    $ NAffection += 10
                    $ item_earrings -= 1
                    show nef happy
                    n "This will be very useful to me. Thank you, Princess."
                    jump allnefferon_menu2
                "Wild flowers" if item_flowers > 0:
                    $ NAffection -= 5
                    $ item_flowers -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu2
                "Turtle shell" if item_shell > 0:
                    $ NAffection -= 5
                    $ item_shell -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu2
                "Herbs" if item_herbs > 0:
                    $ NAffection += 1
                    $ item_knives -= 1
                    show nef
                    n "I don't have much use for these, but thank you."
                    jump allnefferon_menu2
                "Stone arrowhead" if item_arrowhead > 0:
                    $ NAffection -= 5
                    $ item_arrowhead -= 1
                    show nef angry
                    n "Do I look like I would be satisfied with something so...petty?"
                    jump allnefferon_menu2
                "Fruit" if item_fruit > 0:
                    $ NAffection += 5
                    $ item_fruit -= 1
                    show nef happy
                    n "Ah, very nice. Thank you, Princess."
                    jump allnefferon_menu2
                "Gold coin" if item_coin > 0:
                    $ NAffection += 10
                    $ item_coin -= 1
                    show nef happy
                    n "Gold never loses its value; this is an excellent gift. Thank you, Princess."
                    jump allnefferon_menu2
                "Nevermind":
                    jump allnefferon_menu2
        "Nevermind":
            jump allcastlemenu2

label alldurenchat2:
    show duren
    show zuleika normal hidden
    z "I heard that you won another archery competition last week."
    show zuleika happy hidden
    z "Congratulations!"
    show duren happy
    d "Thank you."
    show duren
    d "I spent a long time preparing for it, so I'm glad that it paid off."
    show zuleika normal hidden
    z "Do you enjoy it? Archery, I mean."
    d "I do. It's one of the few things that helps take my mind off of...you know..."
    menu:
        "\"I understand.\"":
            $ DAffection += 20
            z "I think it's good that you've found a hobby that you enjoy like that."
            show zuleika happy hidden
            z "Maybe you can give me lessons some time."
            show duren happy
            d "Sure, I'd love to."
            jump allcastlemenu2
        "\"Er...do you mean Nefferon?\"":
            show duren sad
            d "Of course I mean Nefferon."
            show duren angry
            d "He's so infuriating!"
            show zuleika sad hidden
            z "I can imagine..."
            z "I'm sorry, Duren. I shouldn't have brought it up."
            show duren sad
            d "It's fine."
            jump allcastlemenu2
    
label allnefferonchat2:
    show nef
    show zuleika normal hidden
    z "So, what exactly does an emperor such as yourself do in his spare time?"
    show nef happy
    n "Curious, are we? I'm flattered, Princess."
    show nef
    n "Well, as you can imagine, I'm a very busy man. Between meetings and negotiations, I don't have much time to myself."
    n "When I do have a spare moment, however, I usually spend it reading."
    n "I also spend some time training every now and then, though I haven't done so much lately."
    
    menu:
        "\"What kind of books do you like to read?\"":
            $ NAffection += 20
            n "If I'm reading for recreation, then I like to read mostly fiction...any kind, really."
            n "This may sound silly, but I enjoy imagining myself in other worlds. It's...refreshing."
            show zuleika happy hidden
            z "That's not silly at all! I'm the same way."
            show nef happy
            n "It's good to know that we have something in common, little princess."
            jump allcastlemenu2
        "\"What kind of weapon do you like to train with?\"":
            $ NAffection += 20
            $ investigative_skill += 20
            n "I wield my legendary Blade of Anguish, of course."
            show zuleika sad hidden
            z "I don't know how you manage to even lift that huge weapon of yours, let alone use it accurately."
            n "It just takes a bit of practice and skill, that's all."
            show zuleika happy hidden
            z "Well, next time you practice, maybe you can teach me a thing or two."
            n "...We'll see."
            jump allcastlemenu2
            
label alltournament6:
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
            
            jump alltournament6_choice
            
        "Return to the Castle":
            stop music
            jump allcastlemenu2
            
label alltournament6_choice:
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
                
            jump alltournament6_choice
            
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
                
            jump alltournament6_choice
            
        "Forfeit":
            an "Are you sure you want to forfeit the match?"
            menu:
                "Yes":
                    jump alltournament6
                "No":
                    jump alltournament6_choice
                    
label alltournament6win:
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
    $ tournament6_done = True
    stop music
    hide vboyb
    jump allcastlemenu2
    
label alltournament6lose:
    stop music
    scene bg black with fade
    
    scene bg courtyard with fade
    play music "Audio/Music/Mighty and Meek (Tournament Start).ogg"
    
    show vboyb sad with dissolve
    an "Ouch, sorry that you lost..."
    an "Better luck next time."
    
    menu:
        "Try again":
            jump alltournament6
            
        "Return":
            jump allcastlemenu2

label allchp4B:
    if zuleika_type != 'all' or zuleika_type != 'charming':
        jump allnefferonmissing
        
    scene bg hallway night with fade
    play music "Audio/Sound/Nighttime.ogg"
    "That night, Nefferon called me in to perform my service to him, as usual. However, rather than meeting in his chambers, he asked to meet in the ballroom instead."
    "I wondered what he had in mind..."
    "I could never tell what that man was thinking, and that fact continued to bother me."
    
    stop music
    scene bg ballroom with fade
        
    show nef with dissolve
    n "Ah, there you are, Princess. I've been waiting for you."
    show nef happy
    n "I think you'll be pleasantly surprised by tonight's request."
        
    show zuleika normal hidden
    z "Oh? Now I'm curious."
        
    show nef
    n "Rather than singing for me, tonight I would like you to...dance with me."
        
    show zuleika sad hidden
    z "...Dance? What kind of dance?"
        
    n "You'll find out soon enough."
    n "So, what do you say, Princess? Will you dance with me?"
        
    menu:
        "\"Of course, Your Majesty.\"":
            $ NAffection += 20
            play music "Audio/Music/Tango de Manzana.ogg"
                
            show nef happy
            n "Excellent."
            show nef
            n "As for the dance...I was thinking of my personal favorite dance, the tango."
                
            show zuleika sad hidden
            z "I'm not sure I know how to do that one..."
                
            n "Well then, I'll show you. Just follow my lead, little princess."
            "He wrapped his arm tightly around my waist and pulled me to him, so close I could feel the heat of his body next to mine."
            "I felt my cheeks becoming flushed as I realized that this was a much more...intimate dance than I was used to."
            show nef happy
            n "Don't tell me you're embarrassed, Princess."
            show zuleika sadblush hidden
            z "No, no, it's nothing like that..."
                
            show nef
            n "Here, step with me."
            z "Like this?"
            n "Almost...here, like this."
            "He brushed the hem of my dress up as he grabbed my leg to slide it next to his."
            "Once again, I became all too aware of how close we were to each other..."
            show nef happy
            "I looked at him, and for a moment our eyes locked. There was something in his eyes...a desire so intense it made me melt."
            n "Are you enjoying this, Princess?"
            show zuleika normalblush hidden
            z "Y...yes, Your Majesty...I am."
            n "Good, I'm glad."
                
            hide nef with dissolve
            "As we continued to dance, I felt his desire, his passion, as it burned through me."
            "But just as I thought I had him all figured out and was ready to give myself to him, he left without a word."
            "I just couldn't understand that man..."
                
            stop music
            scene bg black with fade
            with Pause(.5)
                
            jump allnefferonmissing
    
        "\"No, thanks...\"":
            show nef sad
            n "Really? Not even one dance?"
            show zuleika sad hidden
            z "No, I'm sorry...I'll have to pass this time."
            show zuleika normal hidden
            z "Thank you for the kind offer, though."
            show nef angry
            n "Very well, Princess...you're dismissed for now."
                
            scene bg black with fade
            with Pause(.5)
                
            jump allnefferonmissing