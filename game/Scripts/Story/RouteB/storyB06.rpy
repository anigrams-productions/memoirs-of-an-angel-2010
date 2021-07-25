# Story B
# Chapter 06: The Final Battle
label allchp6B:
    call status from _call_status_14

    $ show_button_game_menu = False
    stop music
    
    if ball == "Nefferon":
        jump allballnefferonB
    elif ball == "Duren":
        jump allballdurenB
    elif ball == "Chael":
        jump allballchaelB
    elif ball == "Kirile":
        jump allballkirileB
        
label allballnefferonB:
    stop music
    scene bg castle hallway with fade
    
    "It was now the day of the ball and I was feeling anxious. There were so many things that could go wrong…"
    "What if all of the Order members didn't show up? What if they caught on to our plan and brought back-up? Would we be able to handle it?"
    
    u "What's wrong, little princess?"
    play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
    show nef with dissolve
    "I turned to see the emperor himself standing before me."
    show zuleika normal hidden
    z "Nefferon...I didn't expect to see you here."
    z "So, to what do I owe the pleasure of your visit?"
    
    n "I wanted to tell you that I've had your dress for tonight delivered to your room."
    n "I had it designed and made just for you, and I believe it will accent your beauty marvelously…I hope you find it to your liking."
    
    "I remained silent for a long while as the two of us looked at each other intently, each trying to gauge the other's feelings."

    show nef sad
    n "Well, if you have nothing to say, I suppose I'll take my leave."
    show nef sad2
    "But as Nefferon turned to leave, I caught him by the sleeve."
    show zuleika sadblush hidden
    z "Wait…I…I'm worried, about tonight. Will it be okay? …Will {i}you{/i} be okay?"
    $ NAffection += 20
    show nef sad
    "He turned back to me and looked at me with a serious expression now."
    n "I'm worried, too, and to be honest, I can't promise anything. However…"
    show nef
    n "As long as you're by my side, my princess, I'm sure it will turn out alright. You {i}will{/i} stay with me, won't you?"

    "I hesitated, still not sure whether I could trust this man or not."
    
    scene bg black with fade
    stop music
    "Before I realized what was happening, he had planted his lips on mine, and I instinctively closed my eyes and kissed back." 
    "There was something to it that I couldn't quite put my finger on…something pained about it, perhaps?"

    n "I'll see you tonight, little princess."
    stop music
    scene bg black with fade
    with Pause(.5)
    
    scene bg bedroom with fade
    "After biding my time around the castle until nightfall, I returned to my bedroom to get ready."
    play sound "Audio/Sound/knocking_6.ogg"
    with Pause(1)
    show zuleika normal hidden
    z "Come in."
    
    play music "Audio/Music/Lasting Hope (Sad Duren Theme).ogg"
    show duren sad with dissolve
    d "I’m sorry for interrupting, Zuleika, but…we need to talk."

    "No one else was supposed to know about the plan, but suddenly I feared that the young prince might have found out about it."
    z "What’s wrong, Duren?"

    d "I just…I have a feeling that something bad is going to happen tonight."
    d "I overheard some things…from Nefferon. He's planning something, and whatever it is, it's not going to be good for any of us…especially you."
    d "I'm worried about you, Zuleika, and…I don't think you should go to the ball with him tonight."
    d "Come with me instead; I'll make sure he doesn't hurt you or anyone else ever again."

    "I looked at him and could see that he was genuinely worried and frightened for my life."
    "It was true that I hesitated when Nefferon asked me whether I would stay with him...but how could I leave him hanging at the last minute?"
    "He would surely be arrested by the Royal Guard, if not killed by the Order..."
    "Would I be able to live with his death on my conscience?"
    
    menu:
        "Go with Nefferon":
            $ NAffection += 20
            $ ball = "Nefferon"
            z "I’m sorry, Duren, but I promised that I would go to the ball with him tonight, and I intend to keep that promise, no matter what happens."

            show duren angry
            d "You don't know him like I do, Zuleika...you can't trust that man."
            d "The only one he has ever thought of is himself; everything he does is to benefit him and only him."
            show duren sad
            d "Please, Zuleika, stop this foolishness and come with me."

            show zuleika angry hidden
            z "For your information, I know him better than you think, and I believe that what I'm doing is right."
            show zuleika normal hidden
            z "After tonight, you'll understand; things will change for the better, I'm sure of it."

            z "You've been my best friend for as long as I can remember, and I thank you for always sticking by me all these years, but I've made my decision and I will follow through with it."
            show zuleika sad hidden
            z "As my friend, I hope that you will support me in this…but if not, then so be it."

            d ". . ."
            hide duren with moveoutright
            "As he left in silence, I realized that a single tear was running down my cheek and quickly brushed it away."
            "I had to be strong now, for all of our sakes..."

            jump allballnefferon2B
        "Go with Duren":
            $ DAffection += 20
            $ ending = "Leave"
            $ ball = "Duren"
            show duren
            "I couldn't help feeling a sneaking suspicion that Duren was right."
            "Even though I had somewhat fallen for his charm, there was still something about him that sent shivers down my spine…"
            "Nefferon was a man who couldn't be trusted, and as much as it hurt me to abandon the plans we made together, I just couldn't be sure that it wasn't a trick."

            show zuleika normal hidden
            z "Alright, I’ll go with you."
            
            d "Thank you, Zuleika. You made the right choice, I promise."

            jump allballdurenB

