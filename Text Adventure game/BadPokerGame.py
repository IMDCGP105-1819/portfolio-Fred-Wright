import sys

print("Welcome back to the World Series Of Poker, I'm Lon McEachern and im here with Antonio Esfandiari")
print("Esfandiari: Hey")
print("And we are mere minutes away from finding out the final competitor to the main event, with the winner winning the illustrious WSOP bracelet")
print("During this session, there will only be the table consisting of these 2 players, tune in tomorrow night for that (next game)")
print("Esfandiari: Ive won 3 of them braclets and they're only collecting dust in a cabinet, they're here for that magical, life-changing fifteen million dollar payout")
print("Lon: Yes of course, the highest prize-pot in the history of the main event, from the huge 8 thousand plus entrants, we have already deterined 8 players on the final table.")
print("Esfandiari: Yeah, seriously strong set of players.")
print("We are here on the pinultimate table of the World Series Of Poker main event with only 2 contestents left, of course we have Mr Antoine Labat")
print("Esfandiari: Guy's come from from france with no real history, yet he's taken down some big dogs to get here, and would be only the third frenchamn to get to the main event.")
print("Lon: And he's up against...")
print("Your dad: Look, payday's already big, enough for some of your mom's treatment, you know it, I know it, but dont focus on that, everybody's already so proud of you, anything you do now, is just a bonus, Okay?")
print("You let out a strong but shakey, nervous breath.. ")
print("Your dad firmly places his hands on your shoulders, giving you a mild shake.")
print("Dad: What's your name!?")
name = str(input())
print("Do you know how to play poker!?")
Played_before = input()
while True:
    if Played_before == "yes":
        print("Good, because your here cause of how good you've played through this tournament.")
        print("MANAGER: TIME TO GO!")
        print("If ever you need my help, do: run hand through hair")
        print("i'll cough once to Fold, twice to Check/Call or three times to go big, you shouldnt need me though")
        print("Dont really know why we still have that camera on you, but whatever.")
        print("MANAGER: CAMERA'S ARE ROLLING, COME ON NOW!!")
        print(name,", You got this!")
        print("As you're walking away, your dad yells:")
        print("Im Proud of you son!")
        print("While walking through the back towards the poker table on stage, I walk up to you.")
        print("So, everything you can do is, chipcount, check, call, raise, which will lead to how much you wish to raise")
        print("all in, fold and RHTH, run hand through hair, to get some help")
        print("Try to enjoy")
        break
    if Played_before == "no":
        print("Your dad sigh's as if he's dissapointed")
        print("Clearly you've been relying on our cheating tactic's a little too much")
        print("MANAGER: TIME TO GO!")
        print("Right, when you play you hand and you don't know what to do, do: run hand through hair")
        print("i'll cough once to Fold, twice to Check/Call or three times to go big")
        print("That camera on you has helped quite alot through this journey, it still has its uses")
        print("if you do it too many times, someone may clock on, and we dont want that.")
        print("MANAGER: CAMERA'S ARE ROLLING, COME ON NOW!!")
        print(name, ", You got this!")
        print("As you're walking away, your dad yells:")
        print("Im Proud of you son!")
        print("While walking through the back towards the poker table on stage, I walk up to you.")
        print("Im sure you understand cards themselves, otherwise we have a big problem, google it")
        print("In poker, the aim is to reduce your opponents chips to 0, you do this by winning hands, at the start of each hand you are dealt 2 cards like 4♣ 9♦")
        print("The best 5 cards from your hand and the table are used.")
        print("Hand in order or worth from best to worst are Royal Flush: A♣ K♣ Q♣ J♣ 10♣, Straight flush J♣ 10♣ 9♣ 8♣ 7♣, Four of a kind: K♣ K♠ K♥ K♦ 10♦")
        print("Full house: K♦ K♠ K♥ 10♠ 10♥, Flush: A♥ 5♥ 6♥ 9♥ J♥, Straight: 5♥ 6♠ 7♠ 8♥ 9♦, Three of a kind: 5♥ 5♦ 5♠ 8♥ 9♦, Two pair: 4♣ 4♦ 7♠ K♠ K♠")
        print("One pair: 7♠ 7♣ 9♠ 10♣ K♠ and finally High Card: 2♥ 3♦ 6♣ 8♠ Q♣")
        print("Higher cards of the same value win hands, so a pair of Kings beat a pair of 10's")
        print("On each hand you can Fold, Check/Call or Raise/All in,")
        print("Fold means the hand ends and your opponents take the chips you've put in. Useful if you have a bad hand")
        print("Call means put in the same amount of chips as what the current highest amount is, or if none are in, then you can simply check.")
        print("Raise means increase the amount if chips others need to input to continue with the hand.")
        print("And all in... well means what it say's on the tin")
        print("You still following?")
        following = input()
        if following == "yes":
            print("Just checking, ha!, you see what i did there?... Ok.")
            print("The hand starts, you put in some chips then the flop comes, the first 3 cards, you then proceed")
            print("On the flop you could get a royal flush, highly unlikely but possible, if so, play like you only have a pair, and try to win as many chips as possible")
            print("Going All in straight away could scare opponents into folding, and you dont gain any chips")
            print("After the flop, there is the turn, another card, then the river, after it all plays out the player with the best hand wins.")
            print("The BabySteps feature is enable for if you need it, type !Help when prompted, but apparently your dad does some good advising... hmmm")
            print("So, everything you can do is, chipcount, check, call, raise, which will lead to how much you wish to raise")
            print("all in, fold and RHTH, run hand through hair, to get some help")
            break
        if following == "no":
            print("You're a lost cause, google it.")
            print("When you're done, come back")
            print("I'll enable the BabySteps feature during the first table vs Labat, if you're stuck or dont know what to do, type !Help when prompted")
            print("So, everything you can do is, chipcount, check, call, raise, which will lead to how much you wish to raise")
            print("all in, fold and RHTH, run hand through hair, to get some help")
            break
        else:
            print("What? A simple yes or no would do")
            following = input()
    else:
        print("I can tell you're nervous, you just mumbled, say that again?")
        Played_before = input()

Chipcount = 550000
labat_chips = 300000
dad_coughs = 0
A = "What would you like to do?"
if dad_coughs == 3:
    print("The security guard seems to pick up on your dads coughing")
if dad_coughs == 5:
    print("The security guard walks over to your dad, politely asking him to stop coughing")
if dad_coughs == 7:
    print("A switch seems to go off in the guards head, he calls over the MANAGER and proceeds to whisper in his ear")
    print("The manager looks at you, then at your dad, and squints his eyes, looking cautiously")
if dad_coughs == 9:
    print("The MANAGER walks over and shoves your cards to the dealer, the security guards graps a hold of you and chucks you out of the buidling")
    print("You had enough warnings. You dont get any payout for the tournament, your mum dies of cancer, all beacuse of you.")
    sys.exit(0)

