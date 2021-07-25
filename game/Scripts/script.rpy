# script.rpy is the default entry point into the game.
# Common definitions go here.
init:
    # Characters
    $ a = Character("Assassin", show_two_window=True)
    $ an = Character("Announcer", show_two_window=True)
    $ g = Character("Guard", show_two_window=True)
    $ so = Character("Soldier", show_two_window=True)
    $ m = Character("Man", show_two_window=True)
    $ w = Character("Woman", show_two_window=True)
    $ cr = Character("Crowd", show_two_window=True)
    $ s = Character("Sales Clerk", show_two_window=True)
    $ l = Character("Librarian", show_two_window=True)
    $ i = Character("Inn Keeper", show_two_window=True)
    $ t = Character("Trainer", show_two_window=True)
    $ p = Character("Preacher", show_two_window=True)
    $ dm = Character("Depressed Man", show_two_window=True)
    $ u = Character("???", show_two_window=True)
    $ db = Character("Duren", color="#0000FF", show_two_window=True)
    $ zb = Character("Zuleika", color="#347C2C", show_two_window=True)
    $ cb = Character("Chael", color="#4863A0", show_two_window=True)
    $ kb = Character("Kirile", color="#800517", show_two_window=True)
    $ nb = Character("Nefferon", color="#800080", show_two_window=True)
    $ d = Character("Duren", color="#0000FF", show_two_window=True,
        show_side_image = ConditionSwitch("DAffection < 75", "GUI/HeartBlack.png",
            "DAffection == 75", "GUI/HeartBlack.png",
            "DAffection > 75 and DAffection < 150", "GUI/HeartBlue.png",
            "DAffection == 150", "GUI/HeartBlue.png",
            "DAffection > 150 and DAffection < 225", "GUI/HeartGreen.png",
            "DAffection == 225", "GUI/HeartGreen.png",
            "DAffection > 225 and DAffection < 300", "GUI/HeartYellow.png",
            "DAffection == 300", "GUI/HeartYellow.png",
            "DAffection > 300", "GUI/HeartRed.png",
            xpos = 695, ypos = 535))
    $ n = Character("Nefferon", color="#800080", show_two_window=True,
        show_side_image = ConditionSwitch("NAffection < 75", "GUI/HeartBlack.png",
            "NAffection == 75", "GUI/HeartBlack.png",
            "NAffection > 75 and NAffection < 150", "GUI/HeartBlue.png",
            "NAffection == 150", "GUI/HeartBlue.png",
            "NAffection > 150 and NAffection < 225", "GUI/HeartGreen.png",
            "NAffection == 225", "GUI/HeartGreen.png",
            "NAffection > 225 and NAffection < 300", "GUI/HeartYellow.png",
            "NAffection == 300", "GUI/HeartYellow.png",
            "NAffection > 300", "GUI/HeartRed.png",
            xpos = 695, ypos = 535))
    $ c = Character('Chael', color="#4863A0", show_two_window=True,
        show_side_image = ConditionSwitch("CAffection < 100", "GUI/HeartBlack.png",
            "CAffection == 100", "GUI/HeartBlack.png",
            "CAffection > 100 and CAffection < 200", "GUI/HeartBlue.png",
            "CAffection == 200", "GUI/HeartBlue.png",
            "CAffection > 200 and CAffection < 300", "GUI/HeartGreen.png",
            "CAffection == 300", "GUI/HeartGreen.png",
            "CAffection > 300 and CAffection < 400", "GUI/HeartYellow.png",
            "CAffection == 400", "GUI/HeartYellow.png",
            "CAffection > 400", "GUI/HeartRed.png",
            xpos = 695, ypos = 535))
    $ k = Character("Kirile", color="#800517", show_two_window=True,
        show_side_image = ConditionSwitch("KAffection < 100", "GUI/HeartBlack.png",
            "KAffection == 100", "GUI/HeartBlack.png",
            "KAffection > 100 and KAffection < 200", "GUI/HeartBlue.png",
            "KAffection == 200", "GUI/HeartBlue.png",
            "KAffection > 200 and KAffection < 300", "GUI/HeartGreen.png",
            "KAffection == 300", "GUI/HeartGreen.png",
            "KAffection > 300 and KAffection < 400", "GUI/HeartYellow.png",
            "KAffection == 400", "GUI/HeartYellow.png",
            "KAffection > 400", "GUI/HeartRed.png",
            xpos = 695, ypos = 535))
    $ z = Character(
        None,
        window_left_padding=160,
        show_side_image=ShowingSwitch(
            "zuleika sad", "zuleikasad",
            "zuleika sadblush", "zuleikasadblush",
            "zuleika angry", "zuleikaangry",
            "zuleika normal", "zuleikanormal",
            "zuleika normalblush", "zuleikanormalblush",
            "zuleika happy", "zuleikahappy",
            "zuleika happyblush", "zuleikahappyblush",
            "wzuleika sad", "wzuleikasad",
            "wzuleika sadblush", "wzuleikasadblush",
            "wzuleika angry", "wzuleikaangry",
            "wzuleika normal", "wzuleikanormal",
            "wzuleika normalblush", "wzuleikanormalblush",
            "wzuleika happy", "wzuleikahappy",
            "wzuleika happyblush", "wzuleikahappyblush",
            "wlzuleika sad", "wlzuleikasad",
            "wlzuleika sadblush", "wlzuleikasadblush",
            "wlzuleika angry", "wlzuleikaangry",
            "wlzuleika normal", "wlzuleikanormal",
            "wlzuleika normalblush", "wlzuleikanormalblush",
            "wlzuleika happy", "wlzuleikahappy",
            "wlzuleika happyblush", "wlzuleikahappyblush",
            "bzuleika sad", "bzuleikasad",
            "bzuleika sadblush", "bzuleikasadblush",
            "bzuleika angry", "bzuleikaangry",
            "bzuleika normal", "bzuleikanormal",
            "bzuleika normalblush", "bzuleikanormalblush",
            "bzuleika happy", "bzuleikahappy",
            "bzuleika happyblush", "bzuleikahappyblush",
            None, Null(),
            xpos=0, ypos=263))

    # Backgrounds
    image bg black = "#000000"
    image bg blank = "Images/Backgrounds/BasicBackground-1.jpg"
    image bg bedroom = "Images/Backgrounds/BedroomNight.jpg"
    image bg bedroom day = "Images/Backgrounds/Bedroom.jpg"
    image bg night = "Images/Backgrounds/Night.jpg"
    image bg night2 = "Images/Backgrounds/Night2.jpg"
    image bg hallway night = "Images/Backgrounds/HallwayNight.jpg"
    image bg path = "Images/Backgrounds/Landscape by Kaikei Sozai Mise.jpg"
    image bg camp night = "Images/Backgrounds/GroundNight by Kaikei Sozai Mise.jpg"
    image bg mountains sunset = "Images/Backgrounds/Mountains Sunset by BCS.jpg"
    image bg inside cave = "Images/Backgrounds/Cave Inside by Kaikei Sozai Mise.jpg"
    image bg meadow = "Images/Backgrounds/Meadow by Kaikei Sozai Mise.jpg"
    image bg dungeon = "Images/Backgrounds/Dungeon by Kaikei Sozai Mise.jpg"
    image bg ballroom = "Images/Backgrounds/Castle Hall by katokitiMY.jpg"
    image bg hallway night = "Images/Backgrounds/HallwayNight.jpg"
    image bg castle hallway = "Images/Backgrounds/Hallway2.jpg"
    image bg castle hall = "Images/Backgrounds/Castle Hall.jpg"
    image bg throne = "Images/Backgrounds/Throne.jpg"
    image bg castle library = "Images/Backgrounds/Library by katokitiMY.jpg"
    image bg garden = "Images/Backgrounds/Garden.jpg"
    image bg castle town = "Images/Backgrounds/VillageShop.jpg"
    image bg dungeon = "Images/Backgrounds/Dungeon by Kaikei Sozai Mise.jpg"
    image bg courtyard = "Images/Backgrounds/Courtyard.jpg"
    image bg dancehall = "Images/Backgrounds/Castle Hall2.jpg"
    image bg stream = "Images/Backgrounds/Stream by Kaikei Sozai Mise.jpg"
    image bg jarconia = "Images/Backgrounds/Village by Kaikei Sozai Mise.jpg"
    image bg shop = "Images/Backgrounds/Shop.jpg"
    image bg library = "Images/Backgrounds/Library2.jpg"
    image bg inn = "Images/Backgrounds/Inn by Mei Miyamura.jpg"
    image bg inn sunset = "Images/Backgrounds/Inn Sunset by Mei Miyamura.jpg"
    image bg inn night = "Images/Backgrounds/Inn Night by Mei Miyamura.jpg"
    image bg training = "Images/Backgrounds/Training Hall.jpg"
    image bg church = "Images/Backgrounds/Church.jpg"
    image bg faraway village = "Images/Backgrounds/FarawayVillageSunset by Kaikei Sozai Mise.jpg"
    image bg faraway village day = "Images/Backgrounds/FarawayVillage by Kaikei Sozai Mise.jpg"
    image bg cave = "Images/Backgrounds/Cave by Kaikei Sozai Mise.jpg"
    image bg rundown village = "Images/Backgrounds/RundownVillage.jpg"
    image bg rundown village night = "Images/Backgrounds/RundownVillageNight.jpg"
    image bg dark corridor = "Images/Backgrounds/VillageDarkCorridor by Kaikei Sozai Mise.jpg"
    image bg lake = "Images/Backgrounds/Lake.jpg"
    image bg duggary = "Images/Backgrounds/Village by Mei Miyamura.jpg"
    
    # Miscellaneous Images
    image fire = "Images/Misc/FireFlame.jpg"
    image journal = "Images/Misc/Journal.png"
    image prologue tyrant = "Images/Misc/Tyrant.jpg"
    image prologue emperor = "Images/Misc/medieval-life-5.jpg"
    image prologue princess = "Images/Misc/joanofarc.jpg"
    image goddess = "Images/Misc/Goddess.jpg"
    image chaos god = "Images/Misc/ChaosGod.jpg"
    
    # Map
    image nation map = "Images/Map/Nation Map.jpg"
    image nation map pyralis = "Images/Map/Nation Map - Pyralis.jpg"
    image nation map tyraca = "Images/Map/Nation Map - Tyraca.jpg"
    image nation map nalan = "Images/Map/Nation Map - Nalan.jpg"
    
    # Event images
    image chael hand = "Images/Events/ChaelHoldingOutHand.jpg"
    image chael windo = "Images/Events/JumpingOutWindow.jpg"
    image duren hand mountains = "Images/Events/DurenHoldingOutHandMountains.jpg"
    image chael cave  = "Images/Events/ChaelandZuleikainCave.jpg"
    image kirile cave = "Images/Events/KirileandZuleikainCave.jpg"
    image chael final = "Images/Events/ChaelandZuleikaFinal.jpg"
    image nef violent bedroom = "Images/Events/NefferonandZuleikaViolentBedroom.jpg"
    image nef violent hallway = "Images/Events/NefferonandZuleikaViolentHallway.jpg"
    image duren hand ballroom = "Images/Events/DurenHoldingOutHandBallroom.jpg"
    image nef death = "Images/Events/NefferonandZuleikaDeath.jpg"
    
    # Battle (mini-game)
    image battlezuleika normal = "Images/Sprites/Zuleika/Zuleika - BattleN.png"
    image battlezuleika angry = "Images/Sprites/Zuleika/Zuleika - BattleA.png"
    image battlezuleika sad = "Images/Sprites/Zuleika/Zuleika - BattleS.png"
    image battlezuleika happy = "Images/Sprites/Zuleika/Zuleika - BattleH.png"
    image HPL = ConditionSwitch(
        "ZHP < 1", "GUI/Battle/HPBarL0.png",
        "ZHP == 5", "GUI/Battle/HPBarL5.png",
        "ZHP == 10", "GUI/Battle/HPBarL10.png",
        "ZHP == 15", "GUI/Battle/HPBarL15.png",
        "ZHP == 20", "GUI/Battle/HPBarL20.png",
        "ZHP == 25", "GUI/Battle/HPBarL25.png",
        "ZHP == 30", "GUI/Battle/HPBarL30.png",
        "ZHP == 35", "GUI/Battle/HPBarL35.png",
        "ZHP == 40", "GUI/Battle/HPBarL40.png",
        "ZHP == 45", "GUI/Battle/HPBarL45.png",
        "ZHP == 50", "GUI/Battle/HPBarL50.png",
        "ZHP == 55", "GUI/Battle/HPBarL55.png",
        "ZHP == 60", "GUI/Battle/HPBarL60.png",
        "ZHP == 65", "GUI/Battle/HPBarL65.png",
        "ZHP == 70", "GUI/Battle/HPBarL70.png",
        "ZHP == 75", "GUI/Battle/HPBarL75.png",
        "ZHP == 80", "GUI/Battle/HPBarL80.png",
        "ZHP == 85", "GUI/Battle/HPBarL85.png",
        "ZHP == 90", "GUI/Battle/HPBarL90.png",
        "ZHP == 95", "GUI/Battle/HPBarL95.png",
        "ZHP == 100", "GUI/Battle/HPBarL100.png",
        )
    image HPR = ConditionSwitch(
        "EHP < 1", "GUI/Battle/HPBarR0.png",
        "EHP == 5", "GUI/Battle/HPBarR5.png",
        "EHP == 10", "GUI/Battle/HPBarR10.png",
        "EHP == 15", "GUI/Battle/HPBarR15.png",
        "EHP == 20", "GUI/Battle/HPBarR20.png",
        "EHP == 25", "GUI/Battle/HPBarR25.png",
        "EHP == 30", "GUI/Battle/HPBarR30.png",
        "EHP == 35", "GUI/Battle/HPBarR35.png",
        "EHP == 40", "GUI/Battle/HPBarR40.png",
        "EHP == 45", "GUI/Battle/HPBarR45.png",
        "EHP == 50", "GUI/Battle/HPBarR50.png",
        "EHP == 55", "GUI/Battle/HPBarR55.png",
        "EHP == 60", "GUI/Battle/HPBarR60.png",
        "EHP == 65", "GUI/Battle/HPBarR65.png",
        "EHP == 70", "GUI/Battle/HPBarR70.png",
        "EHP == 75", "GUI/Battle/HPBarR75.png",
        "EHP == 80", "GUI/Battle/HPBarR80.png",
        "EHP == 85", "GUI/Battle/HPBarR85.png",
        "EHP == 90", "GUI/Battle/HPBarR90.png",
        "EHP == 95", "GUI/Battle/HPBarR95.png",
        "EHP == 100", "GUI/Battle/HPBarR100.png",
        )
    image VSDuren = "Images/Sprites/Duren/VSDuren.png"
    image VSZuleika = "Images/Sprites/Zuleika/VSZuleika.png"
    image VSKirile = "Images/Sprites/Kirile/VSKirile.png"
    image VSChael = "Images/Sprites/Chael/VSChael.png"
    image VSNefferon = "Images/Sprites/Nefferon/VSNefferon.png"
    
    # Dance (mini-game)
    image VSBZuleika = "Images/Sprites/Zuleika/VSZuleikaBallgown.png"
    image dancezuleika normal = "Images/Sprites/Zuleika/Zuleika - DanceN.png"
    image dancezuleika happy = "Images/Sprites/Zuleika/Zuleika - DanceH.png"
    image dancezuleika sad = "Images/Sprites/Zuleika/Zuleika - DanceS.png"
    image HP = ConditionSwitch(
        "HP < 2", "GUI/Dance/HPBar0.png",
        "HP == 20", "GUI/Dance/HPBar20.png",
        "HP == 40", "GUI/Dance/HPBar40.png",
        "HP == 60", "GUI/Dance/HPBar60.png",
        "HP == 80", "GUI/Dance/HPBar80.png",
        "HP == 100", "GUI/Dance/HPBar100.png",
        )
    image arrowdown = "GUI/Dance/Arrow - Down.png"
    image arrowup = "GUI/Dance/Arrow - Up.png"
    image arrowleft = "GUI/Dance/Arrow - Left.png"
    image arrowright = "GUI/Dance/Arrow - Right.png"
    
    # Custom Transitions
    $ flash = Fade(.25, 0, .25, color="#fff")
    $ sshake = Shake((0, 0, 0, 0), 1.0, dist=15)
    
    # Custom Positions
    $ top = Position(xpos=0.5, xanchor='center', ypos=0.0,
                   yanchor='top')
    $ topleft = Position(xpos=0.0, xanchor='left', ypos=0.0,
                   yanchor='top')
    $ topright = Position(xpos=1.0, xanchor='right', ypos=0.0,
                   yanchor='top')

    # Cursor
    $ config.mouse = { }
    $ config.mouse['default'] = [
        ("GUI/Cursor3.png", 0, 0)
    ]
    
    # Duren Sprites
    image duren = "Images/Sprites/Duren/Duren.png"
    image duren 2 = "Images/Sprites/Duren/Duren2.png"
    image duren happy = LiveComposite(
                (366, 564),
                (0, 0), "duren",
                (115, 104), "Images/Sprites/Duren/DurenH.png",)
    image duren happyblush = LiveComposite(
                (366, 564),
                (0, 0), "duren",
                (115, 104), "Images/Sprites/Duren/DurenHB.png",)
    image duren blush = LiveComposite(
                (366, 564),
                (0, 0), "duren",
                (115, 104), "Images/Sprites/Duren/DurenB.png",)
    image duren angry = LiveComposite(
                (366, 564),
                (0, 0), "duren",
                (115, 104), "Images/Sprites/Duren/DurenA.png",)
    image duren angry2 = LiveComposite(
                (366, 564),
                (0, 0), "duren 2",
                (175, 104), "Images/Sprites/Duren/DurenA2.png",)
    image duren sad = LiveComposite(
                (366, 564),
                (0, 0), "duren",
                (115, 104), "Images/Sprites/Duren/DurenS.png",)
    image duren sad2 = LiveComposite(
                (366, 564),
                (0, 0), "duren 2",
                (175, 104), "Images/Sprites/Duren/DurenS2.png",)
    
    # Nefferon Sprites
    image nef = "Images/Sprites/Nefferon/Nefferon.png"
    image nef 2 = "Images/Sprites/Nefferon/Nefferon2.png"
    image nef happy = LiveComposite(
                (272, 564),
                (0, 0), "nef",
                (73, 86), "Images/Sprites/Nefferon/NefferonH.png",)
    image nef angry = LiveComposite(
                (272, 564),
                (0, 0), "nef",
                (73, 86), "Images/Sprites/Nefferon/NefferonA.png",)
    image nef sad = LiveComposite(
                (272, 564),
                (0, 0), "nef",
                (73, 86), "Images/Sprites/Nefferon/NefferonS.png",)
    image nef sad2 = LiveComposite(
                (272, 564),
                (0, 0), "nef 2",
                (139, 86), "Images/Sprites/Nefferon/NefferonS2.png",)
    
    # Kirile Sprites
    image kirile = "Images/Sprites/Kirile/Kirile.png"
    image kirile 2 = "Images/Sprites/Kirile/Kirile2.png"
    image kirile happy = LiveComposite(
                (453, 563),
                (0, 0), "kirile",
                (166, 89), "Images/Sprites/Kirile/KirileH.png",)
    image kirile happyblush = LiveComposite(
                (453, 563),
                (0, 0), "kirile",
                (166, 89), "Images/Sprites/Kirile/KirileHB.png",)
    image kirile angry = LiveComposite(
                (453, 563),
                (0, 0), "kirile",
                (166, 89), "Images/Sprites/Kirile/KirileA.png",)
    image kirile angry2 = LiveComposite(
                (453, 563),
                (0, 0), "kirile 2",
                (214, 89), "Images/Sprites/Kirile/KirileA2.png",)
    image kirile sad = LiveComposite(
                (453, 563),
                (0, 0), "kirile",
                (166, 89), "Images/Sprites/Kirile/KirileS.png",)
    image kirile sad2 = LiveComposite(
                (453, 563),
                (0, 0), "kirile 2",
                (214, 89), "Images/Sprites/Kirile/KirileS2.png",)
    image kirile blush = LiveComposite(
                (453, 563),
                (0, 0), "kirile",
                (166, 89), "Images/Sprites/Kirile/KirileB.png",)
    image lkirile = "Images/Sprites/Kirile/Kirile Wingless.png"
    image lkirile 2 = "Images/Sprites/Kirile/Kirile Wingless2.png"
    image lkirile happy = LiveComposite(
                (453, 563),
                (0, 0), "lkirile",
                (166, 89), "Images/Sprites/Kirile/KirileH.png",)
    image lkirile happyblush = LiveComposite(
                (453, 563),
                (0, 0), "lkirile",
                (166, 89), "Images/Sprites/Kirile/KirileHB.png",)
    image lkirile angry = LiveComposite(
                (453, 563),
                (0, 0), "lkirile",
                (166, 89), "Images/Sprites/Kirile/KirileA.png",)
    image lkirile angry2 = LiveComposite(
                (453, 563),
                (0, 0), "lkirile 2",
                (214, 89), "Images/Sprites/Kirile/KirileA2.png",)
    image lkirile sad = LiveComposite(
                (453, 563),
                (0, 0), "lkirile",
                (166, 89), "Images/Sprites/Kirile/KirileS.png",)
    image lkirile sad2 = LiveComposite(
                (453, 563),
                (0, 0), "lkirile 2",
                (214, 89), "Images/Sprites/Kirile/KirileS2.png",)
    image lkirile blush = LiveComposite(
                (453, 563),
                (0, 0), "lkirile",
                (166, 89), "Images/Sprites/Kirile/KirileB.png",)
    
    # Chael Sprites
    image chael = "Images/Sprites/Chael/Chael.png"
    image chael 2 = "Images/Sprites/Chael/Chael2.png"
    image assassin = "Images/Sprites/Chael/ChaelAssassin.png"
    image assassin 2 = "Images/Sprites/Chael/ChaelAssassin2.png"
    image chael happy = LiveComposite(
                (417, 564),
                (0, 0), "chael",
                (127, 89), "Images/Sprites/Chael/ChaelH.png",)
    image chael happy2 = LiveComposite(
                (417, 564),
                (0, 0), "chael 2",
                (225, 89), "Images/Sprites/Chael/ChaelH2.png",)
    image chael happyblush = LiveComposite(
                (417, 564),
                (0, 0), "chael",
                (127, 89), "Images/Sprites/Chael/ChaelHB.png",)
    image chael angry = LiveComposite(
                (417, 564),
                (0, 0), "chael",
                (127, 89), "Images/Sprites/Chael/ChaelA.png",)
    image chael angry2 = LiveComposite(
                (417, 564),
                (0, 0), "chael 2",
                (225, 89), "Images/Sprites/Chael/ChaelA2.png",)
    image chael sad = LiveComposite(
                (417, 564),
                (0, 0), "chael",
                (127, 89), "Images/Sprites/Chael/ChaelS.png",)
    image chael sad2 = LiveComposite(
                (417, 564),
                (0, 0), "chael 2",
                (225, 89), "Images/Sprites/Chael/ChaelS2.png",)
    image chael blush = LiveComposite(
                (417, 564),
                (0, 0), "chael",
                (127, 89), "Images/Sprites/Chael/ChaelB.png",)
    image lchael = "Images/Sprites/Chael/Chael Wingless.png"
    image lchael 2 = "Images/Sprites/Chael/Chael Wingless2.png"
    image lchael happy = LiveComposite(
                (417, 564),
                (0, 0), "lchael",
                (127, 89), "Images/Sprites/Chael/ChaelH.png",)
    image lchael happy2 = LiveComposite(
                (417, 564),
                (0, 0), "lchael 2",
                (225, 89), "Images/Sprites/Chael/ChaelH2.png",)
    image lchael happyblush = LiveComposite(
                (417, 564),
                (0, 0), "lchael",
                (127, 89), "Images/Sprites/Chael/ChaelHB.png",)
    image lchael angry = LiveComposite(
                (417, 564),
                (0, 0), "lchael",
                (127, 89), "Images/Sprites/Chael/ChaelA.png",)
    image lchael angry2 = LiveComposite(
                (417, 564),
                (0, 0), "lchael 2",
                (225, 89), "Images/Sprites/Chael/ChaelA2.png",)
    image lchael sad = LiveComposite(
                (417, 564),
                (0, 0), "lchael",
                (127, 89), "Images/Sprites/Chael/ChaelS.png",)
    image lchael sad2 = LiveComposite(
                (417, 564),
                (0, 0), "lchael 2",
                (225, 89), "Images/Sprites/Chael/ChaelS2.png",)
    image lchael blush = LiveComposite(
                (417, 564),
                (0, 0), "lchael",
                (127, 89), "Images/Sprites/Chael/ChaelB.png",)
    
    # Villager Boy Sprites
    image vboy1 = "Images/Sprites/Villager1/VBoy1.png"
    image vboy2 = "Images/Sprites/Villager1/VBoy2.png"
    image vboya normal = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (157, 160), "Images/Sprites/Villager1/VBoyN.png")
    image vboya nervous = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (157, 160), "Images/Sprites/Villager1/VBoyNV.png")
    image vboya happy = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (157, 160), "Images/Sprites/Villager1/VBoyH.png")
    image vboya sad = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (157, 160), "Images/Sprites/Villager1/VBoyS.png")
    image vboyb normal = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyN.png")
    image vboyb nervous = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyNV.png")
    image vboyb happy = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyH.png")
    image vboyb sad = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyS.png")
    image vboyc normal = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyN.png")
    image vboyc nervous = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyNV.png")
    image vboyc happy = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyH.png")
    image vboyc sad = LiveComposite(
                (417, 564),
                (0, 0), "vboy1",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyS.png")
    image vboyd normal = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (157, 160), "Images/Sprites/Villager1/VBoyN.png")
    image vboyd nervous = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (157, 160), "Images/Sprites/Villager1/VBoyNV.png")
    image vboyd happy = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (157, 160), "Images/Sprites/Villager1/VBoyH.png")
    image vboyd sad = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (157, 160), "Images/Sprites/Villager1/VBoyS.png")
    image vboye normal = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyN.png")
    image vboye nervous = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyNV.png")
    image vboye happy = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyH.png")
    image vboye sad = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (129, 45), "Images/Sprites/Villager1/VBoy - RedHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - RedVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyS.png")
    image vboyf normal = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyN.png")
    image vboyf nervous = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyNV.png")
    image vboyf happy = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyH.png")
    image vboyf sad = LiveComposite(
                (417, 564),
                (0, 0), "vboy2",
                (130, 45), "Images/Sprites/Villager1/VBoy - BrownHair.png",
                (116, 218), "Images/Sprites/Villager1/VBoy - BrownVest.png",
                (157, 160), "Images/Sprites/Villager1/VBoyS.png")
    
    # Villager Girl Sprites
    image vgirl1 = "Images/Sprites/Villager2/VGirl1.png"
    image vgirl2 = "Images/Sprites/Villager2/VGirl2.png"
    image vgirla normal = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (156, 151), "Images/Sprites/Villager2/VGirlN.png")
    image vgirla nervous = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (156, 151), "Images/Sprites/Villager2/VGirlNV.png")
    image vgirla happy = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (156, 151), "Images/Sprites/Villager2/VGirlH.png")
    image vgirla sad = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (156, 152), "Images/Sprites/Villager2/VGirlS.png")
    image vgirlb normal = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlN.png")
    image vgirlb nervous = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlNV.png")
    image vgirlb happy = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlH.png")
    image vgirlb sad = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 152), "Images/Sprites/Villager2/VGirlS.png")
    image vgirlc normal = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlN.png")
    image vgirlc nervous = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlNV.png")
    image vgirlc happy = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlH.png")
    image vgirlc sad = LiveComposite(
                (417, 564),
                (0, 0), "vgirl1",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 152), "Images/Sprites/Villager2/VGirlS.png")
    image vgirld normal = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (156, 151), "Images/Sprites/Villager2/VGirlN.png")
    image vgirld nervous = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (156, 151), "Images/Sprites/Villager2/VGirlNV.png")
    image vgirld happy = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (156, 151), "Images/Sprites/Villager2/VGirlH.png")
    image vgirld sad = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (156, 152), "Images/Sprites/Villager2/VGirlS.png")
    image vgirle normal = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlN.png")
    image vgirle nervous = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlNV.png")
    image vgirle happy = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlH.png")
    image vgirle sad = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (140, 70), "Images/Sprites/Villager2/VGirl - DarkHair.png",
                (143, 339), "Images/Sprites/Villager2/VGirl - RedBodice.png",
                (156, 152), "Images/Sprites/Villager2/VGirlS.png")
    image vgirlf normal = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlN.png")
    image vgirlf nervous = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlNV.png")
    image vgirlf happy = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 151), "Images/Sprites/Villager2/VGirlH.png")
    image vgirlf sad = LiveComposite(
                (417, 564),
                (0, 0), "vgirl2",
                (142, 69), "Images/Sprites/Villager2/VGirl - LightHair.png",
                (144, 340), "Images/Sprites/Villager2/VGirl - BrownBodice.png",
                (156, 152), "Images/Sprites/Villager2/VGirlS.png")
    
    # Zuleika Sprites - Hidden
    image zuleika normal hidden = Null ()
    image zuleika normalblush hidden = Null ()
    image zuleika happy hidden = Null ()
    image zuleika happyblush hidden = Null ()
    image zuleika sad hidden = Null ()
    image zuleika sadblush hidden = Null ()
    image zuleika angry hidden = Null ()
    image wzuleika normal hidden = Null ()
    image wzuleika normalblush hidden = Null ()
    image wzuleika happy hidden = Null ()
    image wzuleika happyblush hidden = Null ()
    image wzuleika sad hidden = Null ()
    image wzuleika sadblush hidden = Null ()
    image wzuleika angry hidden = Null ()
    image wlzuleika normal hidden = Null ()
    image wlzuleika normalblush hidden = Null ()
    image wlzuleika happy hidden = Null ()
    image wlzuleika happyblush hidden = Null ()
    image wlzuleika sad hidden = Null ()
    image wlzuleika sadblush hidden = Null ()
    image wlzuleika angry hidden = Null ()
    image bzuleika normal hidden = Null ()
    image bzuleika normalblush hidden = Null ()
    image bzuleika happy hidden = Null ()
    image bzuleika happyblush hidden = Null ()
    image bzuleika sad hidden = Null ()
    image bzuleika sadblush hidden = Null ()
    image bzuleika angry hidden = Null ()
    
    # Zuleika Sprites - Outfits
    image zuleikaoutfit = ConditionSwitch(
        "outfit == 'default'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png"),
        "outfit == 'red'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - PrincessR.png"),
        "outfit == 'blue'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - PrincessB.png"),
        "outfit == 'green'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - PrincessG.png"),
        "outfit == 'violet'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - PrincessV.png"),
        "outfit == 'mourning'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - PrincessM.png"),
        )
    image wzuleikaoutfit = ConditionSwitch(
        "outfit == 'default'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Warrior.png"),
        "outfit == 'red'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Warrior.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorR.png"),
        "outfit == 'blue'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Warrior.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorB.png"),
        "outfit == 'green'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Warrior.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorG.png"),
        "outfit == 'violet'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Warrior.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorV.png"),
        "outfit == 'mourning'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika - Princess.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - PrincessM.png"),
        )
    image wlzuleikaoutfit = ConditionSwitch(
        "outfit == 'default'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika Wingless.png"),
        "outfit == 'red'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika Wingless.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorR.png"),
        "outfit == 'blue'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika Wingless.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorB.png"),
        "outfit == 'green'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika Wingless.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorG.png"),
        "outfit == 'violet'", LiveComposite(
            (255, 441),
            (0, 0), "Images/Sprites/Zuleika/Zuleika Wingless.png",
            (0, 0), "Images/Sprites/Zuleika/Zuleika - WarriorV.png"),
        )
    image bzuleikaoutfit = "Images/Sprites/Zuleika/Zuleika - Ballgown.png"
    
    # Zuleika Sprites - Accessories
    image zuleikacrown = "Images/Sprites/Zuleika/Zuleika - Crown.png"
    image zuleikanecklacep = "Images/Sprites/Zuleika/Zuleika - NecklaceP.png"
    image zuleikanecklaceb = "Images/Sprites/Zuleika/Zuleika - NecklaceB.png"
    image zuleikasatchel = "Images/Sprites/Zuleika/Zuleika - Satchel.png"
    image zuleikaclaw = "Images/Sprites/Zuleika/Zuleika - Claw.png"
    image zuleikaclaw1 = "Images/Sprites/Zuleika/Zuleika - Claw-1.png"
    image zuleikatiara = "Images/Sprites/Zuleika/Zuleika - Tiara.png"
    
    # Zuleika Sprites - Faces
    image zuleikafaceangry = "Images/Sprites/Zuleika/ZuleikaA.png"
    image zuleikafacehappy = "Images/Sprites/Zuleika/ZuleikaH.png"
    image zuleikafacehappyblush = "Images/Sprites/Zuleika/ZuleikaHB.png"
    image zuleikafacenormal = "Images/Sprites/Zuleika/ZuleikaN.png"
    image zuleikafacenormalblush = "Images/Sprites/Zuleika/ZuleikaNB.png"
    image zuleikafacesad = "Images/Sprites/Zuleika/ZuleikaS.png"
    image zuleikafacesadblush = "Images/Sprites/Zuleika/ZuleikaSB.png"
    
    # Zuleika Sprites - Composite
    image zuleikaangry = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry")
        )
    image zuleikahappy = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy")
        )
    image zuleikahappyblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush")
        )
    image zuleikanormal = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal")
        )
    image zuleikanormalblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush")
        )
    image zuleikasad = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacesad"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesad"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad")
        )
    image zuleikasadblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'None' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'None' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklacep",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (105, 3), "zuleikacrown",
            (115, 112), "zuleikaclaw1",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (112, 95), "zuleikanecklacep",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "zuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush")
        )
    image wzuleikaangry = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        )
    image wzuleikahappy = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy")
        )
    image wzuleikahappyblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush")
        )
    image wzuleikanormal = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal")
        )
    image wzuleikanormalblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush")
        )
    image wzuleikasad = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafacesad"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        )
    image wzuleikasadblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        )
    image wlzuleikaangry = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry")
        )
    image wlzuleikahappy = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy")
        )
    image wlzuleikahappyblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush")
        )
    image wlzuleikanormal = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal")
        )
    image wlzuleikanormalblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush")
        )
    image wlzuleikasad = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafacesad"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad")
        )
    image wlzuleikasadblush = ConditionSwitch(
        "accessory == 'None' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'None' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'None' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (115, 112), "zuleikaclaw1",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Ruby Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (112, 95), "zuleikanecklaceb",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Satchel' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (105, 269), "zuleikasatchel",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Claw Necklace' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "accessory == 'Tiara' and gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "wlzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush")
        )
    image bzuleikaangry = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafaceangry"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafaceangry"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafaceangry"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafaceangry"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafaceangry"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafaceangry")
        )
    image bzuleikahappy = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacehappy"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafacehappy"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacehappy"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacehappy"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappy"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappy")
        )
    image bzuleikahappyblush = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacehappyblush"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafacehappyblush"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacehappyblush"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacehappyblush"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacehappyblush"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacehappyblush")
        )
    image bzuleikanormal = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacenormal"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafacenormal"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacenormal"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacenormal"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormal"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormal")
        )
    image bzuleikanormalblush = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacenormalblush"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafacenormalblush"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacenormalblush"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacenormalblush"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacenormalblush"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacenormalblush")
        )
    image bzuleikasad = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacesad"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafacesad"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacesad"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacesad"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesad"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesad")
        )
    image bzuleikasadblush = ConditionSwitch(
        "princess == True and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacesadblush"),
        "princess == False and gift == 'None'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (121, 38), "zuleikafacesadblush"),
        "gift == 'Satchel'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (121, 38), "zuleikafacesadblush"),
        "gift == 'Ruby Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (105, 3), "zuleikacrown",
            (112, 95), "zuleikanecklaceb",
            (121, 38), "zuleikafacesadblush"),
        "gift == 'Claw Necklace'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (115, 112), "zuleikaclaw",
            (121, 38), "zuleikafacesadblush"),
        "gift == 'Tiara'", LiveComposite(
            (255, 441),
            (0, 0), "bzuleikaoutfit",
            (117, 3), "zuleikatiara",
            (121, 38), "zuleikafacesadblush")
        )