label allballnefferon2B:
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    
    "By the time I arrived at the ball, the room was full of guests, many of which I recognized as nobles from the High Court."
    show nef with dissolve
    "As I entered, I searched the room for Nefferon and quickly found him."
    show nef happy

    n "Amazing…"
    n "You're even more breathtaking than I thought."
    
    show bzuleika normalblush hidden
    z "Thank you, Your Majesty."
    
    show nef
    n "May I have this dance?"
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        show bzuleika happy hidden
        z "Of course!"
    
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
        show VSNefferon at right
        with moveinright
        an "dancing with none other than the infamous Emperor Nefferon!"
                    
        hide VSNefferon with moveoutright
        hide VSBZuleika with moveoutleft
                    
        scene bg ballroom
                                                    
        show dancezuleika normal at left
        with dissolve
                    
        zb "Tonight, let's dance like we mean it."
            
        show nef at right
        with dissolve
                    
        nb "To dance with someone as stunning as you is truly an honor, Princess."
                    
        show HP at top
        with moveinleft
                    
        jump allcompetition7nef_round1
        
    else:
        show bzuleika sadblush hidden
        z "I'm really not very good at dancing..."
        n "That's alright. Just follow me and you'll be fine."
        show nef happy
        n "You trust me, don't you?"
        show nef
        "I nodded hesitantly as he put one arm around my waist while his other hand held mine."
        hide nef with dissolve
        "As the two of us began dancing, I stumbled a lot at first, but soon we were gliding across the dance floor."

        "For a while, I was able to lose myself in the motions and forget about the horrible acts I was to commit that night…but only for a while, until cold reality set in."
        
        jump allnefballroomconfrontation
    
label allcompetition7nef_round1:
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
            show nef sad at right
            zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
            show nef at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7nef_round1
            
        "{image=GUI/Dance/Dance - SevenChoice1B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show nef happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            nb "Well done, Princess."
            show dancezuleika normal at left
            show nef at right
            zb "On to the next one."
            
            jump allcompetition7nef_round2
            
label allcompetition7nef_round2:
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
            show nef happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            nb "Truly splendid."
            show dancezuleika normal at left
            show nef at right
            zb "On to the next one."
            
            jump allcompetition7nef_round3
            
        "{image=GUI/Dance/Dance - SevenChoice2B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show nef sad at right
            zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
            show nef at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7nef_round2
            
label allcompetition7nef_round3:
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
            show nef happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            nb "You're doing very well, Princess."
            show dancezuleika normal at left
            show nef at right
            zb "On to the next one."
            
            jump allcompetition7nef_round4
            
        "{image=GUI/Dance/Dance - SevenChoice3B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show nef sad at right
            zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
            show nef at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7nef_round3
            
label allcompetition7nef_round4:
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
            show nef sad at right
            zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
            show nef at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7nef_round4
            
        "{image=GUI/Dance/Dance - SevenChoice4B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show nef happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            nb "Well done, Princess."
            show dancezuleika normal at left
            show nef at right
            zb "On to the next one."
            
            jump allcompetition7nef_round5
            
label allcompetition7nef_round5:
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
            show nef happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            nb "As I thought, you're a remarkable dancer."
            
            jump allcompetition7nefwin
            
        "{image=GUI/Dance/Dance - SevenChoice5B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show nef sad at right
            zb "Oops, I'm sorry, Your Majesty. I missed a few steps there..."
                
            show nef at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7nef_round5
    
