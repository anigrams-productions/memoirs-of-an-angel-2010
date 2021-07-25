# Story A
# Chapter 00: Starting Out on a Journey
label allchp1A:
    scene bg hallway night with dissolve
    play music "Audio/Music/Ghostpocalypse - 7 Master (Chase).ogg"
    
    "We quickly started to make our escape, rushing down the corridor with limited supplies in hand. "
    "However, we didn't get far before an arrow whizzed past us. "
     
    u "Unhand her, intruder!\nI will not allow you to go any further. "
    show duren angry with dissolve
    "We turned to see none other than Prince Duren, Emperor Nefferon’s angel and my closest friend. "
    "I couldn't help feeling a sinking feeling in the pit of my stomach. I was hoping I wouldn't have to confront him like this... "
    d "Zuleika, I swear on my life that I won't let this man harm you. "
    
    show zuleika sad hidden
    z "Wait, Duren, this isn't what you - "
    
    show duren angry at right with move
    show assassin 2 at left
    with dissolve
    
    "But before I could finish, the prince shot another arrow at the assassin, who dodged it, picked me up, and started running full-speed. "
    hide assassin 2
    show assassin at left
    "Duren followed close behind, bow and arrow in hand, waiting for an opportunity to strike. "
    hide assassin with moveoutleft
    
    scene bg black with fade
    
    "Just when it seemed that we were at a dead end, the assassin lunged himself out of the only exit - "
    scene chael windo with dissolve
    $ persistent.chaelwindo = True
    stop music
    play sound "Audio/Sound/Glass_Crash.ogg"
    "a large window - and spread his large, white wings, propelling him into the sky with me hanging on tightly. "
    
    show zuleika sad hidden
    "I could hear my friend calling after me, but there was no turning back now. "
    z "I'm sorry, Duren...but this is where our paths must part."
      
    scene bg stream with fade
    with Pause(.5)
    play music "Audio/Music/Open Those Bright Eyes (Zuleika Theme).ogg"
    "The next morning, I woke up to the smell of something delicious cooking over a fire. "
    u "It's late."
    show chael with dissolve
    "It took me a minute to remember the events of the night before and to realize that this was the assassin, now unmasked, who had come to kill me just hours earlier. "
    
    show wzuleika normal hidden
    z "Oh, hello there. "
    
    show wzuleika happy hidden
    z "I figured you would have left by now. "
    
    show chael angry
    "He merely 'hmph'ed in reply. "
    
    show wzuleika normal hidden
    show chael
    z "I don't believe we were ever properly introduced. "
    z "I'm Zuleika, as you probably already know. And you are...? "
    
    show chael angry
    c "...If you must call me something, then 'Chael' will do. "
    
    "I paused for a moment, taking in the name. "
    
    show wzuleika sad hidden
    z "Wait...{i}the{/i} Chael? "
    z "As in the assassin from Nalan who slayed a hundred men in a single battle? "
    
    show chael angry2
    "The man silently turned back to the fire, obviously ignoring my question. "
    
menu:
    "\"Why did you save me?\"":
        jump allpain
    "\"What are your plans from here?\"":
        jump allplans
    "\"What's for breakfast?\"":
        jump allbreakfast
        
label allpain:
    $ CAffection += 20
    scene bg stream
    stop music
    show chael angry
    play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
    
    "The question seemed to have struck a chord, and I wasn't sure whether that was good or bad. "
    "He was silent for a moment, then replied quietly, almost whispering. "
    c "I saw it, in your eyes…the pain of someone who has caused many deaths and regrets each one. "
    show chael sad
    c "I…understand that pain. "
    
    show chael angry2
    "He turned away quickly and became silent, as if he felt he had said too much. "
    
    show wzuleika sad hidden
    z "(He's so serious...) "
    
    stop music
    play music "Audio/Music/Open Those Bright Eyes (Zuleika Theme).ogg"
    
menu:
    "\"What are your plans from here?\"":
        jump allplans
    "\"What's for breakfast?\"":
        jump allbreakfast
        
label allbreakfast:
    scene bg stream
    show chael
    
    "Whatever he was cooking, it sure smelled good after all the excitement of the last several hours. "
    "I was starving! "
    
    c "Rabbit. "
    
    "Having been raised in the castle, I choked a little at the thought of eating one of the cute little bunnies I played with in the gardens, but I forced a cheerful smile. "
    
    show wzuleika happy hidden
    z "That...uh...sounds great. "
    
    "He nodded silently. "
    "I wasn't sure why this mysterious man, especially one with such a reputation, was doing all of this for me, but I was thankful either way. "
    
    z "Alright, let's eat! "
    
    jump allplans
        
label allplans:
    scene bg stream
    show chael
    
    c "Once you finish eating, it would be wise to start heading west towards the City of Jarconia. "
    c "Since the city is on the Pyralin border, you'll be able to acquire some weapons and supplies without drawing too much attention. "
    
    show wzuleika sad hidden
    z "Wait...{i}weapons?!{/i}"
    z "Whatever happened to starting new, peaceful lives? "
    show wzuleika angry hidden
    z "I'm a princess, not a warrior, you know. "
    
    "He looked at me with his usual serious, stoic expression. "
    show chael angry
    c "Your king will send men after you soon enough, and if the Holy Mother finds out that I failed to kill you..."
    show wzuleika sad hidden
    z "Holy Mother...?"
    "Again, he ignored my question."
    
    show chael
    c "Your first priority must be to protect yourself. Everything else is secondary. "
    
    show wzuleika normal hidden
    z "And what about you? What do you plan to do?"
    
    c "I will go with you."
    
    show wzuleika angry hidden
    
    z "What? Why?"
    
    c "Simple: I have nowhere else to go."
    
    z "Why don't you just go home and lie to whoever sent you?"
    
    show chael angry
    c "That is...not possible."
    
    z "Well, why not?"
    
    c "...You ask too many questions."
    c "If you do not leave this place soon, they will find you for sure."
    
    show wzuleika normal hidden
    
    z "Fine, fine. Let's go."
    
    call status from _call_status

    $ chael_in_party = True
    
    jump allchp2A