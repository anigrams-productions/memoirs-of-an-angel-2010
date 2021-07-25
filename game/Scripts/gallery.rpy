screen gallery_scenes():
    tag menu

    imagemap:
        ground "GUI/Gallery/scenes_ground.png"
        idle "GUI/Gallery/scenes_idle.png"
        hover "GUI/Gallery/scenes_hover.png"
        selected_idle "GUI/Gallery/scenes_selected_idle.png"
        selected_hover "GUI/Gallery/scenes_hover.png"

        hotspot (31,110, 153,30) action ShowMenu("gallery_scenes")
        hotspot (25,156, 165,38) action ShowMenu("gallery_endings")
        hotspot (28,204, 159,32) action ShowMenu("gallery_profiles")
        hotspot (30,250, 156,34) action Return()

        if persistent.chaelhand == True:
            hotspot (210,107, 155,112) action Show('chael_hand', transition=dissolve)
        if persistent.chaelwindo == True:
            hotspot (370,107, 155,112) action Show('chael_windo', transition=dissolve)
        if persistent.chaelcave == True:
            hotspot (530,107, 155,112) action Show('chael_cave', transition=dissolve)
        if persistent.chaelfinal == True:
            hotspot (210,227, 155,112) action Show('chael_final', transition=dissolve)
        if persistent.kirilecave == True:
            hotspot (370,227, 155,112) action Show('kirile_cave', transition=dissolve)
        if persistent.durenhandmountains == True:
            hotspot (530,227, 155,112) action Show('duren_hand_mountains', transition=dissolve)
        if persistent.durenhandballroom == True:
            hotspot (210,347, 155,112) action Show('duren_hand_ballroom', transition=dissolve)
        if persistent.nefviolentbedroom == True:
            hotspot (370,347, 155,112) action Show('nef_violent_bedroom', transition=dissolve)
        if persistent.nefviolenthallway == True:
            hotspot (530,347, 155,112) action Show('nef_violent_hallway', transition=dissolve)
        if persistent.nefdeath == True:
            hotspot (370,466, 155,112) action Show('nef_death', transition=dissolve)

screen chael_hand():
    imagemap:
        ground "Images/Events/ChaelHoldingOutHand.jpg"
        hotspot (0,0, 800,600) action Hide('chael_hand', transition=dissolve)

screen chael_windo():
    imagemap:
        ground "Images/Events/JumpingOutWindow.jpg"
        hotspot (0,0, 800,600) action Hide('chael_windo', transition=dissolve)

screen chael_cave():
    imagemap:
        ground "Images/Events/ChaelandZuleikainCave.jpg"
        hotspot (0,0, 800,600) action Hide('chael_cave', transition=dissolve)

screen chael_final():
    imagemap:
        ground "Images/Events/ChaelandZuleikaFinal.jpg"
        hotspot (0,0, 800,600) action Hide('chael_final', transition=dissolve)

screen kirile_cave():
    imagemap:
        ground "Images/Events/KirileandZuleikainCave.jpg"
        hotspot (0,0, 800,600) action Hide('kirile_cave', transition=dissolve)

screen duren_hand_mountains():
    imagemap:
        ground "Images/Events/DurenHoldingOutHandMountains.jpg"
        hotspot (0,0, 800,600) action Hide('duren_hand_mountains', transition=dissolve)

screen duren_hand_ballroom():
    imagemap:
        ground "Images/Events/DurenHoldingOutHandBallroom.jpg"
        hotspot (0,0, 800,600) action Hide('duren_hand_ballroom', transition=dissolve)

screen nef_violent_bedroom():
    imagemap:
        ground "Images/Events/NefferonandZuleikaViolentBedroom.jpg"
        hotspot (0,0, 800,600) action Hide('nef_violent_bedroom', transition=dissolve)

screen nef_violent_hallway():
    imagemap:
        ground "Images/Events/NefferonandZuleikaViolentHallway.jpg"
        hotspot (0,0, 800,600) action Hide('nef_violent_hallway', transition=dissolve)

