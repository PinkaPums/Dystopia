'''
Created on 23.09.2018

@author: michagress
'''

import time
from random import randint

# Spieler
mLP = [90] # myLebenspunkte, Lebenspunkte des Spielers
mW = ['Faust'] # Ausgerüstete Waffe
mHP = [3] # ausgeübter Schaden
mI = [ ] # Inventar
mAus = ["Unterhose"] # Kleidung, Rüstung
mS = [1] # Schutz der Kleidung
mLuck = [1]

mG = [] #Zerstörte Gegenstände, Muell
mG2 = [] #Zerstörte Gegenstände, Muell
mG3 = [] #Zerstörte Gegenstände, Muell
mG4 = [] #Zerstörte Gegenstände, Muell
mG5 = []
mG6 = []
mG7 = []
mG8 = []

# Dauerhafte Schäden

mLippeAb = ['Dran']
mLosungswort = ['Bitteschön']
mStoffKuscheltier = ['Rotauge']
mMonsterGesehen = ['Nein']
iVerProf = ['Verrückt']
iBewFrau = ['Aggressiv']
iMedAbtEingang = ['Verschlossen']
iTürHPasswort = ['Unbekannt']
iNarrezMerana = ['Unwissend']
iGenerator = ['Aus']
iKleineRüstung = ['Raum']

# Verbrauchbare Gegenstände

medikit1 = ['Unbenutzt']

# Gegner

iWesen1LP = [6]
iWesen1HP = [2]
iWesen1S = [1]

iWesen2LP = [8]
iWesen2HP = [3]
iWesen2S = [1]

iEtwasLP = [11]
iEtwasHP = [4]
iEtwasS = [1]

iWulffLP = [30]
iWulffHP = [8]
iWulffS = [2]
iWulffLuck = []

iMMonsterLP = [95]
iMMonsterHP = [19]
iMMonsterS = [7]

iRotAuge1LP = [20]
iRotAuge1HP = [7]
iRotAuge1S = [2]
iRotAuge1Luck = []

iRotAuge2LP = [25]
iRotAuge2HP = [8]
iRotAuge2S = [2]
iRotAuge2Luck = []

iRotAuge3LP = [40]
iRotAuge3HP = [9]
iRotAuge3S = [3]
iRotAuge3Luck = []

iRotAuge4LP = [30]
iRotAuge4HP = [8]
iRotAuge4S = [2]

iRotAuge5LP = [25]
iRotAuge5HP = [9]
iRotAuge5S = [1]

iRotAuge6LP = [20]
iRotAuge6HP = [10]
iRotAuge6S = [3]




# Einführung-------------------------------------------------
print("\n\n\n\nPROUDLYPRESENTEDGAMES proudly presents")
time.sleep(3)
print("a HAEFEM gamestudio gamy game")
time.sleep(3)
print("in cooperation with PYTHONKURSFU+00FCREINSTEIGER animation studios")
time.sleep(3)

def startBildschirm(environment):
    print("###########################################################\n")
    time.sleep(0.2)
    print("                          DYSTOPIA                        \n")
    time.sleep(0.1)
    print("                     ")
    time.sleep(1.9)
    print("                           or:                            ")
    time.sleep(0.2)
    print("             ")
    time.sleep(0.5)
    print("   Escape from the Spaceship and don't die while trying   ")
    time.sleep(0.2)
    print("###########################################################\n")
    time.sleep(2.9)
    print("                            play")
    time.sleep(0.2)
    print("                            help")
    time.sleep(0.2)
    print("                            quit")
    time.sleep(0.2)
    print("\n#########################################################")
    time.sleep(0.2)
    
    cmdlist = ['play', 'quit', 'help', 'pay']
    cmd = getcmd(cmdlist)
    
    if cmd == 'play' or cmd == 'pay':
        time.sleep(1)
        print("Game is started")
        time.sleep(1)
        print("And here a little help from the developer:")
        time.sleep(2.5)
        print("    If you get stuck at a specific point in the game:   ")
        time.sleep(2)
        print("            try to LOOK AROUND.            ")
        time.sleep(2)
        print("                Have fun...               ")
        time.sleep(2)
        intro(environment)
    elif cmd == 'quit':
        time.sleep(1)
        print("Goodbye")
        time.sleep(5)
        exit()
    elif cmd == 'help':
        time.sleep(1)
        print("If you run into any trouble while playing, the input 'HELP' will help you")
        print("to find the right command.")
        time.sleep(2)
        print()
        print()
        startBildschirm(environment)

        
def intro(environment):    

    print("...")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("You wake up.")
    time.sleep(3)
    print("After a few seconds of numbness and disorientation,")
    print("a throbbing pain in your head takes over your attention.")
    time.sleep(5)
    print("You touch your head...")
    time.sleep(2)
    print("When you put your hand down, blood sticks to your fingers.")
    time.sleep(2)
    print("...")
    time.sleep(2)
    print("You try to remember what happened last, but you can't remember where you are...")
    time.sleep(2)
    print("...or who you are.")
    time.sleep(1)
    print("...")
    time.sleep(2)
    print("You're wearing nothing but your underwear.")
    time.sleep(7)
    print("After a few minutes you feel strong enough to stand up.")
    time.sleep(3)
    kryokammer(environment)


