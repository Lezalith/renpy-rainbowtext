###################################################################################################
### Defining RainbowTexts inside screen so that they reset everytime the screen is shown. #########
###################################################################################################

screen rainbows_reset(): 

    tag rainbowSCR

    default rainbow_basic = RainbowText("Rainbow text with the default interval of 0.5.")

    default rainbow_slow = RainbowText("Rainbow text with the slower interval of 0.1.", interval = 0.1)
    default rainbow_fast = RainbowText("Rainbow text with the faster interval of 1.0.", interval = 1.0)
    default rainbow_fastest = RainbowText("Rainbow text with the even faster interval of 3.0.", interval = 3.0)

    default rainbow_start = RainbowText("Rainbow text starting at 175.0 (cyan),\nwith very slow interval (0.05) to make it more noticable.", interval = 0.05, start = 175.0)

    default rainbow_desat = RainbowText("Rainbow text with lower saturation", s = 20.0)
    default rainbow_light = RainbowText("Rainbow text with higher lightness.", l = 80.0)
    default rainbow_both = RainbowText("Rainbow text with both lower saturation and higher lightness.", s = 20.0, l = 80.0)

    vbox:
        align (0.5, 0.5)
        spacing 5

        text "This screen resets all RainbowTexts when entered." xalign 0.5 underline True color "fff"

        null height 40

        add rainbow_slow
        add rainbow_basic
        add rainbow_fast
        add rainbow_fastest

        null height 40

        add rainbow_start

        null height 40

        add rainbow_desat
        add rainbow_light
        add rainbow_both

        null height 55

        textbutton "Back to Example Selection" xalign 0.5 action Show("rainbows_pick") text_idle_color "fff"