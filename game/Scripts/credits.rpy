init:
    image credits1 = "Images/Credits/Credits1.jpg"
    image credits1_2 = "Images/Credits/Credits1-2.jpg"
    image credits2 = "Images/Credits/Credits2.jpg"
    image credits2_2 = "Images/Credits/Credits2-2.jpg"
    image credits3 = "Images/Credits/Credits3.jpg"
    image credits3_2 = "Images/Credits/Credits3-2.jpg"
    image credits4 = "Images/Credits/Credits4.jpg"
    image credits4_2 = "Images/Credits/Credits4-2.jpg"
    image credits5 = "Images/Credits/Credits5.jpg"
    image credits5_2 = "Images/Credits/Credits5-2.jpg"
    image credits6 = "Images/Credits/Credits6.jpg"
    
label end:    
    $ persistent.choice_unlocked = True
    
    play music "Audio/Music/Fairytale Waltz (Credits).ogg"
    
    scene black with fade
    with Pause(2)
    
    scene credits1 with fade
    with Pause(2)
    
    scene credits1_2 with dissolve
    with Pause(2)
    
    scene black with fade
    with Pause(1)
    
    scene credits2 with fade
    with Pause(2)
    
    scene credits2_2 with dissolve
    with Pause(3)
    
    scene black with fade
    with Pause(1)
    
    scene credits3 with fade
    with Pause(2)
    
    scene credits3_2 with dissolve
    with Pause(3)
    
    scene black with fade
    with Pause(1)
    
    scene credits4 with fade
    with Pause(2)
    
    scene credits4_2 with dissolve
    with Pause(3)
    
    scene black with fade
    with Pause(1)
    
    scene credits5 with fade
    with Pause(2)
    
    scene credits5_2 with dissolve
    with Pause(3)
    
    scene black with fade
    with Pause(.5)
    
    scene credits6 with fade
    with Pause(1.5)
       
    stop music
    
    scene black with fade
    with Pause(.5)
       
    return