label allcompetition7nefwin:
    scene bg ballroom with fade
    
    if miss < 2:
        $ NAffection += 20
        "As the two of us danced, we glided flawlessly across the dancefloor. The other guests looked on in awe as Nefferon and I executed every move perfectly."
        "For a while, I was able to lose myself in the motions and forget about the horrible acts I was to commit that night…but only for a while, until cold reality set in."
    else:
        "Even though we stumbled awkardly as we danced, I still had a good time with Nefferon."
        "For a while, I was able to lose myself in the motions and forget about the horrible acts I was to commit that night…but only for a while, until cold reality set in."

label allnefballroomconfrontation:
    show nef angry with dissolve
    n "It’s time."
    stop music
    scene bg black with fade
    "While Nefferon took care of the first one, it was my job to prepare a special \"treat\" for another, who was told to meet Nefferon in the ballroom after everyone had left."

    "I brewed the finest tea I could make, then poured half a vial of powerful poison into it."
    "Having been made from dark Nalani magic, it was supposed to be able to kill the strongest and mightiest of beings...even a god."

    "Though I had my doubts, there was no turning back now."

    scene bg ballroom with fade
    "When I arrived at the meeting place, however, I was shocked to find not a member of the Order..."
    play music "Audio/Music/Trio for Piano, Cello, and Clarinet (Sad Zuleika Theme).ogg"
    show nef sad with dissolve
    "...but Nefferon himself. I had a bad feeling about this…"
    
    menu:
        "\"What are you doing here?\"":
            $ NAffection += 20
            show bzuleika sad hidden
            z "What are you doing here? Did something happen?"

            n "I just needed to see you."

            show bzuleika angry hidden
            z "Nefferon, don't tell me you're having doubts about all of this. It's a bit late for that..."

            n "No, that’s not it."
            n "Zuleika…thank you so much for everything."

            "I was shocked; this was completely out of character for him."
            "Why was he doing this? Where was the person who was supposed to be there?"

            n "I have always only been able to see people as resources to be used...I've never been able to connect with anyone. But you…"
            n "Even when I was forsaken by everyone else, you weren't afraid to touch me. Even when I did horrible things to you, you wanted to help me."
            n "You are like no one else…you make this pathetic life worth living."

            show bzuleika sadblush hidden
            z "...Don't say things like that."

            n "I need to say it. You need to hear it."
            n "All I want is to love you, and only you, with my entire being…I want to give you everything...and you, my princess, are the only one who can make me feel this way."

            show bzuleika angry hidden
            z "Nefferon, please, this isn't the time…"

            show nef angry
            n "This is the {i}only{/i} time, don't you see?"
            show nef sad
            n "Everything ends tonight, one way or another."

            z "Nothing is going to end."
            show bzuleika normalblush hidden
            z "We're going to take down the Order just like we planned…we'll do it together."
            
            n ". . ."
            
            show nef happy with dissolve
            play music "Audio/Music/A Singular Perversion (Hungry Nefferon Theme).ogg"
            
            "Much to my surprise, the emperor started laughing."
            "It wasn't a funny laugh, but something else…a sinister laugh that made my skin crawl."
            show nef
            n "My dear, little princess…how naïve you can be. I {i}am{/i} the Order."

            show bzuleika sad hidden
            z "What do you…what do you mean? You said…"

            n "I said a lot of things, my love, and just like my foolish brother, you fell for them all."

            show bzuleika angry hidden
            z "How could you?! I trusted you..."
            
            stop music
            scene bg black with fade
            "Before I could say anything more, I felt a sharp pain in my stomach."
            "Looking down, I first saw the blood...then the sword...then his hand, grasping it tightly."

            play music "Audio/Music/Lone Harvest.ogg"
            scene nef death with fade
            $ persistent.nefdeath = True
            n "I love you, my princess..."

            show bzuleika sad hidden
            z "Then...why?"

            n "That {i}is{/i} why. That's precisely why."
            n "I told you that I want to give you everything…and the ultimate gift, my love, is death. Isn't it wonderful?"
            "In a last, desperate effort, I freed a hand long enough to reach into my dress, take out the half-empty vial of poison, and pour it into my mouth."

            "Nefferon looked at me curiously."
            n "What are you – "

            scene bg black with fade
            "Before he could finish, I forced my lips to his and pushed the cold liquid down his throat."

            "He was shocked for a moment, but took the opportunity to kiss me with all of the intense passion that had brought us to this point."

            "...I kissed back until I couldn't hold on anymore."

            "He held me tightly as the deadly poison took its effect, satisfied. It was, as far as he was concerned, the perfect ending."
            
            "And that...is my story.\n\n(( Ending 13 of 15 ))"
            with Pause(.5)

            $ persistent.ending13 = True
            
            jump end

        "Get out of there":
            $ DAffection += 20
            $ ending = "Leave"
            play music "Audio/Music/A Mission.ogg"
            "This wasn't right at all, and I knew it."
            "If Nefferon was here, where were the people we were supposed to kill? This had to be a trap..."
            "And so, I bolted out of there as fast as I could."
            
            scene bg hallway night with fade

            "It took me a moment to figure it out, but I knew what I had to do: I had to find Duren."

            "I suddenly felt bad that I had doubted my friend’s judgment, but I also knew that now was not the time for regrets."
            "I had to move, quickly."

            "After a bit of searching, I finally found him." 
            show duren
            show bzuleika sad hidden
            z "Duren!"
            show duren sad
            d "Zuleika, what’s wrong? Did something happen?"

            z "…I need your help."
            
            show duren
            d "If this is about Nefferon, I already gathered the Royal Guards...they're surrounding him as we speak."
            show duren sad
            d "I'm sorry that I went behind your back, but I just couldn't bear the risk of losing you."
            z "Oh, Duren...thank you. I'm so sorry that I ever doubted you...I should have known better."
            
            show duren
            d "It's fine. I'm just glad that you're back on my side."
            d "Let's go."
            
            jump allarrestnefferonB
            
