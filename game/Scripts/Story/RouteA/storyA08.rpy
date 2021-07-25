# Story A
# Chapter 08: The Final Battle
label allballchaelA:
    stop music
    scene bg black with fade
    with Pause(.5)
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    
    "By the time we arrived at the ball, the room was full of guests, many of whom I recognized as nobles from the High Court."
    show chael angry with dissolve
    c "Well, here we are..."
    show bzuleika sad hidden
    z "Is something wrong, Chael?"
    c "...I don't like crowded places."
    show bzuleika normal hidden
    z "Neither do I, but let's try to enjoy ourselves while we're here, okay?"
    show chael
    c "Very well..."
    c "Would you like to dance?"
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        show bzuleika happy hidden
        z "I would love to."
    
        stop music
        scene bg black with fade
        with Pause(.5)
    
        $ HP = 0
        $ miss = 0
                    
        scene bg ballroom with fade
                    
        an "The final dance will be..."
            
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
                    
        scene bg ballroom
                                                    
        show dancezuleika normal at left
        with dissolve
                    
        zb "Tonight, let's dance like we mean it."
            
        show chael at right
        with dissolve
                    
        cb "I'm ready whenever you are, Princess."
                    
        show HP at top
        with moveinleft
                    
        jump allcompetition4chael_round1
        
    else:
        show bzuleika sadblush hidden
        z "I'm not actually very good at dancing..."
        show chael happy
        c "Just follow my lead, Princess, and I'm sure you'll do fine."
        hide chael with dissolve
        "As the two of us began dancing, I stumbled a lot at first, but soon we were gliding across the dance floor."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but we were soon approached by the host himself."
        
        jump allchaelballroomconfrontation
    
label allcompetition4chael_round1:
    stop music

    show arrowdown at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
      
    show arrowleft at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
      
    show arrowleft at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice1A.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show chael sad at right
            zb "Oops, sorry, Chael. I missed a few steps there..."
                
            show chael at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4chael_round1
            
        "{image=GUI/Dance/Dance - SevenChoice1B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show chael happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            cb "Well done, Princess."
            show dancezuleika normal at left
            show chael at right
            zb "On to the next one."
            
            jump allcompetition4chael_round2
            
label allcompetition4chael_round2:
    stop music

    show arrowup at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowup at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice2A.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show chael happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            cb "Your moves are as graceful as ever."
            show dancezuleika normal at left
            show chael at right
            zb "On to the next one."
            
            jump allcompetition4chael_round3
            
        "{image=GUI/Dance/Dance - SevenChoice2B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show chael sad at right
            zb "Oops, sorry, Chael. I missed a few steps there..."
                
            show chael at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4chael_round2
            
label allcompetition4chael_round3:
    stop music

    show arrowdown at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowdown at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice3A.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show chael happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            cb "You're doing very well, Princess."
            show dancezuleika normal at left
            show chael at right
            zb "On to the next one."
            
            jump allcompetition4chael_round4
            
        "{image=GUI/Dance/Dance - SevenChoice3B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show chael sad at right
            zb "Oops, sorry, Chael. I missed a few steps there..."
                
            show chael at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4chael_round3
            
label allcompetition4chael_round4:
    stop music

    show arrowright at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowdown at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowright at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowright at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
      
    show arrowdown at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowright at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice4A.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show chael sad at right
            zb "Oops, sorry, Chael. I missed a few steps there..."
                
            show chael at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4chael_round4
            
        "{image=GUI/Dance/Dance - SevenChoice4B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show chael happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            cb "Well done, Princess."
            show dancezuleika normal at left
            show chael at right
            zb "On to the next one."
            
            jump allcompetition4chael_round5
            
label allcompetition4chael_round5:
    stop music

    show arrowleft at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowright at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    show arrowleft at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"

    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"

    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowright at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"

    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"

    hide arrowdown with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice5A.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show chael happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            cb "Wonderful, as expected from you."
            
            jump allcompetition4chaelwin
            
        "{image=GUI/Dance/Dance - SevenChoice5B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show chael sad at right
            zb "Oops, sorry, Chael. I missed a few steps there..."
                
            show chael at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4chael_round5
    
label allcompetition4chaelwin:
    scene bg ballroom with fade
    
    if miss < 2:
        $ CAffection += 20
        "As the two of us danced, we glided flawlessly across the dancefloor. The other guests looked on in awe as Chael and I executed every move perfectly."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but we were soon approached by the host himself."
    else:
        "Even though we stumbled awkardly as we danced, I still had a good time with Chael."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but we were soon approached by the host himself."
    