# end init

# Default Variables
default intelligence = 0
default strength = 0
default charm = 0
default kindness = 0
default gold = 0
default energy = 3
default CAffection = 0
default KAffection = 0
default DAffection = 0
default NAffection = 0
default gift = "None"
default accessory = "None"
default outfit = 'default'
default princess = True
default location = 'none'
default ball = None
default chael_in_party = False
default kirile_in_party = False
default duren_in_party = False
default nef_in_party = False

init python:
    
    def increase_intelligence(value):
        global intelligence
        global CAffection
        global NAffection
        intelligence += value
        CAffection += max(round(value * 0.25), 1)
        NAffection += max(round(value * 0.1), 1)
        
    def increase_strength(value):
        global strength
        global KAffection
        global DAffection
        strength += value
        KAffection += max(round(value * 0.25), 1)
        DAffection += max(round(value * 0.1), 1)
        
    def increase_charm(value):
        global charm
        global NAffection
        global KAffection
        charm += value
        NAffection += max(round(value * 0.25), 1)
        KAffection += max(round(value * 0.1), 1)
        
    def increase_kindness(value):
        global kindness
        global DAffection
        global CAffection
        kindness += value
        DAffection += max(round(value * 0.25), 1)
        CAffection += max(round(value * 0.1), 1)
        
# end init python