print("Lon: And he's up against", name)
print("Esfandiari: Complete nobody, he's from England, has no competitive poker, say's he's playing for his sick mother but i dont buy it! ")
print("Probably a cover story for how he's been playing underground, racking up wins and needs a way to launder money")
print("Lon: Ha! You really do think the worst of people.")
print("Esfandiari: When you've been in the buisness as long as me, nothing suprises me anymore,")
print("Esfandiari: Some guy said he was playing for his grandma's funeral costs, but she was just on a holiday in the bahamas!")
print("Lon: 'sighs' Let's just get down to it, for the final place on the main event table its Antoine Labat versus", name, "!")
print("As you walk through the curtains, applause already fills the room, you wave to thank your newfound supporters, showing respect, you shake your opponents hand, and take your seat.")
print("You quickly do a stack count, you're on", Chipcount, "chips" "while he's on", labat_chips, "chips")
print("The applause dies down, minor talking fills the room, a hell of a lot better than silence, the dealer shuffles.")
print("WARNING: IF YOU INPUT WORDS WHEN PROMPTED FOR NUMBERS, VISE VERSA OR BE A GENERAL IDIOT, THIS GAME WILL BREAK.")
print("She announces the beginning of the game and proceeds to deal you and your opponent 2 cards.")
print("You take a deep breath in, exhale hard but silent, shuffle into your seat, notice the lights have dimmed from the audience in shine off the table")
print("Before you know it, you feel right at home.")
print("You look at your first hand, its a 4♣ 9♠, Labat raises to 30k, you fold immediately")
print("Oh boy...")
print("5 hands go by quickly, minor amounts get's raised between you and Labat, however it amasses to nothing")
print("you see the next hand to be 4♠ & 5♠")
print(A)
hand1 = input()
playing = True
hand1_stake = 5000
hand1_pot = 0
while playing ==  True:
    if hand1 == "fold":
        print("As there is nothing to lose, and all to gain, this is pointless")
        hand1 = input()
    if hand1 == "check" or hand1 == "call":
        print("Labat calmly puts in the Blind, not revealing anything.")
        Chipcount = Chipcount - hand1_stake
        labat_chips = labat_chips - hand1_stake
        hand1_pot = hand1_stake * 2
        break
    if hand1 == "raise":
        while playing == True:
        print("How much would you like to raise?")
        raise1 = int(input())
            if raise1 < 10000:
                print("Thats too low, lowest bet is 10000")
            if raise1 >= 10000 and raise1 < 100000:
                print("Labat calmly puts in the calls your raise, not revealing anything.")
                Chipcount = Chipcount - raise1
                labat_chips = labat_chips - raise1
                hand1_pot = raise1 * 2
                break
            if raise1 >= 100000 and raise1 < 200000:
                print("As you collect the chips and put them into the middle, a hush falls through the room.")
                print("Labat takes a few seconds to consider, arranges the chips needed to call, licks his lips and calls.")
                Chipcount = Chipcount - raise1
                labat_chips = labat_chips - raise1
                hand1_pot = raise1 * 2
                break
            if raise1 >= 200000 and raise1 < Chipcount:
                print("You grab the chips needed, a large stack, but you hear your dad cough a loud 2 coughs, maybe play things a little steadier")
                print(A)
                hand1 = input()
            if raise1 > Chipcount:
                print("You dont have that much chips to use, you have:", Chipcount)
                print(A)
                hand1 = input()
            if raise1 == Chipcount:
                print("You grab the chips needed, a large stack, but you hear your dad cough a loud 2 coughs, maybe play things a little steadier")
                print(A)
                hand1 = input()
            else:
                print("That is not a valid bet")
                print("What would you like to do?")
                hand1 = input()
        break
    if hand1 == "RHTH":
        print("Your dad coughs twice")
        print(A)
        hand1 = input()
        dad_coughs = dad_coughs + 1
    if hand1 == "AllIn":
        print("You grab all your chips, a large stack, but you hear your dad cough a loud 2 coughs, maybe play things a little steadier")
        print(A)
        hand1 = input()
    if hand1 == "chipcount":
        print(Chipcount)
        print(A)
        hand1 = input()
    if hand1 == "!Help":
       print("You have:", Chipcount, "Chips, id reccomend just calling as your hand is mediocre but has a lot of potential.")
       print("You can do: chipcount, check, call, raise, which will lead to how much you wish to raise, all in, fold !Help and run hand through hair")
       hand1 = input()
    else:
        print("Whats that? Type !Help if you're lost")
        hand1 = input()