label allballdurenB:
    scene bg black with fade
    with Pause(.5)
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
    
    if zuleika_type == 'all' or zuleika_type == 'charming':
        z "Of course, Duren."
    
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
        show VSDuren at right
        with moveinright
        an "dancing with the young Prince Duren!"
                    
        hide VSDuren with moveoutright
        hide VSBZuleika with moveoutleft
                    
        scene bg ballroom
                                
        show dancezuleika normal at left
        with dissolve
                    
        zb "Tonight, let's dance like we mean it."
            
        show duren at right
        with dissolve
                    
        db "As long as you put your heart into it, I'm sure our dance will be great."
                    
        show HP at top
        with moveinleft
                    
        jump allcompetition7duren_round1
        
    else:
        show bzuleika sadblush hidden
        z "I'm not actually very good at dancing..."

        d "You have such a wonderful, free spirit, Zuleika...it's one of the things I admire most about you."
        show duren happy
        d "If you put those same feelings into your movements, then I'm sure your dance will be great."
    
        show bzuleika happyblush hidden
        z "You really think so?"
    
        show duren
        d "I do."
    
        z "Well, then, let's dance!"
    
        hide duren with dissolve
        "As the two of us began dancing, I stumbled a lot at first, but soon we were gliding across the dance floor."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but eventually, cold reality set in."
        
        jump alldurenballroomconfrontation
    
label allcompetition7duren_round1:
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
            show duren sad at right
            zb "Oops, sorry, Duren. I missed a few steps there..."
                
            show duren at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7duren_round1
            
        "{image=GUI/Dance/Dance - SevenChoice1B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show duren happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            db "That's the way to do it!"
            show dancezuleika normal at left
            show duren at right
            zb "On to the next one."
            
            jump allcompetition7duren_round2
            
label allcompetition7duren_round2:
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
            show duren happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            db "Keep it up."
            show dancezuleika normal at left
            show duren at right
            zb "On to the next one."
            
            jump allcompetition7duren_round3
            
        "{image=GUI/Dance/Dance - SevenChoice2B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show duren sad at right
            zb "Oops, sorry, Duren. I missed a few steps there..."
                
            show duren at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7duren_round2
            
label allcompetition7duren_round3:
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
            show duren happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            db "You're doing great!"
            show dancezuleika normal at left
            show duren at right
            zb "On to the next one."
            
            jump allcompetition7duren_round4
            
        "{image=GUI/Dance/Dance - SevenChoice3B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show duren sad at right
            zb "Oops, sorry, Duren. I missed a few steps there..."
                
            show duren at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7duren_round3
            
label allcompetition7duren_round4:
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
            show duren sad at right
            zb "Oops, sorry, Duren. I missed a few steps there..."
                
            show duren at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition4chael_round4
            
        "{image=GUI/Dance/Dance - SevenChoice4B.png}":
            play music "Audio/Music/Court of the Queen (Ball).ogg"
            
            show dancezuleika happy at left
            show duren happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            db "That's the way to do it!"
            show dancezuleika normal at left
            show duren at right
            zb "On to the next one."
            
            jump allcompetition7duren_round5
            