screen nef_death():
    imagemap:
        ground "Images/Events/NefferonandZuleikaDeath.jpg"
        hotspot (0,0, 800,600) action Hide('nef_death', transition=dissolve)


screen gallery_endings():
    tag menu

    imagemap:
        ground "GUI/Gallery/endings_ground.png"
        idle "GUI/Gallery/endings_idle.png"
        hover "GUI/Gallery/endings_hover.png"
        selected_idle "GUI/Gallery/endings_hover.png"
        selected_hover "GUI/Gallery/endings_hover.png"

        hotspot (31,110, 153,30) action ShowMenu("gallery_scenes")
        hotspot (25,156, 165,38) action ShowMenu("gallery_endings")
        hotspot (28,204, 159,32) action ShowMenu("gallery_profiles")
        hotspot (30,250, 156,34) action Return()

        if persistent.ending0 == True:
            hotspot (294,124, 311,25) action Show('ending0', transition=dissolve)
        if persistent.ending1 == True:
            hotspot (295,152, 308,25) action Show('ending1', transition=dissolve)
        if persistent.ending2 == True:
            hotspot (290,180, 318,27) action Show('ending2', transition=dissolve)
        if persistent.ending3 == True:
            hotspot (275,210, 348,25) action Show('ending3', transition=dissolve)
        if persistent.ending4 == True:
            hotspot (268,238, 360,27) action Show('ending4', transition=dissolve)
        if persistent.ending5 == True:
            hotspot (267,268, 363,26) action Show('ending5', transition=dissolve)
        if persistent.ending6 == True:
            hotspot (292,298, 311,25) action Show('ending6', transition=dissolve)
        if persistent.ending7 == True:
            hotspot (283,327, 328,25) action Show('ending7', transition=dissolve)
        if persistent.ending8 == True:
            hotspot (283,356, 329,25) action Show('ending8', transition=dissolve)
        if persistent.ending9 == True:
            hotspot (277,384, 343,26) action Show('ending9', transition=dissolve)
        if persistent.ending10 == True:
            hotspot (258,414, 379,25) action Show('ending10', transition=dissolve)
        if persistent.ending11 == True:
            hotspot (274,442, 349,26) action Show('ending11', transition=dissolve)
        if persistent.ending12 == True:
            hotspot (282,472, 330,25) action Show('ending12', transition=dissolve)
        if persistent.ending13 == True:
            hotspot (277,500, 341,25) action Show('ending13', transition=dissolve)
        if persistent.ending14 == True:
            hotspot (274,529, 350,26) action Show('ending14', transition=dissolve)
        if persistent.ending15 == True:
            hotspot (276,558, 346,25) action Show('ending15', transition=dissolve)

screen ending0():
    imagemap:
        ground "GUI/Gallery/Ending0.jpg"
        hotspot (0,0, 800,600) action Hide('ending0', transition=dissolve)

screen ending1():
    imagemap:
        ground "GUI/Gallery/Ending1.jpg"
        hotspot (0,0, 800,600) action Hide('ending1', transition=dissolve)

screen ending2():
    imagemap:
        ground "GUI/Gallery/Ending2.jpg"
        hotspot (0,0, 800,600) action Hide('ending2', transition=dissolve)

screen ending3():
    imagemap:
        ground "GUI/Gallery/Ending3.jpg"
        hotspot (0,0, 800,600) action Hide('ending3', transition=dissolve)

screen ending4():
    imagemap:
        ground "GUI/Gallery/Ending4.jpg"
        hotspot (0,0, 800,600) action Hide('ending4', transition=dissolve)

screen ending5():
    imagemap:
        ground "GUI/Gallery/Ending5.jpg"
        hotspot (0,0, 800,600) action Hide('ending5', transition=dissolve)

screen ending6():
    imagemap:
        ground "GUI/Gallery/Ending6.jpg"
        hotspot (0,0, 800,600) action Hide('ending6', transition=dissolve)

screen ending7():
    imagemap:
        ground "GUI/Gallery/Ending7.jpg"
        hotspot (0,0, 800,600) action Hide('ending7', transition=dissolve)

