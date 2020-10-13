# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Sara", color= "#d0a1ff")
define g = Character("Gab", color= "#10b063")

# The game starts here.

label start:

    play music "audio/jazzyfrenchy.mp3"

    scene bg home evening2

    pause .5

    show sara happy 1 with dissolve:
        xalign -4.0
        yalign 0.35

    s "Let's get going!!"

    show gab surprised 1 with moveinright:
        xalign 4.0
        yalign 0.45

    g "Look at those houses!"

    scene bg park evening with dissolve

    s "Are we going the right way?"

    show sara surprised 2 with dissolve:
        xalign -4.0
        yalign 0.45
    show gab neutral 1 with dissolve:
        xalign 4.0
        yalign 0.45

    "They're not going the right way"

    s "I think we were supposed to turn left back there"

    "Yeah, too late for that now"

    show gab mad 2 with dissolve:
        xalign 4.0
        yalign 0.45
    show sara surprised 2 with dissolve:
        xalign -4.0
        yalign 0.45
    g "Which way are we supposed to go now?"

    menu:
        "I think we should go straight into the park":
            jump park

        "I think we should to left to the underpass":
            jump underpass

    label park:

        scene bg night park
        show gab neutral 1 with dissolve:
            xalign 4.0
            yalign 0.40
        show sara happy 1 with dissolve:
            xalign -4.0
            yalign 0.35

        g "I just feel like we should have gone to the underpass"
        s "{b}{i}That{/i}{/b} is how people die in scary movies"
        "She does kind of have a point. Not exactly the right point, but it's the thought that counts"
        g "Where are we even headed?"
        s "We're just gonna ask someone if they can point us in the right direction"
        g "{b}{i} Actually, that {/i}{/b} is how people die"
        #insert snap sound
        play sound "audio/snapsound.mp3"

        show sara surprised 2:
            xalign -4.0
            yalign 0.45
        show gab surprised 1:
            xalign 4.0
            yalign 0.45

        menu:
            "hello?":
                jump park2
            "I think we should go":
                jump back


    label underpass:

        scene bg underpass
        show sara mad 1:
            xalign -4.0
            yalign 0.45
        show gab mad 2:
            xalign 4.0
            yalign 0.45

        s "Are we sure this is safe?"
        g "There aren't any cars around. There's no way that it's not"
        "That's naïve but okay, I suppose"
        # insert snap sound here
        stop music
        play sound "audio/snapsound.mp3"

        s "{i}What was that?{/i}"

        g "You worry so much"

        show sara surprised 2 with move:
            xalign 2.0
            yalign 0.45
        show gab mad 2:
            xalign 4.0
            yalign 0.45
        play sound "audio/cardriving.mp3"

        g "Nice job almost getting hit"

        s "Nice job not pulling me out of the way"

        g "How was I supposed to know it was there before you did?"

        show casualsurprise with moveinleft:
            xalign -1.0
            yalign 0.55
        stop sound
        play music "audio/creepybg.mp3"
        "Boy" "Excuse me"
        show sara confused 1:
            xalign 2.5
            yalign 0.35
        show gab surprised 1:
            xalign 4.0
            yalign 0.45

        "Oh no"
        s "..Hi"
        s "Can we help you?"
        "Boy" "No, you were just in my way"
        "Yeah that's awkward"

        show gab sorry 1:
            xalign 4.5
            yalign 0.45
        show sara neutral 2:
            xalign -2.0
            yalign 0.55
        hide casualsurprise with dissolve

        g "Anyway"
        s "I don't want to be out here anymore"
        "I don't blame you"
        scene bg turnpike with dissolve
        show sara surprised 2 with dissolve:
            xalign -3.0
            yalign 0.45
        show gab mad 2 with dissolve:
            xalign 4.0
            yalign 0.45
        s "Did you hear that?"
        g "Hear what?"
        stop music
        play sound "audio/tires.mp3"
        scene bg cemetary with dissolve
        "Oops"
        "I probably should have warned them somehow LOL"
        "Maybe next time"
        "The End."
    return



    label park2:
        scene bg night park
        show sara confused 1 with dissolve:
            xalign -4.0
            yalign 0.35
        show gab surprised 1 with dissolve:
            xalign 4.0
            yalign 0.45
        s "Hello?"
        "No one appears"
        g "Maybe we should keep moving. Something's not right out here"
        s "Yeah, let's go"

        play music "audio/creepybg.mp3"
        scene bg park 2 with dissolve
        show gab neutral 2 with dissolve:
            xalign 4.0
            yalign 0.45
        show sara gesture 2 with dissolve:
            xalign -4.0
            yalign 0.45
        "Gab and Sara walk for what seems like forever in the dark"

        scene bg mansion with dissolve
        show gab surprised 1 with dissolve:
            xalign 4.0
            yalign 0.45
        show sara surprised 2 with dissolve:
            xalign -4.0
            yalign 0.45
        "They stumble on a mansion. There doesn't seem to be anyone around, but the lights are on inside."
        s "Do you think they'd let us in? I'm tired of walking"
        g "I mean..probably not but we could try"
        show gab sorry 1:
            xalign 4.0
            yalign 0.45
        show sara happy 1:
            xalign -4.0
            yalign 0.35
        s "Alright take your bets!! Im guessing they will"
        g "I don't think this is a good idea"
        show gab neutral 2

        menu:
            "Go Inside":
                jump mansion
            "Turn around":
                jump back


    label mansion:
        scene bg inside mansion
        show sara gesture 2 with dissolve:
            xalign -4.0
            yalign 0.45
        show gab neutral 2 with dissolve:
            xalign 4.0
            yalign 0.45
        g "This is definitely illegal"
        s "Shhh. I don't hear anyone"
        show gab mad 2 with dissolve:
            xalign 4.0
            yalign 0.45
        g "That doesn't mean we should keep going in!!"
        s "It's too late for that now hun, you're in this with me"
        "They continue walking through what seems to be a deserted mansion."
        "Somehow all the lights are still on"
        "Who's paying the electric bills around here???"


        scene bg mansion room with dissolve
        show gab mad 1 with dissolve:
            xalign 4.0
            yalign 0.40
        show sara happy 3 with dissolve:
            xalign -4.0
            yalign 0.35
        s "You think we should crash here for tonight?"
        g "{i}Absolutely{/i} not"
        "That's..a little gross but do what you want"
        play sound "audio/squeakydoor.mp3"
        g "Sara I swear to God if you just dragged me into an actual haunted mansion"
        stop sound
        s "Don't be so dramatic! This place isn't haunted"
        "Are we sure about that?"
        play sound "audio/yikes.mp3"

        scene bg cemetary with dissolve
        "Who's going to tell them?"
        "Wait is that me?"
        "Oh.. oh well I guess"
        "The End"
        return



    label back:
        stop music
        play music "audio/jazzyfrenchy.mp3"
        scene bg field night with dissolve
        show sara mad 1 with dissolve:
            xalign -4.0
            yalign 0.45
        show gab sad 1 with dissolve:
            xalign 4.0
            yalign 0.45
        "Sara and Gab walked for several hours"
        s "How long have we been walking?"
        g "Too long"
        hide gab sad 1 with dissolve
        hide sara mad 1 with dissolve
        "They carried on until the morning, taking few breaks to try and make it back home."
        "Their cell phones were long dead."
        scene bg sunrise with dissolve
        g "{i}Do {b}not{/b}{/i} tell me that is the sun."
        s "It is, unfortunately"

        "After 12 hours of continous trecking through the night, they finally made it home."
        


return


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    # This ends the game.
