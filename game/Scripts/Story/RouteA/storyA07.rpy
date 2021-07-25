# Story A
# Chapter 07: Preparing for the Battle
label allchp8A:
    call status from _call_status_8

    $ show_button_game_menu = False
    stop music
    
    scene bg stream with fade
    
    "The month flew by quickly, and before I knew it, it was the day before the ball."
    "I still hadn't figured out what I was going to do...I didn't even want to think about it."
    
    play music "Audio/Music/Heartwarming.ogg"
    show chael with dissolve
    c "Remember this spot, Princess?"
    "I looked around, startled from my thoughts."
    "When I realized where we were, I smiled."
    show wzuleika normal hidden
    z "This is where our adventure started, isn't it? It feels like it's been years since that day."
    hide chael with dissolve
    
    show chael 2 at left
    show kirile sad at right
    with dissolve
    
    k "It's hard to believe that this is the last night we'll spend together."
    show kirile at right
    k "I've had so much fun with you two."
    show wzuleika happy hidden
    z "I've had a lot of fun with you, too, Kirile."
    show wzuleika normal hidden
    z "No matter what happens tomorrow, I'll never forget the time we've spent together."
    show chael happy2 at left
    c "Neither will we, Princess."
    show wzuleika happy hidden
    z "Let's make this day count for all it's worth."
    show kirile happy at right
    k "Yeah, let's do it!"
    
    scene bg black with fade
    
    "We spent the day relaxing and playing by the riverside."
    "I think even the ever-serious Chael had fun...\nHe sure had changed since the first time we met."
    "Kirile was the same as ever - always laughing and joking around. His smile lit up the whole world."
    stop music
    "As much as I enjoyed our day together...I knew that it was about to come to an end."
    
    if CAffection > max(KAffection, DAffection, NAffection):
        $ ball = "Chael"
        scene bg night with fade
        "That night, I was approached by just the person I wanted to see."
        play music "Audio/Music/Long Road Ahead B.ogg"
        show chael with dissolve
        c "Good evening, Princess."
        show chael angry
        c "...We need to talk."
        show wzuleika normal hidden
        z "Yes...I know."
        $ CAffection += 50
        show chael happy
        c "I'm glad that I don't have to say it."
        show chael
        c "In Nalan, we don't communicate through words, but rather through thoughts."
        c "Personally, I think it's much more effective."
        show wzuleika sad hidden
        z "Oh? How so?"
        show chael angry
        c "With words, often times the word becomes a substitute for the subject itself."
        c "People then associate feelings and thoughts with the word, rather than the subject."
        c "There are some subjects - like the one described by the word \"love\" - that cannot be understood with words...they must be experienced."
        show wzuleika normal hidden
        z "It almost sounds like you know this from experience."
        show chael happy
        c "I do...thanks to you."
        show wzuleika normalblush hidden
        z "If \"love\" is something that cannot be understood with words, then I wish I could share my thoughts with you so that you could feel how much I love you..."
        show chael happyblush
        c "You can. Here...I'll show you."
        scene bg black with fade
        "He cupped my chin in his hand, and as he placed his lips on mine, it felt as if we became one."
        "I could see, feel, and hear all of his thoughts, and he could do the same with mine."
        "It was strange at first...but it was also the most amazing thing I had ever experienced."
        
        scene bg night with fade
        show chael blush with dissolve
        "As we parted, I couldn't help but long to feel him again...but I knew, from what I felt of his thoughts, that it would have to wait."
        
        show chael angry
        c "The Pyralin won't be too happy about having to stay behind. He was really looking forward to this battle."
        show wzuleika normal hidden
        z "If everything works out, we'll have to make it up to him somehow."
        show chael happy
        c "Agreed."
        
        hide chael
        jump alldecisionA
        
    if KAffection > max(CAffection, DAffection, NAffection):
        $ ball = "Kirile"
        scene bg night with fade
        "That night, I was approached by just the person I wanted to see."
        play music "Audio/Music/Harlequin (Zuleika and Kirile Meeting).ogg"
        show kirile with dissolve
        k "Hey there, Zuleika. Nice night, isn't it?"
        show wzuleika normal hidden
        z "It is...though it's even better now that you're here."
        $ KAffection += 50
        show kirile happy
        k "I was about to say the same."
        show kirile
        k "Small talk aside, we need to discuss your plans for tomorrow."
        k "...I would like to be the one to go with you."
        show wzuleika sad hidden
        z "Are you sure, Kirile? It'll be dangerous, and - "
        show kirile sad
        k "Just listen to me, Zuleika."
        k "When I lost my eye, I thought I would never be able to trust again...or be able to smile again."
        show kirile
        k "But you...something about you opened my heart in a way I never thought was possible."
        k "When I thought all was lost, you showed me that not everyone is bad, that there are good people - wonderful people - in this world, too."
        show kirile happy
        k "And...you brought my smile back."
        show kirile
        k "I don't know what I ever did to deserve the chance to walk alongside someone as amazing as you, but there's nowhere else I'd rather be."
        z "Oh, Kirile..."
        show wzuleika normal hidden
        z "You're an amazing person, too, you know."
        show kirile happy
        k "You really think so?"
        show wzuleika happy hidden
        z "Of course! I wouldn't say it if I didn't mean it."
        show kirile
        k "Then...will you let me take you to the ball?"
        show wzuleika normal hidden
        z "...I would love to go with you, Kirile."
        show kirile sad
        k "Chael won't be too happy about this..."
        z "I'm sure he'll get over it soon enough."
        show kirile
        k "Yeah, I bet you're right. He's a tough guy, after all."
        show wzuleika happy hidden
        z "That he is."
        
        hide kirile
        jump alldecisionB
        
