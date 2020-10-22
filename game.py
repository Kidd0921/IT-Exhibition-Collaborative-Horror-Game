import pyglet
import random


# Jumpscare sounds
def scare_sound():
    s1 = pyglet.media.load("./assets/snd/a1.wav", streaming=False)
    s2 = pyglet.media.load("./assets/snd/a2.wav", streaming=False)
    s3 = pyglet.media.load("./assets/snd/a3.wav", streaming=False)
    s4 = pyglet.media.load("./assets/snd/a4.wav", streaming=False)
    s5 = pyglet.media.load("./assets/snd/a5.wav", streaming=False)

    sounds = [s1, s2, s3, s4, s5]
    selection = random.choice(sounds)
    player = pyglet.media.Player()
    player.queue(selection)
    player.play()

    # Debug
    """
    if selection == s1:
        print("s1")
    elif selection == s2:
        print("s2")
    elif selection == s3:
        print("s3")
    elif selection == s4:
        print("s4")
    elif selection == s5:
        print("s5")
    else:
        print("not in selection")
    """


# Jumpscare animations
def clickdie(index):
    # Get screen width and height
    canvas = pyglet.canvas.Display()
    display = canvas.get_default_screen()
    display_width, display_height = display.width, display.height

    if index == 1:
        ag_file = "./assets/img/s1.gif"
    else:
        ag_file = "./assets/img/s2.gif"

    animation = pyglet.image.load_animation(ag_file)
    sprite = pyglet.sprite.Sprite(animation)

    # Set window to fullscreen
    win = pyglet.window.Window(fullscreen=True)

    # Make sprite same width as screen
    sprite_width = sprite.width
    sprite_scale = display_width / sprite_width

    @win.event
    def on_draw():
        win.clear()
        sprite.draw()

        # Positions the sprite to approximately center of screen
        if index == 1:
            sprite.position = 0, display_height / (2 * sprite_scale)
            sprite.scale = sprite_scale
        else:
            sprite.position = 0, display_height / (4 * sprite_scale)
            sprite.scale = sprite_scale
    scare_sound()
    pyglet.app.run()


# continue, yes/no, play again prompts
def ask_continue():
    cont = input("Press c and then enter to continue: ")
    cont = cont.upper()
    while cont != 'C':
        cont = input("Press c and then enter to continue: ")
        cont = cont.upper()


def ask_yesno():
    var = input("Enter Y or N: ")
    var = var.upper()
    while var != "Y" and var != "N":
        var = input("Enter Y or N: ")
        var = var.upper()
    return var


def ask_playagain():
    play = input("Press s and then enter to play again: ")
    play = play.upper()
    while play != 'S':
        play = input("Press s and then enter to play again: ")
        play = play.upper()
    pass