screen ending8():
    imagemap:
        ground "GUI/Gallery/Ending8.jpg"
        hotspot (0,0, 800,600) action Hide('ending8', transition=dissolve)

screen ending9():
    imagemap:
        ground "GUI/Gallery/Ending9.jpg"
        hotspot (0,0, 800,600) action Hide('ending9', transition=dissolve)

screen ending10():
    imagemap:
        ground "GUI/Gallery/Ending10.jpg"
        hotspot (0,0, 800,600) action Hide('ending10', transition=dissolve)

screen ending11():
    imagemap:
        ground "GUI/Gallery/Ending11.jpg"
        hotspot (0,0, 800,600) action Hide('ending11', transition=dissolve)

screen ending12():
    imagemap:
        ground "GUI/Gallery/Ending12.jpg"
        hotspot (0,0, 800,600) action Hide('ending12', transition=dissolve)

screen ending13():
    imagemap:
        ground "GUI/Gallery/Ending13.jpg"
        hotspot (0,0, 800,600) action Hide('ending13', transition=dissolve)

screen ending14():
    imagemap:
        ground "GUI/Gallery/Ending14.jpg"
        hotspot (0,0, 800,600) action Hide('ending14', transition=dissolve)

screen ending15():
    imagemap:
        ground "GUI/Gallery/Ending15.jpg"
        hotspot (0,0, 800,600) action Hide('ending15', transition=dissolve)


screen gallery_profiles():
    tag menu

    imagemap:
        ground "GUI/Gallery/profiles_ground.png"
        idle "GUI/Gallery/profiles_idle.png"
        hover "GUI/Gallery/profiles_hover.png"
        selected_idle "GUI/Gallery/profiles_hover.png"
        selected_hover "GUI/Gallery/profiles_hover.png"

        hotspot (31,110, 153,30) action ShowMenu("gallery_scenes")
        hotspot (25,156, 165,38) action ShowMenu("gallery_endings")
        hotspot (28,204, 159,32) action ShowMenu("gallery_profiles")
        hotspot (30,250, 156,34) action Return()

        hotspot (211,132, 473,60) action Show('profile_zuleika', transition=dissolve)
        if persistent.ending1 == True or persistent.ending2 == True or persistent.ending3 == True or persistent.ending4 == True or persistent.ending7 == True or persistent.ending14 == True:
            hotspot (211,200, 473,60) action Show('profile_chael', transition=dissolve)
        if persistent.ending5 == True or persistent.ending6 == True or persistent.ending8 == True or persistent.ending15 == True:
            hotspot (211,268, 473,60) action Show('profile_kirile', transition=dissolve)
        if persistent.ending9 == True or persistent.ending11 == True or persistent.ending12 == True:
            hotspot (211,336, 473,60) action Show('profile_duren', transition=dissolve)
        if persistent.ending10 == True or persistent.ending13 == True:
            hotspot (211,404, 473,60) action Show('profile_nefferon', transition=dissolve)

screen profile_zuleika():
    imagemap:
        ground "GUI/Gallery/Profile - Zuleika.jpg"
        hotspot (0,0, 800,600) action Hide('profile_zuleika', transition=dissolve)

screen profile_chael():
    imagemap:
        ground "GUI/Gallery/Profile - Chael.jpg"
        hotspot (0,0, 800,600) action Hide('profile_chael', transition=dissolve)

screen profile_kirile():
    imagemap:
        ground "GUI/Gallery/Profile - Kirile.jpg"
        hotspot (0,0, 800,600) action Hide('profile_kirile', transition=dissolve)

screen profile_duren():
    imagemap:
        ground "GUI/Gallery/Profile - Duren.jpg"
        hotspot (0,0, 800,600) action Hide('profile_duren', transition=dissolve)

screen profile_nefferon():
    imagemap:
        ground "GUI/Gallery/Profile - Nefferon.jpg"
        hotspot (0,0, 800,600) action Hide('profile_nefferon', transition=dissolve)
