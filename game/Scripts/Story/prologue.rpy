# When "New Game" is chosen from main menu, game starts here.
label start:
    # hide all menus and other screens
    $ show_button_main_menu = False
    hide screen adventure
    hide screen story1
    
    scene bg black
    stop music fadeout 1.0

    play music "Audio/Sound/pencil-1.ogg" fadein 0.5
    
    scene bg blank with fade
    show journal with dissolve
    
    "Angels..."
    "They are beings created to serve and protect the gods, their creators."
    "Most take the form of winged beasts who guard their masters dutifully, but in some rare cases, angels can take human form."
    "There are only a few such angels in the whole world...\nand I happen to be one of them."
    "My name is Zuleika, and I am the princess of the nation of Tyraca, home of the Osirian Empire."
    "I'm also well-known for being... "
    
    stop music
    
menu:
    "...a brilliant strategist.":
        $ zuleika_type = 'intelligent'
        jump allprologue
    "...a fearless warrior.":
        $ zuleika_type = 'strong'
        jump allprologue
    "...a charismatic diplomat.":
        $ zuleika_type = 'charming'
        jump allprologue
    "...a defender of the people.":
        $ zuleika_type = 'kind'
        jump allprologue
    "...a well-rounded ruler." if persistent.choice_unlocked == True:
        $ zuleika_type = 'all'
        jump allprologue
        