# The juicy PLOT
def escape():
    print("You're now playing 'The Prison Escape Horror'")
    ask_continue()

    print('''
    You're Elizabeth and you're serving a life sentence in prison for murder.
    Angry and resentful about your situation, you decided that
    you can't spend your life in prison and you began plotting ways to
    escape from the jail.
    ''')
    ask_continue()

    print('''
    One day a caretaker reeks of the smell of alcohol approach you through
    the bars. He doesn't seem to be the type of person who can be trusted and
    rational.
    Do you wish to talk to him <Press Y and enter to continue> or turn a blind
    eye over him <Press N to continue>
    ''')

    choice1 = ask_yesno()
    if choice1 == "N":
        print('''
        You can see the sadness in the caretaker's eyes as he walks away. You went
        to bed.
        ''')

        print('''
        The next evening while you're having your dinner in the cafeteria you spilled
        stew on your shirt and you're now dirty. You now go to the shower room to get
        yourself clean. Mid-cleaning, alone, you hear noises like a metal object is dragging
        through the floor over the distance and moans that sounds like a person is in
        agony. You're confused and afraid. There are a few changing rooms behind you and frail
        ceilings you can break through and escape. QUICK YOU CAN HEAR HIS PRESENCE
        AROUND THE CORNER!

        Hide in the changing rooms <Press Y and enter to continue> or break the ceiling and escape
        <Press N and enter to continue>
        ''')

        choice2 = ask_yesno()
        if choice2 == "Y":
            clickdie(2)
            print('''
            You swiftly hid in one of the changing rooms and held your breath.
            The mysterious man making the noises
            broke every door of the changing rooms and breaks your door eventually.
            To your surprise, it was the caretaker from the day before but drunk and
            covered in blood and intestines of the other inmates on his shoulders holding
            a flimsy beheading axe. He has teary eyes and in a shaking voice he said all
            he wanted was a friend as he raises his axe and chopped you continuously and brutally
            until there is only mushes of flesh & blood and cracked bones.
            *GAME OVER THANK YOU FOR PLAYING*
            ''')
            ask_playagain()

        else:
            clickdie(2)
            print('''
            You tried to climb your way up but before you could reach the ceiling you slipped
            and fell onto the ground. You were unconscious and when you regain consciousness
            you see a man standing next to you. To your surprise, it was the caretaker from
            the day before but drunk and covered in blood and intestines of the other inmates
            on his shoulders holding a flimsy beheading axe. He has teary eyes and in a shaking
            voice he said all he wanted was a friend as he raises his axe and chopped you
            continuously and brutally until there is only mushes of flesh & blood and cracked
            bones.
            *GAME OVER THANK YOU FOR PLAYING*
            ''')
            ask_playagain()

    else:
        print('''
        You two talked and got to know each other and from that day on you've been talking to
        the prison caretaker through the bar since then every night. You became good friends
        with him. His job was to bury any prisoners who died, in a graveyard just outside the
        prison walls. Whenever a prisoner died, the caretaker ring the bell and heard by all
        inmates. The caretaker then get the body and put it in a casket, lid nail shut, put
        the casket on a wagon to take it to the graveyard and bury it.

        Knowing this routine, you devised an escape plan and shared it with the caretaker.
        The next time the bell rang, you would leave the cell and sneak into the dark room
        where the coffins were kept. You would slip into the coffin with the dead body while
        the caretaker is filling out the death certificate. When he returns, he would nail it
        an take it with you in it along with the dead body. He would then bury the coffin.
        ''')
        ask_continue()

        print('''
        The caretaker was reluctant to go along with this plan. Shortly after, he came to your
        cell and agreed to do it. You were thrilled. The caretaker interrupted you politely and
        shyly confessed his feelings to you and asked if you feel the same way. Even after
        quite some time you two have been friends you still have this feeling that he's an
        unstable and dangerous man.

        You now have a choice to lie to him that you
        do feel the same way <Press Y to continue> or tell him the truth <Press N to continue>
        ''')

        choice3 = ask_yesno()
        if choice3 == "Y":
            print('''
            You lied to the prison caretaker. He grinned at you and said that he's
            glad that you feel the same way as he does for you.

            You waited several weeks for one of the other prison inmates to die.
            One night, you were asleep in your cell when you heard the death bell ringing.
            You got up, picked the lock of your cell, and slowly walked down the hallway.
            You were nearly caught a couple of times. Your heart was beating fast.
            ''')

            ask_continue()
            clickdie(1)
            print('''
            You opened the door to the darkened room where the coffins were kept.
            Quietly in the dark, you found the coffin that contained the dead body,
            carefully climbed into it and pulled the lid shut to wait for the caretaker
            to come and nail the lid down.

            Soon you heard footsteps and the pounding of the hammer and nails. The coffin was
            lifted onto the wagon and taken outside to the graveyard. At one point in that
            journey, The caretaker speaks to you through the coffin while riding saying he knew
            you were lying all along and can't bear the pain of the thought of you leaving him. He
            wants you be by 'his side forever' and drove himself and you down to a river. You tried
            to push the lid of coffin but it was a futile attempt as water fills in from the
            holes of the coffin.
            Not long enough you found yourself submerged in water screaming helplessly,
            losing your consciousness...

            *GAME OVER THANK YOU FOR PLAYING*
            ''')
            ask_playagain()
        else:
            print('''
            You told him the truth. He gave you a bitter grin and said it was okay.

            You waited several weeks for one of the other prison inmates to die.
            One night, you were asleep in your cell when you heard the death bell ringing.
            You got up, picked the lock of your cell, and slowly walked down the hallway.
            You were nearly caught a couple of times. Your heart was beating fast.

            You opened the door to the darkened room where the coffins were kept.
            Quietly in the dark, you found the coffin that contained the dead body,
            carefully climbed into it and pulled the lid shut to wait for the caretaker
            to come and nail the lid down.
            ''')
            ask_continue()

            clickdie(1)
            print('''
            Soon you heard footsteps and the pounding of the hammer and nails. The coffin was
            lifted onto the wagon and taken outside to the graveyard. Your coffin was
            lowered into the ground. You didn't make any sound. Finally you were buried and you
            chuckled quietly to yourself.

            Feeling curious, you decided to light a match to find out the identity of the dead
            prisoner beside you. To your horror.. You discovered that you were lying on top of
            the DEAD CARETAKER!

            *GAME OVER THANK YOU FOR PLAYING*
            ''')
            ask_playagain()


# Plays background music
bg_media = pyglet.media.load("./assets/snd/bg.wav")
bg_group = pyglet.media.SourceGroup(bg_media.audio_format, None)
bg_group.loop = True
bg_group.queue(bg_media)
bg_player = pyglet.media.Player()
bg_player.queue(bg_group)
bg_player.play()


# Executes the PLOT
while True:
    for i in range(100):
        print("")
    escape()
