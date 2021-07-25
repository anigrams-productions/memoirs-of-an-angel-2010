## This file contains some of the options that can be changed to customize
## your Ren'Py game. It only contains the most common options... there
## is quite a bit more customization you can do.
##
## Lines beginning with two '#' marks are comments, and you shouldn't
## uncomment them. Lines beginning with a single '#' mark are
## commented-out code, and you may want to uncomment them when
## appropriate.

init -1 python hide:

    ## Should we enable the use of developer tools? This should be
    ## set to False before the game is released, so the user can't
    ## cheat using developer tools.

    config.developer = False

    ## These control the width and height of the screen.

    config.screen_width = 800
    config.screen_height = 600

    ## This controls the title of the window, when Ren'Py is
    ## running in a window.

    config.window_title = u"Memoirs of an Angel: A Fantasy Visual Novel"
    config.window_icon = "GUI/ZuleikaPrincess Sprite.gif"

    #########################################
    # Layouts
    
    ## This enables the use of an in-game menu that is made out of
    ## buttons.

    layout.button_menu()

    #########################################
    # Themes
    
    ## We then want to call a theme function. themes.roundrect is
    ## a theme that features the use of rounded rectangles. It's
    ## the only theme we currently support.
    ##
    ## The theme function takes a number of parameters that can
    ## customize the color scheme.

    theme.bordered(
        # Color scheme: Mocha Latte
                                    
        ## The color of an idle widget face.
        widget = "#3f2f15",

        ## The color of a focused widget face.
        widget_hover = "#ab8757",

        ## The color of the text in a widget.
        widget_text = "#d1c6b5",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffff",

        ## The color of a disabled widget face. 
        disabled = "#3f3627",

        ## The color of disabled widget text.
        disabled_text = "#402a1c",

        ## The color of informational labels.
        label = "#F1EBE5",

        ## The color of a frame containing widgets.
        frame = "#694e23",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "GUI/Menus/title.png",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "GUI/Menus/Background.jpg",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.            
        )


    #########################################
    ## These settings let you customize the window containing the
    ## dialogue and narration, by replacing it with an image.

    ## The background of the window. In a Frame, the two numbers
    ## are the size of the left/right and top/bottom borders,
    ## respectively.

    style.window.background = Frame("GUI/Text Background.png", 625, 157)

    ## Margin is space surrounding the window, where the background
    ## is not drawn.

    style.window.left_margin = 45
    style.window.right_margin = 45
    style.window.top_margin = 7
    style.window.bottom_margin = 5

    ## Padding is space inside the window, where the background is
    ## drawn.

    style.window.left_padding = 25
    style.window.right_padding = 25
    style.window.top_padding = 17
    # style.window.bottom_padding = 6
    
    style.say_who_window.background = Frame("GUI/Text Background-1.png", 112, 45)
    style.say_who_window.left_padding = 15
    style.say_who_window.top_padding = 10
    style.say_who_window.right_padding = 15
    style.say_who_window.bottom_padding = 10

    ## This is the minimum height of the window, including the margins
    ## and padding.

    # style.window.yminimum = 250
    
    style.menu_choice_button.left_margin=50
    style.menu_choice_button.right_margin=50
    style.menu_choice_button.yminimum = 30


    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    style.mm_menu_frame.xpos = 0.95
    style.mm_menu_frame.xanchor = 0.95
    style.mm_menu_frame.ypos = 0.10
    style.mm_menu_frame.yanchor = 0.10


    #########################################
    ## These let you customize the default font used for text in Ren'Py.

    ## The file containing the default font.

    style.default.font = "GUI/dum1.ttf"

    ## The default size of text.

    style.default.size = 25
    
    style.default.color = "#302217"

    ## Note that these only change the size of some of the text. Other
    ## buttons have their own styles.


    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.

    config.has_sound = True

    ## Set this to False if the game does not have any music.

    config.has_music = True

    ## Set this to False if the game does not have voicing.

    config.has_voice = False

    ## Sounds that are used when button and imagemaps are clicked.

    #style.button.activate_sound = "click.wav"
    #style.imagemap.activate_sound = "click.wav"

    ## Sounds that are used when entering and exiting the game menu.

    #config.enter_sound = "click.wav"
    #config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.

    config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.

    config.main_menu_music = "Audio/Music/Living Voyage.ogg"


    #########################################
    ## Help.

    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to
    ##   show help to the user.
    ## - A file name relative to the base directory, which is opened in a
    ##   web browser.
    ## - None, to disable help.   
    config.help = "README.html"


    #########################################
    ## Transitions.

    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = None

    ## Used when the window is hidden.
    config.window_hide_transition = None


    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
    config.save_directory = "GardenGame-1277000302"

init -1 python hide:
    #########################################
    ## Default values of Preferences.

    ## Note: These options are only evaluated the first time a
    ## game is run. To have them run a second time, delete
    ## game/saves/persistent

    ## Should we start in fullscreen mode?

    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.

    config.default_text_cps = 40

    #########################################
    ## More customizations can go here.