label alldecisionA:
    stop music
    $ ball = "Chael"
    scene bg stream with fade
    if zuleika_type == 'strong':
        "The next morning when I woke up, Kirile had already left."
        "I was sad that I didn't get a chance to say good-bye, but I knew that this was probably for the best...it would have been too hard to see him go."
        play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
        show chael with dissolve
        c "Are you ready, Princess?"
        show wzuleika sad hidden
        z "Not particularly..."
        c "Regardless, it's up to us to save this kingdom. We're the only ones who can do it."
        show chael happy
        c "I believe in you, Princess."
        show wzuleika normal hidden
        z "Thank you, Chael."
        show wzuleika happy hidden
        z "As long as you're by my side, I'm sure we'll win this battle."
        c "Shall we go, then?"
        show wzuleika normal hidden
        z "Yes...let's go."
        
        jump allballchaelA
        
    else:
        "The next morning when I woke up, Kirile had already left."
        "I was sad that I didn't get a chance to say good-bye, but I knew that this was probably for the best...it would have been too hard to see him go."
        play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
        show chael with dissolve
        c "Are you ready, Princess?"
        show wzuleika sad hidden
        z "Not particularly..."
        show chael angry
        c "Regardless, we need to come up with a strategy for defeating Nefferon."
        c "How do you think we should do it?"
        
        if intelligence > 199:
            $ relative_int = 'High'
        else:
            $ relative_int = 'Low'
        if strength > 199:
            $ relative_str = 'High'
        else:
            $ relative_str = 'Low'
        if charm > 199:
            $ relative_chm = 'High'
        else:
            $ relative_chm = 'Low'
        if kindness > 199:
            $ relative_knd = 'High'
        else:
            $ relative_knd = 'Low'
            
        show wzuleika normal hidden
        z "(I currently have %(relative_int)s Intelligence, %(relative_str)s Strength, %(relative_chm)s Charm, and %(relative_knd)s Kindess.)"
        z "(Which one of these plans would play to my strengths?)"
    
    menu:
        "Outsmart him":
            $ method = "outsmart"
            show wzuleika normal hidden
            z "Since intelligence is our strength, we should use it to our advantage."
        "Fight him head-on":
            $ method = "fight"
            show wzuleika angry hidden
            z "With your speed and skills, we should be able to take the crown by force."
            z "It may not be the cleanest way, but it's probably the best way."
        "Negotiate with him":
            $ method = "negotiate"
            show wzuleika sad hidden
            z "As much as I hate to say it, it may be in our best interest in this case to meet with him for negotiations."
            z "I doubt he'll be willing to give up the throne willingly, of course, but if we play our cards right, we may be able to distract him long enough for the Royal Guard to step in."
        "Ask Duren for help":
            $ method = "help"
            show wzuleika normal hidden
            z "I think Duren still cares about me...and I know that he's been hoping for a chance to get rid of Nefferon."
            z "If I explain the situation to him, I'm sure he'll help us."
            show wzuleika angry hidden
            z "With his abilities and connection with the Royal Guard, we'll be able to take Nefferon down for sure."
            
    show chael
    c "That sounds like an excellent idea, Princess."
    c "Shall we go, then?"
    show wzuleika normal hidden
    z "Yes...let's go."
    
    jump allballchaelA
            
