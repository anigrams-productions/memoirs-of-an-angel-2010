# Story B
# Chapter 00: Making the Decision
label allprologueB:
    "He once again took out his knife and prepared to strike."
    "Before the assassin could make a move, however, another young man came to the my rescue."
    hide assassin with dissolve
    
    show assassin 2 at left
    show duren angry at right
    with dissolve
    
    "It was none other than Prince Duren, the angel of the new emperor and my closest friend."
    d "Don't worry, Zuleika. I won't let this man hurt you."
    hide assassin 2
    
    show assassin at left
    hide assassin with moveoutleft
    "Duren readied his bow and shot at the assassin, narrowly missing..."
    
    stop music
    play sound "Audio/Sound/glass_breaking.ogg"
    "...as he lunged himself out the nearest window, vanishing into the scenery below."
    hide duren with dissolve
    
    play music "Audio/Music/Silver Blue Light (Duren Theme).ogg"
    
    show duren with dissolve
    d "Are you alright?"
    
    show zuleika normal hidden
    z "Yes, I'm fine."
    show zuleika happy hidden
    z "Thanks, Duren. You really saved me there."
    
    show duren sad
    d "I'm just glad you're safe…I don't know what I would have done if something had happened to you."
    show duren
    d "Why don’t you get some rest?"
    d "I'll secure one of the extra bedrooms for you and have guards stationed outside. We'll make sure he doesn't come back."
    
    hide duren with dissolve
    "I nodded, but I doubted that I would be able to sleep easily that night."
    "Though it had not been easy, I had made my decision: I would accept the emperor's offer and remain in the castle."
    
    call status from _call_status_9
    $ duren_in_party = True
    
    jump allchp1B