###################################################################################################
### These will not get reset when once hidden and shown again. ####################################
###################################################################################################
image rainbow_basic = RainbowText("Rainbow text with the default interval of 0.5.")

image rainbow_slow = RainbowText("Rainbow text with the slower interval of 0.1.", interval = 0.1)
image rainbow_fast = RainbowText("Rainbow text with the faster interval of 1.0.", interval = 1.0)
image rainbow_fastest = RainbowText("Rainbow text with the even faster interval of 3.0.", interval = 3.0)

image rainbow_start = RainbowText("Rainbow text starting at 175.0 (cyan),\nwith very slow interval (0.05) to make it more noticable.", interval = 0.05, start = 175.0)

image rainbow_desat = RainbowText("Rainbow text with lower saturation", s = 20.0)
image rainbow_light = RainbowText("Rainbow text with higher lightness.", l = 80.0)
image rainbow_both = RainbowText("Rainbow text with both lower saturation and higher lightness.", s = 20.0, l = 80.0)

screen rainbows():

    tag rainbowSCR

    vbox:
        align (0.5, 0.5)
        spacing 5

        text "This screen uses defined RainbowTexts that preserve their state when hidden." xalign 0.5 underline True color "fff"

        null height 40

        add "rainbow_slow"
        add "rainbow_basic"
        add "rainbow_fast"
        add "rainbow_fastest"

        null height 40

        add "rainbow_start"

        null height 40

        add "rainbow_desat"
        add "rainbow_light"
        add "rainbow_both"

        null height 55

        textbutton "Back to Main Menu" xalign 0.5 action Return() text_idle_color "fff"