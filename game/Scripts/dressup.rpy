# Dress Up Menu
label change_clothes:
    hide vgirla
    show screen change_clothes
    
    $ renpy.pause(10000)
    
    jump change_clothes
    
screen change_clothes():
    if outfit == 'default':
        if princess == True:
            hbox xpos 53 ypos 88:
                image "GUI/DressUp/default_hover.png"
        else:
            hbox xpos 53 ypos 88:
                image "GUI/DressUp/default2_hover.png"
    else:
        if princess == True:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/default_%s.png" action Jump('outfit_default') pos (53, 88)
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/default2_%s.png" action Jump('outfit_default') pos (53, 88)
            
    if outfit == 'blue':
        if princess == True:
            hbox xpos 192 ypos 88:
                image "GUI/DressUp/blue_hover.png"
        else:
            hbox xpos 192 ypos 88:
                image "GUI/DressUp/blue2_hover.png"
    else:
        if princess == True:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/blue_%s.png" action Jump('outfit_blue') pos (192, 88)
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/blue2_%s.png" action Jump('outfit_blue') pos (192, 88)
            
    if outfit == 'green':
        if princess == True:
            hbox xpos 334 ypos 88:
                image "GUI/DressUp/green_hover.png"
        else:
            hbox xpos 334 ypos 88:
                image "GUI/DressUp/green2_hover.png"
    else:
        if princess == True:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/green_%s.png" action Jump('outfit_green') pos (334, 88)
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/green2_%s.png" action Jump('outfit_green') pos (334, 88)
            
    if outfit == 'red':
        if princess == True:
            hbox xpos 478 ypos 88:
                image "GUI/DressUp/red_hover.png"
        else:
            hbox xpos 478 ypos 88:
                image "GUI/DressUp/red2_hover.png"
    else:
        if princess == True:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/red_%s.png" action Jump('outfit_red') pos (478, 88)
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/red2_%s.png" action Jump('outfit_red') pos (478, 88)
            
    if outfit == 'violet':
        if princess == True:
            hbox xpos 622 ypos 88:
                image "GUI/DressUp/violet_hover.png"
        else:
            hbox xpos 622 ypos 88:
                image "GUI/DressUp/violet2_hover.png"
    else:
        if princess == True:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/violet_%s.png" action Jump('outfit_violet') pos (622, 88)
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/violet2_%s.png" action Jump('outfit_violet') pos (622, 88)
            
    if accessory == 'None':
        hbox xpos 189 ypos 386:
            image "GUI/DressUp/noaccessory_hover.png"
    else:
        hbox xalign 0 yalign 0:
            imagebutton auto "GUI/DressUp/noaccessory_%s.png" action Jump('accessory_none') pos (189, 386)
            
    if persistent.gifttiara == True:
        if accessory == 'Tiara':
            hbox xpos 277 ypos 386:
                image "GUI/DressUp/tiara_hover.png"
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/tiara_%s.png" action Jump('accessory_tiara') pos (277, 386)
    else:
        hbox xpos 277 ypos 386:
            image "GUI/DressUp/unknown_idle.png"
            
    if persistent.giftclaw == True:
        if accessory == 'Claw Necklace':
            hbox xpos 364 ypos 386:
                image "GUI/DressUp/claw_hover.png"
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/claw_%s.png" action Jump('accessory_claw') pos (364, 386)
    else:
        hbox xpos 364 ypos 386:
            image "GUI/DressUp/unknown_idle.png"
            
    if persistent.giftsatchel == True:
        if accessory == 'Satchel':
            hbox xpos 450 ypos 386:
                image "GUI/DressUp/satchel_hover.png"
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/satchel_%s.png" action Jump('accessory_satchel') pos (450, 386)
    else:
        hbox xpos 450 ypos 386:
            image "GUI/DressUp/unknown_idle.png"
            
    if persistent.giftnecklace == True:
        if accessory == 'Ruby Necklace':
            hbox xpos 533 ypos 386:
                image "GUI/DressUp/necklace_hover.png"
        else:
            hbox xalign 0 yalign 0:
                imagebutton auto "GUI/DressUp/necklace_%s.png" action Jump('accessory_necklace') pos (533, 386)
    else:
        hbox xpos 533 ypos 386:
            image "GUI/DressUp/unknown_idle.png"
            
    hbox xalign 0 yalign 0:
        textbutton "Save and Continue" action Jump('change_save') pos (315,536)
            
label outfit_default:
    $ outfit = 'default'
    jump change_clothes
    
label outfit_blue:
    $ outfit = 'blue'
    jump change_clothes
    
label outfit_green:
    $ outfit = 'green'
    jump change_clothes
    
label outfit_red:
    $ outfit = 'red'
    jump change_clothes
    
label outfit_violet:
    $ outfit = 'violet'
    jump change_clothes
    
label accessory_none:
    $ accessory = 'None'
    jump change_clothes
    
label accessory_tiara:
    $ accessory = 'Tiara'
    jump change_clothes
    
label accessory_claw:
    $ accessory = 'Claw Necklace'
    jump change_clothes
    
label accessory_satchel:
    $ accessory = 'Satchel'
    jump change_clothes
    
label accessory_necklace:
    $ accessory = 'Ruby Necklace'
    jump change_clothes
    
label change_save:
    hide screen change_clothes
    
    if princess == True:
        show zuleika normal hidden
        z "This is my new look."
        z "Do I look good?"
        menu:
            "Yes, I'm done changing.":
                jump return_shop
            "No, let's try again.":
                jump change_clothes

    else:
        show wlzuleika normal hidden
        z "This is my new look."
        z "Do I look good?"
        menu:
            "Yes, I'm done changing.":
                jump return_shop
            "No, let's try again.":
                jump change_clothes
                
label return_shop:
    show vgirla normal with dissolve
    s "You now have %(gold)d Gold."
    
    if location == 'allshop1':
        jump allbuy_menu1
    elif location == 'allshop2':
        jump allbuy_menu2
    elif location == 'allshop3':
        jump allbuy_menu3
    elif location == 'allshop4':
        jump allbuy_menu4
    elif location == 'allshop5':
        jump allbuy_menu5