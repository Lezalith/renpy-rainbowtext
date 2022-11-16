###################################################################################################
### Defining RainbowTexts inside screen so that they reset everytime the screen is shown. #########
###################################################################################################

screen rainbows(): 

    tag rainbowSCR

    default rainbow_slow = RainbowText("Rainbow text with the slower interval of 0.1.", interval = 0.1)
    default rainbow_basic = RainbowText("Rainbow text with the default interval of 0.5.")
    default rainbow_fast = RainbowText("Rainbow text with the faster interval of 1.0.", interval = 1.0)
    default rainbow_fastest = RainbowText("Rainbow text with the even faster interval of 3.0.", interval = 3.0)

    default rainbow_start = RainbowText("Rainbow text starting at 175.0 (cyan),\nwith slower interval (0.1) to make it more noticable.", interval = 0.1, start = 175.0)

    default rainbow_desat = RainbowText("Rainbow text with lower saturation (30.0 instead of default 100.0).", s = 30.0)
    default rainbow_light = RainbowText("Rainbow text with higher lightness (80.0 instead of default 50.0).", l = 80.0)
    default rainbow_both = RainbowText("Rainbow text with both above (saturation 30.0, lightness 80.0).", s = 30.0, l = 80.0)

    vbox:
        align (0.5, 0.5)
        spacing 5

        text "This screen resets all RainbowTexts when entered." xalign 0.5 underline True color "fff"

        null height 40

        vbox:

            add rainbow_slow # 1) Slower interval.
            add rainbow_basic # 2) Default interval.

            hbox: # Faster interval, pausable. 
                spacing 20
                add rainbow_fast
                textbutton "Pause/Unpause":
                    yalign 0.5
                    action If(rainbow_fast.paused, false = Function(rainbow_fast.pause), true = Function(rainbow_fast.unpause))

            hbox: # Fastest interval, pausable.
                spacing 20
                add rainbow_fastest
                textbutton "Pause/Unpause":
                    yalign 0.5
                    action If(rainbow_fastest.paused, false = Function(rainbow_fastest.pause), true = Function(rainbow_fastest.unpause))

        null height 40

        hbox: # Slower interval, start argument given, resetable.
            spacing 20
            add rainbow_start
            textbutton "Reset to\nstarting hue":
                yalign 0.5
                action Function(rainbow_start.reset)

        null height 40

        add rainbow_desat # Lower saturation (s = 20.0)
        add rainbow_light # Higher lightness (l = 80.0)
        add rainbow_both # Both above combined.

        null height 55

        textbutton "Back to Main Menu" xalign 0.5 action Return() text_idle_color "fff"