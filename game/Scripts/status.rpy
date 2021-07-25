# Status screen is shown between chapters.
init:
    image statusbg = "GUI/Status/StatusBackground.jpg"
    image statuschael = "GUI/Status/StatusChael.jpg"
    image statuskirile = "GUI/Status/StatusKirile.jpg"
    image statusduren = "GUI/Status/StatusDuren.jpg"
    image statusnefferon = "GUI/Status/StatusNefferon.jpg"
    image statusprincess = "GUI/Status/StatusPrincessGarb.jpg"
    image statuswarrior = "GUI/Status/StatusWarriorGarb.jpg"
    image statusnoaccessory = "GUI/Status/StatusNoAccessory.jpg"
    image statusnecklace = "GUI/Status/StatusRubyNecklace.jpg"
    image statussatchel = "GUI/Status/StatusEmbroideredSatchel.jpg"
    image statusclaw = "GUI/Status/StatusClawNecklace.jpg"
    image statustiara = "GUI/Status/StatusElvenTiara.jpg"
    image statusweapon = "GUI/Status/StatusWeapon.jpg"
    image statustitle = ConditionSwitch(
        "zuleika_type == 'all'", "GUI/Status/StatusTitleAll.jpg",
        "zuleika_type == 'charming'", "GUI/Status/StatusTitleChm.jpg",
        "zuleika_type == 'intelligent'", "GUI/Status/StatusTitleInt.jpg",
        "zuleika_type == 'kind'", "GUI/Status/StatusTitleKnd.jpg",
        "zuleika_type == 'strong'", "GUI/Status/StatusTitleStr.jpg"
        )

label status:
    stop music
    
    play music "Audio/Music/Happy Alley.ogg"
    scene statusbg
    show statustitle at Position(xpos=143, xanchor=0, ypos=143, yanchor=0)

    if princess == True:
        show statusprincess at Position(xpos=89, xanchor=0, ypos=188, yanchor=0)
    else:
        show statuswarrior at Position(xpos=89, xanchor=0, ypos=188, yanchor=0)

    if gift == "Tiara":
        show statustiara at Position(xpos=89, xanchor=0, ypos=212, yanchor=0)
    elif gift == "Claw Necklace":
        show statusclaw at Position(xpos=89, xanchor=0, ypos=212, yanchor=0)
    elif gift == "Ruby Necklace":
        show statusnecklace at Position(xpos=89, xanchor=0, ypos=212, yanchor=0)
    elif gift == "Satchel":
        show statussatchel at Position(xpos=89, xanchor=0, ypos=212, yanchor=0)
    else:
        show statusnoaccessory at Position(xpos=89, xanchor=0, ypos=212, yanchor=0)
    
    show statusweapon at Position(xpos=89, xanchor=0, ypos=236, yanchor=0)

    if princess == True:
        if duren_in_party == True:
            show statusduren at Position(xpos=38, xanchor=0, ypos=273, yanchor=0)

            if nef_in_party == True:
                show statusnefferon at Position(xpos=38, xanchor=0, ypos=404, yanchor=0)
                with fade
                $ show_button_game_menu = True
            else:
                with fade
                $ show_button_game_menu = True
                with Pause(.5)
                show statusnefferon at Position(xpos=38, xanchor=0, ypos=404, yanchor=0)
                with dissolve
  
        else:
            with fade
            $ show_button_game_menu = True
            with Pause(.5)
            show statusduren at Position(xpos=38, xanchor=0, ypos=273, yanchor=0)
            with dissolve

    else:
        if chael_in_party == True:
            show statuschael at Position(xpos=38, xanchor=0, ypos=273, yanchor=0)

            if kirile_in_party == True:
                show statuskirile at Position(xpos=38, xanchor=0, ypos=404, yanchor=0)
                with fade
                $ show_button_game_menu = True
            else:
                with fade
                $ show_button_game_menu = True
                with Pause(.5)
                show statuskirile at Position(xpos=38, xanchor=0, ypos=404, yanchor=0)
                with dissolve
        else:
            with fade
            $ show_button_game_menu = True
            with Pause(.5)
            show statuschael at Position(xpos=38, xanchor=0, ypos=273, yanchor=0)
            with dissolve
    
    centered "\n{image=GUI/Status/StatusSpacer.png}%(gold)d Gold\n\n\n\n{image=GUI/Status/StatusSpacer.png}%(intelligence)d\n\n\n{image=GUI/Status/StatusSpacer.png}%(strength)d\n\n\n{image=GUI/Status/StatusSpacer.png}%(charm)d\n\n\n{image=GUI/Status/StatusSpacer.png}%(kindness)d"

    return