label allchaelballroomconfrontation:
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    show nef
    n "Ah, there you are, little princess. I've been waiting for you."
    show bzuleika angry hidden
    z "I'm sure you have."
    
    if zuleika_type == 'strong':
        z "This ends tonight. I will no longer stand by and watch while you destroy my beloved nation!"
        show nef happy
        n "Oh, is that so? Well, then, let's settle this once and for all."
        show nef
        n "I challenge you to a tournament-style duel. Let's find out which one of us is fit to rule this nation."
        z "...Very well. I accept your challenge."
    
        jump alltournament4
    
    if method == "outsmart":
        show bzuleika normal hidden
        z "But I agree with what you said in your letter...we should put the past behind us."
        show nef happy
        n "I'm glad you think so, Princess."
        z "I'd like to propose a toast, if I may."
        n "Of course. I'll have the servants bring out the wine."
        
        scene bg ballroom with fade
        show nef with dissolve
        "I held up my wine glass, and Nefferon, along with all of the guests, did the same"
        show bzuleika happy hidden
        z "A toast, to the Neffronian Empire, the grandest empire that ever existed!"
        show nef happy
        play sound "Audio/Sound/applause.ogg"
        z "Long live His Imperial Majesty!"
        cr "Long live His Imperial Majesty!"
        
        stop music
        scene bg black with fade
        
        if intelligence > 199:
            "Our plan was a success; Nefferon drank the wine happily, oblivious to the slow-acting poison that had been slipped into his drink."
            "By the time midnight struck, he would be a mighty emperor no more..."
            
            scene bg ballroom with fade
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            show nef with dissolve
            show bzuleika normal hidden
            z "Well, Your Majesty, we've enjoyed our time...but we really must be going now."
            show nef sad
            n "Leaving so soon? You only just arrived."
            z "We'll be back soon, I'm sure."
            show nef
            n "Very well, Princess. I look foward to seeing you again."
            show bzuleika sad hidden
            z "...As do I..."
            stop music
            scene bg black with fade
            
            jump allchaelgoodending
            
        else:
            n "This is really quite kind of you, Princess...too kind, really."
            n "...Did you honestly think I would fall for your little trick?"
            n "Guards! Seize them!"
            "He must have caught on to our plan to poison him with the wine...we had failed."
            "Though Chael and I fought bravely, we were just no match for the dozens of guards who came at us..."
            
            jump allchaelbadending
        
    if method == "fight":
        if zuleika_type == 'all':
            z "This ends tonight. I will no longer stand by and watch while you destroy my beloved nation!"
            show nef happy
            n "Oh, is that so? Well, then, let's settle this once and for all."
            show nef
            n "I challenge you to a tournament-style duel. Let's find out which one of us is fit to rule this nation."
            z "...Very well. I accept your challenge."
    
            jump alltournament4

        play music "Audio/Music/Power Restored.ogg"
        z "Make no mistake...we're not here to make friends."
        z "Your time is up, Nefferon!"
        n "Is it? Those are pretty big words for someone so...small."
        "I looked over to Chael, who nodded and drew his sword."
        show nef angry
        n "Fine. If it's a fight you want, it's a fight you'll get."
        n "Guards! Seize them!"
        stop music
        scene bg black with fade
        play sound "Audio/Sound/SwordClash.ogg"
        
        if strength > 199:
            "The battle was fierce; Chael and Nefferon were both excellent fighters, and for a while, our two forces seemed almost evenly matched."
            "In the end, however, Nefferon's ego got the better of him and he made a wrong move..."
            "The battle was over; Chael and I had won!"
            jump allchaelgoodending
            
        else:
            "The battle was fierce; Chael and Nefferon were both excellent fighters, and for a while, our two forces seemed almost evenly matched."
            "In the end, however, even Chael's incredible speed and skill were not enough to overwhelm the emperor..."
            "The battle was over; we had lost."
            jump allchaelbadending
            
    if method == "negotiate":
        show bzuleika normal hidden
        z "We came because we think we can make you a deal."
        show nef happy
        n "Oh? What kind of deal could you possibly make me, little princess?"
        z "You'll never know unless you hear what I have to say."
        show nef
        n "Very well. Tell me what you had in mind."
        
        stop music
        scene bg black with fade
        
        if charm > 199:
            n "Hmm...that's a very tempting offer, Princess."
            n "And all I have to do is...?"
            "Our discussion went on just long enough for the Royal Guard, most of whom were still loyal to me, to surround the ballroom."
            "Just as he was about to sign the deal, the soldiers burst through the doors, much to the surprise of the ball's attendees, and apprehended the emperor."
            n "You can't do this! I'm the emperor! I OWN YOU ALL!"
            
            scene bg ballroom with fade
            play music "Audio/Music/Second Coming (Title Screen).ogg"
            show duren with dissolve
            d "Thank you, Zuleika. You've done us all a great favor."
            show bzuleika happy hidden
            z "I'm just glad that it's over."
            
            jump allchaelgoodending
            
        else:
            n "Hmm..."
            n "Hah, you really think I'm going to fall for this? How stupid do you think I am?"
            "My offer wasn't convincing enough; he saw through my ruse and called in the guards."
            "Though Chael and I fought bravely, we were just no match for the dozens of guards who came at us..."
            
            jump allchaelbadending
         
    if method == "help":
        play music "Audio/Music/Power Restored.ogg"
        z "Make no mistake...we're not here to make friends."
        z "Your time is up, Nefferon!"
        n "Is it? Those are pretty big words for someone so...small."
        show bzuleika normal hidden
        z "Luckily for us, we have someone special on our side."
        n "Hah! No one can save you now, Princess."
        
        stop music
        scene bg black with fade
        
        if kindness > 199:
            u "We'll see about that."
            "An arrow soared across the ballroom and landed squarely in the emperor's back."
            "Frightened, the ball's attendees rushed out of the exits, running for their lives."
            n "What...? How...could this be...?"
            
            scene bg ballroom with fade
            play music "Audio/Music/Second Coming (Title Screen).ogg"
            show duren angry with dissolve
            d "Your reign of terror is finally over, Nefferon."
            d "You'll never be able to hurt the people of Tyraca again."
            
            hide duren with dissolve
            "And so we watched as the mighty ruler of the Neffronian Empire fell, once and for all."
            "I couldn't help but wonder if Osirus had the same pained look on his face, as he died at the hands of his own brother..."
            
            jump allchaelgoodending
            
        else:
            "I felt fear creeping up my spine."
            "Duren should have been here by now...where could he be?"
            n "Where's your little friend, hm? I don't think he's coming."
            n "Guards! Seize them!"
            "Though Chael and I fought bravely, we were just no match for the dozens of guards who came at us..."
            
            jump allchaelbadending
            
label allchaelbadending:
    $ outfit = 'mourning'
    
    scene bg black with fade
    "Chael was captured and thrown in the dungeons, while I was forced to work in the castle as the emperor's personal servant."
    "He was charged with the high crime treason and sentenced...to death."
    
    scene bg dungeon with fade
    play music "Audio/Music/Wounded.ogg"
    show chael angry with dissolve
    c "Don't blame yourself for this, Princess..."
    show wzuleika sad hidden
    z "How can I not? If you'd never gotten mixed up with me..."
    "I couldn't bring myself to even look at him, knowing that he was about to die because of me."
    show chael
    c "This was my choice, too, remember? And even now, I don't regret it."
    show chael happy
    c "The time I spent with you was the happiest time of my life. If the price for that time is death, then I will happily pay it."
    z "Oh, Chael..."
    z "How will I go on without you? This life...it isn't worth living if you're not here..."
    show chael angry
    c "Don't say that, Princess."
    show chael
    c "Your life is precious...you bring love and happiness to others in a way that no one else can."
    show chael happy
    c "Treasure your life and the gift you have...bring joy to the world as you have brought joy to me."
    "I tried to smile through the tears that were streaming down my face."
    show wzuleika normal hidden
    z "I...I will, Chael...I promise."
    show chael
    g "Alright, time's up. Come on."
    
    show wzuleika sad hidden
    z "Wait! Just a few more minutes..."
    c "It's fine, Princess...go on."
    show chael happy
    c "And remember...no matter what happens, I will always love you."
    z "...I love you, too...my prince..."
    
    stop music
    scene bg black with fade
    
    "The next morning, I ran out to the courtyard where the execution was to take place."
    "I didn't know if there was anything I could do, but I had to see him again...just one last time."
    
    "By the time I got there, he was already positioned with his head on the chopping block."
    "When he saw me, he smiled...that beautiful, longing smile of his..."
    "I saw his lips moving, and though I couldn't hear him over the crowd, I struggled to figure out what he was saying..."
    "\"Let us meet again in the next life, Princess...\""
    "\"Chael!\" I shouted. This couldn't be happening...he couldn't die like this...no, no, it couldn't be..."
    "\"NOOOOO!!\""
    play sound "Audio/Sound/Decapitation.ogg"
    with Pause(1)
    "...Just like that, my love was no more."
    
    with Pause(2)
    
    scene bg blank with fade
    show journal with dissolve
    play music "Audio/Music/End of the Era (Epilogue).ogg"
    
    "Though I tried to keep Chael's kind words in my heart, I was consumed by grief and anger following his death."
    "I was driven by an insatiable thirst for revenge...a quest which cost me dearly."
    "My plot to kill Nefferon ended up taking the lives of many of my closest allies, including my best friends, Duren and even Kirile."
    "In the end, when everything and everyone else had been destroyed, Nefferon and I killed each other in one last desperate battle."
    
    "Without a ruler, the empire collapsed and the nation of Tyraca fell into ruin."
    "Centuries later, I would still be remembered as the princess who both saved and destroyed the empire."
    "And that...is my story.\n\n(( Ending 7 of 15 ))"
    
    stop music
    scene bg black with fade
    with Pause(.5)

    $ persistent.ending7 = True
    
    jump end
    