label allcompetition7duren_round5:
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
            show duren happy at right
                
            $ HP += 20
            
            zb "Perfect!"
            
            db "That was fantastic, Zuleika."
            
            jump allcompetition7durenwin
            
        "{image=GUI/Dance/Dance - SevenChoice5B.png}":
            $ miss += 1
            
            zb ". . ."
                
            show dancezuleika sad at left
            show duren sad at right
            zb "Oops, sorry, Duren. I missed a few steps there..."
                
            show duren at right
            show dancezuleika normal at left
            zb "Let's try that again."
                
            jump allcompetition7duren_round5
    
label allcompetition7durenwin:
    scene bg ballroom with fade
    
    if miss < 2:
        $ DAffection += 20
        "As the two of us danced, we glided flawlessly across the dancefloor. The other guests looked on in awe as Duren and I executed every move perfectly."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but eventually, cold reality set in."
    else:
        "Even though we stumbled awkardly as we danced, I still had a good time with Duren."
        "For a while, I was able to lose myself in the movements and the pleasure of his company...but eventually, cold reality set in."
        
label alldurenballroomconfrontation:
    show duren sad with dissolve
    d "...It's time. Are you ready?"
    show bzuleika sad hidden
    z "As ready as I'll ever be."
    show duren
    d "I'm counting on you."
    
