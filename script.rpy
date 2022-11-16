###################################################################################################
### Screen that picks between rainbows and rainbows_reset. ########################################
###################################################################################################

screen rainbows_pick():

    tag rainbowSCR

    vbox:
        first_spacing 50
        spacing 20
        align (0.5, 0.5)

        text "Both screens shown by buttons below display defined RainbowText displayables." color "fff"

        textbutton "Show a regular (image statement) way.\nPreserves the states when the screen is closed." action Show("rainbows_basic")
        textbutton "Show an alternative (default statement) way.\nResets the states anytime the screen is entered." action Show("rainbows")

###################################################################################################
### start label. ######################################### ########################################
###################################################################################################

label start:

    call screen rainbows_pick

    return