# Umgebung - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def kryokammer(environment):
    
    cmdlist = [
               'look around',
               'look',
               'use terminal',
               'go to terminal', 
               'go to information terminal',
               'use information terminal',
               'go to exit',
               'go to door',
               'examine exit',
               'examine door',
               'use exit',
               'use door',
               'examine cryo pod',
               'examine cryo pods',
               'examine pod',
               'examine pods',
               'use switch',
               'put on clothes',
               'put on prison uniform',
               'put on uniform',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'look around' or cmd == 'look':
        time.sleep(0.5)
        print("You take a closer look around the darkened room.")
        time.sleep(1.5)
        print("It seems that you are in a small cryogenic chamber.")
        time.sleep(1.5)
        print("The room is spartanly furnished, with three CRYO PODs")
        print("on the opposite side of the room's only EXIT.")
        time.sleep(4)
        print("Two of the CRYO PODs are open, the other is closed.")
        time.sleep(1.5)
        print("An INFORMATION TERMINAL is connected to each of the CRYO PODs.")
        time.sleep(1.5)
        if 'Gefangenenoverall' in mAus or 'Gefangenenoverall' in mG:
            kryokammer(environment)
        else:
            print("On the floor next to the CRYO POD you woke up in front of is a PRISON UNIFORM.")
            kryokammer(environment)
        
    elif cmd == 'go to terminal' or cmd == 'use terminal' or cmd == 'go to information terminal' or cmd == 'use information terminal':
        time.sleep(0.5)
        print('There are three terminals in front of you.')
        time.sleep(0.5)
        terminal(environment)
            
    elif cmd == 'go to door' or cmd == 'go to exit' or cmd == 'use exit' or cmd == 'use door' or cmd == 'examine exit' or cmd == 'examine door':
        time.sleep(0.5)
        print('You are standing in front of the exit.')
        time.sleep(1)
        print('Next to the door is a SWITCH for opening the door.')
        time.sleep(1)
        kryokammer(environment)
        
    elif cmd == 'use switch':
        time.sleep(0.5)
        print('Ping\n----\n')
        time.sleep(1)
        print('The door opens and bright, dazzling light shines into the room.')
        time.sleep(2)
        print('What do you want to do?\n')
        time.sleep(1)
        print('(1) Further investigation of cryo chamber?')
        time.sleep(0.5)
        print('(2) Exit cryo chamber?')
        time.sleep(0.5)
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
            
        if cmd == '1':
            time.sleep(0.5)
            print("''I'd better take a closer look around.''")
            time.sleep(1)
            print("The door closes again after a few seconds.")
            time.sleep(0.5)
            kryokammer(environment)          
        elif cmd == '2':
            time.sleep(0.5)
            print('You leave the room.')
            time.sleep(2)
            print("You enter a long corridor and the door closes behind you.")
            time.sleep(0.5)
            print("You walk along the corridor and come to a junction.")
            time.sleep(0.5)
            flurSüd(environment)
                 
    elif cmd == 'examine cryo pod' or cmd == 'examine cryo pods':
        time.sleep(0.5)
        print('You examine the three pods.')
        time.sleep(2)
        print("...")
        time.sleep(3)
        print("A person dressed in a prisoner's uniform is lying in the left one,")
        print("the inside pane is scratched.")
        time.sleep(3)
        print("'The pod was defrosted, but the opening sequence for the gate did not start.")
        print("  The sleeper slowly suffocated.")
        time.sleep(6)
        print("  ...")
        time.sleep(2)
        print("  what a gruesome death.''")
        time.sleep(3)
        print("The right and centre pod are open, you were unconscious in front of the right one.")
        time.sleep(2)
        print("There's a small bloodstain right where your head was.")
        time.sleep(2)
        print("You touch your wound and take another look inside the left pod...")
        time.sleep(1)
        print("''...")
        time.sleep(1)
        print("  I could definitely have been worse off.''")
        time.sleep(0.5)
        kryokammer(environment)

        
    elif cmd == 'put on clothes' or cmd == 'put on uniform' or cmd == 'put on prison uniform':
        if 'Gefangenenoverall' in mAus or 'Gefangenenoverall' in mG:
            time.sleep(0.5)
            print("You had already put on the prisoner's overall...")
            time.sleep(1)
            print("There is nothing left here.")
            time.sleep(1)
            kryokammer(environment)
        elif mAus[0] != "Unterhose":
            time.sleep(0.5)
            print("Take off your clothes before putting on new ones.")
            time.sleep(1.5)
            kryokammer(environment)
        else:
            time.sleep(0.5)
            print("You put on the prisoner's overall.")
            time.sleep(1)
            print("It is quite uncomfortable and offers little protection.")
            time.sleep(1)
            print("''At least it's better than walking around in your underwear.'")
            mAus.remove('Unterhose')
            mAus.append('Gefangenenoverall')
            mS.remove(1)
            mS.append(2)
            time.sleep(1.5)
            kryokammer(environment)
                
def terminal(environment):
    
    time.sleep(0.5)
    print('\nWhich of the terminals do you want to use?')
    time.sleep(0.5)
    print('(1) Terminal left')
    time.sleep(0.2)
    print('(2) Terminal center')
    time.sleep(0.2)
    print('(3) Terminal right')
    time.sleep(0.2)
    print('(4) End operation')   
    time.sleep(0.2) 
            
    cmdlist = ['1', '2', '3', '4',]
    cmd = getcmd(cmdlist)
            
    if cmd == '1':
        time.sleep(0.5)
        print('A field with various selection options is shown on the display.')
        time.sleep(1)
        terminal1(environment)
    elif cmd == '2':
        print('A field with various selection options is shown on the display.')
        time.sleep(1)
        terminal2(environment)
    elif cmd == '3':
        print('A field with various selection options is shown on the display.')
        time.sleep(1)
        terminal3(environment)
    elif cmd == '4':
        print('You turn away from the terminals.')
        time.sleep(1)
        kryokammer(environment)

def terminal1(environment):
    time.sleep(0.5)
    print("\n(1) ''Information about prisoner''")
    time.sleep(0.4)
    print("(2) ''Status''") 
    time.sleep(0.3)
    print("(3) ''Open''")
    time.sleep(0.7)
    print("(4) Go to another terminal")
    time.sleep(0.1)
    print("(5) End operation")
    time.sleep(0.6)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nLoading file...")
        time.sleep(2.1)
        print("...Prisoner 034629/348/23")
        time.sleep(0.8)
        print("...Name: Irc Zoek")
        time.sleep(1.2)
        print("...Transferring offender to Karion 4")
        time.sleep(0.1)
        print("...")
        time.sleep(0.4)
        print("...No further information available.\n''")
        time.sleep(0.5)
        terminal1(environment)
    elif cmd == '2':
        time.sleep(1)
        print("'' \nLoading file....")
        time.sleep(1.7)
        print("...")
        time.sleep(0.8)
        print("No signs of life, subject death\n''")
        time.sleep(0.5)
        terminal1(environment)
    elif cmd == '3':
        time.sleep(1)
        print("'...")
        time.sleep(2.4)
        print("''That's probably not a good idea, I'd rather not do that''")
        time.sleep(0.5)
        terminal1(environment)
    elif cmd == '4':
        time.sleep(0.5)
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("You turn your attention to the rest of the room.")
        time.sleep(0.5)
        kryokammer(environment)
        
def terminal2(environment):
    time.sleep(0.5)
    print("\n(1) ''Information about prisoner''")
    time.sleep(0.4)
    print("(2) ''Status''") 
    time.sleep(0.3)
    print("(3) ''Open''")
    time.sleep(0.7)
    print("(4) Go to another terminal")
    time.sleep(0.1)
    print("(5) End operation")
    time.sleep(0.6)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nLoading file...")
        time.sleep(2.1)
        print("...Prisoner 190662/836/54")
        time.sleep(1.4)
        print("...Name: Izzin Quin")
        time.sleep(1.2)
        print("...Transferring offender to Karion 4")
        time.sleep(0.5)
        print("...")
        time.sleep(0.2)
        print("...No further information available.\n''")
        time.sleep(0.5)
        terminal2(environment)
    elif cmd == '2':
        time.sleep(1.2)
        print("'' \nLoading file...")
        time.sleep(2.3)
        print("...")
        time.sleep(0.3)
        print("...Cryo pod opened manually...")
        time.sleep (0.7)
        print("...\n''")
        time.sleep(0.5)
        terminal2(environment)
    elif cmd == '3':
        time.sleep(1.5)
        print("''\n...")
        time.sleep(0.9)
        print("...Pod opened")
        time.sleep(0.5)
        terminal2(environment)
    elif cmd == '4':
        time.sleep(0.5)
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("You turn your attention to the rest of the room.")
        time.sleep(0.5)
        kryokammer(environment)
        
def terminal3(environment):
    time.sleep(0.5)
    print("\n(1) ''Information about prisoner''")
    time.sleep(0.4)
    print("(2) ''Status''") 
    time.sleep(0.3)
    print("(3) ''Open''")
    time.sleep(0.7)
    print("(4) Go to another terminal")
    time.sleep(0.1)
    print("(5) End operation")
    time.sleep(0.6)
        
    cmdlist = ['1', '2', '3', '4', '5',]
    cmd = getcmd(cmdlist)
        
    if cmd == '1':
        time.sleep(1)
        print("''\nLoading file...")
        time.sleep(2.1)
        print("...Prisoner 976663/124/11")
        time.sleep(0.3)
        print("...Name: Narilyn Rezamo")
        time.sleep(0.2)
        print("...Transferring offender to Karion 4")
        time.sleep(0.2)
        print("...")
        time.sleep(0.2)
        print("...No further information available.\n''")
        time.sleep(0.5)
        terminal3(environment)
    elif cmd == '2':
        time.sleep(1.2)
        print("'' \nLoading file...")
        time.sleep(2.3)
        print("...")
        time.sleep(0.3)
        print("...Cryo pod opened manually...")
        time.sleep (0.7)
        print("...\n''")
        time.sleep(0.5)
        terminal3(environment)
    elif cmd == '3':
        time.sleep(1.5)
        print("''\n...")
        time.sleep(0.9)
        print("...Pod opened")
        time.sleep(0.5)
        terminal3(environment)
    elif cmd == '4':
        time.sleep(0.5)
        terminal(environment)
    elif cmd == '5':
        time.sleep(0.5)
        print("You turn your attention to the rest of the room.")
        time.sleep(0.5)
        kryokammer(environment)
        
def flurSüd(environment):
    time.sleep(0.5)
    print("\n(1) Turn right")
    time.sleep(0.5)
    print("(2) Turn left")
    time.sleep(0.5)
    print("(3) Go back")
    
    cmdlist = ['1', '2', '3', 'look around', 'look',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print('You choose the right path.')
        time.sleep(1.5)
        flurSüdRechts(environment)
    elif cmd == '2':
        time.sleep(0.5)
        print("You choose the left path.")
        time.sleep(1.5)
        flurSüdLinks(environment)
    elif cmd == '3':
        time.sleep(0.5)
        print("You go back.")
        time.sleep(2)
        print("You are standing in front of the closed door to the cryo chamber.")
        time.sleep(1)
        print("(1) Open the door and enter the room")
        time.sleep(0.5)
        print("(2) Go back")
        time.sleep(0.5)
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("You open the door and step inside.")
            time.sleep(1)
            print("Everything is the same as before.")
            time.sleep(1)
            kryokammer(environment)
        elif cmd == '2':
            time.sleep(0.5)
            print("You walk along the corridor and come to a junction.")
            time.sleep(0.5)
            flurSüd(environment)
    
    elif cmd == 'look around' or cmd == 'look':
        time.sleep(0.5)
        print("Two corridors lead off to the left and right.")
        time.sleep(1.5)
        print("After a short distance, both paths turn straight ahead.")
        time.sleep(1.5)
        flurSüd(environment)
        
def flurSüdRechts(environment):
    time.sleep(0.5)
    print("\nYou move towards the bend to the left and look carefully round the corner.")
    time.sleep(2)
    print("An empty corridor leads to a door, with further doors to the left and right along the corridor.")
    time.sleep(3)
    print("(1) Continue along this path")
    time.sleep(0.5)
    print("(2) Examine the other branch")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'look', 'look around',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("As you walk slowly and quietly along the path, you hear a noise behind you.")
        time.sleep(2)
        print("You turn round and see that a kind of emergency airlock is closing the way back to the cryo pods.")
        time.sleep(3)
        print("You run back, but the path is already blocked.")
        time.sleep(1.5)
        print("As you turn round again, there are two people standing in the corridor, one further back and one almost directly in front of you.")
        time.sleep(3.5)
        print("You are about to say something when you realise that the person in front of you hardly looks human.")
        time.sleep(2.5)
        print("It stretches out its arms towards you.")
        time.sleep(1.5)
        print("(1) Fight")
        time.sleep(0.5)
        print("(2) Try to talk")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', 'fight', 'attack']
        cmd = getcmd(cmdlist)
        
        if cmd == '1' or cmd == 'fight' or cmd == 'attack':
            time.sleep(0.5)
            kampf1FlurSüdRechts(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("When you try to talk to the creature, it attacks you.")
            mLP[0] = mLP[0] - 7
            time.sleep(0.5)
            kampf1FlurSüdRechts(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You decide to go the other way after all...")
        time.sleep(1.5)
        flurSüdLinks(environment)
        
    elif cmd == 'look around' or cm == 'look':
        time.sleep(0.5)
        print("As you take a closer look around, you discover a camera at the end of the path.")
        print("It seems to be active.")
        time.sleep(3)
        flurSüdRechts(environment)
        
def flurSüdRechtsGeschlossen(environment):
    time.sleep(0.5)
    print("\nYou are in the corridor near the cryo chamber.")
    
    cmdlist = [
               'look around',
               'look',
               'examine beings',
               'examine corpse',
               'examine corpses',
               'examine opponent',
               'examine door',
               'examine doors',
               'open door',
               'open doors',
               'examine exit',
               'go to exit',
               'open exit',
               'examine camera',
               'examine surveillance camera',
               'examine water dispenser',
               'examine dispenser',
               'use water dispenser',
               'use dispenser',
                ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You look around the corridor.")
        time.sleep(1.5)
        print("The two CORPSES of the strange creatures lie on the ground.")
        time.sleep(1.5)
        print("A SURVEILLANCE CAMERA is pointed directly at you, hanging above the only EXIT at the end of the corridor.")
        print("It appears to be active.")
        time.sleep(5)
        print("Two of the four DOORS on the sides are open,")
        print("presumably the attackers came out of these.")
        time.sleep(3)
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'examine beings' or cmd == 'examine corpse' or cmd == 'examine corpses' or cmd == 'examine opponent':
        print("The two corpses are wearing the same uniform as the two in the")
        if mAus[0] == 'Gefangenenoverall':
            time.sleep(0.5)
            print("cryo pods and as I am currently.")
            time.sleep(1.5)
            print("They no longer breathe and show no sign of life.")
            time.sleep(1.5)
            print("Their faces are pale, their eyes red.")
            time.sleep(1.5)
            print("Otherwise, neither of them has anything interesting on them.")
            time.sleep(1.5)
            flurSüdRechtsGeschlossen(environment)
        else:
            time.sleep(0.5)
            print("cryo pods. They no longer breathe and show no sign of life.")
            time.sleep(2)
            print("Their faces are pale, their eyes red.")
            time.sleep(1.5)
            print("Otherwise, neither of them has anything interesting on them.")
            time.sleep(1.5)
            flurSüdRechtsGeschlossen(environment)
            
    elif cmd == 'examine door' or cmd == 'examine doors':
        time.sleep(0.5)
        print("The two locked doors cannot be opened.")
        time.sleep(1.5)
        print("Behind the two open doors are sparsely furnished rooms.")
        time.sleep(2)
        print("The room is equipped with a toilet, a WATER DISPENSER and a hard bed.")
        time.sleep(1.8)
        print("That's all you find.")
        time.sleep(1)
        flurSüdRechtsGeschlossen(environment)

    elif cmd == 'open door' or cmd == 'open doors':
        time.sleep(0.5)
        print("Two of the doors cannot be opened.")
        time.sleep(1.5)
        print("The others are open.")
        time.sleep(0.5)
        flurSüdRechtsGeschlossen(environment)
        
    elif cmd == 'examine surveillance camera' or cmd == 'examine camera':
        time.sleep(0.5)
        print("You walk to the camera.")
        time.sleep(1)
        print("It remains rigid and you realise that it is switched off.")
        time.sleep(1.5)
        print("The camera is too high to touch.")
        time.sleep(1.5)
        flurSüdRechtsGeschlossen(environment)

        
    elif cmd == 'examine exit' or cmd == 'go to exit' or cmd == 'open exit':
        time.sleep(0.5)
        print("As you stand directly in front of the exit, the airlock opens.")
        time.sleep(1.5)
        print("(1) Walk through")
        time.sleep(0.5)
        print("(2) Investigate room further")
        time.sleep(0.5)
        
        cmdlist =['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("You go on...")
            time.sleep(2)
            narrezGespräch(environment)
        
        elif cmd == '2':
            time.sleep(0.5)
            print("You take another look around the room.")
            time.sleep(1)
            print("The airlock closes again.")
            flurSüdRechtsGeschlossen(environment)
            
    elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
        time.sleep(0.5)
        print("As you approach the water dispenser, a stream of water comes out.")
        time.sleep(1.5)
        print("The red undertone of the water flowing out worries you.")
        time.sleep(1.5)
        flurSüdRechtsGeschlossen(environment)


    elif cmd == 'use dispenser' or cmd == 'use water dispenser':
        time.sleep(0.5)
        print("You drink the water from the dispenser.")
        time.sleep(2)
        print("Something about this water tastes odd...")
        time.sleep(2.5)
        print("You feel strangely light-headed and your eyes start to itch...")
        time.sleep(3)
        print("You lose control of your body and your eyes go black...")
        time.sleep(7)
        exit()
        
def flurSüdLinks(environment):
    time.sleep(0.5)
    print('\nA feeling tells you that the left-hand path will be the right one.')
    time.sleep(1.5)
    print("When you reach the bend, you hear noises from further away.")
    time.sleep(1.5)
    print("You peek carefully around the corner...")
    time.sleep(1)
    print("You see the back of a person sitting on their knees.")
    time.sleep(1.5)
    print("They moves, there seems to be something in front of them that keeps them busy.")
    time.sleep(2)
    print("(1) Go to person")
    time.sleep(0.5)
    print("(2) Take the other path")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'look around', 'look']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You decide to see what's going on back there.")
        time.sleep(2)
        print("As you reach the person, an emergency lock closes behind you.")
        time.sleep(2)
        print("You turn around and are confused.")
        time.sleep(1.5)
        print("At the sight of the airlock, something grabs you by the shoulders...")
        time.sleep(3)
        print("This 'CREATURE' is smeared with blood on his mouth, cheeks and forehead.")
        time.sleep(1.5)
        print("It opens its mouth and tries to bite you.")
        time.sleep(1.5)
        print("(1) Fight")
        time.sleep(0.5)
        print("(2) Do nothing")
        time.sleep(3)
        
        cmdlist = ['1', '2', 'fight',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1' or cmd == 'fight':
            time.sleep(0.5)
            print("You attack!")
            time.sleep(1.5)
            kampfFlurSüdLinks(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("The creature attacks you and bites off a piece of your lip.")
            mLippeAb.remove('Dran')
            mLippeAb.append('Abgebissen')
            mLP[0] = mLP[0] - 12
            time.sleep(3.5)
            kampfFlurSüdLinks(environment)
    
    elif cmd == '2':
        time.sleep(0.5)
        print("You'd rather go the other way...")
        time.sleep(1.5)
        flurSüdRechts(environment)
    
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("Otherwise you don't notice anything special.")
        time.sleep(1)
        flurSüdLinks(environment)

def flurSüdLinksGeschlossen(environment):
    time.sleep(0.5)
    print("\nYou are in the corridor.")    
    
    cmdlist = [
               'look around',
               'look',
               'examine body',
               'examine creature',
               'examine person',
               'examine dead',
               'examine dead person',
               'open exit',
               'examine exit',
               'open door',
               'go to door',
               'go to exit',
               'take pipe',
               
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You look around the corridor.")
        time.sleep(1)
        print("The BODY of the CREATURE lies on the ground in front of you.")
        time.sleep(1.5)
        print("Near the DOOR, which is the only EXIT after the airlock")
        print("blocked the way to the cryo chamber, you find a DEAD PERSON.")
        time.sleep(4)
        print("Otherwise, there is nothing conspicuous in this corridor.")
        time.sleep(1.5)
        flurSüdLinksGeschlossen(environment)
        
    elif cmd == 'examine body' or cmd == 'examine creature':
        time.sleep(0.5)
        print("The creature's face is pale and its eyes are completely red.")
        time.sleep(1.5)
        print("The blood around its face seems to be that of the dead man further back.")
        time.sleep(2.5)
        print("It wears a prisoner's uniform, otherwise you don't notice anything.")
        time.sleep(2.5)
        flurSüdLinksGeschlossen(environment)
    
    elif cmd == 'examine person' or cmd == 'examine dead' or cmd == 'examine dead person':
        time.sleep(0.5)
        print("A badly battered man lies on the ground in front of you.")
        time.sleep(1.5)
        print("He looks like an ordinary person... just a little paler.")
        time.sleep(3)
        print("You can see that the man had probably used a PIPE for defence.")
        time.sleep(1.5)
        flurSüdLinksGeschlossen(environment)
        
    elif cmd == 'take pipe':
        if 'Rohr' in mAus or 'Rohr' in mG4:
            time.sleep(0.5)
            print("Pipe is broken.")
            time.sleep(1)
            flurSüdLinksGeschlossen(environment)
        elif mW[0] != 'Faust':
            time.sleep(0.5)
            print("Pipe is broken.")
            time.sleep(1)
            flurSüdLinksGeschlossen(environment)
        else:
            time.sleep(0.5)
            print("You take the pipe.")
            time.sleep(1.5)
            print("...")
            time.sleep(1.5)
            mW.remove('Faust')
            mW.append('Rohr')
            mHP.remove(3)
            mHP.append(7)
            print("Pipe is now equipped!")
            time.sleep(3)
            flurSüdLinksGeschlossen(environment)

    elif cmd == 'open exit' or cmd == 'examine exit' or cmd == 'open door' or cmd == 'go to door' or cmd == 'go to exit':
        time.sleep(0.5)
        print("As you stand directly in front of the exit, the airlock opens.")
        time.sleep(2)
        print("(1) Go through")
        time.sleep(0.5)
        print("(2) Investigate room further")
        time.sleep(0.5)
        
        cmdlist =['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("You walk into the next room...")
            time.sleep(3)
            narrezGespräch(environment)
        
        elif cmd == '2':
            time.sleep(0.5)
            print("You take another look around the corridor.")
            time.sleep(1)
            print("The airlock closes again.")
            flurSüdLinksGeschlossen(environment)

#
        
def gefangenentraktZentrale(environment):
    
    
    cmdlist = [
               'look around',
               'look',
               'go to man', 
               'go to narrez',
               'examine narrez',
               'examine man',
               'talk to man',
               'talk to narrez',
               'go to airlock', 
               'open airlock', 
               'examine airlock',
               'go to exit', 
               'open exit', 
               'examine exit', 
               'examine escape pod',
               'go to escape pod',
               'use escape pod',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around the room.")
        time.sleep(1.5)
        print("Next to a few lockers, boxes and cable harnesses is a control console,")
        print("in front of which a MAN stands, tapping furiously on the keys of a keyboard.")
        time.sleep(6)
        print("An ESCAPE POD can be seen next to the computer, but it appears to be locked at the moment.")
        time.sleep(3)
        print("There's an AIRLOCK where the man had pointed earlier.")
        time.sleep(1.5)
        print("The path to the cryochamber is and remains closed.")
        time.sleep(1.5)
        gefangenentraktZentrale(environment)
        
    elif cmd == 'go to man' or cmd == 'go to narrez' or cmd == 'examine man' or cmd == 'examine narrez' or cmd == 'talk to man' or cmd == 'talk to narrez' or cmd == 'examine escape pod' or cmd == 'go to escape pod' or cmd == 'use escape pod':
        if iMMonsterLP[0] <= 0:
            time.sleep(0.5)
            print("Narrez turns to you expectantly.")
            print("'Have you dealt with our problem?'")
            time.sleep(0.5)
            print("You answer him with a simple yes")
            time.sleep(0.5)
            print("'Very good, then all you have to do is get the generator running.")
            print(" You'd better hurry up!'")
            time.sleep(0.5)
            print("You turn away from him.")
            time.sleep(0.5)
            gefangenentraktZentrale(environment)
        elif mMonsterGesehen[0] != 'Ja':
            time.sleep(0.5)
            print("'What else are you looking for here!")
            time.sleep(1)
            print(" Go down and fix the generator!")
            time.sleep(1.5)
            gefangenentraktZentrale(environment)
        elif mMonsterGesehen[0] == 'Ja':
            time.sleep(0.5)
            print("You go to Narrez and tell him that a huge monster is lurking down there")
            print("and that it's impossible to march in there without the right equipment.")
            time.sleep(5)
            print("He looks at you aggressively and annoyed.")
            print("'Then go upstairs to the armoury and get something to sweep the thing away!'")
            time.sleep(5)
            print("He turns around and looks at the monitors again.")
            time.sleep(2)
            gefangenentraktZentrale(environment)
        
            
    elif cmd == 'go to airlock' or cmd == 'open airlock' or cmd == 'examine airlock' or cmd == 'go to exit' or cmd == 'open exit' or cmd == 'examine exit':
        time.sleep(0.5)
        print("You move in the direction of the airlock.")
        time.sleep(1.5)
        print("The airlock opens and you walk through it.")
        time.sleep(1.5)
        print("You are in a stairwell.")
        time.sleep(1)
        print("On a map on the wall you can see that the crew quarters should be above you")
        print("and the engine room below you.")
        time.sleep(4)
        print("One way leads upwards, the other downwards.")
        time.sleep(1.5)
        treppenhausGZ(environment)
        
def treppenhausGZ(environment):
    time.sleep(0.5)
    print("\nCurrent position: stairwell")
    time.sleep(0.5)
    print("(1) Go to the engine room")
    time.sleep(0.5)
    print("(2) Go to the crew quarters")
    time.sleep(0.5)
    print("(3) Go to the prison wing")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', '3', 'look', 'look around',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You head towards the engine room.")
        time.sleep(1.5)
        maschinenraumFlur(environment)
    elif cmd == '2':
        time.sleep(0.5)
        print("You go to the crew quarters.")
        time.sleep(1.5)
        mannschaftsquartiereFlur(environment)
    elif cmd == '3':
        if iBewFrau[0] == 'Traurig':
            time.sleep(0.5)
            print("You go to the prison wing.")
            time.sleep(1.5)
            gefangenentraktZentraleKeinNarrezMehr(environment)
        elif iNarrezMerana[0] == 'Wissend':
            time.sleep(0.5)
            print("You go to the prison wing.")
            time.sleep(1.5)
            gefangenentraktZentraleKeinNarrezMehr(environment)
        elif iGenerator[0] == 'An' and iNarrezMerana[0] == 'Unwissend':
            endeKeineFluchtkapsel(environment)
        elif iGenerator[0] == 'An' and iBewFrau[0] == 'Aggressiv':
            endeKeineFluchtkapsel(environment)
        else:
            time.sleep(0.5)
            print("You go to the prison wing.")
            time.sleep(1.5)
            gefangenentraktZentrale(environment)
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        time.sleep(1.5)
        print("There doesn't seem to be anything special in this room.")
        time.sleep(2)
        treppenhausGZ(environment)
    
def maschinenraumFlur(environment):
    time.sleep(0.5)
    print("\nCurrent position: Engine room corridor")
    time.sleep(0.5)
    print("(1) go towards the engine room")
    time.sleep(0.5)
    print("(2) go towards the prison wing")
    time.sleep(0.5)
    print("( ) other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', '2','examine lockers', 'examine locker', 'open j locker' , 'open h locker', 'look around', 'look', 'open j', 'open h',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You go towards the engine room.")
        time.sleep(1.5)
        maschinenraum(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You go towards the prison wing")
        time.sleep(1.5)
        treppenhausGZ(environment)
        
    elif cmd == 'examine locker' or cmd == 'examine lockers':
        time.sleep(0.5)
        print("-Which of the two LOCKERS would you like to OPEN?-")
        time.sleep(2)
        print("-J LOCKER or H LOCKER?-")
        time.sleep(1.5)
        maschinenraumFlur(environment)
        
    elif cmd == 'open j locker' or cmd == 'open j':
        if iTürHPasswort[0] != 'Izzin':
            time.sleep(0.5)
            print("You find a piece of paper with the following written on it:")
            print("Password: 92517")
            iTürHPasswort.remove('Unbekannt')
            iTürHPasswort.append('Izzin')
            time.sleep(1.5)
            maschinenraumFlur(environment) 
        else:
            time.sleep(0.5)
            print("You find a piece of paper with the following written on it:")
            print("Password: 92517")
            time.sleep(1.5)
            maschinenraumFlur(environment)
     
    elif cmd == 'open h locker' or cmd == 'open h':
        if 'Technikeroverall' in mAus or 'Technikeroverall' in mG3:
            time.sleep(0.5)
            print("The locker is empty.")
            time.sleep(1.5)
            maschinenraumFlur(environment)  
        elif mAus[0] != 'Unterhose':
            time.sleep(0.5)
            print("You open the locker and find a technician's uniform inside.")
            time.sleep(2)
            print("However, you are already wearing clothes and cannot put on the uniform.")
            time.sleep(2.5)
            print("Take off your clothes before you put on something new.")
            time.sleep(2)
            maschinenraumFlur(environment)
        else:    
            time.sleep(0.5)
            print("You open the locker and find a technician's uniform inside.")
            time.sleep(2)
            print("(1) Put on technician uniform")
            time.sleep(0.5)
            print("(2) Leave the technician's uniform behind")
            time.sleep(0.5)
        
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("You put on the uniform.")
                time.sleep(1.5)
                print("A little tight, but it fits and is comfortable.")
                mAus.remove('Unterhose')
                mAus.append('Technikeroverall')
                mS.remove(1)
                mS.append(4)
                time.sleep(2)
                maschinenraumFlur(environment)      
                
            elif cmd == '2':
                time.sleep(0.5)
                print("You'd better leave the uniform behind.") 
                time.sleep(1)
                maschinenraumFlur(environment)
        
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around you.")
        time.sleep(1.5)
        print("You are standing in a dark, long corridor.")
        time.sleep(1.5)
        print("Above you, various pipes go in all directions, the floor feels cold and hard,")
        print("the air is stuffy and you can smell pollution in the air.")
        time.sleep(6)
        print("As you walk along the path, you notice something large")
        print("lying on the ground in front of you.")
        time.sleep(3)
        print("You move closer.")
        time.sleep(1.5)
        print("...")
        time.sleep(1)
        print("A cold shiver runs down your spine...")
        time.sleep(1.5)
        print("In front of you lies a pile of corpses.")
        time.sleep(1.5)
        print("At least ten people in technician uniforms lie dead in front of you.")
        time.sleep(3)
        print("There are two LOCKERS near the next door.")
        time.sleep(1.5)
        print("On one LOCKER is the letter J, on the other one a H.")
        time.sleep(1.5)
        maschinenraumFlur(environment)

########
        
def maschinenraum(environment):
    if iMMonsterLP[0] > 0 and mMonsterGesehen[0] == 'Ja':
        mMonsterGesehen.remove('Ja')
        mMonsterGesehen.append('Nein')
        time.sleep(0.5)
        print("\nThe door to the engine room is heavy and squeaks when opened.")
        time.sleep(1.5)
        print("The door closes behind you and the light switches on at the same moment.")
        time.sleep(3)
        print("The monster has been waiting for you and attacks again.")
        time.sleep(2)
        mMonsterGesehen.remove('Nein')
        mMonsterGesehen.append('Ja')
        kampfMMonster(environment)
    elif iMMonsterLP[0] > 0:
        time.sleep(0.5)
        print("\nThe door to the engine room is heavy and squeaks when opened.")
        time.sleep(1.5)
        print("The door closes behind you and the light switches on at the same moment.")
        time.sleep(3)
        print("You can't believe your eyes!")
        time.sleep(1.5)
        print("A huge monster sits next to the door to the generator room and watches you.")
        time.sleep(2)
        print("It follows you with its red, dead eyes and finally attacks you.")
        time.sleep(4)
        time.sleep(2)
        mMonsterGesehen.remove('Nein')
        mMonsterGesehen.append('Ja')
        kampfMMonster(environment)
    else:
        time.sleep(0.5)
        print("\nCurrent position: Engine room")
        time.sleep(0.5)
        print("(1) go towards the prison wing")
        time.sleep(0.5)
        print("( ) other commands")
        time.sleep(0.5)
    
        cmdlist = ['1', 'look', 'look around', 'go to generator room', 'examine generator room' 'examine carcass']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("You walk towards the prison wing")
            time.sleep(1.5)
            maschinenraumFlur(environment)
        
        elif cmd == 'look' or cmd == 'look around':
            time.sleep(0.5)
            print("You take a look around.")
            time.sleep(1)
            print("One door is labelled GENERATOR ROOM.")
            time.sleep(1)
            print("The monster's CARCASS lies in the centre of the room, its stench is polluting the air.")
            time.sleep(2.5)
            print("The animal's cage is dented and covered with scratches and bite marks.")
            print("Otherwise you see large machines, switches, wheels and terminals.")
            time.sleep(1.5)
            maschinenraum(environment)
        
        elif cmd == 'examine generator room' or cmd == 'go to generator room':
            time.sleep(0.5)
            print("You open the door to the generator room and enter.")
            time.sleep(0.5)
            generatorraum(environment)
            
        elif cmd == 'examine carcass':
            time.sleep(1.5)
            print("You move closer to the monster's carcass.")
            time.sleep(1.5)
            print("As you walk around its head, the animal's eyes open.")
            time.sleep(1.5)
            print("You fall to the floor in shock!")
            time.sleep(1.5)
            print("The monster is coming towards you.")
            time.sleep(1.5)
            print("(1) attack the monster from the floor")
            time.sleep(0.5)
            print("(2) get away!")
            time.sleep(0.5)
            
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(1.5)
                print("The monster is getting closer and closer...")
                time.sleep(1.5)
                print("It's ramming you!")
                time.sleep(1.5)
                print("Your head hits the ground, the monster buries you underneath its big body.")
                time.sleep(1.5)
                print("It stops moving and you slowly suffocate in the stench of the monster.")
                time.sleep(4)
                print("GAME OVER")
                time.sleep(7)
                exit()
                
            elif cmd == '2':
                time.sleep(1.5)
                print("You get up and run to the nearest exit.")
                time.sleep(1.5)
                print("The monster is getting closer and closer to you...")
                time.sleep(1.5)
                print("You open the door...")
                time.sleep(1.5)
                print("...and slip into the next room.")
                time.sleep(1.5)
                print("A huge bang sounds as the door bulges towards you.")
                time.sleep(2.5)
                print("...")
                time.sleep(1.0)
                print("Nothing can be heard on the other side.")
                time.sleep(1.5)
                generatorraum(environment)
                

def generatorraum(environment):
    time.sleep(0.5)
    print("\nCurrent position: Generator room")
    time.sleep(0.5)
    print("(1) Go towards the prison wing")
    time.sleep(0.5)
    print("( ) other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', 'look','look around', 'use generator', 'examine generator', 'examine hatch', 'go to hatch']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("You walk towards the prison wing.")
        maschinenraum(environment)
        
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        time.sleep(0.7)
        print("Many GENERATORs provide the energy supply for the spaceship.")
        time.sleep(1.2)
        if iGenerator[0] == 'Aus':
            print("Some have failed, including the 4FK generator of which Narrez had spoken.")
            time.sleep(2)
            generatorraum(environment)
        else:
            print("Some have failed, but you have restarted the 4FK generator.")
            time.sleep(2)
            generatorraum(environment)
            
    elif cmd == 'use generator' or cmd == 'examine generator':
        time.sleep(0.5)
        print("You go to the generator 4FK")
        time.sleep(0.5)
        print("(1) Switch on the generator")
        time.sleep(0.5)
        print("(2) Switch off the generator")
        time.sleep(0.5)
        print("(3) Leave the generator as it is and step away")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            if iGenerator[0] == 'Aus':
                time.sleep(0.5)
                print("You press a button and suddenly the generator starts up again.")
                iGenerator.remove('Aus')
                iGenerator.append('An')
                time.sleep(1.5)
                generatorraum(environment)
            else:
                time.sleep(0.5)
                print("Generator activated")
                time.sleep(0.5)
                generatorraum(environment)
                
        elif cmd == '2':
            if iGenerator[0] == 'An':
                time.sleep(0.5)
                print("You press a button and the generator stops running.")
                iGenerator.remove('An')
                iGenerator.append('Aus')
                time.sleep(1.5)
                generatorraum(environment)
            else:
                time.sleep(0.5)
                print("Generator deactivated")
                time.sleep(0.5)
                generatorraum(environment)
                
        elif cmd == '3':
            time.sleep(0.5)
            print("'I prefer not to do that'")
            time.sleep(0.5)
            generatorraum(environment)
            
    elif cmd == 'untersuche luke':
        time.sleep(0.5)
        print("The hatch cannot be opened from this side.")
        time.sleep(0.5)
        generatorraum(environment)
            
def mannschaftsquartiereFlur(environment):
    time.sleep(0.5)
    print("\nYou are in the corridor of the crew quarters.")
    iRotAuge1Luck.append(randint(1,2))
    if iRotAuge1LP[0] > 0 and mLuck[0] in iRotAuge1Luck:
        time.sleep(0.5)
        print("A red-eyed is attacking you!")
        iRotAuge1Luck.remove(1)
        time.sleep(1)
        kampfRotAuge1(environment)
    elif mLuck[0] in iRotAuge1Luck:
        iRotAuge1Luck.remove(1)
        time.sleep(0.5)
        print("On one wall you will see a map of the area on this floor.")
        print("Continuing straight ahead, another staircase leads further up to the main control center.")
        time.sleep(5)
        mannschaftsquartiereFlur1(environment)
    else:
        time.sleep(0.5)
        iRotAuge1Luck.remove(2)
        print("On one wall you will see a map of the area on this floor.")
        print("Continuing straight ahead, another staircase leads further up to the main control center.")
        time.sleep(5)
        mannschaftsquartiereFlur1(environment)

def mannschaftsquartiereFlur1(environment):
    time.sleep(0.5)
    print("\nCurrent position: Corridor of the crew quarters")
    time.sleep(0.5)
    print("(1) go towards main control center")
    time.sleep(0.5)
    print("(2) go to the prison wing")
    time.sleep(0.5)
    print("( ) other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'look', 'look around', 'use water dispenser', 'use dispenser', 'examine water dispenser', 'examine dispenser']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You continue towards the main control center.")
        time.sleep(0.5)
        print("You stroll further along the corridor and go through a door that leads you into the next room.")
        time.sleep(2)
        print("You enter another corridor, two closed doors on the right and two on the left are in this corridor.")
        time.sleep(0.5)
        print("The following letters are engraved on the doors: A, B, C, D.")
        time.sleep(0.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You go back into the stairwell.")
        time.sleep(0.5)
        treppenhausGZ(environment)
    
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You look around, but discover nothing of interest except the way back to the stairwell,")
        print("the door that takes you further towards the main centre and a WATER DISPENSER.")
        mannschaftsquartiereFlur1(environment)
        
    elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
        time.sleep(0.5)
        print("As you approach the water dispenser, a stream of water comes out.")
        time.sleep(1.5)
        print("You are a little worried because the colour of the water has a red undertone.")
        time.sleep(1.5)
        mannschaftsquartiereFlur1(environment)
        
    elif cmd == 'use dispenser' or cmd == 'use water dispenser':
        time.sleep(0.5)
        print("You drink the water from the dispenser.")
        time.sleep(2)
        print("Something about this water tastes odd...")
        time.sleep(2.5)
        print("You feel strangely light-headed and your eyes start to itch...")
        time.sleep(3)
        print("You lose control of your body and your eyes go black...")
        time.sleep(7)
        exit()
        
def mannschaftsquartiereFlur2(environment):
    time.sleep(0.5)
    print("\nCurrent position: Corridor of the crew quarters")
    time.sleep(0.5)
    print("(1) go towards the main control center")
    time.sleep(0.5)
    print("(2) walk towards the prisoner wing")
    time.sleep(0.5)
    print("() other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', 
               '2', 
               'look',
               'look around',
               'open door a', 
               'open door b', 
               'open door c', 
               'open door d', 
               'use water dispenser',
               'use dispenser',
               'examine water dispenser',
               'examine dispenser'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You continue in the direction of the main control center.")
        time.sleep(1.5)
        print("You continue along the corridor and go through the next door into the next room.")
        iRotAuge2Luck.append(randint(1,2))
        if iRotAuge2LP[0] > 0 and mLuck[0] in iRotAuge2Luck:
            time.sleep(0.5)
            print("A red-eyed is attacking you!")
            iRotAuge2Luck.remove(1)
            time.sleep(1.5)
            kampfRotAuge2(environment)
        elif mLuck[0] in iRotAuge2Luck:
            iRotAuge2Luck.remove(1)
            time.sleep(0.5)
            print("Another hallway, two closed doors on the right and two on the left.")
            time.sleep(2)
            print("Letters are engraved on the doors: E, F, G, H.")
            time.sleep(2)
            mannschaftsquartiereFlur3(environment)
        else:
            iRotAuge2Luck.remove(2)
            time.sleep(0.5)
            print("Another hallway, two closed doors on the right and two on the left.")
            time.sleep(2)
            print("Letters are engraved on the doors: E, F, G, H.")
            time.sleep(2)
            mannschaftsquartiereFlur3(environment)
            
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You go towards the prison wing.")
        time.sleep(1)
        print("You walk along the corridor and go through the door into the next room.")
        time.sleep(2)
        mannschaftsquartiereFlur1(environment)
    
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You can see the following DOORs:")
        time.sleep(1)
        print("DOOR A")
        time.sleep(0.5)
        print("DOOR B")
        time.sleep(0.5)
        print("DOOR C")
        time.sleep(0.5)
        print("DOOR D")
        time.sleep(0.5)
        print("How about trying to OPEN one of them?")
        time.sleep(0.5)
        print("You also see a WATER DISPENDER.")
        time.sleep(2)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'open door a':
        time.sleep(0.5)
        print("This door is locked.")
        time.sleep(0.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'open door b':
        time.sleep(0.5)
        print("This door opens.")
        time.sleep(0.5)
        if medikit1[0] == 'Unbenutzt':
            time.sleep(0.5)
            print("You find a medikit and use it to treat your wounds.")
            time.sleep(3)
            mLP[0] = mLP[0] + 15
            medikit1.remove('Unbenutzt')
            medikit1.append('Benutzt')
            print("That's all you find.")
            time.sleep(1)
            print("There is nothing else of importance in this room and you leave.")
            time.sleep(1.5)
            mannschaftsquartiereFlur2(environment)
        else:
            time.sleep(0.5)
            print("A used medikit is lying on the floor...")
            time.sleep(0.5)
            print("There is nothing else of importance in this room and you leave.")
            time.sleep(1.5)
            mannschaftsquartiereFlur2(environment)
    
    elif cmd == 'open door c':
        if iKleineRüstung[0] == 'Besitz':
            time.sleep(0.5)
            print("You have already searched this room and taken the clothes with you.")
            time.sleep(1)
            mannschaftsquartiereFlur2(environment)
        elif iKleineRüstung[0] == 'Dame':
            time.sleep(0.5)
            print("You have already searched this room and taken the clothes with you.")
            time.sleep(1)
            mannschaftsquartiereFlur2(environment)
        else:
            time.sleep(0.5)
            print("This door opens.")
            time.sleep(1)
            print("There are clothes on a bed that would offer good protection,")
            time.sleep(1)
            print("but you are too big to put them on.")
            time.sleep(1)
            print("(1) take the clothes with you and leave the room")
            time.sleep(0.5)
            print("(2) leave the room without clothes")
            time.sleep(0.5)
            
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("You take the clothes with you.")
                iKleineRüstung.remove('Raum')
                iKleineRüstung.append('Besitz')
                time.sleep(0.5)
                print("You leave the room.")
                time.sleep(0.5)
                mannschaftsquartiereFlur2(environment)
                
            elif cmd == '2':
                time.sleep(0.5)
                print("You leave them.")
                time.sleep(0.5)
                print("You leave the room.")
                time.sleep(0.5)
                mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'open door d':
        time.sleep(0.5)
        print("This door is closed.")
        time.sleep(1.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
        time.sleep(0.5)
        print("As you approach the water dispenser, a stream of water comes out.")
        time.sleep(1.5)
        print("You are a little worried because the colour of the water has a red undertone.")
        time.sleep(1.5)
        mannschaftsquartiereFlur2(environment)
        
    elif cmd == 'use dispenser' or cmd == 'use water dispenser':
        time.sleep(0.5)
        print("You drink the water from the dispenser.")
        time.sleep(2)
        print("Something about this water tastes odd...")
        time.sleep(2.5)
        print("You feel strangely light-headed and your eyes start to itch...")
        time.sleep(3)
        print("You lose control of your body and your eyes go black...")
        time.sleep(7)
        exit()
        
def mannschaftsquartiereFlur3(environment):
    time.sleep(0.5)
    print("\nCurrent position: Corridor of the crew quarters")
    time.sleep(0.5)
    print("(1) go towards the main control center")
    time.sleep(0.5)
    print("(2) go towards the prisoner wing")
    time.sleep(0.5)
    print("() other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', 
               '2', 
               'look around',
               'look',
               'open door e', 
               'open door f', 
               'open door g', 
               'open door h', 
               'use water dispenser',
               'use dispenser',
               'examine water dispenser',
               'examine dispenser'
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You continue towards the main control center.")
        time.sleep(1.5)
        print("The next door takes you into a stairwell.")
        time.sleep(1.5)
        print("There is a map of the building on the wall.")
        print("You can see that it continues upwards to the main control center.")
        time.sleep(3)
        treppenhausHZ(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You go towards the prison wing.")
        time.sleep(1)
        print("You walk along the corridor and go through the door into the next room.")
        time.sleep(3)
        print("You are in the room with the following doors: A, B, C, D.")
        time.sleep(2.5)
        mannschaftsquartiereFlur2(environment)
    
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You see the following doors:")
        time.sleep(0.5)
        print("DOOR E")
        time.sleep(0.5)
        print("DOOR F")
        time.sleep(0.5)
        print("DOOR G")
        time.sleep(0.5)
        print("DOOR H")
        time.sleep(0.5)
        print("How about trying to OPEN one of them?")
        time.sleep(0.5)
        print("You also see a WATER DISPENDER.")
        time.sleep(2)
        mannschaftsquartiereFlur3(environment)
        
    elif cmd == 'open door e':
        time.sleep(0.5)
        print("This door opens.")
        time.sleep(1.5)
        print("You hear a crackling sound...")
        time.sleep(1.5)
        iRotAuge3Luck.append(randint(1,2))
        if iRotAuge3LP[0] > 0 and mLuck[0] in iRotAuge3Luck:
            time.sleep(0.5)
            print("...and a red-eyed attacks you!")
            iRotAuge3Luck.remove(1)
            time.sleep(2.5)
            kampfRotAuge3(environment)
        elif mLuck[0] in iRotAuge3Luck:
            iRotAuge3Luck.remove(1)
            time.sleep(0.5)
            if mStoffKuscheltier[0] == 'Meins':
                time.sleep(1)
                print("You must have imagined that...")
                time.sleep(1.5)
                print("There is accommodation for six people in this room.")
                time.sleep(1.5)
                print("And nobody has left anything useful here...")
                print("You leave the room.")
                time.sleep(2.5)
                mannschaftsquartiereFlur3(environment)
            elif mStoffKuscheltier[0] == 'Rotauge':
                time.sleep(1)
                print("You walk into the room and see a blood-stained stuffed animal.")
                time.sleep(1)
                print("It looks like a monkey.")
                time.sleep(3)
                print("You can't help yourself and take him in your arms.")
                mStoffKuscheltier.remove('Rotauge')
                mStoffKuscheltier.append('Meins')
                time.sleep(2)
                print("You leave the room.")
                time.sleep(1)
                mannschaftsquartiereFlur3(environment)
        else:
            iRotAuge3Luck.remove(2)
            time.sleep(1)
            print("You must have imagined that...")
            time.sleep(1.5)
            print("There is accommodation for six people in this room.")
            time.sleep(1.5)
            print("And nobody has left anything useful here...")
            print("You leave the room.")
            time.sleep(3)
            mannschaftsquartiereFlur3(environment)    
        
    elif cmd == 'open door f':
        time.sleep(0.5)
        print("This door is closed.")
        time.sleep(1.5)
        mannschaftsquartiereFlur3(environment)
    
    elif cmd == 'open door g':
        time.sleep(0.5)
        print("This door is closed.")
        time.sleep(1.5)
        mannschaftsquartiereFlur3(environment)
    
    elif cmd == 'open door h':
        time.sleep(0.5)
        if iTürHPasswort[0] != 'Izzin':
            time.sleep(0.5)
            print("This door cannot be opened.")
            time.sleep(1)
            print("You see that the door control unit is password protected.")
            time.sleep(1)
            print("If only you knew the password...")
            time.sleep(1)
            mannschaftsquartiereFlur3(environment)
        else:
            time.sleep(0.5)
            print("This door cannot be opened.")
            time.sleep(1)
            print("You can see that the door control unit is password protected.")
            time.sleep(1)
            print("You remember the note in the machine deck.")
            time.sleep(1)
            print("''92517''")
            time.sleep(2)
            print("PING")
            time.sleep(0.5)
            print("...")
            time.sleep(0.5)
            print("The door opens and you walk in.")
            time.sleep(1)
            raumH(environment)
            
    elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
        time.sleep(0.5)
        print("As you approach the water dispenser, a stream of water comes out.")
        time.sleep(1.5)
        print("You are a little worried because the colour of the water has a red undertone.")
        time.sleep(1.5)
        mannschaftsquartiereFlur3(environment)
        
    elif cmd == 'use dispenser' or cmd == 'use water dispenser':
        time.sleep(0.5)
        print("You drink the water from the dispenser.")
        time.sleep(2)
        print("Something about this water tastes odd...")
        time.sleep(2.5)
        print("You feel strangely light-headed and your eyes start to itch...")
        time.sleep(3)
        print("You lose control of your body and your eyes go black...")
        time.sleep(7)
        exit()

#############################
            
def raumH(environment):
    time.sleep(0.5)
    print("\nYou are in room H.")
    time.sleep(0.5)
    print("(1) leave")
    time.sleep(0.5)
    print("( ) other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', 
               'look around',
               'look',
               'open locker', 
               'open lockers',
               'examine lockers',
               'examine lockers',
               'examine bed', 
               'examine beds', 
               'open medicine cabinet',
               'open boxes',
               'open box',
               'examine boxes',
               'examine box',
               'examine bedside table',
               'examine bedside tables',
               'open bedside table',
               'open bedside tables',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("You leave the room.")
        mannschaftsquartiereFlur3(environment)
    
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around the room.")
        time.sleep(0.5)
        print("The room contains:")
        time.sleep(0.5)
        print("four LOCKERS,")
        time.sleep(0.5)
        print("some CRATES,")
        time.sleep(0.5)
        print("some BEDS,")
        time.sleep(0.5)
        print("a MEDICINE CABINET")
        time.sleep(0.5)
        print("and some BEDSIDE TABLES")
        time.sleep(0.5)
        raumH(environment)
        
    elif cmd == 'open locker' or cmd == 'open lockers' or cmd == 'examine lockers' or cmd == 'examine locker':
        if 'Jonas Laserkanone' in mAus or 'Jonas Laserkanone' in mG2:
            time.sleep(0.5)
            print("The locker is empty.")
            time.sleep(1)
            raumH(environment) 
        elif mW[0] != 'Faust':
            time.sleep(0.5)
            print("You open the lockers and find a laser cannon inside.")
            time.sleep(2)
            print("However, you already have a weapon equipped.")
            time.sleep(1.5)
            print("Put down the weapon to equip a new one.")
            time.sleep(1.5)
            raumH(environment)
        else:    
            time.sleep(0.5)
            print("You open the lockers and find a laser cannon inside.")
            time.sleep(2)
            print("(1) take laser cannon")
            time.sleep(1.5)
            print("(2) don't touch the laser cannon")
            time.sleep(1.5)
        
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("You take the laser cannon.")
                time.sleep(1.5)
                print("'Izzy' is engraved on the barrel.")
                print("'Thx Izzy'")
                mW.remove('Faust')
                mW.append('Jonas Laserkanone')
                mHP.remove(3)
                mHP.append(10)
                time.sleep(1.5)
                raumH(environment)
            
            elif cmd == '2':
                time.sleep(0.5)
                print("You better leave the laser cannon where it is.") 
                time.sleep(1)
                raumH(environment)
        
    elif cmd == 'examine bed' or cmd == 'examine beds':
        time.sleep(0.5)
        print("You check the beds.")
        time.sleep(1)
        print("As you pick up a pillow, you discover a note.")
        time.sleep(0.5)
        print("(1) read note")
        time.sleep(0.5)
        print("(2) put note back")
        time.sleep(0.5)

#################################################################################################################
                
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("You decide to read the note.")
            time.sleep(1.5)
            print("\n'Recording 42-01_028")
            print(" ")
            print(" Mex and I got on the ship with virtually no problems. So the biggest")
            print(" issue of the whole endeavour is behind us. Now we just have to find Izzin,")
            print(" cause chaos and escape from this ship.")
            print(" Everything is planned and the plan is foolproof.")
            print(" ")
            print(" ")
            print(" Recording 54-01_283")
            print(" ")
            print(" The transfer worked like a charm! We've been trying to move one of us to the prisoner")
            print(" wing for almost a fortnight, but there is a lot of competition down here. It's hard to")
            print(" believe how many technicians want to be moved away from the engine room.") 
            print(" I wasn't transferred, but promoted because nobody else dared to touch this critter but me!!")
            print(" I'm now in the most comfortable crew quarters and have a locker where I can finally hide my")
            print(" Izzy. Mex persuaded the overseer to move him to the prisoner wing. Now he can look around")
            print(" and report back. When we're out here, I'll introduce you to him, he's a really nice lad.")
            print(" ")
            print(" Recording 57-01_739")
            print(" ")
            print(" Today is the day.")
            print(" We will start the operation after breakfast. I'll cause confusion in the engine room")
            print(" by pulling a few plugs in the generator room and cutting the power supply. To buy myself")
            print(" some time, I'll release the critter in the engine room. It's risky, but I'll get out of")
            print(" there somehow. Mex is going to dump this red substance into the water supply that I scammed")
            print(" from that weirdo on Vega 7. That'll paralyse the crew for a while. When the power supply")
            print(" is cut, Mex will open your cryo chamber in the prisoner wing and get you out of there.")
            print(" I told him to open another one to draw the attention away from us.")
            print(" As I said, the plan is foolproof! Soon we will be reunited my Izzin. We will then disappear")
            print(" with the escape pod in the prisoner wing as soon as the power supply is restored.")
            print(" The lights are switching on.")
            print(" I have to go.")
            print(" ")
            time.sleep(10)
            print("After you have read the note, you put it back.")
            time.sleep(0.5)
            raumH(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("You put the note back.")
            time.sleep(0.5)
            raumH(environment)
        
    elif cmd == 'open medicine cabinet':
        time.sleep(0.5)
        if iKleineRüstung[0] == 'Dame':
            if 'Monsterhunter' in mAus or 'Monsterhunter' in mG6:
                time.sleep(0.5)
                print("The medicine cabinet is empty.")
                time.sleep(1)
                raumH(environment) 
            elif mW[0] != 'Faust':
                time.sleep(0.5)
                print("You open the medicine cabinet and inside is a huge gun.")
                time.sleep(1.5)
                print("It says 'Monsterhunter' on the overdimensional gun.")
                time.sleep(1.5)
                print("However, you already have a weapon in your hand.")
                time.sleep(1.5)
                print("Put down the equipped weapon first to equip a new one.")
                time.sleep(1.5)
                raumH(environment)
            else:    
                time.sleep(0.5)
                print("You open the medicine cabinet and inside is a huge gun.")
                time.sleep(1.5)
                print("It says 'Monsterhunter' on the overdimensional gun.")
                time.sleep(1.5)
                print("(1) take Monsterhunter")
                time.sleep(1.5)
                print("(2) leave Monsterhunter behind")
                time.sleep(1.5)
            
                cmdlist = ['1', '2']
                cmd = getcmd(cmdlist)
                
                if cmd == '1':
                    time.sleep(0.5)
                    print("You take Monsterhunter.")
                    time.sleep(1.5)
                    print("Thanks Edith")
                    mW.remove('Faust')
                    mW.append('Monsterhunter')
                    mHP.remove(3)
                    mHP.append(30)
                    time.sleep(1.5)
                    raumH(environment)
                
                elif cmd == '2':
                    time.sleep(0.5)
                    print("You'd rather leave the Monsterhunter behind.") 
                    time.sleep(1)
                    raumH(environment)
        
        else:
            time.sleep(0.5)
            print("The door is locked.")
            time.sleep(0.5)
            raumH(environment)
            
    elif cmd == 'examine bedside table' or cmd == 'examine bedside tables' or cmd == 'open bedside table' or cmd == 'open bedside tables':
        time.sleep(0.5)
        print("You examine all the bedside tables in this room,")
        print("but there is nothing useful in any of them.")
        time.sleep(2)
        raumH(environment)

    elif cmd == 'open crates' or cmd == 'open crate' or cmd == 'examine crates' or cmd == 'examine crate':
        time.sleep(0.5)
        print("You examine all the crates in this room,")
        print("but there is nothing useful in any of them.")
        time.sleep(2)
        raumH(environment)
            
def treppenhausHZ(environment):
    time.sleep(0.5)
    print("\nCurrent position: Stairwell crew quarters/main control center")
    time.sleep(0.5)
    print("(1) go in the direction of the main control center")
    time.sleep(0.5)
    print("(2) go towards the crew quarters")
    time.sleep(0.5)
    print("( ) other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'look', 'look around']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You go up the stairs and through the door.")
        if mLosungswort[0]=='Dystopia':
            time.sleep(0.5)
            hauptzentraleFlur(environment)
        elif iWulffLP[0] <= 0:
            time.sleep(0.5)
            hauptzentraleFlurNachKampf(environment)
        else:
            time.sleep(0.5)
            print("The first thing you see is an older man pointing a gun at you.")
            time.sleep(2.5)
            print("...")
            time.sleep(0.5)
            print("''Not again''")
            time.sleep(0.5)
            print("...")
            time.sleep(2)
            begegnungMitWulff(environment)
    
    elif cmd == '2':
        time.sleep(0.5)
        print("You walk towards the prisoner wing.")
        time.sleep(1)
        print("You walk along the corridor and go through the door into the next room.")
        time.sleep(2.5)
        print("You are in the room with the following doors: E, F, G, H.")
        time.sleep(2)
        mannschaftsquartiereFlur3(environment)
        
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        print("However, there is nothing interesting to discover in this stairwell.")
        time.sleep(1)
        treppenhausHZ(environment)
        
def begegnungMitWulff(environment):
    if mLippeAb[0] == 'Abgebissen':
        time.sleep(0.5)
        print("\n'So it is you who killed the father of the honourable ones,' says the old man")
        time.sleep(2.5)
        print("and fires his gun at you without hesitation.")
        mLP[0] = mLP[0] - 6
        time.sleep(2)
        kampfWulff(environment)
        
    else:
        time.sleep(0.5)
        wulffGespräch(environment)
        
def hauptzentraleFlur(environment):
    time.sleep(0.5)
    print("\nWulff gives you a nod")
    time.sleep(2)
    print("Current position: Hallway")
    time.sleep(0.5)
    print("(1) go towards the crew quarters")
    time.sleep(0.5)
    print("(2) Go towards the main control center")
    time.sleep(0.5)
    print("()  other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'look', 'look around']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You go towards the crew quarters.")
        time.sleep(0.5)
        treppenhausHZ(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You go towards the main control center.")
        time.sleep(0.5)
        hauptzentrale(environment)
        
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        time.sleep(0.5)
        print("There seems to be nothing here except WULFF.")
        time.sleep(0.7)
        hauptzentraleFlur(environment)
        
    elif cmd == 'talk to wulff':
        time.sleep(0.5)
        print("You go to Wulff.")
        time.sleep(0.5)
        print("'Ah, it's you.")
        time.sleep(0.7)
        print(" ...")
        time.sleep(1.2)
        print(" ...'")
        time.sleep(1.8)
        print("...")
        time.sleep(1)
        print("You walk away without saying anything.")
        time.sleep(0.5)
        hauptzentraleFlur(environment)
        
def hauptzentraleFlurNachKampf(environment):
    time.sleep(0.5)
    print("\nWulff lies dead on the floor.")
    time.sleep(2)
    print("Current position: Hallway")
    time.sleep(0.5)
    print("(1) go towards the crew quarters")
    time.sleep(0.5)
    print("(2) Go towards the main control center")
    time.sleep(0.5)
    print("()  other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', 'look', 'look around', 'examine wulff']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You go towards the crew quarters.")
        time.sleep(0.5)
        treppenhausHZ(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("You go towards the main control center.")
        time.sleep(0.5)
        hauptzentrale(environment)
        
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        time.sleep(0.5)
        print("There doesn't seem to be anything interesting in this corridor,")
        print("except for the dead WULFF on the floor.")
        time.sleep(2)
        hauptzentraleFlurNachKampf(environment)
        
    elif cmd == 'examine wulff':
        time.sleep(0.5)
        print("When you examine Wulff's body, you find an arrowhead")
        print("in one of his pockets. You'd better leave it where you found it.")
        time.sleep(3)
        hauptzentraleFlurNachKampf(environment)
    #######################################################################################################
def hauptzentrale(environment):
    time.sleep(0.5)
    print("\nCurrent position: Main control center")
    time.sleep(0.5)
    print("(1) Go towards the crew quarters")
    time.sleep(0.5)
    print("(2) Go towards the armoury")
    time.sleep(0.5)
    print("(3) Go towards the lab")
    time.sleep(0.5)
    print("(4) Go towards the medical department")
    time.sleep(0.5)
    print("()  other commands")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', '3', '4', 'look', 'look around', 'talk to woman', 'talk to merana', 'go to woman', 'go to merana', 'open crate', 'open chest',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("You enter the corridor in the direction of the stairwell")
        time.sleep(0.5)
        if mLosungswort[0]=='Dystopia':
            hauptzentraleFlur(environment)
        elif iWulffLP[0] <= 0:
            hauptzentraleFlurNachKampf(environment)
        else:
            hauptzentraleFlur(environment)
            
            
    elif cmd == '2':
        time.sleep(0.5)
        print("You head towards the armoury")
        time.sleep(1)
        waffenkammerFlur(environment)
        
    elif cmd == '3':
        time.sleep(0.5)
        print("You head towards the lab")
        time.sleep(1)
        laborFlur(environment)
        
    elif cmd == '4':
        time.sleep(0.5)
        print("You head in the direction of the medical department")
        time.sleep(1)
        medAbteilungFlur(environment)
    
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        time.sleep(1)
        print("Apart from the imposing interior of the main centre, there is very little going on here.")
        time.sleep(2)
        print("The two guards are standing near the woman, but the one who was talking to you")
        print("is trying hard not to look in your direction.")
        time.sleep(4)
        print("The WOMAN sits quietly in her chair with her eyes closed.")
        time.sleep(2)
        print("Four paths lead from the main centre in four different directions.")
        time.sleep(2)
        hauptzentrale(environment)
        
    elif cmd == 'talk to woman' or cmd == 'talk to merana' or cmd == 'go to merana' or cmd == 'talk to merana':
        time.sleep(0.5)
        print("You walk past the two guards to the woman in the captain's seat. ")
        print("She is wearing an elegant grey-green robe, opens her eyes and looks at you calmly.")
        time.sleep(5)
        gesprächMerana(environment)
        
    elif cmd == 'open chest' or cmd == 'open crate':
        time.sleep(0.5)
        if iNarrezMerana[0] == 'Wissend':
            time.sleep(0.5)
            print("You unlock the chest with the key.")
            time.sleep(1)
            print("Inside is a huge diamond!!!")
            time.sleep(2)
            print("...")
            time.sleep(1)
            print("It's too heavy to take with you.")
            time.sleep(1.5)
            print("You lock the chest again.")
            time.sleep(1)
            hauptzentrale(environment)
        else:
            time.sleep(0.5)
            print("The chest is locked.")
            time.sleep(1.4)
            hauptzentrale(environment)
             
def waffenkammerFlur(environment):
    
    if iRotAuge4LP[0] <= 0:
        time.sleep(0.5)
        print("\nCurrent position: Corridor towards the armoury")
        time.sleep(0.5)
        print("(1) go towards the main centre")
        time.sleep(0.5)
        print("(2) go towards the armoury")
        time.sleep(0.5)
        print("()  other commands")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', 'look around', 'look', 'examine water dispenser', 'use water dispenser', 'use dispenser', 'examine dispenser']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("You head towards the main centre.")
            time.sleep(1)
            hauptzentrale(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("You head towards the armoury.")
            time.sleep(1)
            waffenkammer(environment)
            
        elif cmd == 'look' or cmd == 'look around':
            time.sleep(0.5)
            print("You take a look arounf")
            time.sleed
            print("A WATER DISPENSER is attached to the right-hand wall.")
            print("Apart from that, there doesn't seem to be anything conspicuous here.")
            time.sleep(2.5)
            waffenkammerFlur(environment)
            
        elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
            time.sleep(0.5)
            print("As you approach the water dispenser, a stream of water comes out.")
            time.sleep(1.5)
            print("You are a little worried because the colour of the water has a red undertone.")
            time.sleep(1.5)
            waffenkammerFlur(environment)
            
            
        elif cmd == 'use dispenser' or cmd == 'use water dispenser':
            time.sleep(0.5)
            print("You drink the water from the dispenser.")
            time.sleep(2)
            print("Something about this water tastes odd...")
            time.sleep(2.5)
            print("You feel strangely light-headed and your eyes start to itch...")
            time.sleep(3)
            print("You lose control of your body and your eyes go black...")
            time.sleep(7)
            exit()

            
    
    elif iRotAuge4LP[0] > 0:
        time.sleep(0.5)
        print("\nAs you enter the room, a red-eyed attacks you!")
        time.sleep(0.5)
        kampfRotAuge4(environment)
        
        
def waffenkammer(environment):
    if 'Jonas Laserkanone' in mW and iBewFrau[0] == 'Aggressiv':
        print("\nDu betritts die Waffenkammer.")
        time.sleep(0.5)
        print("A woman armed to the teeth approaches you.")
        time.sleep(1.5)
        print("'Hey, what are you lookin...'")
        time.sleep(0.8)
        print("'...'")
        time.sleep(1.8)
        print("She looks at your laser pistol.")
        time.sleep(0.8)
        print("'Where did you get that?! It belonged to Jona!'")
        time.sleep(1)
        print("You tell her that you've found the laser cannon in a locker belonging to Jona")
        time.sleep(2.5)
        print("You also tell her that his chances of survival are relatively low.")
        time.sleep(1.5)
        print("When you tell her the story, her eyes glaze over and tears stream down her face.")
        time.sleep(2)
        print("Deep compassion takes hold of you.")
        time.sleep(0.5)
        print("You give her Jona's laser gun.")
        mW.remove('Jonas Laserkanone')
        mW.append('Faust')
        mG2.append('Jonas Laserkanone')
        mHP.remove(10)
        mHP.append(3)
        time.sleep(3)
        print("'Thank you...' says the woman, wiping the tears from her face with a sleeve.")
        time.sleep(2.5)
        print("'I'm leaving here now, you can take what you want.")
        time.sleep(2)
        print(" And again, thank you.'")
        iBewFrau.remove('Aggressiv')
        iBewFrau.append('Traurig')
        time.sleep(1.2)
        print("The woman gives you an exhausted smile and steps out of the armoury.")
        time.sleep(2)
        waffenkammer(environment)
    elif iBewFrau[0] == 'Aggressiv':
        time.sleep(0.5)
        print("\nYou enter the armoury.")
        time.sleep(1)
        print("A loud bang can be heard!")
        time.sleep(0.7)
        print("...")
        time.sleep(0.5)
        print("A shot just missed your head.")
        time.sleep(1)
        print("you hear a voice")
        time.sleep(1)
        print("'One step closer and you're a head shorter!'")
        time.sleep(1.5)
        print("(1) take a step closer")
        time.sleep(0.5)
        print("(2) go back to the corridor")
        time.sleep(0.5)
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("You are taking another step forwards.")
            time.sleep(1)
            print("Unfortunately, the voice was right.")
            time.sleep(1)
            print("You can't go any further with a shortened head, so you stay down and are dead.")
            time.sleep(7)
            exit()
        
        elif cmd == '2':
            time.sleep(0.5)
            print("You take flight as quickly as possible.")
            time.sleep(1)
            waffenkammerFlur(environment)
        
        
    else:    
        time.sleep(0.5)
        print("\nCurrent position: Armoury")
        time.sleep(0.5)
        print("(1) go towards the main control center")
        time.sleep(0.5)
        print("( ) other commands")
        time.sleep(0.5)
    
        cmdlist = ['1', 'look around', 'look', 'open locker']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("You head towards the main control center.")
            time.sleep(0.5)
            waffenkammerFlur(environment)
        
        elif cmd == 'look' or cmd == 'look around':
            time.sleep(0.5)
            print("You take a look around.")
            time.sleep(0.5)
            print("The armoury has been completely looted!")
            time.sleep(2)
            print("'The way the woman was equipped earlier, she must have taken everything with her...'")
            time.sleep(1.5)
            print("A LOCKER in the room seems to contain something useful.")
            time.sleep(1.5)
            waffenkammer(environment)
            
        elif cmd == 'open locker':
            if 'Monsterjäger' in mAus or 'Monsterjäger' in mG8:
                time.sleep(0.5)
                print("The locker is empty.")
                time.sleep(1.5)
                waffenkammer(environment)  
            elif mAus[0] != 'Unterhose':
                time.sleep(0.5)
                print("You open the locker and find a monster hunter's armour inside.")
                time.sleep(2)
                print("However, you are already wearing clothes and cannot put on the armour.")
                time.sleep(2.5)
                print("Take off your clothes before you put on something new.")
                time.sleep(2)
                waffenkammer(environment)
            else:    
                time.sleep(0.5)
                print("You open the locker and find a monster hunter's armour inside.")
                time.sleep(2)
                print("(1) Put on armour")
                time.sleep(0.5)
                print("(2) Leave armour behind")
                time.sleep(0.5)
            
                cmdlist = ['1', '2']
                cmd = getcmd(cmdlist)
                
                if cmd == '1':
                    time.sleep(0.5)
                    print("You put on the armour.")
                    time.sleep(1.5)
                    print("Now you're ready for a monster hunt, at least as far as looks are concerned.")
                    mAus.remove('Unterhose')
                    mAus.append('Monsterjäger')
                    mS.remove(1)
                    mS.append(13)
                    time.sleep(2)
                    time.sleep(2.5)
                    waffenkammer(environment)      
                    
                elif cmd == '2':
                    time.sleep(0.5)
                    print("You'd better leave the armour behind.") 
                    time.sleep(1)
                    waffenkammer(environment)
            
def laborFlur(environment):
    
    if iRotAuge5LP[0] <= 0:
        time.sleep(0.5)
        print("\nCurrent position: Hallway")
        time.sleep(0.5)
        print("(1) Go towards the main control center")
        time.sleep(0.5)
        print("(2) Go towards the lab")
        time.sleep(0.5)
        print("() other commands")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', 'look', 'lok around', 'open chest', 'open crate', 'examine water dispenser', 'use water dispenser', 'use dispenser', 'examine dispenser']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("You head towards the main control center.")
            time.sleep(0.5)
            hauptzentrale(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("You head towards the lab.")
            time.sleep(0.5)
            labor(environment)
            
        elif cmd == 'open chest' or cmd == 'open crate':
            if 'Laserschwert' in mAus or 'Laserschwert' in mG7:
                time.sleep(0.5)
                print("The chest is empty.")
                time.sleep(1)
                laborFlur(environment) 
            elif mW[0] != 'Faust':
                time.sleep(0.5)
                print("You open the chest and find an officer's sword inside.")
                time.sleep(2)
                print("However, you already have a weapon in your hand.")
                time.sleep(1.5)
                print("Discard the weapon to equip a new one.")
                time.sleep(1.5)
                laborFlur(environment)
            else:    
                time.sleep(0.5)
                print("You open the chest and find an officer's sword inside.")
                time.sleep(2)
                print("(1) take the sword")
                time.sleep(0.5)
                print("(2) leave the sword behind")
                time.sleep(0.5)
            
                cmdlist = ['1', '2']
                cmd = getcmd(cmdlist)
                
                if cmd == '1':
                    time.sleep(0.5)
                    print("You take the sword.")
                    time.sleep(1.5)
                    mW.remove('Faust')
                    mW.append('Laserschwert')
                    mHP.remove(3)
                    mHP.append(15)
                    time.sleep(1.5)
                    laborFlur(environment)
                
                elif cmd == '2':
                    time.sleep(0.5)
                    print("You'd better leave the sword behind.") 
                    time.sleep(1)
                    laborFlur(environment)
                
            
        elif cmd == 'look' or cmd == 'look around':
            time.sleep(0.5)
            print("You take a look around.")
            time.sleep(1)
            print("A WATER DISPENSER can be found on one side of the room.")
            time.sleep(1.5)
            print("There is a CHEST underneath.")
            time.sleep(1)
            laborFlur(environment)
            
        elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
            time.sleep(0.5)
            print("As you approach the water dispenser, a stream of water comes out.")
            time.sleep(1.5)
            print("You are a little worried because the colour of the water has a red undertone.")
            time.sleep(1.5)
            laborFlur(environment)
            
        elif cmd == 'use dispenser' or cmd == 'use water dispenser':
            time.sleep(0.5)
            print("You drink the water from the dispenser.")
            time.sleep(2)
            print("Something about this water tastes odd...")
            time.sleep(2.5)
            print("You feel strangely light-headed and your eyes start to itch...")
            time.sleep(3)
            print("You lose control of your body and your eyes go black...")
            time.sleep(7)
            exit()
    
    elif iRotAuge5LP[0] > 0:
        time.sleep(0.5)
        print("\nAs you enter the room, a red-eyed attacks you!")
        time.sleep(0.5)
        kampfRotAuge5(environment)
            
def labor(environment):
    if iVerProf[0] == 'Verrückt':
        time.sleep(0.5)
        print("\nAs you enter the lab, a man with long, dishevelled hair comes towards you.")
        time.sleep(2)
        print("He asks you: 'Have you got my Shnuffy with you?")
        time.sleep(1.5)
        if mStoffKuscheltier[0] == 'Rotauge':
            print("He looks at you expectantly, but after a few seconds he turns around")
            print("and runs in circles, tearing his hair.")
            time.sleep(3)
            print("As a precaution, you leave the room.")
            time.sleep(0.5)
            laborFlur(environment)
        else:
            print("'YOU HAVE FOUND MY SHNUFFY!!!")
            time.sleep(1.5)
            print(" Many thanks for that!")
            time.sleep(1)
            print(" If I can help you in any way, just let me know.'")
            iVerProf.remove('Verrückt')
            iVerProf.append('Schnuffi')
            time.sleep(2)
            labor(environment)
    else:
        time.sleep(0.5)
        print("\nCurrent position: Laboratory")
        time.sleep(0.5)
        print("(1) go towards the main control center")
        time.sleep(0.5)
        print("( ) other commands")
        time.sleep(0.5)
    
    cmdlist = ['1', 'look', 'look around','talk to man', 'talk to professor', 'open hatch', 'open locker',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("Go towards the main control center")
        time.sleep(0.5)
        laborFlur(environment)
        
    elif cmd == 'talk to man' or cmd == 'talk to professor':
        time.sleep(0.5)
        print("The man holds his stuffed animal in his hand and looks at you overjoyed.")
        time.sleep(2)    
        print("He asks you cheerfully: 'What do you want to know?'")
        time.sleep(1.5)
        gesprächProfessor(environment)
                
    elif cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around.")
        time.sleep(0.5)
        print("An old, battered LOCKER immediately catches your eye, otherwise there are stacks ")
        print("of boxes scattered around the room.")
        time.sleep(2.2)
        print("Otherwise, there are strange devices on many tables that you should rather not touch.")
        time.sleep(2.2)
        print("The old MAN is playing with his soft toy in a corner.")
        time.sleep(0.9)
        labor(environment)
        
    elif cmd == 'open locker':
        if 'Panzerung' in mAus or 'Panzerung' in mG5:
            time.sleep(0.5)
            print("The locker is empty.")
            time.sleep(1.5)
            labor(environment)  
        elif mAus[0] != 'Unterhose':
            time.sleep(0.5)
            print("You open the locker and find an armoured jumpsuit inside.")
            time.sleep(2)
            print("However, you are already wearing clothes and cannot put on the jumpsuit.")
            time.sleep(2.5)
            print("Take off your clothes before you put on something new.")
            time.sleep(2)
            labor(environment)
        else:    
            time.sleep(0.5)
            print("You open the locker and find an armoured jumpsuit inside.")
            time.sleep(2)
            print("(1) put on armoured jumpsuit")
            time.sleep(0.5)
            print("(2) leave the armoured jumpsuit behind")
            time.sleep(0.5)
        
            cmdlist = ['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(0.5)
                print("You put on the jumpsuit.")
                time.sleep(1.5)
                print("A little heavy, but you haven't felt this protected for a long time.")
                mAus.remove('Unterhose')
                mAus.append('Panzerung')
                mS.remove(1)
                mS.append(15)
                time.sleep(2)
                labor(environment)      
                
            elif cmd == '2':
                time.sleep(0.5)
                print("You'd better leave the armoured jumpsuit behind.") 
                time.sleep(1)
                labor(environment)
            
    elif cmd == 'open hatch':
        time.sleep(0.5)
        print("\nYou push aside a crate and there is a hatch underneath.")
        time.sleep(2)
        print("You open it and climb down a ladder.")
        time.sleep(1.5)
        print("Once at the bottom, you open another hatch.")
        time.sleep(1.3)
        print("You jump out and the door closes.")
        time.sleep(1.2)
        print("You try to open the hatch from this side, but without success.")
        time.sleep(1.4)
        generatorraum(environment)
    
def medAbteilungFlur(environment):
    
    if iRotAuge6LP[0] <= 0:
        time.sleep(0.5)
        print("\nCurrent position: Hallway")
        time.sleep(0.5)
        print("(1) go towards the main control center")
        time.sleep(0.5)
        print("(2) Go towards the medical department")
        time.sleep(0.5)
        print("()  other commands")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', 'look', 'look around', 'examine water dispenser', 'use water dispenser', 'use dispenser', 'examine dispenser']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            print("You head towards the main control center.")
            hauptzentrale(environment)
            
        elif cmd == '2':
            print("You head towards the medical department.")
            medAbteilung(environment)
            
        elif cmd == 'look' or cmd == 'look around':
            print("You take a look around.")
            print("There's a camera hanging in front of the medical department.")
            print("There is also a WATER DISPENSER here.")
            medAbteilungFlur(environment)
            
        elif cmd == 'examine water dispenser' or cmd == 'examine dispenser':
            time.sleep(0.5)
            print("As you approach the water dispenser, a stream of water comes out.")
            time.sleep(1.5)
            print("You are a little worried because the colour of the water has a red undertone.")
            time.sleep(1.5)
            medAbteilungFlur(environment)
            
        elif cmd == 'use dispenser' or cmd == 'use water dispenser':
            time.sleep(0.5)
            print("You drink the water from the dispenser.")
            time.sleep(2)
            print("Something about this water tastes odd...")
            time.sleep(2.5)
            print("You feel strangely light-headed and your eyes start to itch...")
            time.sleep(3)
            print("You lose control of your body and your eyes go black...")
            time.sleep(7)
            exit()
    
    elif iRotAuge6LP[0] > 0:
        time.sleep(0.5)
        print("\nAs you enter the room, a red-eyed attacks you!")
        time.sleep(0.5)
        kampfRotAuge6(environment)
                
def medAbteilung(environment):
    if 'Jonas Laserkanone' in mW and iMedAbtEingang[0] == 'Verschlossen':
        time.sleep(0.5)
        print("\nA camera in front of the entrance is focussed on you.")
        time.sleep(1)
        print("''Who are you?' drones from the intercom under the camera.")
        time.sleep(1.5)
        print("'Uuuhh, what have you got there?")
        time.sleep(1)
        print(" If you let me have your firearm, I'll let you in.")
        time.sleep(1.5)
        print(" I could treat your wounds too")
        time.sleep(1.5)
        print(" What do you think?")
        time.sleep(0.9)
        print("(1) Agree")
        time.sleep(0.5)
        print("(2) Decline")
        time.sleep(0.5)
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("'Very well, I'll open the door.")
            time.sleep(1)
            print("The door opens and an elderly lady steps out.")
            iMedAbtEingang.remove('Verschlossen')
            iMedAbtEingang.append('Geöffnet')
            time.sleep(2)
            print("'That's nice of you, very nice.")
            time.sleep(1.8)
            print("You give her your weapon.")
            time.sleep(1)
            mW.remove('Jonas Laserkanone')
            mW.append('Faust')
            mG2.append('Jonas Laserkanone')
            mHP.remove(10)
            mHP.append(3)
            time.sleep(1)
            print("'What has happened to you?")
            time.sleep(1)
            print(" You look as if a spaceship has hit you!")
            time.sleep(1.5)
            print(" Let me tend to your wounds for a moment...")
            time.sleep(1)
            print("...")
            time.sleep(0.5)
            time.sleep(0.5)
            mLP[0] = mLP[0] - mLP[0] + 100
            print(" That's all.")
            time.sleep(0.5)
            print(" If you come back here again with clothes that offer better protection than mine,")
            time.sleep(2.5)
            print(" I'll give you something in return. My name is Edith, by the way.'")
            time.sleep(2.5)
            print("The old lady walks through the door again.")
            time.sleep(1)
            print("You're following her.")
            time.sleep(0.9)
            medAbteilung(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("'Then please leave, if you would be so kind.'")
            time.sleep(2)
            print("You leave.")
            time.sleep(0.5)
            medAbteilungFlur(environment)
      
    elif iMedAbtEingang[0] == 'Verschlossen':
        time.sleep(0.5)
        print("\nA camera in front of the entrance is focussed on you.")
        time.sleep(1)
        print("'Who are you?' drones from the intercom under the camera.")
        time.sleep(1.5)
        print("'You have no business here and I don't know you, go away!")
        time.sleep(1.8)
        print("You don't feel like arguing, so you take a few steps back.")
        time.sleep(1.5)
        medAbteilungFlur(environment)
        
    else:        
        time.sleep(0.5)
        print("\nCurrent position: Medical department")
        time.sleep(0.5)
        print("(1) Go towards the main control center")
        time.sleep(0.5)
        print("( ) other commands")
        time.sleep(0.5)
    
        cmdlist = ['1', 'look', 'look around', 'talk to edith', 'talk to woman']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("You head towards the main control center")
            time.sleep(0.5)
            medAbteilungFlur(environment)
        
        elif cmd == 'look' or cmd == 'look around':
            time.sleep(0.5)
            print("You take a look around.")
            time.sleep(0.5)
            print("Apart from the old WOMAN called EDITH, there is nothing special in the room.")
            time.sleep(0.5)
            medAbteilung(environment)
            
        elif cmd == 'talk to woman' or cmd == 'talk to edith':
            time.sleep(0.5)
            gesprächEdith(environment)

##################################################################################################################################################
            
def gefangenentraktZentraleKeinNarrezMehr(environment):
    time.sleep(0.5)
    print("\nYou enter the room.")
    time.sleep(0.5)
    print("Everything seems to be as before, but Narrez has disappeared without a trace.")
    time.sleep(1)
    
    cmdlist = [
               'look around',
               'look',
               'go to airlock', 
               'open airlock', 
               'examine airlock',
               'go to exit', 
               'open exit', 
               'examine exit', 
               'examine escape pod',
               'go to escape pod',
               'use escape pod',
               ]
    cmd = getcmd(cmdlist)
    
    if cmd == 'look' or cmd == 'look around':
        time.sleep(0.5)
        print("You take a look around the room.")
        time.sleep(1.5)
        print("Many locked lockers are on the opposite side of the computer.")
        time.sleep(2.5)
        print("An ESCAPE POD can be seen next to the computer.")
        time.sleep(1.5)
        print("The path to the cryochamber is and remains closed.")
        time.sleep(1.5)
        gefangenentraktZentraleKeinNarrezMehr(environment)
        
    elif cmd == 'examine escape pod' or cmd == 'go to escape pod' or cmd == 'use escape pod':
        if iGenerator[0] == 'An':
            time.sleep(0.5)
            print("You can see that the escape pod is active again.")
            time.sleep(1)
            dieFlucht(environment)
        else:
            time.sleep(0.5)
            print("The escape pod cannot be opened.")
            time.sleep(0.7)
            print("The associated GENERATOR must first be switched on again.")
            time.sleep(1.2)
            gefangenentraktZentraleKeinNarrezMehr(environment)
                
    elif cmd == 'go to airlock' or cmd == 'open airlock' or cmd == 'examine airlock' or cmd == 'go to exit' or cmd == 'open exit' or cmd == 'examine exit':
        time.sleep(0.5)
        print("You move in the direction of the airlock.")
        time.sleep(1.5)
        print("The airlock opens and you walk through it.")
        time.sleep(1.5)
        print("You are in a stairwell.")
        time.sleep(1)
        print("On a map on the wall you can see that the crew quarters should be above you")
        print("and the engine room below you.")
        time.sleep(4)
        print("One way leads upwards, the other downwards.")
        time.sleep(1.5)
        treppenhausGZ(environment)
        

# - - - - - Gespräche - - - - -                          

def narrezGespräch(environment):
    time.sleep(2)
    print("\nAs you enter the room, a man is aiming a blaster at you.")
    time.sleep(1.7)
    print("He has a chapped lip and doesn't seem surprised to see you.")
    time.sleep(1.8)
    print("He is wearing a 'Galaxy Space Merchants' mechanic's uniform, red with black decorations.")
    time.sleep(1.9)
    print("His stature is rather skinny, his face sunken, dark circles hang under his eyes.") 
    time.sleep(2)
    print("'What are you doing here?' it booms from his bulging lips.")
    time.sleep(1.6)
    narrezGespräch1(environment)

def narrezGespräch1(environment):
    time.sleep(0.4)
    print("\n(1) Ask where you are")
    time.sleep(0.4)
    print("(2) Explain that you have lost your memory")
    time.sleep(0.4)
    print("(3) Ask what attacked you")
    time.sleep(0.4)
    print("(4) Ask to lower the weapon")
    time.sleep(0.4)
    print("(5) Threaten to make him put the gun down")
    time.sleep(0.4)
    
    cmdlist = ['1', '2', '3', '4', '5']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        print("The man shakes his head.")
        time.sleep(0.8)
        print("'You don't know that? What's wrong with you?")
        time.sleep(1)
        print(" We are travelling to Karion 4 on a Merchants Ship.")
        time.sleep(1.2)
        print(" They probably need food, weapons and whatnot.")
        time.sleep(1.1)
        print(" Oh yes, and prisoners.")
        time.sleep(1)
        print("The man raises an eyebrow, narrows his eyes and examines you.")
        time.sleep(2)
        if mAus[0] == 'Gefangenenoverall':
            print("'By the look of you, you must have been caged for something.")
            time.sleep(1.3)
            print(" What did you do? Killed someone? Taken something that doesn't belong to you?")
            time.sleep(1.4)
            print(" Doesn't really matter now.")
            time.sleep(0.4)
            print(" Any last words before I shoot you?'")
            time.sleep(1)
            narrezGespräch2(environment)
        else:
            print("'You must be mad, the way you walk around")
            time.sleep(1)
            print(" Any last words before I shoot you?'")
            time.sleep(1.2)
            narrezGespräch2(environment)
            
    elif cmd == '2':
        time.sleep(1)
        print("The man looks at you in surprise.")
        time.sleep(1)
        print("'You can't remember anything?")
        time.sleep(1)
        print(" You must have run into a wall, huh?'")
        time.sleep(1)
        print("The corners of the man's mouth turn upwards.")
        time.sleep(1)
        print("'Since you come from the prisoner wing of the ship, you can probably guess who you are,")
        print(" or at least what you are.")
        time.sleep(3.5)
        print(" Any last words before I shoot you?'")
        time.sleep(1)
        narrezGespräch2(environment)
        
    elif cmd =='3':
        time.sleep(1)
        print("The man shrugs")
        time.sleep(1)
        print("'Who knows, there are morons running around all over the ship.")
        time.sleep(2)
        print(" But the more important question is, what are you doing here?'")
        time.sleep(1)
        narrezGespräch1(environment)       
    
    elif cmd == '4':
        time.sleep(1)
        print("'I won't do shit!'")
        time.sleep(1)
        narrezGespräch1(environment)
        
    elif cmd == '5':
        time.sleep(1)
        print("'HAHAHAHA'")
        time.sleep(1)
        print("The man laughs and before you even think about attacking him, he shoots at you.")
        time.sleep(3)
        print("The blaster burns a hole through your head.")
        time.sleep(2)
        print("You are instantly dead...")
        time.sleep(1)
        print("GAME OVER")
        time.sleep(7)
        exit
        
def narrezGespräch2(environment):
    time.sleep(1)
    print("\n(1) Beg him not to shoot you")
    time.sleep(0.4)
    print("(2) Attack")
    time.sleep(0.4)
    print("(3) Take flight")
    time.sleep(0.4)
    
    cmdlist = ['1', '2', '3',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(1)
        print("'Mhhhh...'")
        time.sleep(1)
        print("He scratches his head with the blaster.")
        time.sleep(1)
        print("'That could be arranged if you do something for me.'")
        time.sleep(1)
        print("(1) Agree")
        time.sleep(0.4)
        print("(2) Decline")
        time.sleep(0.4)
        
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(1)
            print("'Splendid!'")
            time.sleep(1)
            print("He puts down his gun.")
            time.sleep(1)
            print("'We're going to be best friends if it goes on like this.")
            time.sleep(1.8)
            print(" I'm Narrez, by the way.'")
            time.sleep(1)
            narrezGespräch3(environment)
            
        elif cmd == '2':
            time.sleep(1)
            print("'Too bad, you could have been useful to me.'")
            time.sleep(1)
            print("The man shoots at you.")
            time.sleep(1)
            print("The blaster burns a hole through your head.")
            time.sleep(2)
            print("You are instantly dead...")
            time.sleep(1)
            print("GAME OVER")
            time.sleep(7)
            exit()
            
    elif cmd == '2' or cmd == '3':
        time.sleep(1)
        print("'What are you doing there?'")
        time.sleep(1)
        print("The man shoots at you without hesitation.")
        time.sleep(1)
        print("The blaster burns a hole through your head.")
        time.sleep(2)
        print("You are instantly dead...")
        time.sleep(1)
        print("GAME OVER")
        time.sleep(7)
        exit()
        
def narrezGespräch3(environment):
    time.sleep(1)
    print("\n'Now open your ears.")
    time.sleep(1)
    print(" As far as I understand the situation here, some of the ship's generators have failed.")
    time.sleep(2.5)
    print(" One of us has to go down to the engine deck and restart the generator 4FK from there.")
    time.sleep(2.5)
    print(" You will be that lucky one.")
    time.sleep(1)
    print(" Will you?")
    time.sleep(1)
    print()
    time.sleep(0.5)
    print("(1) Yes")
    time.sleep(0.5)
    print("(2) No")
    time.sleep(0.5)
    print("(3) F*ck off")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', '3']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("'Great decision.")
        time.sleep(1)
        print(" This is the way to the engine room.")
        time.sleep(1)
        print("He points in the direction of the airlock.")
        time.sleep(1)
        print("'Just ignore the way up, only chaos and red-eyed morons there.")
        time.sleep(1.5)
        print(" Hurry up, time runs out.'")
        time.sleep(1.5)
        print("He turns to a large computer placed in the center of the room")
        print("and ignores you.")
        time.sleep(2)
        gefangenentraktZentrale(environment)
        
    elif cmd == '2' or cmd == '3':
        time.sleep(1)
        print("'Too bad... Things were going so swell between us.")
        time.sleep(2)
        print("A shot is fired...")
        time.sleep(1)
        print("GAME OVER")
        time.sleep(7)
        exit()
        ####################################################
def wulffGespräch(environment):
    time.sleep(0.5)
    print("\n'Who are you,' the old man asks in a grizzled voice.")
    time.sleep(1)
    print("He wears a gray-green worn out robe that is adorned with a strange coat of arms.")
    time.sleep(2.2)
    if mAus[0] == 'Gefangenenoverall':
        time.sleep(0.5)
        print("It seems as if he's only now noticing your clothes.")
        time.sleep(1.2)
        print("'A prisoner then... prepare yourself!")
        time.sleep(1.2)
        kampfWulff(environment)
    else:
        time.sleep(0.5)
        print("'You seem to be one of the ship's personnel, congratulations on surviving this long.")
        time.sleep(2.5)
        print(" My name is Wulff, I take care that no one uninvited comes in here.")
        time.sleep(2)
        print(" I'll tell you the password, then you can go on to the main control center.")
        time.sleep(2)
        print(" It is 'Dystopia'")
        mLosungswort.remove('Bitteschön')
        mLosungswort.append('Dystopia')
        time.sleep(1)
        print(" Go on now, I have to stand guard here.'")
        time.sleep(1.5)
        print("After Wulff has taken up his post again, you go into the main control center.")
        time.sleep(2.2)
        aqariaGespräch(environment)
    
def aqariaGespräch(environment):
    time.sleep(0.5)
    print("\nThe ship's main control center seems huge. There are vast numbers of terminals,")
    print("screens, seating and standing areas and strange equipment. The only persons you see are")
    print("two armed men in grey-green robes and a woman sitting in the captain's seat.")
    time.sleep(8.5)
    print("The two men, both armed with fighting sticks, turn towards you and immediately approach you.")
    time.sleep(2)
    print("The one on the left asks you a question.")
    time.sleep(1.5)
    aqariaGespräch1(environment)
    
def aqariaGespräch1(environment):
    if mLosungswort[0]=='Dystopia':
        print("\n'What is the password?'")
        time.sleep(0.5)
        print("(1) Dystopia")
        time.sleep(0.5)
        print("(2) Narrez?")
        time.sleep(0.5)
        print("(3) Galaxy Space Merchants?")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("'Okay, you can move around freely here.")
            time.sleep(1)
            print(" But don't get into mischief. Do you understand?'")
            time.sleep(1)
            hauptzentrale(environment)
        elif cmd == '2' or cmd == '3':
            aqariaGespräch2(environment)
            
          
    else:
        print("\n'What is the password'")
        time.sleep(0.5)
        print("(1) Name the password")
        time.sleep(1)
        print("(2) mh... Narrez")
        time.sleep(1)
        print("(3) Galaxy Space Merchants?")
        time.sleep(1)
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(1)
            print("...You have no way of knowing that...")
            time.sleep(1.8)
            aqariaGespräch1(environment)
        elif cmd == '2' or cmd == '3':
            aqariaGespräch2(environment)
                  
def aqariaGespräch2(environment):
    time.sleep(0.5)
    print("\n'Enemy, what are you doing here?")
    time.sleep(1)
    print(" So tell us! What was going on out there'")
    time.sleep(1)
    print("(1) I have nothing bad in mind, please believe me")
    time.sleep(0.5)
    print("(2) What kind of fools are you?")
    time.sleep(0.5)
    if iWulffLP[0] <= 0:
        print("(3) I've killed that one out there and now it's your turn!!! (attack)")
        time.sleep(0.5)
        
        cmdlist = ['1', '2', '3']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            time.sleep(0.5)
            print("'Nothing bad in mind? We'd better play it safe and ki...'")
            time.sleep(2)
            print("A bright voice can be heard from further back.")
            time.sleep(1.5)
            print("'I believe you, please let this person pass.'")
            time.sleep(1.5)
            print("'But mistress, we can't...'")
            time.sleep(1.2)
            print("'no objections!'")
            time.sleep(1.1)
            print("The chatty guard looks down and his face hardens.")
            time.sleep(2)
            print("'Yes mistress... You may go now.'")
            time.sleep(2)
            print("You walk past the guards.")
            time.sleep(2.5)
            hauptzentrale(environment)
            
        elif cmd == '2':
            time.sleep(0.5)
            print("'FOOLS?!")
            time.sleep(1)
            print("The man hits you with his staff.")
            time.sleep(1)
            mLP[0] = mLP[0] - 6
            
            if mLP[0] >= 0:
                print("Ouch!")
                time.sleep(1)
                aqariaGespräch2(environment)
            else:
                print("That was one hit too many...")
                time.sleep(1)
                endingDeath(environment)
            
        elif cmd == '3':
            time.sleep(0.5)
            print("The two of them beat you up without hesitation.")
            time.sleep(1)
            print("You pass out...")
            time.sleep(1)
            print("GAME OVER")
            time.sleep(7)
            exit()
        
    else:
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            time.sleep(0.5)
            print("'Nothing bad in mind? We'd better play it safe and ki...'")
            time.sleep(2)
            print("A bright voice can be heard from further back.")
            time.sleep(1.5)
            print("'I believe you, please let this person pass.'")
            time.sleep(1.5)
            print("'But mistress, we can't...'")
            time.sleep(1.2)
            print("'no objections!'")
            time.sleep(1.1)
            print("The chatty guard looks down and his face hardens.")
            time.sleep(2)
            print("'Yes mistress... You may go now.'")
            time.sleep(2)
            print("You walk past the guards.")
            time.sleep(2.5)
            hauptzentrale(environment)            
        elif cmd == '2':
            time.sleep(0.5)
            print("'FOOLS?!")
            time.sleep(1)
            print("The man hits you with his staff.")
            time.sleep(1)
            mLP[0] = mLP[0] - 6
            
            if mLP[0] >= 0:
                print("Ouch!")
                time.sleep(1)
                aqariaGespräch2(environment)
            else:
                print("That was one hit too many...")
                time.sleep(1)
                endingDeath(environment)
    ###########################
def gesprächMerana(environment):
    time.sleep(0.5)
    print("\n(1) What is your name?")
    time.sleep(0.5)
    print("(2) Why are you on this ship?")
    time.sleep(0.5)
    print("(3) What is in the lab?")
    time.sleep(0.5)
    print("(4) What will I find in the armory?")
    time.sleep(0.5)
    print("(5) What's in the medical department?")
    time.sleep(0.5)
    print("(6) End conversation")
    time.sleep(0.5)
        
    cmdlist = ['1', '2', '3', '4', '5', '6',]
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("'My name is Merana, my two friends here are called Dalex and Femin,")
        print(" the guard outside is called Wulff. They are my protectors on my way")
        print(" to Karion 4.")
        time.sleep(4)
        gesprächMerana(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("'My father's murderer, Narilyn Rezamo, better known as Narrez, is being")
        print(" taken to Karion 4, the prison planet. Or at least that was the plan before")
        print(" the accident with the water supply. Everyone who drank water from the dispenser")
        print(" went insane and got those horrible eyes.")
        time.sleep(5)
        print("(1) Tell Merana about Narrez in the central prison wing")
        time.sleep(0.5)
        print("(2) Ask something else")
        time.sleep(0.5)
        
        cmdlist = ['1', '2']
        cmd = getcmd(cmdlist)
        
        if cmd == '1':
            if iNarrezMerana[0] == 'Unwissend':
                time.sleep(0.5)
                print("'This king slayer is no longer in his cryogenic chamber?")
                time.sleep(1)
                print(" Dalex, Femin, since we will most likely never land on Karion 4,")
                print(" we will take care of this stain on humanity.")
                print(" You know what you have to do.'")
                time.sleep(4.5)
                print("Without hesitation, the two guards leave the room in the direction of the prison wing.")
                time.sleep(1.4)
                print("'Thank you for being honest to me. You can use this key to open that CHEST at the wall.")
                print(" The content should represent your reward.'")
                time.sleep(2.5)
                print("After a short time, the two guards return to the main office.")
                time.sleep(1.6)
                print("Merana looks at both of them with interest, the silent guard just nods silently.")
                time.sleep(1.7)
                print("A relieved smile crosses the woman's face.")
                time.sleep(2)
                print("'Good,' is all she has to say.")
                iNarrezMerana.remove('Unwissend')
                iNarrezMerana.append('Wissend')
                time.sleep(1)
                gesprächMerana(environment)
                
            else:
                time.sleep(0.5)
                print("'You already said that.'")
                time.sleep(0.5)
                gesprächMerana(environment)
                          
        elif cmd == '2':
            time.sleep(0.5)
            gesprächMerana(environment)
            
    elif cmd == '3':
        time.sleep(0.5)
        print("'There is a strange professor in the laboratory.")
        time.sleep(1)
        print(" He had also drunk some of this water, but he had an antidote ready quickly enough.")
        time.sleep(2)
        print(" Now he is no longer completely sane, the poison had probably already attacked his brain.")
        time.sleep(1.9)
        print(" All he talks about is some toy.")
        time.sleep(1)
        print(" Femin said he had seen such a stuffed animal in the team quarters.")
        time.sleep(1.9)
        print(" But he doesn't know exactly where he last saw it.")
        time.sleep(1.5)
        gesprächMerana(environment)
    
    elif cmd == '4':
        time.sleep(0.5)
        print("'Some crazy prisoner has barricaded herself in the armory.")
        time.sleep(1.2)
        print(" Anyone who goes in there will not come out again.")
        time.sleep(1)
        print(" You can only get in there with the right firepower.")
        time.sleep(1.1)
        gesprächMerana(environment)
        
    elif cmd == '5':
        time.sleep(0.5)
        print("' An elderly lady has locked herself in the medical department.")
        time.sleep(1.8)
        print(" It has no protection and won't let anyone in for security reasons.")
        time.sleep(1.7)
        print(" If you gave her something that would make her feel a little safer,")
        print(" she might even open the door for you.")
        time.sleep(2.5)
        gesprächMerana(environment)
        
    elif cmd == '6':
        time.sleep(0.5)
        print("You continue to look around the room.")
        time.sleep(0.5)
        hauptzentrale(environment)
         
def gesprächProfessor(environment):
    time.sleep(0.5)
    print("\n(1) What has happened to you?")
    time.sleep(0.5)
    print("(2) Do you have anything useful in here?")
    time.sleep(0.5)
    print("(3) Do you know anything useful about generators?")
    time.sleep(0.5)
    print("(4) End conversation")
    time.sleep(0.5)
    
    cmdlist = ['1', '2', '3', '4']
    cmd = getcmd(cmdlist)
    
    if cmd == '1':
        time.sleep(0.5)
        print("'I was almost as red-eyed as the others, but I was clever!")
        time.sleep(1.5)
        print(" Medicine helps everyone, as long as you keep carrying on!")
        time.sleep(2)
        gesprächProfessor(environment)
        
    elif cmd == '2':
        time.sleep(0.5)
        print("'There's an old armored suit in the LOCKER back there, you can have it for all I care.")
        time.sleep(2)
        print(" I now have everything I need to be happy.'")
        time.sleep(1.5)
        gesprächProfessor(environment)
        
    elif cmd == '3':
        time.sleep(0.5)
        print("'I no longer have anything to do with generators!")
        time.sleep(1.2)
        print(" There is a HATCH under that crate at the back, it leads directly to the generators.")
        time.sleep(1.8)
        print(" Why should there be a shortcut to the generators be installed in a laboratory at all?'")
        time.sleep(1.9)
        gesprächProfessor(environment)
        
    elif cmd == '4':
        time.sleep(0.5)
        print("You walk away from the professor.")
        time.sleep(0.5)
        labor(environment)
         
def gesprächEdith(environment):
    time.sleep(0.5)
    print("\nYou go to Edith.")
    time.sleep(0.7)
    if iKleineRüstung[0] == 'Besitz':
        print("Edith looks at you with excitement.")
        time.sleep(0.8)
        print("'That's a nice set of clothes and it looks sturdy too.")
        time.sleep(1.3)
        print("Edith takes the clothings.")
        time.sleep(0.7)
        print("'Thank you for this, here, I'll give you the key to the MEDICINE CABINET")
        print(" in ROOM H.")
        iKleineRüstung.remove('Besitz')
        iKleineRüstung.append('Dame')
        time.sleep(2)
        medAbteilung(environment)
    else:
        time.sleep(0.5)
        print("'I don't think we have anything more to discuss at the moment.'")
        time.sleep(0.5)
        medAbteilung(environment)
        
          
    
# - - - - - Kämpfe - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -                          

def kampf1FlurSüdRechts(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'flee', 'status enemy',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iWesen1LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You defeated the enemy!!!")
            time.sleep(1)
            print("The enemy further back is attacking you!")
            kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iWesen1S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                
                if mS >= iWesen1HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iWesen1HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen1HP[0] #
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
            elif iWesen1S < mHP: #
                iWesen1LP[0] = iWesen1LP[0] + iWesen1S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iWesen1HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iWesen1HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen1HP[0] #
                    kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("The path behind you is blocked, escape is impossible!")
        kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iWesen1LP >= [6]:
            print("The enemy is still in top shape!")
            kampf1FlurSüdRechts(environment)
        elif iWesen1LP >= [3]:
            print("The enemy is getting weak!")
            kampf1FlurSüdRechts(environment)
        elif iWesen1LP >= [0]:
            print("The enemy is badly injured, just a few more hits!")
            kampf1FlurSüdRechts(environment)
        elif iWesen1LP <= [0]: #
            print("Just one more blow!!!")
            kampf1FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN

def kampf2FlurSüdRechts(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iWesen2LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            time.sleep(1)
            print("Still perplexed by the fight, you sink to the ground.")
            time.sleep(1.7)
            print("''What kind of creatures were they?''")
            time.sleep(1.5)
            print("After a few minutes of rest, you get up again.")
            time.sleep(2)
            flurSüdRechtsGeschlossen(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iWesen2S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                
                if mS >= iWesen2HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iWesen2HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen2HP[0] #
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
            elif iWesen2S < mHP: #
                iWesen2LP[0] = iWesen2LP[0] + iWesen2S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iWesen2HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iWesen2HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iWesen2HP[0] #
                    kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("The path behind you is blocked, escape is impossible!")
        kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN     
    elif cmd == 'status enemy':
        if iWesen2LP >= [8]:
            print("The enemy is still in top shape!")
            kampf2FlurSüdRechts(environment)
        elif iWesen2LP >= [4]:
            print("The enemy is getting weak!")
            kampf2FlurSüdRechts(environment)
        elif iWesen2LP >= [0]:
            print("The enemy is badly injured, just a few more hits!")
            kampf2FlurSüdRechts(environment)
        elif iWesen2LP <= [0]: #
            print("Just one more blow!!!")
            kampf2FlurSüdRechts(environment) #HIER ENVIRONMENT ÄNDERN
        
 
def kampfFlurSüdLinks(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iEtwasLP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            flurSüdLinksGeschlossen(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iEtwasS >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")               
                if mS >= iEtwasHP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iEtwasHP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iEtwasHP[0] #
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
            elif iEtwasS < mHP: #
                iEtwasLP[0] = iEtwasLP[0] + iEtwasS[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iEtwasHP: #
                    time.sleep(1)
                    print("...however, your opponent does not seem to take any damage.")
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iEtwasHP: #
                    time.sleep(1)
                    print("....and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iEtwasHP[0] #
                    kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("There is no way out!")
        kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iEtwasLP >= [10]: #
            print("The enemy is still in top shape!")
            kampfFlurSüdLinks(environment)
        elif iEtwasLP >= [5]: #
            print("The enemy is getting weak!")
            kampfFlurSüdLinks(environment)
        elif iEtwasLP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfFlurSüdLinks(environment)
        elif iEtwasLP <= [0]: #
            print("Just one more blow!!!")
            kampfFlurSüdLinks(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfWulff(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee',]
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iWulffLP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            print("You waste no time and move on to the next room.")
            time.sleep(2)
            aqariaGespräch(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iWulffS >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                 
                if mS >= iWulffHP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iWulffHP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iWulffHP[0] #
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN
            elif iWulffS < mHP: #
                iWulffLP[0] = iWulffLP[0] + iWulffS[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iWulffHP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iWulffHP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iWulffHP[0] #
                    time.sleep(1)
                    kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You escape!")
        time.sleep(1)
        treppenhausHZ(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iWulffLP >= [20]: ######
            print("The enemy is still in top shape!")
            kampfWulff(environment)
        elif iWulffLP >= [10]: ######
            print("The enemy is getting weak!")
            kampfWulff(environment)
        elif iWulffLP >= [0]: ######
            print("The enemy is badly injured, just a few more hits!")
            kampfWulff(environment)
        elif iWulffLP <= [0]: #
            print("Just one more blow!!!")
            kampfWulff(environment) #HIER ENVIRONMENT ÄNDERN
    
def kampfMMonster(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iMMonsterLP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the monster!!!")
            time.sleep(1)
            print("Now you can take a closer look around the engine room.")
            time.sleep(1)
            maschinenraum(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iMMonsterS >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                 
                if mS >= iMMonsterHP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iMMonsterHP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iMMonsterHP[0] #
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN
            elif iMMonsterS < mHP: #
                iMMonsterLP[0] = iMMonsterLP[0] + iMMonsterS[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iMMonsterHP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iMMonsterHP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iMMonsterHP[0] #
                    time.sleep(1)
                    kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You escape!")
        time.sleep(1)
        maschinenraumFlur(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iMMonsterLP >= [66]: #
            print("The enemy is still in top shape!")
            kampfMMonster(environment)
        elif iMMonsterLP >= [24]: #
            print("The enemy is getting weak!")
            kampfMMonster(environment)
        elif iMMonsterLP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfMMonster(environment)
        elif iMMonsterLP <= [0]: #
            print("Just one more blow!!!")
            kampfMMonster(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfRotAuge1(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge1LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            mannschaftsquartiereFlur1(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iRotAuge1S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                 
                if mS >= iRotAuge1HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge1HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge1HP[0] #
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge1S < mHP: #
                iRotAuge1LP[0] = iRotAuge1LP[0] + iRotAuge1S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iRotAuge1HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge1HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge1HP[0] #
                    time.sleep(1)
                    kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You cannot escape!")
        time.sleep(1)
        kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iRotAuge1LP >= [12]: #
            print("The enemy is still in top shape!")
            kampfRotAuge1(environment)
        elif iRotAuge1LP >= [7]: #
            print("The enemy is getting weak!")
            kampfRotAuge1(environment)
        elif iRotAuge1LP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfRotAuge1(environment)
        elif iRotAuge1LP <= [0]: #
            print("Just one more blow!!!")
            kampfRotAuge1(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfRotAuge2(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge2LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            mannschaftsquartiereFlur3(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iRotAuge2S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                 
                if mS >= iRotAuge2HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge2HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge2HP[0] #
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge2S < mHP: #
                iRotAuge2LP[0] = iRotAuge2LP[0] + iRotAuge2S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iRotAuge2HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge2HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge2HP[0] #
                    time.sleep(1)
                    kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You cannot escape!")
        time.sleep(1)
        kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iRotAuge2LP >= [14]: #
            print("The enemy is still in top shape!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge2LP >= [8]: #
            print("The enemy is getting weak!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge2LP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge2LP <= [0]: #
            print("Just one more blow!!!")
            kampfRotAuge2(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfRotAuge3(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge3LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            print("The opponent dropped something...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You pick up the item...")
            time.sleep(1)
            print("It is a stuffed animal.")
            time.sleep(1)
            print("It looks like a monkey")
            time.sleep(1)
            print("Take the item with you?")
            print("(1) Yes")
            print("(2) No")
            
            cmdlist =['1', '2']
            cmd = getcmd(cmdlist)
            
            if cmd == '1':
                time.sleep(1)
                print("You take the stuffed animal.")
                time.sleep(1)
                print("Sweet")
                time.sleep(1)
                mStoffKuscheltier.remove('Rotauge')
                mStoffKuscheltier.append('Meins')
                print("You leave the room.")
                time.sleep(1)
                mannschaftsquartiereFlur3(environment)
            elif cmd == '2':
                time.sleep(1)
                print("You'd rather leave it there and leave the room.")
                time.sleep(1)
                mannschaftsquartiereFlur3(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iRotAuge3S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                
                if mS >= iRotAuge3HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge3HP: #
                    time.sleep(1)
                    print("...and hits you!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge3HP[0] #
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge3S < mHP: #
                iRotAuge3LP[0] = iRotAuge3LP[0] + iRotAuge3S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iRotAuge3HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge3HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge3HP[0] #
                    time.sleep(1)
                    kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You escape!")
        time.sleep(1)
        print("You close the door behind you...")
        time.sleep(1)
        print("...the enemy is trapped behind.")
        time.sleep(1)
        mannschaftsquartiereFlur3(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iRotAuge3LP >= [20]: #
            print("The enemy is still in top shape!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge3LP >= [8]: #
            print("The enemy is getting weak!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge3LP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge3LP <= [0]: #
            print("Just one more blow!!!")
            kampfRotAuge3(environment) #HIER ENVIRONMENT ÄNDERN
    
def kampfRotAuge4(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge4LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            print("You can see that the opponent had something in his jacket...")
            time.sleep(1)
            print("It's a medikit!")
            time.sleep(1)
            print("You use it right away.")
            mLP[0] = mLP[0] + 10
            time.sleep(1)
            waffenkammerFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iRotAuge4S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                 
                if mS >= iRotAuge4HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge4HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge4HP[0] #
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge4S < mHP: #
                iRotAuge4LP[0] = iRotAuge4LP[0] + iRotAuge4S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iRotAuge4HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge4HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge4HP[0] #
                    time.sleep(1)
                    kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You escape!")
        time.sleep(1)
        hauptzentrale(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iRotAuge4LP >= [18]: #
            print("The enemy is still in top shape!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge4LP >= [7]: #
            print("The enemy is getting weak!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge4LP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN  
        elif iRotAuge4LP <= [0]: #
            print("Just one more blow!!!")
            kampfRotAuge4(environment) #HIER ENVIRONMENT ÄNDERN 
    
def kampfRotAuge5(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge5LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            laborFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iRotAuge5S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                
                if mS >= iRotAuge5HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge5HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge5HP[0] #
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge5S < mHP: #
                iRotAuge5LP[0] = iRotAuge5LP[0] + iRotAuge5S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iRotAuge5HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge5HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge5HP[0] #
                    time.sleep(1)
                    kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You escape!")
        time.sleep(1)
        hauptzentrale(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iRotAuge5LP >= [15]: #
            print("The enemy is still in top shape!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge5LP >= [6]: #
            print("The enemy is getting weak!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge5LP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge5LP <= [0]: #
            print("Just one more blow!!!")
            kampfRotAuge5(environment) #HIER ENVIRONMENT ÄNDERN
            
def kampfRotAuge6(environment): #HIER ENVIRONMENT ÄNDERN
    print("\nThe battle is on!")
    cmdlist = ['a', 'attack', 'attack enemy', 'flight', 'status enemy', 'flee']
    cmd = getcmd(cmdlist)
    if cmd == 'a' or cmd == 'attack' or cmd == 'attack enemy':
        if mLP[0] <= 0:
            time.sleep(1)
            print("You're too weak for another attack...")
            time.sleep(1)
            print("The enemy approaches you...")
            time.sleep(1)
            print("...you pass out...")
            time.sleep(1)
            endingDeath(environment)    
        elif iRotAuge6LP[0] <= 0: #
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("...")
            time.sleep(1)
            print("You have defeated the enemy!!!")
            time.sleep(1)
            print("You can see that the opponent had something in his jacket...")
            time.sleep(1)
            print("It's a medikit!")
            time.sleep(1)
            print("You use it right away.")
            mLP[0] = mLP[0] + 10
            time.sleep(1)
            medAbteilungFlur(environment) #HIER ENVIRONMENT ÄNDERN: NÄCHSTERRAUM        
        else:
            print("You attack...")
            if iRotAuge6S >= mHP: #
                time.sleep(1)
                print("...however, your opponent does not seem to take any damage.")
                print("Fleeing would be a good idea!")
                time.sleep(3)
                print("The enemy attacks...")                
                if mS >= iRotAuge6HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN              
                elif mS < iRotAuge6HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge6HP[0] #
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
            elif iRotAuge6S < mHP: #
                iRotAuge6LP[0] = iRotAuge6LP[0] + iRotAuge6S[0] - mHP[0] #
                time.sleep(1)
                print("...and hit!!")
                time.sleep(1)
                print("The enemy attacks...")
                if mS >= iRotAuge6HP: #
                    time.sleep(1)
                    print("...Your armor absorbs all the damage!")
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN               
                elif mS < iRotAuge6HP: #
                    time.sleep(1)
                    print("...and hits you!!!")
                    mLP[0] = mLP[0] + mS[0] - iRotAuge6HP[0] #
                    time.sleep(1)
                    kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'flight' or cmd == 'flee':
        time.sleep(1)
        print("You escape!")
        time.sleep(1)
        hauptzentrale(environment) #HIER ENVIRONMENT ÄNDERN
    elif cmd == 'status enemy':
        if iRotAuge6LP >= [12]: #
            print("The enemy is still in top shape!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge6LP >= [5]: #
            print("The enemy is getting weak!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge6LP >= [0]: #
            print("The enemy is badly injured, just a few more hits!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
        elif iRotAuge6LP <= [0]: #
            print("Just one more blow!!!")
            kampfRotAuge6(environment) #HIER ENVIRONMENT ÄNDERN
            
# Ende

def endingDeath(environment):
    time.sleep(1)
    print("You died.")
    time.sleep(1.5)
    print("GAMEOVER")
    time.sleep(3.5)
    exit(0)
    
def endeKeineFluchtkapsel(environment):
    time.sleep(0.5)
    print("You enter the room.")
    time.sleep(1)
    print("Narrez escaped with the escape pod!")
    time.sleep(1.5)
    print("There is no other way to escape from the spaceship...")
    time.sleep(2)
    print("GAME OVER")
    time.sleep(3)
    exit()
           
def dieFlucht(environment):
    time.sleep(0.5)
    print("\nYou open the escape pod and climb inside.")
    if iBewFrau[0] == 'Traurig':
        time.sleep(1.5)
        print("Shortly before you initiate the launch process, you hear footsteps outside the pod.")
        time.sleep(2)
        print("'Take me with you,' you hear a familiar voice.")
        time.sleep(2)
        print("A person stands in front of the escape pod")
        time.sleep(1.5)
        print("It is the woman from the armoury.")
        time.sleep(2)
        print("'Please take me with you, I don't want to die here!'")
        time.sleep(2)
        print("You nod to her, she thanks you and climbs into the pod with you.")
        time.sleep(2)
        print("'My name is Izzin, by the way, what's yours?")
        time.sleep(2)
        iWulffLuck.append(randint(1,2))
        if iWulffHP[0] >= 0 and iWulffLuck[0] == 1:
            print("Suddenly someone starts shouting.")
            time.sleep(1.5)                
            print("'Do you still have a free seat?' someone shouts loudly from outside.")
            time.sleep(2)
            print("The next moment, guard Wulff jumps into the escape pod")
            time.sleep(2)
            print("'Do you still have a place for me? All this has become too much for me!")
            time.sleep(2)
            print(" What's your name, kid?")
            time.sleep(2) 
            print("")
            print("Suddenly the memory of your past comes back to you...")
            time.sleep(2)
            print("...")
            time.sleep(1.5)
            print("'My name is Mex...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print(" and I am to blame for this chaos'")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("You activate the launch process and the pod is shot into space.")
            time.sleep(5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!CONGRATULATIONS!!!\n")
            time.sleep(4)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       You have successfully finished the game!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n               until next time!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(15)
            exit()
        else:
            print("Suddenly the memory of your past comes back to you...")
            time.sleep(2)
            print("...")
            time.sleep(1.5)
            print("'My name is Mex...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print(" and I am to blame for this chaos'")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("You activate the launch process and the pod is shot into space.")
            time.sleep(5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!CONGRATULATIONS!!!\n")
            time.sleep(4)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       You have successfully finished the game!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n               until next time!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(15)
            exit()
    else:
        print("Suddenly you hear several footsteps from outside.")
        time.sleep(2)
        print("Merana and her two guards are standing in front of you.")
        time.sleep(2)
        print("'I request entry into this escape pod so that my men and I can see our home again.")
        time.sleep(2)
        print(" Would you be so kind as to take us with you?'")
        time.sleep(2)
        print("Meanwhile, the two guards have long since entered the capsule and made room")
        print("for their escort.")
        time.sleep(2)
        print("'What is the name of our saviour?")
        time.sleep(2)
        if iWulffHP[0] >= 0:
            print("Outside, someone starts shouting.")
            time.sleep(2)
            print("'Don't forget me!' someone shouts loudly from outside.")
            time.sleep(2)
            print("The next moment, guard Wulff jumped into the escape pod.")
            time.sleep(2)
            print("'You almost forgot about me! Who should I thank for that, eh?'")
            time.sleep(2)
            print("Suddenly the memory of your past comes back to you...")
            time.sleep(2)
            print("...")
            time.sleep(1.5)
            print("'My name is Mex...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print(" and I am to blame for this chaos'")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("You activate the launch process and the pod is shot into space.")
            time.sleep(5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!CONGRATULATIONS!!!\n")
            time.sleep(4)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       You have successfully finished the game!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n               until next time!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(15)
            exit()
        else:
            print("Suddenly the memory of your past comes back to you...")
            time.sleep(2)
            print("...")
            time.sleep(1.5)
            print("'My name is Mex...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print(" and I am to blame for this chaos'")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("You activate the launch process and the pod is shot into space.")
            time.sleep(5)
            print("")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n              !!!CONGRATULATIONS!!!\n")
            time.sleep(4)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n       You have successfully finished the game!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("\n               until next time!!!\n")
            time.sleep(3)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(0.5)
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            time.sleep(15)
            exit()      
        
# Haupteingaben
        
def getcmd(cmdlist):
    
    cmd = input('\nInput: ')
    cmd = cmd.lower() # Eingegebene Großbuchstaben werden klein
    
    if cmd in cmdlist:
        return cmd
    
    elif cmd == 'help' or cmd == 'input options' or cmd == 'controls' or cmd == 'controlsystem':
        print("\nThe following entries can be used in the correct places:")
        print("\n-----------------------------------------------------------------------------------")
        print("                 Main Menu     ")
        print()
        print("look/look around               -> look around the room")
        print("use 'object'                   -> use an object")
        print("go to 'object/person'          -> go to an object or a person")
        print("open 'object'                  -> open an object if it is open or")
        print("                                  you have the required key/know the")
        print("                                  required password")
        print("examine 'object/person'        -> examine an object, a person")
        print("take 'object'                  -> take object, this will move it to the inventory")
        print("                                  or to your weapon slot if it is empty")
        print("talk to 'person'               -> enter 'man', 'woman' or specific name to talk to the person")
        print("discard weapon                 -> empty the weapon slot, a new weapon can be")
        print("                                  be equipped")
        print("status                         -> show you your health status")
        print("discard clothes                -> take off your current equipment")
        print("put on 'clothes/equipment'     -> put on equipment, you must take off your")
        print("                               -> equipment first")
        print("")
        print("            You can end the game at any time by entering QUIT            ")
        print("")
        print("Not all entries are always usable, so don't despair if an entry is not available.")
        print("Usually -CAPITALISED- words are usable in some way")
        print("\n-----------------------------------------------------------------------------------")
        print()
        print("                 Combat menu       ")
        print()
        print("                 attack, a       -> attacks enemy")
        print("                 flee, flight    -> Escapes from opponents if possible")
        print("                 status enemy    -> shows the status of the opponent")
        print("\n-----------------------------------------------------------------------------------")
        print()
        print("                 Selection menu")
        print()
        print("                 1")
        print("                 2")
        print("                 3")
        print("...")
        print("At some points in the game you have to make a decision, here you only have")
        print("a limited choice that works with a number input.")
        print("This function will also make it easier to move around once the game has started.")
        print("\n-----------------------------------------------------------------------------------")
        
        return getcmd(cmdlist)
    
    elif cmd == 'status':
        if mLP >= [100]:
            print("You are fully energised!!!")
            print("You still have: {} health points".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [80]:
            print("You've got a few scratches on you!!")
            print("You still have: {} health points".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [60]:
            print("You are slightly injured!")
            print("You still have: {} health points".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [40]:
            print("You are hurt, seek help.")
            print("You still have: {} health points".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [20]:
            print("Critical condition!!!")
            print("You won't be able to take it much longer.")
            print("You still have: {} health points".format(mLP))
            return getcmd(cmdlist)
        elif mLP >= [0]:
            print("Too many injuries...")
            print("If you don't do anything soon, you won't last much longer...")
            print("You still have: {} health points".format(mLP))
            return getcmd(cmdlist)
        elif mLP <= [0]:
            print("One more hit and you're dead!")
            return getcmd(cmdlist)
            
    elif cmd == 'discard clothes':
    
        if 'Unterhose' in mAus:
            print("'Why should I take off my underpants!'")
            print(" I'll leave them on!...''")
            return getcmd(cmdlist)
        elif 'Gefangenenoverall' in mAus:
            print("A tear has appeared when taking off the clothes...")
            print("Item no longer usable.")
            mAus.remove('Gefangenenoverall')
            mAus.append('Unterhose')
            mG.append('Gefangenenoverall')
            mS.remove(2)
            mS.append(1)
            return getcmd(cmdlist)
        elif 'Technikeroverall' in mAus:
            print("A tear has appeared when taking off the clothes...")
            print("Item no longer usable.")
            mAus.remove('Technikeroverall')
            mAus.append('Unterhose')
            mG3.append('Technikeroverall')
            mS.remove(4)
            mS.append(1)
            return getcmd(cmdlist)
        elif 'Panzerung' in mAus:
            print("A tear has appeared when taking off the clothes...")
            print("Item no longer usable.")
            mAus.remove('Panzerung')
            mAus.append('Unterhose')
            mG5.append('Panzerung')
            mS.remove(10)
            mS.append(1)
            return getcmd(cmdlist)
        elif 'Monsterjäger' in mAus:
            print("A tear has appeared when taking off the clothes...")
            print("Item no longer usable.")
            mAus.remove('Monsterjäger')
            mAus.append('Unterhose')
            mG5.append('Monsterjäger')
            mS.remove(13)
            mS.append(1)
            return getcmd(cmdlist)
        
    elif cmd == 'discard weapon':
        
        if 'Faust' in mW:
            print("At the moment you have no weapons, only your fists.")
            return getcmd(cmdlist)
        elif 'Jonas Laserkanone' in mW:
            print("Jona's laser cannon short-circuited.")
            print("Jona will be very sad about this.")
            mW.remove('Jonas Laserkanone')
            mW.append('Faust')
            mG2.append('Jonas Laserkanone')
            mHP.remove(10)
            mHP.append(3)
            return getcmd(cmdlist)
        elif 'Rohr' in mW:
            print("The pipe breaks in two when discarded...")
            mW.remove('Rohr')
            mW.append('Faust')
            mG4.append('Rohr')
            mHP.remove(7)
            mHP.append(3)
            return getcmd(cmdlist)
        elif 'Monsterhunter' in mW:
            print("The Monsterhunter breaks when you put it down...")
            print("So much for the monster hunt...")
            mW.remove('Monsterhunter')
            mW.append('Faust')
            mG6.append('Monsterhunter')
            mHP.remove(30)
            mHP.append(3)
            return getcmd(cmdlist)
        elif 'Laserschwert' in mW:
            print("The sword breaks when you put it down...")
            mW.remove('Laserschwert')
            mW.append('Faust')
            mG7.append('Laserschwert')
            mHP.remove(15)
            mHP.append(3)
            return getcmd(cmdlist)
                
    elif cmd == 'quit':
        print("    ...terminating progress...")
        time.sleep(1)
        print("    (1) play again")
        print("    (2) quit")
    
        cmdlist = ['1', '2',]
        cmd = getcmd(cmdlist)
    
        if cmd == '1':
            print("    Game restarting")
            print("    ...")
            time.sleep(2)
            print("    ERROR OCCURRED")
            time.sleep(1)
            print("    EXIT")
            time.sleep(7)
            exit()
                
        elif cmd== '2':
            print("EXITZ")
            time.sleep(7)
            exit()
                
    else:
        time.sleep(0.2)
        print("\n...")
        time.sleep(0.2)
        print("You cannot do that here")
        time.sleep(0.2)
        print("...")
        time.sleep(0.2)
        print("In case you get stuck,")
        print("enter 'help' to get several input options")
        print()
        time.sleep(0.8)
        
        return getcmd(cmdlist)
    
if __name__ == "__main__":
    environment = ['service port']
    startBildschirm(environment)