label allarrestnefferonB:
    
    if ball == "Nefferon":
        stop music
        scene bg black with fade
        "As I planned with Duren, I asked Nefferon to meet me in the ballroom after everyone else had gone home."
        "I was nervous, of course, but I knew I had to be strong and push my fear aside, for all of our sakes."
    
        scene bg ballroom with fade
        play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
        show nef with dissolve
        n "I didn't expect you to wish to meet with me like this, Princess...after all, we have a date in my chambers tomorrow, remember?"
    
        show bzuleika normal hidden
        z "I've just enjoyed our recent visits so much, Your Majesty, that I simply couldn't wait to see you again."
    
        show nef happy
        n "Is that so?"
        show nef
        n "Well, then, I suppose I shouldn't deny a lady's request."
    
        "Right on schedule, one of the maid servants brought us some freshly brewed tea."
        "Thanks to my preparations, however, the tea was specially brewed with a heavy dose of sedatives."

        n "Ah, thank you…just what I needed."
        n "Would you like some too, little princess?"

        z "No, thank you."

        "I had hoped that my response would deter him, but he poured me a cup anyway and handed it to me."
        show nef sad
        n "Come now, I'm sure you must be parched after all that dancing."

        show bzuleika sad hidden
        z "No, really, I'm fine."
        show bzuleika normal hidden
        z "But thank you for offering."

        show nef angry
        n "Please, I insist."
        "This wasn't looking good..."
        "I took the cup and sat with it, waiting for him to take a drink."
        show nef
        n "Go on, drink up."
    
        z "Wouldn't you rather I sing something for you? I know the perfect song."
        show nef angry
        "Nefferon frowned at me, and for a moment, I feared that he had caught on."
        show nef
        n "Very well."
    
        scene bg black with fade
        play music "Audio/Music/A Mission.ogg"
        "He took a drink, and within seconds, he was fast asleep...just in time, too, judging from the commotion I could hear going on outside."

        "I motioned to the maid servant, who was still nearby, and she brought a pile of heavy-duty rope. The two of us proceeded to bind the emperor’s hands and feet as tight as we could manage."

        "I could hear swords clashing and took a peak outside, but I couldn't tell which side was winning."
        "I suddenly worried about Duren; he was an excellent fighter, but would he be okay?"
        stop music
        scene bg ballroom with fade
        "Just then, the doors burst open and soldiers filled the room."
    
        play music "Audio/Music/Second Coming (Title Screen).ogg"
        show duren with dissolve
        "I was relieved to see that it was, in fact, Duren standing at the door commanding them."

        "As a couple of soldiers carried the unconscious and bound Nefferon off to the dungeons, Duren came over to me and, much to my surprise, hugged me."

        d "It's all over now…we won."
        show duren blush
        d "Thank you so much for everything you've done, Zuleika. I couldn't have done it without you."
        show duren

        so "Prince Duren, I believe this is yours."
        "He handed him Nefferon's crown, which he rarely wore, but which signified his rank as the Emperor of the High Court."

        "With the transfer of the crown, that title fell upon the young angel's shoulders, and he accepted it gracefully."
        d "With this, I vow to serve the people, to serve my country, and to change the nation of Tyraca for the better."

        play sound "Audio/Sound/applause.ogg"
        "Everyone applauded and cheered for the new emperor."
        
        jump alldurenendingB
        
    else:
        stop music
        scene bg black with fade
        "As I planned with Duren, I asked Nefferon to meet me in the ballroom after everyone else had gone home."
        "I was nervous, of course, but I knew I had to be strong and push my fear aside, for all of our sakes."
    
        scene bg ballroom with fade
        play music "Audio/Music/Rising Game (Nefferon Theme).ogg"
        show nef with dissolve
        n "I didn't expect you to wish to meet with me like this, Princess...after all, we have a date in my chambers tomorrow, remember?"
    
        show bzuleika normal hidden
        z "I've just enjoyed our recent visits so much, Your Majesty, that I simply couldn't wait to see you again."
    
        show nef happy
        n "Is that so?"
        show nef
        n "Well, then, I suppose I shouldn't deny a lady's request."
    
        "Right on schedule, one of the maid servants brought us some freshly brewed tea."
        "Thanks to my preparations, however, the tea was specially brewed with a heavy dose of sedatives."

        n "Ah, thank you…just what I needed."
        n "Would you like some too, little princess?"

        z "No, thank you."

        "I had hoped that my response would deter him, but he poured me a cup anyway and handed it to me."
        show nef sad
        n "Come now, I'm sure you must be parched after all that dancing."

        show bzuleika sad hidden
        z "No, really, I'm fine."
        show bzuleika normal hidden
        z "But thank you for offering."

        show nef angry
        n "Please, I insist."
        "This wasn't looking good..."
        "I took the cup and sat with it, waiting for him to take a drink."
        show nef
        n "Go on, drink up."
    
        z "Wouldn't you rather I sing something for you? I know the perfect song."
        show nef angry
        "Nefferon frowned at me, and for a moment, I feared that he had caught on."
        show nef
        n "Very well."
    
        scene bg black with fade
        play music "Audio/Music/A Mission.ogg"
        "He took a drink, and within seconds, he was fast asleep...just in time, too, judging from the commotion I could hear going on outside."

        "I motioned to the maid servant, who was still nearby, and she brought a pile of heavy-duty rope. The two of us proceeded to bind the emperor’s hands and feet as tight as we could manage."

        "I could hear swords clashing and took a peak outside, but I couldn't tell which side was winning."
        "I suddenly worried about Duren; he was an excellent fighter, but would he be okay?"
        stop music
        scene bg ballroom with fade
        "Just then, the doors burst open and soldiers filled the room."
    
        play music "Audio/Music/Second Coming (Title Screen).ogg"
        show duren with dissolve
        "I was relieved to see that it was, in fact, Duren standing at the door commanding them."

        "As a couple of soldiers carried the unconscious and bound Nefferon off to the dungeons, Duren came over to me and, much to my surprise, hugged me."

        d "It's all over now…we won."
        show duren blush
        d "Thank you so much for everything you've done, Zuleika. I couldn't have done it without you."
        show duren

        so "Prince Duren, I believe this is yours."
        "He handed him Nefferon's crown, which he rarely wore, but which signified his rank as the Emperor of the High Court."

        "With the transfer of the crown, that title fell upon the young angel's shoulders, and he accepted it gracefully."
        d "With this, I vow to serve the people, to serve my country, and to change the nation of Tyraca for the better."

        play sound "Audio/Sound/applause.ogg"
        "Everyone applauded and cheered for the new emperor."
        