label allchaelgoodending:
    scene bg hallway night with fade
    play music "Audio/Sound/Nighttime.ogg"
    show chael with dissolve
    show bzuleika happy hidden
    z "We did it! I can't believe it."
    show chael happy
    c "I never doubted you for a second, Princess. I was sure we would succeed."
    z "Thank you, Chael."
    show chael
    c "What will you do now that you're \"free,\" so to speak?"
    show bzuleika sad hidden
    z "To be honest, I haven't really thought about it."
    show chael happy
    c "Somehow, I'm not surprised."
    show bzuleika angry hidden
    z "Hey...what do you mean by that?"
    c "Nothing, nothing."
    show chael
    c "I have a proposition, if you would like to hear it."
    show bzuleika normal hidden
    z "Sure, I'm listening."
    
    if CAffection > 400:
        c ". . ."
        stop music
        show chael blush
        c "This may seem sudden, but..."
        c "Princess...will you marry me?"
        show bzuleika normalblush hidden
        z ". . ."
        show bzuleika happyblush hidden
        z "Yes...yes, of course I will!"
        play music "Audio/Music/Atlantean Twilight.ogg"
        show bzuleika happyblush hidden
        z "I would be honored to be your wife, Chael."
        show chael happy
        c "I'm so happy. Thank you...Zuleika."
            
        scene chael final with fade
        $ persistent.chaelfinal = True
        
        if kindness < 300:
            "A few weeks later, I went with Chael to his homeland of Nalan, where I was blessed by the High Priestesses of Order."
            "There, in the sacred forests of Nalan, the two of us were joined in holy matrimony, the first marriage ever between two angels."
            "Once we were married, we agreed to return to Tyraca to take on the difficult task of rebuilding the nation."
            "Without Nefferon to back them up, the High Court gave in and allowed me to take my rightful place on the throne."
            "Thus, with Chael by my side, I became the Empress of Tyraca, much to the delight of the public."
            "Duren remained as the next-in-line to the throne, and being freed from his master, he was finally able to help the people as he had always wanted."
            "Kirile, still determined as ever to turn over a new leaf, started up a small group in the city to catch criminals, thus forming the first organized police force."
            "As for Chael and I..."
            "...We lived happily ever after."
    
            scene bg black with fade
            "And that...is my story.\n\n(( Ending 1 of 15 ))"
            $ persistent.ending1 = True
            
        else:
            "A few weeks later, I went with Chael to his homeland of Nalan, where I was blessed by the High Priestesses of Order."
            "There, in the sacred forests of Nalan, the two of us were joined in holy matrimony, the first marriage ever between two angels."
            "Once we were married, we agreed to return to Tyraca to take on the difficult task of rebuilding the nation."
            "But though I was offered the position of Empress, I turned it down."
            "With Chael, Duren, and even Kirile by my side, I worked with the High Court to create a new governing system."
            "Though it was a difficult change, Tyraca henceforth became the first democratic nation of the known world, ruled not by corrupt and greedy monarchs and nobles, but by the average citizens who loved their nation, just as I did long ago."
            "As for Chael and I..."
            "...We lived happily ever after."
    
            scene bg black with fade
            "And that...is my story.\n\n(( Ending 3 of 15 ))"
            $ persistent.ending3 = True
    
        stop music
        scene bg black with fade
        with Pause(.5)
    
        jump end
        
    else:
        if kindness < 300:
            play music "Audio/Music/Atlantean Twilight.ogg"
            c "This nation needs a new ruler, one who will support and protect the interests of the people."
            show chael happy
            c "The one this nation needs...is you."
            show bzuleika normal hidden
            show chael
            z "You really think so?"
            show bzuleika sad hidden
            z "I'm not sure I'm ready..."
            show chael happy
            c "Don't worry, Princess. I'll be with you to help you along the way."
            show bzuleika happy hidden
            z "Thank you so much, Chael."
            show bzuleika normal hidden
            z "It would be an honor to have you as my royal adviser."
            c "The honor is all mine, Princess."
        
            stop music
            scene bg black with fade
            with Pause(1)
    
            scene bg blank with fade
            show journal with dissolve
        
            "Without Nefferon to back them up, the High Court gave in and allowed me to take my rightful place on the throne."
            "Thus, with Chael as my royal adviser, I became the Empress of Tyraca, much to the delight of the public."
            "Duren remained as the next-in-line to the throne, and being freed from his master, he was finally able to help the people as he had always wanted."
            "Kirile, still determined as ever to turn over a new leaf, started up a small group in the city to catch criminals, thus forming the first organized police force."
            "And so began a long age of peace and prosperity for the nation of Tyraca."
            "Chael and I ruled the nation together for many years, and we would be remembered fondly for many more."
        
            "And that...is my story.\n\n(( Ending 2 of 15 ))"
            $ persistent.ending2 = True
            
        else:
            play music "Audio/Music/Atlantean Twilight.ogg"
            c "This nation needs a hero, one who will support and protect the interests of the people."
            show chael happy
            c "The one this nation needs...is you."
            show bzuleika normal hidden
            show chael
            z "You really think so?"
            show bzuleika sad hidden
            z "I'm not sure I'm ready..."
            show chael happy
            c "Don't worry, Princess. I'll be with you to help you along the way."
            show bzuleika happy hidden
            z "Thank you so much, Chael."
            show bzuleika normal hidden
            z "It would be an honor to have you by my side."
            c "The honor is all mine, Princess."
        
            stop music
            scene bg black with fade
            with Pause(1)
    
            scene bg blank with fade
            show journal with dissolve
        
            "Without Nefferon to back them up, the High Court relunctantly offered me the position of Empress. However, I decided to turn it down."
            "With Chael, Duren, and even Kirile by my side, I worked with the High Court to instead create a new governing system."
            "Though it was a difficult change, Tyraca henceforth became the first democratic nation of the known world, ruled not by corrupt and greedy monarchs and nobles, but by the average citizens who loved their nation, just as I did long ago."
            "Thus began a long age of peace and prosperity for the nation of Tyraca."
        
            "And that...is my story.\n\n(( Ending 4 of 15 ))"
            $persistent.ending4 = True
            
        stop music
        scene bg black with fade
        with Pause(.5)
            
        jump end
            