init python:

    # Give us some space on the right side of the screen.
    style.window.right_padding = 100
    
    show_button_game_menu = False
    show_button_main_menu = False

    def button_game_menu():

        if show_button_game_menu:

            # to save typing
            ccinc = renpy.curried_call_in_new_context

            ui.vbox(xpos=695, ypos=550)
            ui.textbutton("Save", clicked=ccinc("_game_menu_save"), xminimum=80)
            ui.close()
            
        if show_button_main_menu:

            # to save typing
            ccinc = renpy.curried_call_in_new_context

            ui.vbox(xpos=688, ypos=562)
            ui.textbutton("Return", clicked=ccinc("_main_menu"), xminimum=80)
            ui.close()

    config.overlay_functions.append(button_game_menu)

    
    config.main_menu = [
        (u"New Game", "start", "True"),
        (u"Continue", _intra_jumps("load_screen", "main_game_transition"), "True"),
        (u"Options", _intra_jumps("preferences_screen", "main_game_transition"), "True"),
        (u"Quit", ui.jumps("_quit"), "True")
        ]
        
        
init:

    python:

        import math

        class Shaker(object):

            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }

            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child

            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor

                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)

        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)

            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
        
screen main_menu():
    tag menu

    imagemap:
        ground 'GUI/Menus/title.png'
        hover 'GUI/Menus/title_hover.png'
        
        hotspot (553, 33, 246, 46) action Start()
        hotspot (553, 88, 246, 46) action ShowMenu('load')
        hotspot (553, 143, 246, 46) action ShowMenu('gallery_scenes')
        hotspot (553, 197, 246, 46) action ShowMenu('preferences')

init -2 python:
    layout.imagemap_navigation(
        "GUI/Menus/nav_ground.png",
        "GUI/Menus/nav_idle.png",
        "GUI/Menus/nav_hover.png",
        "GUI/Menus/nav_selected_idle.png",
        "GUI/Menus/nav_hover.png",
        [

            (0,549, 160,600, "Save Game"),
            (160,549, 320,600, "Load Game"),
            (320,549, 480,600, "Preferences"),
            (480,549, 640,600, "Main Menu"),
            (640,549, 800,600, "Return"),
            ])
        
screen navigation():
    # The background of the game menu.
    window:
        style "gm_root"

    # The various buttons.
    imagemap:
        ground "GUI/Menus/nav_ground.png"
        idle "GUI/Menus/nav_idle.png"
        hover "GUI/Menus/nav_hover.png"
        selected_idle "GUI/Menus/nav_selected_idle.png"
        selected_hover "GUI/Menus/nav_hover.png"
       
        hotspot (0,549, 161,51) action ShowMenu("save")
        hotspot (160,549, 161,51) action ShowMenu("load")
        hotspot (320,549, 161,51) action ShowMenu("preferences")
        hotspot (480,549, 161,51) action ShowMenu("main_menu")
        hotspot (640,549, 161,51) action Return()
    
init -2 python:
    layout.imagemap_load_save(
        "GUI/Menus/load_ground.png",
        "GUI/Menus/load_ground.png",
        "GUI/Menus/load_selected.png",
        "GUI/Menus/load_selected.png",
        "GUI/Menus/load_selected_hover.png",
        [
            (102,132, 141,169, "previous"),
            (192,132, 269,169, "page_auto"),
            (330,132, 368,169, "page_1"),
            (437,132, 475,169, "page_2"),
            (548,132, 586,169, "page_3"),
            (653,132, 692,169, "next"),
                               
            (70,196, 285,440, "slot_0"),
            (293,196, 508,440, "slot_1"),
            (515,196, 730,440, "slot_2"),
            ])
    
    style.file_picker_ss_window.xpos = 5
    style.file_picker_ss_window.ypos = 5
    style.file_picker_text_window.xalign = 0.5
    style.file_picker_text_window.yalign = 0.779    
    config.thumbnail_width = 204
    config.thumbnail_height = 155
    config.file_entry_format = "%(time)s\n%(save_name)s"
    
init:
    $ layout.MAIN_MENU = u"Return to the main menu?\nThis will lose any unsaved progress."
    
screen preferences():

    tag menu
    use navigation

    imagemap:
        ground "GUI/Menus/pref_ground.png"
        idle "GUI/Menus/pref_idle.png"
        hover "GUI/Menus/pref_hover.png"
        selected_idle "GUI/Menus/pref_selected_idle.png"
        selected_hover "GUI/Menus/pref_selected_hover.png"

        hotspot (98, 173, 97, 32) clicked Preference("display", "window")
        hotspot (207, 173, 116, 32) clicked Preference("display", "fullscreen")
        hotspot (29, 286, 165, 32) clicked Preference("skip", "seen")
        hotspot (207, 286, 148, 32) clicked Preference("skip", "all")
        hotspot (42, 385, 152, 32) clicked Preference("after choices", "stop")
        hotspot (207, 385, 159, 32) clicked Preference("after choices", "skip")
        hotspot (123, 431, 159, 32) clicked Skip()

        hotbar (526, 180, 225, 20) value Preference("music volume")
        hotbar (526, 229, 225, 20) value Preference("sound volume")
        hotbar (464, 346, 262, 20) value Preference("text speed")
    
screen yesno_prompt():

    modal True
    
    imagemap:
        ground "GUI/Menus/yesno_ground.png"
        idle "GUI/Menus/yesno_idle.png"
        hover "GUI/Menus/yesno_hover.png"
       
        hotspot (269,324,118,54) action yes_action
        hotspot (420,324,118,54) action no_action

            
        text _(message):
            text_align 0.5
            xalign 0.5
            yalign 0.45
    


## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "MemoirsofanAngel-1.2"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "Memoirs of an Angel"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    