label alldurenendingB:
    
    if ending == "Stay with Duren":
        scene duren hand ballroom with dissolve
        $ persistent.durenhandballroom = True
        "Duren's eyes locked with mine, and he held out his hand to me."

        d "Are you ready, Zuleika?"
        "I nodded happily and took his hand."
        scene bg ballroom with dissolve
        show duren with dissolve
        "He addressed the crowd now."
        show duren happyblush
        d "This is my new royal adviser, Lady Zuleika."
        play sound "Audio/Sound/applause.ogg"
        "As the crowd applauded, we smiled and looked at each other, still holding hands."
        show duren blush
        d "I'm so happy that you're here with me. Together, we'll make this country great again."
        show bzuleika normalblush hidden
        z "I know. You'll make a fine emperor, Duren."
        
        stop music
        scene bg blank with fade
        show journal with dissolve

        "Thus began a long age of peace and prosperity for the nation of Tyraca."
        "The two of us ruled the nation together for many years, and we would be remembered fondly for many more."
        
        "And that...is my story.\n\n(( Ending 11 of 15 ))"
        with Pause(.5)

        $ persistent.ending11 = True
            
        jump end
        
    elif ending == "Leave":
        play music "Audio/Music/The Parting.ogg"
        "I was happy for him, and I knew that he would make an excellent emperor."
        "However, I was sure that my place was elsewhere, not here in the castle. That's why..."
        show duren sad
        "Duren's eyes met mine as I tried to move away from the growing crowd around him."
        "He looked sad, but he nodded as a signal that he understood. He was, truly, a good friend."
        hide duren with dissolve
        "As difficult as it was to pull myself away from his friendly gaze, the one I had known and loved for so long, I knew I had to do it."
        "It was time that I saw the world with my own eyes and learned what life was all about; I couldn't hide in the castle forever."
        scene bg black with fade
        "Thus, I turned around and started walking...out into the hall, then out to the courtyard, then out the castle gates and beyond without looking back."
        "I didn't know where I would end up or if I would ever return, but I knew that I would keep going no matter what came my way."
        "I was, after all, no longer the princess of the Osirian Empire, but Zuleika the Courageous, a name that was mine and mine alone."
        
        stop music
        "And that...is my story.\n\n(( Ending 12 of 15 ))"
        with Pause(.5)

        $ persistent.ending12 = True
            
        jump end
        
label allballchaelB:
    scene bg bedroom with fade
    "The night of the ball, I sat in my bedroom, waiting for my date to arrive."
    "It was already getting late, and I was worried that he may not come after all..."
    
    "That's when, suddenly, a white-clad figure appeared through my window."
    play music "Audio/Music/Dreamy Flashback.ogg"
    show chael with moveinleft
    u "I see you still haven't fixed your window..."
    show bzuleika angry hidden
    z "Hey...aren't you that assassin who came to kill me a few months ago?"
    
    c "...My name is Prince Chael of the nation of Nalan."
    show chael happy
    c "It's so good to finally meet you, Princess. You're even more beautiful than I imagined."
    
    z "Hey, don't change the subject. I'm 100,000 Gold in debt thanks to you!"
    show chael sad
    z "Don't they know how to use doors in Nalan?"
    
    c "Actually.....no, nevermind."
    show chael
    c "Are you ready, Princess?"
    
    show bzuleika normal hidden
    z "As ready as I'll ever be. Let's go."
    
    stop music
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    
    "By the time we arrived at the ball, the room was full of guests, many of which I recognized as nobles from the High Court."
    "We weren't left to enjoy the scenery for long, however..."
    
    show duren sad with dissolve
    d "...Lord Chael? What are you doing here?"
    d "There's no way you were invited..."
    show duren angry
    d "Wait...don't tell me that {i}you{/i} are her date for tonight!"
    
    show bzuleika sad hidden
    z "He is, Duren, so please...don't start anything."
    
    hide duren
    show chael angry2 at left
    show duren sad at right
    with dissolve
    c "You should listen to her, Duren."
    c "I'm not here to cause trouble; I'm just here to dance with the princess."
    
    play music "Audio/Music/Power Restored.ogg"
    d "It's not me that you should be worried about..."
    
    hide duren
    hide chael
    show nef angry
    n "You! How dare you come here, Nalani scum?"
    n "Guards! Seize him!"
    hide nef
    
    show chael angry
    c "Not again..."
    with Pause(.5)
    show chael
    c "Come, Princess. It's time to take our leave."
    
    stop music
    scene bg black with fade
    "He suddenly picked me up and started running...out into the hall, then out to the courtyard, then out the castle gates and beyond."
    play music "Audio/Music/Atlantean Twilight.ogg"
    scene bg night with fade
    
    "We finally stopped in a small clearing, with the starlit sky hanging above us."
    
    show chael
    c "Are you okay, Princess?"
    
    show bzuleika normal hidden
    z "I'm fine...though I think all that excitement wore me out."
    
    c "Do you think you still have enough energy left for a dance?"
    
    show bzuleika sad hidden
    z "But there's no music to dance to..."
    
    show chael happy
    c "You can't always dance to the music given to you, Princess..."
    c "Sometimes, you just have to make your own."
    
    scene bg black with fade
    "And so we danced for hours under the stars, moving in rhythm to the beat of our own hearts..."
    with Pause(2)
    "Though Prince Chael and I went our separate ways after that night, I never forgot what he taught me about making my own music...and forging my own destiny."
    "I soon made the decision to leave the castle and the life I once knew, never to return."
    "I didn't know where I would end up, but I knew that I would keep going no matter what came my way."
    "I was, after all, no longer the princess of the Osirian Empire, but Zuleika the Courageous, a name that was mine and mine alone."
    
    stop music
    "And that...is my story.\n\n(( Ending 14 of 15 ))"
    with Pause(.5)

    $ persistent.ending14 = True
            
    jump end
    