label allballkirileA:
    stop music
    scene bg black with fade
    with Pause(.5)
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    $ ball = "Kirile"
    
    "By the time we arrived at the ball, the room was full of guests, many of whom I recognized as nobles from the High Court."
    show kirile
    k "Wow, this is one crowded place."
    show kirile sad
    k "I must admit that I've never been good with these stiff formal functions..."
    show bzuleika normal hidden
    z "It'll be fine. I doubt anyone will bother trying to talk to us, anyway."
    show kirile
    k "You're probably right."
    show kirile happy
    k "And plus, even if they do, that's why I have you here, right?"
    show bzuleika happy hidden
    z "That's right."
    show kirile
    k "Well, shall we dance?"
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        z "I'd love to!"

        stop music
        scene bg black with fade
        with Pause(.5)
    
        $ HP = 0
        $ miss = 0
                    
        scene bg ballroom with fade
                    
        an "The final dance will be..."
            
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
                    
        scene bg ballroom
                                                    
        show dancezuleika normal at left
        with dissolve
                    
        zb "Tonight, let's dance like we mean it."
            
        show kirile at right
        with dissolve
                    
        kb "Whatever happens, let's just have fun."
                    
        show HP at top
        with moveinleft
                    
        jump allcompetition4kirile_round1
        
    else:
        show bzuleika sad hidden
        z "To be honest, I'm not actually very good with dancing..."
        show kirile sad
        k "Hmm...neither am I."
        show kirile happy
        k "So, then, let's just make fools of ourselves."
        show bzuleika happy hidden
        z "Hehe, sounds like a plan."
        hide kirile with dissolve
        "As we stumbled across the dancefloor, we got quite a few looks, but we didn't mind as long as we were having fun together."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but we were soon approached by the host himself."
        
        jump allkirileballroomconfrontation
    
label allcompetition4kirile_round1:
     
    stop music

    show arrowdown at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowright at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
      
    show arrowleft at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice1A.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show kirile sad at right
            zb "Oops, sorry, Kirile. I missed a few steps there..."
                
            show kirile at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4kirile_round1
            
        "{image=GUI/Dance/Dance - SevenChoice1B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show kirile happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            kb "That was great!"
            show dancezuleika normal at left
            show kirile at right
            zb "On to the next one."
            
            jump allcompetition4kirile_round2
            
label allcompetition4kirile_round2:
     
    stop music

    show arrowup at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice2A.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show kirile happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            kb "Yes, you're doing it!"
            show dancezuleika normal at left
            show kirile at right
            zb "On to the next one."
            
            jump allcompetition4kirile_round3
            
        "{image=GUI/Dance/Dance - SevenChoice2B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show kirile sad at right
            zb "Oops, sorry, Kirile. I missed a few steps there..."
                
            show kirile at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4kirile_round2
            
label allcompetition4kirile_round3:
     
    stop music

    show arrowdown at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice3A.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show kirile happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            kb "You've got some really great moves. Keep it up!"
            show dancezuleika normal at left
            show kirile at right
            zb "On to the next one."
            
            jump allcompetition4kirile_round4
            
        "{image=GUI/Dance/Dance - SevenChoice3B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show kirile sad at right
            zb "Oops, sorry, Kirile. I missed a few steps there..."
                
            show kirile at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4kirile_round3
            
label allcompetition4kirile_round4:
     
    stop music

    show arrowright at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowdown at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowup at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowright at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice4A.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show kirile sad at right
            zb "Oops, sorry, Kirile. I missed a few steps there..."
                
            show kirile at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4kirile_round4
            
        "{image=GUI/Dance/Dance - SevenChoice4B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show kirile happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            kb "That was great!"
            show dancezuleika normal at left
            show kirile at right
            zb "On to the next one."
            
            jump allcompetition4kirile_round5
            