print("The dealer put one card aside, and reveals the flop:")
print("|3♠||10♦||K♠|")
print("Labat takes his time carefully, but cautiously looking at the cards")
print("He proceeds to check.")
print("You have:", Chipcount, "Labat has:", labat_chips, "& the pot is:", hand1_pot)
print(A)
hand2 = input()
while playing ==  True:
    if hand2 == "fold":
        print("As there is nothing to lose, and all to gain, this is pointless")
        hand2 = input()
    if hand2 == "check" or hand2 == "call":
        print("The dealer puts one card away, and with no theatrical building, puts down..")
        print("The 9 of Spades!!!! A Flush!!!")
        print("Labat doesnt move, clearly in deep thought, after 30 seconds, he reaches for an amount of chips")
        print("Dealer: Raise 70 thousand.")
        labat_chips = labat_chips - 70000
        hand1_pot = hand1_pot + 70000
        print(A)
        hand3 = input()
        while playing ==  True:
            if hand3 == "fold":
                print("Folding a flush is a hard thing to do, however it seemingly must be done.")
                print("You throw your cards face down, he chooses to flip his cards face up, A pair of kings!")
                print("Your flush would have beat his kings, with the river left, your chances of winning were high, but its all in the past now.")
                print("Its the fist major hand, but as all hands pass, blinds will be raised to a point where you must go big or home.")
                labat_chips = labat_chips + hand1_pot
                hand1_pot = hand1_pot - hand1_pot
                break
            if hand3 == "raise":
                print("How much would you like to raise?")
                raise3 = int(input())
                while playing ==  True:
                    if raise3 <= 70000:
                        print("Thats too low, lowest bet is 70001")
                        raise3 = int(input())
                    if raise3 > 70000 and raise3 < 100000:
                        Chipcount = Chipcount - raise3
                        labat_chips = labat_chips - (raise3 - 70000)
                        hand1_pot = hand1_pot + ((raise3 * 2) - 70000)
                        if labat_chips < 100000:
                            print("You put", raise3, "chips to the middle, with your bet, Labat would be left with a small amount")
                            print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                            print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                            print("All in.")
                            print("You can either call or fold, and in a situation like this, no help can be given.")
                            print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise3), "to call.")
                            print(A)
                            handX = input()
                            while playing ==  True:
                                if handX == "call":
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Your father yells: Come on!")
                                    print("The room falls to silence as the dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips
                                    hand1_pot = hand1_pot + (labat_chips * 2)
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                                if handX == "fold":
                                    print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                    print("You throw your cards away and labat takes the big amount in the pot.")
                                    print("He also just throws away his cards not allowing you to see them")
                                    print("Dad: Your getting hasty son! This is your time!")
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    break
                                else:
                                    print("You cant do that")
                                    print(A)
                                    handX = input()
                            break
                        if labat_chips >= 100000:
                            print("Labat sees your weak re-raise, and capitalises immediately, he places 1 chip towards the middle and exclaims: All in.")
                            print("You can either call or fold, and in a situation like this, no help can be given.")
                            print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise3), "to call.")
                            print(A)
                            handX = input()
                            while playing ==  True:
                                if handX == "call":
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Your father yells: Come on!")
                                    print("The room falls to silence as the dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips
                                    hand1_pot = hand1_pot + (labat_chips * 2)
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                                if handX == "fold":
                                    print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                    print("You throw your cards away and labat takes the big amount in the pot.")
                                    print("He also just throws away his cards not allowing you to see them")
                                    print("Dad: Your getting hasty son! This is your time!")
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    break
                                else:
                                    print("You cant do that")
                                    print(A)
                                    handX = input()
                            break
                    if raise3 >= 100000 and raise3 < labat_chips:
                        Chipcount = Chipcount - raise3
                        labat_chips = labat_chips - (raise3 - 70000)
                        hand1_pot = hand1_pot + ((raise3 * 2) - 70000)
                        print("You put", raise3, "chips to the middle, with your bet, Labat would be left with a small amount")
                        print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                        print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                        print("All in.")
                        print("You can either call or fold, and in a situation like this, no help can be given.")
                        print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise3), "to call.")
                        print(A)
                        handX = input()
                        while playing ==  True:
                            if handX == "call":
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Your father yells: Come on!")
                                    print("The room falls to silence as the dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips
                                    hand1_pot = hand1_pot + (labat_chips * 2)
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                            if handX == "fold":
                                    print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                    print("You throw your cards away and labat takes the big amount in the pot.")
                                    print("He also just throws away his cards not allowing you to see them")
                                    print("Dad: Your getting hasty son! This is your time!")
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    break
                            else:
                                print("You cant do that")
                                print(A)
                                handX = input()
                        break
                    if raise3 == labat_chips:
                        print("You put", raise3, "chips to the middle, with your bet, Labat would be all in.")
                        print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                        print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                        print("All in.")
                        print("As per rules of the game, both players place down their hand.")
                        print("You place your 4♠ & 5♠, he places...")
                        print("K♥...")
                        print("K♦!!! A pair of kings, with a king on the board!?")
                        print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                        print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                        print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                        print("The room's silence has erupted, your father is shouting for the right card to come")
                        print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                        print("The dealer puts one card away, and with no theatrical building, puts down..")
                        print("The 9 of Spades!!!! A Flush!!!")
                        print("Your father lets out a roar and you let out a huge sigh")
                        print("The dealer puts another card away for the river...")
                        print("She puts down.. The three of hearts")
                        print("A full house.. 'Its alright", name, "You're still in this!")
                        Chipcount = Chipcount - (labat_chips + 70000)
                        hand1_pot = hand1_pot + ((labat_chips) * 2) + 70000
                        labat_chips = labat_chips - labat_chips
                        labat_chips = labat_chips + hand1_pot
                        print("You now have", Chipcount, "chips")
                        print("Labat now has", labat_chips, "chips")
                        print("Dad: Maybe going all in was not the best idea on the first main hand")
                        break
                    if raise3 > labat_chips:
                        print("Labat only has", labat_chips, "Please only bet and amount he can call.")
                        raise3 = int(input())
                    else:
                        print("Thats an invalid bet")
                        raise3 = int(input())
                break
            if hand3 == "check" or hand3 == "call":
                Chipcount = Chipcount - 70000
                hand1_pot = hand1_pot + 70000
                print("You take a while, thinking about the hand, after some time, place down the chips needed to call.")
                print("The dealer puts another card away for the river...")
                print("She puts down the three of hearts")
                print("The board is: |3♠||10♦||K♠||9♠||3♥|")
                print("Labat thinks long and hard, surveying the cards, 4 minutes pass")
                print("He puts a single chip into the middle and exclaims: All in")
                print("You can either call or fold, and in a situation like this, no help can be given.")
                print("You have", Chipcount, "Chips, and would need to put in", labat_chips, "to call.")
                print(A)
                handX = input()
                while playing ==  True:
                    if handX == "call":
                        print("As per rules of the game, both players place down their hand.")
                        print("You place your 4♠ & 5♠, he places...")
                        print("K♥...")
                        print("K♦!!! A pair of kings, with a king on the board!?")
                        print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                        print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                        print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                        print("The room's silence has erupted, your father is shouting for the right card to come")
                        print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                        print("The dealer puts one card away, and with no theatrical building, puts down..")
                        print("The 9 of Spades!!!! A Flush!!!")
                        print("Your father lets out a roar and you let out a huge sigh")
                        print("The dealer puts another card away for the river...")
                        print("She puts down.. The three of hearts")
                        print("A full house.. 'Its alright", name, "You're still in this!")
                        Chipcount = Chipcount - labat_chips
                        hand1_pot = hand1_pot + (labat_chips * 2)
                        labat_chips = labat_chips - labat_chips
                        labat_chips = labat_chips + hand1_pot
                        print("You now have", Chipcount, "chips")
                        print("Labat now has", labat_chips, "chips")
                        print("Dad: Maybe going all in was not the best idea on the first main hand")
                        break
                    if handX == "fold":
                        print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                        print("You throw your cards away and labat takes the big amount in the pot.")
                        print("He also just throws away his cards not allowing you to see them")
                        print("Dad: Your getting hasty son! This is your time!")
                        labat_chips = labat_chips + hand1_pot
                        print("You now have", Chipcount, "chips")
                        print("Labat now has", labat_chips, "chips")
                        break
                    else:
                        print("You cant do that")
                        print(A)
                        handX = input()
                break
            if hand3 == "RHTH":
                print("Your dad coughs three times")
                print(A)
                hand3 = input()
                dad_coughs = dad_coughs + 1
            if hand3 == "allin":
                print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                print("All in.")
                print("As per rules of the game, both players place down their hand.")
                print("You place your 4♠ & 5♠, he places...")
                print("K♥...")
                print("K♦!!! A pair of kings, with a king on the board!?")
                print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                print("The room's silence has erupted, your father is shouting for the right card to come")
                print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                print("The dealer puts one card away, and with no theatrical building, puts down..")
                print("The 9 of Spades!!!! A Flush!!!")
                print("Your father lets out a roar and you let out a huge sigh")
                print("The dealer puts another card away for the river...")
                print("She puts down.. The three of hearts")
                print("A full house.. 'Its alright", name, "You're still in this!")
                Chipcount = Chipcount - (labat_chips + 70000)
                hand1_pot = hand1_pot + ((labat_chips * 2) + 70000)
                labat_chips = labat_chips - labat_chips
                labat_chips = labat_chips + hand1_pot
                print("You now have", Chipcount, "chips")
                print("Labat now has", labat_chips, "chips")
                print("Dad: Maybe going all in was not the best idea on the first main hand")
                break
            if hand3 == "chipcount":
                print("You have:", Chipcount, "Chips and Labat has:", labat_chips, "chips.")
                print(A)
                hand3 = input()
            if hand3 == "!Help":
                print("You have:", Chipcount, "Chips, id reccomend Raising as you have a flush.")
                print("You can do: chipcount, check, call, raise, which will lead to how much you wish to raise, all in, fold !Help and run hand through hair")
                hand3 = input()
            else:
                print("Whats that? Type !Help if you're lost")
                hand3 = input()
        break
    if hand2 == "raise":
        print("How much would you like to raise?")
        raise2 = int(input())
        while playing ==  True:
            if raise2 < 10000:
                print("Thats too low, lowest bet is 10000")
                raise2 = int(input())
            if raise2 >= 10000 and raise2 < 100000:
                Chipcount = Chipcount - raise2
                labat_chips = labat_chips - raise2
                hand1_pot = hand1_pot + (raise2 * 2)
                if labat_chips < 100000:
                    print("You put", raise2, "chips to the middle, with your bet, Labat would be left with a small amount")
                    print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                    print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                    print("All in.")
                    print("You can either call or fold, and in a situation like this, no help can be given.")
                    print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise2), "to call.")
                    print(A)
                    handX = input()
                    while playing == True:
                        if handX == "call":
                            print("As per rules of the game, both players place down their hand.")
                            print("You place your 4♠ & 5♠, he places...")
                            print("K♥...")
                            print("K♦!!! A pair of kings, with a king on the board!?")
                            print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                            print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                            print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                            print("The room's silence has erupted, your father is shouting for the right card to come")
                            print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                            print("The dealer puts one card away, and with no theatrical building, puts down..")
                            print("The 9 of Spades!!!! A Flush!!!")
                            print("Your father lets out a roar and you let out a huge sigh")
                            print("The dealer puts another card away for the river...")
                            print("She puts down.. The three of hearts")
                            print("A full house.. 'Its alright", name, "You're still in this!")
                            Chipcount = Chipcount - labat_chips
                            hand1_pot = hand1_pot + (labat_chips * 2)
                            labat_chips = labat_chips - labat_chips
                            labat_chips = labat_chips + hand1_pot
                            print("You now have", Chipcount, "chips")
                            print("Labat now has", labat_chips, "chips")
                            print("Dad: Maybe going all in was not the best idea on the first main hand")
                            break
                        if handX == "fold":
                            print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                            print("You throw your cards away and labat takes the big amount in the pot.")
                            print("He also just throws away his cards not allowing you to see them")
                            print("Dad: Your getting hasty son! This is your time!")
                            labat_chips = labat_chips + hand1_pot
                            print("You now have", Chipcount, "chips")
                            print("Labat now has", labat_chips, "chips")
                            break
                        else:
                            print("You cant do that")
                            print(A)
                            handX = input()
                    break
                if labat_chips >= 100000:
                    print("Labat takes his time, but in the end, calls.")
                    print("The dealer puts one card away, and with no theatrical building, puts down..")
                    print("The 9 of Spades!!!! A Flush!!!")
                    print("Labat doesnt move, clearly in deep thought, after 30 seconds, he reaches for an amount of chips")
                    print("Dealer: Raise 70 thousand.")
                    labat_chips = labat_chips - 70000
                    hand1_pot = hand1_pot + 70000
                    print(A)
                    hand4 = input()
                    while playing == True:
                        if hand4 == "fold":
                            print("Folding a flush is a hard thing to do, however it seemingly must be done.")
                            print("You throw your cards face down, he chooses to flip his cards face up, A pair of kings!")
                            print("Your flush would hve beat his kings, with the river left, your chances of winning were high, but its all in the past now.")
                            print("Its the fist major hand, but as all hands pass, blinds will be raised to a point where you must go big or home.")
                            labat_chips = labat_chips + hand1_pot
                            hand1_pot = hand1_pot - hand1_pot
                            break
                        if hand4 == "raise":
                            print("How much would you like to raise?")
                            raise4 = int(input())
                            while playing == True:
                                if raise4 <= 70000:
                                    print("Thats too low, lowest bet is 70001")
                                    raise4 = int(input())
                                if raise4 > 70000 and raise4 < 100000:
                                    Chipcount = Chipcount - raise4
                                    labat_chips = labat_chips - (raise4 - 70000)
                                    hand1_pot = hand1_pot + ((raise4 * 2) - 70000)
                                    if labat_chips < 100000:
                                        print("You put", raise4, "chips to the middle, with your bet, Labat would be left with a small amount")
                                        print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                                        print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                                        print("All in.")
                                        print("You can either call or fold, and in a situation like this, no help can be given.")
                                        print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise4), "to call.")
                                        print(A)
                                        handX = input()
                                        while playing == True:
                                            if handX == "call":
                                                print("As per rules of the game, both players place down their hand.")
                                                print("You place your 4♠ & 5♠, he places...")
                                                print("K♥...")
                                                print("K♦!!! A pair of kings, with a king on the board!?")
                                                print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                                print("Your father yells: Come on!")
                                                print("The room falls to silence as the dealer puts another card away for the river...")
                                                print("She puts down.. The three of hearts")
                                                print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                                Chipcount = Chipcount - labat_chips
                                                hand1_pot = hand1_pot + (labat_chips * 2)
                                                labat_chips = labat_chips - labat_chips
                                                labat_chips = labat_chips + hand1_pot
                                                print("You now have", Chipcount, "chips")
                                                print("Labat now has", labat_chips, "chips")
                                                print("Dad: Maybe going all in was not the best idea on the first main hand")
                                                break
                                            if handX == "fold":
                                                print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                                print("You throw your cards away and labat takes the big amount in the pot.")
                                                print("He also just throws away his cards not allowing you to see them")
                                                print("Dad: Your getting hasty son! This is your time!")
                                                labat_chips = labat_chips + hand1_pot
                                                print("You now have", Chipcount, "chips")
                                                print("Labat now has", labat_chips, "chips")
                                                break
                                            else:
                                                print("You cant do that")
                                                print(A)
                                                handX = input()
                                    if labat_chips >= 100000:
                                        print("Labat sees your weak re-raise, and capitalises immediately, he places 1 chip towards the middle and exclaims: All in.")
                                        print("You can either call or fold, and in a situation like this, no help can be given.")
                                        print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise4), "to call.")
                                        print(A)
                                        handX = input()
                                        while playing ==  True:
                                            if handX == "call":
                                                print("As per rules of the game, both players place down their hand.")
                                                print("You place your 4♠ & 5♠, he places...")
                                                print("K♥...")
                                                print("K♦!!! A pair of kings, with a king on the board!?")
                                                print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                                print("Your father yells: Come on!")
                                                print("The room falls to silence as the dealer puts another card away for the river...")
                                                print("She puts down.. The three of hearts")
                                                print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                                Chipcount = Chipcount - labat_chips
                                                hand1_pot = hand1_pot + (labat_chips * 2)
                                                labat_chips = labat_chips - labat_chips
                                                labat_chips = labat_chips + hand1_pot
                                                print("You now have", Chipcount, "chips")
                                                print("Labat now has", labat_chips, "chips")
                                                print("Dad: Maybe going all in was not the best idea on the first main hand")
                                                break
                                            if handX == "fold":
                                                print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                                print("You throw your cards away and labat takes the big amount in the pot.")
                                                print("He also just throws away his cards not allowing you to see them")
                                                print("Dad: Your getting hasty son! This is your time!")
                                                labat_chips = labat_chips + hand1_pot
                                                print("You now have", Chipcount, "chips")
                                                print("Labat now has", labat_chips, "chips")
                                                break
                                            else:
                                                print("You cant do that")
                                                print(A)
                                                handX = input()
                                        break
                                if raise4 >= 100000 and raise4 < labat_chips:
                                    Chipcount = Chipcount - raise4
                                    labat_chips = labat_chips - (raise4 - 70000)
                                    hand1_pot = hand1_pot + ((raise4 * 2) - 70000)
                                    print("You put", raise4, "chips to the middle, with your bet, Labat would be left with a small amount")
                                    print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                                    print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                                    print("All in.")
                                    print("You can either call or fold, and in a situation like this, no help can be given.")
                                    print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise4), "to call.")
                                    print(A)
                                    handX = input()
                                    while playing ==  True:
                                        if handX == "call":
                                            print("As per rules of the game, both players place down their hand.")
                                            print("You place your 4♠ & 5♠, he places...")
                                            print("K♥...")
                                            print("K♦!!! A pair of kings, with a king on the board!?")
                                            print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                            print("Your father yells: Come on!")
                                            print("The room falls to silence as the dealer puts another card away for the river...")
                                            print("She puts down.. The three of hearts")
                                            print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                            Chipcount = Chipcount - labat_chips
                                            hand1_pot = hand1_pot + (labat_chips * 2)
                                            labat_chips = labat_chips - labat_chips
                                            labat_chips = labat_chips + hand1_pot
                                            print("You now have", Chipcount, "chips")
                                            print("Labat now has", labat_chips, "chips")
                                            print("Dad: Maybe going all in was not the best idea on the first main hand")
                                            break
                                        if handX == "fold":
                                            print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                            print("You throw your cards away and labat takes the big amount in the pot.")
                                            print("He also just throws away his cards not allowing you to see them")
                                            print("Dad: Your getting hasty son! This is your time!")
                                            labat_chips = labat_chips + hand1_pot
                                            print("You now have", Chipcount, "chips")
                                            print("Labat now has", labat_chips, "chips")
                                            break
                                        else:
                                            print("You cant do that")
                                            print(A)
                                            handX = input()
                                    break
                                if raise4 > labat_chips:
                                    print("You cant bet that amount as Labat only has", labat_chips, "chips.")
                                    raise4 = int(input())
                                if raise4 == labat_chips:
                                    print("You put", labat_chips, "chips to the middle")
                                    print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                                    print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                                    print("All in.")
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                                    print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                                    print("The room's silence has erupted, your father is shouting for the right card to come")
                                    print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                                    print("The dealer puts one card away, and with no theatrical building, puts down..")
                                    print("The 9 of Spades!!!! A Flush!!!")
                                    print("Your father lets out a roar and you let out a huge sigh")
                                    print("The dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. 'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips - 70000
                                    hand1_pot = hand1_pot + (labat_chips * 2) + 70000
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                                else:
                                    print("Thats an invalid bet")
                                    raise4 = int(input())
                            break
                        if hand4 == "check" or hand4 == "call":
                            Chipcount = Chipcount - 70000
                            hand1_pot = hand1_pot + 70000
                            print("You take a while, thinking about the hand, after some time, place down the chips needed to call.")
                            print("The dealer puts another card away for the river...")
                            print("She puts down the three of hearts")
                            print("The board is: |3♠||10♦||K♠||9♠||3♥|")
                            print("Labat thinks long and hard, surveying the cards, 4 minutes pass")
                            print("He puts a single chip into the middle and exclaims: All in")
                            print("You can either call or fold, and in a situation like this, no help can be given.")
                            print("You have", Chipcount, "Chips, and would need to put in", (labat_chips), "to call.")
                            print(A)
                            handX = input()
                            while playing ==  True:
                                if handX == "call":
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                                    print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                                    print("The room's silence has erupted, your father is shouting for the right card to come")
                                    print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                                    print("The dealer puts one card away, and with no theatrical building, puts down..")
                                    print("The 9 of Spades!!!! A Flush!!!")
                                    print("Your father lets out a roar and you let out a huge sigh")
                                    print("The dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. 'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips
                                    hand1_pot = hand1_pot + (labat_chips * 2)
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                                if handX == "fold":
                                    print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                    print("You throw your cards away and labat takes the big amount in the pot.")
                                    print("He also just throws away his cards not allowing you to see them")
                                    print("Dad: Your getting hasty son! This is your time!")
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    break
                                else:
                                    print("You cant do that")
                                    print(A)
                                    handX = input()
                            break
                        if hand4 == "RHTH":
                            print("Your dad coughs three times")
                            print(A)
                            hand4 = input()
                        if hand4 == "allin":
                            print("You put", labat_chips, "chips to the middle")
                            print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                            print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                            print("All in.")
                            print("As per rules of the game, both players place down their hand.")
                            print("You place your 4♠ & 5♠, he places...")
                            print("K♥...")
                            print("K♦!!! A pair of kings, with a king on the board!?")
                            print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                            print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                            print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                            print("The room's silence has erupted, your father is shouting for the right card to come")
                            print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                            print("The dealer puts one card away, and with no theatrical building, puts down..")
                            print("The 9 of Spades!!!! A Flush!!!")
                            print("Your father lets out a roar and you let out a huge sigh")
                            print("The dealer puts another card away for the river...")
                            print("She puts down.. The three of hearts")
                            print("A full house.. 'Its alright", name, "You're still in this!")
                            Chipcount = Chipcount - labat_chips - 70000
                            hand1_pot = hand1_pot + (labat_chips * 2) + 70000
                            labat_chips = labat_chips - labat_chips
                            labat_chips = labat_chips + hand1_pot
                            print("You now have", Chipcount, "chips")
                            print("Labat now has", labat_chips, "chips")
                            print("Dad: Maybe going all in was not the best idea on the first main hand")
                            break
                        if hand4 == "chipcount":
                            print("You have:", Chipcount, "Chips")
                            print(A)
                            hand4 = input()
                        if hand4 == "!Help":
                            print("You have:", Chipcount, "Chips, id reccomend Raising as you have a flush.")
                            print("You can do: chipcount, check, call, raise, which will lead to how much you wish to raise, all in, fold !Help and run hand through hair")
                            hand4 = input()
                        else:
                            print("Whats that? Type !Help if you're lost")
                            hand4 = input()        #
                    break
            if raise2 > labat_chips:
                print("Labat only has", labat_chips, "Please only bet and amount he can call.")
                print(A)
                raise2 = int(input())
            if raise2 >= 100000 and raise2 < 200000:
                Chipcount = Chipcount - raise2
                labat_chips = labat_chips - raise2
                hand1_pot = hand1_pot + (raise2 * 2)
                if labat_chips < 100000:
                    print("You put", raise2, "chips to the middle, with your bet, Labat would be left with a small amount")
                    print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                    print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                    print("All in.")
                    print("You can either call or fold, and in a situation like this, no help can be given.")
                    print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise2), "to call.")
                    print(A)
                    handX = input()
                    while playing ==  True:
                        if handX == "call":
                            print("As per rules of the game, both players place down their hand.")
                            print("You place your 4♠ & 5♠, he places...")
                            print("K♥...")
                            print("K♦!!! A pair of kings, with a king on the board!?")
                            print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                            print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                            print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                            print("The room's silence has erupted, your father is shouting for the right card to come")
                            print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                            print("The dealer puts one card away, and with no theatrical building, puts down..")
                            print("The 9 of Spades!!!! A Flush!!!")
                            print("Your father lets out a roar and you let out a huge sigh")
                            print("The dealer puts another card away for the river...")
                            print("She puts down.. The three of hearts")
                            print("A full house.. 'Its alright", name, "You're still in this!")
                            Chipcount = Chipcount - labat_chips
                            hand1_pot = hand1_pot + (labat_chips * 2)
                            labat_chips = labat_chips - labat_chips
                            labat_chips = labat_chips + hand1_pot
                            print("You now have", Chipcount, "chips")
                            print("Labat now has", labat_chips, "chips")
                            print("Dad: Maybe going all in was not the best idea on the first main hand")
                            break
                        if handX == "fold":
                            print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                            print("You throw your cards away and labat takes the big amount in the pot.")
                            print("He also just throws away his cards not allowing you to see them")
                            print("Dad: Your getting hasty son! This is your time!")
                            labat_chips = labat_chips + hand1_pot
                            print("You now have", Chipcount, "chips")
                            print("Labat now has", labat_chips, "chips")
                            break
                        else:
                            print("You cant do that")
                            print(A)
                            handX = input()
                    break
                if labat_chips >= 100000:
                    print("Labat takes a long while, but in the end, calls.")
                    print("The dealer puts one card away, and with no theatrical building, puts down..")
                    print("The 9 of Spades!!!! A Flush!!!")
                    print("Labat doesnt move, clearly in deep thought, after 30 seconds, he reaches for an amount of chips")
                    print("Dealer: Raise 70 thousand.")
                    labat_chips = labat_chips - 70000
                    hand1_pot = hand1_pot + 70000
                    print(A)
                    hand5 = input()
                    while playing ==  True:
                        if hand5 == "fold":
                            print("Folding a flush is a hard thing to do, however it seemingly must be done.")
                            print("You throw your cards face down, he chooses to flip his cards face up, A pair of kings!")
                            print("Your flush would hve beat his kings, with the river left, your chances of winning were high, but its all in the past now.")
                            print("Its the fist major hand, but as all hands pass, blinds will be raised to a point where you must go big or home.")
                            labat_chips = labat_chips + hand1_pot
                            hand1_pot = hand1_pot - hand1_pot
                            break
                        if hand5 == "raise":
                            print("How much would you like to raise?")
                            raise5 = int(input())
                            while playing ==  True:
                                if raise5 <= 70000:
                                    print("Thats too low, lowest bet is 70001")
                                    raise5 = int(input())
                                if raise5 > 70000 and raise5 < 100000:
                                    Chipcount = Chipcount - raise5
                                    labat_chips = labat_chips - (raise5 - 70000)
                                    hand1_pot = hand1_pot + (raise5 * 2)
                                    if labat_chips < 100000:
                                            print("You put", raise5, "chips to the middle, with your bet, Labat would be left with a small amount")
                                            print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                                            print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                                            print("All in.")
                                            print("You can either call or fold, and in a situation like this, no help can be given.")
                                            print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise5), "to call.")
                                            print(A)
                                            handX = input()
                                            while playing ==  True:
                                                if handX == "call":
                                                    print("As per rules of the game, both players place down their hand.")
                                                    print("You place your 4♠ & 5♠, he places...")
                                                    print("K♥...")
                                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                                    print("Your father yells: Come on!")
                                                    print("The room falls to silence as the dealer puts another card away for the river...")
                                                    print("She puts down.. The three of hearts")
                                                    print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                                    Chipcount = Chipcount - labat_chips
                                                    hand1_pot = hand1_pot + ((labat_chips * 2) - 70000)
                                                    labat_chips = labat_chips - labat_chips
                                                    labat_chips = labat_chips + hand1_pot
                                                    print("You now have", Chipcount, "chips")
                                                    print("Labat now has", labat_chips, "chips")
                                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                                    break
                                                if handX == "fold":
                                                    print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                                    print("You throw your cards away and labat takes the big amount in the pot.")
                                                    print("He also just throws away his cards not allowing you to see them")
                                                    print("Dad: Your getting hasty son! This is your time!")
                                                    labat_chips = labat_chips + hand1_pot
                                                    print("You now have", Chipcount, "chips")
                                                    print("Labat now has", labat_chips, "chips")
                                                    break
                                                else:
                                                    print("You cant do that")
                                                    print(A)
                                                    handX = input()
                                            break
                                    if labat_chips >= 100000:
                                        print("Labat sees your weak re-raise, and capitalises immediately, he places 1 chip towards the middle and exclaims: All in.")
                                        print("You can either call or fold, and in a situation like this, no help can be given.")
                                        print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise5), "to call.")
                                        print(A)
                                        handX = input()
                                        while playing ==  True:
                                            if handX == "call":
                                                print("As per rules of the game, both players place down their hand.")
                                                print("You place your 4♠ & 5♠, he places...")
                                                print("K♥...")
                                                print("K♦!!! A pair of kings, with a king on the board!?")
                                                print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                                print("Your father yells: Come on!")
                                                print("The room falls to silence as the dealer puts another card away for the river...")
                                                print("She puts down.. The three of hearts")
                                                print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                                Chipcount = Chipcount - labat_chips
                                                hand1_pot = hand1_pot + (labat_chips * 2)
                                                labat_chips = labat_chips - labat_chips
                                                labat_chips = labat_chips + hand1_pot
                                                print("You now have", Chipcount, "chips")
                                                print("Labat now has", labat_chips, "chips")
                                                print("Dad: Maybe going all in was not the best idea on the first main hand")
                                            if handX == "fold":
                                                print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                                print("You throw your cards away and labat takes the big amount in the pot.")
                                                print("He also just throws away his cards not allowing you to see them")
                                                print("Dad: Your getting hasty son! This is your time!")
                                                labat_chips = labat_chips + hand1_pot
                                                print("You now have", Chipcount, "chips")
                                                print("Labat now has", labat_chips, "chips")
                                            else:
                                                print("You cant do that")
                                                print(A)
                                                handX = input()
                                        break
                                if raise5 >= 100000 and raise5 <= labat_chips:
                                    Chipcount = Chipcount - raise5
                                    hand1_pot = hand1_pot + raise5 + (raise5 - 70000)
                                    labat_chips = labat_chips - (raise5 - 70000)
                                    print("You put", raise5, "chips to the middle, with your bet, Labat would be left with a small amount")
                                    print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                                    print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                                    print("All in.")
                                    print("You can either call or fold, and in a situation like this, no help can be given.")
                                    print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise5), "to call.")
                                    print(A)
                                    handX = input()
                                    while playing ==  True:
                                        if handX == "call":
                                            print("As per rules of the game, both players place down their hand.")
                                            print("You place your 4♠ & 5♠, he places...")
                                            print("K♥...")
                                            print("K♦!!! A pair of kings, with a king on the board!?")
                                            print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                            print("Your father yells: Come on!")
                                            print("The room falls to silence as the dealer puts another card away for the river...")
                                            print("She puts down.. The three of hearts")
                                            print("A full house.. Labat wins. Dad:'Its alright", name, "You're still in this!")
                                            Chipcount = Chipcount - labat_chips
                                            hand1_pot = hand1_pot + (labat_chips * 2)
                                            labat_chips = labat_chips - labat_chips
                                            labat_chips = labat_chips + hand1_pot
                                            print("You now have", Chipcount, "chips")
                                            print("Labat now has", labat_chips, "chips")
                                            print("Dad: Maybe going all in was not the best idea on the first main hand")
                                            break
                                        if handX == "fold":
                                            print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                            print("You throw your cards away and labat takes the big amount in the pot.")
                                            print("He also just throws away his cards not allowing you to see them")
                                            print("Dad: Your getting hasty son! This is your time!")
                                            labat_chips = labat_chips + hand1_pot
                                            print("You now have", Chipcount, "chips")
                                            print("Labat now has", labat_chips, "chips")
                                            break
                                        else:
                                            print("You cant do that")
                                            print(A)
                                            handX = input()
                                    break
                                if raise5 > labat_chips:
                                    print("Labat only has", labat_chips, "Please only bet an amount he can call.")
                                    raise5 = int(input())
                                if raise5 == labat_chips:
                                    print("You put", labat_chips, "chips to the middle")
                                    print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                                    print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                                    print("All in.")
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                                    print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                                    print("The room's silence has erupted, your father is shouting for the right card to come")
                                    print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                                    print("The dealer puts one card away, and with no theatrical building, puts down..")
                                    print("The 9 of Spades!!!! A Flush!!!")
                                    print("Your father lets out a roar and you let out a huge sigh")
                                    print("The dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. 'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips - 70000
                                    hand1_pot = hand1_pot + (labat_chips * 2) + 70000
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                                else:
                                    print("Thats an invalid bet")
                                    raise4 = int(input())
                            break
                        if hand5 == "check" or hand5 == "call":
                            Chipcount = Chipcount - 70000
                            hand1_pot = hand1_pot + 70000
                            print("You take a while, thinking about the hand, after some time, place down the chips needed to call.")
                            print("The dealer puts another card away for the river...")
                            print("She puts down the three of hearts")
                            print("The board is: |3♠||10♦||K♠||9♠||3♥|")
                            print("Labat thinks long and hard, surveying the cards, 4 minutes pass")
                            print("He puts a single chip into the middle and exclaims: All in")
                            print("You can either call or fold, and in a situation like this, no help can be given.")
                            print("You have", Chipcount, "Chips, and would need to put in", labat_chips, "to call.")
                            print(A)
                            handX = input()
                            while playing ==   True:
                                if handX == "call":
                                    print("As per rules of the game, both players place down their hand.")
                                    print("You place your 4♠ & 5♠, he places...")
                                    print("K♥...")
                                    print("K♦!!! A pair of kings, with a king on the board!?")
                                    print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                                    print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                                    print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                                    print("The room's silence has erupted, your father is shouting for the right card to come")
                                    print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                                    print("The dealer puts one card away, and with no theatrical building, puts down..")
                                    print("The 9 of Spades!!!! A Flush!!!")
                                    print("Your father lets out a roar and you let out a huge sigh")
                                    print("The dealer puts another card away for the river...")
                                    print("She puts down.. The three of hearts")
                                    print("A full house.. 'Its alright", name, "You're still in this!")
                                    Chipcount = Chipcount - labat_chips
                                    hand1_pot = hand1_pot + (labat_chips * 2)
                                    labat_chips = labat_chips - labat_chips
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    print("Dad: Maybe going all in was not the best idea on the first main hand")
                                    break
                                if handX == "fold":
                                    print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                                    print("You throw your cards away and labat takes the big amount in the pot.")
                                    print("He also just throws away his cards not allowing you to see them")
                                    print("Dad: Your getting hasty son! This is your time!")
                                    labat_chips = labat_chips + hand1_pot
                                    print("You now have", Chipcount, "chips")
                                    print("Labat now has", labat_chips, "chips")
                                    break
                                else:
                                    print("You cant do that")
                                    print(A)
                                    handX = input()
                            break
                        if hand5 == "RHTH":
                            print("Your dad coughs three times")
                            print(A)
                            hand5 = input()
                            dad_coughs = dad_coughs + 1
                        if hand5 == "allin":
                            print("You put", labat_chips, "chips to the middle, with your bet, Labat would be all in.")
                            print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                            print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                            print("All in.")
                            print("As per rules of the game, both players place down their hand.")
                            print("You place your 4♠ & 5♠, he places...")
                            print("K♥...")
                            print("K♦!!! A pair of kings, with a king on the board!?")
                            print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                            print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                            print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                            print("The room's silence has erupted, your father is shouting for the right card to come")
                            print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                            print("The dealer puts one card away, and with no theatrical building, puts down..")
                            print("The 9 of Spades!!!! A Flush!!!")
                            print("Your father lets out a roar and you let out a huge sigh")
                            print("The dealer puts another card away for the river...")
                            print("She puts down.. The three of hearts")
                            print("A full house.. 'Its alright", name, "You're still in this!")
                            Chipcount = Chipcount - labat_chips - 70000
                            hand1_pot = hand1_pot + (labat_chips * 2) + 70000
                            labat_chips = labat_chips - labat_chips
                            labat_chips = labat_chips + hand1_pot
                            print("You now have", Chipcount, "chips")
                            print("Labat now has", labat_chips, "chips")
                            print("Dad: Maybe going all in was not the best idea on the first main hand")
                            break
                        if hand5 == "chipcount":
                            print("You have:", Chipcount, "Chips and Labat has:", labat_chips, "chips.")
                            print(A)
                            hand5 = input()
                        if hand5 == "!Help":
                            print("You have:", Chipcount, "Chips, id reccomend Raising as you have a flush.")
                            print("You can do: chipcount, check, call, raise, which will lead to how much you wish to raise, all in, fold !Help and run hand through hair")
                            hand5 = input()
                        else:
                            print("Whats that? Type !Help if you're lost")
                            hand5 = input()
                    break
            if raise2 >= 200000 and raise2 < labat_chips:
                print("You put", raise2, "chips to the middle, with your bet, Labat would be left with a small amount")
                print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                print("All in.")
                print("You can either call or fold, and in a situation like this, no help can be given.")
                print("You have", Chipcount, "Chips, and would need to put in", (labat_chips - raise2), "to call.")
                print(A)
                handX = input()
                while playing == True:
                    if handX == "call":
                        print("As per rules of the game, both players place down their hand.")
                        print("You place your 4♠ & 5♠, he places...")
                        print("K♥...")
                        print("K♦!!! A pair of kings, with a king on the board!?")
                        print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                        print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                        print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                        print("The room's silence has erupted, your father is shouting for the right card to come")
                        print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                        print("The dealer puts one card away, and with no theatrical building, puts down..")
                        print("The 9 of Spades!!!! A Flush!!!")
                        print("Your father lets out a roar and you let out a huge sigh")
                        print("The dealer puts another card away for the river...")
                        print("She puts down.. The three of hearts")
                        print("A full house.. 'Its alright", name, "You're still in this!")
                        Chipcount = Chipcount - labat_chips
                        hand1_pot = hand1_pot + (labat_chips * 2)
                        labat_chips = labat_chips - labat_chips
                        labat_chips = labat_chips + hand1_pot
                        print("You now have", Chipcount, "chips")
                        print("Labat now has", labat_chips, "chips")
                        print("Dad: Maybe going all in was not the best idea on the first main hand")
                        break
                    if handX == "fold":
                        print("You wait a few minutes, pretending to hmm and arr, however this is just to unease Labat")
                        print("You throw your cards away and labat takes the big amount in the pot.")
                        print("He also just throws away his cards not allowing you to see them")
                        print("Dad: Your getting hasty son! This is your time!")
                        labat_chips = labat_chips + hand1_pot
                        print("You now have", Chipcount, "chips")
                        print("Labat now has", labat_chips, "chips")
                        break
                    else:
                        print("You cant do that")
                        print(A)
                        handX = input()
                break
            if raise2 == labat_chips:
                print("You put", raise2, "chips to the middle, with your bet, Labat would be all in.")
                print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
                print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
                print("All in.")
                print("As per rules of the game, both players place down their hand.")
                print("You place your 4♠ & 5♠, he places...")
                print("K♥...")
                print("K♦!!! A pair of kings, with a king on the board!?")
                print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
                print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
                print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
                print("The room's silence has erupted, your father is shouting for the right card to come")
                print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
                print("The dealer puts one card away, and with no theatrical building, puts down..")
                print("The 9 of Spades!!!! A Flush!!!")
                print("Your father lets out a roar and you let out a huge sigh")
                print("The dealer puts another card away for the river...")
                print("She puts down.. The three of hearts")
                print("A full house.. 'Its alright", name, "You're still in this!")
                Chipcount = Chipcount - labat_chips
                hand1_pot = hand1_pot + (labat_chips * 2)
                labat_chips = labat_chips - labat_chips
                labat_chips = labat_chips + hand1_pot
                print("You now have", Chipcount, "chips")
                print("Labat now has", labat_chips, "chips")
                print("Dad: Maybe going all in was not the best idea on the first main hand")
                break
            else:
                print("That is not a valid bet")
                raise2 = int(input())
        break
    if hand2 == "RHTH":
        print("Your dad coughs twice")
        print(A)
        hand2 = input()
        dad_coughs = dad_coughs + 1
    if hand2 == "all in":
        print("Labat thinks for a while, seemingly an eternety, he grabs a single $1000 chip")
        print("He twiddles with it through his fingers and thumbs, he places it on the table and says:")
        print("All in.")
        print("As per rules of the game, both players place down their hand.")
        print("You place your 4♠ & 5♠, he places...")
        print("K♥...")
        print("K♦!!! A pair of kings, with a king on the board!?")
        print("Esfandiari: A Huge moment in the game! And we're only a couple of hands in!")
        print("Lon: Theres a 73% Chance Labat comes home with it, doubling his chip count and putting himself in a commanding position!")
        print("Esfandiari:But of course", name, "can win! Ive seen alot worse odds, he should still feel good about himself!")
        print("The room's silence has erupted, your father is shouting for the right card to come")
        print("Both you and Labat are out of your chairs, you shake his hand and look down, hoping for anything.")
        print("The dealer puts one card away, and with no theatrical building, puts down..")
        print("The 9 of Spades!!!! A Flush!!!")
        print("Your father lets out a roar and you let out a huge sigh")
        print("The dealer puts another card away for the river...")
        print("She puts down.. The three of hearts")
        print("A full house.. 'Its alright", name, "You're still in this!")
        Chipcount = Chipcount - labat_chips
        hand1_pot = hand1_pot + (labat_chips * 2)
        labat_chips = labat_chips - labat_chips
        labat_chips = labat_chips + hand1_pot
        break
    if hand2 == "chipcount":
        print(Chipcount)
        print(A)
        hand2 = input()
    if hand2 == "!Help":
        print("You have:", Chipcount, "Chips, id reccomend just calling as your hand is mediocre but has a lot of potential.")
        print("You can do: chipcount, check, call, raise, which will lead to how much you wish to raise, all in, fold !Help and run hand through hair")
        hand2 = input()
    else:
        print("Whats that? Type !Help if you're lost")
        hand2 = input()

print(Chipcount, labat_chips)


if Chipcount < 300000:
    print("Esfandiari: Its been a bad start for", name, "Labat with one good hand, and a little bit of luck asserts a 300k lead.")
    labat_chips = 475000
    Chipcount = 375000
    print("Lon: Yes however dont count", name, "out, we said before that both these players have taken down big players to get here, however", name, "i believe has that better track record.")
    print("Esfandiari: Im prosuming you're talking about that nasty bluff against Phil Ivey, trip ace's versus a pair of 2's!", name, "has got balls, no doubt")
    print("Lon: I was reffering to when he knocked you out with the strai-")
    print("Esfandiari: Shutup! I would rather not relive that terrible experience.")
    print("Lon: Ha! Well we are back after 2 hours 30 of close action, after a few decent hands for", name, "he's back to only being 100k behind")
if Chipcount >= 300000 and Chipcount < 450000:
    print("Esfandiari: Its been a alright start for", name, "Now both are moderately even in this showdown.")
    print("And i think", name, "has it in him to do this.")
    print("Lon: Yes however dont count Labat out, we said before that both these players have taken down big players to get here, however Labat i believe has that better track record.")
    print("Esfandiari: Im prosuming you're talking about that nasty bluff against Phil Ivey, trip ace's versus a pair of 2's! Labat has got balls, no doubt")
    print("Lon: Theres also", name, "Who knocked you out with the strai-")
    print("Esfandiari: Shutup! I would rather not relive that terrible experience.")
    print("Lon: Ha! Well we are back after 2 hours 30 of close action, after a few decent hands for", name, "he's now take a minor lead of 50k")
    Chipcount = 450000
    labat_chips = 400000
if Chipcount >= 450000:
    Chipcount = 575000
    labat_chips = 275000
    print("Esfandiari: Its been a good start for", name, "Getting out of the first major hand is a skill all great players need")
    print("And i think", name, "has it in him to do this.")
    print("Lon: Yes however dont count Labat out, we said before that both these players have taken down big players to get here, however Labat i believe has that better track record.")
    print("Esfandiari: Im prosuming you're talking about that nasty bluff against Phil Ivey, trip ace's versus a pair of 2's! Labat has got balls, no doubt")
    print("Lon: I was reffering to when he knocked you out with the strai-")
    print("Esfandiari: Shutup! I would rather not relive that terrible experience.")
    print("Lon: Ha! Well we are back after 2 hours 30 of close action, after a few decent hands for", name, "he's now take a commanding lead of 300k")

print("We now resume the action.")
print("With a couple of good hands, you feel momentum is now on your side, lets see if the next hand can convert it.")
print("The dealer shuffles, passing both you and Labat 2 cards, you reveal them to be:")
print("Q♠ & Q♦")
print(A)
hand1 = input()
labat_chips = labat_chips - 25000
Chipcount = Chipcount - 25000
hand2pot = 50000
while playing == True:
    pre-flop
    if hand1 == "fold":
        unable
    if hand1 == "check" or hand1 == "call":
        flop
        hand2 = input()
        while playing == True:
            if hand2 == "fold":
                unable
            if hand2 == "check" or hand2 == "call":
                turn
                hand3 = input()
                while playing == True:
                    if hand3 == "fold":
                        unable
                    if hand3 == "check" or hand3 == "call":
                        river
                        hand4 = input()
                        while playing == True:
                            if hand4 == "fold":
                                unable
                            if hand4 == "check" or hand4 == "call":
                                allin
                            if hand4 == "raise":
                                raise1 = int(input())
                                while playing == True:
                                    if raise1 < 10000:
                                        no
                                    if raise1 >= 10000 and raise1 < 100000:
                                        if labat_chips < 100000:
                                            k
                                        if labat_chips >= 100000:
                                            k
                                    if raise1 >= 100000 and raise1 < 200000:
                                        if labat_chips < 100000:
                                            k
                                        if labat_chips >= 100000:
                                            k
                                    if raise1 >= 200000 and raise1 < labat_chips:
                                        fold
                                    if raise1 > labat_chips:
                                        no
                                    if raise1 == labat_chips:
                                        allin
                                    else:
                                        print("Please place a valid bet")
                                        raise1 = int(input())
                                break
                            if hand4 == "RHTH":
                                p
                            if hand4 == "AllIn":
                                z
                            if hand4 == "chipcount":
                                z
                            if hand4 == "!Help":
                                z
                            else:
                                print("Whats that? Type !Help if you're lost")
                                hand4 = input()
                        break
                    if hand3 == "raise":
                        raise2 = int(input())
                        while playing == True:
                            if raise2 < 10000:
                                no
                            if raise2 >= 10000 and raise2 < 100000:
                                if labat_chips < 100000:
                                    k
                                if labat_chips >= 100000:
                                    calls
                                    river
                                    hand5 = input()
                                    while playing == True:
                                        if hand5 == "fold":
                                            unable
                                        if hand5 == "check" or hand5 == "call":
                                            ok
                                        if hand5 == "raise":
                                            raise3 = int(input())
                                            while playing == True:
                                                if raise3 < 10000:
                                                    no
                                                if raise3 >= 10000 and raise3 < 100000:
                                                    if labat_chips < 100000:
                                                        k
                                                    if labat_chips >= 100000:
                                                        k
                                                if raise3 >= 100000 and raise3 < 200000:
                                                    if labat_chips < 100000:
                                                        k
                                                    if labat_chips >= 100000:
                                                        k
                                                if raise3 >= 200000 and raise3 < labat_chips:
                                                    fold
                                                if raise3 > labat_chips:
                                                    no
                                                if raise3 == labat_chips:
                                                    allin
                                                else:
                                                    print("Please place a valid bet")
                                                    raise3 = int(input())
                                            break
                                        if hand5 == "RHTH":
                                            p
                                        if hand5 == "AllIn":
                                            z
                                        if hand5 == "chipcount":
                                            z
                                        if hand5 == "!Help":
                                            z
                                        else:
                                            print("Whats that? Type !Help if you're lost")
                                            hand5 = input()
                                    break
                            if raise2 >= 100000 and raise2 < 200000:
                                if labat_chips < 100000:
                                    k
                                if labat_chips >= 100000:
                                    calls
                                    river
                                    hand6 = input()
                                    while playing == True:
                                        if hand6 == "fold":
                                            unable
                                        if hand6 == "check" or hand6 == "call":
                                            ok
                                        if hand6 == "raise":
                                            raise4 = int(input())
                                            while playing == True:
                                                if raise4 < 10000:
                                                    no
                                                if raise4 >= 10000 and raise4 < 100000:
                                                    if labat_chips < 100000:
                                                        k
                                                    if labat_chips >= 100000:
                                                        k
                                                if raise4 >= 100000 and raise4 < 200000:
                                                    if labat_chips < 100000:
                                                        k
                                                    if labat_chips >= 100000:
                                                        k
                                                if raise4 >= 200000 and raise4 < labat_chips:
                                                    fold
                                                if raise4 > labat_chips:
                                                    no
                                                if raise4 == labat_chips:
                                                    allin
                                                else:
                                                    print("Please place a valid bet")
                                                    raise4 = int(input())
                                            break
                                        if hand6 == "RHTH":
                                            p
                                        if hand6 == "AllIn":
                                            z
                                        if hand6 == "chipcount":
                                            z
                                        if hand6 == "!Help":
                                            z
                                        else:
                                            print("Whats that? Type !Help if you're lost")
                                            hand6 = input()
                                    break
                            if raise2 >= 200000 and raise2 < labat_chips:
                                fold
                            if raise2 > labat_chips:
                                no
                            if raise2 == labat_chips:
                                allin
                            else:
                                print("Please place a valid bet")
                                raise2 = int(input())
                        break
                    if hand3 == "RHTH":
                        p
                    if hand3 == "AllIn":
                        z
                    if hand3 == "chipcount":
                        z
                    if hand3 == "!Help":
                        z
                    else:
                        print("Whats that? Type !Help if you're lost")
                        hand3 = input()
                break
            if hand2 == "raise":
                raise5 = int(input())
                while playing == True:
                    if raise5 < 10000:
                        no
                    if raise5 >= 10000 and raise5 < 100000:
                        if labat_chips < 100000:
                            k
                        if labat_chips >= 100000:
                            k
                    if raise5 >= 100000 and raise5 < 200000:
                        if labat_chips < 100000:
                            k
                        if labat_chips >= 100000:
                            k
                    if raise5 >= 200000 and raise5 < labat_chips:
                        fold
                    if raise5 > labat_chips:
                        no
                    if raise5 == labat_chips:
                        allin
                    else:
                        print("Please place a valid bet")
                        raise1 = int(input())
                break
            if hand2 == "RHTH":
                p
            if hand2 == "AllIn":
                z
            if hand2 == "chipcount":
                z
            if hand2 == "!Help":
                z
            else:
                print("Whats that? Type !Help if you're lost")
                hand2 = input()
        break
    if hand1 == "raise":
        if raise = 70k:
        raise6 = int(input())
        while playing == True:
            if raise6 < 10000:
                no
            if raise6 >= 10000 and raise6 < 125000:
                if labat_chips < 100000:
                    k
                if labat_chips >= 100000:
                    flop
                    hand7 = input()
                    while playing == True:
                        if hand7 == "fold":
                            unable
                        if hand7 == "check" or hand7 == "call":
                            turn
                            hand8 = input()
                            while playing == True:
                                if hand8 == "fold":
                                    unable
                                if hand8 == "check" or hand8 == "call":
                                    allin
                                if hand8 == "raise":
                                    raise7 = int(input())
                                    while playing == True:
                                        if raise7 < 10000:
                                            no
                                        if raise7 >= 10000 and raise7 < 100000:
                                            if labat_chips < 100000:
                                                k
                                            if labat_chips >= 100000:
                                                river
                                                hand9 = input()
                                                while playing == True:
                                                    if hand9 == "fold":
                                                        unable
                                                    if hand9 == "check" or hand9 == "call":
                                                        allin
                                                    if hand9 == "raise":
                                                        raise8 = int(input())
                                                        while playing == True:
                                                            if raise8 < 10000:
                                                                no
                                                            if raise8 >= 10000 and raise8 < 100000:
                                                                if labat_chips < 100000:
                                                                    k
                                                                if labat_chips >= 100000:
                                                                    k
                                                            if raise8 >= 100000 and raise8 < 200000:
                                                                if labat_chips < 100000:
                                                                    k
                                                                if labat_chips >= 100000:
                                                                    k
                                                            if raise8 >= 200000 and raise8 < labat_chips:
                                                                fold
                                                            if raise8 > labat_chips:
                                                                no
                                                            if raise8 == labat_chips:
                                                                allin
                                                            else:
                                                                print("Please place a valid bet")
                                                                raise8 = int(input())
                                                        break
                                                    if hand9 == "RHTH":
                                                        p
                                                    if hand9 == "AllIn":
                                                        z
                                                    if hand9 == "chipcount":
                                                        z
                                                    if hand9 == "!Help":
                                                        z
                                                    else:
                                                        print("Whats that? Type !Help if you're lost")
                                                        hand9 = input()
                                                break
                                        if raise7 >= 100000 and raise7 < 200000:
                                            if labat_chips < 100000:
                                                k
                                            if labat_chips >= 100000:
                                                river
                                                hand10 = input()
                                                while playing == True:
                                                    if hand10 == "fold":
                                                        unable
                                                    if hand10 == "check" or hand10 == "call":
                                                        allin
                                                    if hand10 == "raise":
                                                        raise9 = int(input())
                                                        while playing == True:
                                                            if raise9 < 10000:
                                                                no
                                                            if raise9 >= 10000 and raise9 < 100000:
                                                                if labat_chips < 100000:
                                                                    k
                                                                if labat_chips >= 100000:
                                                                    k
                                                            if raise9 >= 100000 and raise9 < 200000:
                                                                if labat_chips < 100000:
                                                                    k
                                                                if labat_chips >= 100000:
                                                                    k
                                                            if raise9 >= 200000 and raise9 < labat_chips:
                                                                fold
                                                            if raise9 > labat_chips:
                                                                no
                                                            if raise9 == labat_chips:
                                                                allin
                                                            else:
                                                                print("Please place a valid bet")
                                                                raise9 = int(input())
                                                        break
                                                    if hand10 == "RHTH":
                                                        p
                                                    if hand10 == "AllIn":
                                                        z
                                                    if hand10 == "chipcount":
                                                        z
                                                    if hand10 == "!Help":
                                                        z
                                                    else:
                                                        print("Whats that? Type !Help if you're lost")
                                                        hand10 = input()
                                                break
                                        if raise7 >= 200000 and raise7 < labat_chips:
                                            fold
                                        if raise7 > labat_chips:
                                            no
                                        if raise7 == labat_chips:
                                            allin
                                        else:
                                            print("Please place a valid bet")
                                            raise7 = int(input())
                                    break
                                if hand8 == "RHTH":
                                    p
                                if hand8 == "AllIn":
                                    z
                                if hand8 == "chipcount":
                                    z
                                if hand8 == "!Help":
                                    z
                                else:
                                    print("Whats that? Type !Help if you're lost")
                                    hand4 = input()
                            break
                        if hand7 == "raise":
                            raise10 = int(input())
                            while playing == True:
                                if raise10 < 10000:
                                    no
                                if raise10 >= 10000 and raise10 < 100000:
                                    if labat_chips < 100000:
                                        k
                                    if labat_chips >= 100000:
                                        k
                                if raise10 >= 100000 and raise10 < 200000:
                                    if labat_chips < 100000:
                                        k
                                    if labat_chips >= 100000:
                                        k
                                if raise10 >= 200000 and raise10 < labat_chips:
                                    fold
                                if raise10 > labat_chips:
                                    no
                                if raise10 == labat_chips:
                                    allin
                                else:
                                    print("Please place a valid bet")
                                    raise10 = int(input())
                            break
                        if hand7 == "RHTH":
                            p
                        if hand7 == "AllIn":
                            z
                        if hand7 == "chipcount":
                            z
                        if hand7 == "!Help":
                            z
                        else:
                            print("Whats that? Type !Help if you're lost")
                            hand7 = input()
                    break
            if raise6 >= 125000 and raise6 < 200000:
                if labat_chips < 100000:
                    k
                if labat_chips >= 100000:
                    k
            if raise6 >= 200000 and raise6 < labat_chips:
                fold
            if raise6 > labat_chips:
                no
            if raise6 == labat_chips:
                allin
            else:
                print("Please place a valid bet")
                raise6 = int(input())
        break
    if hand1 == "RHTH":
        p
    if hand1 == "AllIn":
        z
    if hand1 == "chipcount":
        z
    if hand1 == "!Help":
        z
    else:
        print("Whats that? Type !Help if you're lost")
        hand1 = input()