label alldecisionB:
    $ ball = "Kirile"
    stop music
    scene bg stream with fade
    if zuleika_type == 'strong':
        "The next morning when I woke up, Chael had already left."
        "I was sad that I didn't get a chance to say good-bye, but I knew that this was probably for the best...it would have been too hard to see him go."
        play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
        show kirile with dissolve
        k "We've got a long day ahead of us. Are you ready?"
        show wzuleika sad hidden
        z "Not particularly..."
        k "Whatever will be, will be. All you can do is try your hardest and hope for the best."
        z "I'm not sure that's very encouraging..."
        k "Let's just go and try our best, okay?"
        show kirile happy
        k "And no matter what happens, I'll be with you."
        show wzuleika happy hidden
        z "Thank you, Kirile."
    
        jump allballkirileA
        
    else:
        "The next morning when I woke up, Chael had already left."
        "I was sad that I didn't get a chance to say good-bye, but I knew that this was probably for the best...it would have been too hard to see him go."
        play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
        show kirile with dissolve
        k "We've got a long day ahead of us. Are you ready?"
        show wzuleika sad hidden
        z "Not particularly..."
        k "Whatever will be, will be. All you can do is try your hardest and hope for the best."
        z "I'm not sure that's very encouraging..."
        k "Well, what do you want to do?"
        
        if intelligence > 199:
            $ relative_int = 'High'
        else:
            $ relative_int = 'Low'
        if strength > 199:
            $ relative_str = 'High'
        else:
            $ relative_str = 'Low'
        if charm > 199:
            $ relative_chm = 'High'
        else:
            $ relative_chm = 'Low'
        if kindness > 199:
            $ relative_knd = 'High'
        else:
            $ relative_knd = 'Low'
            
        show wzuleika normal hidden
        z "(I currently have %(relative_int)s Intelligence, %(relative_str)s Strength, %(relative_chm)s Charm, and %(relative_knd)s Kindess.)"
        z "(Which one of these plans would play to my strengths?)"
    
    menu:
        "Outsmart him":
            $ method = "outsmart"
            show wzuleika normal hidden
            z "Since intelligence is my strength, I should use it to my advantage."
        "Fight him head-on":
            $ method = "fight"
            show wzuleika angry hidden
            z "With your strength, we should be able to take the crown by force."
            z "It may not be the cleanest way, but it's probably the best way."
        "Negotiate with him":
            $ method = "negotiate"
            show wzuleika sad hidden
            z "As much as I hate to say it, it may be in our best interest in this case to meet with him for negotiations."
            z "I doubt he'll be willing to give up the throne willingly, of course, but if we play our cards right, we may be able to distract him long enough for the Royal Guard to step in."
        "Ask Duren for help":
            $ method = "help"
            show wzuleika normal hidden
            z "I think Duren still cares about me...and I know that he's been hoping for a chance to get rid of Nefferon."
            z "If I explain the situation to him, I'm sure he'll help us."
            show wzuleika angry hidden
            z "With his abilities and connection with the Royal Guard, we'll be able to take Nefferon down for sure."
            
    show kirile happy
    k "Then that's what we'll do."
    show kirile
    k "Now, let's go and try our best."
    show kirile happy
    k "And no matter what happens, I'll be with you."
    show wzuleika happy hidden
    z "Thank you, Kirile."
    
    jump allballkirileA