label allcompetition4kirile_round5:
     
    stop music

    show arrowleft at Position(xpos = 145, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
    
    show arrowup at Position(xpos = 217, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundUp.ogg"
    
    with Pause(.5)
    hide arrowup with dissolve
    
    show arrowleft at Position(xpos = 289, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundLeft.ogg"
    
    with Pause(.5)
    hide arrowleft with dissolve
      
    show arrowright at Position(xpos = 361, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowright at Position(xpos = 433, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundRight.ogg"
    
    with Pause(.5)
    hide arrowright with dissolve
    
    show arrowdown at Position(xpos = 505, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    hide arrowdown with dissolve
    
    show arrowdown at Position(xpos = 577, ypos=320)
    with dissolve
    play sound "Audio/Sound/ArrowSoundDown.ogg"
    
    with Pause(.5)
    
    hide arrowup
    hide arrowdown
    hide arrowleft
    hide arrowright
    
    "Which is the correct combination?"
    
    menu:
        "{image=GUI/Dance/Dance - SevenChoice5A.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show kirile happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            kb "I've never seen anyone dance as well as you."
            
            jump allcompetition4kirilewin
            
        "{image=GUI/Dance/Dance - SevenChoice5B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show kirile sad at right
            zb "Oops, sorry, Kirile. I missed a few steps there..."
                
            show kirile at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4kirile_round5
    
label allcompetition4kirilewin:
    scene bg ballroom with fade
    
    if miss < 2:
        $ KAffection += 20
        "As the two of us danced, we glided flawlessly across the dancefloor. The other guests looked on in awe as Kirile and I executed every move perfectly."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but we were soon approached by the host himself."
    else:
        "Even though we stumbled awkardly as we danced, I still had a great time with Kirile."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but we were soon approached by the host himself."
    
label allkirileballroomconfrontation:
    play music "Audio/Music/Crisis (Nefferon Theme).ogg"
    show nef
    n "Ah, there you are, little princess. I've been waiting for you."
    show bzuleika angry hidden
    z "I'm sure you have."
    
    if zuleika_type == 'strong':
        z "This ends tonight. I will no longer stand by and watch while you destroy my beloved nation!"
        show nef happy
        n "Oh, is that so? Well, then, let's settle this once and for all."
        show nef
        n "I challenge you to a tournament-style duel. Let's find out which one of us is fit to rule this nation."
        z "...Very well. I accept your challenge."
        
        jump alltournament4
    
    if method == "outsmart":
        show bzuleika normal hidden
        z "But I agree with what you said in your letter...we should put the past behind us."
        show nef happy
        n "I'm glad you think so, Princess."
        z "I'd like to propose a toast, if I may."
        n "Of course. I'll have the servants bring out the wine."
        
        scene bg ballroom with fade
        show nef with dissolve
        "I held up my wine glass, and Nefferon, along with all of the guests, did the same"
        show bzuleika happy hidden
        z "A toast, to the Neffronian Empire, the grandest empire that ever existed!"
        show nef happy
        play sound "Audio/Sound/applause.ogg"
        z "Long live His Imperial Majesty!"
        cr "Long live His Imperial Majesty!"
        
        stop music
        scene bg black with fade
        
        if intelligence > 199:
            "Our plan was a success; Nefferon drank the wine happily, oblivious to the slow-acting poison that had been slipped into his drink."
            "By the time midnight struck, he would be a mighty emperor no more..."
            
            scene bg ballroom with fade
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            show nef with dissolve
            show bzuleika normal hidden
            z "Well, Your Majesty, we've enjoyed our time...but we really must be going now."
            show nef sad
            n "Leaving so soon? You only just arrived."
            z "We'll be back soon, I'm sure."
            show nef
            n "Very well, Princess. I look foward to seeing you again."
            show bzuleika sad hidden
            z "...As do I..."
            stop music
            scene bg black with fade
            
            jump allkirilegoodending
            
        else:
            n "This is really quite kind of you, Princess...too kind, really."
            n "...Did you honestly think I would fall for your little trick?"
            n "Guards! Seize them!"
            "He must have caught on to our plan to poison him with the wine."
            "Though Kirile and I fought bravely, we were just no match for the dozens of guards who came at us..."
            
            jump allkirilebadending
        
    if method == "fight":
        if zuleika_type == 'all':
            z "This ends tonight. I will no longer stand by and watch while you destroy my beloved nation!"
            show nef happy
            n "Oh, is that so? Well, then, let's settle this once and for all."
            show nef
            n "I challenge you to a tournament-style duel. Let's find out which one of us is fit to rule this nation."
            z "...Very well. I accept your challenge."
    
            jump alltournament4
            
        play music "Audio/Music/Power Restored.ogg"
        z "Make no mistake...we're not here to make friends."
        z "Your time is up, Nefferon!"
        n "Is it? Those are pretty big words for someone so...small."
        "I looked over to Kirile, who nodded and drew his sword."
        show nef angry
        n "Fine. If it's a fight you want, it's a fight you'll get."
        n "Guards! Seize them!"
        stop music
        scene bg black with fade
        play sound "Audio/Sound/SwordClash.ogg"
        
        if strength > 199:
            "The battle was fierce; Kirile and Nefferon were both excellent fighters, and for a while, our two forces seemed almost evenly matched."
            "In the end, however, Nefferon's ego got the better of him and he made a wrong move..."
            "The battle was over; Kirile and I had won!"
            jump allkirilegoodending
            
        else:
            "The battle was fierce; Kirile and Nefferon were both excellent fighters, and for a while, our two forces seemed almost evenly matched."
            "In the end, however, even Kirile's incredible strength and skill were not enough to overwhelm the emperor..."
            "The battle was over; we had lost."
            jump allkirilebadending
            
    if method == "negotiate":
        show bzuleika normal hidden
        z "We came because we think we can make you a deal."
        show nef happy
        n "Oh? What kind of deal could you possibly make me, little princess?"
        z "You'll never know unless you hear what I have to say."
        show nef
        n "Very well. Tell me what you had in mind."
        
        stop music
        scene bg black with fade
        
        if charm > 199:
            n "Hmm...that's a very tempting offer, Princess."
            n "And all I have to do is...?"
            "Our discussion went on just long enough for the Royal Guard, most of whom were still loyal to me, to surround the ballroom."
            "Just as he was about to sign the deal, the soldiers burst through the doors, much to the surprise of the ball's attendees, and apprehended the emperor."
            n "You can't do this! I'm the emperor! I OWN YOU ALL!"
            
            scene bg ballroom with fade
            play music "Audio/Music/Second Coming (Title Screen).ogg"
            show duren with dissolve
            d "Thank you, Zuleika. You've done us all a great favor."
            show bzuleika happy hidden
            z "I'm just glad that it's over."
            
            jump allkirilegoodending
            
        else:
            n "Hmm..."
            n "Hah, you really think I'm going to fall for this? How stupid do you think I am?"
            "My offer wasn't convincing enough; he saw through my ruse and called in the guards."
            "Though Kirile and I fought bravely, we were just no match for the dozens of guards who came at us..."
            
            jump allkirilebadending
         
    if method == "help":
        play music "Audio/Music/Power Restored.ogg"
        z "Make no mistake...we're not here to make friends."
        z "Your time is up, Nefferon!"
        n "Is it? Those are pretty big words for someone so...small."
        show bzuleika normal hidden
        z "Luckily for us, we have someone special on our side."
        n "Hah! No one can save you now, Princess."
        
        stop music
        scene bg black with fade
        
        if kindness > 199:
            u "We'll see about that."
            "An arrow soared across the ballroom and landed squarely in the emperor's back."
            "Frightened, the ball's attendees rushed out of the exits, running for their lives."
            n "What...? How...could this be...?"
            
            scene bg ballroom with fade
            play music "Audio/Music/Second Coming (Title Screen).ogg"
            show duren angry with dissolve
            d "Your reign of terror is finally over, Nefferon."
            d "You'll never be able to hurt the people of Tyraca again."
            
            hide duren with dissolve
            "And so we watched as the mighty ruler of the Neffronian Empire fell, once and for all."
            "I couldn't help but wonder if Osirus had the same pained look on his face, as he died at the hands of his own brother..."
            
            jump allkirilegoodending
            
        else:
            "I felt fear creeping up my spine."
            "Duren should have been here by now...where could he be?"
            n "Where's your little friend, hm? I don't think he's coming."
            n "Guards! Seize them!"
            "Though Kirile and I fought bravely, we were just no match for the dozens of guards who came at us..."
            
            jump allkirilebadending
            
label allkirilebadending:
    $ outfit = 'mourning'
    
    scene bg black with fade
    "Kirile was captured and thrown in the dungeons, while I was forced to work in the castle as the emperor's personal servant."
    "He was charged with the high crime treason and sentenced...to death."
    
    scene bg dungeon with fade
    play music "Audio/Music/Wounded.ogg"
    show kirile with dissolve
    k "Hey, don't look so down."
    show wzuleika sad hidden
    z "How can I not? If you'd never gotten mixed up with me..."
    k "Zuleika, if I'd never met you, I probably would have jumped off that cliff that night."
    z "Really? That's what you were...?"
    show kirile sad
    k "It's true...I had given up. I was ready to die."
    show kirile
    k "But then you showed up...you, with your strength and courage..."
    k "I've never deserved your love, your smile, your selflessnes...yet, even now, here you are, crying for me as if I'm worth something."
    z "That's because you {i}are{/i} worth something...you're worth everything to me, Kirile..."
    k "Hearing that means so much to me, it really does."
    show kirile sad
    k "I just wish I could have given you more..."
    "I tried to smile through the tears that were streaming down my face."
    show wzuleika normal hidden
    z "No, no...you gave me so much!"
    show kirile
    z "You brightened my world in a way that no one else could."
    show kirile happy
    k "Then I'm glad I could give you that much, at least."
    show kirile
    k "Promise me something, okay?"
    show wzuleika sad hidden
    z "Sure, anything."
    k "Promise me...that you'll never give up."
    k "Treasure your life, live it to the fullest...and don't forget to smile."
    show wzuleika normal hidden
    z "Okay, Kirile...I promise."
    
    g "Alright, time's up. Come on."
    
    show wzuleika sad hidden
    z "Wait! Just a few more minutes..."
    k "It's fine, lass...go on."
    show kirile
    k "No matter what happens to me, my heart will always belong to you."
    z "...And mine to you...my prince..."
    
    stop music
    scene bg black with fade
    
    "The next morning, I ran out to the courtyard where the execution was to take place."
    "I didn't know if there was anything I could do, but I had to see him again...just one last time."
    
    "By the time I got there, he was already positioned with his head on the chopping block."
    "When he saw me, he smiled...that sweet, cheerful smile of his..."
    "I saw his lips moving, and though I couldn't hear him over the crowd, I struggled to figure out what he was saying..."
    "\"Let's meet again in the next life...\""
    "\"Kirile!\" I shouted. This couldn't be happening...he couldn't die like this...no, no, it couldn't be..."
    "\"NOOOOO!!\""
    play sound "Audio/Sound/Decapitation.ogg"
    with Pause(1)
    "...Just like that, my love was no more."
    
    with Pause(2)
    
    scene bg blank with fade
    show journal with dissolve
    play music "Audio/Music/End of the Era (Epilogue).ogg"
    
    "Though I tried to keep Kirile's kind words in my heart...I was consumed by grief and anger following his death."
    "I was driven by an insatiable thirst for revenge...a quest which cost me dearly."
    "My plot to kill Nefferon ended up taking the lives of many of my closest allies, including my best friends, Duren and even Chael."
    "In the end, when everything and everyone else had been destroyed, Nefferon and I killed each other in one last desperate battle."
    
    "Without a ruler, the empire collapsed and the nation of Tyraca fell into ruin."
    "Centuries later, I would still be remembered as the princess who both saved and destroyed the empire."
    "And that...is my story.\n\n(( Ending 8 of 15 ))"
    
    stop music
    scene bg black with fade
    with Pause(.5)

    $ persistent.ending8 = True
    
    jump end
    
label allkirilegoodending:
    scene bg hallway night with fade
    play music "Audio/Sound/Nighttime.ogg"
    show kirile with dissolve
    show bzuleika happy hidden
    z "We did it! I can't believe it."
    show kirile happy
    k "Of course we did! I told you before that we'd make a great team, didn't I?"
    z "That you did."
    show kirile
    k "What'll you do now?"
    show bzuleika sad hidden
    z "To be honest, I haven't really thought about it."
    show kirile happy
    k "I thought you were supposed to be the brains of this operation."
    show bzuleika angry hidden
    z "Be quiet, you!"
    k "I'm just kidding."
    show kirile
    k "Seriously, though..."
    k "I may have an idea, if you'd like to hear it."
    show bzuleika normal hidden
    z "Sure, I'm listening."
    k "Well...I've been thinking about returning to Pyralis."
    show kirile sad
    k "I hear that dragons have started popping up all over the place again, and...well...they could use some help."
    show kirile
    show bzuleika happy hidden
    z "That's great, Kirile."
    show bzuleika sad hidden
    z "Well, not that dragons are terrorizing the villages, but..."
    show kirile
    k "I get what you mean, lass."
    
    if KAffection > 400:
        show kirile sad
        k "But...um..."
        z "Yes?"
        stop music
        show kirile blush
        k "I'd really love it if you would come with me..."
        k "...as my mate."
        show bzuleika normalblush hidden
        z ". . ."
        show kirile sad
        k "Unless you don't want to..."
        show bzuleika happyblush hidden
        z "No, no, of course I do!"
        show kirile blush
        play music "Audio/Music/Atlantean Twilight.ogg"
        show bzuleika happyblush hidden
        z "I'd love to go with you."
        show kirile happyblush
        k "Great!"
        show bzuleika sad hidden
        z "But Kirile..."
        show kirile
        k "Yes?"
        show bzuleika angry hidden
        z "I'm not wrestling any dragons."
        show kirile happy
        k "Of course not, lass. They'd snap you in half like a toothpick."
        show bzuleika normal hidden
        z "Then you better protect me well, \"mate.\""
        show kirile
        k "Yes, ma'am, I will."
            
        scene bg black with fade
            
        "A few days later, Chael returned for an official good-bye. It was hard to believe that I wouldn't be traveling the country with him anymore."
        "The Nalani angel had his place at the castle, though."
        "With Nefferon off the throne, the title of Emperor was given to the young Prince Duren, who asked none other than Chael to be his royal adviser."
        "Once we had said our good-byes, Kirile and I left for his homeland, the mountains of Pyralis, where we would spend the rest of our days."
        "The two of us lived happily ever after, dragons and all."
        "And that...is my story.\n\n(( Ending 5 of 15 ))"
    
        stop music
        scene bg black with fade
        with Pause(.5)
        
        $ persistent.ending5 = True
    
        jump end
        
    else:
        k "Anyway, I was thinking that once I'm there, I can talk to my mistress and convince her to help you out."
        k "You may need a bit of outside help if you're going to try to rebuild this country."
        show bzuleika sad hidden
        z "You're assuming that I'm going to be the one rebuilding it..."
        show kirile happy
        k "Trust me, lass. You'll make a great empress."
        show kirile
        k "You're the one this nation needs right now."
        show bzuleika normal hidden
        z "You really think so?"
        show bzuleika happy hidden
        z "I guess I'll give it a shot."
        show kirile happy
        k "That's my girl! Just go out there and give it everything you've got."
        show kirile
        k "I'll look forward to seeing the amazing things you're going to do."
        show bzuleika normal hidden
        z "Thank you, Kirile."
        show bzuleika sad hidden
        z "Are you sure you have to go? I'm sure I'll need a bodyguard even more once I'm the Empress..."
        k "As much as I would love to stay, I think my own people need me more."
        show bzuleika normal hidden
        z "If that's how you feel, then I wish you all the luck in the world, Kirile."
        show kirile happy
        k "Don't worry, lass, I'll come back to visit every once and a while."
        show bzuleika happy hidden
        z "Just make sure to bring some good souvenirs whenever you come, okay?"
        k "Got it."
        
        stop music
        scene bg black with fade
        with Pause(1)
    
        scene bg blank with fade
        show journal with dissolve
        
        "Without Nefferon to back them up, the High Court gave in and allowed me to take my rightful place on the throne."
        "Thus, I became the Empress of Tyraca, much to the delight of the public."
        "Duren remained as the next-in-line to the throne, and being freed from his master, he was finally able to help the people as he had always wanted."
        "Not wanting to return to his old life, Chael remained in Tyraca as my adviser and helped to keep the High Court in check."
        "Soon, Queen Aukinora of Pyralis agreed to create a steady alliance with us, which put an end to much of the bandit activity along the border."
        "As promised, Kirile returned to Tyraca every winter bearing gifts...This became my favorite time of the year."
        "Thus began a long age of peace and prosperity for the nation of Tyraca."
                
        "And that...is my story.\n\n(( Ending 6 of 15 ))"
        with Pause(.5)

        $ persistent.ending6 = True
            
        jump end
        
label alltournament4:
    stop music
    scene bg black with fade
    with Pause(.5)
    
    $ ZHP = 100
    $ EHP = 100
               
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
            
    zb "For my people, I must win this fight!"
            
    show nef at right
    with dissolve
            
    show HPR at topright
    with moveinright
            
    nb "You'll look even more beautiful when I've slit that pretty throat of yours."
            
    jump alltournament4_choice
            
label alltournament4_choice:
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
                
            jump alltournament4_choice
            
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
                
            jump alltournament4_choice
                    
label alltournament4win:
    stop music
    scene bg black with fade
    
    n "I can't...believe...I lost..."
    
    if ball == "Kirile":
        jump allkirilegoodending
        
    else:
        jump allchaelgoodending
    
label alltournament4lose:
    stop music
    scene bg black with fade
    
    show bzuleika sad hidden
    z "I'm sorry, everyone...I failed you..."
    
    if ball == "Kirile":
        jump allkirilebadending
        
    else:
        jump allchaelbadending
    
label allballnefferonA:
    scene bg stream with fade
    
    "The month flew by quickly, and before I knew it, it was the day before the ball."
    "I still hadn't told my companions that I was planning to go to the castle by myself and attend the ball with Nefferon..."
    "How could I tell them that I had fallen for their sworn enemy?"
    
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
    "That night, when the others had fallen asleep, I snuck away quietly..."
    
    with Pause(.7)
    "The next morning, they woke to find the quick note I had left for them."
    "\"My dear friends...\""
    "\"This may seem sudden, but I've decided to go to the ball with the Emperor...as his date.\""
    "\"I ask that you refrain from coming after me; there is no need.\""
    "\"I hope you both discover love and happiness wherever life leads you.\""
    "\"...Good bye.\""
    
    scene bg stream with fade
    play music "Audio/Music/Monster Promenade.ogg"
    
    show chael angry2 at left
    show kirile sad at right
    with dissolve
    
    c "...Is she {i}serious{/i}? How could she just run off with that...?!"
    show kirile angry at right
    k "I know! She's not the type of girl to fall for some lame older guy tortured by a stupid \"dark past\"."
    show kirile sad at right
    k "...Well, okay, maybe she is..."
    c "She must be under some kind of spell. That's the only explanation for it."
    show kirile angry at right
    k "Yeah, that's got to be it. That creep!"
    show chael 2 at left
    c "...We have to save her and take that guy down."
    show kirile at right
    k "Right, let's do it."
    
    stop music
    scene bg black with fade
    with Pause(.5)
    
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    "When they arrived at the ball, the room was already full of guests."
    "They were soon approached by a familiar face."
    
    show duren angry with dissolve
    d "What are you two doing here?"
    hide duren
    
    show chael 2 at left
    show duren angry at right
    with dissolve
    
    c "We're not here to pick a fight."
    show duren at right
    c "We came to find Zuleika and bring her back to her senses. Has she been acting strangely at all?"
    d "Not at all."
    show duren sad at right
    d "Why do you ask?"
    show chael angry2 at left
    c "We think she may be under some kind of love spell."
    d "That's highly unlikely. His Majesty would never use that kind of thing."
    show duren at right
    d "As strange as it is, I think her feelings for him are genuine."
    hide duren
    show kirile angry at right
    with dissolve
    k "There's no way! He had to have done {i}something{/i} to her."
    c "It {i}has{/i} to be some form of mind control. Are you sure he hasn't done anything?"
    hide kirile
    show duren sad at right
    with dissolve
    d "Sorry guys, but seriously, he hasn't done anything."
    show duren at right
    d "She's just...moving on, I guess."
    hide duren
    stop music
    
    show kirile sad at right
    show chael sad2 at left
    with dissolve
    
    c "Moving on...?"
    k "No way..."
    
    play music "Audio/Music/Monster Promenade.ogg"
    show chael angry2 at left
    c "This is all your fault, you idiot."
    c "She was perfectly happy with me until you came along."
    show kirile angry at right
    k "My fault? I bet she just got sick of you being Mr. Pouty Face all the time."
    k "Seriously, would it kill you to smile every once and a while?"
    c "As if I would give you the pleasure."
    c "No, she probably just became fed up with your stupidity."
    k "Hey, I'm not that stupid! Just because I'm not a genius like you..."
    
    hide chael
    hide kirile
    stop music
    
    show duren angry with dissolve
    d "Look, it's no one's fault."
    
    play music "Audio/Music/Happy Boy End Theme.ogg"
    show duren
    d "She loves you both, but she made her choice to be with the Emperor."
    d "She moved on, and perhaps it's time for you two to do the same."
    hide duren
    
    show chael sad2 at left
    show kirile sad at right
    with dissolve
    c "He's right...this is silly."
    show chael angry2 at left
    c "We can't dictate who she dates; that choice is hers and hers alone."
    k "I guess you're right...we have to let her make her own decisions."
    show chael 2 at left
    c "Right, even if we don't agree with them."
    show kirile at right
    k "So...we're moving on."
    c "Yes, we are."
    k "Yep..."
    c "Indeed..."
    show kirile sad at right
    k ". . ."
    show chael sad2 at left
    c ". . ."
    show kirile at right
    k "Want to get a drink?"
    show chael 2 at left
    c "That...actually sounds pretty good right about now."
    
    stop music
    scene bg black with fade
    
    "That night, I had a wonderful time at the ball with Nefferon. Despite past hostilities, he was actually quite polite and romantic."
    "Though he and I went our separate ways after that night, I never forgot the choice I had made: a choice that was all my own."
    "I soon made the decision to leave the castle and the life I once knew, never to return."
    "I didn't know where I would end up, but I knew that I would keep going no matter what came my way."
    "I was, after all, no longer the princess of the Osirian Empire, but Zuleika the Courageous, a name that was mine and mine alone."
    
    "And that...is my story.\n\n(( Ending 10 of 15 ))"
    with Pause(.5)

    $ persistent.ending10 = True
            
    jump end
    
label allballdurenA:
    scene bg stream with fade
    
    "The month flew by quickly, and before I knew it, it was the day before the ball."
    "I still hadn't told my companions that I was planning to go to the castle by myself and attend the ball with Duren..."
    "How could I tell them that I had fallen for the same person who had tried to kill them before?"
    
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
    "That night, when the others had fallen asleep, I snuck away quietly and hoped that they wouldn't come looking for me..."
    
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    
    "By the time I arrived at the ball, the room was full of guests, many of which I recognized as nobles from the High Court."
    show duren with dissolve
    "As I entered, I searched the room for Duren and quickly found him."
    
    d "Wow, Zuleika...you look beautiful tonight."
    show duren sad
    d "Not that you don't usually...I mean..."
    
    show bzuleika normal hidden
    z "It's alright, Duren. I know what you meant."
    show duren
    show bzuleika happyblush hidden
    z "Thank you."
    
    d "May I ask you for this dance?"
    z "I would - "
    stop music
    hide duren
    u "Hold it!"
    
    show kirile angry at right
    show chael angry2 at left
    with dissolve
    
    play music "Audio/Music/Monster Promenade.ogg"
    
    c "We would appreciate it if you would unhand our princess."
    k "Yeah, let her go, you little punk. She belongs with us."
    
    hide kirile
    hide chael
    show duren angry
    with dissolve
    d "{i}Your{/i} princess? Over my dead body!"
    
    hide duren
    show kirile angry at right
    show duren angry2 at left
    with dissolve
    
    k "You wanna pick a fight with us, huh? Bring it on!"
    d "This time, I definitely won't lose."
    
    show bzuleika angry hidden
    z "Now boys, there's really no need -"
    
    k "Ha! You don't know who you're talking to, kid. Run along before you get hurt."
    d "I don't think you know who {i}you're{/i} talking to, old man. Don't underestimate me just because I look young."
    
    hide kirile
    hide duren
    show chael
    with dissolve
    
    show bzuleika sad hidden
    z "Chael, aren't you going to do something to stop them?"
    c "Hm? Oh, no, I was just going to let them beat each other up. Then it might actually be quiet for once..."
    show bzuleika angry hidden
    z "Chael!"
    show chael angry
    c "Fine, fine...as you wish, Princess."
    show chael
    c "...Come on, Kirile. Let's just take her and run."
    
    hide chael
    show kirile at right
    show chael 2 at left
    with dissolve
    
    k "Now you're talkin'! Sounds like a good plan to me."
    
    z "Hey, that's not what I meant!"
    show bzuleika sad hidden
    z "Sorry, guys, but I'm staying here with Duren."
    
    show kirile happy at right
    k "Then we'll stay, too. We can help you around the castle, right, Chael?"
    c "Correct."
    
    show bzuleika angry hidden
    z "No, you can't stay here. Go home already!"
    
    show kirile sad at right
    show chael sad2 at left
    
    c "But Princess..."
    k "You can't ditch us...we're the heroes of this story!"
    show chael angry2 at left
    c "And we're far better looking."
    show kirile angry at right
    k "It's true. I mean, have you {i}seen{/i} that guy's nose?"
    
    stop music
    
    z "Stop it, both of you. I won't tolerate you insulting my boyfriend."
    show chael sad2 at left
    show kirile sad at right
    k "Boyfriend...?"
    c "Very well, Princess...if that's how you feel, then we'll leave."
    show chael angry2 at left
    c "Let's go, Kirile."
    k "Aww...I wanted to be her boyfriend..."
    
    hide chael
    hide kirile
    
    play music "Audio/Music/Court of the Queen (ball).ogg"
    
    show duren with dissolve
    d "Finally, we're alone again at last."
    
    show bzuleika sad hidden
    z "I'm sorry about that, Duren...I guess they got a little attached to me over these past few months."
    
    d "It's fine, really. I'm just glad you managed to take care of it."
    show duren happy
    d "You sure have changed since you left the castle."
    
    show bzuleika normal hidden
    z "Really? How so?"
    
    show duren
    d "You seem...stronger now."
    show duren sad
    d "I remember a time when you simply went along with whatever your master asked, even if you knew it was wrong..."
    show duren
    d "But seeing you act against those guys without hestitation..."
    show duren happy
    d "You're even more amazing than I thought, Zuleika."
    
    show bzuleika happy hidden
    z "I guess you're right; I have changed. Thanks, Duren."
    show bzuleika normal hidden
    z "If I ever see those two again, I'll be sure to thank them, too."
    show bzuleika happy hidden
    z "But for now...how about that dance?"

    stop music
    scene bg black with fade
    
    "That night, I had a wonderful time at the ball with Duren. I was glad that I chose to go with him after all."
    "Though he and I went our separate ways after that night, I never forgot the choice I had made: a choice that was all my own."
    "I made the decision to leave the castle and travel the countryside by myself, without relying on anyone else."
    "I didn't know where I would end up, but I knew that I would keep going no matter what came my way."
    "I was, after all, no longer the princess of the Osirian Empire, but Zuleika the Courageous, a name that was mine and mine alone."
    
    "And that...is my story.\n\n(( Ending 9 of 15 ))"
    with Pause(.5)

    $ persistent.ending9 = True
            
    jump end
