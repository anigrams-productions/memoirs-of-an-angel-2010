init:
    image intro23 = "Images/Intro/AnigramsIntro23.jpg"
    image intro45 = "Images/Intro/AnigramsIntro45.jpg"
    image logoA = Animation("Images/Intro/ASide.png", 0.1, "Images/Intro/ATurn2B.png", 0.1, "Images/Intro/ATurn2.png", 0.1, "Images/Intro/A.png", 1.5, "Images/Intro/ATurn.png", 0.1, "Images/Intro/ATurnB.png", 0.1, "Images/Intro/ASide.png", 0.1, "Images/Intro/PTurn2B.png", 0.1, "Images/Intro/PTurn2.png", 0.1, "Images/Intro/P.png", 1.5, "Images/Intro/PTurn.png", 0.1, "Images/Intro/PTurnB.png", 0.1, "Images/Intro/ASide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoN = Animation("Images/Intro/NSide.png", 0.1, "Images/Intro/NTurn2B.png", 0.1, "Images/Intro/NTurn2.png", 0.1, "Images/Intro/N.png", 1.5, "Images/Intro/NTurn.png", 0.1, "Images/Intro/NTurnB.png", 0.1, "Images/Intro/NSide.png", 0.1, "Images/Intro/R2Turn2B.png", 0.1, "Images/Intro/R2Turn2.png", 0.1, "Images/Intro/R2.png", 1.5, "Images/Intro/R2Turn.png", 0.1, "Images/Intro/R2TurnB.png", 0.1, "Images/Intro/NSide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoI = Animation("Images/Intro/ISide.png", 0.1, "Images/Intro/ITurn2B.png", 0.1, "Images/Intro/ITurn2.png", 0.1, "Images/Intro/I.png", 1.5, "Images/Intro/ITurn.png", 0.1, "Images/Intro/ITurnB.png", 0.1, "Images/Intro/ISide.png", 0.1, "Images/Intro/ETurn2B.png", 0.1, "Images/Intro/ETurn2.png", 0.1, "Images/Intro/E.png", 1.5, "Images/Intro/ETurn.png", 0.1, "Images/Intro/ETurnB.png", 0.1, "Images/Intro/ISide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoG = Animation("Images/Intro/GSide.png", 0.1, "Images/Intro/GTurn2B.png", 0.1, "Images/Intro/GTurn2.png", 0.1, "Images/Intro/G.png", 1.5, "Images/Intro/GTurn.png", 0.1, "Images/Intro/GTurnB.png", 0.1, "Images/Intro/GSide.png", 0.1, "Images/Intro/S2Turn2B.png", 0.1, "Images/Intro/S2Turn2.png", 0.1, "Images/Intro/S2.png", 1.5, "Images/Intro/S2Turn.png", 0.1, "Images/Intro/S2TurnB.png", 0.1, "Images/Intro/GSide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoR = Animation("Images/Intro/RSide.png", 0.1, "Images/Intro/RTurn2B.png", 0.1, "Images/Intro/RTurn2.png", 0.1, "Images/Intro/R.png", 1.5, "Images/Intro/RTurn.png", 0.1, "Images/Intro/RTurnB.png", 0.1, "Images/Intro/RSide.png", 0.1, "Images/Intro/E2Turn2B.png", 0.1, "Images/Intro/E2Turn2.png", 0.1, "Images/Intro/E2.png", 1.5, "Images/Intro/E2Turn.png", 0.1, "Images/Intro/E2TurnB.png", 0.1, "Images/Intro/RSide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoA2 = Animation("Images/Intro/ASide.png", 0.1, "Images/Intro/ATurn2B.png", 0.1, "Images/Intro/ATurn2.png", 0.1, "Images/Intro/A.png", 1.5, "Images/Intro/ATurn.png", 0.1, "Images/Intro/ATurnB.png", 0.1, "Images/Intro/ASide.png", 0.1, "Images/Intro/N2Turn2B.png", 0.1, "Images/Intro/N2Turn2.png", 0.1, "Images/Intro/N2.png", 1.5, "Images/Intro/N2Turn.png", 0.1, "Images/Intro/N2TurnB.png", 0.1, "Images/Intro/ASide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoM = Animation("Images/Intro/MSide.png", 0.1, "Images/Intro/MTurn2B.png", 0.1, "Images/Intro/MTurn2.png", 0.1, "Images/Intro/M.png", 1.5, "Images/Intro/MTurn.png", 0.1, "Images/Intro/MTurnB.png", 0.1, "Images/Intro/MSide.png", 0.1, "Images/Intro/TTurn2B.png", 0.1, "Images/Intro/TTurn2.png", 0.1, "Images/Intro/T.png", 1.5, "Images/Intro/TTurn.png", 0.1, "Images/Intro/TTurnB.png", 0.1, "Images/Intro/MSide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    image logoS = Animation("Images/Intro/SSide.png", 0.1, "Images/Intro/STurn2B.png", 0.1, "Images/Intro/STurn2.png", 0.1, "Images/Intro/S.png", 1.5, "Images/Intro/STurn.png", 0.1, "Images/Intro/STurnB.png", 0.1, "Images/Intro/SSide.png", 0.1, "Images/Intro/STurn2B.png", 0.1, "Images/Intro/STurn2.png", 0.1, "Images/Intro/S.png", 1.5, "Images/Intro/STurn.png", 0.1, "Images/Intro/STurnB.png", 0.1, "Images/Intro/SSide.png", 0.1, "Images/Intro/LetterBlank.png", 60)
    
# Splashscreen is shown before main menu is loaded.
# ("Anigrams Presents" animation)
label splashscreen:
    scene black
    with Pause(.5)
    
    show logoA at Position(xpos = 153, ypos = 320)
    with Pause(.1)
    show logoN at Position(xpos = 225, ypos = 320)
    with Pause(.1)
    show logoI at Position(xpos = 297, ypos = 320)
    with Pause(.1)
    show logoG at Position(xpos = 369, ypos = 320)
    with Pause(.1)
    show logoR at Position(xpos = 441, ypos = 320)
    with Pause(.1)
    show logoA2 at Position(xpos = 513, ypos = 320)
    with Pause(.1)
    show logoM at Position(xpos = 585, ypos = 320)
    with Pause(.1)
    show logoS at Position(xpos = 657, ypos = 320)
    
    with Pause(5)
    
    return