label allballkirileB:
    scene bg bedroom with fade
    "The night of the ball, I sat in my bedroom, waiting for my date to arrive."
    "It was already getting late, and I was worried that he may not come after all..."
    
    "That's when, suddenly, a black-clad figure tumbled through my window, landing on his back."
    play music "Audio/Music/Radio Martini (Kirile Theme).ogg"
    show kirile sad
    u "I expected there to be a window there to break..."
    show bzuleika angry hidden
    z "Yeah, well, you're not the first idiot to jump through my window."
    z "Why didn't you just use the door like a normal person?"
    show kirile angry
    u "Hey, a man's gotta make a dramatic entrance."
    z "You certainly did that..."
    show kirile
    "He stood up quickly and bowed."
    k "My name is Prince Kirile of the nation of Pyralis."
    show kirile happy
    k "It was definitely worth the long trip to get here tonight. You look amazing!"
    
    show bzuleika happyblush hidden
    z "Aw, thank you."
    show bzuleika normal hidden
    z "Shall we go?"
    
    show kirile
    k "After you, milady."
    
    stop music
    scene bg ballroom with fade
    play music "Audio/Music/Court of the Queen (Ball).ogg"
    
    "By the time we arrived at the ball, the room was full of guests, many of which I recognized as nobles from the High Court."
    "We weren't left to enjoy the scenery for long, however..."
    
    show duren angry with dissolve
    d "Who are you? You weren't invited."
    
    show bzuleika angry hidden
    z "What do you mean he wasn't invited?"
    
    hide duren
    show kirile sad2 at left
    show duren angry at right
    with dissolve
    
    k "Well, about that..."
    
    show kirile 2 at left
    k "C'mon, can't we just let it slide this time?"
    k "I'm not here to cause any trouble; I just wanna dance with the princess."
    
    show duren sad at right
    play music "Audio/Music/Power Restored.ogg"
    d "It's not me that you should be worried about..."
    
    hide duren
    hide kirile
    show nef angry
    n "You! How dare you come here, filthy demon?"
    n "Guards! Seize him!"
    hide nef
    
    show kirile
    k "As much as I would love to stay and fight with you guys..."
    k "Time to go, lass."
    
    stop music
    scene bg black with fade
    "He suddenly picked me up and started running...out into the hall, then out to the courtyard, then out the castle gates and beyond."
    play music "Audio/Music/Atlantean Twilight.ogg"
    scene bg night with fade
    
    "We finally stopped in a small clearing, with the starlit sky hanging above us."
    
    show kirile happy
    k "Well, that was fun."
    
    show bzuleika angry hidden
    z "If I'd known that you weren't invited..."
    
    show kirile
    k "Sometimes, lass, you can't just wait for others to invite you. You have to make your own invitation, make your own decisions."
    show kirile happy
    k "That's my philosophy, anyway."
    
    z "And just look how well it worked out."
    
    show kirile
    k "Oh, c'mon...who wanted to dance around in that stuffy old ballroom, anyway?"
    show kirile happy
    k "I think things worked out perfectly."
    
    show bzuleika normal hidden
    z "I suppose you're right."
    show bzuleika happy hidden
    z "It's much more beautiful out here, plus there aren't any snooty nobles to contend with."
    
    k "See? Perfect!"
    
    scene bg black with fade
    "We talked and laughed for hours under the stars, just forgetting our worries and enjoying the moment together..."
    with Pause(2)
    "Though Prince Kirile and I went our separate ways after that night, I never forgot what he taught me about taking chances and making my own decisions."
    "I soon decided to leave the castle and the life I once knew, never to return."
    "I didn't know where I would end up, but I knew that I would keep going no matter what came my way."
    "I was, after all, no longer the princess of the Osirian Empire, but Zuleika the Courageous, a name that was mine and mine alone."
    
    stop music
    "And that...is my story.\n\n(( Ending 15 of 15 ))"
    with Pause(.5)

    $ persistent.ending15 = True
            
    jump end