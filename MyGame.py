print("Welcome back to the World Series Of Poker, I'm Lon McEachern and im here with Antonio Esfandiari")
print("Esfandiari: Hey")
print("And we are mere minutes away from finding out the final competitor to the main event, with the winner winning the illustrious WSOP bracelet")
print("Esfandiari: Ive won 3 of them braclets and they're only collecting dust in a cabinet, they're here for that magical, life-changing fifteen million dollar payout")
print("Lon: Yes of course, the highest prize-pot in the history of the main event, from the huge 8 thousand plus entrants, we have already deterined 8 players on the final table.")
print("Esfandiari: Yeah, seriously strong set of players.")
print("We are here on the pinultimate table of the World Series Of Poker main event with only 2 contestents left, of course we have Mr Antoine Labat")
print("Esfandiari: Guy's come from from france with no real history, yet he's taken down some big dogs to get here, and would be only the third frenchamn to get to the main event.")
print("Lon: And he's up against...")
print("Your dad: Look, payday's already big, enough for some of your mommy's treatment, you know it, I know it, but dont focus on that, everybody's already so proud of you, anything you do now, is just a bonus, Okay?")
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
        print("If ever you need my help, do: RunHandThroughHair")
        print("i'll cough once to Fold, twice to Check/Call or three times to go big, you shouldnt need me though")
        print("Dont really know why we still have that camera on you, but whatever.")
        print("MANAGER: CAMERA'S ARE ROLLING, COME ON NOW!!")
        print(name,", You got this!")
        print("As you're walking away, your dad yells:")
        print("Im Proud of you son!")
        print("While walking through the back towards the poker table on stage, I walk up to you.")
        print("So, everything you can do is, ChipCount, Check, Call, Raise, which will lead to how much you wish to raise, Allin, Fold and run hand through hair")
        print("Try to enjoy")
        break
    if Played_before == "no":
        BabySteps = True
        print("Your dad sigh's as if he's dissapointed")
        print("Clearly you've been relying on our cheating tactic's a little too much")
        print("MANAGER: TIME TO GO!")
        print("Right, when you play you hand and you don't know what to do, do: RunHandThroughHair")
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
            print("So, everything you can do is, ChipCount, Check, Call, Raise, which will lead to how much you wish to raise, Allin, Fold !Help and run hand through hair")
            break
        if following == "no":
            print("You're a lost cause, google it.")
            print("When you're done, come back")
            print("I'll enable the BabySteps feature during the first table vs Labat, if you're stuck or dont know what to do, type !Help when prompted")
            print("So, everything you can do is, ChipCount, Check, Call, Raise, which will lead to how much you wish to raise, Allin, Fold !Help and run hand through hair")
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
print("She announces the beginning of the game and proceeds to deal you and your opponent 2 cards.")
print("You take a deep breath in, exhale hard but silent, shuffle into your seat, notice the lights have dimmed from the audience in shine off the table")
print("Before you know it, you feel right at home.")
print("You look at your first hand, its a 4♣ 9♠, Labat raises to 30k, you fold immediately")
print("Oh boy...")
print("5 hands go by quickly, minor amounts get's raised between you and Labat, however it amasses to nothing")
print("you see the next hand to be 4♠ & 5♠")
print("Labat Calls the blind")
print("What would you like to do?")
hand1 = input()
playing = True
while playing == True:
    if hand1 == "fold":
        print("As there is nothing to lose, and all to gain, this is pointless")
        hand1 = input()
    if hand1 == "check":
        print("ok")
        break
        playing = False
    elif hand1 == "call":
        print("ok")
        break
    elif hand1 == "raise":
        print("How much would you like to raise?")
        raise1 = int(input())
        if raise1 < 10000:
            print("Thats too low, lowest bet is 10000")
        if raise1 >= 10000 and raise1 < 100000:
            print("ok")
        if raise1 >= 100000 and raise1 < 200000:
            print("Agressive, but risky")
            Chipcount = Chipcount - raise1
        if raise1 >= 200000 and raise1 < Chipcount:
            print("You grab the chips needed, a large stack, but you hear your dad cough a loud 2 coughs, maybe play things a little steadier")
            print("What would you like to do?")
            hand1 = input()
        if raise1 > Chipcount:
            print("You dont have that much chips to use, you have:", Chipcount)
            raise1 = int(input())


    elif hand1 == "all in":
        print("You grab all your chips, a large stack, but you hear your dad cough a loud 2 coughs, maybe play things a little steadier")
        print("What would you like to do?")
        hand1 = input()
    elif hand1 == "chipcount":
        print(Chipcount)
        print("What would you like to do?")
        hand1 = input()
    elif hand1 == "!Help":
       print("You have:", Chipcount, "Chips, id reccomend just calling as your hand is mediocre but has a lot of potential.")
       print("You can do: chipcount, check, call, raise, which will lead to how much you wish to raise, all in, fold !Help and run hand through hair")
       hand1 = input()
    elif hand1 == "run hand through hair":
        print("Your dad coughs twice")
        print("What would you like to do?")
        hand1 = input()
        dad_coughs = dad_coughs + 1
    else:
        print("Whats that? Type !Help if you're lost")
        hand1 = input()

print("The hand continues")