label allprologue:
    if zuleika_type == 'intelligent':
        $ increase_intelligence(100)
        $ increase_strength(25)
        $ increase_charm(50)
        $ increase_kindness(50)
        $ investigative_skill = 0
    elif zuleika_type == 'strong':
        $ increase_intelligence(25)
        $ increase_strength(100)
        $ increase_charm(50)
        $ increase_kindness(50)
        $ battle_skill = 0
    elif zuleika_type == 'kind':
        $ increase_intelligence(50)
        $ increase_strength(50)
        $ increase_charm(25)
        $ increase_kindness(100)
        $ gifting_skill = 0
        $ item_bouquet = 0
        $ item_makeup = 0
        $ item_liquor = 0
        $ item_knives = 0
        $ item_spellbook = 0
        $ item_earrings = 0
        $ item_flowers = 0
        $ item_shell = 0
        $ item_herbs = 0
        $ item_arrowhead = 0
        $ item_fruit = 0
        $ item_coin = 0
    elif zuleika_type == 'charming':
        $ increase_intelligence(50)
        $ increase_strength(50)
        $ increase_charm(100)
        $ increase_kindness(25)
        $ dancing_skill = 0
    elif zuleika_type == 'all':
        $ increase_intelligence(50)
        $ increase_strength(50)
        $ increase_charm(50)
        $ increase_kindness(50)
        $ investigative_skill = 0
        $ battle_skill = 0
        $ gifting_skill = 0
        $ dancing_skill = 0
        $ item_bouquet = 0
        $ item_makeup = 0
        $ item_liquor = 0
        $ item_knives = 0
        $ item_spellbook = 0
        $ item_earrings = 0
        $ item_flowers = 0
        $ item_shell = 0
        $ item_herbs = 0
        $ item_arrowhead = 0
        $ item_fruit = 0
        $ item_coin = 0
        
    play music "Audio/Sound/pencil-1.ogg" fadein 0.5
    scene bg blank
    show journal
    
    "Or, at least I {i}was{/i}."
    "As Tyraca went through a period of radical change, my life, too, was turned upside-down. "
    "...This is where my story begins. "
    
    stop music fadeout 1.0
    scene bg black with fade
    with Pause(1.5)
    
    play music "Audio/Music/Final Count.ogg"
    scene fire with fade
    with Pause(.5)
    
    show prologue tyrant at truecenter
    with dissolve
        
    "The long, bloody War of the Nations, which engulfed the entire continent in a struggle for power and land for nearly a decade, had finally ended with the death of my master, the mighty Tyracan emperor Osirus the Great. "
    "During this time, dozens of villages throughout Tyraca were destroyed, and the war left many people without homes or food, not to mention the thousands of lives lost in the battles themselves. "
    
    show prologue emperor at truecenter with dissolve
    
    "The empty throne was quickly filled by Nefferon the Cruel, the late emperor's younger brother, who played off of the corruption of the High Court to take the seat of power for himself. "
    "He had no apparent interest in helping to rebuild the nation that was destroyed by his brother’s war, and instead seemed to focus solely on satisfying the rich noblemen who supported him. "
    
    show prologue princess at truecenter with dissolve
    
    "To make matters worse, I was forced out of my position by the High Court, who despised the idea of a woman in power, much less an angel. "
    "The new Emperor Nefferon, however, offered to allow me to stay in the castle, as I had no where else to go. "
    "He had one condition...that I be his personal servant. "
    
    scene bg black with fade
    
    "I was now faced with what would be the most important decision of my life. "
    "Would I stay in the castle I had lived in all my life, even if I had to serve the man who killed my master, in order to fight the corruption of the Court from within? "
    "Or would I leave the only life I had ever known to live as a peasant, trying to repair the damage that had been done to the kingdom one step at a time? "
     
    stop music
    
    play sound "Audio/Sound/Nighttime.ogg"
    scene bg bedroom with fade
    with Pause(1)
    
    scene bg night with dissolve
    play music "Audio/Music/Lamentation (Sad Zuleika Theme).ogg"
    
    "That night, I sat in my bedroom, staring out at the starry sky and contemplating my next move. "
    
    show zuleika sad hidden
    z "Perhaps this is punishment for what Emperor Osirus and I did during the war... "
    
    show zuleika angry hidden
    
    if zuleika_type == 'strong':
        z "I killed many soldiers while on the front lines, most of whom had families waiting for them back home, but what else could I have done? "
    elif zuleika_type == 'charming':
        z "Many people suffered because of the deals I made to help Osirus win his battles, but what else could I have done? "  
    else:
        z "Many people suffered because of how I used my gift of foresight to help Osirus win his battles, but what else could I have done? "
    z "Osirus ordered me to do it, and as his angel, I couldn't disobey...or at least, that's what I tell myself. "
    
    show zuleika sad hidden
    z "He had told me that it was for the people, for the nation we both loved…and I believed him, even though I knew in my heart it was wrong. "
    
    show zuleika angry hidden
    z "He had gone mad with power, but I refused to admit it. "
    
    show zuleika sad hidden
    z "This was the man who created me, after all…the man who always smiled, who showered me with gentle affection. "
    z "He was the man who united the quarrelling kingdoms long ago and created the Osirian Empire, where, for decades, there were only peace and prosperity. "
    z "He was a man who was once filled with pride and honor and love for his people. " 
    
    show zuleika angry hidden
    z "I can't believe that he became such a monster..."
    show zuleika sad hidden
    z "…and now, I can't believe that he's gone forever. "
     
    stop sound
    stop music
    scene bg black
    
    play sound "Audio/Sound/glass_breaking.ogg"
    "Suddenly, the sound of glass breaking and shouting outside disturbed me from my thoughts. "
    play music "Audio/Music/Ghostpocalypse - 7 Master (Chase).ogg"
    g "Intruder! "
    g "Get the intruder! "
     
    scene bg bedroom
    show assassin with moveinright
    
    "Before I knew it, the intruder was there, in my bedroom, with a knife in hand. "
    "I was positive – this truly was my punishment. "
    "I looked my assassin in the eye, ready to accept my due punishment for the lives I helped destroy. "
    "He looked right back into mine, in position to deal the life-ending strike at any moment. "
    "I couldn’t help but notice his features: long, silver hair and ice blue eyes. "
    show zuleika normal hidden
    z "(He must be a Nalani, and a beautiful one at that. And those wings...is he an angel?) "
    stop music
    
    play music "Audio/Music/Finding the Balance (Chael Theme).ogg"
    scene chael hand with dissolve
    $ persistent.chaelhand = True
    "But to my surprise, he put away his knife and instead held out his hand. "
    a "...I do not wish to kill you."
    a "Come with me, Princess…I'll take you away from here, before someone else is sent to finish the job."
    "Shocked, I simply stared at him. I couldn't believe this was happening. "
    a "Hurry! Take my hand."
     
    "This was my best opportunity to get out of the castle and start a new life, one where I could help rebuild my beloved nation. "
    "But to leave with a strange man who came here to kill me could be dangerous… "
    
menu:
    "Take his hand":
        "I took the strange assassin’s hand, knowing that this was probably my only chance to get out of the castle and live the life I always wanted. "
        scene bg black
        stop music
        with fade
        $ CAffection += 20
        $ KAffection += 20
        $ princess = False
        
        "Obtained \"Warrior's Garb\" and 500 Gold."
        $ gold += 500
        
        jump allchp1A
        
    "\"I'm sorry, but I can't.\"":
        stop music
        
        scene bg bedroom with dissolve
        show assassin with dissolve
        
        play music "Audio/Music/Ghostpocalypse - 7 Master (Chase).ogg"
        $ DAffection += 20
        $ NAffection += 20
        a "Very well, then.\nI'm afraid I have no other choice... "
        a "At the very least, I will try to grant you a quick death."
        
        jump allprologueB