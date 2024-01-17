# -*- coding: utf-8 -*-
# !/usr/bin/env python

# -----> Version Notes ------------------------------------------------------------------------------
# Ver 1   -- The dawn of time.
# Ver 2   -- Added branch support, custom output paths, one_liners, and more
# Ver 3   -- Deprecated output schemes (deleted lists_flag), corrected default master pulls, ensured confirmation before overwrite (deleted branch_flag), and changed landing zone after pull
# Ver 4   -- Added turbo search to standards search, can use spaces in queries now, updated logo, added more one_liners, pokemon mode
# ---------------------------------------------------------------------------------------------------

# -----> Import Modules
import urllib
import math
from collections import OrderedDict
import os
import time
from datetime import datetime,date
import calendar
from ctypes import windll, byref
from ctypes import wintypes
import random

# -----> Declare global variables
flag = ""
skip_flag = False
query = ""
label = ""
rocket_banner = ""
clone_status = ""
no_results = False
index_dict = {}
choice_number = 0
mapping_website = ""
back = "  <-BACK-] "
pull_list = []
working_dir = ''
change_back = False
turbo_mode = False
one_liners = "\"640K ought to be enough for anybody.\" (Bill Gates, 1981)\n\"A newspaper is a collection of half-injustices\"\n\"Are your cookies made with real Girl Scouts?\"\n\"But honey, we need a 4 TB drive for word processing!\"\n\"Do not touch\" is the scariest thing you can read in Braille\n\"Good morning!\" is an opinion, not a greeting.\n\"Ground Beef\" -- A Cow With No Legs!\n\"Hex Dump\" - Where Witches put used curses?\n\"This should only take 5 minutes right?\"\n\"This should only take me an hour to code up\"\n\"What could go wrong?\"\n(A)bort, (R)etry, (F)ail, (G)rab_Hammer\n*IT IS* documented, look under \"For Internal Use Only.\"\n*ratchet straps* That\'s not going anywhere, and if it does we thought it wouldn\'t!\n......64..65...66...67...68...69... \"STOP RIGHT THERE!\"\n...So simple a child could do it?  Go find me a child!\n1 + 2 = 3; Therefore, 4 + 5 = 6.\n10 days and 18 messages later, \"Oh I understand now\"\n74% of all statistics are made up on the spot\n89.6% of all statistics are wrong.\nA big enough hammer can usually fix anything.\nA bird in the hand is a big mistake.\nA bird in the hand is better than one overhead!\nA career is a job that takes about 20 more hours a week.\nA clean desk is a sign of a cluttered desk drawer.\nA cynic smells flowers and looks for the casket.\nA day without radiation is a day without sunshine.\nA diploma proves only that you know how to find an answer.\nA dry sense of humor is better than slobbering everywhere\nA field upgrade,HAL. We\'re going to make you IBM compatible.\nA fool with a tool is a well-equipped fool\nA nuclear war can ruin your whole day...\nA nudist has no reason to fear a pickpocket.\nA scone is a biscuit that\'s gone to college.\nAGGHHhhh, 4 AM Already!\nASCII silly questions and you\'ll get some silly ANSI\nActions are usually right, but the reasons seldom are.\nAge and treachery can always overcome youth and skill.\nAlien pub...call that a SPACE BAR. -Lil Wayne (probably)\nAll I want is a warm bed, a kind word, and unlimited power.\nAlways consider the alternative before making a choice.\nAlways remember you\'re unique - just like everyone else.\nAm I ignorant or apathetic?  I don\'t know and don\'t care!\nAny sufficiently advanced bug will become a feature.\nAnything not nailed down is a cat toy.\nBackup not found: (A)bort (R)etry (P)anic\nBank Rule: To get a loan, first prove you don\'t need it.\nBank: IMPORTANT message NOW. Message: \"Hello we are your bank :)\"\nBecome a programmer and never see the world!\nBetter one true friend than a hundred relatives.\nBuildings are already built.\nBuying a bigger bed gives you more bed room and less bedroom.\nCall me if you need my phone number!\nCats are smarter than dogs. Eight cats won\'t pull a sled.\nChemists don\'t die, they just stop reacting!\nCircular Definition: see Definition, Circular.\nWe need another meeting to discuss the meeting.\nCompatible: Blows up a little later than Incompatible\nCross river *THEN* insult alligator.\nDespite the high cost of living, it remains popular.\nDid you expect mere proof to sway my opinion?\nDo NOT look into laser with remaining eye..\nDo artificial plants need artificial water?\nDo crabs think fish can fly?\nDo molecular biologists wear designer genes?\nDo radioactive cats have eighteen half-lives?\nDo witches use Spell-checkers?\nDo you always hit the nail right on the thumb?\nDog for sale: eats anything and is fond of children\nDon\'t bother pressing that key, there is no ESC.\nDon\'t confuse me with facts, my mind is made up!\nDon\'t even TRY to THINK without proper tools.\nDon\'t lend people money.  It causes amnesia.\nIf you don\'t want to see someone ever again, lend them money.\nDon\'t look now, but your file is unzipped.\nDon\'t open the darkroom door; it lets all the dark out.\nDon\'t take life seriously...it isn\'t permanent.\nDon\'t worry the next message will be better!\nEeeeuw!  You mean you actually TALK on the phone?\nElvis Stamps:  Where will your mail be spotted next?\nError-Disk Full Error,Formatting Drive C: to make space..loljk\nEvery exit is an entrance into something else.\nEvery great thinker was called insane.\nEvery valuable idea offends someone.\nEveryone is a genius at least once a year.\nEveryone is gifted. Some just open their packages sooner.\nFeatures should be discovered, not documented!\nFloppy Disk = Lower back trouble.\nFools and their money become popular quickly.\nGo ahead, correct my typos. I\'ll make mores.\nGoals are dreams with deadlines.\nGoing to \"the mall\" because you can shop at \"them all\"\nHe does when go to but if and I confused.\nHelp stamp out, eliminate, and abolish redundancy!\nHelp!  I\'ve been possessed by a daemon!\nHey, wake up! It\'s time for your sleeping pills.\nHire teenagers while they still know everything.\nHistory is a set of lies agreed upon by the Victors\nHonesty pays, but not enough to satisfy some people.\nHong Kong, Son of King Kong\nHot water Heaters:  hot water needs heating?\nHow did I get round from eating square meals?\nHow do you keep a person in suspense?\nHow does shower towel get dirty?\nHow much deeper would the oceans be without sponges?\nHow to make Murphy\'s Law fail - try to prove it to someone.\nI am correct, the rest of you are wrong!\nI am not arguing with you, I\'m telling you.\nI am not young enough to know everything.\nI am the Shopping Cart that nicks at your paint-job.\nI can keep a secret.  It\'s the people I tell that can\'t.\nI can spell, I justs cant type worth as hoot!\nI don\'t have a solution but I really admire the problem.\nI don\'t have all the answers, just those that count.\nI don\'t remember if I forgot or not!\nI have a mind like a steel... uh... thingy.\nI have often depended on the blindness of strangers.\nI have seen the data...now bring me some I can agree with\nI haven\'t lost my mind, it\'s backed up on disk\nI idiot-proof my programs...I think.\nI know everything, but I\'m sworn to secrecy.\nI may be wrong, but I\'m never in doubt!\nI never get lost, just momentarily disoriented.\nI think my learning curve has turned into a circle.\nI think, therefore I am, I think\nI tñld yoñ, \"Neverñtouch ñhe microchip!\"\nI used to be indecisive, but now I\'m not sure.\nI want my data back, machine, and I want it now!\nI was on a roll, till I slipped on the butter.\nI was so much older then, I\'m younger than that now.\nI wasn\'t there.  I didn\'t do it.  I want my lawyer!\nI\'d give my right arm to be ambidextrous\nI\'d love to, but I\'m teaching my ferret to yodel.\nI\'d love to, but my bathroom tiles need grouting.\nI\'d love to, but my favorite commercial is on TV.\nI\'d love to, but my patent is pending.\nI\'d love to, but my uncle escaped again.\nI\'d love to, but the President said he might drop in.\nI\'ll get to it on the 2nd Tuesday of next week.\nI\'ll have what the gentleman on the floor is having.\nI\'m easy to please as long as I get my way.\nI\'m not afraid of flying, I\'m afraid of crashing.\nI\'m not afraid of heights; I\'m afraid of death.\nI\'m not laughing at you, WE\'RE laughing at you!\nI\'m one-of-a-kind.  (Just what kind, nobody is really sure.)\nI\'m the head monkey in charge of the banana factory\nI\'ve got it!  I\'ve got it!  Now, for the cure...\nIf I put kitty litter on the ground, is it kitty litter?\nIf I save time, when do I get it back ?\nIf Version 1.0 works someone goofed...\nIf a program is useful, it will have to be changed.\nIf all goes well, you\'ve overlooked something!\nIf an experiment works first try, something has gone wrong\nIf at first you don\'t succeed, call it Ver 1.0\nIf corn oil comes from corn, where does baby oil . . .\nIf ignorance is bliss, why aren\'t there more happy folks?\nIf it jams, force it....If it breaks, it needed replacing\nIf it works, rip it apart and find out why!\nIf it\'s useless, it will have to be documented.\nIf nothing is impossible then it\'s possible for something to be impossible.\nIf space is the final frontier, what\'s TIME?\nIf two wrongs don\'t make a right, try three. That oughta do it.\nIf you can\'t make it good, make it big.\nIf you can\'t make it good, make it shiny.\nIf you have nothing to say, say nothing - or...not.\nIf you needed a sign to do that thing, this isn\'t it. Keep thinking.\nIf you really want to know, you won\'t ask me.\nIf you want someone to keep a secret, keep the secret yourself.\nIf your code compiles first try, something has gone terribly wrong\nInsert disk 5 of 4 and press any key to go back\nIs the S or C silent in \"scent\"?\nIt is always darkest just before you turn on the lights.\nIt\'s like trying to herd greased cats...\nIt\'s not hard to meet expenses, they\'re everywhere.\nIt\'s not the money I want, it\'s the stuff.\nJunk - bad stuff.  Stuff - good junk.\nJust because the fix is obvious doesn\'t mean the solution is the same.\nLife is like... an analogy.\nLife is not fair...it IS, however, quite a circus.\nLife is short, eat dessert first.\nLife is unfair to everyone - and that makes it fair.\nLoan? If your momma won\'t let you borrow the money, heck I won\'t either!\nMadness takes it\'s toll. Please have exact change.\nMail your ideas written on the back of a $20 bill to...\nMe, indecisive?  I don\'t think I am, do you?\nMinds, like parachutes, work best when open.\nMoney is like a promise, easier made then kept.\nMoney talks - mine says \"Goodbye\"\nMultitasking = messing up several things at once.\nMy bit bucket runneth over...\nMy hovercraft is full of eels.\nNever believe anything until it\'s been officially denied.\nNoses run and feet smell.\nNot my circus not my monkeys!\nOF COURSE I\'m listening!  (Which meeting is this?)\nOf all the people I\'ve met, you\'re certainly one of \'em.\nImmortal = Im mortal.\nOranges are orange but lemons aren\'t yellows\nI\'m always worrying about what other people think of me. Don\'t worry, no one thinks about you.\nPhilosophy:  unintelligible answers to insoluble problems\nPhotographers fade faster than photographs.\nPlagiarism is the sincerest form of flattery.\nProcrastination Day Has Been Postponed!\nProofread carefully to see if you any words out!\nROM wasn\'t built in a day.\nRecursiveFunction(RecursiveFunction)\nSand is just a combo of \"sea\" and \"land\".\nSoap on the floor. Which one is clean and dirty?\nSoftware independent: won\'t work with any software.\nSome days you\'re the windshield, some days the bug.\nStipulation #1:  There will be no stipulations\nSure I can help you out! Which way did you come in?\nThe bigger they are, the harder they hit you.\nThe check\'s in the mail... Trust me!\nThe human brain named itself.\nThe most expensive component is the one that breaks.\nThere IS intelligent life in the universe.  It ignores us.\nThere is no such thing as bravery; only degrees of fear.\nThere\'s an \'L\' in NOEL, even though it says the opposite.\nThere\'s no such thing as thanksgiving music\nThis is your brain. What on brain your is this.\nThis time around the revolution will not be televised.\nTo clone a felon, do I use the COPY CON command?\nTo every exception there is an exception.\nTo get a loan you must prove you don\'t need it.\nTo get the point, rub a porcupine backwards.\nTo know the road ahead, ask those coming back.\nTo make it work, you have to DO the work.\nToday is the first day of the rest of your life.\nToday you\'re the oldest you\'ve been and youngest you\'ll ever be.\nTomorrow never comes, it only becomes today.\nTwo mind readers, reading each others minds - what are they reading?\nUnsolicited advice requested\nUpgrading your software to fix 3 and break 12. :) Ur welcome\nWaiting for the waiter makes you the waiter.\nWar never decides who is right or wrong, only who is left.\nWashing the dishes makes you a dishwasher.\nWe give nothing as willingly as our advice.\nWe have no solution, but we sure admire the problem.\nWe make our own fortunes and call them our fate.\nWe\'ll burn that bridge when we come to it.\nWe\'re all sitting in the same boat, but I\'m in the captains chair.\nWe\'re judged by what we finish, not what we start.\nWe\'re lost but we\'re making good time.\nWell, to be frank, I\'d have to change my name.\nWhat if there were no hypothetical questions?\nWhat was the best thing BEFORE sliced bread?\nWhen all else fails, read the directions.\nWhen all else fails, read the manual.\nWhen all is said and done, more is said then done.\nWhen in trouble, delegate.\nWhen talking nonsense try not to be serious.\nWho is General Error, and *WHY* is breaking my stuff?\nWho told you I\'m paranoid?\nWhy is there a \"d\" in fridge?\nWitty one-liner\nYou can never get rid of a bad temper by losing it.\nYou cannot strengthen the weak by weakening the strong.\nYou have been selected for a secret mission.\nYou have to be sharp to be on the cutting edge.\nYou have two choices for Tylenol: Take it or Leave it.\nYou will become rich and famous unless you don\'t.\nYou would if you could but you can\'t so you won\'t.\nYou\'re not losing more hair, you\'re gaining more scalp.\ncopy *.txt > brain\nI failed math so many times at school, I can\'t even count.\nI was wondering why the frisbee kept getting bigger and bigger, but then it hit me.\nI want to die peacefully in my sleep like my grandpa, unlike his screaming passengers.\nDon\'t you hate it when someone answers their own questions? I do.\nI can\'t believe I got fired from the calendar factory. All I did was take a day off.\nMost people are shocked when they find out how bad I am as an electrician.\nA maid\'s house is never clean.\nThe password is always *******\nThe chain is only as strong as the weakest link.\nMatryoshka dolls are so full of themselves.\nA termite walks into the bar and asks, \'Is the bar tender here?\'\nTwo fish are in a tank. One says, how do you drive this thing?\'\nJust burned 2,000 calories...in the oven.\nThis is your sign to go drink some water.\nHe NEEDS some milk!\nWeaving the fabric of spacetime.\nDiscerning the Transmundane\nDon\'t walk a mile in their shoes. Instead, run so they can\'t catch you...\nTake care of your chickens, become a chicken tender.\nWhen you\'re cleaning the vacuum, you are the vacuum cleaner.\nFrog shoes are open toad sandals.\nUnsharpened pencils are pointless.\n6:30 is the best time on a clock, hands down.\nTwo wifi engineers got married. The reception was fantastic.\nBessy dind\'t give any milk today, what an udder failure.\nIf attacked by a mob of clowns, go for the juggler.\nI can tell when people are being judgemental just by looking at them.\nThe rotation of Earth really makes my day.\nWhat if there were no hypothetical questions?\nAre people born with photographic memories, or does it take time to develop?\nThe world champion tongue twister got arrested. I hear it\'ll be a tough sentence.\nGeography is where it\'s at.\nYou have cat to be kitten me right meow...\nThe man who invented knock-knock jokes should get a no bell prize.\nWhiteboards are remarkable.\nI threw a boomerang a couple years ago; I now live in constant fear.\nGrandma on speed dial. I call it insta-gram.\nRoad work ahead? Uh yea, I sure hope it does.\nIt is Wednesday my dudes.\nA potato flew around my room before you came, excuse the mess it made…\nWHAT ARE THOSEEEEE? THEY are my crocs!\nWhat\'s 9 plus 10? 21.\nIt\'s an avocado, thanks!\nHi my name is Trey I have a basketball game tomorrow.\nMetal music at Denny\'s\nI\'m in my mum\'s car. Broom broom!\nI could have dropped my croissant!\nI didn\'t get no sleep \'cause of y\'all! Ya\'ll not gonna get no sleep \'cause of me!\nPi? pi. No? no. Chi? chi. O? o. Pinocchio. PIKAPIKAPIKAPIKAPIKA!\nCaution: This is a \'no flex zone\'\nUsing these flowers, we can lure these beez in the trap.\nBirds love house, mice hate trap.\nYou\'re not my dad!\nThat was legitness.\nI am shooketh.\nLook at all those chickens!\nHi, welcome to Chili\'s.\nChipotle is my life.\nWhy you always lyin\'?\nI\'m sorry I didn\'t see you there. I was too busy b-blocking out the haters.\nThat\'s my best friend; that\'s my best friend.\nWhen will you learn, that your actions, have consequences!?\nShe\'s thinks she\'s the queen, and were the sorry people.\nCan I PLEASE get a waffle?\nIs this allowed? Is this allowed!?\nI smell like beef.\nI wanna be a cowboy baby.\nLipstick? In my Valentino white bag?!\nYou know what, I\'m about to say it. I don\'t care that you broke your elbow.\n And they were roommates.\nUm, I\'m never been to oovoo javer.\nA mug shot? I don\'t even drink coffee.\nTask failed successfully.\nWhy are you running, why are you running?\n...a birthday gift on my birthday to my birthday party on my birthday with a birthday gift?\nGo to Del Taco. They got a new thing called freesha-freeshavacado.\nNice Ron. I sneezed, oh, what, am I not allowed to sneeze?\nWait oh yes, wait a minute Mr. Postman. HaaaAHH.\nWait a minute, who ARE you?\nMan I really miss the \"Jimmy Timmy Power Hour\"\nI <3 Python\nDragonborn, huh? Was it your ma or your pa that was the dragon?\nMy cousins out fighting dragons, and what do I get? Guard duty.\n\"No lollygaggin\" - Riften Guard\nLet me guess, someone stole your sweetroll?\nShor\'s bones!\nWait... I know you...\nNever should've come here! *intense music starts playing*\nTeenage Mutant Ninja Squirtle Squad\nPizza Pizza".split('\n')
clear = lambda: os.system('cls')
logo = """\n     _______ __  __      __       ______           __                    
    / ____(_) /_/ /___ _/ /_     / ____/  ______  / /___  ________  ___NEW!
   / / __/ / __/ / __ `/ __ \   / __/ | |/_/ __ \/ / __ \/ ___/ _ \/ ___/
  / /_/ / / /_/ / /_/ / /_/ /  / /____>  </ /_/ / / /_/ / /  /  __/ /    
  \____/_/\__/_/\__,_/_.___/  /_____/_/|_/ .___/_/\____/_/   \___/_/     
                                        /_/                              \n"""

# -----> Animation played during the cloning process
def animate_Rocket(_rocket_banner):
	global rocket_banner
	distanceFromTop = 0
	while True:
		print logo
		print _rocket_banner
		print "\n" * distanceFromTop
		print """                   .             
                    .           
                . ;.            
                 .;             
                  ;;.           
                ;.;;            
                ;;;;.           
                ;;;;;           
                ;;;;;           
                ;;;;;           
                ;;;;;           
                ;;;;;           
              ..;;;;;..         
               ':::::'          
                 ':`            """
		time.sleep(0.1)
		os.system('cls')
		distanceFromTop += 1
		if distanceFromTop < 10:
			distanceFromTop += 1
		else:
			break


def peaceOut():
	clear()
	quit()


def reloadScreen():
	clear()
	print logo


def readSettingsFile():
	global flag, skip_flag,working_dir
	settings_file = os.environ['USERPROFILE'] + "\\settings.pb"
	with open(settings_file, 'r') as settings:
		lines = settings.readlines()
		for line in lines:
			if 'gitlab_explorer=standard' in line.strip().lower().replace(' ',''):
				flag = 's'
				skip_flag = True
			if 'gitlab_explorer=custom' in line.strip().lower().replace(' ',''):
				flag = 'c'
				skip_flag = True
			if 'gitlab_explorer=all' in line.strip().lower().replace(' ',''):
				flag = 'a'
				skip_flag = True
			if 'gitlab_explorer_output_path=' in line.strip().lower().replace(' ',''):
				working_dir = line.split('=')[-1].replace('\"','').replace('\'','').strip()
			else:
				working_dir = os.environ['USERPROFILE']
	return flag


def throwPokeball():
	global logo,pokemon_appeared,pokelines,poke_number
	print("\n  Throwing a pokeball at {}!".format(pokemon))
	time.sleep(3)
	if 80 >= random.randint(1,100):
		print("  The pokeball bumped left...")
		time.sleep(3)
		if 80 >= random.randint(1,100):
			print("  The pokeball bumped right...")
			time.sleep(3)
			if 80 >= random.randint(1,100):
				print("  ALMOST!!!!!")
				time.sleep(5.5)
				if 80 >= random.randint(1,100):
					print("  GOTCHA! The wild {} was caught!".format(pokemon))
					pokelines += '{}\n'.format(pokemon)
					pokelog = open('{}\\pokelog.txt'.format(os.environ['USERPROFILE']),"w")
					pokelog.writelines(pokelines)
					pokelog.close()
					print("  Added {} to your pokedex! {} was sent to BOX1".format(pokemon,pokemon))
					print_pokemon(poke_number)
					time.sleep(4.5)
				else:
					print("  DRATS! The wild {} broke free and fled!".format(pokemon))
			else:
				print("  DRATS! The wild {} broke free and fled!".format(pokemon))
		else:
			print("  DRATS! The wild {} broke free and fled!".format(pokemon))
	else:
		print("  DRATS! The wild {} broke free and fled!".format(pokemon))
	pokemon_appeared = False
	time.sleep(1.5)
	logo = original_logo +"  "+one_liners[random.randint(0, len(one_liners)-1)]+"\n\n "

def printPokedex():
	if os.path.exists('{}\\pokelog.txt'.format(os.environ['USERPROFILE'])):
		pokelog = open('{}\\pokelog.txt'.format(os.environ['USERPROFILE']),"r")
		pokelines = pokelog.readlines()
		print('')
		if len(pokelines) < 10:
			print("  Oak's rating: You still have lots to do. Look for pokemon in grassy areas!")
		elif len(pokelines) >= 10 and len(pokelines) <= 19:
			print("  You're on the right track! Get a Flash HM from my Aide")
		elif len(pokelines) >= 20 and len(pokelines) <= 29:
			print("  You still need more pokemon! Try to catch other species!")
		elif len(pokelines) >= 30 and len(pokelines) <= 39:
			print("  Good, you're trying hard! Get an Itemfinder from my Aide")
		elif len(pokelines) >= 40 and len(pokelines) <= 49:
			print("  Looking good! Go find my Aide when you get 50!")
		elif len(pokelines) >= 50 and len(pokelines) <= 59:
			print("  You finally got a least 50 species! Be sure to get Exp.All from my Aide")
		elif len(pokelines) >= 60 and len(pokelines) <= 69:
			print("  Oh! This is getting even better!")
		elif len(pokelines) >= 70 and len(pokelines) <= 79:
			print("  Very good! Go fish for some marine pokemon!")
		elif len(pokelines) >= 80 and len(pokelines) <= 89:
			print("  Wonderful! Do you like to collect things?")
		elif len(pokelines) >= 90 and len(pokelines) <= 99:
			print("  I'm impressed! It must have been difficult to do!")
		elif len(pokelines) >= 100 and len(pokelines) <= 109:
			print("  You finally got at least 100 species I can't believe how good you are!")
		elif len(pokelines) >= 110 and len(pokelines) <= 119:
			print("  You even have the evolved forms of pokemon! Super!")
		elif len(pokelines) >= 120 and len(pokelines) <= 129:
			print("  Excellent! Trade with friends to get some more!")
		elif len(pokelines) >= 130 and len(pokelines) <= 139:
			print("  Outstanding! You've become a real pro at this!")
		elif len(pokelines) >= 140 and len(pokelines) <= 149:
			print("  I have nothing left to say! You're the authority now!")
		elif len(pokelines) == 150:
			print("  Your pokedex is entirely complet...wait...what was that on the windmill...")
		elif len(pokelines) == 151:
			print("  You caught the mythical Mew!!!?\nYour pokedex is entirely complete! Congratulations!")
		print("\n  --------------------------------------")
		print("  | You have {} pokemon in your pokedex: |".format(len(pokelines)))
		for x in pokelines:
			print('  |\t{}{}|'.format(x.strip(),' '*(33-len(x))))
		print("  --------------------------------------")
	else:
		print("  --------------------------------------")
		print("  | Oak's rating: You still have lots to do. Look for pokemon in grassy areas! |")
		print("  | You have {} pokemon in your pokedex! |\n".format(len(pokelines)))
		print("  --------------------------------------")
	pokewait = raw_input("\n  Any to continue...")

def prompt_mapping_category():
	global flag
	reloadScreen()
	while True:
		choice = raw_input("  <HOME> What kind of mapping? [standard(s), custom(c), all(a)]: ").strip().lower()
		if choice == 'pokeball' and pokemon_appeared == True:
			throwPokeball()
			reloadScreen()
			continue
		if choice in ['pokedex','pokemon']:
			printPokedex()
			reloadScreen()
			continue
		if choice in ['s', 'standard', 'st','sta', 'stan', 'stand', 'standa', 'standar','/s']:
			# Standard selected
			flag = 's'
			break
		if choice in ['c', 'custom', 'cu', 'cus', 'cust', 'custo','/c']:
			# Custom selected
			flag = 'c'
			break
		if choice in ['','a','al','all','/a']:
			# All selected
			flag = 'a'
			break
		if choice in ['b', 'ba', 'bac', 'back']:
			reloadScreen()
			exit_prompt = raw_input("  <EXIT> Nowhere to go homie, exit? [y/n]: ").strip().lower()
			if exit_prompt == 'pokeball' and pokemon_appeared == True:
				throwPokeball()
				reloadScreen()
				exit_prompt = raw_input("  <EXIT> Nowhere to go homie, exit? [y/n]: ").strip().lower()
			if exit_prompt in ['pokedex','pokemon']:
				printPokedex()
				reloadScreen()
				exit_prompt = raw_input("  <EXIT> Nowhere to go homie, exit? [y/n]: ").strip().lower()
			if exit_prompt in ['y', 'ye', 'yes','exit']:
				peaceOut()
			else:
				reloadScreen()
		if choice == 'exit':
			peaceOut()
		else:
			reloadScreen()
	reloadScreen()
	return flag


def prompt_query_criteria():
	global flag, query, label, no_results
	while True:
		if flag == 's':
			label = "  <STANDARD MAPPINGS> "
		if flag == 'c':
			label = "  <CUSTOM MAPPINGS> "
		if flag == 'a':
			label = "  <ALL MAPPINGS> "
		if no_results:
			message = "  | (0) results found for "+query.upper().replace('+',' ')+"! |"
			board = "  |"+'-'*(len(message)-4)+"|"
			result = logo[:-1]+'\n'+board+"\n"+message+"\n"+board+"\n"
			no_results = False
			clear()
			print result
			time.sleep(1.15)
		reloadScreen()
		if skip_flag == False:
			query = raw_input(back+label.lstrip()+ "Enter your search criteria: ").strip().lower()
		else:
			query = raw_input(label+ "Enter your search criteria: ").strip().lower()
		cleaned = ''.join(item for item in query if item.isalnum())
		if query == 'pokeball' and pokemon_appeared == True:
				throwPokeball()
				reloadScreen()
				if skip_flag == False:
					query = raw_input(back+label.lstrip()+ "Enter your search criteria: ").strip().lower()
				else:
					query = raw_input(label+ "Enter your search criteria: ").strip().lower()
		if query in ['pokedex','pokemon']:
			printPokedex()
			reloadScreen()
			if skip_flag == False:
					query = raw_input(back+label.lstrip()+ "Enter your search criteria: ").strip().lower()
			else:
				query = raw_input(label+ "Enter your search criteria: ").strip().lower()
		if query == 'exit':
			peaceOut()
		if cleaned == '':
			reloadScreen()
			continue
		if query == 'back':
			if skip_flag == False:
				reloadScreen()
				flag = prompt_mapping_category()
				if flag in ['s', 'c', 'a']:
					reloadScreen()
					break
			if skip_flag == True:
				reloadScreen()
				exit_prompt = raw_input("  <EXIT> Nowhere to go homie, exit? [y/n]: ").strip().lower()
				if exit_prompt == 'pokeball' and pokemon_appeared == True:
					throwPokeball()
					reloadScreen()
					exit_prompt = raw_input("  <EXIT> Nowhere to go homie, exit? [y/n]: ").strip().lower()
				if exit_prompt in ['pokedex','pokemon']:
					printPokedex()
					reloadScreen()
					exit_prompt = raw_input("  <EXIT> Nowhere to go homie, exit? [y/n]: ").strip().lower()
				if exit_prompt in ['y', 'ye', 'yes','exit']:
					peaceOut()
				else:
					reloadScreen()
		if cleaned != "":
			query = query.replace(' ', '_')
			break
	return flag


def setUrls():
	global url,change_back,turbo_mode
	change_back = False
	turbo_mode = False
	if query == '':
		url = 'http://gitlab.cernersphere.net/public/projects?utf8=%E2%9C%93'
	elif flag == 's' and query != 'cms': # EXCEPTION FOR 'STANDARD' gitlab group
		url = 'http://gitlab.cernersphere.net/public/projects?utf8=%E2%9C%93&page=1&search=standard_' + query
		scrape = urllib.urlopen(url)
		html = scrape.read()
		for value in html.split('\n'):
			if 'Projects (' in value:
				number_of_projects = value.replace('(', '').replace(')', '').split()[-1]
				if number_of_projects == "0":
					url = 'http://gitlab.cernersphere.net/public/projects?utf8=%E2%9C%93&page=1&search=' + query
					change_back = True
				else:
					turbo_mode = True
	else:
		url = 'http://gitlab.cernersphere.net/public/projects?utf8=%E2%9C%93&page=1&search=' + query
	return url


def parseData(_html):
	global group_dict,no_results,query,flag
	group_dict = OrderedDict()
	for value in _html.split('\n'):
		if 'Projects (' in value:
			number_of_projects = value.replace('(', '').replace(')', '').split()[-1]
			page_max = int(math.ceil(float(number_of_projects) / 20.0))
			if int(number_of_projects) > 0:
				# Query returned results
				if page_max > 1:
					if page_max > 20 or len(query) < 3:
						# Prompt user if they really want to load that many results
						reloadScreen()
						prompt_multi_page = raw_input(back+"<JEEPERS> Like zoinks, that's a lot of clues Scoob!\n\n  Are you sure you want to look for \'"+query.replace('+',' ')+ "\'? [y/n]: ").strip().lower()
						if prompt_multi_page == 'pokeball' and pokemon_appeared == True:
							throwPokeball()
							reloadScreen()
							prompt_multi_page = raw_input(back+"<JEEPERS> Like zoinks, that's a lot of clues Scoob!\n\n  Are you sure you want to look for \'"+query.replace('+',' ')+ "\'? [y/n]: ").strip().lower()
						if prompt_multi_page in ['pokedex','pokemon']:
							printPokedex()
							reloadScreen()
							prompt_multi_page = raw_input(back+"<JEEPERS> Like zoinks, that's a lot of clues Scoob!\n\n  Are you sure you want to look for \'"+query.replace('+',' ')+ "\'? [y/n]: ").strip().lower()
						if prompt_multi_page == 'exit':
							peaceOut()
						if prompt_multi_page not in ['y','ye','yea','yeah','continue','yes','re','rea','reah','reah!']:
							no_results = False
							query = "back"
							reloadScreen()
							continue
						else:
							reloadScreen()
							print """
                                                  :\                  
                                                  ;\\                 
                                                  ; ;;  __            
                                                  :/ :-", |    _.ggp. 
                                                  :     (O).-"" :$$$$;
    _____ _____   ____   ______      ____     __ ;              T$$$;
   / ____|  __ \ / __ \ / __ \ \    / /\ \   / /:     _,-        `TP 
  | |  __| |__) | |  | | |  | \ \  / /  \ \_/ /;      `.  _      ;  
  | | |_ |  _  /| |  | | |  | |\ \/ /    \   / ;        "" \    /   
  | |__| | | \ \| |__| | |__| | \  /      | |  ;            `-+'    
   \_____|_|  \_\\\____/\____/   \/       |_|   :            .-'     
                                                ;      \;   ;       
                                                :       `--+'-.     
     .---.                                       ;         ;`       
    :_    `.                                     :         ;        
      "-,   ;                                   / "-.      :        
         ;  :                                .p""-.  ""--..:        
         ;  :                             .-T$$P   ""--..___l-,     
         ;  :                          .-"   ""            :\()l    
         ;  ;              _________.-"         $$          ;`-'    
         ;  ;         .--""$$$$$$$P                         :       
         ;  '._____.-"_.   'T$$T^'                          :       
         :         .-"                                 \    :       
         '.___...-"                                     ;   :       
               /                                        ;   ;       
              :                   .            /       /   /        
              ;                 .J__          :       /  .'         
              ;               .;    "-.       ;      j.-"           
              :             .'/        "-.    ;     : :             
               ;          .' /            "---:     ; ;             
               :       .-"  /                 :    : :              
               ;    .-"  .-"                   ;   ; ;              
              /   .'  .-"                      :  : :               
             /  .'  .'                         :  | ;               
            :  /\  :                           :  ;:                
            ; :  ; ;                           : : ;                
           :  ;  : :__                         ; | :                
           ; _L__J   -`,                      :  : '--.             
           :  l l l____l                       \ _`-,-:             
          ( l ;_:-'                            /  l |`;             
           \"""                                :_l :_;_l             """
							time.sleep(1)

					# Load results
					
					for i in range(1, page_max + 1):
						reloadScreen()
						if turbo_mode == True:
							print " [TURBO MODE] LOADING", query.upper(), str(int(float(i) / float(page_max) * 100.0)) + "% COMPLETED\n"
						else:
							print "  LOADING", query.upper(), str(int(float(i) / float(page_max) * 100.0)) + "% COMPLETED\n"
						if (i*5) < page_max*5:
							leftovers = page_max*5-(i*5)
							print "  ["+'#'*(i*5)+' '*leftovers+']'
						if str(int(float(i) / float(page_max) * 100.0)) == "100":
							reloadScreen()
							print ""
						if flag == 's' and change_back == False and query != 'cms':
							multi_url = 'http://gitlab.cernersphere.net/public/projects?utf8=%E2%9C%93&page=' + str(i) + '&search=standard_' + query
						else:
							multi_url = 'http://gitlab.cernersphere.net/public/projects?utf8=%E2%9C%93&page=' + str(i) + '&search=' + query
						multi_scrape = urllib.urlopen(multi_url)
						multi_html = multi_scrape.read()
						extractHTMLData(multi_html)

				# Query returned only one page of results
				else:
					extractHTMLData(_html)


def cloneMappings():
	global clone_status,mapping_choice, working_dir, folder,pull_list,query,no_results,choice_number
	if group_dict:
		while True:
			count = 0
			max_branch_name_length = 0
			max_branch_change_length = 0
			branch_list = []
			my_dates = []
			branch_dict = OrderedDict()
			reloadScreen()
			print_query_results()
			if clone_status != "":
				print clone_status
				clone_status = ""
			print('  Type \'all\' to pull every mapping (master) from a group \n  or \'done\' to open mappings pulled from this session or...\n')
			mapping_choice = raw_input(back+"<MAPPING CHOICE> Select choice number: ").strip().lower()
			if mapping_choice == 'pokeball' and pokemon_appeared == True:
				throwPokeball()
				reloadScreen()
				print_query_results()
				print('  Type \'all\' to pull every mapping (master) from a group \n  or \'done\' to open mappings pulled from this session or...\n')
				mapping_choice = raw_input(back+"<MAPPING CHOICE> Select choice number: ").strip().lower()
			if mapping_choice in ['pokedex','pokemon']:
				printPokedex()
				reloadScreen()
				print_query_results()
				print('  Type \'all\' to pull every mapping (master) from a group \n  or \'done\' to open mappings pulled from this session or...\n')
				mapping_choice = raw_input(back+"<MAPPING CHOICE> Select choice number: ").strip().lower()
			if mapping_choice != "":
				while mapping_choice[0] == "0" and len(mapping_choice) > 1:
					mapping_choice = mapping_choice[1:]
			if (
					mapping_choice.isdigit()
					and int(mapping_choice) >= 0 and mapping_choice in index_dict.keys()
			):
				reloadScreen()
				folder = str(working_dir) + '\\' + index_dict[mapping_choice].split('/')[-1].split('.')[0]
				mapping_website = index_dict[mapping_choice].split()[-1][:-4]+"/branches"
				#print mapping_website
				branch_scrape = urllib.urlopen(mapping_website)
				branch_html = branch_scrape.read()
				for item in branch_html.replace('\n', "").split('<li>'):
					if 'commits' in item and item[:6] == '<h4><a':
						branch_name = item.split('commits/')[1].split('>')[0][:-1]
						branch_change = item.split('<span class=\'light\'>')[1].split('<')[0]
						if len(branch_name) > max_branch_name_length and len(branch_name) <= 28:
							max_branch_name_length = len(branch_name)
						if len(branch_change) > max_branch_change_length:
							max_branch_change_length = len(branch_change)
				for item in branch_html.replace('\n', "").split('<li>'):
					if 'commits' in item and item[:6] == '<h4><a':
						branch_name = item.split('commits/')[1].split('>')[0][:-1]
						branch_change = item.split('<span class=\'light\'>')[1].split('<')[0]
						branch_time = item.split('<span class=\'light\'>')[-1].split('title=\'')[-1].split('\'>')[0].strip()
						if (max_branch_name_length - len(branch_name)) == 0:
							output_line = branch_name + " / ["+ branch_change+"] @ "+ branch_time
						else:
							output_line = branch_name +" "+" " * (max_branch_name_length - len(branch_name)-1) + " / ["+ branch_change+"] @ "+ branch_time
						if branch_time not in my_dates:
							my_dates.append(branch_time)
						if output_line not in branch_list:
							branch_list.append(output_line)
				#max_branch_name_length = 0
				while True:
					count = 0
					reloadScreen()
					buffer = (96-len(mapping_website.split('.net')[-1].split('/branches')[0][1:]))/2-1
					top_gun = "  "+"~"*buffer+" "+mapping_website.split('.net')[-1].split('/branches')[0][1:].upper()+" "+"~"*buffer+"\n"
					print top_gun
					print "  Branches are ordered from newest to oldest:\n"
					my_dates.sort(key=lambda date: datetime.strptime(date, "%b %d, %Y %H:%M%p"),reverse=True)
					for date in my_dates:
						for branch in branch_list:
							if date in branch:
								x = branch.split("] @")[0].split('/')[0].strip()
								y = branch.split("] @")[0].replace("&#39;","").split('/')[-1]
								spaced_change_and_time = " "*(max_branch_change_length-len(branch.split("] @")[0].replace("&#39;","").split("/ [")[-1])-1)+"] "+datetime.strptime(date, "%b %d, %Y %H:%M%p").strftime("%Y-%m-%d")
								long_spaced_and_time = " "*(max_branch_change_length-len(branch.split("] @")[0].replace("&#39;","").split("/ [")[-1].strip())-1)+"] "+datetime.strptime(date, "%b %d, %Y %H:%M%p").strftime("%Y-%m-%d")
								spaced_choice_and_branch = "["+str(count)+"] <- "+branch.split("] @")[0].replace("&#39;","")
								if len(str(count)) < 2:
									if "..." == branch.split("] @")[0].replace("&#39;","")[-3:] and len(x)<=28:
										branch_output_line = "   "+spaced_choice_and_branch+spaced_change_and_time
									else:
										if len(y[2:]) < 40:
											branch_output_line = "   "+spaced_choice_and_branch+"."+spaced_change_and_time
										else:
											branch_output_line = "   "+spaced_choice_and_branch+spaced_change_and_time
								else:
									if len(y[2:]) < 40:
										branch_output_line = "  "+spaced_choice_and_branch+"."+long_spaced_and_time
									else:
										branch_output_line = "  "+spaced_choice_and_branch+long_spaced_and_time
								if len(branch_output_line) <= 96:
									print branch_output_line
								else:
									if len(str(count)) < 2:
										print "   ["+str(count)+"] <- "+x+" /"+y[:69-len(x)]+"...] "+datetime.strptime(date, "%b %d, %Y %H:%M%p").strftime("%Y-%m-%d")#"   "+' '.join(str(x) for x in branch_output_line.split()[:3])+" "*(max_branch_change_length-len(branch.split("] @")[0].replace("&#39;","").split("/ [")[-1].strip()))+"] "+branch_output_line.split()[-1]
									else:
										print "  ["+str(count)+"] <- "+x+" /"+y[:69-len(x)]+"...] "+datetime.strptime(date, "%b %d, %Y %H:%M%p").strftime("%Y-%m-%d")
								branch_dict[count] = branch
								count+=1
					print "\n  "+"~"*(len(top_gun)-3)
					# MAPPING CHOICE IS VALID
					branch = ''
					brach_choice = ''
					branch_choice = raw_input(back+"<BRANCH CHOICE> Select branch number or hit enter for master: ").strip().lower()
					if branch_choice == 'pokeball' and pokemon_appeared == True:
						throwPokeball()
						reloadScreen()
						continue
						branch_choice = raw_input(back+"<BRANCH CHOICE> Select branch number or hit enter for master: ").strip().lower()
					if branch_choice in ['pokedex','pokemon']:
						printPokedex()
						reloadScreen()
						continue
						branch_choice = raw_input(back+"<BRANCH CHOICE> Select branch number or hit enter for master: ").strip().lower()
					if branch_choice in ['back','b','ba','bac']:
						break
					if branch_choice == "exit":
						peaceOut()
					if branch_choice == "":
						branch = 'master'
					if branch_choice != "":
						while str(branch_choice)[0] == "0" and len(str(branch_choice)) > 1:
							branch_choice = branch_choice[1:]
					if (
							(str(branch_choice).isdigit() and branch_choice >= 0 and int(branch_choice) in branch_dict.keys()) or branch == 'master'
					):
						if not branch:
							branch = branch_dict[int(branch_choice)].split('/')[0].strip()
						projecto = str(index_dict[mapping_choice].split('/')[-1].split('.')[0]).lower()
						if (os.path.exists(folder) and branch not in os.listdir(folder) or not os.path.exists(folder)):
							# FOLDER IS EMPTY OR NULL
							if not os.path.exists(working_dir):
								os.mkdir(working_dir)
							os.chdir(working_dir)
							if not (os.path.exists(projecto)):
								os.mkdir(projecto)
							os.chdir(projecto)
							if not os.path.exists(branch):
								os.mkdir(branch)
							os.chdir(branch)
							purgeAndClone("clone",branch)
							break
						else:
							# FOLDER EXISTS AND CONTAINS FILES
							while True:
								reloadScreen()
								print_query_results()
								response = raw_input("  OVERWRITE " + working_dir + "\\"+projecto + " ("+branch+") [y/n]: ").strip().lower()
								if response == 'pokeball' and pokemon_appeared == True:
									throwPokeball()
									reloadScreen()
									clone_status = ""
									break
								if response in ['pokedex','pokemon']:
									printPokedex()
									reloadScreen()
									clone_status = ""
									break
								if response == 'exit':
									peaceOut()
								if response in ['y', 'ye', 'yes']:
									purgeAndClone("overwrite",branch)
									break
								if response in ['n', 'no','back','b','ba','bac']:
									clone_status = ""
									break
						break
				if branch_choice in ['back','b','ba','bac']:
					continue
			elif mapping_choice == 'exit':
				peaceOut()
			elif mapping_choice in ['back','b','ba','bac','back']:
				reloadScreen()
				break
			elif mapping_choice == 'done' or mapping_choice == '\'done\'' and pull_list != []:
				for item in pull_list:
					os.startfile('{}\\{}\\{}'.format(item,branch,item.split('\\')[-1]))
				peaceOut()
			elif mapping_choice == 'all' or mapping_choice == '\'all\'' or mapping_choice == 'al' or mapping_choice == 'a':
				while True:
					reloadScreen()
					print("  ~~~~~~~~~~~~~~~~~~~~~~~~~ GROUP PULL ~~~~~~~~~~~~~~~~~~~~~~~~~\n")
					indx = 0
					group_pull = {}
					for k,v in group_dict.items():
						print('  ['+str(indx)+'] '+k.upper())
						group_pull[str(indx)] = k
						for vv in v:
							print('\t'+vv.split('/')[-1].split('.')[0])
						print('')
						indx += 1
					print("  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
					group_input = raw_input(back+"<GROUP CHOICE> Select group choice to pull all mappings (master): ").strip().lower()
					if group_input == 'pokeball' and pokemon_appeared == True:
						throwPokeball()
						reloadScreen()
						clone_status = ""
						break
					if group_input in ['pokedex','pokemon']:
						printPokedex()
						reloadScreen()
						clone_status = ""
						break
					if (group_input.isdigit() and int(group_input) >= 0 and group_input in group_pull.keys() and group_pull[group_input] in group_dict.keys()):
						if not os.path.exists(working_dir+"\\"+group_pull[group_input].upper()):
							# CREATE AND PULL
							os.mkdir(working_dir+"\\"+group_pull[group_input].upper())
							os.chdir(working_dir+"\\"+group_pull[group_input].upper())
							for item in group_dict[group_pull[group_input]]:
								os.system(item.split('&')[-1])
								clear()
								rocket_banner = "  Cloning " + item.split('&')[-1].split('/')[-1].split('.')[0]
								animate_Rocket(rocket_banner)
							pull_list.append(os.path.realpath(working_dir+"\\"+group_pull[group_input].upper()))
						else:
							while True:
								response = raw_input("\n  OVERWRITE " + working_dir +'\\'+ group_pull[group_input].upper()+ "? [y/n]: ").strip().lower()
								if response == 'pokeball' and pokemon_appeared == True:
									throwPokeball()
									reloadScreen()
									continue
								if response in ['pokedex','pokemon']:
									printPokedex()
									reloadScreen()
									continue
								if response == 'exit':
									peaceOut()
								if response in ['y', 'ye', 'yes']:
									group_folder = group_pull[group_input].upper()
									os.chdir(working_dir)
									delete_command_1 = "del /f /s /q \"" + str(os.path.realpath(working_dir+"\\"+group_folder))+ "\" >nul 2>&1"
									delete_command_2 = "rmdir /s /q \"" + str(os.path.realpath(working_dir+"\\"+group_folder))+ "\" >nul 2>&1"
									os.system(delete_command_1)
									os.system(delete_command_2)
									os.mkdir(working_dir+"\\"+group_folder)
									os.chdir(working_dir+"\\"+group_folder)
									for item in group_dict[group_pull[group_input]]:
										os.system(item.split('&')[-1])
										clear()
										rocket_banner = "  Cloning " + item.split('&')[-1].split('/')[-1].split('.')[0]
										animate_Rocket(rocket_banner)
									pull_list.append(os.path.realpath(working_dir+"\\"+group_folder))
									break
								if response in ['n', 'no','back','b','ba','bac']:
									clone_status = ""
									break
						break
	else:
		if query != 'back':
			reloadScreen()
			no_results = True

def print_query_results():
	global choice_number, index_dict
	index_dict = {}
	index = 0
	choice_number = 0

	# Populate index_dict
	for group, mapping_list in group_dict.items():
		for mapping_commands in sorted(mapping_list):
			index_dict[str(index)] = mapping_commands.strip().split('&')[-1]
			index += 1

	reloadScreen()
	top_border = "  ~~~~~~~~~~~~~~~~~~~~~~~~~ " + query.upper() + " ~~~~~~~~~~~~~~~~~~~~~~~~~"
	print top_border

	# Print query options
	for group, mapping_list in group_dict.items():
		print " ", group.upper(), '\n'
		for mapping_commands in sorted(mapping_list):
			mapping_name = mapping_commands.strip().split('&')[-1].split('/')[-1].split('.')[0]
			mapping_website = "http://gitlab.cernersphere.net/"+group+"/"+mapping_name
			# Print options
			print (" "*(6-len(str(choice_number))))+"[" + str(choice_number) + "] <-", mapping_name
			if choice_number + 1 < len(index_dict.keys()):
				# Print separator
				if group != index_dict[str(choice_number + 1)].split('/')[-2]:
					print "\n ", ''.join('-' for x in range(len(top_border) - 3)), "\n"
				project = '_'.join(str(x) for x in mapping_name.split('_')[:-1])

				# Group mappings visually
				if len(project.split('_')) <= 2:
					if '_'.join(project.split('_')[:-1]) != '_'.join(str(x) for x in index_dict[str(choice_number + 1)].split('/')[-1].split('.')[0].split('_')[:-1]) and group == index_dict[str(choice_number + 1)].split('/')[-2]:
						print ''
				else:
					if '_'.join(project.split('_')[:3]) != '_'.join(str(x) for x in index_dict[str(choice_number + 1)].split('/')[-1].split('.')[0].split('_')[:3]) and group == index_dict[str(choice_number + 1)].split('/')[-2]:
						print ''
					#if project != '_'.join(str(x) for x in index_dict[str(choice_number + 1)].split('/')[-1].split('.')[0].split('_')[:-1]) and group == index_dict[str(choice_number + 1)].split('/')[-2]:
						#print ''
			choice_number += 1
	print ''

	# Print end border
	print " ", ''.join('~' for x in range(len(top_border) - 3))


def extractHTMLData(_html):
	for multi_line in _html.split('\n'):
		if (
				flag == 's'
				and 'git clone http://gitlab.cernersphere.net/standard'
				in multi_line
		):
			parseHTML(multi_line)
		if (
				flag == 'c'
				and 'git clone http://gitlab.cernersphere.net/' in multi_line
		):
			parseHTML(multi_line)
		if (
				flag == 'a'
				and 'git clone http://gitlab.cernersphere.net/' in multi_line
		):
			parseHTML(multi_line)

def parseHTML(multi_line):
    if multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').strip().split('/')[-2] not in group_dict.keys():
        group_dict[multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').strip().split('/')[-2]] = []
    if len(multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').split('/')[-1].split('.')[0].split('_')[-1]) > 2:
        group_dict[multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').split('/')[-2]].append(
            multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').split('/')[-1].split('.')[0] + "&" + multi_line.strip(
                '<pre class=\'public-clone\'>').strip('</pre>'))
    else:
        print
        group_dict[multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').split('/')[-2]].append(
            multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').split('/')[-1].split('.')[0][:-1] + "0" + multi_line.strip('<pre class=\'public-clone\'>').strip('</pre>').split('/')[-1].split('.')[0][-1] + "&" + multi_line.strip(
                '<pre class=\'public-clone\'>').strip('</pre>'))

def purgeAndClone(_clone_or_overwrite, _branch):
	global rocket_banner, clone_status, mapping_choice
	if _clone_or_overwrite == 'overwrite':
		os.chdir(working_dir)
		delete_command_1 = "del /f /s /q \"" + str(os.path.realpath(folder))+'\\'+_branch + "\" >nul 2>&1"
		delete_command_2 = "rmdir /s /q \"" + str(os.path.realpath(folder))+'\\'+_branch  + "\" >nul 2>&1"
		os.system(delete_command_1)
		os.system(delete_command_2)
		os.chdir(working_dir)
	if not os.path.exists(working_dir+"\\"+str(index_dict[mapping_choice].split('/')[-1].split('.')[0])+"\\"+_branch):
		os.mkdir(working_dir+"\\"+str(index_dict[mapping_choice].split('/')[-1].split('.')[0])+"\\"+_branch)
	os.chdir(working_dir+"\\"+str(index_dict[mapping_choice].split('/')[-1].split('.')[0])+"\\"+_branch)
	pull_command_1 = index_dict[mapping_choice]
	pull_command_1 += ' >nul 2>&1'
	os.system(pull_command_1)
	reloadScreen()
	rocket_banner = "  Cloning " + str(index_dict[mapping_choice].split('/')[-1].split('.')[0]) + " ("+_branch+")"
	if _clone_or_overwrite == "clone":
		if len(_branch) <= 50:
			clone_status = "  ["+mapping_choice+"] Cloned: " +index_dict[mapping_choice].split('/')[-2].upper()+"/"+ index_dict[mapping_choice].split('/')[-1].split('.')[0] +" ("+_branch+")\n"
		else:
			clone_status = "  ["+mapping_choice+"] Cloned: " +index_dict[mapping_choice].split('/')[-2].upper()+"/"+ index_dict[mapping_choice].split('/')[-1].split('.')[0] +" ("+_branch[0:46]+"...)\n"
	elif _clone_or_overwrite == 'overwrite':
		clone_status = "  ["+mapping_choice+"] Overwrote: " +index_dict[mapping_choice].split('/')[-2].upper()+"/"+ index_dict[mapping_choice].split('/')[-1].split('.')[0] +" ("+_branch+")\n"
	clear()
	animate_Rocket(rocket_banner)
	pull_list.append(os.path.realpath(folder))
	if _branch != "master":
		os.chdir(folder+"\\"+_branch+"\\"+index_dict[mapping_choice].split('/')[-1].split('.')[0])
		branch_command1 = "git checkout "+_branch+ " >nul 2>&1"
		os.system(branch_command1)
	time.sleep(1)
	os.chdir(working_dir)

def resizeBuffer():
    left = 0
    #top = 0
    right = 100
    #bottom = 80
    STDOUT = -11
    width = right - left + 1
    #height = bottom - top + 1
    hdl = windll.kernel32.GetStdHandle(STDOUT)
    #rect = wintypes.SMALL_RECT(left, top, right, bottom)  # (left, top, right, bottom)
    #windll.kernel32.SetConsoleWindowInfo(hdl, True, byref(rect))
    bufsize = wintypes._COORD(width, 1750)
    windll.kernel32.SetConsoleScreenBufferSize(hdl, bufsize)


resizeBuffer()
readSettingsFile()
curr_date = date.today()
weekday = calendar.day_name[curr_date.weekday()]
weekday_chance = 30
original_pokemon_list = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran(Female)","Nidorina","Nidoqueen","Nidoran(Male)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr.Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
pokemon_list = ["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran(Female)","Nidorina","Nidoqueen","Nidoran(Male)","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr.Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
pokemon_appeared = False
def print_pokemon(n_pokemon):
    if n_pokemon + 1 == 1:
        print('''                                   
                                 _,.------....___,.' ',.-.
                              ,-'          _,.--\"        |
                            ,'         _.-'              .
                           /   ,     ,'                   `
                          .   /     /                     ``.
                          |  |     .                       \\.\\
                ____      |___._.  |       __               \\ `.
              .'    `---\"\"       ``\"-.--\"'`  \\               .  \\
             .  ,            __               `              |   .
             `,'         ,-\"'  .               \\             |    L
            ,'          '    _.'                -._          /    |
           ,`-.    ,\".   `--'                      >.      ,'     |
          . .'\\'   `-'       __    ,  ,-.         /  `.__.-      ,'
          ||:, .           ,'  ;  /  / \\ `        `.    .      .'/
          j|:D  \\          `--'  ' ,'_  . .         `.__, \\   , /
         / L:_  |                 .  \"' :_;                `.'.'
         .    \"\"'                  \"\"\"\"\"'                    V
          `.                                 .    `.   _,..  `
            `,_   .    .                _,-'/    .. `,'   __  `
             ) \\`._        ___....----\"'  ,'   .'  \\ |   '  \\  .
            /   `. \"`-.--\"'         _,' ,'     `---' |    `./  |
           .   _  `\"\"'--.._____..--\"   ,             '         |
           | .\" `. `-.                /-.           /          ,
           | `._.'    `,_            ;  /         ,'          .
          .'          /| `-.        . ,'         ,           ,
          '-.__ __ _,','    '`-..___;-...__   ,.'\\ ____.___.'
          `\"^--'..'   '-`-^-'\"--    `-^-'`.''\"\"\"\"\"`.,^.`.--' 

         ''')

    elif n_pokemon + 1 == 2:
        print('''                               ,'\"`.,./.
                                      ,'        Y',\"..
                                    ,'           \\  | \\
                                   /              . |  `
                                  /               | |   \\
                     __          .                | |    .
                _   \\  `. ---.   |                | j    |
               / `-._\\   `Y   \\  |                |.     |
              _`.    ``    \\   \\ |..              '      |,-'\"\"7,....
              l     '-.     . , `|  | , |`. , ,  /,     ,'    '/   ,'_,.-.
              `-..     `-.  : :     |/ `   ' \"\\,' | _  /          '-'    /___
               \\\"\"' __.,.-`.: :        /   /._    l'.,'
                `--,   _.-' `\".           /__ `'-.' '         .
                ,---..._,.--\"\"\"\"\"\"\"--.__..----,-.'   .  /    .'   ,.--
                |                          ,':| /    | /     ;.,-'--      ,.-
                |     .---.              .'  :|'     |/ ,.-='\"-.`\"`' _   -.'
                /    \\    /               `. :|--.  _L,\"---.._        \"----'
              ,' `.   \\ ,'           _,     `''   ``.-'       `-  -..___,'
             . ,.  .   `   __     .-'  _.-           `.     .__    \\
             |. |`        \"  ;   !   ,.  |             `.    `.`'---'
             ,| |C\\       ` /    | ,' |(]|            -. |-..--`
            /  \"'--'       '      /___|__]        `.  `- |`.
           .       ,'                   ,   /       .    `. \\
             \\                      .,-'  ,'         .     `-.
              x---..`.  -'  __..--'\"/\"\"\"\"\"  ,-.      |   |   |
             / \\--._'-.,.--'     _`-    _. ' /       |     -.|
            ,   .   `-..__ ...--'  _,.-' | `   ,.-.  ;   /  '|
           .  _,'         '\"-----\"\"      |    `   | /  ,'    ;
           |-'  .-.    `._               |     `._// ,'     /
          _|    `-'   _,' \"`--.._________|        `,'    _ /.
         //\\   ,-._.'\"/\\__,.   _,\"     /_\\__/`. /'.-.'.-/_,`-' 
         `-\"`\"' v'    `\"  `-`-\"              `-'`-`  `''')

    elif n_pokemon + 1 == 3:
        print('''                           _._       _,._
                                 _.'   `. ' .'   _`.
                         ,\"\"\"/`\"\"-.-.,/. ` V'\\-,`.,--/\"\"\".\"-..
                       ,'    `...,' . ,\\-----._|     `.   /   \\
                      `.            .`  -'`\"\" .._   :> `-'   `.
                     ,'  ,-.  _,.-'| `..___ ,'   |'-..__   .._ L
                    .    \\_ -'   `-'     ..      `.-' `.`-.'_ .|
                    |   ,',-,--..  ,--../  `.  .-.    , `-.  ``.
                    `.,' ,  |   |  `.  /'/,,.\\/  |    \\|   |
                         `  `---'    `j   .   \\  .     '   j
                       ,__`\"        ,'|`'\\_/`.'\\'        |\\-'-, _,.
                .--...`-. `-`. /    '- ..      _,    /\\ ,' .--\"'  ,'\".
              _'-\"\"-    --  _`'-.../ __ '.'`-^,_`-\"\"\"\"---....__  ' _,-`
            _.----`  _..--.'        |  \"`-..-\" __|'\"'         .\"\"-. \"\"'--.._
           /        '    /     ,  _.+-.'  ||._'   \"\"\"\". .          `     .__\\
          `---    /        /  / j'       _/|..`  -. `-`\\ \\   \\  \\   `.  \\ `-..
         ,\" _.-' /    /` ./  /`_|_,-\"   ','|       `. | -'`._,   L  \\ .  `.   |
         `\"' /  /  / ,__...-----| _.,  ,'            `|----.._`-.|' |. .` ..  .
            /  '| /.,/   \\--.._ `-,' ,          .  '`.'  __,., '  ''``._ \\ \\`,'
           /_,'---  ,     \\`._,-` \\ //  / . \\    `._,  -`,  / / _   |   `-L -
            /       `.     ,  ..._ ' `_/ '| |\\ `._'       '-.'   `.,'     |
           '         /    /  ..   `.  `./ | ; `.'    ,\"\" ,.  `.    \\      |
            `.     ,'   ,'   | |\\  |       \"        |  ,'\\ |   \\    `    ,L
            /|`.  /    '     | `-| '                  /`-' |    L    `._/  \\
           / | .`|    |  .   `._.'                   `.__,'   .  |     |  (`
          '-\"\"-'_|    `. `.__,._____     .    _,        ____ ,-  j     \".-'\"'
                 \\      `-.  \\/.    `\"--.._    _,.---'\"\"\\/  \"_,.'     /-'
                  )        `-._ '-.        `--\"      _.-'.-\"\"        `.
                 ./            `,. `\".._________...\"\"_.-\"`.          _j
                /_\\.__,\"\".   ,.'  \"`-...________.---\"     .\".   ,.  / \\
                       \\_/\"\"\"-'                           `-'--(_,`\"`-` ''')

    elif n_pokemon + 1 == 4:
        print('''              _.--\"\"`-..
                     ,'          `.
                   ,'          __  `.
                  /|          \" __   \\
                 , |           / |.   .
                 |,'          !_.'|   |
               ,'             '   |   |
              /              |`--'|   |
             |                `---'   |
              .   ,                   |                       ,\".
               ._     '           _'  |                    , ' \\ `
           `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|
           |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\
         -:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .
           `,         \"\"\"\"'     `.              ,'         |   |  ',,
             `.      '            '            /          '    |'. |/
               `.   |              \\       _,-'           |       ''
                 `._'               \\   '\"\\                .      |
                    |                '     \\                `._  ,'
                    |                 '     \\                 .'|
                    |                 .      \\                | |
                    |                 |       L              ,' |
                    `                 |       |             /   '
                     \\                |       |           ,'   /
                   ,' \\               |  _.._ ,-..___,..-'    ,'
                  /     .             .      `!             ,j'
                 /       `.          /        .           .'/
                .          `.       /         |        _.'.'
                 `.          7`'---'          |------\"'_.'
                _,.`,_     _'                ,''-----\"'
            _,-_    '       `.     .'      ,\\
            -\" /`.         _,'     | _  _  _.|
             \"\"--'---\"\"\"\"\"'        `' '! |! /
                                     `\" \" -' 

         ''')

    elif n_pokemon + 1 == 5:
        print('''                      ,-'`\\
                           _,\"'    j
                    __....+       /               .
                ,-'\"             /               ; `-._.'.
               /                (              ,'       .'
              |            _.    \\             \\   ---._ `-.
              ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.
              l'    \\ ,'._,\\ `.    .              /       ,--. l
           .,-        `._  |  |    |              \\       _   l .
          /              `\"--'    /              .'       ``. |  )
         .\\    ,                 |                .        \\ `. '
         `.                .     |                '._  __   ;. \\'
           `-..--------...'       \\                  `'  `-\"'.  \\
               `......___          `._                        |  \\
                        /`            `..                     |   .
                       /|                `-.                  |    L
                      / |               \\   `._               .    |
                    ,'  |,-\"-.   .       .     `.            /     |
                  ,'    |     '   \\      |       `.         /      |
                ,'     /|       \\  .     |         .       /       |
              ,'      / |        \\  .    +          \\    ,'       .'
             .       .  |         \\ |     \\          \\_,'        / j
             |       |  L          `|      .          `        ,' '
             |    _. |   \\          /      |           .     .' ,'
             |   /  `|    \\        .       |  /        |   ,' .'
             |   ,-..\\     -.     ,        | /         |,.' ,'
             `. |___,`    /  `.   /`.       '          |  .'
               '-`-'     j     ` /.\"7-..../|          ,`-'
                         |        .'  / _/_|          .
                         `,       `\"'/\"'    \\          `.
                           `,       '.       `.         |
                      __,.-'         `.        \\'       |
                     /_,-'\\          ,'        |        _.
                      |___.---.   ,-'        .-':,-\"`\\,' .
                           L,.--\"'           '-' |  ,' `-.\\
                                                 `.' ''')

    elif n_pokemon + 1 == 6:
        print('''                 .\"-,.__
                          `.     `.  ,
                       .--'  .._,'\"-' `.
                      .    .'         `'
                      `.   /          ,'
                        `  '--.   ,-\"'
                         `\"`   |  \\
                            -. \\, |
                             `--Y.'      ___.
                                  \\     L._, \\
                        _.,        `.   <  <\\                _
                      ,' '           `, `.   | \\            ( `
                   ../, `.            `  |    .\\`.           \\ \\_
                  ,' ,..  .           _.,'    ||\\l            )  '\".
                 , ,'   \\           ,'.-.`-._,'  |           .  _._`.
               ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\
             .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.
             |  '          ..         `-...-\"  |  `-'      / /        . `.
             | /           |L__           |    |          / /          `. `.
            , /            .   .          |    |         / /             ` `
           / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\
          / .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.
         .  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\
         ' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`
         |'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\
         ||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|
         ||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||
         || '              V      / /           `   | `   ,'   ,' '.    !  `. ||
         ||/            _,-------7 '              . |  `-'    l         /    `||
         . |          ,' .-   ,' ||               | .-.        `.      .'     ||
          `'        ,'    `\".'    |               |    `.        '. -.'       `'
                   /      ,'      |               |,'    \\-.._,.'/'
                   .     /        .               .       \\    .''
                 .`.    |         `.             /         :_,'.'
                   \\ `...\\   _     ,'-.        .'         /_.-'
                    `-.__ `,  `'   .  _.>----''.  _  __  /
                         .'        /\"'          |  \"'   '_
                        /_|.-'\\ ,\".             '.'`__'-( \\
                          / ,\"'\"\\,'               `/  `-.|\" ''')

    elif n_pokemon + 1 == 7:
        print('''               _,........__
                     ,-'            \"`-.
                   ,'                   `-.
                 ,'                        \\
               ,'                           .
               .'\\               ,\"\".       `
              ._.'|             / |  `       \\
              |   |            `-.'  ||       `.
              |   |            '-._,'||       | \\
              .`.,'             `..,'.'       , |`-.
              l                       .'`.  _/  |   `.
              `-.._'-   ,          _ _'   -\" \\  .     `
         `.\"\"\"\"\"'-.`-...,---------','         `. `....__.
         .'        `\"-..___      __,'\\          \\  \\     \\
         \\_ .          |   `\"\"\"\"'    `.           . \\     \\
           `.          |              `.          |  .     L
             `.        |`--...________.'.        j   |     |
               `._    .'      |          `.     .|   ,     |
                  `--,\\       .            `7\"\"' |  ,      |
                     ` `      `            /     |  |      |    _,-'\"\"\"`-.
                      \\ `.     .          /      |  '      |  ,'          `.
                       \\  v.__  .        '       .   \\    /| /              \\
                        \\/    `\"\"\\\"\"\"\"\"\"\"`.       \\   \\  /.''                |
                         `        .        `._ ___,j.  `/ .-       ,---.     |
                         ,`-.      \\         .\"     `.  |/        j     `    |
                        /    `.     \\       /         \\ /         |     /    j
                       |       `-.   7-.._ .          |\"          '         /
                       |          `./_    `|          |            .     _,'
                       `.           / `----|          |-............`---'
                         \\          \\      |          |
                        ,'           )     `.         |
                         7____,,..--'      /          |
                                           `---.__,--.''')

    elif n_pokemon + 1 == 8:
        print('''     __                                _.--'\"7
             `. `--._                        ,-'_,-  ,'
              ,'  `-.`-.                   /' .'    ,|
              `.     `. `-     __...___   /  /     - j
                `.     `  `.-\"\"        \" .  /       /
                  \\     /                ` /       /
                   \\   /                         ,'
                   '._'_               ,-'       |
                      | \\            ,|  |   ...-'
                      || `         ,|_|  |   | `             _..__
                     /|| |          | |  |   |  \\  _,_    .-\"     `-.
                    | '.-'          |_|_,' __!  | /|  |  /           \\
            ,-...___ .=                  ._..'  /`.| ,`,.      _,.._ |
           |   |,.. \\     '  `'        ____,  ,' `--','  |    /      |
          ,`-..'  _)  .`-..___,---'_...._/  .'      '-...'   |      /
         '.__' \"\"'      `.,------'\"'      ,/            ,     `.._.' `.
           `.             | `--........,-'.            .         \\     \\
             `-.          .   '.,--\"\"     |           ,'\\        |      .
                `.       /     |          L          ,\\  .       |  .,---.
                  `._   '      |           \\        /  .  L      | /   __ `.
                     `-.       |            `._   ,    l   .    j |   '  `. .
                       |       |               `\"' |  .    |   /  '      .' |
                       |       |                   j  |    |  /  , `.__,'   |
                       `.      L                 _.   `    j ,'-'           |
                        |`\"---..\\._______,...,--' |   |   /|'      /        j
                        '       |                 |   .  / |      '        /
                         .      .              ____L   \\'  j    -',       /
                        / `.     .          _,\"     \\   | /  ,-','      ,'
                       /    `.  ,'`-._     /         \\  i'.,'_,'      .'
                      .       `.      `-..'             |_,-'      _.'
                      |         `._      |            ''/      _,-'
                      |            '-..._\\             `__,.--'
                     ,'           ,' `-.._`.            .
                    `.    __      |       \"'`.          |
                      `-\"'  `\"\"\"\"'            7         `.
                                             `---'--.,'\"`' ''')

    elif n_pokemon + 1 == 9:
        print('''                       _
                     _,..-\"\"\"--' `,.-\".
                   ,'      __.. --',  |
                 _/   _.-\"' |    .' | |       ____
           ,.-\"\"'    `-\"+.._|     `.' | `-..,',--.`.
          |   ,.                      '    j 7    l \\__
          |.-'                            /| |    j||  .
          `.                   |         / L`.`\"\"','|\\  \\
            `.,----..._       ,'`\"'-.  ,'   \\ `\"\"'  | |  l
              Y        `-----'       v'    ,'`,.__..' |   .
               `.                   /     /   /     `.|   |
                 `.                /     l   j       ,^.  |L
                   `._            L       +. |._   .' \\|  | \\
                     .`--...__,..-'\"\"'-._  l L  \"\"\"    |  |  \\
                   .'  ,`-......L_       \\  \\ \\     _.'  ,'.  l
                ,-\"`. / ,-.---.'  `.      \\  L..--\"'  _.-^.|   l
          .-\"\".'\"`.  Y  `._'   '    `.     | | _,.--'\"     |   |
           `._'   |  |,-'|      l     `.   | |\"..          |   l
           ,'.    |  |`._'      |      `.  | |_,...---\"\"\"\"\"`    L
          /   |   j _|-' `.     L       | j ,|              |   |
         `--,\"._,-+' /`---^..../._____,.L',' `.             |\\  |
            |,'      L                   |     `-.          | \\j
                     .                    \\       `,        |  |
                      \\                __`.Y._      -.     j   |
                       \\           _.,'       `._     \\    |  j
                       ,-\"`-----\"\"\"\"'           |`.    \\  7   |
                      /  `.        '            |  \\    \\ /   |
                     |     `      /             |   \\    Y    |
                     |      \\    .             ,'    |   L_.-')
                      L      `.  |            /      ]     _.-^._
                       \\   ,'  `-7         ,-'      / |  ,'      `-._
                      _,`._       `.   _,-'        ,',^.-            `.
                   ,-'     v....  _.`\"',          _:'--....._______,.-'
                 ._______./     /',,-'\"'`'--.  ,-'  `.
                          \"\"\"\"\"`.,'         _\\`----...' 
                                 --------\"\"'

         ''')

    elif n_pokemon + 1 == 10:
        print('''                   _,........_
                        _.-'    ___    `-._
                     ,-'      ,'   \\       `.
          _,...    ,'      ,-'     |  ,\"\"\":`._.
         /     `--+.   _,.'      _.',',|\"|  ` \\`
         \\_         `\"'     _,-\"'  | / `-'   l L\\
           `\"---.._      ,-\"       | l       | | |
               /   `.   |          ' `.     ,' ; |
              j     |   |           `._`\"\"\"' ,'  |__
              |      `--'____          `----'    .' `.
              |    _,-\"\"\"    `-.                 |    \\
              l   /             `.               F     l
               `./     __..._     `.           ,'      |
                 |  ,-\"      `.    | ._     _.'        |
                 . j           \\   j   /`\"\"\"      __   |          ,\"`.
                  `|           | _,.__ |        ,'  `. |          |   |
                   `-._       /-'     `L       .     , '          |   |
                       F-...-'          `      |    , /           |   |
                       |            ,----.     `...' /            |   |
                       .--.        j      l        ,'             |   j
                      j    L       |      |'-...--<               .  /
                      `     |       . __,,_    ..  |               \\/
                       `-..'.._  __,-'     \\  |  |/`._           ,'`
                           |   \"\"       .--`. `--,  ,-`..____..,'   |
                            L          /     \\ _.  |   | \\  .-.\\    j
                           .'._        l     .\\    `---' |  |  || ,'
                            .  `..____,-.._.'  `._       |  `--;\"I'
                             `--\"' `.            ,`-..._/__,.-1,'
                                     `-.__  __,.'     ,' ,' _-'
                                          `'...___..`'--^--' ''')

    elif n_pokemon + 1 == 11:
        print('''                                   ,--..
                                           /     `.
                                          /|       `.
                                         / |        |
                                        /  j        |
                                       /  |         `
                                      '  ,'          \\
                                    ,'                L
                                   /                  +
                                 .:.                   .      `
                              ,\"`.  `.       ,..-._    +
                              |  |`.  L     '   _.'`.   .
                              j  `.,\\ '    | ,.' |  +.  +
                             '`.    |,'    |\" `\"\"   / `, .
                            |   `\"\"'/      `-.____.'    \\|
                          ,'|     ,'                     Y
                         /  |    /                      '|
                        /   |  ,'                     ,' +
                       /    \\-'                      /    `
                      /    /                       ,'      `
                     .     ,`'-.                 ,'         L
                      \\   /     \\               /            .
                         /      `               \\            |
                       `/          _,            `          ,'
                        |                         `       ,'
                        |           \"'             `.   ,'
                        j         -\"'               |`-'
                       /                           /'/
                      /           ,               / /
                     /            '              j /
                   .' ___                        '/
                   |-'   `\"`-.                  '/
                   '          \\                .'
                 ,\"            l          _,.-'
                ,---..         |L     _.-'
              ,'      `.      / |  ,-'
             /          `  _,'  ;-'
           ,'--.       ,-`|  ,-'
          /     L   _,'  _|-'
         (       \\-' _,-'
          `......^.-' 

         ''')

    elif n_pokemon + 1 == 12:
        print('''       ,-.                                            ___.._
          _     `. `.                                    _,-\"\"\"      ',._
         `.`.      `.\\                                _,'         _..-'  `.
           `._\\       `.                            ,'         _,'_,.-'-.  \\
               `.       `.                        ,'        ,-',-\"       \\  .
                 `.       \\                      /  _,----\"',-'           L  L
                   `.      \\                   ,' _.--\"-.  [              |  |
                     `.     .                 / ,'       | |     _..---../   |
                       .     L               / /         | j ,.-'        `   |
                        \\    .              ' /          j ,'             |  |
                         \\    .            ' /          ' /               |  |
                          \\   l           / /          /,'                j  '
                           L__L._        / /          +'      __,........'  j
                         ,'   '  \"`.    / /         .' _,.--'\"           \\  |
                        /,\"\"-.      `. ' '        _/.-'                  | F
                       /|   / l       . /       ,'                       | |
                      | |  /  |       ]'      ,'                         | |
                     ,._\\\"'   |       |     ,'-'\"\"\"\"\"\"\"\"\"\"\"\"\"'----.._    / |
                     |  \\`.._,'       F  _,'                         `--'  |
                     `..'           _/ ,:_____                         L   |
                       `..          .-'       `'--.._                   | j
                     _,. /,---.       \\              `--..              | |
                    F  <j-.'   `       ._                 `\"-._        j  '
                    |  <|`,.    |       `L._                   `..   _, ,'
                    `..<|`.___,'        |.  `-.                   Y\"' _.
                       `L               | `.   `-.._____________,',.-'
                         `.            .Y   \\      `\"\".\"\"\"\"\".  .\"'
                           `.        ,' |\\   `.        `+-._ \\  |
                             `,--. -'   | .    `.       `   `.| |
                             /    //    |  \\    ``-..___/     | |
                            j    .l     |   .    F   \\   `   F  |
                            |    ||     |    `   `    .   ` ,  /
                            |    ||    F      `-.|     . _,' _'
                            |   / |    |       `._`-----'  ,'
                            |  /  |   /           `-------'
                            l /   \\_,'
                             \" ''')

    elif n_pokemon + 1 == 13:
        print('''               ,`.
                        L  \\
                       ,    \\
                      j      \\
                      ,       \\
                     j         `
                     ,          .__
                  ,-'Y          `  `-.
               .-'    `..___..-'      `-.
              /__           ,-.          \\
             /(__)         `   '          `.
            |               `\"'             L
            `.------._                      |
          ,'          `                     |
         F             |                    |
         |             |                    |
         `._         ,'                     j
            `+------'                      /
              \\                           /                         |`._
               `.                       ,'                          |   \\
                 `._                _,-'                            |    \\
                    `-,.________,.-'   `.                           |     L
                     /                   '                          |     |
                    /             _,._   |                          ,`---,'
                  ,'|            /    .  j                        .'      `.
                  . L            '    | ,                      ,-'\"'`-..   |
                   .,\\            `--' / `.               ___./       ,.' ,'
                      \\              ,'    \\__         ,-'     \"-.    | |'
                       `-._______,.-'  __   | `'-._.,- ._        _`   `\"Y
                         |           .\"  \\  |     \\      `.    ,'  \\   ,'
                         |           '    | ;      .       .   `._./.-'
                         7.           `'\"' / `.--. |   _.. |      j
                         `.__       `   _-'   |   |j  /   ||     .'
                             `-...,_..-'      `--'/   `._, ^----'
                                  .\\            _'       ,'
                        `         `._-.______,.'`.___,.-'
         ''')

    elif n_pokemon + 1 == 14:
        print('''           _,--'\"\"\"\"\"\"---.._
                  ,'                 `._
                ,'                      `.
              ,'                          \\
             .                             \\
           ,'.                  ,-`.        \\
          /   \\               ,'    ,        \\
         |`.  |\\            ,`      |         |
         L  `.| |         .''     _,'        _'
          \\    \"'        ,`'_..-''        _,'
           `.            '\"\"          _,.' `.
             /._                 _..-\"       \\
            /   `.          _,.-'             \\
           /      \\-.___.--'/                  \\
          |      ,/.     .-^+.._               F
           L..-''.' \\  .'   |   `'--.....___   .
           /     /   `/     |               `\"-;
          /     j    j      '                ,'
          `.    |    |       L          _.-'Y
           ,`._/     |        .    _,.-'     .
           `.  '|    |         \\\"\"\"|         |
            |   |    |         |   |         |
            |   |    |        ,'   |         |
            |   L    +      ,'     |         |
            |    \\    L    ,\\      j         |
            L     \\   |   /  `.   /          j
             \\    j\\  |  /    `. /          .
              L  .  ` | /       \\          /
              +  |   `|/                  /
               \\ | _,..._         \\      /
                ./'      `-._      \\   ,'
                 l           `.     ^_/
                 +             `   /
                  L-\"\"--.       .,'
                  |      `.     ,
                  .        \\  ,'
                   `       _.'
                    `....-' ''')

    elif n_pokemon + 1 == 15:
        print('''                     ,--\"\"+--.
                             /     j   /`.
                            |     /   |   `.
                            |   ,'    '     \\
                            j,-'     '`..    \\
                           +      _ /    `._/ \\
                           |     / '-.     |   .
                           |    /     |   /    |
                           |   /     j   j     |
                           |  j      |   |     |._
                           | .'     7    |     |  `.
           ___      _.._   | j      |    +     '    `.
          |.---=-.,'+-. `. |/       F     L  ,'    ,'`.
          ||,==--'|_' |  j  \\      /      |,'   ,`'    L
          'Y'   | |  '/ ',.-.\\    j     ,,^  _,' \\     |
         `.||   |  `.'  '    `.   / _,-'   `'     L   F
           ||   `     .  ,-.   `,--'              |   |
           `'    `.  /_,' ,'     `--------------\"\"\"\"'Y
                  _:\"'_.-'       /_>:-.__           /
               `-\".`\"'__,`-.,-._/      `.\"\"`------\"'
               `.| `\"'      | | _.--'\"\"'--\\
                || /        | '\"  ___,.._  \\
               _|||__      / /,.-'       `- .
             ,'   `. .    /,'/'  _.,-\"\"\"--._F
             7     | |  .',L'|_-'           |
             +     | | / / ',\"'  ,.-'\"\"'`-._|
              L    ' |. /  .-.`\"'           |
              |   j j   \\  `-.'\\           j
              +   | | \\  `.   ` `.  _.... ,
               L  | |  \\   .   `  \\\"     /
               | ,' |   L  ,'    \\ `    .
               | || |   '  |      L `   |
               `./|j     `. .     `. \\ j
                |  '       ` .     | '\\`
                            \\ '.   | \\
                             | |  /,-'
                             j l  \"
                           _/_,'
                          ',' ''')

    elif n_pokemon + 1 == 16:
        print('''                   .,
                     , _.-','
                   \"\"|\"    `\"\"\"\".,
                  /'/       __.-'-\"/
                 ','  _,--\"\"      '-._
             _...`...'.\"\"\"\"\"\".\\\"\"-----'
          ,-'          `-.) /  `.  \\
         +---.\"-.    |     `.    .  \\
              \\  `.  |       \\   |   L
               `v  ,-j        , .'   |
              .'\\,' /        /,'      -._
             ,____.'        .            `-.
                 |         /                `-.
                /          `.                  `-.
               /             `. |                 `.                  _.
              .                `|                 ,-.             _.-\" .
             j                  |                 |  \\         _.'    /
             .                  |               .'    \\     ,-'      /
             |                  |            ,-.\\      \\  ,'      _.-
             |                . '  `.       |   `      `v'  _,.-\"/
             ||    \\          |  ` |(`'-`.,.j         \\ `.-'----+---.
             |'|   |L    \\  | |   `|   \\'              L \\___      /
             ' L   |`     L | |     `.                 | j   `\"\"\"-'
                `-'||\\    | ||j       `.       ._    ` '.
                   `\\ '\"`^\"- '          `.       \\    |/|
                     `._                  `-.     \\   Y |
             __,..-\"\"`..`._                  `-._  `\\ `.|
            +.....>+----.' \"\"----.........,--\"\"\" `--.'.'
                ,' _\\  ,..--.-\"' __>---'  |
               --\"\"  \"'  _.\" }<\"\"          `---\"\"`._
                        /...\"  L__.+--   _,......'..'
                          /.-\"\"'/   \\ ,-'
                              .' ,-\"\"'
                             /.-' ''')

    elif n_pokemon + 1 == 17:
        print('''                        |
                            ____ A,
                        _,-'\\  || /`'`.
                       /-.   '.'|    ,'-.
                     .'   `. |/j | ,'    ..
                    .\"\"|._  \\` | ,'  _.,\\--.
                    '/ |  |\"\\\\,| |,\"| |  |  \\
                    |.'_..|().\\../()|_/\\ |\\ |'
                    | |     ,'   `    L \\| Y
                    | '    /.-\"\"-.`    |||  \\
                    . |   |_,-----.|   j||  `
                    | .   . .     ,'  /,'/
                  __|  \\   \\ \\__,'/  // j
              _,'\" ,'   `._ `.__.'  ,'  |---._
            ,'    .        `\"----\"\"'    .     `.
           ,     .                       `      `
          /     /    ,-\"\"\"\"\"\"\"\"\"\"\"\"\"--._  \\      '
          |    j   ,'                   `. `     |
         |'.'  |  /                       `.|    |
         | `.  /.'                          \\  | |
         L  `'v'/                            . |,|
          \\   '|                             | 'j
               |                             ./ /
           `   '                             j /
            `  `                            / /
             `. .                          / /
               `.`.                       /,'
                  \\`.                   ,',
                   . `                 .-
                    `.  +.       _,.- ,'
                     |`-| `\"--\"\"' `,'-|
                    ,'  | _      _ |  |
            ,--...-'    `' |> <(\"     |-..__,..
          ,'    _.+- ,  +..'    --.  .  `.___  '
         `-\"\"--:-' ,' |  `.       |   `..   .||_\\
              /\"|_'   `.,-|       | _.|  `-.'_\\ `
              .'        | |        ` ||
                         '          V' ''')

    elif n_pokemon + 1 == 18:
        print('''                   ..-`\"-._
                          ,'      ,'`.
                        ,f \\   . / ,-'-.
                       '  `. | |  , ,'`|
                      `.-.  \\| | ,.' ,-.\\
                       /| |. ` | /.'\"||Y .
                      . |_|U_\\.|//_U_||. |
                      | j    /   .    \\ |'
                       L    /     \\    .j`
                        .  `\"`._,--|  //  \\
                        j   `.   ,'  , \\   L
                   ____/      `\"'     \\ L  |
                ,-'   ,'               \\|'-+.
               /    ,'                  .    \\
              /    /                     `    `.
             . |  j                       \\     \\
             |F   |                        '   \\ .
             ||  F                         |   |\\|
             ||  |                         |   | |
             ||  |                         |   | |
             `.._L                         |  ,' '
              .   |                        |,| ,'
               `  |                    '|||  j/
                `.'    .             ,'   /  '
                  \\\\    `._        ,'    / ,'
                   .\\         ._ ,'     /,'
                     .  ,   .'| \\  (   //
                     j_|'_,'  |  ._'` / `.
                    ' |  |    |   |  Y    `.
             ,.__  `; |  |-\"\"\"^\"\"\"'  |.--\"\"`
          ,--\\   \"\"\" ,    \\  / \\ ,-     \"\"\"\"---.
         '.--`v.=:.-'  .  L.\"`\"'\"\\   ,  `.,.._ /`.
              .L    j-\"`.   `\\    j  |`.  \"'--\"\"`-'
              / |_,'    L ,-.|   (/`.)  `-\\.-'\\
             `-\"\"        `. |     l /     `-\"`-'
                           `      `- ''')

    elif n_pokemon + 1 == 19:
        print('''                                      ,'\"\"`--.
                                              |     __ `-.
                                              |    /  `.  `.
                                               \\        ,   `.
                                                `.      \\_    `.
                                                  `.    | `.    \\
                                                    `--\"    `.   `
                                                              `.  `
                          ,.._                                  \\  `
                        /_,.  `.                                 \\  `
                       j/   .   \\                  ___            \\  \\
                       |    |   `____         _,--'   `.           .  L
                        L  /`--\"'    `'--._ ,'   ,-`'\\ |            . |
                         |-                /  ,''     ||            | |
              -v._      /                   ,'        ||            | |
                `.`-._,'               _     \\        |j    _,...   | |
                  `,.'             _,-. \\     |      /,---\"\"     `- | |
                 .'              ,\".   ||     `..___/,'            `' |
                 |   ,         _/`-'  /,'                            `|
                 |-.__.-'\"''\"\"' \"\"\"\"\"\"\"\"--`_,...-----'*'--...--      `.
                  `.____,..              \"\"   __,..---\"\"\"              |
                   |       `              --\"'.                        `
                   |     ,' `._                \\'                       `
                   | |  .^.    `.             /                          `.
                  ,'_]__|  \\   / `.          /          /____._            `._
                ,'          \\ j    '        /          /       `.             `.
          ___,.' `._       __L/    |     __'          /     _, / \\             |
         `-._       L,.-\"\"\"  .    ,' _.-','          /-----'-./   `--.         |
            '   / ,'         '..'\"_,'    /         F /  .\"'_,'        |.__     '
           / ,.\\,'              \"\"      /         / (,'\\ .'        ,.-\"'  `.  j
           -'   '                      /        ,'     `\"         / __/' .- ,'
                                    __.'\"`.    /                 `-' | _,L,'
                                  .',      `\"\"'                      '/,--
                                   / _..' _,,'
                                   ,' `-\"' ''')

    elif n_pokemon + 1 == 20:
        print('''                        |.     .|
                               `.  `._.' |,'Y'     _.......
               +--------..  _\\\"'  \"\"\"\"\"\"'--.=-_ ,-'  ,.-- '     .
                |  '\"\"`.  `.`-._           .-\" |   .'    (      |`
                j       \\  |..'-- ,-----. ,.]..|  /       `.    L .
           ____(___     |      _.' -  , `--..    | __.....-/-..__|L
         .'._______\"\"\"\"----  ,'   _____._    ` ,-':,...------\"\"\"\"i .
                  |\"\"\"\"-.  -'    '.     /`    ' -------.j__      | |
              .,--------        / \\    j  L      `=..-\"\"----'    | |
                    ,-_,.-     j   L | |   .     `-..:-.__       | |
                 ,++-.  |      |   /-+-|   |       | `\"-._`._    | |
               .+\"\" '- .'      L  j  | L   j       | L    `-.`.  F-|
             ,'    .-) `,       \\_/     \\ /        j  \\       ` /-.|
            '        |  .        `.......-        /   j_       j  j
                  .--|  ,\\_                      ,'\". / )     ,^-.|
                   `.`,-                        /  / / ,`._  ,.   F
                \"\"\"| '  .'`.'                   `-'\\ \"'  \\ \\,  \\ /
               | j`.    |     . ,. .,..  ,_  .     `...-.| |.  ,'
               `-'  /\"\"/    ,' .' \\ '  `/. `-       Y   |`\"  `/
                   j  /'                             .  | \\ ,'
                    \\ \\                              |  | ,'
                    ' '                              j j-'
                     `.\\                            ,.'
                     _+.`.                       _.,---.._    _
            ,-\"\"--.,'   `--.._              ,::`\"-        '\"\"' -.
          .'  _..--          ,`\"`--------\"\"'  `._    ....<\"\"`-\",.'
          `-\"'   _,-\"\"'  _,-'                    `-..__   v._  `.
            / ,-'/  _,-`'                              `-. \\ `-.|
            -'  |_,'                                      \"' ''')

    elif n_pokemon + 1 == 21:
        print('''               _,
                      .'.'  _.
                    ,' ._,-'_\"'
                 _,'   '  ------\"\"'`._
               ,'                 _,.--\"'              ___        __,..
               |    _,..       ,-'             _,.--\"\"'   7_,.--\"'    ,'
               j. .'D  |       |            ,'\"       _.-'       _.-\"\"'.  _,..-\"'
          ,---'  `+----'       |`._      _.'         '                '.-'      /
         j         `.       ,-'    `'--,\"                           ,'       ,-'
         |    __    |      '-.._,    .'                           ,'     ,.-'
         `. ,' ('T--'        .\"     /                          _.'  _,--\"
           `   `,  /         _`.   j                         _', ,-\"__,..,-.
               `-\"`.        \\   `-.|                        _,'\"\"\"\"'       l
                    `.,      \\     L                     _.'      __,...--'
                     ` '-    .`     `._             _,.-' ,--'\"\"\"\"
                      '  \\`.,\\         `+------,--\"'     /
                          \\ )`'      ,-'      /         /
                           `     _,-'       ,'         /
                            `+\"\"'         ,'     ,.  ,'
                              `.        ,'     ,'   .
                                `-._.,-'      /. _.,j
                                    \"\"`-----.'  '  /
                                         / /   /  /
                             _.......__,' /__,' ,'
                           ,\\  ,--..--------\"_  ...._
                          '--\"(_,`|  ,..-' _,....__  |.
                                 '-./...-'\"        `\"\"\"- ''')

    elif n_pokemon + 1 == 22:
        print('''    ,---...__     ,.._
           .\"\"\"_...   \"\"---\\.,_`\"-._                    __,..._
          ,--   \"\"\"\"\"\":--..    \"-   `-._ _,.        ,-\"\" ..----'\"\"\",
         `---........_____ ._     `-._  `. |       / /'      '\"\"\"\"-----.
         \\\"'\"\"\"\"\"\"''\"\"\"'\"-`           `-. `.      / j     .\\ |\\   -.,:,- .
          `-.......___     `._           \\  \\    ]\\ |   . |L ||/\\   `. ` .`.
                  __,..==--'/ '           \\  L  A|,'|    \\| |||||  ` .`.. -._
             .--\"\"          `.             L | j  /'\"-.__\\V '/|||   | `. `._ `.
               `....----_..-`\"`/.          | | | j   __ `._   | |'_`.\\  `.  `. |
                     -\"'       \\           | `_|.   l  `.  `.   |||   ` | `   \\'
                     `-._,...-\"\"\\-         |        |    .   /`.  \\  ..Y   `.  \\
                        `-..,'  .`         '         L \\  .  `--\"`.`.`|  .   \\  |
                           \\  ,'  `|     ,'          .\\ +-'-...-^._`. | |..  ,\\ '
                            `\\     `.._ j             /\"       \\  |\\ `..- `.'- `
                             `. ,' | .  |           .'          \\ | `._`.
                               +   | | j           /             `'    `.`.
                                `.+._j_'      __..)                      `..
                                 _,-'   .,   j ` .'\"\"`--.                  `
                              _.' .-'  /,'`\"-.  ,` .\\ \\` `
                            ,'  .' / /`,'    ||'` ,'`T|.`-|
                          ___,'/_,._/        L|   . |'-'\\\"
                                             `-   ||    ' ''')

    elif n_pokemon + 1 == 23:
        print('''        _,--\"\"'\"\"\"-.
               ,'   .,-.     `.
              '`...( |  |      \\
             |      `--'        .
             '_,...__,'          `
              `._                 `
                 `..______         |
                      |.          ,|
                      | `-.....,-\" |
                      |            j
                      ^.         _F
                     /  `-.....-'/
                    /          ,'
                   /          /
                  /          /
                 j       _.-- .
                 |      /     ,+---....___
                 L     /     /            \"\"`-.._
                  \\   j     j                    `-.
                   `. |     |            .'         `
                     `+...__|__       .,+-..         |
                               \"\"`._.l      `.       j
                               ,.-\"   \"-.     L    ,'
                             ,'          L    : _.'
                            /            |   _:'
                           .            .|,-'
                            .            `.._
            '\\               `-.             `\"-.
          ,`.'                  `-.              L
          |  )                     `-. _...__     |
         .'-'                         )      `.   j
         |  |_                      _,'\"\"`.    \\ /
          .-' `+._               _,\"       `.  |/
           \\   |  \"`,,,,,....---'           | .'
            `-.'   /                        |+
               `--+                     _.-'
                   `--.___       __.---'
                          `\"\"\"\"\"\" ''')

    elif n_pokemon + 1 == 24:
        print('''                   _,.----'\"\"\"'---..._
                       _,-'\"                   `-..
                    _,'                            `-.
                  ,'                                  `-.
                ,'                                _,..._ `.
               /                               ,.\"     `:- L
             ,'                             |.'         / ||
            /            _,.-._             L        .-' -,'
           /        _,.-\"      `.            `     __   .'
          j      _,\"           ||\\|           `. ,-  _.'
         .     ,' `-..________.-' |            |' ,-'
         |   .' `--,.___       _,'| /`.        ` '
         |   |     `._  '\"\"\"\"\"'   . `_Y.        Y_
         `._          `-...__      `.`-'        | `-,...___
            ``-,.._          `\"\"--.._`.         |  /     _,+`-._
             .'    '--._             `-+      _ |./    ,\"       \\
            ,  _,...._  `..             `-.:L_,v-'\"`-./_____     L
           .,-\"       `-.| `,                )/       \\     \"`   |
           j             |  \\`\\       _,......|       |       `  |
           |       _,.---^.v[\\_   _,-'        |       |        \\ '
           |     ,\"       _>.. \"\"\"            |       |        _V
           '    .        /  |'`\\              |.._   ,'     _,'
            .  j       ,'    |  `._           |   `\"\"-----\"'
             \\ |      j      '     `--..,,,..j
              Y       |       \\             /
               `.     |        \\           /
                 `.   `         `.      _,'
                   `._ `.         `--..'
                      `---...,,,...-\"' 
         ''')

    elif n_pokemon + 1 == 25:
        print('''                                             ,-.
                                                   _.|  '
                                                 .'  | /
                                               ,'    |'
                                              /      /
                                _..----\"\"---.'      /
          _.....---------...,-\"\"                  ,'
          `-._  \\                                /
              `-.+_            __           ,--. .
                   `-.._     .:  ).        (`--\"| \\
                        7    | `\" |         `...'  \\
                        |     `--'     '+\"        ,\". ,\"\"-
                        |   _...        .____     | |/    '
                   _.   |  .    `.  '--\"   /      `./     j
                  \\' `-.|  '     |   `.   /        /     /
                  '     `-. `---\"      `-\"        /     /
                   \\       `.                  _,'     /
                    \\        `                        .
                     \\                                j
                      \\                              /
                       `.                           .
                         +                          \\
                         |                           L
                         |                           |
                         |  _ /,                     |
                         | | L)'..                   |
                         | .    | `                  |
                         '  \\'   L                   '
                          \\  \\   |                  j
                           `. `__'                 /
                         _,.--.---........__      /
                        ---.,'---`         |   -j\"
                         .-'  '....__      L    |
                       \"\"--..    _,-'       \\ l||
                           ,-'  .....------. `||'
                        _,'                /
                      ,'                  /
                     '---------+-        /
                              /         /
                            .'         /
                          .'          /
                        ,'           /
                      _'....----\"\"\"\"\" ''')

    elif n_pokemon + 1 == 26:
        print('''                                        _,--\"\"`---...__
                                     _.---\"\"\"\"`-'.   .-\"\"\"'`-.._`-._
                         _,.-----.,-\"         .\". `-.           \"---`.
                      _,' _,.-..,'__          `.'  ,-`...._      ,\"\"''`-.
                    ,' ,-'     / (  .   ,-.       |    `.  `-._  .       `.
                  ,',-\"       /   `\"    `\"'       '      .    _`. \\
                ,','       ,-'7--.                 `.__.\"|   ( ` `j
               '.:--.    ,'   |   .       |\\             '    `--'
              /.     | ,'     |   |       `'            .
             '       |',\".    |._,'                     `      _.--\"\"\"\"\"-._
         '.          `-..'    `.                      ,  \\  ,-' _.-\"\"\"\"\"-. `.
         ` `                   F  -.                 /    ,' .-'          `  `
          \\ `                 j     `.              ,-.   . /               . `
             `.               |     .-`.           .  '-.  V                 . `
           `   `.      .      | .    \\  \\         j      \\/|                  ' .
            .    `.    |`.    |-.`._/`   .        |    ,'  A                  | |
             \\     `. F   \\   |--`  \"._  |        `-.-\"   / .                 | |
              \\      -'    `. |        `\"'                  |                 F '
               \\             `+`.                           |                / .
                \\              .-`                     .    j               / ,
                 \\              \\   `.               .'    /               ' .
                  \\       |`._   \\    `-.._        ,'    ,'              ,'.'
                   '      |   `.  `.       `<`\"\"\"\"'    .'             _,'.'
                    `     |     `-. `._      )   `.     .          _.'_.'
                     `    |        `--/     /`-._  .     `.___..--'_.\"
                      `   |          /     /._   `\"\"`.     `. _,.-\"
                       `  |         /     /   `--.....`.     `._
                        ` |       ,'     /              .\"\"\"\"'  `.
                         `'      , `-..,7                `    . `.`.
                                .       '                 `.   \\  `v
                               j.  ,   /                    `.._L_.'
                               || .   /
                               `\"-'__/ 

         ''')

    elif n_pokemon + 1 == 27:
        print('''          _...-----'`._
               _,-'   _`. .\"\". \\`._
             ,'    ,-'   ` ` |  \\/--.
           ,:_  ,-'       ` `|  |`.  `.
          /   `'-..        `  .-'  `   \\
         j         `.--,    \\       `   :
         |         '--' |    \\       `._'-.
         |___     |     |     L      .'    `.
         |   `-. /|___.' `.   |    .'.       .
         |     ,'          .  j.  /   `.      \\
         .  _,'            |,'  `.      \\   ,<`.
          .'             _.-      `      j.'  \\ \\                          ,.
           `       ,v-\"\"'   \\      )__,+'      . \\                       ,' |
            `.    / |  /  _,'`.  ,'  \\  \\       /`.                   _.:   |
              `,-'-`  / ,'     \\'    j,  \\   ,.'   L               ,-'   . F
              / ,. | / .        \\  .'     \\.-\\     |         _,.-\"`.     `,'
              (_\\/|'|   \\        .'   _,-\"    `    +....---+'       `     '
              . \\ |.     \\    ,.^---`<_        | ,'||       \\        \\   /
               `.'| \\_    :v-'         `.      |-  | \\ __..--\\     _,'\\,'
                 `'/`----'/              '.  ,'    |  Y       L_,-'  ,'
                   \\     /            ___,.'\\     j   |       |    .'
                    \\   .\"`\",\"\"'\"\"\"'\"`     | .   .'   |       |  ,'
                     \\  |   |         |    | | .' j,.-|       j-'
                      `. ___|________/.....|_Y'  /    |   _.-'
                   __,-' \\                 |    /    _j,-'
                  '--.    .                `...+---\"\"
                 `_____\\  _`..__    __,..-\"'
                       .-'_|._  `\"\"\"       \\
                      , -'    .          __/
                      \"------------\"\"\"\"\"\" 
         ''')

    elif n_pokemon + 1 == 28:
        print('''                    ,\\
                         _,-'.+..----\"/_____
                      _,'---,        /      `\"\",
                    .'    ,'  __..../_     _,-'
                   /    ,' ,-\"       ,'---+--...__
                 ,'   ----'        ,'             `\"
                '                ,'     ______  ,-\"`-._
               /  ,+\"\"\",   ....-^--..<\"\"      ``-._    `-.
             ,' .'-'  /      |        `._          `-.   _`-
            /    `\"\"\"'       `           `.           `,\"
           |                  `.           `.      ,-'\"--.
           '               ,-   `._ ,-\"\"\"`.__:---\"\"'-._   `._
            `-----..__  _,'     .-\".       `._         `.    `.
            /________.'\"/      /  j         | `-._       `.    `.
         \\`-.`.__    )_/__    ._,-|         |     `.       `.\"\"\"'
          .      `\"\"\"\"j   `\"\"`'   |         |       `.       `.
          \\`._       /            L         '         `.....---
           `  `..___'              \\      ,\"            .   `.
            `.     `              _.\\ _.-\" `-._          `.   `.
              `-._  \\         _,-\"-. '|        .`-.-\"\"\"\"``\\     `.
                  `\"-^'   _.-'        |         \\  `.      `---...-
                       \\.\"            |          L   `.     `.
                       /              `          |     \\      `.
                      j                `.        |      `,....__`
                      |                  \\       |       `   \\
                       .                  .      F        \\   `.
               _,...,---`.                 `.   j `.       L--..`
             ,\",.--\"'-.   -.                _`. |   `._    .
             ,'        \\_.--`._     ,----.-<.  V       `-._ ._
            /.---\"\".-\"\"\" )     `\"\"\"'      `. `-.._         `' `._
                 ,' _.-\"\"\"\"`.               |     `\"-..__        `-.
                 '\"\"         \\         _,..-'            `\"\"----...-'
                  '-----------+---\"\"\"\"\" 

         ''')

    elif n_pokemon + 1 == 29:
        print('''        .'-.                            ,.. _,._
           ,--\"\".`.  `.                        ,'  /'    `-.._
           \\__   `-`   \\                     ,'  ,' _____     `-.
              | ,-.._   \\                  ,'    _,'     \\   ___.'
              j |    `   L               .'    ,'        |  |
             . j      \\  |              /    ,'  ___     |  |
             | |  .\"\"\"|  `    _,.--....'|   /-'\"\"   `.   |  '
             |j  j    `   `-\"\"          '  '         |   | F
             ||  |    ,'                   `         |   | |
             |`. |   /      ,\"\".       .    \\        |   ' |
             `  `.  /,\\     |   \\     / `    \\       |,-' F
              `.  `/ | \\    '    .   /.  |    \\   _,-   ,-'
                `-. j  |\\       \"   /.|  |     `\"\"__..-'
                 .' |_ |(`        ,' )|__'      `._____
         .-------'.   `-'-`       `--\"\"      \"\"\"\"\"__..-'
          \"\"\"\"\"\"--.                           \"\"\"(
              ___.'        .                 -----..._
            .\"____..       '   -'              \"\"`----`_
                   `.     . _._   _,             ,. `./ |
                     >     `.  .\"\".              \\ |  \\ j
                    j       `.,'  /               \"'   Y
                   /          `..'                     |
                                                       |
                  .                             ,\"-.   |
                  |                             |   \\  |
                  |                             .   /  |
                  |                              `-'   |
                  |   `.                           ,   '
                  L     \\                      _  /   /.
                   \\     \\             |      ( `/  .'  `.
                    L     `.           |       \"/ _/    _|
                  _,|       -,_        |       j-'_._  ,  `.
                 '..|       (_.'--.._  L       |-+_  ..`.,.`
                    |      j         \"\" .    __|   `\"'
                    |,..__<             |\"`,\"  \\
                    | _,x..)            '-' --.'
                     \" ''')

    elif n_pokemon + 1 == 30:
        print('''                           _            _
                                   / )  _  _,.-\"\" )
                                 ,' /..' /\"   _,+'--\"`.
                                /     / j_.-\"'     ,-\"
                              ,'    ,'       _____  `
                            _+__   .     _.-'     \\  `...._
                       ,'\"\"\"    \"\"/  _.-'          .       \\
                     ,'          '  ',--'\"\"`-.      L   ,-\"
                   .\"              .'         \\     |  /
                 ,' _                          \\    | j      _
                / ,'   _,+-'                 _,'   ,' /_,.-\"\" |
             _.' '  .+'.  \\               ,-\"___..\"  -'      ,'
          ,-\"     ,'-' |  |           .,-\"\"''___,..-'       /
         j        `\"\"\"\"---'             '\"'\"\"       ._    , _.--\".
         \\   ,                                        `- ' `._  ,'
          \\                            _.-'            .\"`.   `-. ____...----\"\"`
           `.-\"-._,..---+ +          ,'       `         `.'      `.             |
               `.        \\/        ,'          |            ,.---. \\           .
                 `._               +__,...__   |     ,     |     |  L        .'
                    `--...-\"\"`-._   /       `,\"    ,'      `     |  |      ,'
                              /  `./        /    ,'         \\    j  '    .'
                             /    j        /    .       _    `._'     ,-'
                            j     '       /     |     .\" `         ,-'
                            |, .<(       '      `      \\_/       ,'
                            |-...+.___,./`.______\\             ,'
                            `.'`.' \\/  V /_/.___  `.  _     _,'
                                         `....\\_`,-\",' |,-./
                                                 `\"\"..-'---` ''')

    elif n_pokemon + 1 == 31:
        print('''                                          .\"
                                                 ,'  |
                                               _,... '.___
                                      +--._  ,'.-\"+.      \"`-.
                                  _,---\\   `\" / |p|.'     \"'   \\
                                ,- _.---\".   |_,'      ,-\"\"\"\"-._|
                              ,' ,.'    .'          ,-'        ,'
                            ,' ,' |    .          .^---._      |
                     |. _  `. /   .    |   ,---.+'       `.    |
                    ,| | `/\\|.    `    |  .      `-.       .  /
                .---. \"`-`.,\\ \\    `-.,'  |         `-._   | '
                 `.-'        , \"\"\"\"--'..-  \\            `--'.L
                   .          |`.     `     `._             _,'   .
                    `.        |  `.    |_,..   `-..______.-'  _,-| |. ,\"\\
                      -.     /     +--'/    `.            -,\"'   `\"  \".-'
                        `-+-'      |  /       `.        '\\ |           .L_
                    -\"--.,-`._..._,' j          `.     / | '           (_,'
                   `.    j.-'     `- |            \\   j  |  `.  _...___'
                     `. /__ ,...._  \\|             |  |  |...-`\"
                       j|  `      ,-/`.           /   `  ;.._
                   ,-. ||   |\"\"-.'  |  `..__,...-'     \\'    `.
                   `   |/`--    .  /|                  /----.__\\
                    \\  .         `' /                 /         \\
                     . |           ,`.              ,'     ___..+--.
                     +-|          /   `-..______..-\"     ,\"  `.   /___
                   ,'  |         j               .'    ,'      `\"|    /
                ,-+    .         |`._          ,+_    /          `-..'
            _.-'  |     `.      /    ``-----:='   `.,'         _,..'
         ,-'      L       `-.--'         ,,'        |       ,-'
         \\_        \\         `._    _,.-'           `.___..'
           `.._     `._      __.+'\"'
               `---... +---\"\" ''')

    elif n_pokemon + 1 == 32:
        print('''                  .\"\\                            _
                           | |  ,.                    _,-\" /
                           j `-' /                 _.'   /..
                         ,'     |                ,'   _..  |
                        /       `.          .\"','  ,-'   \\ `...
                      .'          \\       ,' ,' ,-'      |   _/
                     /             \\     /    ,'         |  |
                    /               `.  /    /           |  '
                   |                  `/    /            | `.
                .-.`                  /   ,'            j   |        _
                \\                   /V   /              |  ,'     ,-' |
                 .                _/    /               | /    ,-'   /
                 |               |    ,'               j / _.-'    ,'
                 |               |   /                 ' \"\"       /
              `\"--               |  /                  |        ,'  _,..-.
               \\                 | j                  .'       ---\"'     /
                \\               j  |                  /                ,'
                 \\       __...--.  |                 /_..-----.       /
                  \\   ,\"\"       |  |   _.           /        /      ,'
                   . /          |  |  /  |        ,'        /      /
                    Y           |  |.'   F    _,-'         /__,._ `.......
                 _,'               '    / _.+'   ,-\"\"-.        .'       ,'
             _.-'                      `-'| |   ,      .       -._   ,-'
         _.-'                  .\"\\        | |    ._   ,'         / .'
          `\"\"\"---...._        /D  |       | |      \"\"' .     __  `--.
                / |  ,      ,`  `-|       ` |  /`    ,'    /\"  \\     `.
               .  `_/      /  `-..|         |  .'   /      `.  |       \\
               `          '-......'         |      .         `-'        L
                \\                          ,'     j                     |
                 `                      _.'       |                    .-.
                 /    ,            _,.-'          |                    '  \\
                j._            ,-+'             __|                  ,^.   \\
               | | `+\"\"-.....,' .'           ,-'   `._           _.-'\"\"\"`\"\"
               |,|  _`. |     ,+          _,'         `\"-------\"'
               '  \"\"   \"     | ,\"\"-.   _,'
                             |,` _.+--'
                             ' \"' ''')

    elif n_pokemon + 1 == 33:
        print('''    `._
              \\ `.
               \\  `.
                .   `.
                j     :-----+...-.
                /  _,'   /\"\"_     `.     _,..._
              ,'  '      .-\"c|\"`+- -+--\"'      `-.._
            ,'            \"\"\"+_ |       _,--\"\"--.._ `---..
           '     _             \"'      '\\          `--._  `.
          |    -'                      _.'              `-. `.
          (     __   ,.----.._        \\``-.                |  `._
           `.  /_ \"\"\"   ___.| ,.      j  `.`.   ,          `.    `.
             `'| |    ,'    '.'/'\"\"'\"'   j`. \\,'|  _________||\"\"`-'`.
               `_.\\   j       j      __-'|_/'\"._:.\"  __       .    \"
                   | /        /      \\ `/        |`.   .   ..._`.
                   ||        /       | /         | |    :.'    -/
                   |'    _,-'        |.`.       ,' |   | |\\_
             _     | `--'     _,-    . `.`--- ,'   /   |  .\\`-..
             |`v,-'\"\"\"'`-.,.-'        `._``--'  _,'    |  | \\  ,'
         ,--'`- _       \\ \\              '\"\"''`'       `_,'  +-
          -.'    \\       . |                        /`     ,---.
          -`\\    |       | L                        `-'     '\"\"'`\\
          '---...:_      / \\                          |   ,.-\"\"\".|
                   '---+'   \\                         ' ,'       `
                        '`''\".                       / /          `.
                              \\                     j |            '.
                               `.                   | |              \\
                                 \\ _                |/             /\\|
                                  / \"-   --\"\"----+--'             / ||
                                 `v'\"\"\"\"\"-..     |      `..__.,.-'-.,,
                                  |         `-.,'           .`.J     /
                                  |            |             '---...'
                                  |     .     /
                                  |    | `,  j
                                 ..--+'\"--_  /
                                  `-.|     \\'
                                      `----' ''')

    elif n_pokemon + 1 == 34:
        print('''                  _.___.._              ,'            ,. ____
                            \\      '-.._      |: | '       __,- _ ... )
                            j-\"\"\"|\"`-._ `.'.  | \\| |    ,\"'_,--.     `.
                           |     |     `. `.\\-' j   .-.'  '     `.    |
              _.           `     |       \\  \"  /    \\   .'       |    |
             /  |           \\    L       j           )   \\       j   j
            /   |            \\    `.   ,'_ ..   .__,. ,   `     /   ,'
           /   j              `-._  `./  /`. \\       / /\"| \\ .-'  ,'
          .  ,.|                _`+..    |.)`       ' (| |  ``._.'
          |-'  |              ,'    /,     \"`'       '--\"   |   '`.
         j     |             '        \\ './.             |\\-'      `
         |     |            |          \\  `/, . . . _-|./ |        _\\
         | ,-\"\".            `-\"\"-.     |`-._`| \\--|'/|, ,,'    _.-' /
         |/     \\        __(      \\   ,+..._`---...-'_.--\"\". .'     \\
         |       `   ,-\"'   `._   | _.      `\"-....-'       `.    ,.---.
         |    ,-'\"  '\"'\\       L,-|'            `v           |  ,'      `
         L   /    .\"`--'       |  |              |           |||         `'
          | /     `..        ,.|  |.             |          ,' '|       .\"\".\\
          `'      | /        . `. | `.       _,--+--._    ,',-''|        `-'|
           `     .,\"`. ,..  / `  `|   `-...-'         `\"-' / ,.-\\         /\"\".
            \\   j    |`. |.-   `/. `.     __.-----...__   ,`/    `.___    \\  |
             .  |    |  \\|      | \\\\ `- -'             `.. |       |  `,\"\" `.'
              ` |   j .         | | \\                   |  |       |,-| \\
               `'   | \".      ,-' `. L                  .-' `        ,'  |
                 `. |   \\    /     .'`.               ,'     `      /    |
                   `.    `\"\"'      /   `-._       __.' .'\\    `....'    /
                    ,'             \\ _____ `\"\"\"\"\"\"  _.'  /             '
                    ' ,--'\"\"`--.___,'     \"\"------''    '_    _,...__ /`.
                     `-........'                          `-.'       `,\"
                                                              `\"\"\"---' ''')

    elif n_pokemon + 1 == 35:
        print('''                    __.._
                         ,--'     \"`-._    _,.-,--------.
             ________ ,-'              `-\"'   /     _.-'|
          ,-'  '     :                       .    ,'    '
         |    '     j      _.._              |  ,'     j
         L   /      |    .'    `.            |.'      /
          \\ j       |    `.,'   |           ,'       /    _
           .|      ,'\\         /           '.___    / _.-\" |
            `    .'   `-.....-'                 `- +-'    /
             `. ,'                                `.     <__
               `.             .\\ \\                 |   ___ ,'
               |     | #      || |                  ,\"\"   \"`.
               |     | #      `'_/                   .       `.
              ,'     `.         ,-\"\".                L         `.
             /     (__)       _  \"\"\"                  :\"\"-.      .
            /             \\\"'u|         |/            |    \\     |
           .               \\  |         |           | |     |    |
           |     _          `-'        j           /  |     '    |
           L      `.                   |          /   |   ,'     '
            \\       `.                ,'         /    |_,'      /
             `.   ,.<'                `+--.    ,'     /       ,'
               `./`._'                 '_.`._,'      j      _,
                 /\"'                      \"          |   _,'
                /   `._              .              '..-'
               j       `-._           `            /
               |        _,'`\"--........+.         /
               ,\"-.._,-'                 `.  .-._/
               '---'                       `+__,' ''')

    elif n_pokemon + 1 == 36:
        print('''                                       __,......._
             _............___          ____....<__         `\"._
            '._      `\",     `'--._,.-'   ___     `\"-.    ___..>---,---------..
          ____ -.,..--\"            `-  ,-'   `       .`-\"'       .'_         ,-'
         '._  \"\"'-.                  .'     _.._                    `-._ ,.-'
            `-._   `._              .     ,'    `.                    ,-'----.._
                _>.   -.            `     |      |                _,-'          )
         ,..--\"\"`--\"\"\"\"\"`-.          \\    `-.    |             ,.+.__   _,;---\"\"
         \\_ |              `.         `.       _.'         _,-`      `\"\"   `.
           \"\\                `       / _`\"----'           '                 /-.
            `.____                  |  #      #' \\                         `,..'
                ,-\"--...__          `--        --'                   ___,..'
               '-.---\"'  |           -.,........,            ,.---\"\"\" .
                         |            |        \\'             \\\"\"--..._`
                         |             \\       /              |
                         .              `.    /               |
                          ,               `--'                j
                         j \\                                 /
                         |  .                               '`.
                          L._`.                           .' ,|
                          |  `.:-._                    _,' ,' |
                          `.,'| \"\"\"`.__            _,< _..-   '
                              `...-'   `----------'   `-.__|`' ''')

    elif n_pokemon + 1 == 37:
        print('''               _,.+-----__,._
                       /  /    ,'     `.
              ,+._   ./...\\_  /   ,..   \\
              | `.`+'       `-' .' ,.|  |
              |  |( ,    ,.`,   |  `-',,........_       __......_
               \\ |..`/,-'  '\"\"\"' `\"\"'\"  _,.---\"-,  .-+-'      _.-\"\"`--._
                .\"|       /\"\\`.      ,-'       / .','      ,-'          \\
               .'-'      |`-'  |    `./       / / /       /   ,.-'       |
              j`v+\"      `----\"       ,'    ,'./ .'      /   |        ___|
              |                      |   _,','j  |      /    L   _.-\"'    `--.
               \\                     `.-'  j  |  L     F      \\-'             \\
                \\ .-.               ,'     |  L   .    /    ,'       __..      `
                 \\ `.|            _/_      '   \\  |   /   ,'       ,\"    `.     '
                  `.             '   `-.    `.__| |  /  ,'         |            |
                    `\"-,.               `----'   `-.' .'   _,.--\"\"\"'\" --.      ,'
                       |          ,.                `.  ,-'              `.  _'
                      /|         /                    \\'          __.._    \\'
            _...--...' +,..-----'                      \\-----._,-'     \\    |
          ,'    |     /        \\                        \\      |       j    |
         /| /   |    j  ,      |                         ,._   `.    -'    /
         \\\\'   _`.__ | |      _L      |-----\\            `. \\    `._    _,'
          \"\"`\"'     \"`\"---'\"\"`._`-._,-'      `.              `.     `--'
                                \"`--.......____:.         _  / \\
                                        `-----.. `>-.....`,-'   \\
                                               `|\"    `.  ` . \\ |
                                                 `._`..'    `-\"'
                                                    \"' ''')

    elif n_pokemon + 1 == 38:
        print('''        ,-\"\"'-.._
            .---'\"\" \">` - `--
            `.      `-._  .`-.
              `-.       \\ .` : -.
               _.>._     / ` `:..,
          ,.../...._`\"-./    '.|, `
         `---.._\"'-.`-._    |    \"'--.
                `--.\\`. `._,'         `.---------------.._
                     \"-'--.___          \\`'\"-..__         `-._
                              `.\"`-\\     ` `\"--..\"`-.-..__    `\".
                                `.  `.     |``._ `--. `-..`\"-._`.\\-.
                                  \\   -....' `-.`-.  `-._ `-.  `-.\\ `.
                                   `-.__  `.`-. `. `._   `._ `-.  `.  `.
                                        `-..`` `. `.  `.    `.  `-.     \\
                                            \\`.` `  `.  `.    `.   `-.   `.
                                             `.`-'`.  \\   .     `.    `.   \\
                                               `..  \\  \\   \\      `.    `.,_`.
                                                  \\` \\  .   `.     '\\     `.`.`._
                                                   \\``.  \\    \\     \\`.    |
                                                    ' '.  \\    \\     \\ \\   L
                                                      \\ \\  '    `    '. `.  \\
                                                       ` `. \\    `    '.  `. `.
                                                        `. `,`.   `.   `.   `._.
                                                          `-  \\._   `.  `.     \"`
                                                               ` `.   `.  .
                                                                   `-. ``-.:-.
                                                                       -.`. '\"-'
                                                                          `\"-. ''')

    elif n_pokemon + 1 == 39:
        print('''   ,..__
           |  _  `--._                                  _.--\"\"\"`.
           |   |._    `-.        __________         _.-'    ,|' |
           |   |  `.     `-..--\"\"_.        `\"\"-..,-'      ,' |  |
           L   |    `.        ,-'                      _,'   |  |
            .  |     ,'     ,'            .           '.     |  |
            |  |   ,'      /               \\            `.   |  |
            |  . ,'      ,'                |              \\ /  j
            `   \"       ,                  '               `   /
             `,         |                ,'                  '+
             /          |             _,'                     `
            /     .-\"\"\"'L          ,-' \\  ,-'\"\"\"\"`-.           `
           j    ,' ,.+--.\\        '    ',' ,.,-\"--._`.          \\
           |   / .'  L    `.        _.'/ .'  |      \\ \\          .
          j   | | `--'     |`+-----'  . j`._,'       L |         |
          |   L .          | |        | |            | |         |
          |   `\\ \\        / j         | |            | |         |
          |     \\ `-.._,.- /           . `         .'  '         |
          l      `-..__,.-'             `.`-.....-' _.'          '
          '                               `-.....--'            j
           .                  -.....                            |
            L                  `---'                            '
             \\                                                 /
              ` \\                                        ,   ,'
               `.`.    |                        /      ,'   .
                 . `._,                        |     ,'   .'
                  `.                           `._.-'  ,-'
             _,-\"\"\"\"`-,                             _,'\"-.._
           ,'          `-.._                     ,-'        `.
          /             _,' `\"-..___     _,..--\"`.            `.
         |         _,.-'            `\"\"\"'         `-._          \\
         `-....---'                                   `-.._      |
                                                           `--...' ''')

    elif n_pokemon + 1 == 40:
        print(''',-.                                                 .
         .` `.                                             .'|
         ` `. `-._                     _,.--._            /  |
          `  ..   `.                  /       `.        ,' , '
           `  ` `.  `-._              | '\".     \\      /  / .
            `. `   `.   `.          ,\"'---'      .   ,' ,'' |
              ` `.    `.  `.       .             |  /  / /  F
               `. .     `.  \\ ,..--|             |,'  / /  /
                 \\ `.     .  |      \\           ,.   / /  /
                  `._`._   j   .----.`._     _,` | ,\" / ,'
                     `._`\"`  ,',\"\"\"\"-.`.\"\"--' ,-\":+.-'.'
                     ,'     . |`._)   . L     ||_7\\+-'
                    /       | |       | |     .\\   \\.
                   /        |  .      | |      \\\\_,'j
                  .          ._ `----' /        `--\" '
                 j             \"--..--'              |
                ,|                        ,-\".       |
              ,' |                       /   |       '
             /   '                       `..'    ,'   \\
            /   j                               /      L
           j    |                              .       |
           |  _.'                              |     , |
           `-' .                               |   ,'  '
               |                               `.-'     .
               |                                        |
               |                                        j
               '                                       .
                `                                     /
                 `.                                  /
              ______.                              ,'
            ,'       `-._                     _,.'\"\"`--..
           .         ___,+ -...._________,...<_          \\
            .___,.-\"'                          `-._      |
                                                   `-....' ''')

    elif n_pokemon + 1 == 41:
        print('''                                        `\"--.._
                                                  '  ,__`-._
                                                   ` |   `-.`._
                                                    |`       `._`.
                                             ./\"\\   | `.        `.`.
                                           .'/   .  | _ `.        `.`.
              /|                          / /    |  || `-.`.         `..
             / |                         . /     |  ||    `.`.         `.`
            /  '        _.,.____      _,.'._     '  j       `.`          `..
           j ,-.`       . \"\"--._`-. ,',.-++.`. ,'  //         `..          `..
           / '  \\`       \\      `. '.'|  ''  \\`   //            ``.          `.
          j /    \\`.      \\       || `'       |\\ //              `..    __,....`.
          |.      `.`.     `.     ||         [|'//                 \\\\_,\"        `
          ||       |,.`._    `----.`_\"\\   _.-\"  .        ___........\\|
         jj        || `-.`-.______ `/`--'\"       \\   _.-'
         |.        ||     `--..___\"\"              .,'
         ||        ||             \"\"|             Y
         ||        ||               \\            /
         ||        ||           _....\\.         ,\\
         ||        '|        ,-'       `,.___,.-. .
         ||         L      ,'           `  /     ` .
         ||         '`    /              ||       ` .
         ||          \\| ,'               ||        `.`
         ||        ___|/                 '|          .`.
         ||    _,-'    |                  L           ` .
         ||  ,'                           ||           ` .
         ` ./                             ||            ` .
          `V                              ||             ` .
                                          ||              ``
                                          ||               ``
                                          ||                `\\
                                          ||                 `'
                                          ||
                                          ||
                                          !|
                                          _/ ''')

    elif n_pokemon + 1 == 42:
        print('''                           ---..__
         _____                          `._\"`._
           `._`\"--_._                      `.  `._._
              `._   `-._._                   `.   `.`._
                 `.     `-._.                  `.    `.`._
                   `.       `-`._                `.    `-.`.
                     `.        `-`._               \\      `.`.
                       \\          `.`.              \\       `-.`.
                        \\            `..             \\         `.`.
                         \\             `..            \\          `.`
                          \\             _:`.           |           `..
                           L       _,-\"\" jj            |     ___......:
                           |     ,'      ||            |  ,.\"        .'
                           |   ,'        ||            |\"'           / \\
                           |  /         /|L       ,\".   ]`.         /   L
                           |,'         . ` \\      /  \"\"\"  \"`.      j    |
                           /_          |  `.\\    (\\  <.)|    \\     |    |
                             `-.       |    \\`.  |_____..     \\   j     |
                                `,     |     `.`.\\|    V \\   .'\\  |     |
                                  \\    |       `._|       | <  ` j     j
                                   `.  |          `.      |  \\  |      |
                                     \\ |           |L      L  L |__    |
                                      \\|           ||      |  |  __`. j
                                       Y           ||.-.   |  | |   \\ |
                                        \\,--\"\"\"\"\"`-.|`. \\  |  |/|    `
                                         '          |  \\ `.'    j
                                                   (|  | ,.`.  /
                                               _.-\"_`._| | `' /
                                       ,....../ ,'\" `.__.'_,-'
                                       `-----._`..      \"\"
                                               `.J ''')

    elif n_pokemon + 1 == 43:
        print('''                           .-\"--.__
                   _                / '+.--'
                    \\.-._          j / |
                     \\`-.`._      . j  |
                      \\  `. `.    | |  L                        _,,--+='
                       L   `. `-. | |   \\                  _.-+'    /
                       |     \\   j  |    \\            _,-'\" .'    ,'
                       .      \\  |  |     \\         ,'   _,'    ,'
                        \\      `j   |      \\      .'   ,'      /
                         `.     |   |       \\   ,'   ,'       /
                           \\    |   |        \\ /    /        /
           _,-''\"\"\"\"'\"\"'\"\"`--. j    |         V    /      _,+............._
         -=`...-----...__     `|    |         .   /   _.-'        _,.--\"\",..=.
               `-.       `._   |    |          L,'  ,'       _,.-'    ,-'
                  `.        `. |    |          |  .'     _.-'       ,'
                     .        \\|    '          L/    _,-'          /
                      `._      `.    L        /   _,'            ,'
                         `-._    \\   `       ,' ,'             ,'
                             `-.. `   \\     /,-'           _.-'
                               ,'\"-..  .   /_,..---\"`+'\"\"\"\"
                              /           '           `.
                             j                          .
                            .                           |
                            |   .-.       ,.            |
                            |    -'       `.'           |
                            `                           '
                             `.      .--.             ,'
                               `.    `._|          ,-'
                             _.-`   ,..______.. .  `-.
                           ,'       |          |      `.
                         ,'         '          |        `.
                        /         ,'            .         .
                        \\     _,-'               `._      |
                         `---'                      `-....' ''')

    elif n_pokemon + 1 == 44:
        print('''                            ,.--\"\"+`-,
                             ___,..-'  C'  `.' `-.
                          .\"|      `-,...._   ___:.
                         /'\"|   _,..^..__ _'\"'     `-.
                        ' `\" ,-`c.   ..  `.     ,\"\".  `.
                       /,  ,'       `._'   `.|)  \"'    /\\           .
                   _,.|'- /  .-.             \\         `\".          |\\
               _.-'   |  |   '-        _     |           |          | \\
             ,'       |  |            \\.'    |           |          |  .
            ,          . |                   |           j          j  |
           /_.-'\"\"\"'\"':.+|                   |          /         ,'   |
          /'       ,-'    \\                 /        _,'-..___,..'     j
         j|       /        `.             ,^.......-+                 /
         ||      /     _,-.\"\"'-..____,..-'-._        \\               /
         | \\   ,|    ,' .'   ,'    .         `.       \\__         ,-'
          . `-'.|   /  /  _.'       `.         \\       . `---+.-'|
           `._, ' j   j '\"            `--..     `.     |.     `. |
                 .|   |                           .    ||       `|
                 `'   |,----......__...._         '    ||        |
                      |`._=-=====___''-. `-.      |   / |        '
                   _,.L   `\"\"\"------|  .---'      |  /`-+_
              ,'\"`/    \\            |  |          |.'.    `\"\"'-.
              |   \\__,.'`           | j              _+-._     |
              |    `     `._        | |             ,     `---\"
               .    `...,-' +._      `|            /
                `.       -'\"   `-...________,..--.  `.,..
                  \\     |                         `.     |
                   `._  |                          '    /
                      `'                      _,.-'    /
                                           ,-'        /
                                          `.       _,'
                                            `'----' ''')

    elif n_pokemon + 1 == 45:
        print('''                        _..--------..__
                             ,-\"'    __         `-.
                          ,-'    .-\"'  |   .--.    `. ____
                        ,'  _..   `\"\"\"'    `-'  _.-'\"'    `\"--._
                      .'   `..'  _           _,' ,\"\"`,        __`._
               _.--\"\"\"`\"---.._  '.\"   ___..,'__   `\"'        `. `. `.
             .'__       .-,   `'-+.--\"-------..`-.   `=`       `\"'   \\
           ,'(__,'   _   \"       |( ,-'\"\"'\"\"'`-.`,|  _.----\"\"'\"`--.../
          /         |_)          | `-...______,.' |-'        `-'      `-.
         j                      .'_,..........__,'     c.          .-.   `.
         |        _,..  `+' _,.-'\"        .,    `-._               \\__'    `
         |       `___,'   ,'   .:\"',     '\"    .-,  `-.     ,--.      _     |
          \\             ,'       \"\"             `      `.   `--'    ,' |    |
           `.         ,'  .'\"\"`.          :\",       __   \\          `..'    '
             `._     .    `---'            \"       |  `.  \\               ,'
                `\"--+                   __          `\"'    .           _,'
                    |                 ('  )                |...,,...-'\"
                     `.                 \"'                ,'
                       `-..__                          _,'
                             `+---.=,---------+.----+\"'
                         ,'\"`/     \"          \"   ,-.\\
                         \\    \\         _        /  | +.
                        .`.            '/       /   | | \\
                      ,'   A   '               /    j |  `.
                     '    / \\   \\             j    / /`.   \\
                      `--'   \\   \\            |   j,'   `.,'
                               . |-.........,.|   .
                                `'            `,.' ''')

    elif n_pokemon + 1 == 46:
        print('''           ____                               ____
               ,-\"|\"    \"\",._                    _,--\"' |  ``-.
              /   \\.   _,'   `-.               ,'  \\   ,'    ,-\".
             /      `\"'        |              /     \\.'      |   L
            /_     .-..    ,'\"\"|             |   _,.    ,--. `.__|
           j  \\   /    |  /    |     _____   `  j   \\  |    \\     L
           |  |   `    L  \\   / _.\"\"|    .\"'--._|    |  `.__/     |
           |  '    `-./    `.+-'    `..-'       |-.  |        ,\"`.|
           `-'            ,'  )   __,...__       ` `-._      /   ||
            `,---.      ,'  .'_,-'        ``-._   `-.__|-.../_...'
             `-..,\\.--'/..-`.'  ..-------..._ ,-.\"'`-.    `.
                     ,\"`.__  `.'    `'  `-' .(   ).   \\     . ,--._
                  ,\"|`._)  `. |  _      ,.  |`-,'  `. |     |'     `.
                 / _|  .    | | `-'     -'  |  .   ,' |,-\"\"-`.,--.   `.
                /\"\" `.  `\"-'  '    ___       `. `\"'  .'       .   I-.  `.
              ,'      `-..,.-' ,-'\"   `-.      `\"--'\"/         \\   \\ `.  `
             /         |      /         |\"-.        /           `.  `. `. \\
            /          |.    | `. ___ ,.'  |       j            \\ `   `. \\ .
           j           | `. (`._ \\  .\"   _,{      ,'             L `.   . \\|
           |           |,' `-.  `\\   \",-'  |_,..-'|              |   L  |  '
           |           |      `-..'  '__,.-'      |              |    . |
          /|            L        `\"\"\"'           j               |    | |
         j |            |                        |              j     | |
         | |             L                       |              .     ' j
         | [             |                       |             /       '
          - `.           |                       |            /
             `.   ,'\"\"`-,                        |.--..__    /
               `.'      \\                        '       `.,'
                 `.      \\                     ,'      _,-'
                   `.     `.                 ,'    _,-'
                     `-..__ \\              <___..-\" ''')

    elif n_pokemon + 1 == 47:
        print('''                                       _______
                                            _,\"\"|      `-._
                                          ,\"  _.'          `.
                                         ,'\"\"'               `.
                                       ,'       ,.----._  .--. \\
                                      /        `____    \\  \\_ ) \\
                                    ,'              \"\"`-'    \"   L
                                  ,'                             |
                                ,'.'                              L
                              ,'-'    _,...._             .\"\"`.   |
                           _,'     ,-'       `.       ,.   `.  `. '
                       _.-'      .'     ______/       `_)    `._;  \\
                    ,-'           `-\"'\"\"                            \\
                  ,'   ,.---,                                        \\
                 /   .'   _,                    ,\"\"\"`-._         .\"`-.'
                 7-\"'-+--'     ___               `-.__  `.       `.   `
               ,'      \\_____.'   `.--.'\"\"`.          `-.'         `-..\\
              /         `.`._|     | |      |`--...,.---.               `.
            ,'      . `  |    \\    ,-|     ,'..,-'       `.,_             \\
           /     \"       |.,.._\"'\"'   `-..'  .'            \\ `\"-.._      __\\
          /              | '-..\"\"..________./              |..-\"\". `+.  (  ,
         j               | L\"`--._....___  /               |_...  `/  \\  -.'
         |             | | |      `--._  \"/                j__..`  `.  `.-'
         |          /  j ' |           \"./       ,.'    \" /_..-\"'\\   \\.  `.
         |         /' / /| |            /         ' \"    /'       \\   \\`.  `.
          L       / |V j | |           /               ,'          \\   \\ \\   `.
          |      j  |  | |  L         j              ,'            /    | \\   |
           L     |  |  | `.  \\        |            ,'             j    /   \\  |
           .    j   `. L   `._`.     j          _,'               '   '     . |
            \\   |     `.\\     `\"`    |       _.'                 /   /      | |
             \\  |       `           /   _,.-'                   /   /       j .
              \\ |                  /.-\"'                    _,-'  ,'       /,'
               '                                           '----\"' ''')

    elif n_pokemon + 1 == 48:
        print('''                                           _.----.
                                                __,'   _,-'
                                           _..\"_..---\"'
                                        _.'_,-'_____________,......
                             `. .   ._,_.-',--',.-...........    __;
                          __  `/ ),`','_.'..,--'_,.---;      `\"\"\"
                       `.,..`\"'  ,.'.-_.-',..-'\"   ,-'
                     _,..        ___-'           ,'
                  ,-'    |     ,'   `-.         '----..
                ,'       |   ,'        \\             \\.
               /         '  /           L            `-
              |        ,'  j            |        ,     `.
              |    _,+----.|            |       . `.    .-.
              |   /\\    ,..\\L           '       |   .   |`---
              |`-| ,\\___|  | \\.        /        |   |  .--            .,|
              |   V     / ,   '-.....'\"         |   |   `.           ,.-'`'
              |\\       `-'                      `._,     _\\
              '|                                         ` _   .-.--\".-
           _,.. |                                       ,./`.,/   ,.-'
         .' .   |,                            ,---,     \"._      /
         |  `     `.                         /   `.     ,--     /.----...,
          \\         \\                        \\   .\"    '.._             |
           `.        L                        `...'  `..--. -\"\"_..    _.'
             `.      '.,`.                          ..'-.`,_      `-\"'
               \\       \\` ',-                     .'     \\
                `.      L  `.  .             ,.-'\"\\       \\
                  \\     |    '`.`. .-. .-..,..'.   \\       \\
                   `-._,'         `\". `-..          \\       `.
                                                     `. -.   |
                                                       '-.+--' ''')

    elif n_pokemon + 1 == 49:
        print('''                      ,-\"\"-.                _ _,....._
                             ,'     |            _,-\"_..----\"\"-\"\\
                       .   ,      ,'|         _,\"_.-'            |
                     ,'/  /|    ,'  |      ,-'_,'                |
                    / /  /j    /    |   ,-'_,'            __,..--'
                   / /  / '   /    j  ,' ,'          _.--'      /
                  / /  / /   /     |,' .'         ,-'          /
                 / /  j /   /     /' .'        ,-'            /
                / /   |j   /  __.' ,'       _,'             ,'
               / /  ,\",|  /,-\".' ,'       ,:_______________/
              / , ,','j  /\", /,\"/|      ,'                /
             /  |' /  |_/ / / .' |    ,'                 /
            /   |,'  ,' .' / /  j   ,'                _,`
           j   '/ ,-' .'  / /   | ,'              _.-\" |
          .'   j.'  ,'|  / /    ,'          _,.--'     j
          | _.-_,../| | / /    |      _,,-'\"        _./
          j  ,( )__ `.// /   ,'|  _.-'          _.-'  |
         .   | `(  ) |/ /   /  ,`+        _,..-'      '
         |   |   \"'  | /  ,'_,'   `.  _,-'           .
         |   .`.___,'--. /,'       ,+\"               |
         |  | `/         \\     ,-'\"\"'\"\"-.._         .'
          .,j /           \\ ,-'         \\  `-.      /
           `|'      /`.    Y-\"'\"\"\"---.._|     `.   /
            |     ,' / 7   |            |`-.    \\ /
            |___,'  / /`.  |_           |   `.  ,'
            `.___..' / /  /  .,.__      |     `.
              `.____/,' _'   /`.  '`-.._|      Y
                `-+----'   ,'   7-..   j -.     .
                  |  __.,-'    -|   `-.+   `-.  |
                  |\"'      ,.'` ',   /  `._   `.|
                  |_  _,,.'      |`..      `.   |
                   .'\"          ,'  \\.       `. \"-.
                   `        ,./\"|\\   \\|        `.  |
                    `v.^.,`.    | \\   )     ,    `.|
                      `._     .'   `./_\\.--' .     `.
                         `---'               '      /
                                              `. _,'
                                                \" ''')

    elif n_pokemon + 1 == 50:
        print('''                     _,.---'\"\"'\"--.._
                            ,\"                `-.
                          ,'                     `.
                         /     _       ,.          `.
                        /     ||      |\"|            \\
                       /      ||      | |             \\
                      /       .'      `_'              L
                     j                                 |
                     |        __,...._                 |
                     |      .\"        `.               |
                     |      '           )              |
                     |       `-...__,.-'               |
                     |                                 |
                     |                                 |
                  ...|                                 |
               _,'   |                                 |
           _,-'  ___ |                                 |.-----_
         -' ,.--`.  \\|                                 |     . \\
         ,-'     ,  |--,                               |  _,'   `- -----._
               ,' ,'    - ----.            _,..       _|.',               \\
          ,-\"\"' .-             \\  ____   `'  _-'`  ,-'     `.              `-
          .--'\"`   ,--:`.       --    ,\"'. ,'  ,'`,_
                 _'__,' |  _,..'_    ,:______,-     --.         _.
                 -__..--' '      ` ..`L________,___ _,     _,.-'
                                                       '\" ' ''')

    elif n_pokemon + 1 == 51:
        print('''                                        _..-----._
                                              ,-'__      __`-.
                                            ,'  '  `    /  |  \\
                            _____          /   ,...            \\
                       _.-\"\"     `-.      |   /    `. ,-\"\"`.    \\
                      /             `.    |  |   `  || .    |    .
                     j             _. \\   |  `..__.' '      |    |
                    .     __     ,'--. \\ j       ,....`....-'    |
                    |     .---. .     | \\|      (__    )         |
                    |   .'   . || '   |  Y         \"\"\"'          |
                    |   |      | `-..-'  |                       |
                    |    `-...',.--.     |      ,--,.--\"\"'\"-.._ j
                    |        .\"    _|    |      .-\" |    ,\"\"\"`.`|
                    |        `---\"'      `.    /    '   /     |  `
                    |                     L   /,-\"\"-.   _,...     \\
                _._  L                    |  j|    _ | /     `.    L
              ,'   `-|                     L ||      | |  '   |    |
          ,--\"     _||                     |j  `----'  `      |    |
         \"       ,',:|                     .     ,-\"\"--.`-- -'     | _
              ,-._'  '.                    |     `-...__)         j'\" `-.
             :,.._:.   `.               ,-'|                      |_,.._ ---.
                        _:......--.,..-'   |                      |     `.  ,`.
                   `\"\"\"' ..../__,  \"----.\"'-\\  _,-'\"`._           | .   __
                                         '-..- .....- .`-...,-\"\"`-,|___.
                                                         '\"-----\"'. ''')

    elif n_pokemon + 1 == 52:
        print('''                                        .
                                  |              |
                                  |             ,|
                         ,_       |\\            F'   ,.-\"\"`.
                        /  `-._   |`           // ,-\"_,..  |
                       |   ___ `. | \\ ,\"\"\"`-. /.-' ,'    ' |_....._
                       |  /   `-.`.  L......|j j_.'      ` |       `._
                       | |      _,'| |______|' | '-._     ||  ,.-.    `.
                        L|    ,'   | |      | j      `-.  || '    `.    \\
         ___            | \\_,'     | |`\"----| |         `.||       |\\    \\
          \"\"=+...__     `,'   ,.-.   |....._|   _....     Y \\      j_),..+=--
              `\"-._\"._  .   ,' |  `   \\    /  ,' |   \\     \\ j,..-\"_..+-\"  L
                   `-._-+. j   !   \\   `--'  .   !    \\  ,.-\" _..<._  |    |
                       |-. |   |    L        |   !     |  .-/'      `.|-.,-|
                       |__ '   '    |        '   |    /    /|   `, -. |   j
                 _..--'\"__  `-.___,'          `.___,.'  __/_|_  /   / '   |
            _.-_..---\"\"_.-\\                            .,...__\"\"--./L/_   |
          -'\"\"'     ,\"\"  ,-`-.    .___.,...___,    _,.+\"      \"\"\"\"`-+-==++-
                   / /  `.   )\"-.._`v \\|    V/  /-'    \\._,._.'\"-. /    /
                   ` `.  )---.     `\"\"\\\\__  / .'        /    \\    Y\"._.'
                    `\"'`\"     `-.     /|._\"\"_/         |  ,..   _ |  |
                                 `\"\"\"' |  \"'           `. `-'  (_|,-.'
                                        \\               |`       .`-
                                         `.           . j`._    /
                                          |`.._     _.'|    `\"\"/
                                          |    /\"\"'\"   |  .\". j
                                         .`.__j         \\ `.' |
                                         j    |          `._.'
                                        /     |
                                       /,  ,  \\
                                       \\|  |   L
                                        `..|_..' ''')

    elif n_pokemon + 1 == 53:
        print('''
                  ,-\"\"--.
                 /       \\
                 | ,\"`.   L
                 |     |  |
                 \\_   /   |
                   `-' |  |
                       |  |
                       |  |
                       j  j
                      .  .
                      j  j
                     .  .
                     |  |
                     |  |
                     |  |
                     L  |
                      \\_|._
                _.-,-\"     `\".
              ,' .'           \\
             /  /              \\
          _,'  /  /             \\
         <    /  /              |\\
         <+-'|  j               |/
          `--+  |    ___        `    ..-.
              \\ |  ,\"--.`.       \\__/,\"\".|
               `-\\||    `.\\--\"\"\"\"' //    |
                  |`    / `          \\  ,'
                   \\|. / ,.  ,-.  _.. \\'___..
               _____| Y |  `.`./ /  | ;.=\"
                  \"-+=+.|  ! \\  /_! / |_____
                   _|_L, `\"\"\" ._. \"\"  .---------
                _+==+-`\\. .__,.|...,-=+\\._
              ,\"\"   | .+-+ \\     )/.'   \\\"-+
                    ,+'  |` \\    // \\    \\
                   '|    | `.\\..'/   \\    \\
                    |    |   `\"\"'     \\    L
                    |    |             \\   |,._
                    |    `             _j .'  '>
                    |  ,..\\           /        /-.
                   ,^.' _  |          `.  .--.'  j
                 ,'  | |/  |-\"`.       |'-'\"\"``-|/
                 |_   .,---.  |\\
                 |/_,`-...-^..`' ''')

    elif n_pokemon + 1 == 54:
        print('''                              ,-'   ,\"\",
                                      / / ,-'.-'
                            _,..-----+-\".\".-'_,..
                    ,...,.\"'             `--.---'
                  /,..,'                     `.
                ,'  .'                         `.
               j   /                             `.
               |  /,----._           ,.----.       .
              ,  j    _   \\        .'  .,   `.     |
            ,'   |        |  ____  |         | .\"--+,^.
           /     |`-....-',-'    `._`--....-' _/      |
          /      |     _,'          `--..__  `        '
         j       | ,-\"'    `    .'         `. `        `.
         |        .\\                        /  |         \\
         |         `\\                     ,'   |          \\
         |          |                    |   ,-|           `.
         .         ,'                    |-\"'  |             \\
          \\       /                      `.    |              .
           ` /  ,'                        |    `              |
            /  /                          |     \\             |
           /  |                           |      \\           /
          /   |                           |       `.       _,
         .     .                         .'         `.__,.',.----,
         |      `.                     ,'             .-\"\"      /
         |        `._               _.'               |        /
         |           `---.......,--\"                  |      ,'
         '                                            '    ,'
          \\                                          /   ,'
           \\                                        /  ,'
            \\                                      / ,'
             `.                                   ,+'
               >.                               ,'
           _.-'  `-.._                      _,-'-._
         ,__          `\",-............,.---\"       `.
            \\..---. _,-'            ,'               `.
                   \"                '..,--.___,-\"\"\"---' ''')

    elif n_pokemon + 1 == 55:
        print('''                ,|
                       ,' |         .',
                      /   |    /\\_,' j
                     /    |  ,' |    |
                   ,'     |,'   |   .
                  /       '    j   j    _,.-/
                 /      ,'     |   |..-\"  ,'
                /              |         /                      `
               /               |       ,'
             ('  (                 ,\"\"`-.                        /|
              | | .              ,'      \\                      / |
              | |p'             /        |                     /  |
              |.`              '       ,'|-.                 ,'   '
              /`\"`\"\"\"'\"`-.    /       .  |. `.___           /    /
             /      ,-\"'_|._,'        |  | `.    `\"--..    /    j
           ,'     ,',-\"',-'           |,'    `-.       | ,'     |
          /     .'.'   /  ,-'|       \\'         `.    ,'/      j
         |    .','    /  /   |   ,-.  \\           `+-','       '
         |  .''      .._/   /   /   \\  \\           `.'        /
          \\/         | /`\"-.'  /_,..\"\\,\\                     /
                     '/    |\"|(       \\ .                  ,'
                            .| \\       `'                 /
                             ' _\\       ,.----\"\"-\\      ,'
                          ,-'\"\"  \\    ,'          `   ,'
                         |        `-.'              ,'
                         .           \\           _.'
                          \\        ___\\         `.
                           `.    \"\" `. \\          \\
                     ,-/\"\"\"\"'._       \\_`.         `.
         `         _.`-'\"\"            /_`.\\          \\
                  /.-n+==`       _,,-'\"    \\          \\
                    ,\\ __.-\"\"\"\"'\"           )          `..__
                   (,.'                   _/         .._   _\\_
                   '                    ,\"  _,.-._   -. `_/__ \\
                                       / ),+....._\\ ,--.\"    `'
                                      `\"'          `.._ \\
                                                       `' ''')

    elif n_pokemon + 1 == 56:
        print('''                                ,.-\"\".
                                        ,| .   `.
            ,-\"\"\"\"'\"`.                 '/ |   /  \\
           ,'     _.  \\           ,.  (/ ,'  `    .               ,-\"\"--.
         .'j ,  ,\"\"`.  \\         /  \\  -.\\   |\\   L             ,'  ,..  `.
         |( |   |    \\  \\|`-.  ,//\"  \\   `\"--' \\   \\           j   /---.   .
         `-\\|_..'     \\  ||. `/`/  \\  \\---,    `.   \\          |  '.    |  |
                       \\ || \\    `-.|  ` '`\"-,  |    .         '   |    |__|
                        `||/        `       `.. |    |          `--'    |  |
                        ,'                 __.-\"     |                  |  |
                       /                ,'\"       ,-\"'                  '  |
                      /   ,'           '        ,'L                    /   '
                     /. .'.                   .'   |                  /   /
                    |/ /|||               __,'     L                 /   /
                   .-.'|L|'__            --         \\               '   /
                  | . \\                             `.           _,'   /
                  ` ' ,                              .`       _,'    ,'
                   `-+                              /--------'    _,'
                     \\             .               {         _,.-\"
                    ,\"\\            \\       .     ,-\"-----\"\"\"'
                _,.'   `.           )      |  __,.
               /        __.        /       |-'
               .   ..--+.  `/`v  ./     ,-\"\"\"-.
                `-\"`.    \\     `/ \\           '
                     `-.  \\        `\"\"\"\"--.._  `.
                        )  \\___              `._ `.
                      _/       `-.               _ `._
              .'\"\"\"--' ,  ,-\"\"`..'           ,\"\"``    `.
              \\ _.,--.' ,'                   ( ,-.    __'\"\"\"`.
               \" '.___./                      '  |  '\"  `-.   '.
                                                 |   -.    `-._/
                                                 |   /
                                                 '--.' 
         ''')

    elif n_pokemon + 1 == 57:
        print('''                                       _.-\"\"'-.
              _______                        ,-'        `.
            ,\" .  ,  `.                  ,. .             \\
           / ,.-\"\"     \\      ,v\\       / '\\|              `'.
          /  |     _    |__  j   \\  /| / .  |               |.\\
         j   `._,.+.. ,-'  \\ |.\\ ,`,`'/ /|   \\         ,\"\"- '/ |
         '        |  / _.,_/ || \\,'  / / `    \\_    _.:-...+'  |
          `-._    `-| /.\"  \\ |''      `. _\\   '.`---..|`-\"'  _/
              `---' `.L\\    /'   | \\_.  ' `           '--.--'  \\
                        \\ ,-    .'  ,                    |      \\
                         V ,-   -. l            __       |       .
                       ,','    , '              ..+.....'        |
                      /.'    .|                 `,              /
                     | '   .' |                 .'           _.'
                     | . ,'!  |                 `--....,...-'--.. _
                    _|_`-..--\"                   -'             <__
                   /,  `.                                       ,.'
                   \\'   |                                    _,'
                    ._ ,'                                   <
                      \\                                    ,-`
                       \\                                  <\"`
                       .\\                                  \\
                    _,'  \\                     _     ___ ,--\"
                  .'      \\              ,.'--`|:._.._`. `
                  |       _\\'.,_        '| `\"- | `--. `\"`
                   \\         ) `...|`-`,-|      `.._
                    `\"-.     \\-.   `.    '          `,
                        j__._,-'|         `---.       \\ _
                       |-.-'   _'              ` _      )|.
                       `.__..-' `-.               +.__.,'  |
                        ,'         /              \\..-'   ,`.
                ,-\"----'      ,.--'                \\___,-'   `.
                /  .-\"'    ,-'                        `.       `.._
                `-..L____,'                            j __        |
                                                      |    `.      |
                                                       `___,'--....' ''')

    elif n_pokemon + 1 == 58:
        print('''


                            _,
                          .',_..,
                        ,'     /,--
                      .'       ,./.__
                      |_,.----/,,'`.  _
                     .'__     //    `...>
                ____//|) |    `      /.'
               (/    `-.-'.._     _,|                 ,.-------.._
               .             `.  '   \\               /            `-._
               `..---._       |       `.            j                 `.
                 >-,-\"`\"\"'    |        |`\"+-..__    |              -. `-.
                ( /|         /____     |  |  |  \\\"\"|+-.._     ___    `.  `.
                 \" `-..._     \"--,_    |  |  `   | |   | `.-.\"   \"-._  |  -`
                      ,'        '_>_   j ,'  '. ,` |,  |   `. `.-v.' `-+..._`.
                     '.         >       '     | |  ' \\ L     ..`.  '        `._
                      '.       /              '|`     \\|      '^,         ..,{ `.
                     / /      /                '       v          |__    ___,'\"\"
                   ,'  >---+-+.        |   __,..--\"`-._          /.-'`\"----'
                  /`.       `. '.      |-\"'            `\"--....-'._
                .'___'        `._`,    j             ___,-','      `-..._
           _ _.'    '/.-          '  ,'       __..<\"\"__,.-'              `.
          `.)         |'---\"\"`.+-.--'-------\"\"-...__  ,-'/ .\"\\          _  |
         ,\"\\ ,--.  _,-          ` `'                `'\"\"\"'`\"'\"\"\"`--._  . `/
          `-`.___.'                                                  `\"-\"'



         ''')

    elif n_pokemon + 1 == 59:
        print('''            /  ,'(
                    /`-'   \\__.,
                  ,'     .-\"\\ `---/                     /
               |`'      /,'||    '.               ,`. ,(,_. _,
           __  |  ,--+--.  ||     `'/  .     _.-\"'   `    \"\"`.
         .\" ,'-'.\"d__|  `.'_'    _,-    ,.  /        ._      `\\_
         |,'     `-..-----\"._     `.     ` |           `.     \\.
          `\"V\"--._           `.   `._    ' |             \\     \\,
           \\      `----      '. _,-'    ,' |              \\     .
            `._             .--`       `.  |               .    |
               `-.          `,.       ,--  |               L    '
                 /   [-,=.---' `.__`,`     `.              |     \\
             _.-'    `.._'--.._   - `--+\"\"\"\" '._           |      `._,
             \\        _  ---..__`--._'-.`,  ,' ,`._       j         -,'
            .'        ,-..     ,'    `. `  . ,'  / `._   /`._    ___,-'_
            l        .|_  `,  -' . .-\"      v   /   _.`.'`   7\",',-,.-\" --,
             \\      `.  .,  -..',')'\"\",   .    /  .'    |  ,'.',/| ,.     >
              V-.    '    -._,-\"    _,  .,'   j ,^    ,'/`--' `    -..,   `...
              '  \\/\\|.     :/       './`'|    |/    ,' /            `___    ,'
                    | `. ,'`-.        /  |    ' _.-'  |               ,'  .\"
                    L._`.'   |       Y,.'|    ,-    ,-'          __.,'  .'
                     \\ \\  /`.|     _,.',''.  .`-,../         ,.-/,...-`'
                      \\ ,|| |/_.-\\\" .+'    \\._  _,'       _.'\"  |
                       '  ' L| | `,' |      `.\"\"          ,.    |
                       )    `|\"      |        `>.. _,..--\" j    |
                    ,-'      |____,..'       ,',-\"'       /   _,'
                   /\"'    _,.'               |(      _..-' `\"\"
                   `----\"'                    `'\"\"'\"\" 

         ''')

    elif n_pokemon + 1 == 60:
        print('''  _..__                                    ___
          /     `._                          ,--\"\"\"\"   `\"-.
         |         `.                    _.'\"\"/`.        |/`-.
         |           `.                ,+ `..' | |       |'...+.
         |     \\       \\              / /\\____,' '    __ `.`._,\".
         |      ..      \\           ,'  \\      .' ,-\"'  `. `.._,'`.
         |       .`.     \\         /     `-..-'  .  _.... |._      \\
         '        ' `     \\       /          ,-\"\"`.____...'  `.     \\
          `        `.`.    \\     '         ,'   _,--------.`.  `.    L
           `         ` `.   \\   j         /  .,' ,\"_.....`.`.`   \\   |
            `.        `. `.  \\  |        / ,'/ .','..... `.\\ \\|   .  |
              `.        `. .  \\ |       j . / ..'.,-\"\". \\ || ||   |  |
                `.        `.`. \\'.      | | | |||.   .,.','/ /'   |  |
                  `-.       `. .:\\      | | | ||'`..___.'.','/   j   |
                     `-._     `-._\\      \\'.`.`..`..__....','   ,   /
                         `--......-\\      \\ `.`.`.......-\"'   ,'   /
                                    `.     `. `-..____,.-\" _.'   ,'
                                      >.     '--...___,..-'   _.\"
                                    ,'  `--,__            _,-\"  `-.
                                _.-'      '   `'--------\"' `.      `-.
                              .'        ,'                   \\        `.
                             .        .'                      `.        .
                             |      ,'                          `._     |
                              `----'                               `\"--\" 

         ''')

    elif n_pokemon + 1 == 61:
        print('''             ___   _,-'\"\"-.
                    /`.  `./,\\`.    `.
                   /'. |  / || |      .
                  . `|,+-'| `| |       `._
                  `,-'    `. | '          `.
                 ,' -'      `\"'             `.
                /\"`-.                         `.
               :`.   \\                          .
              ' `.\\   \\                          `
             .`.  .`   `           `.             .
            / `.'  .`   .      .     \\             \\
           /``  .`  `\\   .      \\     .             .
          j  .\\  .:  .'  :       .    '             |
          |`. .. ||  :|  |        ,..--`._          |
          |:| |: :|  |:  |      ,'        |         |
          ||| :: |:  |:  |      |         |         |
          :'j '| :|  :|  |      |         |         |
          `/ .j  ,:  :|  |     ,'         `         |
           \\/ / . '  ',  |   .'            \\        '
           ` , /,'  /.  j   |               .      /
            `.'/   /'   '   |  .             .   ,'
              .  .'/   /    `._/             '  /
               `.,'   /       |          __,' .'
                 `-._,         `.   _,.-\" _,-'
                     `+..____    `\"'    .'
                    _/    |  `\"\"\"''\\    '
              _,.-\"'      \\        |     \\
          _.-'             .       |      `
         ,                 |       |       `.
         `_          __,,-'        '         `.
           `'\"\"'\"'\"''             .            .
                                  |            |
                                  '            /
                                   `.        ,'
                                     `-..,.-' ''')

    elif n_pokemon + 1 == 62:
        print('''                               __,.-\"\"\"'\"--..._.,---.
                                    _,-'               /      `.
                                 _.'                 ,'   ,-\"\"`.|
                               ,'                        / ,+\"`.;
                             ,'   ____                  . |_/  /
                            /  .\"'    `-.               ` `..-/`.  _
                           '  /                     .    `---'   `: `.
                          /  .    ,-\"\"`.           .'             \\`-.`+\"\"`\"`.
                         /   |  .' ,\"\".|               _,...,._    L |  `     `.
                        /    |  | ._)  /     \\    _.-\"'        \"`. | j          .
                       j     `  ' |  ,'        ,-'   ___......_   .|\"           |
                       |         `-+'        ,'  _,\"__.---\"\"\"`-.`.||            |
                       '                   ,'  ,'.-'    _______ `.`|\\           |
                     .\"                   /  ,\",'   _,\"+.------+`.`:|           |
                   ,'     .             ,' .,-'   .\".-'  _..._  ` \\''    .      ;
                _,+      /             ,  ,/    ,'.' .-\",.----.+ `7  `.   `._,.'
               /  '    ,'             .  '.   ,\".\" .:,-'__     :|j     `-.-'
              j    \\  /|`            ,  //   .,' ,'.' .\"__`.   ||'
            ,-+     `\" | \\             /.   //  /,\" ,'.'  \\ \\  |'
           /           '  \\         : j '  //  //  .,'     || ,\"
          /           /    \\        | :|  j.' j/   ||_.\") , ;<_
         .            `-.   `.      : ||  || |.    `..-'.'.'   `'-._
         |              |     `.    | |:  :| |'        _,'          `.
         |              |      /`-._`.`:. \\' `.`..__.-'+              `
         `          .   F     ,     /\"`+-+.^+--`\"\"\"     `._            |
          `.       |   /     /     .                       `._         /
            `._   _,..'    ,'      '                          `\"-....-'
               `\"\"        /       j
                        ,'        |
                       /          |
                      j           '
                      |          /
                      |         /
                      '        /
                       `.___,.' ''')

    elif n_pokemon + 1 == 63:
        print('''                                                        _
                                                            _, -\"'|
                                                        _.-'   ,'j
                                ____           _,.....-'      /  |
                               `.   `'--..,--\"'              .   |
                                `.                           |   |
                                 .`.                         \\  j
                         _.,     '  .                         ` |
                       .','       . |                            \\
                     ,\" /         `./                             \\
                    /  /           /                    ,-'        \\
                  ,'  j           j  .._              ,'            L._
                 /    |           |     `.          ,'             ,'  `-.
                .     |           |       `.       .            _,'       `.
                |     |           `.        `               _,-'            \\
                |     `           / `-.                  ,\"/                `.
                |    _.\\         j     `-.._       ,   .' |                  ;
                '  ,'   \\        |        _,'.    '  ,'    `.              .'
                 +'   ,.-^.      `-..,..-'/ _,^-----+.       `._       _,-'
                 .+--`._   `-._     L_   j-\"          `-.  _,-\\ `..,--'
                   \\    `      `\"-+'  `-.'               \"\" ,.'/ ` |      ,
         _____      L    `       /       `.._.----.._   _.-'  /   F     ,'|
         `.   `.    |     \\     '.           `\"\"\"-+.-`\"'     '    |`. ,'  |
           `.   `.  |      L   _,+\\__              `          \\   |/ /    |
             \\    +,'      |  '     `.`._           `.         |  |.,     |
             `.  '         |,\"        \\  `.          |.      _,|         /
               `           |           |   +.       / | _,-+'  |        /
                \\          |          '    |\\.     /-',\"  /    |       j
                 \\         |         /_    | \\`..,-\".\"   |     j       |
                  \\         \\ _   _,'  `-.  `-,|/___.\\,-.|    /        '
                  `         `' \"\"\"        `\"\"'            \\  |        .
                   `. ,\"\"'   |                             `-+`./     |
                     `.     '                                  |      F
                       )   |                                    \\    /
                      /__,.'                                     \\,.' ''')

    elif n_pokemon + 1 == 64:
        print('''                       .-
                                | \\               _,
                               j   \\           ,-' |
                               |    \\       ,''   .'
                               |     \\    ,'   .  |
                  .-`.        .|    __\\_,'    ,  ,
                ,'   |        ||  \"\"        .'  /
               .     +.      ,\"'           .   /   ___
             ,-.\\ _,`.'     ,  __._        `. ,  ,'   |
             .  `'   /     /  <   ,'    _    \\`.'     `-,._
          ,\\_|`.,-`.'     /`. `-^-'  _.|    .-\"||     .'   `-.
         ` `. //`.`      j \\`.     ,'|)|   ,\\  |`.    |  ,.--'
          `. `'`//       |  `|   .:,-'     |`.'   `.___`\" '
           `.|>,'\\       |`..|  /     ____.' |    `-. >    \\,_..._
           // `   \\     ,',-'| /  \"'-\".  ` `.`.    ,-\"\"\\  ,'      `\".
          (/   :  `-._,/ /,'`./  '\"-._ `. `. ``--..\\_,-' ,'          \\
               '.    .',' /'|     /|  `. `. ._.__ _,'.\"|'             \\
                 .   `,' /  |  ` /-'    \\  `. ` -..-'  |\"`.            '
                  `--'/ /    `+-'        \\  ``.       .    `.          `
                     ' .       `-.  ,-\"--.+  \\ .    .' `.    `    .   | \\
                    '| |          `.\\,\" ,. ` ' '_.-'     \\    \\   |   ' |
                    |' |    __,.-\"' .| '|`. . \\`.   \\     \\    .  | ,'  |
                    || |  ,'\\        .`. V  | |     |      .   |  '   /.'
                    `| | /   `._     `. _|  | ||    |      |   | /..-' /   .
                     ' . '      /`---'.`.`._| '|,--.|      |   |'     /    '|
                      . . \\    ,'      ` \\/ '/ `    `._    '  ,'     |   ,' |
                       `.\\ `.  \\        `. .'   |      `.,' ,'|      '+-'   '
                     _.--`.-j   `-.-..    `-.   `-.     | ,/  `.       `  .'
                   .'_.'+\"\"' _   _,.'-`      `-..._,\\   |-'     `-...__..'
                   ' /_..|/-' `\"'                ,_.`'   `..__
                                                   `.  `-._  ,-'
                                                    `,..`. `/  |
                                                     :  /    `.'
                                                      `.' ''')

    elif n_pokemon + 1 == 65:
        print('''                                               _,'|
                                                      .'  /
                             __                     ,'   '
                            `  `.                 .'    '
                             \\   `.             ,'     '
                              \\    `.          ,      /
                               .     `.       /      ,
                               '       ..__../'     /
                                \\     ,\"'   '      . _.._
                                 \\  ,'             |'    `\"._
                                  |/               ,---.._   `.
                                ,-|           .   '       `-.  \\
                              ,'  |     ,   ,'   :           '__\\_
                              |  /,_   /  ,U|    '            |   .__
                              `,' `.\\ `./..-'  __ \\           |   `. `.
                                `\",_|  /     ,\"  `.`._       .|     \\ |
                               / /_.| j  ---'.     `._`-----`.`     | |
                              / // ,|`'  `-/' `.      `\"/-+--'    ,'  `.
                          _,.`,'| / |.'  -,' \\  \\       \\ '._    /     |
          .--.      _,.-\"'   `| L \\ \\__ ,^.__.\\  `.  _,--`._,>+-'  __,-'
         :    \\   ,'          |  | \\          /.   `'      '.  `--'| \\
         '    | ,-.. `'   _,--' ,'  \\        `.\\            7      |,.\\
          `._ '.  .`.    .>  `-.-    |-.\"\"---..-\\        _>`       `.-'
             `.,' | l  ,' ,>         | `.___,....\\._    ,--``-.
            j | .'|_|.'  /_         /   _|         \\`\"--+--.   ` ,..._
            |_`-'/  |     ,' ,.._,.'\"\"\"'\\           `--'    `-..'     `\".
              \"-'_,+'\\    '^-     |      \\                    /         |
                   |_/         __ \\       .                   `.`.._  ,'`.
                           _.:'__`'        `,.                  |   `'   |
                          `--`-..`\"        /--`               ,-`        |
                            `---'---------'                   \"\"| `#     '.
                                                                `._,       `:._
                                                                  `|   ,..  |  '.
                                                                  j   '.  `-+---'
                                                                  |,.. |
                                                                   `. `;
                                                                     `' ''')

    elif n_pokemon + 1 == 66:
        print('''                        ,.\"--.
                            _.../     _\\\"\"-.
                          //  ,'    ,\"      :
                         .'  /   .:'      __|
                         || ||  /,    _.\"   '.
                         || ||  ||  ,'        `.
                        /|| ||  ||,'            .
                       /.`| /` /`,'  __          '
                      j /. \" `\"  ' ,' /`.        |
                      ||.|        .  | . .      _|,--._
                      ||#|        |  | #'|   ,-\"       `-.
                     /'.||        |  \\.\" |  /             `
                    /    '        `.----\"   |`.|           |
                    \\  `.    ,'             `  \\           |
                     `._____           _,-'  `._,..        |
                       `\".  `'-..__..-'   _,.--'.  .       |
                        ,-^-._      _,..-'       `.|       '
                    _,-'     |'\"\"'\"\"              `|  `\\    \\
                _.-'         |            `.,--    |    \\    \\
           _,.\"\"'\"\"'-._      '      `.     .      j      '    \\
          /            `.___/.-\"    ._`-._  \\.    |      |     L
         /  ____           /,.-'    . `._ '\"\"|`.  `      |     |
          `.    `\"-.      / _,-\"     `._ `\"'\".  `. \\     '     '
            \\       `-   .\"'            \"`---'\\   ` `-._/     /
             `-------.   |                     \\   `-._      /
                      \\ j                      .       `...,'
                       `|                       \\
                        '                        \\
                         .                      / \\
                         |`.                   /   `._
                         |    `.._____        /|      `-._
                         |        |   Y.       |.         `.
                         |       j     \\       '.`\"--....-'
                      _,-'       |      |        \\
                   .-'           |     ,'         `.
                  '              |     |            `.
                  `.        __,..'     '.             \\
                    `-.---\"'             `-..__      _/
                                               `'\"\"\"' ''')

    elif n_pokemon + 1 == 67:
        print('''           ,-\"\"\",.--
                  ,:-'_.--\"\"\"\\
                ,\"/,-'  _,..--+-.
               .,'/ _.-'         \\
               |||,'_.-.          \\ ____
               |.','U| |         .-'    `-.
             ,\"   |_L:/        ,'          `.
            j                 /              .
            \\_______...-7    j           ___ |
             V V/     _.'    |    _,.---- ,_`\"-.
              ,/_...-\"   __.-|  -\"    `,.   ``.'`.
              `..,......\"    `.  | \\    `+`. `  \\ .
                j /            `./ \\\\    ` .  \\\\ . .
                | |               ` `\\     \\'  \\' \\|
                | |              | `.`+. /         \\
                ` '              |   `\".',  `\\  `|  )
                 \\ \\           .'     . ||   || ||.'
                  `>`.,.....-----\"'\"\"\"\"\\`|   |' |||
                  / .||D.\\\\|.'\\ () (_) (\\|  j|  j/|
                 / +,|| ||||_____........|  || / .'
              _,'.\"'_|\\.'/|   _,---._    |  .' ,'
           .\"' .   '\"j-...' ,' ,     `. .'  '  |
          /  ,/  ,'.'`     /  /       ,'       `.
          | /| ,`./   \\   / .'        |         |.
          | ||_|./ .   `.j /          `.        | )
          `-'`.+' /      | `          ,'`.__     Y
              .' /       | `.       .'   /  `\"\"'\"
              |  '      /|    .___.'   ,'
               `.   / -' `.        ,   `.
                |  /       `+.     |     `.
                |  \\        | `    `       \\
                 \\  `.      |`.`.   `.      |
                  \\   `.    |  `..    `.    '
                  /     `-. |    `.     `  /
           ____.-'          `.  _,'      --\\
         ,' .'_.,_.         __:\"            `.
         | ( | (         ,-\" ,-'.\" ,'_.      |
         `-`-^--`--------'__|__(  | /   _,--\"
                                \"\"--'..' ''')

    elif n_pokemon + 1 == 68:
        print('''                 __.\"`. .-.                    ,-..__
                       ,-.  \\  |-| |               ,-\"+' ,\"'  `.
                       \\  \\  \\_' `.'             .'  .|_.|_.,--'.
                        \\.'`\"     `.              `-' `.   .  _,'.
                         \\_     `\"\"\"-.             .\"--+\\   '\"   |
                         | `\"\"+..`..,'             `-._ |        |
                        j     |                       '.       _/.
                       /   ,' `.      _.----._          `\"-.  '   \\
                      |   |     |   ,'  ,.-\"\"\"`.           |  .    \\
             __       |   '    /-._.  ,'        `.         |   \\    \\
            (  `.     `.     .'    | /  _,.-----. \\       j     .    \\
             `. |.  __  `,         |j ,'\\        `|\"+---._|          ,
          .-\"-|\"' \\\"  |   \". '.    ||/d |_-\"\"`.    /     ,'.          )
          `._. |  '.,.'     '  `  ,||_.-\"      |  j     '   `        .
         .\"'--:' .  )        `.  (     _.-+    |  |                  |
         `-,..'  ` <_          `-.`..+\"   '   ./,  ._         |      |
          `.__|   |  `-._     _.-\"`. |   /  ,'j      `. `....' ____..'
            `-.,.'    \\  `. ,'     ,-|_,'  /  |        `.___,-'   )
               `.      `.  Y       `-..__.',-'    __,.'           '
                 `         '   ,--.    |  /            `+\"\"       `.
                  `.       ,--+   '  .-+-\"  _,'   ,--  /     '.    |
                    `-..   \\     __,'           .'    /        `.  |
                        `---)   |  ____,'      ,....-'           `,'
                           '                 ,' _,-----.         /
                            `.____,.....___.\\ _...______________/
                                           __\\:+.`'O O  O O  O |
                                       ,-\"'  _,|:;|\"\"\"\"\"\"\"\"\"\"\"\"|
                                     ,'   ,-'  `._/    _.\"  .`-|
                                  .-\"    '      \\    .'      `.`.
                                 :      .        \\   |        / |
                                  .      \\.__   _,`-.|       /  |
                                  `.      \\  \"\"'     `.         `....
                                    .     |            \\             `.
                                   .'   ,'              \\              |
                           ,------'     `.               `-...._  '\"-. '.
                          / ,'\"'\"`        |                  `--`._      `.
                          `\"......---\"\"--'                         \\       .
                                                                   |        `.
                                                                  (   -..     .
                                                                   `\"\"\"' `....' ''')

    elif n_pokemon + 1 == 69:
        print('''                _.--\"'\"\"\"--._
                       .\"             `.
                      /                 .
                     j                   .
                     |                   |
                     |                   |
                     | (')              j
                     `                 ,`.
                      \\               ,^. `.
                       .             /   \\  .
                       |            /     . |
                       |          ,'      | |
                      ,'---..___ /        | |
                     ' `--..___ \"`.      .  |
                      `\"--....___.'     /  j__.....__
                                       /   |         `.
                                      / _,------._     `.
                                     /,+_         `.     `.
                                   ,'    `-.        \\      .
                                  .         `.       \\      \\
                                  |           `.     |       \\
                                  |             `.   |_,..__  .
                                  |\\              \\  |      `.|
                                  | `.,--------._  \\ |        `
                                  |  |           `. \\|
                                  |  |             `.|
                                  |  |
                                  |  |
                                  |. '
                                 .' \\ `.
                              _,' ,' `. ._
            ---====+,______,.\"_.-'     .  `.
            _,..==`'_.+'-\"\"\"\"'         / ^.\\`:._
          ,=\"/    ,\"            ....==+ /  `\\  `:.
         '  /    / |               _+:-'    .|   ``.
                '  `.           --\"\"        |'     `\\
                                            ' ''')

    elif n_pokemon + 1 == 70:
        print('''                                    _...._
                                           ,'   __ `.
                                         .'   ,'  `. |
                                        .   .'      .|
                                       /   .        ||
                                   .-\"'\"\"\"-'        ,'
                               _,'\"\"\"'\"--._ `.
                             .'            `.:
                           ,'                `.
                          /     _              \\
            ..--._       /     ._;              \\
          ,'      `.    j                        .
         .          `.  |                        |
         |           ,+-' ,-\"\"-.       _.-\"'\"\"\"`\"`._
         |          : |/ /`.    |    ,'             `.
         |          |// :  |    |   ,                 '.
         '    .     |/  '-\"     |  /                    `.
          `    \\   ,'    `-...,'  j                       `
           '._/_\\.'               |                        `
           .'   `\"-._             |                         \\
           |         `.           |                          \\
           | --+.      `.          .                 ___      .
           '   | `.      `.         .           _.-\"\"   `\"._  |
            .  '    .      `.        `-.____,.-' /          `.|
             .  `    `.      .                  /             `
              `. `.    `.     \\                ,
                .  .     .     .             ,'
                 `  `.    `.    .           .
                  `.  `.    .   |        _,'
                    `    `. |   |      ,'
                     `.    `'   |  _.-'
                       `-.      ;-'
                          `--..\" ''')

    elif n_pokemon + 1 == 71:
        print('''                                       ___
                                             ,\"\" __\"`.
                                            / .'\"   `-`.
                                           / /        ` .
                                     _,.__. /_,...._   \\ \\
                                  ,-'     |j        `-._\\ \\
                               _,'        ||            `._\\
                             ,'_,..,.      |        .----._`.
                           _,\"'   / /     `'         `.   :`-'
                                 / j               ,_  \\   `|
                                j ,'-._      _..-\"\"' | `.  ||
                                | |    `'-.,'        |  |  ||
                                | |  _.              ' j   ||
                                ' '.'.'         \\\"-./ ,    |'
                                 ` `/_           \\_/ /     | L
                                  `._ `-..___,.-'\"_,:      | |
                                   | `._      _,-' ||      | |
                                   |`..,+----`.__,\" |      | |
                                   |                |      | |
                  _.--\"\"\"\"--._     |               _'    _.+-'\"\"\"'`-._
                ,'            `-.  |.-.           , `\\ ,'             `.
              ,'                 \\j |  |          `./ /                 `.
             / _.--\"\"\"--._        | `-\"               |    _,.-------.._  \\
            /.'           `-.    j                    | ,-'             `-.\\
           ,'                `-. |                    |'                   '.
          /   __                \\|                    /                      `
         j .'\"  \"-..             |  _         ,\"`.    |           _,.--'\"\"'-. .
         |/:        `._          / | \\        |  |    |        _,:           \\|
         ` '           `-._    ,'| `.,'       '.-'    `..__,..' '`.   __
          '                `\"\"'  '                    ;          `.`.'  \"'--...,'
                                  .  Y.          /\"','             '-..____,.-'
                                   `-._         _`-'
                                       `\"------\" ''')

    elif n_pokemon + 1 == 72:
        print('''                             _,--'\"\"\"`\"--._
                                    ,'            _.-+._
                                ,-.'            ,'      `.
                              .'  |            .          `.
                             /    '            |            \\
                            /    /             |             L
                           /    /            . |             |
                          j    /             | '             |
                          |   /              '  .            |
                          |  j  .             \\  .           |
                          '  | /               `  `.       .''
                           \\ |j                 `.  `-....\" j
                           |`'|   ,',..           `.._      |
                           `. `   |/   \\              `     |
                             `.   `.   |                    |
                              |     `__'                    |_,..---..
                            __|                            ,'         |
                         .\"\"  '     .    '               ,'           |
                         |     .    |     \\   ____     ,'             |
                         .      `-..L      `,'u   `:-./              j
                         '        |u \\     /    _,-'  |             /
                          `.   ,./`\"\"`\\_ ,'`\"--'      |            /
                            `./  \\..._  |    _,..._   |.---+.    ,'
                             / ,'     `.|  ,'      `--'-.   \\`--'
                            j .         `.'              `.  .
                            | |                           |  |
                            | |                           |  |
                           j j                            |  |
                          ,' |                            |  |
                    ___.-'  ,'                            |  |          _,-..
             _,.-'\"\"   __,.-'                             |  |       ,-' ,--\"'
          ,-',.-' _,.-'                                   |  '     ,'  .'   /
         . ,' _,-'                                         .  `---'  ,'  _,'
         |/ .'                                              `.    _,' _,'
         `-'                                                  `\"-`.,-' ''')

    elif n_pokemon + 1 == 73:
        print('''                                      _.._,-\"\"-.._     
                                      _....\"\".'_,./        `.
                                    .'  ,|   ,'   |          `.
                                   ' _,'\"'\"\"'      `.          |
                                  .,' ___            `--....__ |
                                 ,|.\"\"   `-.____,.--'\"\"\"\"`-._ `'.
                               ,','            _,.--         `.._`.._
                             ,.,'          _.-\"   /'\"\"-._        `\"'-`.
                            /      ,-\"\"\"-,'-.._,.'       `.           |
                           (      |`.__,' `.      ,-.      |         (
                            `._   |_.'     |  /|  ` |,\" .  |          |
                              /`  |       .'  |`   `.'.`\\`/          ,'
                             '._ j       /   .` .    .``.`.`-._ _,.-'
                                `/      /    ||`.`    `..``.`-.`.._
                _              ,'      /,.___'|  ``.,..-\\`-\\`/ `._.+,------._
               \\ `\"-.__      ,+      .'|| | j |+-+-`._`+.\\+--\"\"\"\"            `-.
                `._    \"'\"'\"'/|     j| |' . | |\\`.`.  |+---+--+-+--.....__      \\
              __..-`--------+-|     || | \\ / / \\\\ \\ \\ | `.\\ \\. \\ \\   `. `.`-.___/
            .'       _,.-',','`     || |  /,\\  ` \\ ' \\|   `\\ \\`.\\ '    \\  \\
          ,'     _,-'    / . .'\\    || |,'/\\ \\  \\ \\ \\ |    | |-. L`+._  \\  |
         /    ,/'       . j  | |\\   '.-'.'  \\ `. \\ \\ .|    / `  `| |  `-.`-'
         |   ,'        j  | j  | `.  `.\"\\    `  \\ . .|'   /|  \\  | |`.   .
         `..'          .  | |  `.  /. `. `    `. `| |/   / |  |  |  . `-.'
                       |  | `.  | /  +. \\ `.    \\ |,'  ,'\\ |  |  |  |
                       |. |  `..' | .' `\".  .   _\\+  _.| | |  '  '  '
                       .`.'       `-'    `--'  '--+\"'| `.' `-'  `..'
                                                  `--' ''')

    elif n_pokemon + 1 == 74:
        print('''                                            _,.---.
                                                 _,-'       `.
                                              _,'  ,          \\
                                            ,'  _,'   .        `.
                                           /  ,'     ,'          `.
                  __                       .,'    _,'              `.
             _,..'  `-....___              :    ,'     '             \\
           ,'   /            :             /`.,'      /               `
          /    /  ._         |         __..|  `.    .'       ,         `.
          |   |   ,'\"--._    |      ,-'    `-._`.,-'       ,:            .
         .'\\   \\     _,'.    `'___.'           `\"`.     _,' /            |
         |  \\   \\---'       ,\"'  .-\"\"'\"----.       `.  '  ,'             |
          `. `-.'          /    /                    `-..^._             '
            |._|    _.    /    /                            `._           .
            `...:--'--+..'   ,'                              /            |
                '._  `|   ,-'       _..._                   j     \\       |
                  |` |   /       ,-'     `-.__              |      L      |
                  |  |  /      ,'                           |      |      |
                  |_,'        /         _,-                  .     |      |
                 ,'  ,   |  ,'        ,|            ,..._     \\    |      '
                ,     \\ j  '       _.\" |           /     `-.__'    '    ,'
                 +._   '|       ,'|    |          /        ,'    .'    /
                 |  `._  `-' .:|  |    '.       -'        '           j
                 '    |`    ' |'  |     |                             |
                  `.  |       |--'     _|        .                    |
                    \\ |       '----'\"\"\"           \\      __,....-+----'
                    | '                            `---\"\"      .'
                    `. `.                                     ,
                      `\" \\_...-\"\"\"'--..         _+          ,'
                           '            -.'  `-'  `.  .\"-..'
                            `-..._            _____,.'
                                  `--.....,-\"' ''')

    elif n_pokemon + 1 == 75:
        print('''               __..  ,..--+'\"\"--.._
                     ,-'    \\_|_...'        |
              ,'\\  ,'`.,----\"    '          |.._
             /  _\\_'   `.                _,.+.  `-.___
             |          |           ,.--'     \\       `.
           /'|          |\\,-.       |          `\"--.    `.
          |  |          |/   \\                      :     |
          |  '          /    '                      |     |
          `.|         ,'    /                       '     `
         |\"j               _,\\                             \\
         | /  ,          -'   \\                             \\
          |  '/     _.-       |            _,.               `..
         .'| /   ,-'/     --- `         -\"'   `.                |
          `| `--d  |         __        __       |        __     |
          /    /...'   .  ,\"'  .         `.    .'          \\    |
         '..-----.._ ,'   |    '           \\    `           |   |
            |/  _,.-'     '                      \\          /  ,'
           /'\"\"'                      .\"\\         \\       ,'   |
            -...--.__                 `  \\        _\\..     \\   `.
             `.                        \\\"        :   |     |   /
              |    _..-.    ,..-.       `.    ..\"    `     /  .'
            ,-|   |     `---;             |           `.  '   |
            \\  `. `---._ '\"\"`---.         |             | __.-'
            |..\"|+.\"`-'        /         j.            /  |
             `. | \\          \"'      _.' '|           /  /
              |\"\"`.`\"'          __,\"\"  __.-          j ,'
              .--- \\ `--------\"'      ,              +'
              |__,' `+.          .    |.            |
            ,'  |     \\`-.___,-' `.__.' `.          |
            |._,'   | |   |         |   ,'\\    '.   '
            |\"`.--|-+.' _.'         |`..  /`--/ :.-.|
            '  |  \\  |,'.. _     .-' _ .-'   /.-'  /
             `-'   `.|_(._|______|_ /  '.__,' \\,...'
                                   `\"-------'\" ''')

    elif n_pokemon + 1 == 76:
        print('''                            _____   ____
                                _,.,|     `\"`-.._`--._
                             _,\" ,j |            `\"-. `-,
                          _,\"_,-' ' |._              `.  \\`.
                        ,' ,',.....L   `-._            \\  . `.
                      .' ,\"'\"`.__  |       `-.._        | |   \\
            ,.._     ,'-/     '  `.|..'\"\"|`._   `-.___.-','-._ `.
          ,' . _>-.._/ /     /    /   `-.' \\ `-._  |   ,'     `-..
         /,..|`._'  / /     /   ,'   _ _\\   `.   `-:..'          `\\
         ''  | .--./ /     /   / ,'\"\"|/ .'\"\"'\\`.._ |  \\            |
           /'`.   / |`...+.   /.' _.`+._ `._/ \\'| `|\\  `.____      |
          /,..:.-+ _|.-\"'\"\"`./__.\"      `.|    j   `.\\  /---._\"---.|`.
          '     _:\"    ____  | |          `+---'     `\\/       \"-._| |
              ,'    ,+\"  |   ' '.           \\`.       |            `.|
             .     d |  /     \\  \\          |  \\      |             ||
             |   _/..+.'       \\  \\      __,^.  '._   |            j |
            ,'_,'        ___    \\  `----\" ,.--`+..,.-'+`-.._       | |
           ',\"     ____,'/     / +...--'_,.--\"'||       '._ `-..__/ /
            `...--\"'|  .'   _,'| / ..-'\"       ||          `.    / |
                   ,'./ ,.-'   |j |          __||          .'`,\"__.'
                   \\__.'\\     j | |        ,'    `-.     ,\" ,'.\" .'
                       \\|     | 'j       ,'         `. ,' .',' .'
                      . `.____|/ |__    :            |`,-'.'_.\"
                      '.  `._ _.\"-._`-._|            +----'\"
                        `.   `\"\"-.._`-._|            |
                         |          `<\" `.           |
                         /            `.  `.         '
                    ,.\":\"_,-           |,..'          `._
                   '.__|' ,--.    __,.\"'> .             /`.
                       '\"\"`---`'\"\"  \\_.' _|-\":__,....--'\"''
                                      `-',..-' ''')

    elif n_pokemon + 1 == 77:
        print('''                    .' .
                            .| '\\
                    _...___/`'   .
                  ,'             |
              ,|,\"             )/|                             , .
             / |              / , .                            \\` \\
            /            ...-'  ',                              .  \\
           .           ,>      .                                |   |
           |          .'   ___`,                  .'  ,--.._,.-'/  ,'
         ..|          |.-\"', /                  ,' | /       .\"'   '.
         \\ '          |  ,'//                   .'  \"    __,._'    |
          \\ `         /.\"_/'_,                 '.       /         _'
           `.\\     _,'   \\.`  ) ,^.              `     '       ,-\"
             |.  .'  _   | `. '-  `,            , \\     `.    ,-
             | `w  ,\" |  |   \\   .'   _,_ :\"'. / 7 . ,`..'   .'
             '|    `.'  /     \\   `-'\"   `   _:_,.}|  :  _. ,'
              \\       .'       `-.      _,.-\"       `-+-`  '
              |       |           ``--\"'               `.
              \\   .- .                                   \\
               `.._,\":                                    \\
                     '                                    `.  '-7
                      \\                                  .'`-\"  :
                       \\                        .        `      `-'
                      j \\                       `.        `.     |
                      |  `.  |      .^,'.       ,.+        :    _'
                      |   |`.|      |    \\,  ,-'  :`.       \\  /_.,
                     /    |  |     /     .,-'.     `.`.      \\   /
                    /    .' j     / _._,\"     `      ':`.     . (
                   /    /,-\"|    j  `.         `-.    |  .    |/
                   .   `'   |    |    7           |   |   |   |
                    `.   .  |    |  v'            |  .'   |   |
                      `.  `.|   j'.'              |  |    |  j
                        \\   |   |                j   |   j   |
                         `.j   /\\                |_,j    |  j
                           /  /`\"              ,\"   |    '  |
                          /  j                 '_,.-'   /.-'|
                         |   |                         /__.-'
                        .'`-.'
                       /    |
                       `----' ''')

    elif n_pokemon + 1 == 78:
        print('''                     :`./
                             _|  ,-
                        ,'\"\"'    ,`
                      ,'.\\       `.    __  ,.-.
                   . ./ `'    __  '. ,'  \\ `.|
                   \\\\  \\   .\"'  L   \"     `\" `\\                          _,-.
                    \\` |\\.`      7     .,   :._|   --'`.                 ` |
                   ` \\`+ `'\\      \\^--\"  `. |    ,'     `.            ,..' |
                    | ,.    |              ` `.  |    ..  '.          |    /
                    ':P'     '.    ,..      \\  `-+`\"-'  `._ \\     -`,- ..,'
                   /        / `-,-'  ,'`.    `.   ; .--'   `+    '.   | ,
                  /     _..     .   `-.  \\,.   `-'  '.  `.^  `\".__|   ' |
                 '   , / |       `.   \\    |        ,'     \\           /
                  `\"' \" .         \\   |  __ \\    ,-'       `----.   _,'
                       /           |  `\"' _} `\"\"'                `-'
                      /.'         /     .-.         ,\".
              .._,.  /           /     '-.,'    ,'-. .'.
             /  `. \\/             `-.      `.   /`.  :
            /  __ `.'                '-.     `-+_.'  .'          ,__
           / .'  `.___                  `,..__      <__          \\ (
          / /       \"..   /                   `-.     .' .-'\"`--.'  \\
         /  |       /-'  /                       \\ ,._|  |          /'
         \\.'|+.+.  (`..,'                         \\`._ _,'           \\__
          \\ |||| \\ _`.^ `.            .            |  \"    .'`\"-.       `.
           `+'|/ `( \\'    `-....__    |            |._,\".,'     `,        |
                                  `:-.|            `           ..'   ,'`.,-
                                   |  |            |`.        '-..    . /
                                   '  |           /  /           `.   |
                                    ` '          /  ',.         ,     `._
                                     \\|        ,'   \\'|         :  __    '
                                      `,     ,`     .._`..       `'  `-,.`.
                                _`'`\".  `.   ``-._ /   F   )        ,._\\ `
                               '-\"'`, \\   \\ ,. ).-'-.^,|_,'         `  '.
                                   '.. \\___j  `\"'               ,..  | .'
                                      \\            ___       ,. `\\ \\,+-'
                                       7.._   .--+`.  |_    |  `,'
                                    _,'  .'`--'  '    7 ` v.-
                                  .\"._  /-.  -.   \\.^-`
                                .'  __+'...`'  `--'
                                 `\"\" ''')

    elif n_pokemon + 1 == 79:
        print('''                                  _.---\"'\"\"\"\"\"'`--.._
                                      _,.-'                   `-._
                                  _,.\"                            -.
                              .-\"\"   ___...---------.._             `.
                              `---'\"\"                  `-.            `.
                                                          `.            \\
                                                            `.           \\
                                                              \\           \\
                                                               .           \\
                                                               |            .
                                                               |            |
                                         _________             |            |
                                   _,.-'\"         `\"'-.._      :            |
                               _,-'                      `-._.'             |
                            _.'                              `.             '
                 _.-.    _,+......__                           `.          .
               .'    `-\"'           `\"-.,-\"\"--._                 \\        /
              /    ,'                  |    __  \\                 \\      /
             `   ..                       +\"  )  \\                 \\    /
              `.'  \\          ,-\"`-..    |       |                  \\  /
               / \" |        .'       \\   '.    _.'                   .'
              |,..\"--\"\"\"--..|    \"    |    `\"\"`.                     |
            ,\"               `-._     |        |                     |
          .'                     `-._+         |                     |
         /                           `.                        /     |
         |    `     '                  |                      /      |
         `-.....--.__                  |              |      /       |
            `./ \"| / `-.........--.-   '              |    ,'        '
              /| ||        `.'  ,'   .'               |_,-+         /
             / ' '.`.        _,'   ,'     `.          |   '   _,.. /
            /   `.  `\"'\"'\"\"'\"   _,^--------\"`.        |    `.'_  _/
           /... _.`:.________,.'              `._,.-..|        \"'
          `.__.'                                 `._  /
                                                    \"' ''')

    elif n_pokemon + 1 == 80:
        print('''                   ,-'\"-.
                      __...| .\".  |
                 ,--+\"     ' |   ,'
                | .'   ..--,  `-' `.
                |/    |  ,' |       :
                |\\...-+-\".._|       |
              ,\"            `--.     `.     _..-'+\"/__
             /   .              |      :,-\"'     `\" |_'
          ..| .    _,....___,'  |    ,'            /\\
         ..\\'.__.-'  /V     |   '                ,'\"\"
         `. |  `:  \\.       |  .               ,'         ,.-.
           `:       |       |  '             .^.        ,' ,\"`.
             `.     |       | /               _.\\.---..'  /   |     ,-,.
               `._  A      / j              .\"       /   /    |   .',' |
                  `. `...-' ,'             /        /._ /     | ,' /   |
                    |\"-----'             ,'        /   /-.__  |'  /    |
                    | _.--'\"'\"\"`.       .         /   /     `\"^-.,     |
                    |\"       ____\\     j             j            `\"--.|
                    |  _.-\"\"'     \\    |             |                j
                  _,+.\"_           \\   |             |                |
                 '    . `.     _.-\"'.     ,          |                '
                |_    | `.`. ,'      `.   |          |               .
                | `-. |  ,'.\\         .\\   \\         |              /
                |\\   ;+-'   \"\\      ,'  `.  \\        |             /
                '\\\\.\"         \\ _.-'     ,`. \\       '            /
                 \\\\\\           :       .'   `.`._     \\          / `-..-.
                  ``.          |    _.\" _...,:.._`.    `._     ,'   -. \\'
                   `.`.        |`\".'__.'           `,...__\"--`/  |   / |
                     `.`.     _'    \\|             ,'       ,'_  `..'  |..__,.
                       `._`--\".'     \\`._      _,-'       ,' `-'  /    | .  ,'
                          `\"\"'        `. `\"'\"\"'   ,-\" _,-'    _ .'     '  `' `.
                                        `-.._____:  |\"       _,\" .\"  ,'__,..\"'
                                                  `.|-...,.<'    `,_\"\"'`./
                                                      `.'   `\"--'\" ''')

    elif n_pokemon + 1 == 81:
        print('''                                  _,._,._
                                          '-\"._,\"--,
                                           `\"..-+-'
                                           :'==-:
                                           :`=-\":
                                          _.\"-..|
              _____                  _.-'\"  `\"\"' `-._
             |  |  `\"\"'----._      ,'                `.
             |__|            `.  ,'                    '.
             '..|\"\"'---._     | /                        \\    _.......______
                   `\"\"\"--:    |/         ,.---._          \\ .'.------.....__`-...
                         |    j        ,'       `.         . '              |\"--|
         .'\"\"|\"---......-'   .|       /           \\        |'     ______    |   |
         |   |              / |      .      .      .       |    .'      `\"\"`--..'
         :\"\"'|---.....___.-'.'|      |             |       |    :
          `\"`+---....____,.'  `      `.           /       /|    '_
                               \\ _,..  `.       ,'       / `      `\"\"'--....,._
                               .'::__:   `-...-'        ,   `._            '   |
                               |-..--|          ,-\"-. ,'       \"--.....___:   j
                               `.::_,          |.-''-:                     `\"'
                                     `\"-...____' \" :.'
                                                `\"\"' 





         ''')

    elif n_pokemon + 1 == 82:
        print('''                                 _
                                       ,\"'_\\
                                  ,\"\\  `.\"  \\       ,..._
                                 '.' \\   \\   .     ('\"\"`.\\     _
                                  \\   \\  `.  |      /=.:.'  ,:`.`.
                                   \\   \\.';  |\"\"\"\"\"`-./   .'   .`
                                    \\   `\"   '         `.'   ,' ,\"`.
                                     `.___..'            `. `..:'`./
                                     /             _,.._   \\    _.'
                          _....__   /            ,\"     `.  ._,'
                      ,-\"'       `\"+.           :         . |
         +'\"|\"\"'-.  ,'               `.         |      \"  | |
         \\\\_|__   `:                   \\         \\       /  |          _,-.
               :)  |        ,.-----.    \\         ._   .'   '._    _,-'`\\  j
           ...,'   |       /        \\    . __ _ _,\".`\"'   ,'   `.,\"    _.`\"
           \\\\ |  _,'      .          .   || |I ' -'|    _, _     `   ,\"'  _.\".
           `\"\"'':         '     \"    |   |`\"'^\"`\"| /  ,`:://\\     \\  `..-' \\  '
                '          \\        /   ,\"\"`--..`\"\"-\"`\"\"':{.|      .      _,+\"
                 .          `-....-'   :`:'-|            |l,'      |.__.-\"
                  \\,.                  '. :/                       |
              .-.\":`.`.              ,'  \"'     ,\"-.   _       _,._|
              \\`. \\`,\"`._        __,:      .    `.'/`,'.`.   .'    '
               '.`.;     \"--+--'\"_  `       `     `.` \"' ; ,'  .  /
                 `\"         ||  :|.  :       `.     \\_:.' :    _.'
                            ||  |||__|         `._        `...\"
                            ||__||| _|            `\"-....-\"\\\\,\\
                            || _| `\"                  \\\\  \\ \\\\'
                            `\"'                        \\`.-\\
                                                        \\\\.' ''')

    elif n_pokemon + 1 == 83:
        print('''        .
               ,' \\\\
              /   ' \\
           _  \\    \\ \\
          / \". \\    ` \\                                        ,.
         j    \\ \\    ` \\                \"\"\"'-. ..          .. :| \\
         |     `.\\    ` `              __ `.  \\: \\         \\ `||  .    ___
          `.     `\\    `.`.            \\ `\"-`. \\ |          \\ `|  |   //  |
          _ '.     `     . `.           `-.,    `'-.._       \\    |  //   |
         | `._`.          `. `         .-'   --._  || `.      \\   | //   j
         |    `.`           . `.      /     .\"\"-.`._|.\".\\      \\,-|'/    |
         '       `.          `. `.   /      | '::|  '|:| .      : |,     '
          `._                  .  \\ :       |  ::|.-\"\"\"'.|___...+-+-..  /
             `-.                \\  `:       '__.,'               _,..-)/
            .\"`-`.               \\   .       .'_....__    __..-\"' _.-'/
             \\                    \\   \\      :\"       `'\"\"  __.-\": |,\":\"`.
              \\                    \\   \\ .,\"--`.       _..-\",'   | |.\"   |
               `._                  \\    j      `\"'\"\":'  ,'      |,'     |
                  `.                 .   /           |_,'      ,-'       |
               \\`._ `.                `\"'            '       ,'          |
                .  `-.:._                           j       /          _.'
                 `.     .`.._                       |      :.......--\"\" '
                   `. '`   `.`-._                  .      .'           /
                     `:      `                    ,       \"-..._____..'
                 `\"\"\"-.--.....__                .'         _.' /  /
                 _.`--         .`,           _,'----....--'   /  /
                \"---..,.  __,--`-........,.-\"                /  /
                     /..-\"_..---\"'   _.-'                   /  j
                        --.,..    _,'                      /   |
                          .','_,-'                         '--\"
                          `\"-' ''')

    elif n_pokemon + 1 == 84:
        print('''                                  _.---.._
                                         ,'       ,.
                                        :    _    '_|
                      _,-\"'--._         :  :'|\\      :
                    .'         `.       |  `--'  .\"\".;
                    |     __     .      `.       `. '.
                    |    :_'|    :        `.    _.'`. `.
                    ,\"'. `--'    .          |\"''     `. '.
                   '  ,'        /           | |        `. `._
                 .' ,'`.   __,-\"            | |          `.  `.
               .' .'    `|\" |              j .             `.  \\
             ,' .'       |  | _   ._      .  '               `.'
           ,' ,'         '  |' `-'  `..\"',  j
         .' .'         .\"'  '          ,'  .'
         `-'         .'   `  `.      .\"  ,'  \\
                    <      `   \\      `-'     .
                     :      `  .'             ,
                    j        `\"         .-   :
                    :                  .  \"   `
                    |               .  `       '
                   `.                         7
                    ,                        '
                     '.                    .'
                       ,-.               ,'
                          '..        _.-:
                             `|\".-.-' | |
                              | |     | |
                              | |     | |
                              ' .     ' '
                             . .       , .
                               |       | |
                            :  '       | |
                   ,-\"`----\"'  .___    | |
                  '-'..--\",    ___:_`.\"'  -..____
                      _.-'_,.  ._\\_,.      _____:_\\
                    ,\"  ,'   : `    / ,-.  \\
                   ,'.,'     |  : ,' /   '  \\
                  '.-\"       `.\"\": ,'     `  `.
                               '/`.        `.\"|
                                .'           \\' ''')

    elif n_pokemon + 1 == 85:
        print('''                            .
                                   .'/   .
                                 .\" / ,\".'    _.--:'`-......___
                              , / ,-\"_,' ___.\"   ,.`-.....-\"\"
                            // //_.-'   /.._\"\"\". |_'  : `-...
                          ,/.-'`'  `.  '  '._..-.     '
                        ..','   _,   :      `.,'    .'
                      .'/-.: |,'|_   :       /\\__ ,'
                    ,'_,   _'_ \"     ;       j,| |\"`--,\\_
                   :_`.'_,\"_,+\\   ,^.`.     '/ | |      '.
          ,.------\"...,\".-\" '/`\"'`   `.`.  ,'  ` l       `.    _.---._,.-..
         '-...-\"' .\",.____./`.\"-._     `.`...   `_\\       '_.-'_,.-'       \\
                .','      :/  `-._`\"---..`.._|            : ,-\" __..--\"\"'`.-'
               +\"'        /       `\"'\"\"----.              ;,.-\"'          _|
                         /                 :_     '.   _;\"'+.,--\"'\"''\"'\"\"\"
                                           ' `-:.,' `'\"     /-..
                                               |     .-----'--..`.
                                               ;___,'           `.`.
                           _.,....---------...' ,'                `.`.
                     _.--\"',     ____,.....----\"                    `.`-._     ,
                    :-'.,-' .-._'.                                    `._ `----')
                   '._\".  .'    \"'                                       `. `.__
                  `' ',.-'                                                `.-...' ''')

    elif n_pokemon + 1 == 86:
        print('''                            _,.--\"\"\"'--._
                                   ,\"             `.         _,.--'\"\"\"\"--.._
                                  /                 `.     ,\"               `.
                                 |  ,                 \\   '                   `.
                                 '.'                   \\ /                -..   .
                                  j                     '                    \\  |
                                  |                                    .._    . |
                                  .    .       _...         _,..._        `.  :'
                                   `-./      ,'    `.      /      \"`.      |  ;
                                      '.   ,'       |     (          \\     .-'
                                        `\"'         |      \\          `-..'
                                                   /        \\
                                                 ,'          \\
                                              _,'             `.
                                          _,-'                  \\
                                        ,'                       \\
                                       /  /\\                      \\
                                      /  /  \\                      \\
                                     /  /    \\                      l
                                  _,.-\"/      '--._                 |
                                ,'      `.  '      `.               |
                              ,' _..          _      `.             |
                             ,   _  `       ,' `.      \\            |
                            .  .\".`          ...        \\           '
           _.--\"\"`--....--\"'|  |`' |       .(_) |        .         /
         ,'  _              |  `../        `.__.'        |        /
         | ,'              ,'-\"'--._,...  ______         |    _  /
         |/  _.           .  .      \\_,'\"'      `-.      '     `'..__,...----._
         ' ,'             | | \\               ,'|  \\    /                      `
          `|          _,-\"'.|  \\ .---,-._    /  |   | .' __                \"\"`-.\\
           `.     _.-'      |  .:   j    `-.j   |  /.'--'  `.           .       |
             `'\"\"'           `-''   '     ,'|   | ,'         `.          \\      |
                                 `-......'--...`-'             \\          .    ,'
                                                                `-._      |_,.'
                                                                    `\"---\"' ''')

    elif n_pokemon + 1 == 87:
        print('''                      /\\
                 _.--'  `\"-.
                ' ,.        `
              ,' '_.'        \\
             |                .
             \"..+--.,-        :
                ||'           '
                `._            `.
                   |             `._
                   |                `.._
                   |  .                 `\"--.._
                   | /   . .                   `-._
                   `/    |  .                      `.
                   /    j   |                        `.
                 ,'    '|   |                          \\
               ,' .\"  / |   |                           \\
             .' ,'  ,'  '   |                            \\
            /          '    ._                            .
            `\"\"-.          /  `-._                         .
                 `\"'-....-'       `\"--...__                |
                                           `\"-.._          |
                                                 `.        |
                                                   `.      '
              ,-._                                   .    .
             /    `-._                               |    '
            j         `-._                           |   /
            |    ___      `-.                       ,'  /
          ,'        `\"--..__ `-._                _,'  ,'
         |                  `\"--.``---........--'    /
         `                               _..-      ,'
          `.                    __...--\"' _,'    .'
           |     '\"\"'\"-----\"'`\"\"      _.-'    _,'
          /                    __,.-\"'  _. _,'
          `.    _______....--\"'      _,'_.'
            `.                   _,.'_.'
             |           ___,..-'_,-'
             `._          __..-\"'
                \"'`._...-\" ''')

    elif n_pokemon + 1 == 88:
        print('''                                        _.---.
                       __             _____  _.-'      |
             .\"\"\"--._,'  \\          .\"     \"\"          |
             '.    `.`._ /          |                 / `.
          .---'      `._|  _,....._  `.___          .`   /
         |     ...._   .`\"'    __  `\"-. ` `.     _.'___,'
         `._      `.`.'\\     ,\"  `.    `.)`.`-\"\"'_.\" .'
            |.____.,'. |   _/ .    ;__  ,   ``\"\"\"     `.
            |,-.  /    ' .\" |     ,__ `.'           . ,'
            '   `j`---'.',-\"`----'   `\"| \\ __       | |
             `.  |   `'\"'            .  \\ `._\"..__.'  .
              |  '                  /:  |\"`--',..\"     |
              |`. `.___...----.....' '  `    |  |     .'
              |-.`.__,--|          |\"   :    |  |    /(
             .   `-.___.|   ,--.,-\"|    ``.  |  |   . .'
             `          |  /       |   . `.`.`--' ,'.'  `-
              '.        | /        |   |   `.`...-,'      |
               '`-._  _/|j        /  ,.'     '---\"   _..-\"|
                `._.`\" |||       / .','            .' _..'|
                 |  `..||\\     ,'.\".-     ``.    .' .'    `.
                 |     \\`\"-..-'  :|         \\`\"\"' .'     .'.`.
                ,'      `-----.-\".'   '`._   `\"--'     .','   \\
               .               `\"      `..-'     .\"\"`-','.'   |
               |.__..        ___       .        /.'\"\"\" .'     '.
               '___.--..__.-\"_..`.    ,..___  ,'  `\"'\"'       _.'.
                 '---. `.__,\"`._`-._,' `----`'              .'  ,-'\\
              _,'  ___`--\"                      ,-'\"`..___.' .-'   |
            ,\"   ,..-.`\"._  ___..._    .\"\"..__,'.'\"\"`-......'       `._
           /    _____ `.__`\" _.-\"'       `-..--\"       _...._  _....__ `.
           | .\"'----.`._  `\"\"       ,.\"\"--._         _.....,_`\"_.----...'
           `------'\"\"`._`.      _,.--\"''\"\"--......-\"'        \"\"
                        `\"-----\" ''')

    elif n_pokemon + 1 == 89:
        print('''                             _,..-------.._
                                  _,-'              `-._
                                ,\"               .---.._`.
                               /----.       _._,.._\"\"\":\"`\"`.
                              /`--\"\"     _.'.'  / .`-.'-\"'\"`\\_
                             /\"\"-._`----\" .'  .' '   _.`     \\\"-._
                            .      `.___.'   / ,' . |   |  ._  . .``-._
                          _,' _.            .,' ,\"| |   |   .`.|'.' ,--\".
                        ,'    ||`._..____..\"' ,'--'.|   |    `.|'  .'\"-._|
                       /___...'|   :._     _,'      `'-. |     |  _,.._  |.
                      |,--.._|j  ,'   `'\"\"'         ||  `|     '.'_..._` | )
                     ,'      /  /                   ||   |    /',\"     ` '/|
                  ,-'   .,-./  /      _,..----..___,':`_'    /.'        `.' ._
                 /  __.._ `-\\.'-----\"'  _,...__      '\"     /.\"\"-..-\"\"\"-. |_  `._
            __..:--\"_.--.`.  `---....-`\"..__.\" `-...      _.\"'\"''`---..__`._`\"\"__\\
         .-'  `\"\"''\"       `..--\"\"-.   _.--.._   _.-\"\"-_,'              _.._`-._  '_
         |\"\"-.    __.-----._ '....`._-\" _,-\"'`-..._,..`__...\"\"\"-.__  _.'_.._`-..:'\"-)
          `\"\"`..-\"_...----..___)     `\"\"              `....------._\"\",-'    `..-'`\"\"
               `\"                                                  `\" ''')

    elif n_pokemon + 1 == 90:
        print('''               _,.-'\"\"\"''--..._
                    _,-'               `.\"-.._
                  .\"     _..-'\"'\"\"--._   `.   `-._
                ,'   _.-'             `._  `.     `-._
               /   .`                    `.  \\        `.
              /  .'                        `. `.        `.       _,..
            .'  /                            `. `.        `...-\"'    \\
           /   /                               _. `.               ,-'
          j   /                   ,-\"\"'`.   ,\"'  `. `.           .'
          |  .     _..------...__'  \"   |  |   \"   |  `.       ,'
          `._...-'\"_,.-\"'        `..__,\"    `._ _,.'`.  `    .'\\
            ,\"  _,'             __..-\"\"'`\"'.  ,'    `..  `.     .
          ,'  .\"        _..-''\"\"            \\/        `.   \\    '
         :         _..+'----\"'               `.         `.  \\    \\
         :      _,'    `-._                               \\  \\    \\
          `...-'           `.                              \\  \\
                             \\                              \\  \\   .
                              \\                              .     '
                             / \\                    .        '  `  :
                           ,'   \\               .    \\        \\  \\  `-,._
                         ,'    __\\               \\    \\        \\  \\  /._ `.
                        .  _.\"'   \\               \\    \\        `._'/._ \"-.\\
                         `\"        `.              `._.'        ,'.-.. `-._ `
                                     `-._                    _.'.  `,\"`-._ `.`
                                         `--...__     ___..-\"  \\ `. '     `._`|
                                                 `\"'\"\" \\   :    \\  `.`.      \"
                                                        \\  :     `   `.`.
                                                         '\":      `.__,.'
                                                           `-.....' ''')

    elif n_pokemon + 1 == 91:
        print('''                                                          _
                                                                ,\"  '
                                                              ,'   /
                                                             /    /
                                                           ,'    /
                                                         ,'     .
                                              _...      /       '
                                           ,'\"'\"\".`.   |_..    /
                                 ,-\"'\".   /       \\\\  ,'   `.\"'
                                .\"\"\"'. |,'         .`\".    /.
                               /     | |           `...`\".',___
                              /      | `.            _.-' /.___`\".
                            .'       `-._`-.._____,-'    /     \\ |
                      ,..    \\           `. . ,'.'      /       .|
                    .'   `.   \\   /        .||.'       '.`.._   ||--.
                    \\      `...`-'         ||||      .'  `-.._`.||_ |
                _,.--`\"'-..\"'              ||``. ,-\"\"\"\"`'\"--._`\"-._`-.
           _,-\"'           `.              ' .\\`'             `.   `. \\......
         ,'                 '               || .|              |`.   \\ \\   .'
         `.._____________ ,'\"`+-\"\"'*'       || ||              |  \\  `. .-'
                        |    .    _..-'    j | ||              |  |    ||
                        |    |   .         |. j |              |_'|.   ||
                        |    '    `-.._    || | |  .........      | |  ||
                        |     `._          || ' '   \\  __.-\"  _,' '.. , '
                        `._      `..       ' . `..   \"\"_,..-\"'  .'  \\/.'
                           ``.    /         \\`.  ``-._`-....\"_,'   .,'|`._
                              `..'           `.`._  `.`--\"'      .,'\\ :   `.
                               /     _.-   .    `-.:-._ ` '._    :   . `--..'
                             ,'  _,-' `.   :    __  `-.` `.._`. /,  ,','
                           .'  .'       `-. `-'\"       \\`.   ` ',  ','
                           `--' `--..     | `-._____   `._:---.| .'/
                                     \\    |     .'  \"-.____`\". |-\"'
                                      `.__|    /           `\"'\"
                                          |   /
                                          '._' ''')

    elif n_pokemon + 1 == 92:
        print('''                             _
                                   .\"' `..._
                                  '         `.
                                .'      ___..'
                          _   .\"       '   .__,-.,\"\", ,----.
               ,.-\"\"''-..\" :  :        `--'        ' :      :
             .'            :_,'                    `._`\"--. ;
             :              _,.--'\"'\"\"`--._           `.  `\"
            j             ,'               `-.      ,._.'  ,\"\".
            :           ,'                   ,-.   .   __  `..'
            `--.    .'.'                   ,'   `. :_,\"  `.
          ,.   ;   .   \\                 ,'      |         `.
         ' :  :    |    `.             ,'        |\\         `.  _
          `.   ._  |      \\         _.'          | .      ___ `\" :
                 : '     . \\      ,'  .          ' |     :   `...'
                ,'  \\       `.   .             ,'  |     '  __
               .    `.       |    \\          .'    '    .  (  `.
             .'      \\`.___,'      `-.____.-'     '     :   `-.'
              .   ,\". \\ ..___              _     /      :    .
              :   . :  \\|/\\  `\"'--------+\"|,'  ,'       `-..' :
               `-\" .'   `: `\"-.._______,.\\|  .'               '
                   `--. _ `._             _,'        ,\"\"-.__,'
                       \" :   `\"--.....--\"'     __   .
                       ,-'                 ,.-\"  `-'
                      :   ,..             .    ,\"\".
                     .'   .  :   __..._   `\"-. :   :
                     `.._  : ' ,'      `\"--..' `--\"
                         `-' `\" ''')

    elif n_pokemon + 1 == 93:
        print('''               -._                                   _.
                         \\ `-.._                           _,' |
                          \\     `-._    _,.--------.._  _.\"    '
                           \\        `--'              ``.     /
                            \\                                j    __
         __         __       \\                               |.-\"' /
          `.`-.`-.__`.`'\"----\"\\                              |    /
             `.       `.       '        ._                       /
             `..        \\               | `.               /|   /
               `.        `.             |   `._          .' |  /
                 `.  .-----`            |      `.       /   ' '\"\"''
                   `. `.            .    ._      `_    /  ,'    .'
                     `. `.           `._   `'\"\"'\"'     \"\"' ,  ,'
                       `. `.          `.`.              ,-/ ,'       _..
                         `. `.          \\|,---..  ,--\"./ / ,--------\".  \\
                           `._           `.     `/ , .`.',:           \\  \\
                              `._          `..\".,./ ' _.' :            \\  `.
                            ,-'\" `-._              _.\"     .   |.-\"`.   \\  |
                           .         `-..........-'        |   `..   \\   |_'
                           |           `\".                 `.._   .  '  ,'
                           |         |   |                     `\"'    .'
                           |   /\\    |'  '
                           '  /  \\   ||   .
                          '   \\  '   |'   ;
                           \\  '  \\   `...'
                            `\"\"   `,' ''')

    elif n_pokemon + 1 == 94:
        print('''                 |`._         |\\
                          `   `.  .    | `.    |`.
                           .    `.|`-. |   `-..'  \\           _,.-'
                           '      `-. `.           \\ /|   _,-'   /
                       .--..'        `._`           ` |.-'      /
                        \\   |                                  /
                     ,..'   '                                 /
                     `.                                      /
                     _`.---                                 /
                 _,-'               `.                 ,-  /\"-._
               ,\"                   | `.             ,'|   `    `.
             .'                     |   `.         .'  |    .     `.
           ,'                       '   ()`.     ,'()  '    |       `.
         '-.                    |`.  `.....-'    -----' _   |         .
          / ,   ________..'     '  `-._              _.'/   |         :
          ` '-\"\" _,.--\"'         \\   | `\"+--......-+' //   j `\"--.. , '
             `.'\"    .'           `. |   |     |   / //    .       ` '
               `.   /               `'   |    j   /,.'     '
                 \\ /                  `-.|_   |_.-'       /\\
                  /                        `\"\"          .'  \\
                 j                                           .
                 |                                 _,        |
                 |             ,^._            _.-\"          '
                 |          _.'    `'\"\"`----`\"'   `._       '
                 j__     _,'                         `-.'-.\"`
                   ',-.,' ''')

    elif n_pokemon + 1 == 95:
        print('''                                                       _
                                                ___            | |
                                            .-\"'   `...._      | |
                               _,--\"'-.   ,' .           `.    | |
                             .'       ,`,'    \\            `.  | |
                           ,'.      .','       \\            | j  |
                    __,..,'   `----\"  `         \\       _..-+.`  |..
                 ,'\"     .             '._  ___...-._ ,'     |   |  `--.
                /       _|              | `\"        .'       |   |      `.
               /`  _.-`'  ._..----\"\"`._ |         ,'         |   |        .
              | .-\"         `-._    _,.' `.     .'          j    |         `.
           ,-\"\"\"--..._       |  '`\"\"       `-../\\     _,\"''\"|    |.._       ,|
          /    '.     `\"----,'                 ` '._,'      |   j    `.   .' |
         /_.-'\"  `-.___..-.\"                    \\ ,'   \\    |   '    | `.'   '
         `                |                    _.'          |  |,_   '   `. /
          .        _______|                 .-'    |.       `. '           |
           `...---\"     .-'               .'       | `.                 ,  '
           ,'._     _,-\"                  `        |  ,`.  ,  .    _.-'|    `.
          .    `\"\"-'    `.                 \\       `.....`.     .-',   |      .
          |             _,|                 ._ --.        |     '\"--...       '
           `.--\"`.....-\" ,                    /\".`        |   |        _____,'
             .       | .'_                   /   \\        |  j       \"'_,..'
              /`-...-+\"   `.                 '   .'.__ -..'  |_,..   ,'  |
             '          ____.                 \\  |    \"`-..___,....-.    '
              .     _.\"\"'   |                  `. .                 / .-'
               `. .'       .._                   \\ \\               / /
                 `-._   _.'   `.                  \\.--......____ .' /
                   .'`\"\"    .'  .                  .            '_.'
                   |       /    |____               `\"._     _,-\"      ,-'\"'
                    `. _.,'     |    `.                 `--\"'       _.--,.'
                      `'--.__,.\"       |                          ,' .' |
                            |   ,.._   |\"--._                  ,-+-.'  /
                            `..'    ``.'   ,.`.     _..__.-\"\"\"-.__.'\\\"'
                              `----.,\"    '   .--..'   _..`-../:  _,'
                                    .    /  .'  _.'\\.-\"  |     '-\"
                                     \"--+--\"`..'   |.   ,^.__,'
                                              `---\"  `-\" ''')

    elif n_pokemon + 1 == 96:
        print('''                        .\"'`-._,........_.------..
                                / _.-'          ,' ,---\"\"/
                               /.'                /   ,.'
                             .'                      `-.
                           ,'                           `.
                          /          _..                  \\
                 ______,..         .',\"\"\"\"\\)               `.
            .\"\"\"\"        |.-----           -                 \\
           /.' .   _     |______                              \\
         .'/   | ,'      '        _.....-         _,---.       \\
          \\  ,\"'/-._      \\----  /-..____.   _,.-\"              .
           `.|      `\"-.._ \\____/        ,---..._               '
                          `            .' .      `.              \\
                           |           |  |  |  |/       ,        .
                           |           './|  |`.'.._   .'         |
                           |               `.'      `\"\"           |
                           |--.      ___       _,...    _.'\"`-...'|
                         ,/    `---\"'   `-....'     `--\"          |
                       .'.                         _...           |
                      /  |                      ,-'               |
                     /   |                    ,'                 j
                    .     \\                  /                   |
                    |      \\                .                    |
                    '       `               |                    |
                     `.      `._            '                    '
                       `.       `._          \\                  /
                     ,.\".          `.-........'.               /
                   ,.-'  `.____....-'           `.            '
                   '...--\"'                       )           `.
                                                .',.-,----.    |
                                                `.  |      \\_.'
                                                  `-+----\"\"' ''')

    elif n_pokemon + 1 == 97:
        print('''                  .\\
                          .  \\
                              \\              _,|
                         j    _\\____      _.\" ||
                         |  -'      `\"-.-',---.|_
                        /                /j      `.
                       /                . |    |   `.
                      ,                 | |    |     \\
                     /|.                ' `    |  / ,'|
                   ,' |\\`.               `.`.__|_/.',`
                  :   | `|      ,.--..     ||\\   '\"   `.
                 .'   | /      |`'-\"\"'     '| \\         `.
                 )    `j       `.         / |  \\          .
                ,`-'   |       .'        /  | `.\\         |
               / |   _ |     ,'       _,'  _|_ | \\        '
           _,-'  `. /  \\   ,'......--'   .\" _ `.  `      /
         .\" ---._ ,'|   --`              | . `. |------\"'
         |       |  '    .       .       `.`-' .'
         |       |   `.  |        |      _/:--'
         |       |    \\`-|        | _..-'  |
         |       |  _,.\\  `\"--..-\"'`      ,^.
         |       `.'    `                    `-.
         `         `\"-.                         `.
          \\       .---'                           \\
           \\\\\\  . `.         __....._              \\
            \\\\\\__\\__'    _,-'        `-.            .
            |          ,+             .'`.         .'
            '.     _.-'  \\            '            \\
           ,-\"`-...     ,'             \\     _ '\"-. `.
          / ,'   .-    /                `.    `.   \\.'
          \\_|  .'    ,'                   `-...'--\"
            `--'---'\" ''')

    elif n_pokemon + 1 == 98:
        print('''            ,-\"'\"'\"--.                       ,-\"\"\"\"'`-.
                    '          `.                   /           \\
                   '             \\                 ' __          \\
                  /       .+\"\"`'`-                `-'  `\",        \\
                 /       , |                             |\\        .
                .       .  |          ,.    ,-.       .  | .       |
                '       |  |.\".       | .   | |      ' `.| |       |
                 \\      |_.'  '      .' .  .  |       `  `.|       '
                 .    _,'    /    ,\"\"-. `-.' ,-\"\"-.    |    `.    .
                 j-..'      / ,-.'  .  \\    |  .   .--.'      `...'.
                 | `-`._.--'.'  `._     |   |   __.'   \\`--...'-'  |
                 `....'     | /\\___`'--'     `\"\"_....\"\\ \\     `...'
                  | |-\"-._,`.'     `\"-._     _.\"       \\|\". ,^.|  |
                  | `..,\"_,'            `---'           \\  `-..'  |
                  `._|_.\\ `._____                 _...__.`._,_' _.|
                  /  '`-.`-._|.  `-._           ,\"     .','_,\"'`\\ \\
                 ' .'    `-._`.`.    `.       ,'     ,' _.'      . `
           ____.'  |         `\"  `\"---+------'-----\" `\"'         |  `.____
         ,'_,.-`._,'                                             '.--...._`
         `\".--..__'                                               `._.---`\"` ''')

    elif n_pokemon + 1 == 99:
        print('''                                 _,.._
                                     _,-'\"     `.
                                _,.-'            `._
                              .'                    `-._
                             .       /                  `-.
                             |      /                      |
                             |   _,'                       |
           ,'\"\"'\"`-._        |`\"\"                          |
          /          `-.     |       _,....._              |
         /...._         .    '    ,-'| | |`-.`.            '
              ``.       '  _  `./\\`\\ | | | | `.`.   _,.---- `.
           ,.  | .       \\ ``.    ._\\|_| | | / \\ \\._          `.
           | `.| |        . `.`.  |\\   `-'.|/_,.-\"  `          |
           \\    `._       |   `.`-' `.              |         ,'
            \\      `.   ,'     _\\,.'\"\"`.            |        .\\
             `.     |  /   ||.'./ /.   |`.          |       / |
               `-._.'_.    |||,' ._...-' .`-.._____.'    _,' .'
                   \\\" |   ,'|'   _ _   ,'   | .-\". `-..-'  ,|
                    . |   \\  `..' \" `-'     '/|   `._`\".    |.
                    | `:\"-'`.                `+.._   `\"|    .'
                    `._|_,\".\"`.   ........_   ,\"  `-._ '.    )|
                           ' /.`-._        `\"'...-\"_.'`._\\_,' '
                       __.' j  /`..`..__      _.:-'    | |  \\  \\
                     ,__/   |-`.,'      `\"`'\"\"         | |   \\  \\
                        `--\"'-.'                       |  \\   .  `___
                                                       `./\"\"\"-`./\"'__`
                                                         `..--.|`-'  `' ''')

    elif n_pokemon + 1 == 100:
        print('''                         __...--------...__
                             _.--'                  `\"-..
                         _.-'                  ,.        `-._
                      _,'                    .'  \\           `._
                    ,\"                     ,'     .             `.
                  ,'                      /        `.             `.
                 /                       .           \\              `.
               ,'                         `.._        .               .
              /                               `-._    /`               \\
             /                                    `-._  \\               \\
            /    __,........----...__                 `\"-'               \\
           /.--\"\"                    `'--.._                 ...........
          j                                 `\"-._            `. /      |  `
          '                                      `._           `.      .   .
         .                                          `._          `.    '   |
         |                                             `.          \\  /    |
         |                                               `.         `'     |
         |                                                 `.              |
         |                                                   `.            |
         '                                                     `.          |
          .                                                      .         |
                                                                  \\        '
           '                                                       \\      '
            .                                                       \\    /
             \\       ____                                            .  /
              \\    .\"    `\"\"-._                                       '/
               `   '           `-.                                   ,'
                `.  `.            `.                               ,'
                  `.  .             `.                           .'
                    `._`-.            \\                        .'
                       `._`._          '                    _,'
                          `._`\"-._     |                 _.\"
                              \"-.._`--'           __,.-\"'
                                   `\"\"----------\"' ''')

    elif n_pokemon + 1 == 101:
        print('''
                                  _,.--\"'\"\"\"''\"\"\"''--..__
                             _.-\"'                       `-._
                          _.'                                `-._
                       _,'                     ._                `.
                     ,'                          `._               `.
                   .'                               `._              `.
                  /                                    `.              \\
                ,'                             .         `.    |        `.
               /                               |           `.  |   |      .
              /                                |             \\ |   |       \\
             /                                                `    | ,.-\"'  \\
            /                                                                \\
           j                                                        |         .
           |                  __...--'\"''\"\"'\"'\"\"\"'`--..__           |         '
          j             _.--\"'                           `-.._                 .
          |         _,-'                      .\"\"'`--..__     `\"-._            |
          |     _.-'                          |          `\"-._     `._         |
          |  _.'                              |               `-._    `._      |
          |,'                                 |    |              `-._   `.    |
          |                                   |    |                  `-.  `._ |
          |                                   '    |     |               `.   `'
          |                                    `\"--'.....+................'   j
          '                                                                   |
           .                                                                  '
            .                                                                /
             `                                                              /
              '                                                           ,'
               `.                                                        .
                 .                                                      /
                  `.                                                  ,'
                    `.                                              .'
                      `._                                        _.'
                         `._                                 _.-'
                            `-._                         _,-\"
                                `\"--..__           __..-'
                                        `\"\"\"''\"'\"\"\" ''')

    elif n_pokemon + 1 == 102:
        print('''                       __.__._
                              .\"   ) `.`\".
                             /     `.../  \\
                            |   _.'   \\    .
                            |  '       `.  |
                            '            `.'
                             \\          _,..---..._
                  _,.._       `._     ,'           |.
               ,\"\\  `. `\".       `\"\".'             | `.
              /   \\ _|_  _\\       .'               |   `.
            ,'     `...' `.\\    ,'                 |     \\         _......_
           .        ,' ___. .  /                  j    _,'\\      .'   |    `.
           |       .        | /                   |.--\"    \\    /     |      /.
           |       |        |.                    |            /      |     /  \\
           '       |        '                     '         ' j       |`  .'    .
            `.  ,`.|       /|     `.                         .|`-._   .--,      |
              `/   |    _.' |      |`._             _,       || `--` '--'       '
                `\"-+---\"    |      `   `-._     _.-'  |      | .   ----        /
               _.......__   |       `.....'   -.______'      |  \\            ,'
             ,'         `\"--|_            ____               '   `-._    __.'
            /                 |.         -....-\"            /        `\"\"\"
           /         '   -._  | `.                         /
          /         / \\     `.|   \\                      .'
         .         / .'       '._  \\                   ,'
         |        /.\"            '--._                .__..._
         '  .....,               |  | `-.._     __..-\"\"      `\".
          . |  .'  _.-           |  |      `'\"\"'.\"              `.
          `. `\" .-'              |  '          /                  \\
            .                    ' .          /                    .
             `.                .' /          |                     |
               `.              |.'           |                     |
                 `-._       _,-'             `.     '-.        _,- '
                     \"'---\"'                   \\     `..`.  ....' /
                                                \\                /
                                                 `._   --==-. _,'
                                                    `---...--' ''')

    elif n_pokemon + 1 == 103:
        print('''
                                       .'
                                       | \\
                                       |  .
                       '._             |   .
                       `. `._          |   |        .             __...
                         `.  `.        |   '      .'        _,.-\"'_.'
                           .   `.      |    .    / '    _,-'   _,'
                            `.   `.    |        / /  _,\"    _,\"
                    `+.._     `    `.  '     . / / .\"     ,\"
                       `._`-._ `.    `. .    |/ /,'     .'
             _,..---\"\"\"\"--`.  `-.`.    \\|    | ./     ,'  _,.---,________
          -`=..__                `-.    |    |.'    .'_..+---\"\"\"         `\"-..
                 `\"\"---..___        `.  |    |'   .'-\"          ___,.....---\"\"`'
                        _,.-\"\"__,.._  `   ___'  .'  ____..---\"\"'
                  _,.-\"\"    .'  ,.  \\ .-\"'   `-.  \"\"-------...__
               .-\"    __.-.'   '-\"'  / -='   `\"'\\......__       `\"-..._
             .\" _,.--\"\"  / .\"\"\"|    /            \\  _  ..`.-.....______`_
            '.-' .'_.-\"\".  | _.|   .   `.-----\"'  .'\"  __  `             '
                -\"'     '  |'  |   |              | '\"\"     .
                         \\  ...'   |              '         |`-.
                          `._      ,.            /          '\"--'
                             `\"\"\".'  `._     _,\"`.       _,'
                                /.....__`\"\"\"'     \\--..-\"
                               /        `'\"\"'----...
                         .    /____                |
                        | |  j----.`\"\"---..__      |
                  '`-.,-`.'--|`-.  `.        `'\"--.|
                   `./   ___ `.  .  |              '
                    ' ,\"'   `. . |  |             /
                    . |      | | | .'          .'j
                     \\`.     | '-'`..._____..-'  |
                      `.`.__.'/     ,'`._       ,'
                        `\"--`'     . \\   `-.__ /
                                   |  `...___.'
                                   /\"`__.._'\".
                                   `\"'     `\" ''')

    elif n_pokemon + 1 == 104:
        print('''                                             ..
                                                    .'  |
                                                    |   '
                                                    '    \\
                                                   /      `-._
                                           _...--\"'           `\"-._
                                         ,'                        `-.______
                                        j                                   |
                                        |                                  ,'
                                        |           _                    ,'
                                       /          ,':\"\"\"\"\"-.           .'
                                      .___..  __,'\"       `.`.         |
                                        |       ||        `.\\ .        |
                                      ,'|      _||  `-._   | ||        |
                           .\"`-------'  `-..,-\" ||...._()`-  '|        '
                           `.               \\.-\"       `.__,','       /
                             \\            .\"            |_.-'        .
                              /                    _...-'            |
                             /                   .'.                 |
                           ,'                  .'   |        __      '
                          ,                  ,'     |      .'  `      `.
                         /                  '       |___   |   /    .--'
                        .        ____                 | `. `..'   ,'
                        |            `\"-.             |   \\     .'
                     _,\"j'               `.           |    `--+\"-._
                   ,\"  /                   \\          |       |    `.
                _,'   .                     .         |       '.     `.  _,.
              ,\"      |                     |         '      /  |    ,\"._  '
           _,'        |_,...._              |       ,'      /__.'  ,'    `/
         ,'           |   _.' `\".          .     _,'\"--.._,'     .'      /
         `._          `--'       \\        /_,.-\"'  __,.-'       '      ,'
            `\"'\"\"------`.        .\"`----\"\"     _.-\"..__________      ,'
                         `._     |          ,-'                `\"--'\"
                            `-..-`._       /
                                    `.   ,'
                                      `\"' ''')

    elif n_pokemon + 1 == 105:
        print('''      ,.                           __     ,\"`.
              / |                      _.-\"'  `\"--'   |
             /  |              .\"--..,'               |
            j   |              `                      |
            '    `-.            `.                    |
           .       .'            '                    |
           |    ,-\"               .                   '
           |     \\                |                    ,\"\"`.
           |      \\               |                   ||    `
           |       \\             j     `-.           .||     `.
           |        \\            |       |`.         |||      |
           |         \\         __|       |  |`.      |'|\\   .'
           |          `.  _.-\"'   `-.._  `._'  `.    | | `-\"
           |          _,+\"             `.   `\"\"--\\     |
           '        .'                   `.            |
           '      ,'                      |`.       .  '
            \\   .'                        `. `.     , /
             \\,'             _,.-+\"\"'.      `  `.   .'
             /            .-'     `-. '      `.  `\"'
           ,'           ,'\\          `.`.      `
          '            /.  `.         ,\\ \\      `._
         .            /  \\   `._    .'  \\ .        `\".
         |           /._  `-._  `,-'    ,' `.         \\
         |          /   `\"-+---\"'      |    |         ,-.._
         |..____,.-'       |`.         '   ,'         |    `\"-._        __
         `---'\"            |  \\         `.'  `-.._   ,|      `._`\"-._.\"'  `.
                           |`._`.        |        `.  `-._      \"-          .
                            `.,' `.___..'           `\"    `._                |
                                                             `.              |
                                                               `._         .'
                                                                  `        |
                                                                   .       |
                                                                    \\      |
                                                                     `..,.' ''')

    elif n_pokemon + 1 == 106:
        print('''                                                   __           ,-\"\".
                                                          .'  `.       ,'     .
                                                     _____|     \\    ,'       |
                                               _,-'\"\"     |      `..'     _,-'
                                             ,\"           `.            ,'
                                            /       /|   ,\"'`,        ,'
                        _,..__             /      ,'.|  .  .',`.     `.
                     .\"'      `'--\"\"-._  .'     .' ,'/  |  | |' |      `.
                 __.'             `.   `.       |`'.'      ` '.`|        `
            .-\"\"'   |               `\"-.' ,\"`.  '-'         `---'.        \\
           `-.      '             ____   '.`\"\"/               .'  `\"-.     .
              `-.__/            ,'    `\".  `./._              |       '    |
                _,.            j        |   |  |`\"-._         '      .     '
          _,.-\"'   \\           |        |   |  |   | `+-.\"\"-.  .     |    .
         '._       |           |        |   '  |   '  |  |.    |     `..-'
            `\"-....'           `.      ,'  '  ,'  ,   |  ' .   '
                  .._            `-...'  ,'--+---+--.'_.'  |  .
                .'   `                _.'      `.     `-..'  /
              ,'     _\\         __..-\",'         `     \\    /
              \"'`\"'\"'  `\"----'\"\"/.-+\"             `     `  /
                             ,-'---|               \\      .
                            /      |                `.__..'
                          .'    .' `.                \\    /.
                        ,'  ,..\" ..  `.               \\-\"'  \\
                        '._'  |  | `-.'                \\  _,`.
                              |  '                      \\'   /.
                              `.  )                      . ,'  '+-._
                                `'                        `. .' ||.\"`.
                                                            `._,'||   |
                                                             |._,' `-.|
                                                             `.       |
                                                              '       |
                                                               .__ _ .|
                                                                | | | |
                                                                '.`.'.' ''')

    elif n_pokemon + 1 == 107:
        print('''                                            __
                                                   ,'  `\".
                                             _    /      '
                                         .-\"' | ,'      /
                                      ,.j     |/       /   _,\".
                                    ,' ||     |       j _,\"    `.
                                   |   ||             '\"      .'
                                   |    |                   ,\"
                                   |                      .' _..-.
                    _______        |   \\                  `'\"     \\
               _,-\"'       `-._    |  | \\                      _.\"
             .'                `.  |  | b`       _..+-      _,'  ___......
            ,                    \\ `. `-     -'\"d   |   _,.---'\"\"         |
          ,.                      \\  `.----.._  ---'_.-'                  |
         | |                       ',-\"`._    `-.,-'                    .'
         `.|                       |      `\"---.'  _..,.-\"\"\"\".      _.-'
           `.                      |\\        ,'. .\"    |    __...-\"'
             `.                   ,'/`\"-.__,'  ,'    __|.-'\"    /
               `-._            _,\\.'         `.  _,-\"\\`-._____,'._
                   `\"-...----'\"   \\---...____.'\"\"_.'  `-..,'   `  `-.
                                   `\"'\"`\\   `._.'     .' /      '    \\
                                         `._,'      ,'  /       |     \\
                                             `\"-.  .   /        |      \\
                                           ,'   ,'\"'`-+...-'\"\"'/__..--\"'
                                       _,.'   .'        |     /
                                     ,\"     ,'          |    .
                                   ,'      .            |    '.__
                                 .'      .'             `.       `.
                              _.'|    _,'                 `.       `.
                            .\"   `-..'7                     `.       `.
                          .'         /                        \\        \\
                          |        .'                          \\        ,\".
                          `--....-\"                          ..-`'\"\"`--'   \\
                                                            /              '
                                                            `._      _...-'
                                                               `\"--\"' ''')

    elif n_pokemon + 1 == 108:
        print('''             _____                       ,\".
                 _.-\"'     ``.                  .'   `
               ,'             .               ,'      |
             .'               |            _,'        |
           ,'                 '          ,'           |
          ,               / ,'         .'             '---.._
          '              /.'         ,'              /       `-.
         .              ,\"          /               '           `.
         |      |      .           .                              \\
         |      |      |           |                               \\
         |      |      |           |                                .
         |      |      |           `
         '      |      |            `.             _,.._             .
          \\     |      '    __...._   `.__     _,-'     \"-.          |
           \\    '      ' ,\"'       ``./   `'\"\"'            `.        |
            \\    .      '.       ___  `.                     \\       '
             \\    \\      \\       ,..`                         \\     /
              `.   \\      \\     ( \" )          ,......--'\"\"`.  \\   /
                .   \\      \\     `\"'                   ,\".   |  `.'
             ,..|`.  \\      `.                         `\"'   |    \\
            |    . `.-`\"''\"\"\"`--._                        _.'      \\
            ,\".   `.|             `-..    /`. .._      _,\"          \\
            `\"'._   '                   ,'  | |  `\"+\"\"' ,-'\"\"''-.    .
                 `\"--`._             _.\"    | |   |    .  ,...   .   |
                       |`+..____,..-'       ' |   |    | .    |  |   |
                       |/  ,..\\           ,'  '   |    | `.__,'  |  ,'
                       '  |   |`.___   _.'   /    `.   `._     _.' ,-.
                        \\ `--'   /._'\"\"   _,'     .'`._   `\"--\"  .'   `.
                         `-..,.-'   `---\"'     _,'_,.--`\".___,.-'      |
                            /-----\"'   ,`\"\"''\"\"           |   _....._ .'
                           ,-'\"\"--._,-'                   '.\"'      .\"
                            -..---'                         `\"-----' ''')

    elif n_pokemon + 1 == 109:
        print('''                               ,----.
                                       '      |
                                      /       '
                                __,..'         \"-._        _
                           _.-\"\"                   `-.   ,\" `\".
                  ,-._  _.'                           `\"'      '
                ,'    `\"                                       |
               .                                               .
                `.          _.--..               ____          '
                /         ,'    . `           ,\"' .  `.         `.
               /         .         |         /         \\          \\
              /          `------...'        ._____      .          \\
             .                                    `'\"\"\"'            \\
             '                    ________                           .
            j           `.\"\"/'\"\"\"`        '\"\"\"'\"'--....,-            |
            |             `/.                      ,\\ /              `.
            |                `-._               _.'  '                 `-.
            |                    `\"-----------\"'                         |
          .\"                         ____                                |
         |                      ,-\"\"'    `\".                            ,'
         |                     .   .----.   `.                        .\"
         `.._                  |  '.____,'   |                        '
             |             ,\". `.           ,' _                     /
             '            '   `._`.'._\".__,' .' .                   /
              .            `'-._ `._     _.-'  _.'                 /
               `.               `.  `--'\" _,.-'                    `
                 .               ,'     .\"                          '
                  '        .-..-' _,.--._`\"-..,-.                 ,'
                 /         \\    ,'       `-.    |           .-'\"-\"
                 \\          `-.'            `..'         _,'
                  `.,.-\"`._                           ,-'
                           `\"-.                       |
                               \\       ,..----.     _.'
                                `\"\"---\"        `..-\" ''')

    elif n_pokemon + 1 == 110:
        print('''                  __....____,'  `-.
                  ,\"\"-..-'\"          \"-    |       ..      _.._
                  |        _, .,           '._    /  `'\"\"\"'    |
                 .'         _____             `.,'     ____     `.
              _,\" _.'      \\  |  '\"--..        '       \\__ `\"-.   `.
             | ,'\"|/        `-.______,'      `     ' |\\_  `'\"\"'  .  \\
             .'---'      _____             . '   `   |,'\"\"\"-._  ' \\  .
            /   __..--\"\"|___/ \"-.._/|         ,'       ___    `. \\ \\ '_
           . .'...-----'\"\"----.._.' |-.      |        | ,.`\".   \\ `'   |
           | `\"                  \"-.'-'      `.        \\`._`.\\   |.  .-'
         .\"        _..._                 .              `._  ,   `.' |
          `.    ,\"'_....`\".               |                \"\"       .
           |    | |     | |             -'   `,                    /
           `,.  `._`---'_,'  ,-.    '        ' `-.             _   |
           ,\\ `._  |___|  _,'  |  `    \\        . /-.__     _.' `-\"
           \\ `.._`-._ _.-'_,.--'        |        `.    |  ,'
            `-\"\\ `-. ' ,'_         `-..'       .-'    /  /
                `._.---._ `\"----.        .   ,'.   _.'  /
                  `.     `'-.._/       -\" ,-\" `.`-'      `.
                    `.,       .-\"    _    |     | .     ) |
                      '._  ,\"`----\"\"`.    |     ' `'       .
                         \"\"           `--'       \\`      ,\"'
                                                  `-._,-' 







         ''')

    elif n_pokemon + 1 == 111:
        print('''
                                                 '\"-.
                                                //   .
                                     .,.       '/    `
                                    |   \\     /.      \\        ,.
                                    |    `.  / '       \\     ,' |
                                   .|      `\"-'         \\  ,'   |
                                   ||                    \\'     '
                            ,--.   ||             _,.     `\"-.   `.
                         __.  ,.`.j '    _.-'\"\"','  |__ ..    |    `.
                        .  |  |/  `.   ,'    .'     ' .'  `. ,_...   \\
                        '  '        \\-+.._,.'      .,'      `    .'   .
                       .  /      '  |     .-'      /           ./     |
                      /  /     .'   |             .'         ,'_|,..   .
                     /  '     /     '             |        _.-\"   .'   |
                    /  '    .' _.'   `.        __ |    _,-'      /      .
                   / ,'    / .'        `.    ,'. ||_,-'         /       |
                  /,'     /.'           `._,',\"  '|           ,'        '
                ,+'      .'            .'\".'    / '          .           .
               |         '           .','      |,`.         j            |
         .\"\"'--+--     .'           | /        '   .        |            |
          \\          ,_|             \\'         `._|        |            '
           `._     .'    ______      .+---.        `--..    |             .
              `. ,'   _.\" |    `-. ,'      `.          |    |             |
               |    .' /\\ |    ,' /         |        ,'     '.            |
                `--'  /,'\"    /  /          |      ,'        /            |
                     /.     .' .'           |    ,:    ___  /             |
                    . |    /  /.  ,---.    j    /. `..'   \"           ,-. |
                    | |  .'  / |.'     `.  |   / ,\"-..__,...--._     /   \\|
                    |`-\"' _.' .'|      . .' `-'.'        /     |`..-'     |
                    `..-\"'--\"/  |    .'| |    '_.-. _.--'     .'.    /\\   |
                             ..-'----' |,          '          |.`._ . | _,'
                                      `                       '    `| ,'
                                                                     \" ''')

    elif n_pokemon + 1 == 112:
        print('''            ,\".
                     |--\\
                     | .'\\   |.
                     |'  _\\  |' ,.
                     |,.._ \\_| `.|    .-\"|
                   .'      .--   `. ,',\" '
                  '_..._   ..|`    \\ '  /
                  `     `.       .  /  /
                   .     ``.     ,' `./
                   |      `|`.   `-._ `\"\"\".
                   '       |.'`.     '   '
                    \\           \\  .'     `__,..
                     `.                ,.-'    '
                 _..-' `.     _.'   \"-.|      /
             _.-'    |  ,`\"'\"\"   _       `.  .-..
           ,\"   |    | .       .'  `     | `.  /  _,..
          |     '    ' |      /     |    |   `.`'\"   '                _,..__
         .'.     `.__..| |\\  /      '    |     \\    /             _,'\\    _.'
         |,'     ,' _..|.-'\".            |      \\  .            .'.   \\,-'
          \\\",  .'  ,`-.      `.          |       \\ `\".       _,'   \\ .'
           `\"\"'    ` ._\\      |   _,.'   '        \\ /___,.--\"`.    .'
                   .`         |,-\"     .+       _  V    `.     \\  /
                    `-._    _,' `\"-...' ,\\ .\"    `.|      .     \\'
                       ,`.            .'  /        `.     |    /
                     ,'   \\\"--.....-\"'   .        .  \\    |  ,'
                    .    .\"\\           _,|        |   .   |.'
                    |  ,'   `-.____..-\"  |        '   |_..'
                    | |       /`._      _|         \\  |
                   ,. .       \\   `-.-'\"  .         \\ |
                 .' |,-`     _/       `'\"\"-`.        `.
                -'\".'  \\_,-\"\"                |.     .. |
                  ''\"'\"\"                     ' |  ,'  \\|
                                            | .'..|    |
                                            '\"     `... ''')

    elif n_pokemon + 1 == 113:
        print('''
                             _,.-''\"\"\"`-._
                           ,\"             `._
                         ,'   ..     .       `.
                       .'     ||     ||        `._
            ,.....---'\"                         `._`-..._
            `._  _,.-\"/        `\"--'         `  `. `._   `\"'-.
           __..-'   ,' /                      \\   `.  `-.__.-'
         `._    __,'  ,                        `.   `.    \"--.
            `\"'.'   .'       _,.+..              `.   `.-...-'
             ,'  _,'     _.-\"   A  `-._            `._  `-.
             `\"+'       '     ,' `     `-             \"''-'
               '            ,' ___`.                   |
              .            ' .`   `.`.                 |  _,.
              |            ,'       `                  |,\" ,'
              |           /          \\                 |  /
              |          j            '                | /
              '          |'`\"\"''\"`'\"\"\"|                |/
               .         `            '               ,'
                `.        \\          /              ,'
                  `._      `._     ,'             .'
                     `._      `\"\"\"'             .'
                   _,'  `-.....___________...-'`-.
                  `...---'               `--.....-' ''')

    elif n_pokemon + 1 == 114:
        print('''                      _____         ____
                            ,\"'     `.   ,-\"'    `\".     ,.
                           .  ,---.   |,'   _...    .    | `.
                      _.---'`'\"-._ |  /   .'.---`.  '    '  |
                    ,'            `| /...-._____ |  |`\".'   |
                   /    _,---+-.   ,'       `-. ||  '   `..-.._
                  .   ,`._    `.`,'.   _...    \\` .  `.   `.   `-.
                  |_,.-...`---\"'|  ,`.|  .\"`    \\`.`.  `.   \\     \\
          ,      ,'             |  |  |  |  \\    \\ `.`._ `.  \\`.   .
         | \\    '     __......-\"|  |  |  |`._\\    '. `\"-`. .  . \\,\"'-._
         |  `\"'|   .\"'   ___    |  |  '  `-...\\...|_`.._ | |..:-'      `.
          `-..-|  .    .\"  _`+.,'  |   `._          `-.,'  |     ,+\"|`. |
          ,'  ,|  |  ,' ,\"'     __,'      `'\"\"\"\"'`-.   .  ,'...-' | | | |
         .   / `  |  | .   ,-'\"'             ____   `. |-'-.| |   ',' `'
         |  |   \\ |  | | .'   ,-'\"\"'-.    ,'\"    `.  | |.   | |__     ,.
         '  `.   `|  ' | |  .'        \\  .         | | `.`. '  . `\"-.' |
          \\ |\\`-..|   .`.|  |    ()    | |   ()    ' `._ ,.' \\  `---' ,
           `| `--\"    | |   '          ' '        .    .' |   |.____,' \\
            `.       ,' '    `.     _,'   `. ___.'_..,'   |   |  | `.   .
              `-...-' .' _...  `---\" _....._  _.'\"    `..'|   |  |  |   |
             ,'    _.\" ,'    |    .-' ___   `'   _..    `/|   |`.|  |   '
            '    ,'/  /   _,.'  ,' .-'   `\".  \\,'   `.   | .  `  .  '  /
           .   ,` ' .'   '    |/  /   ____/ \\  . ,-\"'|   '-.`.__,',' ,'
           |   | |  ||  |`-..\"/  /`.'\"   /   . |'  _,'  /.  `. .\"' .'`..__,.
           `   `.|_..'  `._  /  /   `._ /   /| | ,'/   /  \\   \\  ,\"._    _,'
           ,`.        \\    `-._/ `.    `-.,' | |. /  ,'   /.   \\'  __`--\"
           |  |-..,.\"| `-._    `.  `,      \",  '-j  .   ,',`.   `\"'  '
           |  |   `. `-../ `-.   `.' `\"+-..' .'  |  |_,'.\"| |`.   _,'
           '   `-._ `._.'   / `.  | _,'  |\"'|`-..|  |   | | |  `\"\"
            `._    `\"'   _.|__.-| |\" `---|  '.   |  '.,'  `.'
               `-.....-\"'  |___,  '       `. \\`+-`.   `.
                      .'   '  /  /          \"'/    `\"--'-._
                    _,:  ,'   `-\".           .             `._
                 ,-'   `\"         |          |                `.
               ,'                 |          '                  `.
              /                 _,'           `._                |
             |               _,\"                 `-..__        _,'
             `.        __..-'                          `\"\"\"`\"''
               `-----\"' ''')

    elif n_pokemon + 1 == 115:
        print('''                               |`.
                                        |  \\
                                   __   |   `.
                                 _|  \\  |     .
                               .' \\`-.. `     | _____
                               ,`-`  `.| \\   ,\"'     `-.     ______
                              |        |  \\.'           `.,\"'      `\",'
                              `.     __| ,'|             |        _.'
                               '    .  :/  |             |......-'
                              j      `./  .'\\            | |
                             ||      ,/   ' \"'         ,'  |
                             ||     . `.   `.|       .'|   |
                             '+     `.  `.   '     ,|__'   '
                              `    .'    \\`.  `\"-.'      .'_
                               \\   `   ,  `.`.    _..-|     `---....-\"-._
                                \\ . `.' _..---`.._..-\"|   |              `,
                                 /    .'          `.  |  ,` ._           /|
                               .'    /              \\ `-|     |        ,'|'
                              '/    /                .  '    .' ,-----'\"\"'
                         _ ,.-'    /       _.._      |   \\.-'--'
                       .\"         /   ,..\"'`\\/ `     |   |
                      /|         j  _,`/    _| \"`.   |   |\\
                     j `-.       |,' `.    |.|    .  |   .|
                     |    |    . |     `._.`-|`.  |  |    '
                     |    |  _ ` |       `..'\"`\"\"' \\ '     `.
                  _.-'\"\"\"\"' | `\"\\`                  .       |.
               ,-'|   .\"`.  `.   \\`.                '      j  .
             _'_..'   |   :-.--.' `.`._           ,'       |  |
           .'          `+'_  `.|      _`.._____,-' ,\"`.    `._/
          /         _____  `-.__..--\"\"         `-.'    \\     |
         .    _,.-\"'     ``\"\"'                    `-..-\"  ___/\\
         '.,-'                                      .',-.'   |'
                                                    ,'   `.  |
                                                           `\" ''')

    elif n_pokemon + 1 == 116:
        print('''                          _,..----.._
          ,\"''-.               _.-'           `\"-._
         .,-.   `._          ,'    ,---.           `.             _,..
         ||  \\     `._     ,'    .' |   .            `.     _,.-\"' _,'
         ||   .       `-._.      |.'|   |            _...-\"'    _,'
         ''   |           '      |  '   |         --'       _,-'
          \\\\  |                  '.'    |                 ,'
           .`.'                   `.    '                (
            `.____                  `--'                  `--..__
                  ``\"-.._                                        ``--..__
                         |\"                                              ``.
                         `                             .--\"''\"\"\"'`--------'
                          `.                           \\
              ,-\"'`-._      `-._                 `._    `.
             /        `.     ,._`-.._          _,'  `-.   .
            .    _      `.   |  `\"-._`     .-\"'        `-. `.
            |     `\"-._   `. |--.._  `._   \\              `. .
            |          `-._ `|     `-._ `-. `.              `'
            `        ._    `/'         `-. `. .
             \\         `\"-.'  .-....__    `. `.`.
              .          /    '       `\"-.._   | \\
               `.       /------\\            `  |  \\
                 `.___./        `              '   .
                      ,          `._        ,-'    |
                      |.-\"''\"\"'--.._`\"---'\"/       |
                      |  ______      `\"-../        |
                      .\"'      `\".       /         '
                    ,'            .     /         .
                   .              |   .'         /
                   |       ,'     |.-'          /
                   |       |      '            '
                    .       `-..-\"          _,'
                     `.                  _,\"
                       `._          __.-'
                          `'------\"' ''')

    elif n_pokemon + 1 == 117:
        print('''                                .                ,'
                                        /|               /,
                                       'j               / |
                                      / |              / j
                                     .  |             /  |
                      .              |  |      _     /  j                _,..
            ,         |\\            j   |   _,\",'   /   |           _.-\"',-'
            '`        | `.      ,.  |   | ,'  '    /   j        _.-', _.'
             \\`.      |   `...-\" '  |   \"'  ,'    /    |    _.-' _.','
              \\ \\     |           \\ |      /     /     L_.-'  _,' .'
               \\ `. ,\"`            v      `.__  /           ,' _.'
                \\  \\   .           |        .' /         _,' ,'
                 \\  `  '           '      ,'  /        ,'  ,'
               .--`.    \\   .     .     .'---/      ,-'   (
                `.  \\| | .  |    |`.  .'    /    _,'       `-..__
                  `. | ' '  |    ' |  |        ,'                `\"---...__
                   .'`. ` \\ '   ..'|  |    `,              __________......\"
                   `\"--`.`.\\ ` `---' ,    -.    -'\"'\"\"`''\"\"
                         |\"\"`      .'     /  .._.'  .  `\"`.
                __..--'\"\" `.       |`__|\\.     |  __`     |
          _,.-\"'            \\      | |     .  .'    |  --.'\\
         `-----\"`'\"\"''+.  _,'|     |/|      `-'  .  |    |  \\
                    .' _,\"   |     ' `..'_......._`\"  .  '   .
                  .'_,\"   _. |    _.'  ,'         `.   `'    |
                 /.\"  _.-'  '`.--\"   .'             \\  /     |
               .''_.-'     .  /     /        __      .'      |
             ,'_.'         ' /     .       ,\"  `.    |       |
            .-'           / /      |       |    '    |       '
                         . /       '       '         '      /
                         ,'         \\       .       /      /
                                     \\       `-...-'     .'
                                      `.              _,'
                                        `._        _,\"
                                           `\"----\"' ''')

    elif n_pokemon + 1 == 118:
        print('''                                            _.--.
                                               __  ,'     \\
                                             ,'  `\"        .
                                            |              |
                                 ,'`.      ,'              |
                           .._  /    \\   .'                |
                          /   `'      `. |     .          .'
                         .   |   _...__ |'    .           |
                         |   |.\"'      `|     '           .
                         |  ,'           \\   /            `.
                  '`.   .| .              \\ j               |
                   \\ `./ | |               .|              ,
                    \\  . `.|                .            .'
                     \\  `.                  '           _|_
                      \\   `.                 .        .'__ `
                     / .   |                 |        |\"  | `-...._
                    .      |       ,.--.     |     _.'    |        `.
          .-._      |   `  |      /     \\    |.--'\"       '         |
          |   `'\"\"'\"|    `       .     .'|                 \\        |
          |        ||            |    /| |                  \\       |
          '        ||            |  ,d | '                  |       |
         .         :`             .'\"-' /  /`.            _,'`.      `.
         |          \\.             `..-'  / \\ \\       .\"\"'     `.      |
         '._         '                   /   \\ `.    /           `    .'
            `-.     .'`. .._____        /     \\  \\   |                |
             _|     |   \\  ___  '    _,'       .  `  .`-._            '
           ,' |     |    `. \"\" / __,\"           `-..'     `.           `.
           |  `-----'     |\"''\"'\"                          '            |
           '              |                                 .           '
            \\          _.'                                  |          |
            |     ,-\"''                                      ._   _..  `.
            |    /                                             `\"'   `.  '
            `...'                                                      `\" ''')

    elif n_pokemon + 1 == 119:
        print('''                     ,-'\"\"\"--..__  .'\\
                             .            `\"   \\
                             '                  \\
               _____          .                  .
           ,\"\"'     `'--.._    \\                 '
          /                `._  \\  \\    +.     :' .
         .                    `._`. `.            |
         |                       `-`  .      _ .  |
         |                      '-._`._\\  \\ ' ||  |
         `.                         `. `.  . \\||  '
           `.                 .  ...  `._`.|  '` .
             `._              `   `.:    `.`.   '|
                `.                     '`  `.\\  ||  _,...._
                  `                   -.     ``.'|,\"       `-._
                   |                \" ._`-._ . -._`._ |  .     `--..  ...
                   |           ,....    `-.-'    .'  `.  ;       ,'  /   \\
                   |           `\"\"'   \"' /     .\"_     `.      .'   .     '
                   |       _       _,.-'/  .      \"\"-.   .   ,'.   j      .
                   |       +'    ,\"    /     +\"    _,.'  |  /.  \\  | . |  |
                   '           ,'     j  .'     ._ ...   | /  `. \\ |   '  |
                  ,.`----...._'`.    /|           _..-'  |/  ,-.  \\|  '   |
                  \".      __  `-.`. / |     +' _.\"  __....._  `.`._| / ,  '
                    `.   `\"-'      `-.|      .'_,-'\"        _.-\"'/ |/ '  /
                      \\         `\"-.._`-.   ,-'         ,-\"'   .`. |,' .'
                       |          `   `-.`./ _.._      |     ,'__ \\| ,'
                       |       __  +' -- .'.'.--.`.     \\  .','..`.+'
                       .      `--' .\"_,.\"  |||  | |      `\" | |  ||
                       `.         _.\"  /\\  || \"\" ||         || \"\"'|
                         `-...,-\"' ,' /  \\ `.`..'/          ' `..'
                            '        /    `. `--'            `.,'
                             \\      /       `=+=  ,--------. .'
                              `.___,           `.| `.____.','
                                                  `-.....-' ''')

    elif n_pokemon + 1 == 120:
        print('''                                ..
                                        .  .
                                           '
                                       ' \\/ '
                                      /  .  `
                                     .   |   .
                                     '   |
                                         |    '
                                    '    |
         ..__                      /     |     .
         '   \"-..__               .      |
          `.       `\"--..____..          |      '                  __..--.
            ..            |   |..'       |       ..\"-. ____,..---\"'      /
             .`.          |   ' \\        |      .'/   /              .','
              `.`.        `    \\ `. _,..-'._   , /   .            _.','
                `.`.       \\       \"        `\"' /    '          ,' ,'
                  . `.      .   '              /    /        _,' .'
                   `. `.     .   \\            /   .'       .\"  .'
                     `. `.  /`    \\          /   , \\     .' _,'
                       `  `/  \\    \\        /   /   \\  ,' ,'
                      ,\"`./    \\  ,-'\"\"'\"-./   /     \\_.-'
                      |._ `.    ,',-\"\"'\"\"`-.` '    _,' `.
                      |  `-._  . /          \\`._.-' _.-\"|
                       `._   `-|.            .|..-\"'    |
                       /  \\\"._ ||            ||     _,-\".
                      .    \\  `.|            ||..-''/   |
                      '     .   `           .'    ,'    '
                     .       .  .`._      .'`.  .'       .
                            .|,'   /\"----\"\\   `._|.      '
                    '     ,' `. _,\"-.    ,\"'._  .' `.
                   /    .'  _.'\"     `..'     `\"-.   \\    .
                  .   ,' _,'                      `.  `.  `
                  | .'_,'                           `'. `. .
                  `\"\"'                                 `. `|
                                                         `\" ''')

    elif n_pokemon + 1 == 121:
        print('''             .\"-.._          ____
                      \\     `-._     /  /\"\"\"-.
                       .    `\"-.`-_.'`.j      \\
              _________'  .,---'\"\",|   |...___.'
            .'          \\ `-.._ ,' |  ,      || \\ ____
             `.    __,.-+--'\"_.'  ,^./       ||  |____`\"\"---..__
            _,.`\"\"\"__....--.'   .\"  `..___   ||_.'  `.\"\"'\"\"`--- '.
           /_.--\"'\"       /   ,'      |   |\"\"'\\  \\    `.       .'
          .'             '  .' ___    |   |`\"--\\  \\ ____`.   ,'
           `.             \\,.-'   `.  |  j      \\  \\`.`.   ,'
             `-.                 /  \\ |  |       \\  \\ `.`.' `._
                `._             /   |j  j  ..--.  \\  \\  `.`.   `-._
                   `._        ,'    ||  | /  \\  `. '  .   `.`.     `.
                      >.     /      |'. |'    \\   `._,'     `.`.     `.
                    .\"  `.  /       |   |      \\               .` _..\"
                  ,\"    ,'`.         |\".'       \\               `.`.
                ,'   _,'   |         | |         \\                `.`.
              ,'  _,'      '        j j           \\                 \\ .
            ,'  ,\"          .       | |          _.\\....___          \\'
           '  .'            '       | '         /`   |     `\"\"`---..__|
         .'_.'               .     j .         '  `.  .
         |\"                  '     | |       ,'     \\  \\
          ''\"''\"\"\"\"''---------.    | |      /        `  \\
                              '   .' |    .'          \\  \\
                               .  | .    ,'.           `. .
                               ' j  |   /   `-.          . \\
                                .|  | ,'       `-.        . \\
                                `|  |.            `._      \\ \\
                                 `\"-'                \"._    ` .
                                                        `._  \\|
                                                           `-.| 

         ''')

    elif n_pokemon + 1 == 122:
        print('''               ,---.    ___
                        |(__)| .',-.`.
                        `.  j  | \\.'.'
                        _'  `\"'  ,-'___
                      ,\"         `\"',--.\\                     _..--.
                      |           __`..''                _,.-'      `-.
            ,-\"\"'`-.. '          (  `\"\"'         _...--\"'        ,.--..'
          ,'        .' `._____  ,.`-..--\"\"\"'----.               /
         /   _..._,'   .\"     \\ `..'|            `.        ___.'
         '.-\"  .'    ,'        '---\"               `.     /
              |    .'.._     ,'                      `.  /
               \\   `    `._ /      |  !    !  |        |\"
                `.  `.     |   __  |          j  ,--. _|..._
                  \\   `.\"\"\"\"-.'  `. '           /  ,'\"      `-.
                   `.   `.    `.  |   _____|   |  /            `.
                   |`....'     |_,'   `.   '    `.              |
                   |           |---....____....-\"`        .--.  '
                    .         ,'                  `..._  (    `'
                     `--..,.-'      _.--\"\"\"'\"'.   |,\"\".`. ,--.. \\
                          |       ,'       .\"\"\"`. ``-\" | |(__)|  `.
                          |      .         |(__) `-'   '\"   ,\"     |
                         / `     |          `--.          .'_,..-\"'
                        /   `._   ._       .\"\"\"`-         ||
                        '..._  `._  `-....( (__) __    _.','
                       ,'    `.   `---.....`..-\"'  `\"'\"_,\".
                  ,-\"\"`. _.---+..-'            `\"---+-'   `
                 /      `.                       .\" , \\    \\
                 ._    ,--.                     |  |  |.    \\
                  _:--'    `.                   |  `._| `..-|
              ,-'\"  `.    .' |                  '    `\"--...'-.
             .        `\"\"'_.-'                   `.           |
             |         ,-'                         `-.______,.'
             '.     _.'
               `---' ''')

    elif n_pokemon + 1 == 123:
        print('''           ______
                _.-\"______`._             ,.
              ,\"_,\"'      `-.`._         /.|
            ,',\"   ____      `-.`.___   // |
           /.' ,-\"'    `-._     `.   | j.  |  /|
          // .'   __...._  `\"--.. `. ' |   | ' '
         j/  _.-\"'       `._,.\"\".   |  |   |/ '
         |.-'                    `.'/| |   | /
         '                        '/ | |   |/
                                  /  ' '   '
                            |.   ` .'/.   /
                            | `. ,','.  ,'
                            |   \\.' j.-'/
                            '   '   '. /
                           |          `\"-...__
                           |             _..-'
                          ,|'      __.-7'   _......____
                         . |    ,\"/   ,'`.'__........___`-...__
                          .    '-'_..' .-\"\"-._         `\"\"'-----`---...___
                          |____.-','\" /      /`.._,\"\".                 _.-'
                       ,\"`| ,'   '   |      .,--. ;--|             _,-\"
                      |   '.| `-.|   `.     ||   /   '`---.....--\"'.
                      '     `._  |     `+----`._;'.   `-..____..--'\"
                       `.    | \"'|__...-|,|       /     `.
                         |-..|`-.7    /   '      /   |  '|
                         ' |' `.||`--'    |      \\   | . |
                                 |        |       \\  ' | |
                                 `.      .'        .   ' '
                                   `'-+-\"|`.       '  ' /
                                      |`-'  \\     /  /.'
                                      `   _ ,.   / ,'/
                                       ||'.'`.  / /,'
                                        `      ' .'
                                              /.' ''')

    elif n_pokemon + 1 == 124:
        print('''                _   _,.-.' .-.
                     _ .' |,'   .\"\".| |.\"\"._
                    ( || ,',\"\". `._`' `  '  `.
                    `\\ | `\" .-\"`-..`     .    `.
                     |     `..--.._       |     \\
                   _,|      _...'_.'     ,+.     `.
              ,\"\"'|   `...-'..\"\"(__.._ -\"   `\"--.. `.
             |`._,'  ,'  /\\ .'\"\"` .'\"\"`. `.    |  `. \\
             '      / / /  ||    ||    |.`.`.   .   | \\
              `.__,'-._'  /|` -\"'  `-.'  \\ \\ \\   `\"-'  \\
               ' `.   /  /_| | |'\"\"| | .-\"\"'`'\"`-,.-\"\\  .
              . / .\\ .  /  | | `._.' ||        ,'     \\  \\
             ' / / |/  /_.-+._`-..--\"-.       .   .    \\  `
            / /.'  '  ,'\"\"'-. `\".\"'\"\"'`..     |.        \\  \\
           / . |  j  .       . |        |\\__,\" |.  `    '   \\
          .  | |  |  |       ' |        '|   | ' `  \\    \\   .
          |    |  |  `.____,'   ..____,' |   |    .       \\
          |    |  |  | ._  _..---._   _,'    |       .        '
          |    |  |  | | \"\"  .    |`\"'   \\ `.|     '  '  '     .
          |    |  |  | |     |    |       `  `      .  .  \\    |
          |    |  |  | |     '    |        \\  `.    |  |   .   |
          '    '  |  | |      .   `         \\   \\   |  |   |   |
           \\      `  | |      |              .   `. |  |   |   |
            \\      \\ ' |      `    '          `    `+..|___|___|_........
             \\      \\ \\|       '    .           `.    `.                 |
              `.     \\ .        .   `             `.    `-.            .'
             _,'`.    \\'         .   \\              `-.._  `._       ,'
          _.\"     `._ `.`        |    .                       `._   .
         `._       _,`\"--`.      |     .                         `. |
            `-._ ,'              |      `.                         `|_
               ,'         |      |        `.                          `.
             .'   __...__.|      |          \\ __..._     _,..,.__       `.
             `-`\"'        `._..--'-.__      .'      `-..'        ``'\"--..-'
                                      `\"---' ''')

    elif n_pokemon + 1 == 125:
        print('''              '
                      .
                      | '
                      | |
                   .  ` '                              .
                   '`. . .          .--.              , .
                ..  `.`| `....___  '   |            ,_' |
               |  |   .    _,   .`-`,-\"          ,.'    '-.
               `..`._,'` .'.   '  ,'            /    .....|
                   `.'  ','      '  `-._      ,'     `----'
                   ,'| '/               `.  ,'   \\ .-\"\".   \\
                 |' |`'/ .|               `.     .'  _,'_.\"'
                /   `.' /_|  __       _...-'   .' |.' .\"    \\
              ,' `-.   '\" .-\"V `-.  ,'       ,'   |    `-'\"\"'
             ,--.'. `.   /      / ,' ,      /`.   |          |
           .'---'  `./\"\"|'.    / /  /      '   `-.|          |
          /         /   `-....','  /              `.|    | . |
         .|       .'       .'.'   /      _,        .'   .  | '
         ||       |        |/    /    _,'  7    _,\" `---'--\"'        _.._
         |`  .   /         |    . _.-\"    /   ,\"     |             ,'    `.
         `.`-', /          |   '.' ,.    /  ,'     ,-'.          .'       |
           `.              |   _.-' |   '  /    _,'   |         .\"\"`.   _,'
                           '.-'     '  /  /   ,\"      |        ,\"'.  |.\"
                            `      .  /  /  ,'        .       /    |,'
                          ,\".`.      .  '_.'        _.-`.    ,\"-.  /
                        .'`._`.`. '  ' ,'          `_.'\"\".  /\".  |'
                        |.`._`\" .`-.'           .     ___|.'   |'
                    ,--'  `-.' `|   `\"--..__..-\"' | .\" __|   ,'
                  ,' )       _,'            `'\"._.'  \"'   `-'
                 '\",' )__.-'\"                    `.          |.
                   '\"\"                             `-.  .    | |
                                                      `| `.-'`-.
                                                        `.'
                                                          ' ''')

    elif n_pokemon + 1 == 126:
        print('''
                                                          ,--'*'-.
                                                        ..    `'  `
                                                         '    .'...'
                                                     '  ,'::     |
                                                        ,..-Y-'  /--
                                             .              |' _.'
                                           .' .______ ,-'\"|  ,'
                                    /,  ,. '-'     .-' .\" | '
                                   /  \"'  ' -=L;'\\'    `-.'.
                      ,,          /__       ],L_/'        .'            |\\
                |`.  '\\  _,          |         .        ,'          =-. `|
                `. ,' |.`            '`-v      `'-.    |             | -,..
                 _:  \" `\\,.     ___    _'|  ,-,_-  `-..'          .]---> _`'
               . ___.   ' /'--.  -.=[----`, |   '-  ,'                | </
                      ]..b--`. -'- , ----`` |'--v -'            __-- ' ,,
                     .'|    <\\]``,[ -    '\\\\._  |'  '*'`- _  _,|    `''|
            \\\"''L     |   X`.  ` /--,    |  -`.:_ `.    ' TX_,.:'..  ,|
            `   |       \"` =. ----  _|    |      ` _ `\\ |=:| /   '-\\ --'
            |.   `.          '*'-..L    _,'      .' `,.``-() Y.-[ .'
            '    .            _. _.. -]-,..-,'    v.   \\|  ` '`'
         `.'       `.        ' ---.'- /-[  .',_   -.   ,)L
           |       .'      __,...-`=..__       '   '     '.
            ,\"', .'      -`... _-'      `.     ` ,'      | `.
                .`            .'          .     '        |   \\
                  '           |           |             .'    .
                 \\ `.         '           '            ,'     |
                  \\  `.        `         /           .'     _.'
                   '.  `-.     /`__    ,'.._______,-'--...-` `.
                     `.   `--..'J  \"'.'         ,'       `._\\` ``-...
                       `.   .'   `'|'        _,'          |    _    \"-.
                         `.'|  ..  |     _,-'             `-._| '.---.'
                         / _,_/  |-`---\"'                     `-..|
                        `-\"   | .'
                              -''')

    elif n_pokemon + 1 == 127:
        print('''                        _.-\".
                         ..-\"\"`.'    '..__,
                         `-. .'     /  ,.`.
                           ,'      '`. .'  `.
                          /       .-'        `....
                       ..'.      .\\             .|
                       .`./      | `.            '.
                       |         |  .\\       /|    \\
                      .'         |)  `\\       '   (_`
                     ,|          |    `.            |
                      |          |  _,.-.           |
                      |          |,'     \\          |
                      |          |        \\         |
                      |      \\,  '.        \\        |
                      '           |         `._     |
                       \\          |            `-..,+___
                        \\         |          /       |  `.
                         \\        '         / ,      '    \\
                          \\      ,  _      /.'      /|    `-.
                           `.   .    `-.    __     ' |     .'
                             `..'   -\"'  .-\"| |  ,'  |    |  '-..
                             /`.        (_`.`\" \\'    |_.-'-\"'-. .`.
                            .   \\       `._. `\".|    |         `|  .
                            |    \\`----\"\"`.`. / |,.-\"'`-.        `. '
                            |     \\        `-+-\"   /     \\         \\ \\
                           ,'     _\\ ___..-'      .       \\         \\ \\
                           j\"._,-\".'`.       _.-\"'|     _  \\         . \\
                          / ,'   /    `.._,-'    _| _.-'   `.        |  \\
                        .' '    ._      `-..__.-\"_|'        |        `..\"`.
            _..      _,'\"-/     | `-._   .'   `\"' `.      __|        /|  | \\_
          .'   `--\"\"' _.-'    .-|     `.'          '._  .`  `.      / |  |.'|
         .  \\ .\"\\ _,-'        `.'..-.-'           /   `.-._   .     `.|./__.'
         |`.` | /\"               |.'             / _.'     `-.|
         `_|.'`'                                `-' 
         ''')

    elif n_pokemon + 1 == 128:
        print('''                                                           .'`.'
                                                                   `     '
                                                      ,-'.`.        `    ``
                     '\"--.                          /'      \\        |    |
                      \\   `                         '.      `.      ',    '
                       .   |                          `- _,.\"-._-._   `. /
                       '   |,`.----.                            \"-.`.  |'
          ,\".        .'    '       '---.                            \\\\ ||
          | :     ,-'|    .             '                            ..||
          |  `._.',||`._.'|              \\.                          ||||
          `.   / ._| `-...'\\              \\`._                       |. '
           _,-'             . `--.         \\  `.                     '.'
         .\" .'             _|     `-`\".     .   `.                 .'.
          '-....'          |           `-. _.'    `._           _.','
           `.             .'                .-       `.       .'_,'
             `..__....._ `.               ,'           `-._ .',\"
                   /    `.|               '                `.'....__
                  .                   _:.]                   `\"''-._`.
                  '                 :\"    '                   `.    `. .
                   \\                |                                 `.`.
                    .               |                           .       ` .
                    |               '         |                          ` .
                    '.             .          |                  '        .|
                      |`.          |          |                  |        ||
                      |  `.        '          '                  |       . '
                      |    \"--.     |        /_                  |     -'   |
                      |        `.   |       /  `'\"\"`-._          |    ,'    |
                      '        ,\"'..|      .      '    `.        |    |.    |
                       .     ,'     '.     |\\    .       `       |      | ,/
                       |    /        |     | .   |        `.     |      `'
                       |   .         |    ,' |  .           \\    |
                       |   |         |    .  | .'            .__ '
                       '-..|         |___.   '\"              |../
                      /.-'           \\ .'
                                      ' ''')

    elif n_pokemon + 1 == 129:
        print('''

                                          __.--.._,-'\"\"-.
                                       ,-' .' ,'  .-\"''-.`.       .--.
                                     ,'    |  |  '`-.    \\ \\       `-.|
                                    /       .   /    `.   \\ \\        ||
                                   /         `..`.    `.   \\ .       ||
                                  /        . .    `.    \\   . .      '.
                         .\"-.    .  ,\"\"'-. | |      \\    \\   `.`.__,'.'
                          `. `. .   |     `. |       \\    .    `-..-'
                _______     .  `|   |   '   .'        .   |...--._
                `.     `\"--.'   '    .      | .        .  |\"\"''\"-._\"-._
                  `.             \\    `-._..'. .       |  |---.._  `-.__\"-..
             -.     `.           |\\           `.`      |  |'`-.  `-._   +\"-'
             `.`.     `-.        | `            .`.       | `. `.    `,\"
               `.`.      `.      |  '.           ` `      `.  \\  `   /
               | `.`.    __`.    |`/  `.     ...  `.`.     |   `.   .
               |   \\ .  `._      | `. / `. .'.' |   \\ \\    |     \\  |
               |.   ` \\    `-.   |   \\   .'.'/' |    \\ \\   |      ._'
               | `.  `.\\      `. |    \\ / , '.  |_    . \\  '-.
              ,     .  .\\       `|     . ' / |  | `-...\\ \\'   `._
              `.     `.  \\       |.    '/ .  |  |       ' .      `-.
               .`._    \\` \\      | `. /'  '  |  |       | |       ,.'
                .  `-.  \\`.\\    ,|   //  '   |  |__  .' | |      |
                |     `._`| `--' `  //  .    |  '  `\"  /| |   . -'
                '        `|       `//   '    |   .    / | |   |
               /....._____|       //   .  ___|   |   /  | |  ,|
              .         _.'      /, _.--\"'-._ `\".| ,'   | |.'
              |      _,' / ___   `-'.        `. _|'     |,
              |  _,-\"  ,'.'   `-.._  `.      _,'         `
              '-\"   _,','          \"- ....--'
             /  _.-\"_.'
            /_,'_,-'
          .'_.-'
          '*''')

    elif n_pokemon + 1 == 130:
        print('''
                                     /|
                         /`     |   / |
                        . |     |`.'  |  ,          .
                        | |     |     `\"'/       _,'           ,\"'
                        | |     |       /      .\" ,'         ,'/_
                        | |   ,\"| .-\"\"\"''`,`.,'  /      /|  /  ' )
              .'.       | |\"\"+._|'   .    '     ,__    / ) /   .'
               `.`.   .'| |     '_,\".`     \\     .'   '   '   /  _
                 `.`./ j  |  _,-'_,'.       `-..'    .        `-'/
                  _\\' `   |,\" _.' `. `.     _..|     |         ,'
          .    .\"'  \\._____.-' '    `-|  .-'  ,|    _|   ___  /
           \\`._ `-. `|.___,'| /     _.'      / |  ,\" |.-'   `.'.
            \\-.`\"-'  _______`'    ,' __.---.' ,^.' _.'_    __ `.`.
            |    `-.,...... `.   |,-\"     / .'. |-'    `-.\"  | |` \\
            '      ||\\/  |/`.|  .`       (,'   `|         `.'  '.| \\
            `-..--.||       || j      ____\\     |       _  |  /     `.---------.
               |   ||  ___..|||,.--\"\"'|.      .\"|     ,' | |\"/ `. ,'. .   ,.--\"
               |  .||.'      ||.._    ' )  _,'\\ |`'-.'   | |/    ||.' |   `.
               |,',|||      . |\"-.`._  `+`\"    \"      `.'  ^,.__,'.   |  ,--'
                // |||      |j  |\\\\  \"'  `.     |   ,-` `./ '     |   |`.\\
               .'  |||      ||  | .'      |   .\"`..|_ |  .   \\    |  /|
               ||  ||`.___.'f   ' ||     ,'--\"`._|,-.`|  '    +.._|,'.|
               ||  |`-.....'|    .'`.\"\"'`.       /\\ | `.'     |    |  |
          .'`  ''   `--....-'    | \\|   ``\\     '  \\|   |     |`._,'-\"'
          |`..''                 |  '    )|.   /`..|'   '     |   \\  /
           `\"\"'                  |   `-..''|  /    |   /    _..\"`.` /
                                 `         |,'     |  /  ,\"'_,|     \\
                                  `,_   _.-'.      |,' .'-'\"  '    , \\
                                   `.\"\"'     `.   .' .'      /   ,' | .
                                     `._       \\,'  .       /   /   | |
                                        `\"----\"'     \\  _  /  ,'    | |
                                                      `\" 7._,`      | |
                                                             \\      | '
                                                              `-. ,.|/
                                                                 '  |''')

    elif n_pokemon + 1 == 131:
        print('''                                       ,|
                                                ||
                                        ,-\"'\"\"`' `._
                                       '----.     __`....._
                                        `    `.  `. ;      `.
                                         `.    `.  `   ,\"`. |
                                           `.  _.`._   |  ' |
                                           .','  ,' `.  `--'
                                          /.' _,'    | /
                                         '/_.'       |.
                                          `---`\".    ||
                                                |    ||
                                               ,'    `|
                                  _           /       |
                                 ' `.        .'       |
                                  .  `._  _,'/|       |
                                 _|     \"'  / |       '
                             _,-' |        /  '        .
                          |\"'            ,'  '          \\
                          |   _        ,'   /            \\
                          ;  '        /    j              .
                     ,\"--'    `.    .      |              |         ________
                     `.   -.       / '     |              |   _,-\"\"'   __.._\"`-._
                      ,' ,-.`-.__.' /      '              |.-'  _..--'\"       _.-'
                      \\.'   `-.___.'      ,               '__.-\"           _.'
                      /        _..--    . |              /               ,'
                    ,`      .-'         | |           _,'._          _,-'
                _,-'      ,'           .' '       _.-'     \"-.....-\"'
              ,'     __ ,'          _.'  /  __..-'
            ,' _.-\"\"'  /         _.'  _.'-\"'
           '-'\"       /      _.-' _.-\"
                     /    _.' _.-'
                    .   .'_.-'
                    | ,'.'
                    | .`
                     `''')

    elif n_pokemon + 1 == 132:
        print('''
                                                    ,--._
                                                 _,'     `.
                                       ,.-------\"          `.
                                      /                 \"    `-.__
                                     .         \"        _,        `._
                                     |            __..-\"             `.
                                     |        ''\"'                     `._
                                     |                                    `\"-.
                                     '                                        `.
                                    .                                          |
                                   /                                           |
                                _,'                                           ,'
                              ,\"                                             /
                             .                                              /
                             |                                             /
                             |                                            .
                             '                                            |
                              `.                                          |
                                `.                                        |
                                  `.                                      '
                                    .                                      .
                                    |                                       `.
                                    '                                        |
                                  ,'                                         |
                                ,'                                           '
                               /                                _...._      /
                              .                              ,-'      `\"'--'
               ___            |                            ,'
            ,-'   `\"-._     _.'                          ,'
           /           `\"--'             _,....__     _,'
          '                            .'        `---'
          `                 ____     ,'
           .           _.-'\"    `---'
            `-._    _.\"
                \"\"\"''')

    elif n_pokemon + 1 == 133:
        print('''
                                               |
                                              /|
                                            ,' |
                                           .   |
                                             | |
                                          ' '| |
                                         / / | |
                _,.-\"\"--._              / /  | |
              ,'          `.           j '   ' '
            ,'              `.         ||   / ,                         ___..--,
           /                  \\        ' `.'`.-.,-\".  .       _..---\"\"'' __, ,'
          /                    \\        \\` .\"`      `\"'\\   ,'\"_..--''\"\"\"'.'.'
         .                      .      .'-'             \\,' ,'         ,','
         |                      |      ,`               ' .`         .' /
         |                      |     /          ,\"`.  ' `-. _____.-' .'
         '                      |..---.|,\".      | | .  .-'\"\"   __.,-'
          .                   ,'       ||,|      |.' |    |\"\"`'\"
           `-._   `._.._____  |        || |      `._,'    |
               `.   .       `\".     ,'\"| \"  `'           ,+.
                 \\  '         |    '   |   .....        .'  `.
                  .'          '     7  \".              ,'     \\
                            ,'      |    `..        _,'      F
                           .        |,      `'----''         |
                           |      ,\"j  /                   | '
                           `     |  | .                 | `,'
                            .    |  `.|                 |/
                             `-..'   ,'                .'
                                     | \\             ,''
                                     |  `,'.      _,' /
                                     |    | ^.  .'   /
                                      `-'.' j` V    /
                                            |      /
                                            |     /
                                            |   ,'
                                             `\"\"''')

    elif n_pokemon + 1 == 134:
        print('''                                                                                                    
                                               ``                                                            
                                                o`                                                           
                                                -/                                                           
                                                 /-                                                          
                                                 ./`                            .-:`                         
                                                  ::                        `.-:-/`                          
                                                  .:-                     ..:-. -`                           
                                                 .-::-....--.`         `...-`   :                            
                                            ``...` `:-    :  `....`  .-..-`     :                            
                                           :```    ./:-...-.`  `-`---``-.    .-:.                            
                                         `-` ..`...``-:  `....-- .-` ..   .-..-                              
                                      `...    --`..  -:  ..`....-` .-` `--` `-                               
                    `-:://:------.....:.`..` -`.-`.-`    :    `-. -. .-.`   -`                               
                         `.-.````......``.--/.-.    .-. .-  .-oss/``.`  ``.`/                                
                            ..       ``....``:`.::..  `.-  ::+NMd-. `.--.``:.                                
                             :.............`---mNd+/o`     hmNds/ :`````` ..                                 
                             `..-.`  ``````  :`oydmmd:  `  .--.`` :``````:-                                  
                                 `-`  `...`  .: .--.`   ..``      :       :                                  
                                   :-:.``  `..-.      .-...-      /..``  `-                                  
                                   ```:.`......:.      .-  :    `-`  ``  -`                                  
                                      ./.`..`   ...     `.-`  `.:.      `.-                                  
                                      -.        .-......````-.`  `-`   ..`                                   
                                      ``..`    -.     :`````.-     `  ..                                     
                                          ::` ``     `-      .`    ```:                                      
                                     ````..`/```     ``         `.:.```                                      
                               ``.....```.`-..``...``  ``.....`..`..                                         
                            ....`` ```...``        `.-.``     ``   :                                         
                         `..````....``                             :               ```.....```               
                        .- `..``     `````               `.   ``   :            ``..```   `...-.``           
                       :` ..`        `````...`   :       ..  .-   `/````````  `.``             `.-/`         
                      .- .-                 `..  :       -..::-.::::-:::--:---.                `--`          
                     -. .-                    `-`-    ``-/.---```.............:.              .-`            
                     : .-                      `::``-.--.``.-.``.        ```.       ``     `.-.              
                    -. -`       ..````````````.-::::``....`       ``..```   -        `-.```.`                
                    .-`-`         `````..-:--:-   `...`        `.:.`        -          ..                    
                    ``:.-`.`   `    ````-.  ```....`        `.-.`:          :           .-                   
                    `.`--.`.-.......```.``.....          `.:.`  ..          `-           .-                  
                     -  `......``........`             `-/.:    :            `-.          /                  
                     `-        ``                   `--. -`:    :              `--`       -.                 
                      .-                         `::/    `-:    :                 .--`    `:                 
                        --`                  `.---.+:`    ::  ``:.                   .--` `:                 
                          ..-..`        `.--//-``-:- -` .`:/-.:-:`                      .:/.                 
                              `..........`     ```    ..-..   ''')

    elif n_pokemon + 1 == 135:
        print('''XH                             HX               
         H;XHX                         HXH               
         H;;;;XH                      XHXH               
         XXXX;;;H                     HX;H               
          HXHHX;;H                   HXH;H    XH         
          HXXHHX;;X                 HXXH;H  HX;H         
          XXXHHHX;H        X  H     HXHX;HHX;;;X         
           HXHHHHX;H       HH HH   HXHH;;X;;;;X       XHX
            HXHHHHX;X XH  XXXHHXH  HHHH;XHX;;;H    XHX;;H
             HXHHHH;;XHXH HX;XHX;HHXHHX;H;H;;XXXHHX;;;;H 
          HHHXXXHHHX;;HXXXHX;;XHXHXHHH;;;XH;HXXX;;;;;XH  
           HXXXXXXHHX;;H;XXX;;;HX;HHHXX;XHHHXX;;;;;;XH   
            XHXXXXHHXX;X;;XXX;;;X;XHHXXH;;;HX;;;;;XXH    
              HHHXXX;;;;;;;;X;;;;;;XHXH;;;HX;;;;;XXH     
               HXHXXX;;;;;;;;;;;;;;HXH;;;;HX;;;;XXH      
                XHHX;XHXX ;;;;;;;XXXH;;;;HX;;;;XX;;XHX   
                HXXH;;HH X ;;;;;X H;H;;XHHHHHHXX;;;;;;HX 
              XHX;HX;;XHHHX;;;;XHHX;X;;;;;;;  H;;;;;;HX  
           XHX;;;HXHX;;XHHH;;;;HHX;;;H;;;    H;;;;;HX    
          XH;;;;;XHXH;;;;;;;XH;;;;;;XH      HXX;;HX      
            XHX;XHXHXX;H;;;;;;;;;H;XHX    HHXXXXX;;XHHHHX
               XH;;;HHXXHHHHHHHHH;XH    ;;  HXXXXXXXX;;H 
              H;;;;;;XX;XHHXXXXHH;H      H;; HXX;;;;;;H  
            XH;;;H;;;;HX;HXXXXXH;X        HHHXX;;;;;;H   
             HHHX;;;;;;H;;HHHHH;XH   ;;    HXXX;;;;HX    
               H;; ;;;;;HX;;;;;H     HX;;   HX;;;XHH     
              H;;   ;;;;;;XHHHX      XHHX;;  H;XH;;H     
             H;;    ;;;;              HHHHHHHH;H;;;XH    
            H;;   XHX;;;        X;    XHHHHHXXXX;;;;H    
           H;;XHHXH;H;;  H;     XX;    HHHHXXXXX;;;;XH   
          XHHHHHHHXX;;  ; H;     HHX;  XHHHXXXXXX;;;;XX  
                 HXH;   H; H;    HHHX;  HHXHXXXXXXX;;;H  
                 HXH   HXH; H;   XHHHHX; H   XHHXXXX;;;X 
                HXXH  HX  H;HH;   HHXXHHHHX     HHXXX;;H 
                HXX;HHX   XH;;H;  HHXXXXXHH      HXXX;;H 
               HXX;;HH   HXX;;;H; H HXXXXXX       HXX;;X 
              HXXX;;H    HXX;;;XH;H HXXXXXH       HXX;;;X
             HXXX;;X     HXX;;;XXHH  HXXXXH       HXX;;;H
          HHHXX;;;XH    HXX;;;XH  X  HXHXXX       HXX;;;H
         HXXX;;;;;H     HXX;;;H      XHHHX        HXX;;;H
         HX;HH;;HH     XXX;;;;H                   HHX;H;H
         HH;H;XHH      HX;;;;XX                   XHX;H;X
           HHHHX      HXX;;;;H                     XHHHX 
                    XHXX;;;;XH                           
                    HXX;;H;;H                            
                    XH;;H;;XH                            
                     XH;H;XH                             
                       XHHX''')

    elif n_pokemon + 1 == 136:
        print('''                         /|     '
                                 / `.  ,'|,-.____
                                /    `'  `       `\"\"----...,
                      .    ,__.'                        .-'._
                     / |   ' .'                   ,_         `'`--.._
                  _.'  . ,'                        `.`-._            `'.
                 |      `                            .  .`-._,\"'--._    `-.
              ,_.'     `                              `. .`._`.     `-._   '
               .                                     ..'  `. `.`.       `-. `.
               |                                       `.   `. `.`.        `. \\
               |                                       ,',.'\"-\\  \\ `.         `
             ,-'                                       /     .\"\\  `  \\
              .                              '`._ ,.  /      |  '  `. \\
          ..._)                               |  \"  `.        `-'.  |  .
            \\        '.---.._'._  .\"'-._     .'      |            `.|  '
             `.         `._ .._ `-'     `.`-.|       '              ` /
               `.          `-. `. `-.__   '-  `._     \\              |.
                L_            `._ `.   `\"--..__  `\"-../\\             ||-.,\\
                  `.'            `-.`.         `-._     `-._       .' |`.  \\
                     .           _..`.`.._       ..`      __`\"-..-'   |.'  '-'
                     /___     .\"'     `-._`\"----\"'   `  .( )`.          `.  .
                         -.,./      `\"\"   `\"\"'\"\"'`--.   `._   `.        /    \\
                            /        ,               `._   `\"\"'  _____.'      '
                                      .                 `._      \"...'       /
                           .         .'                    `\"\"-----'        ' _
                           '         `-.                                    .'
                         ,'            /                                   _,
                        /         _..-\"|\"--..                             |
                       /       .\"'     |  .'.,----,                  ,.-'\"|
                      .      ,'        |     \\   `--'.        __...-\"`...-'
                      '     /          '      \\       `-----\"'
                     /     '            .      \\        \\
                    .       .           '._,'_.'`.       \\
                    '._.  ).'                    `        `.
                       `\"'                        \\         `
                                                   `.   .   ,'
                                                     `\"-'--''')

    elif n_pokemon + 1 == 137:
        print('''


                                          :+///////:--.``                                                    
                                       .++-       ``.--+hs-                                                  
                                    `/+:`            .o/` ++                                                 
                                 `:+/`             `++`    -s.                                               
                               -++-              `++`       `o:                              `--.            
                            `/+:`      .---::://+s.           /+`                          `++-:ho`          
                           .s-         y:..``````/+.           .s.                       `/+. .s`.y          
                          :o`          y`   odmd+ `/+.          `o/                     :o.  .s` :o          
                         +/           `y   `mmmmd`  `++:://///////h                   -o-   .s`  y.          
                       `o-            `y    :sys.    .s.`        :o                 -o:    .s.  :o           
                      -s.            .os/           -s`          s.               .o/`    .s.   y.           
                     /+`           `++` +/     ``.-/o`          `y              `++`     `s.   :o            
                   `o:            /o.   .y+/////:-.`            +/            `/+`      `s.    y`            
                  `s+///////::--:o-   -+/`                   `/+.            :o.       `s.    :o             
                 `s.        ``-yoo:`-o:`                   `oy-`           -o-        `s.     y`             
                `s-         `++`  oho`                   .+/`.-://///:-.`.o:         `s.     :+              
                o:         :o. `:o- :o.                -o/           `.-:+////:-.`  `s.      y`              
               +/        -o: `/+-    `++`            :o:                      `.-://oo/`    :+               
              /+       `+/``/+.        .o:     ``.-+o-                                //    y`               
             .y`     `/o``++.      ``.-:/yo/////:-./h+.                               .s   :+                
              ://////y:.os/:///////ss-.`            y./+-                              y`  y`                
                    `-:/:-.`      :o`               -o  -+/`                           o- :+                 
                               .:oo                  s.   .++.                         :+ y`                 
                           .///:+o                   .s     .y                         .y:+                  
                         `o/`  /+                     +:    s-            `ooo//::--/+//yy`                  
                        /o`   /s`                     `y`  -s            `s-`:++-..-:///oo/////:-..`         
                      -o-     -ohs///:.                :+  y`           `o:    `:+/`           `.--++`       
                    `+/`         -s+-.-/////:.`         y.:+       `-//+h:        `/+:`             .o/`     
                   :o.          `+/`:+/.    .-/////:.`  .sy`  `-////-` +/            .++-             -o:    
                 .s:           :o.    `/+/`        `-////hs////.      /+                -++-```......---os   
                 :y/////:.`  .o:         ./+:`           `y.         :+                   /o:::------...:o   
                  y.    .-//+s`           .:os+-`         `y.       :o                  `o:             +:   
                  `:/+/.    .s        .///:.   -++-        .y`     -s                  .s.              y`   
                      `:++:``y   `-/+/:`          :+/.      .s    .s`                 /o`             `:s    
                          ./+h////-`                `-////:-`-o  .s`                `o:            `:+/.     
                              `                           `-:/oo+y`                .s.          `/+/.        
                                                                y+-.`             :o`        `/+/.           
                                                                /o.-://///:-.`  `o/       `/+/`              
                                                                 y.       `.-://y-     ./+/`                 
                                                                 -s`            y`  ./+:`                    
                                                                  -///////:-.`  y-/+:`                       
                                                                          `.-://o:`                          
                                                                                        ''')

    elif n_pokemon + 1 == 138:
        print('''                                                                                                    


                                                                     `.:+oyhhhhhhhhhhyyso+:.                 
                                                                .:oyhyo+/-.``         ``.:/oyy+-             
                                                            `:oys+:.                         `:sho`          
                                                         `/ss/.`                                `/h/         
                                                       -ss/``..----------.....``                  `oy.       
                                                     :yy::---.`````````.-----:://///::-`            :h.      
                                                   -yo-`                            ```-:::.         :d.     
                                                 `os.                                     `-/-        +h     
                                                .y/                                          ./.       y+    
                                               :y.    `......```                               /-      .m`   
                                              +y---:::---...-------------..`                    +.      d+   
                                             os:``                     ````.-----..`            `s     .od   
         `                                  oo`                                 ```.--..         o     /.N.  
         `                                 +s`                                        ``:-.      +   `:` m-  
         `                                :y`                                            `.:.  `-+----`  d:  
                                         .h.                                                -/--`  +`    d:  
                                        `y/       ````````                                  `+`    :`    m-  
                                        +s`..-::--...........--------.....`                `:`     -.    m`  
                                       `d/.``                        `````.----...        ./       .- `./m   
                                       ++                                      ``.-:-.   `/        ./..`/h   
                                      `h`                                           `.:-`+`   -:-  ..   so   
                                      /+                                               `o-   .. /  :`   d/   
         `                            h`                                               .+   .-  /  /   `m.   
         `                           -s     ```.....`````                              +`   :   /  +```+h    
         `                           o:.-----.....``....------.......``               -/   :`   / `/```d/    
         `                          `d:.`                      `````...------...`     +`   : `.:` /`  -d`    
         `                   `.-:/o:++                                       ``..-:.` s    : `:. ./`  so     
         `                .:++/:-oo`d.                                             .--s   `:    `:.-:-m`     
         `              -oo:`   /s`+o                                                -s    /   .:   `ho      
         `            .oo.     .h`+o`                                                `y    --.::`   -h`      
         `           :y-       y:oo`                                                  h`    /::`.- .h-       
         `          /y.       `ds/    .-:+//::::-.`              ..-:::::/-..`        o+   :` /  `:y+        
         `         :h`        `m/   -+/o+-`.-::-..--`         `:+:-.```.-/oo-:/-`     `h.`-`  /  `ho         
         `        `h-          y   +/`/. .sdNNmN+/..+`      ./y/  .+syy+:` /o``-+-     -y.    : `yo          
         `        :h           :/ `h ./ `hNNmmmNddy :s-```./::o  +mmmNNyhh` /+   :/`    -o`  -..y/           
         `        +y            //`y::- .mNNNNmmmms //.-::-` o. -mNmmmNNmm-  y    `+.    .o.`:/s-            
         `        :d             -+oy++``ymmmmmm.`o`       o` .mmNNNNmmm`  s    `-+.    `syo/              
         `         h/              .-.`/:.:+oss+:.-:`        ::  +dmmNN:  :-     --+     `y+               
         `         .h+`                 `---.----.`           /-` .:///-` ./:       /s.     -m`              
         `          .os-`                                      .::-````.:/:`         ++     .N`              
         `            `/o/.`                                      `.----.             :+`   oy               
         `             `.os--.`                                                        `//`+y`               
         `         `-/++/.    `-`                                     :             .`   .+h:`               
         `         :y/-....-:/.       .      .                       :.             .:     `:++-``           
         `           .-:/oy+.       .-`     .:         .        `.  ::              +//.      `:+so-`        
         `            .so:`    ``.-/.      ./         .y.        .//-              +: `:/-`       .+s+`      
         `            `:/://:/+sho-       :/        .+o-s-   ``-/o/`             `o/     .:::.`````.:d/      
         `                  `yy:`       .+-      `/so. ./hooooo/-              `:h/``       `/dsooo+/-.`     
         `                   .+o+++///+yo` `.-:+oo:`   h+.``                `-+o::ddysoo++++oo:.```````      
         `                            sy+++o+:-`       `+o/-`          ``-+syo-```.sy``````                  
         `                                                .:+++++++ossoo+sy:+osssso/`                        
         `                                                         `:/+++:`                                  
         `                                                                    ''')

    elif n_pokemon + 1 == 139:
        print('''
                                                         +s.                                                  
                                                       `h`o+                                                 
                                                       /o  -o-           `-.                                 
                                                      `d.    +yo++++/::oo/.s-                                
                                    -/-`         -/+++/s.....:-    ``.:///--h                                
                                    `h-:///:../oso/:--.-.....`           ./+o+/`                             
                                     /s   ``:oo.`           `.--..`        ./`.+o-                           
                                      s/      `s                  .-.       `+  `/o:                         
                                      `d/    .:-                    `-.      ./   `/s.                       
                                     .o/::-.............`             ..      +     `y/                      
                                    /o...---..```````````..-..`        -`     +      /oo                     
                             ``.--:oh++::-.                `.-:-.       :     /      /`o+                    
                           /yo:--....`````.:`           -//:-s/ ./.     :    `:     --  y-                   
                            ./+/`          `/         .o/`  s/   `:-    :..-::/-. .:.  `:h--.`               
                              `-+s:.       .-        .y-   -y      --  -:``    `-+. `//:..-/+/               
                                :o-/+:-...-.         y.    ++       /.:`  `---.  `:/o.  ./h.`                
                                h`   `..--.....-...-:o     :s``     `+-..:/.``-:  /o`  //`y-                 
                               -y  ``.--.````       .s      oo...`  :`  -+   ` `: y`  :s` ++                 
                               ++...`                +-     `/o:.`../```o.   -  / y   h:--o+                 
                ``.``          o+`  `.....``       ``.+:      `-++:-/...s`   /``/ y  .h   o/                 
              :+/:::/+:.       o/-:::--...``. `.:+++//+s/`       `/oo`  -:   .-.` s- -s   y.                 
             :s-.-..``-o/     :y+-`         .//-.`      -/         `:o/` +-`    `.h- :s  .h                  
             `-----:+-  o/    `/h+:-.``     -.   .-----.+-           `+s-..-:-::/+s  /o--s-                  
                    `y  `h`  `s/`  `---::---`  `:...`  `:-             s+ `..:///-  .s` ++                   
                     s-  o/  o+   -::-:.      .y` - -    +             :h/:--.`  `.//` /o                    
                     +/  .s-.+s` :-..``-:`   `/:. `..`   +             oo   `.-:/:-:.`/+                     
                     .y.  `:/+o//y `.-  :+:---` :.`..-``:-            :h--://oo+/:-.+o:                      
                   `/oyh+//::::/+//`... :. ``````.-----.`           `/y/:.       `-:o+.                      
                 `+o:.`    `...`  `-------/..-+.......`            .s/``.-:///+/-.`  .++.            `-.     
                 s/                   `-.:- `o       ./:`         ..+/+/:.``-/y-.-:/:.`.++-`       .+/oo     
                :s   `-::-`           :  `/ -+`````---``/           .s`       :o    `:/:`./++:-..-++-/o`     
                +/ `+o:-.-/+.        `+--.:  ------```.:/            .+o/::.   ++`     `:/:.`-:::-./+-       
               `:s/o.      -y+-`      /..-:. /+::---..-:               /+-`-/-  /o/---:/. `-::/::::.         
              /+os.      `s+` -/s:--+``-..`/ `::` `...`                 `:o:`:+/-.----/s:                    
              y. +s-`  `:s.  .+y/  -s    `......:///////:-.`               /s  `.:///:-                      
              -s. `:++//-  .o+`h  oy:        -+o+:.`    `.-::///:-`        -y                                
               `++-`    .:o+.  s-`m:      `/+:`                 `.:////////-                                 
                 `:///++:.      ///++/:://:`                                                                 
                                                                         ''')

    elif n_pokemon + 1 == 140:
        print('''
                                                `--:----------------.`                                        
                                       `-------.`                  -+++::-.                                  
                                  `-----`                         .:   -:-.:---                              
                              .:::-                                --.`  `o   `---.                          
                          `:/o-                                       .---`       `-:-`                      
                       `:/:``/-                                                      `-:-`                   
                     -o+..--:`                                                          `:-.                 
                   :/-`...`                                                                -:.               
                 -/.                                                                         -/`             
               ./.                                                                           .+::            
              /:`                  :                                                          :-.:`          
            `/-                    :`                     .:oyhdyyo/-`                         +` --         
           `+`        -+ydh+-`      /                 `-odNMMMMMMMMMN+.                      `+  ./`       
           +`      .+hNMMMMMNdo-`   `-.            .:sdNMMMMMMMMMMMMMMMMmy-                     -:  `/`      
          /.     .sNMMMMMMMMMMMNdy+-.``.      `.:ohmMMMMMMMMMMMMMMMMMMMMMMNy.                    o   `/`     
          s     /mMMMMMMMMMMMMMMMMMNmmdhysssyhmNMMMMMMNmNNMMMMMMMMMMMMMMMMMMm:                   ::    /`    
          h    +.dMMMMMMMMMMMmdddmMMMMMMMMMMMMMMMMMms:..../sNMMMMMMMMMMMMMMMMNo`                  :-   `/    
          s    + yMMMMMMMMNs-`` `./hMMMMMMMMMMMMMMy`        .hMMMMMMMMMMMMMMMM:`                 ./.  ./   
          o    / +MMMMMMMM/        `yMMMMMMMMMMMMm`          .MMMMMMMMMMMMMMMMMMNdo:`                -:` o`  
          /`   ` .NMMMMMMN          :MMMMMMMMMMMMd           `NMMMMMMMMMMMMMMMMMMMMM+:.             `/-.+  
          `/`     +MMMMMMM/        `yMMMMMMMMMMMMM+         `sMMMMMMMMMMMMMMMMMMMMMMMMMMmy/.`           -/y` 
           `:-`    sMMMMMMNs-`` `.:hMMMMMMMMMMMMMMMy:.` ``./dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd+.          `:/ 
             .:-``  sMMMMMMMMmdhdmMMMMMMMMMMMMMMMMMMMNdhddNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.          s 
               `.:-`-yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNsooosdMMMMMMMMMN/         o 
                 `+/- -hNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs:`      `NMMMNNMMMMMo        +`
                .+.     -smMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy.          dd+:--yMMmyy+       o 
               -+         ./yNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd            o`     +d`  .:      o 
               s             +shNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+            :-      +    --    `+ 
               o            /:.+-/ymNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/             +      ./    -`   +` 
               +`           + ./    -+hmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd             o       -+.` :`  ::  
               `+           `+o`   `   `yoohmNMMMMMMMMMMMMMMMMMMMMMMMMMMMNm:            o        o.-:s``-/   
                -:         `-::---.-/.-+:`-/:/:so++ooooo++osdhhmNNNNmdhs+-+.           /-      `/`   `..     
                 ./.              `::   ....  .+--.----.----    ````    `+-          `/.      ::             
                   -:-`         .::`         .+                :/.-------           :/      -/`              
                      ---::.`.::/:.        `::                 `+-                ::`     -:.                
                          .--`    `--.------                     -::.          -:-.--.----`                  
                                                                    .---.------ ''')

    elif n_pokemon + 1 == 141:
        print('''
                              `...........`        ``                                                         
                        ``..-..........  -       `  .`                                  ``.                  
                    ``.-....`         `  :      .    ``.````````        ``....`     ```` ``                  
                 `.....              ``. :     ``     `        `........``     ..```    `.                   
                ....                .`  :`:`   .     `                       ..        `.                    
              ...`      `..........-`    : -.  .    ``                     ..         `.                     
             ..`     ...`                -` --..    .                    `.          `.                      
            ..`   `.-`                    -.:-:     .                  `.`          ..                       
           - `  `-.                       ````-    .                  ..           -`                        
          -   `-.                            `/`   .                .-`          `:.                         
         .`  .-                               `:   -               --           -- `..                       
         - `-`                                 -`  :`            .:`-         .-.``..-:                      
         -.-                                    :` --           .::.-       .-.      ``                      
         ..                                      -.`:          -.`.`      `-.`..````````                     
                                                  `..-        -`      ```.-` `. .     ``....`                
                                                    `--      -`````````  -    - `          ``-.`             
                                                      `-..``.`.   .`    `-  `.-  `````````````.:             
                                                        `..`  `.   ..```.  .....` . ```....`````             
                                                      `````.`  `...-.`..  ````  - `-``    ``.`               
                                                  `````  `  ..`     `.`  `-     .` ``..``....`               
                                               `.``````..`.` `..-..``...`.-```..      `.`  ```               
                                             ..` `.`   .`  ..``.......-```..  -         -``  `.`             
                                           `.` `.`      .   ````        .`  . .`        - `....:             
                                          `-  .`      ``.  .`           -`   - -        `-  ```              
                                          -  -`    ``.``  .             `.--.:`-.        :    ```            
                                         -  -    `.`      -          ``..``````.:        ..     `.`          
                                        `. -`   `.        -..`````...``         :         :       `.         
                                        - ..   ..        .``..-```              -.   ```.`-``       .`       
                                        - :   .`         .    -                  .-.`-  `/. ````     `.      
                                       .`..  `.          -   .`                     `-... `-   ```     .`    
                                       .`:   -          ..  -                        ..    `.     ```   ``   
                                       `.:  .`          :  -                          `..   .-      `.`  ``  
                                        :.` .          -` `.                            `-`  `..      `.`  ` 
                                        : ` .         .`  .                               :`   `-       `.```
                                        -`  .        .`   .`                               :    ..        ``-
                                         :  .      `..... .`                               `.    -           
                                         .. -```-`..`.`  ..                                 -    -           
                                         .:`-.``.`.   -`  .                                 -  `..           
                                         . -..`   -``.....`                                 ....`.-`         
                                           `.`...`                                          :`.````:/`       
                                           ..`                                             `-` -  . `--      
                                                                                          .`  .-``..`  :     
                                                                                          - .`      `-.-     
                                                                                           :          .:  ''')

    elif n_pokemon + 1 == 142:
        print('''                              +H+                       
                                      H;;+          +HHHHHHHHHHH+
                                      +;+ +H+   +HH+;;;;;HHHHH+  
                                     +;;HH;;HHH+;;;;;;+HHH+HH+   
                                  H  H;+H;;++;;;;+HHHHHH+++H+    
                                 H;H H;HH;++;;+HHHHHH++++H+      
                                 +;+HH;HH++HHHHHHH++++++H        
                                  H;;+;;;HHHHHH++++++++H         
                                   +HH+;;;HHH+++++++++H          
                                      H;;+HH+++++++++H           
                                      +;+HH++++++++++            
                                     +;;HHH+++++++++H     +HHHHH+
                               H+    H;;HHH++++++++H  +HH+;;;;;H 
                            H+ +HH+  H;+HH+++++++++HH+;;;;;;;;H  
                           H;H  +HHH++;HHH++++++++H;;;;;;;;;;H   
            +H+           H;++  HHHHH;;HHH+++++++++;;;;;;;;;H    
           +;;;H         H;++  H+HHH+;;HHH+++++++H;;;;;;;;;H     
           H+;;+    +HHH+;++H H++HH+;;;+HH+++++++H;;;;;;;;+      
          ++;;;;H+ +;;;;;++HHH++HH+;;;HHHH++++++++;;;;;;;;H      
          H;;;;;;;H;++H;;;;+HH+HH+;;;+HHHHH++++++;;;;;;;;H       
         +;;;;;;;;;+   ;;;H+HHHH+;;+HHHHHHHH++++H;;;;;;;H        
         H;;;;;;;;+  H ;;;H++HH+;;+HHHH+++HHHH+++;;;;;;H         
         H;;;;;;;;;++H+;;H+++HH;;;HHHH++++++++HH;;;;;;;H         
         +;+HH+;;;;;;;;;;H++HH+;;+HHH++++++++++H;;;;;;+          
          +    +HHH++;;;;;++HH;;++HH+++++++++++++;;;;;H          
                H+++H++;;;+HHH;++HH+++++++++++++H;;;;;+          
               H+H++++;;;H+HH+;+HHH++++++++++HH+;;;;;+           
               HH H;;;;;H+++H;++HHH+++++++HH+;;;;;;;;H           
             +H H+;;;;H++++++;++HHH+++++H+;;;+H;;;;;;H           
            + H+;;;;H+  H++++;;+HHHH+++H+;;;;;;+H;;;;H           
            H+;;;;+H     H++;;;;+HHH++H++;;;;;;;;+H;;H           
           H;;;;;+H       H++;;;;+HHH+++;;;+HHHH+;;H+H           
           +H;;++++        H;;;;;;+HHH++;H+      +HHHH           
             H+++H         H;;;;;;;;+H+++            +           
              HHH          H;;;;;;;;;;+HH+                       
                           +;;;;;;;;;;;+++H                      
                            +;;;;;;;;;;;;++H                     
                            H;;;;;;;;;;;;;;++H                   
                    H       +;;+;;;;;;+;;;;;;;H                  
                   ++H       HHH;;;;;;H;;;;;;;;H                 
                   H++H       H;;;;;;;H;;;;;;;;;H                
                   H;++H      +;;;;+++H+;;;;;;;;;H               
                   H;;++H    +;;;;+++HHH+;;;;;;;;;H              
                   H;;;++H   H;;;;++H    +H;;;;;;;+              
                   H;;;;++H  H;;;;+H   +HH H+;;;;;;+             
                   H;;;;;;;H +;;;;H   H;;+ H++;;;;;H             
                   H;;;;;+H   H;;;;+HH;;H  ++++;;;;H             
                   +;;;;;H     +H+;;;;;;+   H+H;;;;H             
                    +H+;;;H       +HH+;++H+  HH;;;;+             
                       H;;;H         H;++++H  +;;;+              
                        H;;;+H+       +;++++H+;;;;H              
                         +H;;;;+H+    H++++H+;;;;H               
                           +H+;;;;+HHHHHH+;;;;;;H                
                              +HH+;;;;;;;;;;;;+H                 
                                  +H+;;;;;+HH+                   
                                     +HHHHH+''')

    elif n_pokemon + 1 == 143:
        print('''      ::                                              
               HHH:                   :HH                      
               HHHHH:               :HHHH                      
               HHHHHH: :HHHHHHHHH: :HHHHH                      
               HHHHHHHHHHHHHHHHHHH:HHHHHH                      
               :HHHHHHHHHHHHHHHHHHHHHHHHH                      
               ,HHHHHHHH:,,,,:HHHH:,,:HHH                      
                HHHHHH:,      ,:H:    ,:H                      
                HHHHH:,  :HH:  ,:  :H: ,:                      
               :HHHH:,,:H             :H,:                     
               HHHHH,,,,       :::       H                     
               HHHH:,,,,      :::::      :,                    
               HHHH,,,,,,    ,:::::,     ,:                    
              ,HHHH,,,,,,,   H::,,:H     ,H,                   
              :HHHH,,,,,,,,  H: ,, H    ,,HH:,:HHHH:,          
              H:::HHHH:,,,,,:HHHHHHHHHHHH:HHHHHHHHHHH:         
             ::HHHH:,:H:,:HH::,,         ,:HHH ,HHHHHH:        
            :HHHHHHHH:, HH::,,             ,:H :HHHHHHH:       
           :HHHHHHHHHHHHH:,,,               ,:HH:,, HHHH:      
           HHHHHHHHHHHH:, :,                  :H,,  HHHHH      
          ,HHHHHHHHHHHHH: H,                   :H  :HHHHH:     
          :HHHHHHHHHHHHHH:,                     :HHHHHHHHH     
          HHHHHHHHHHHHHH,,,                      :HHHHHHHH     
         ,HHHHHHHHHHHHH:,,,,                     ,:HHHHHH:     
         :HHHHHHHHHHHH:,,,,,,                    ,,HHH: HHH:   
         HHHHHHHHHHHH:,,,,,,:,                   ,,HHH, HH,H H:
         HHHHHHHHHHHH,,:,,,H H,                 ,,:HH:,,:, H:,H
         HHHHHHHHHHH:,: :,:   :,,H:            ,,,H::::H :H:, H
         HHHHHHHHHHH,,H  HH,  H:H,H,,        ,,,,:H::,,     : :
         HHHHHHHHHHH,:,  ::,, :H, H,,,,,,,,,,,,,,H::,,      ,: 
         :HHHHHHHHHHHH,,:,,:H:,:, :,,,,,,,,,,,,,:H:,,,       H 
         ,HHHHHHHHHH:,:H,      ,:H,,,,,,,,,,,,,:H::,,        : 
          HHHHHHHHHH,,,,         ,:,,,,,,,,:HHHHH:,,,   ,:,  ,:
          HHHHHHHHHH,,,           H,,,:HHHHHHHHHH:,,   ,:::,  H
          HHHHHHHHH:,,,   ,:::,   :::HHHHHHHHHHHH:,,   :::::  H
          HHHHHHHHH,,,    :::::,  ,HHHHHHHHHHHHHH:,,   :::::  H
          HHHHHHHHH,,,   ,::::::   HHHHHHHHHHHHHH:,,   ::::, ,:
          HHHHHHHHH,,,   :::::::   HHHHHHHHHHHHHH:,,   ,::,  : 
          HHHHHHHHH,,,   :::::::   HHHHHHHHHHHHHH:,,    ,,   H 
          :HHHHHHHH,,,   :::::::   HHHHHHHHHHHHHH:,,,       ,: 
          ,HHHHHHHH,,,   ::::::,   HHHHHHHHHHHHHHH:,,      ,:  
           HHHHHHHH,,,   ,:::::   ,HHHHHHHHHHHHHHH:,,,,  ,,H   
           :HHHHHHH,,,    ,:::,   :HHHHHHHHHHHHHHHH:,,,,,H:    
            :HHHHHH:,,,    ,:,   ,HHHHHHHHHHHHHHHHHHHHHH:      
             :HHHHHH,,,          :HHHHHHHHHHHHHHHHHH:,         
              :HHHHH:,,,        ,HHHHHHHHH:,                   
               :HHHHH:,,,      ,:HHHHHH:,                      
                 H:HHH:,,,    ,:HH:,                           
                       :HHHHHH:''')

    elif n_pokemon + 1 == 144:
        print('''    :--:.                                                                                .--/`      
             +   -:.                                                                           .::.  --      
             -:    -:`                                                                    .:///.   `/:       
              .-    `:-                                                             `-:///-`    .:/:         
           ----`-.     -.`                                                     `-///:.``    `-:/:`           
           +` `--:/.     -:.                                               .://:.....`` .-://-----:          
           `/-    `-//.    -/.                                          -/+:``---`    ..`       .::          
         `----:.     `.`    `::                                       /+-``::-`             .:::-`           
         ./``.-:/-`           `+`                                   `o: ./:`           `-/++/:---            
          -:`    `...`      `. ./                                   o: //`         `.---.``   `:/            
          .-/:.      `       :  o                                  :o -o         ```       `-::`             
         o``.-:/:--.`        :` o                                  y` s.               `-:::.`               
         -/-    ```..`       :`.o                                 :+ -o           .--://::----               
          `.::-.             : +-                                 s. o.         `-.``       -/               
             `-://:.`        :`s                                 `y `s                 `--::.                
           -::.``           ..+-                                 :+ :/           `..-://:::-                 
          /-`   `..`        :`s                                  o- +`        `..```    .-:-                 
          .:::++:.`        ..+-                                  y  /              `--::.`                   
           `::.`           .`s                                  `o  -         `.---------                    
           +.   `.-..     ``/:         `    `.-`                ::  .              `.--::                    
           :::/++:``      ` s        `-/`..-`:.  .:             o` ``        `.--://--`                      
            -/-`    `       y       .:`:-`  :-.--/.            `+                   `-:                      
           :/`   ...`       s`      / .- `..```./.            `+`       ``...------::-`                      
           ./:::/:`         .+.     -`:`-```.-::`           .::`        ``.-:::-.``                          
             `-:`  .--`    ```/:     ://:++/`.-          `-:.`        ````    `.-:-                          
             -/..-/:.       `.`-/`  :..::..`  /`      `.-.`            ```.::...``./`                        
             `..:/.   .`     `..`/. .:--`     :.    .--`              .`    ./:..--:`                        
               `o``.:/.        `-`-- /        -:  `-.` ``              .:.`   -/`                            
                ::--/`   `      `-.`::        `o .-` `.`             `  `:--...:/                            
                  `+`  `-` `      -`/          :--  ..           ``   -`  :.```.`  `...---::---..`           
                  .+..:o` .` `    `:`           `  -`             `.  `/-` +`  `.-:-..`` `````...::-`        
                   ...::`:` -.   `-`        `-    ..       ``  ``  `/.`:--:/--:-.`  ..-::-.```.----:/-`      
                      /:+` -/   `/-          /`   `         -   -.  :-.- `-:-`  `-::..`           `.-/+:     
                      ``--:o  ` :/`          ./     `` `    `+` `/:-/` `-:.  `-:-.`  `..-:::-..---..` `-/`   
                         ` +-:: .+-           /   `` :` -   `o:::. ` `-:.  `::.` `.-:-..``..........-:-.`/.  
                           `.`-`:+`          `/    :-`:--/..+.     `::.  .::. `-::.``.-:/:..::....:/:....-+. 
                               ``:.-         `/     -/--..--`    .::` `-/-``.:-. `.:-.` `-`  +     -.`.-..:s`
                                 `//        `:.      -         .:-` .-:. `-:-``.:-.       :  /`     :   `-`-/
                                   -:-    ..:-      -:      .-:.``-:-` .::. .::.          :  /`     /     - /
                                    //--.::``       ./ ``.---..-:-. .-:-``-:-`           -.  +     -.     . /
                                    .: ..-.`.-      `o..--.-:-..`.::-.`.:-.             .:  :-    `/       `:
                                     :-   `--::`    .+..---.--:---..---.               -:  -:    `/`       :`
                                      --  `-` `::`  //---:::-----...                 `:- `:-    `/.      `:` 
                                       ::-:`    `/`.+`                             `::` .:.    `/.      `-`  
                                       :`:`      /--+                           `.:-``.:.     .+.      .-    
                                      .::`       : -`                       ``-::.`.:-.     ./:`     `-`     
                                      /`:       .-:`                    ``-::-.`.:-.      ./:`     `..       
                               ``` ``:`:`       /--               ```-::--.`.-:-.      `-/:`     `..         
                             ...-:::-` ..```   -./`         ```-:::--.`.-:--.`      `-//-     `..`           
                            -:.-:..--....../-`.- .-:- ```-:::-:-.-::---.`     ```-:/:-    ``...`             
                            .. :-:`:.-`  `.-..   `::/::--..-:---.`    ````.-::::-.`  ``.-:-.                 
                                -  /.    ...:..///:-``----.`````.--:::::--.`` ```.-:::-.`                    
                                         :-::::.``-:--``.:::::-:-..``..-:://:::::-`                          
                                         /o:.`.::-..::::-..-:///:::::--.`                                    
                                       `/:``::-.://:://:::-.`                                                
                                      :/``/:`.+o+/:-.                                                        
                                    `/. -+``/s/-                                                             
                                    +. /: -+-                                                                
                                   :- /: +/                                                                  
                                   o `o +:                                                                   
                                   + /.-+                                                                    
                                   /.+.+-                                                                    
                                    /://:                                                                    
                                     -o-o:                                                                   
                                       --+o/:-.``...`                                                        
                                          `-::///::---.                                                      
                                                       `   ''')

    elif n_pokemon + 1 == 145:
        print('''
                                                                                                         .-:o:
                                /-                                                                `------:-  
         /o:--`                 .::-                                         `//             `-----   -:.    
           -:`.----.             --`::         :.                          -:/o-o`      .----.     `::`      
             -:.   `----- `o/----`:- `:-       :--      `+`             -:- -/`/` `-----`        `:-         
               .:-      `---++`  .-+.  `/-     / --    :-/           `::`  :-`o----            -::--         
                 .:-          .----./`   .:.:` /  :. -: ..         -:.    -/-.               -/-.-:.         
                   `::             `--    .+y::+   /:`  /  `../..:-                       `::` .:.           
                /++---::`                  :-      `   `:..-:/++:..                     .:-  .:.             
                   ---. ::`                 -:             `.``---                    -:.  .:.               
                      `---::.                `/.+    :yy`   .--                     ::`  .:.                 
                          .-+o.              -. do-/+dh`  --`                    `/:   .:.                   
            ./++/-------------:            `+--//--oo     `/                     ..----:--------/+-          
                .-----`                      `// `/+: .+--.`:`                           .------`            
                      .-----                 .o` +- .::/`  .--                    .---://:/:                 
                           `-----.           /`-:      -`    `             .------`  .----`                  
                                 `-----`    /`:+             :       .-----`    .----`                       
                                       +`  :-: ---       .:. /        :-   -----`                            
                                   `::/`  .+-`-/++-`    ---`-+        `.//-`                                 
                                   `o-:/``::--:-  ::`   .+`   :-   `--/  -:`                                 
                                 `-:`+` o.   --    /.   /:     /---/`-+    ::                                
                             `//+--:+./ `/  ./:`   -:   .-.   `:: -- //-`.-:-+:                              
                                .----..` .:-`-/---:/.     `+--/`.:+ :.`-/. -+ ./`                            
                               `+----`     -:`     :.      :-` ---` ...`---.----/:                           
                              -::--------` +      ::         .--/      -----+.. `-`                          
                                         : /    ::             :.  .--------+-.                              
                                         .:+  ::              -. --/-                                        
                                          :.::`.-:.            o:+` `:.                                      
                                          -+:--``/         `    o.-+-..:`                                    
                                         `:`    +   `/+    o.   ./-./.--o`                                   
                                               --  /- ::  ---/   + .--                                       
                                               + .//`/`+  /:-+/` `/                                          
                                              `/:. ::  :.`: .: :- /                                          
                                              -:        //      `:+`                                         
                                                        /:        `        ''')

    elif n_pokemon + 1 == 146:
        print('''                                                                                                 `  
                                                                                                        ``.. 
                `                                                                                    `.-  -  
             ..``.                                ``.`                                          ``.`.``  .   
          ``:`  `.                              ``. .                         `.              .``.``    `.   
          :-:   `.``                      `` .`.` `.`          `             `.`.            .``.       .    
         .`  -    .`                    ``. ``    ``          ..``   -`     `.  .          ```.`      -.     
         ``  -    `.`              `` . -`     `.      .``````.` . .:..`   ..  -`      `````-.       --      
          `` -       .             :::...    ``.      `-         - ..  .`  -   `-````.`  ..-`      ```       
           . ```     `.``      ``  `.:     ..-        .`       ``.``   -  `-``...`     `.``        .         
           .`  .       `-      :.. ..     `-     `.`   .      `-``..` `.````         ``         `.`          
            `. ..`     ..    ...`.`.   ```-      `-`.` .`    `-`.`..          .-```..          -`            
             `.``.`     `-``-`   `.    +.-    -`.`.  -`..     ````       ````.``` `            :.            
               .. -`      `.-          ``.    -` `   ```     `.`     `..`                   `..`             
                .``-.`    -      ```````.     `.          ````     `.-`                ````..                
                 -  `.-. -.`    `-`` ````   .`-.. ````.``     ` ``.`                 ```````                 
                 `````` .-.-````:`      ````.::`..````    ```...``                 .`:`                      
                     `...``:-``-/-   ``   `..`-.`       ``.                      -..``                       
                        `..``...-``.-``.     -.       ...`                   ````-`                          
                        `.``..-...`` .` .   .`   ````..`               `-..`.````                            
                       `.`--``  ``.`` `..       --`.`        ``.`       :` `                                 
                      ....`        `..  .        `.`..```.`````         :`                                   
                     `.`              ..`            `.``              -:                                    
                                       -               ``             :-.`                                   
                                       .                 .            ` --                                   
                                       .                  .`          ...                                    
                                       `.       `          ..``       -                                      
                                       .`       .           - -      .                                       
                                       `.       `.          - ````````                                       
                                        -`  ```` ..         -                                                
                                         ...```.````.``  ``.`                                                
                                          . `.         `.. `.                                                
                                        `.`.-             .` .`                                              
                                       .`..`               `. -                                              
                                  `...```.`                 . ``                                             
                                .--..`.``..-               `.` ``.``                                         
                                `.`-..     .             `--- ...-.-.                                        
                                   .`                       -.` .-.                                          
                                                            `.   ``                                          ''')

    elif n_pokemon + 1 == 147:
        print('''                              H  
                        +             H + 
           +HHHH+      + H           +; H 
          H+++;;;+H    H +           H; H 
         +HH+++;;;;H   H  +   +HHHHH+;; H 
         +   H++;;;;H  H; H H+;;;;;;;H  H 
              ++;;;;;+H+;; ++;;;;;;+H;H + 
              H++;;;;H;;H; H;;;;;;H  H;+ +
               ++;;;;+;;;H H;;+H;;+; +;H H
               H+;;;;;+;;  H;+  +;;+H;+ +H
               H+;;;;;H;;  H;HH H;;;;;H H+
               H;;;;;;H;   H;HHHH;;;;;HHH 
               H;;;;;;H   H+;+HH+;;+HH+H+ 
               +;;;;;;+  ++;;;++;+H    H  
              +;;;;;;;;+H H+;;;+H       + 
              H;;;;;;;;H  H+;;++;;      H 
              +;;;;;;;;+   H;;+H;;;;    + 
             +;;;;;;;;;;+  H+;++;;;;;; +  
             H;;;;;;;;;;H  H+;;+H+;;;;+   
             H;;;;;;;;;+H  H+;;H;;+HH+    
             H;;;;;;;;;+H  H+;+  ;;;H     
             H;;;;;;;;;++H H+;H      +    
             H;;;;;;;;;++HH+;;+      H    
             H;;;;;;;;;+++H;;+       +    
             H;;;;;;;;;;+H;;;H        +   
             H+;;;;;;;;;H;;;;+        H   
             +++;;;;;;;;;;;;H         H   
              H++;;;;;;;;;;;+         H   
              ++++;;;;;;;;;+          +   
               H+++++;;;;;;H         +    
               H++++++++++H;;;       H    
                H++++++++H;;;;;;    +     
                 H++++++H;;;;;;;;  H      
                  H+++H+;;;;;;;;; H       
                   +HH;;;;;;;;;;H+        
                      +H;;;;;;H+          
                        +HHHH+''')

    elif n_pokemon + 1 == 148:
        print('''                          H:              
                                  H H            H:
                                 :  H           H H
                                 H  :          H  H
                       H:        :   :         H  :
                     H:         : H  H  :HHH: :  : 
                    ::          H  H  H:     :H   :
                   :H           H     :    :   :  H
                   HH           :H : H    : :  H H 
                  ::H           H H  :    H H   HH 
                  H H           : H ::    :H:  :H: 
                  H:H            H HH:H:      : H  
                  HHH             :HHHH :     H H  
                 ::  :              HHH H     HH:  
                 H:: H              H:HHH:   ::H   
                 H:HHH              : :HH:     ::  
                 :H:  H             H H::       H  
                  H:::H              : H::      H  
                  :HH :H             H  H:::   ::  
                    :H  :H           :   H:::::H   
                      H   :H:         : H::HHH:    
                       H     :H       H H::  H     
                        H::    H      H  :::::     
                         :::    H     :   :H:      
                         H:::   :      :  :  :     
                         H:::    :     H  :  H     
               :H:       :::     H     H  :  :     
             H:   :H   :H::      H     H  :   :    
            H       :H:          H     H  :   H    
           H                    :H     H  :   :    
          HH      :             H:     H  :    :   
          :H      H:::         ::      :  :    H   
         : :       :::::      : H     H   :    H   
         H :        :H:::   :H H      :  :     H   
         H  :         :H:::H  H      H   :     H   
         H  :           :H:  H      H    :     H   
         :   :            :H:     H:    :      H   
          :   :              :HHH:      :      H   
          H    :                       :       H   
           H    :                     :        :   
            H    ::                  :        H    
             H     ::             :::         :    
              H:     ::::    :::::           H     
                H:       ::::               H      
                  H:                       H       
                    :H:                  :H        
                       :HH:           :H:          
                           :HHHHHHHHH:''')

    elif n_pokemon + 1 == 149:
        print('''                                                     `-`                                            
                             --`                              --`                    `                       
                             --             .-.     `        .--                     ` `                     
                             :-`          `..`.-....---.....:--`                                             
                             ---``....``...-` `-`---:-.....-``                                               
                             `.-------:-`` `` ` `-````-`                           ```                       
                               ``````.-``             `-`                                                    
                                  ```-``       `-::`    :`                           `                       
                               ``````-/`      `-/yh:    `:          `````              `                     
                                 ````-o+       -/hdy`    -`         -``......``                              
                             ````````.:-`      ``/-.      :         `.:`........`                            
                          ````` `  `-``                   :          -:    ```...-`                          
                             ``````-`              ``.    :         `-/ `      `...-`                        
                                  `-`              --`    ..       `-.- `-       `..-`                       
                               ``  .-` ``   .`    `:`      -.    ``---   ..        .--.                      
                              ``  `-:.-.````````..-:        .-``..-.`     -`        .-:`                     
                                 `-:`  --.`.-..-..`-.        `::.`         -         .-:                     
                     `   `.      -:`   -    :```  ``/          ..          .`         --.                    
                    `:.-.::``   `/.`   -    :....```..          `-`         -          -:                    
                    `/.-`...-.``-:`    :   ..        :            ..        ..         -:                    
                   `-``   ````../:````.-.../` `    `.-.   -        `-`       -         -:                    
                   -::`          `...`    ..`.`       -   -`         --      `.   `..  -:                    
                    --                   `-      `....-`   -`         `-`        -` `:`::                    
                     .-`                 :....        .-    ..          ./..... :    `:o`                    
                       --`              .-  ..........`-     .-`          -.  `:.     +:           `.        
                         ...--..........:...           :`      -`          .-         `         `..-:        
                                       .`               -       -.          `-                ... `:         
                                      `.  `...`.```.....:        .-          -`            ...   `:          
                                      :...`             ..        `-.        /:        `...     `:           
                                     -`                `./          `..-..:./.-`   `...`       .-            
                                    `:            `....` `-..         -:::-:/......`          -.             
                                   ..-      ```...`       -`          `` -.``               `-`              
                                  :` :......``           -`               :               .:.                
                                 :.  -`                .-.                -.          ``..-`                 
                                 :   `-           ``...`:                  -        `--`..                   
                                ..    `-`    ```..``    :                  :     `.-`.:.`                    
                                -`     `--...```        -.                .- ``.:` /..`                      
                                `-       `-`        ```...-`              /.:`` :...                         
                                 -`        `...``...```   `.-`           :. ..`..`                           
                                  -.         `.-.``         .:-`        ./``-.`                              
                                   .-`          `-`..`````..```.-       /:.`                                 
                                     --.`      `.    ```.-....../` .   `.                                    
                                 ``...`--     ..                `- `    -`                                   
                              `-.``          .`                 -`      `:`                                  
                            `--:-`        `..`                 -`        `-`                                 
                           ./-..-:. ``...``                    :`   `..----:                                 
                            :.:-.-:..`                         `-.-.+. -/.:`                                 
                                                                 ...:.-:`-`                                  
                                                                   `. `-   ''')

    elif n_pokemon + 1 == 150:
        print('''
                                                        `/:+`                      ```                        
                                                       :- .+`     `....``        -+-:/:                      
                                                       ./. `/--:::-....--:::::-./:   +.                      
                                                        `/.  .`              `.:`  `/.                       
                                                         `/                       `+`                        
                                                         `o                       /.                         
                                                         :-                       /.                         
                                                        `+                        ./                         
                                                        .:                        `+                         
                                                        `+    `.`           `     .+                         
                                                         :-`-:``.-`      `..` `-.`/.                         
                                                         `+``o/o.` `- `- ```:+-/ ./                          
                                                          :- //Nh/. .:-/ .:hNh--.+`                          
                                 `-:::::-`                `+```:+ss::.`:/yoo/.``+`                           
                                `+-`   `.+.              `:+-     ``     `     -:                            
                                /-       .o              +.`./-.            `-:-`                            
                                :/       :+:`           ::  --.-::.` ``. `.::.                               
                                 :/-...-/:`./:--..`     o   o    s.::-..::-`                                 
                                  `..-+-`    -+:..-:-.` + `.+:---o````.+-                                    
                           `...`      :+      `:/-..-//:+:/:-.` `.--:``-:-.-.                                
                         -/:-.-:/-``.:/. -      .s:...-/-````.-:`  `..-:-  `:-                               
                        .o`     `o/--.  `o      o`     `o`     `/.      -``  -:                              
                 ```    -/       /-      +`     s       o`       +`     ` .:` :-                             
             `-//:::://:-s:`   `:o.``    `.   ``++.`  `:/-`      -/     .- -/  +`                            
           `//-`       `-:os+:::----:::.````-/:-.-:::::. ./`     `+      /  +` :/                            
          .o.   ``...:.    `:+.       `-::::-`            `+.    `+      `  :` :s                            
         `o.  `::----:+/`    `+:                           `/:`   /.      `..``/o                            
         :+  `+.       -+`     //                            ./-` `::-..-::-` :./`                           
         o.  :/         -o`     /+                             -/.    `    `  /..:                           
         y   +.          :+      //                             `::        /. :-`/                           
         y   +.           //      o-                              +.       `o``+`/`                          
         s`  /:            +/     .o                              -/        .+ .+./`                         
         +-  .o             /+`    s.                             -:         -- .+.+`                        
         -+   +-             -o:   s`                        ./::-:` .`       `  `/:o`                       
          o`  `o.              -///-                      `:/-        ``       ````-/o:                      
          .o   `o`                                      `//`              .:-::::::/++s+                     
           :/   `+-                                    -+`                 -:        :+:+-                   
            //    :+`                                 :/`                   +         `o-:+`                 
             :+`   `//`                              :/                     o          `s`-o`                
              -+`    .//-                           -+                     .o           o. -+                
               `+-     `-/:-.                     `-s                      +-           o.  /:               
                `//`      `.-:::---.....-------::::s.                     .o           `s   `s               
                  .+:`         ````......``````   :/                     `o.           //    s`              
                    -/:`                         `o`                     +-           .o`    s`              
                      ./:`                       -/                    `+-           `o.     s`              
                        .:/-`                    +.                   `+-           `o-      s               
                          `-/:.`                 o`                  .+-           -+.      `o               
                             `-/:-.`             o`                `//`          ./:`       :-               
                                `.-:::-.``       :`              `:/.          .//.        ./                
                                     `.--::::-.-:+`            .:/.         `-/:.        .::`                
                                           `.://:`          `.//.        `-:/-`       .-/-`                  
                                           -/-`          `-/+:.````...-:/s:.      `.-/-.                     
                                          `o         .::::-:---------..` o       `+-`                        
                                           o`      `-:-`                 ::      .+                          
                                           o`     ./.                     +`     +.                          
                                          `o     .o`                      +.     +                           
                                          ::     o.                      `o`     /`                          
                                         `o`    :+                      `+-      `+-                         
                                         :/     y`                    ./o/-`      `:/.                       
                                        `o`     h/-                  -+. `-s`       `//.`                    
                                       `o.      y`o`                 o`    o.         `:/:`                  
                                       /:       s.o.                 -o.``:s.`           .:/:.`       ````   
                                      :/        :o-                   `///-`-:/:.         ...:///::::/::://` 
                                     :/         `o.`..``                       .:+.        .-:/::/++-`    .+:
                                    -+  `://`    `/:..::/-                       `+:`               -+-    `s
                                   -o      -+            //                        -//:.```         `/o-:--:.
                                   /:     `/o-:::::::`   `s                           `-:::::::::--:-`       
                                    :/::://-        `:////-  ''')

    else:
        print('''                /H                   
                        / =/        /H/       
                  /HHHH/ ==H       H   H      
          /H/  /H/      H==H      /=    H     
         /   HH=          =H      H==    /    
         H== ==           //      /==    H    
         /==             // /      H==   /    
          H=   /H/==     H H /      H==   /   
           H=  H=H/=     /H/ H       H==  H   
            H= H HH/     =/ =/        H===H/  
            H= H H /      ==H  H       H=H=H/ 
            /==/HH/=       H  H=/       H= HH/
             H======       / H=/H      /=  / H
              /H==/==     H H== /      H= /  H
                 HH/HHHHH/ H/==H       /= H =H
                  H///==/H///HH/      /=    //
                  ///====/HHH= H/     H=    / 
                 H/===== =H=H  HH     H= =  H 
                H==/=     H H  H=/    H =/ // 
               H=  H=     / /  / H    H // H  
              H=   /     /=      H    H // /  
             H=   /=     H       H    H ///   
            H==  /H=     H       H    H = H/  
            /=H /H / =   H  =/= =/   H=  //H  
             / /   H==/H H  /// /=/H H   H/H  
                   H==  /H  /// H==/H=   H=H  
                   H===  H  ///=/=====  /H=H  
                  H/==== /= =/=/====/HH/ /=/  
                 H///===///=   HHHH/    H H   
                H//HH==///H=  =/        / /   
               H///  /HHH/H== /        H H    
               H//H      H/===H     /H/ H     
                ////H/     /=/  /HH/=  H      
                 //////HHHHHHHH/====/H/       
                  /HH//==========/H/          
                      /HHHHHHHHH/''')

if weekday == "Monday" and random.randint(0, weekday_chance) == 1:
	logo = logo +"  Just another manic monday!\n\n"
elif weekday == "Tuesday" and random.randint(0, weekday_chance) == 1:
	logo = logo +"  It\'s chewsday init\n\n"
elif weekday == "Wednesday" and random.randint(0, weekday_chance) == 1:
	logo = logo +"  It is Wednesday my dudes.\n\n"
elif weekday == "Thursday" and random.randint(0, weekday_chance) == 1:
	logo = logo +"  Thursday. Thursday. Thursday. Thursday. Thursday.\n\n"
elif weekday == "Friday" and random.randint(0, weekday_chance) == 1:
	logo = logo +"  It's Friday, Friday, gotta get down on Fridayyyy\n\n"
else:
	if random.randint(0, 9) == 1:
		pokemon_appeared = True
		if os.path.exists('{}\\pokelog.txt'.format(os.environ['USERPROFILE'])):
			pokelog = open('{}\\pokelog.txt'.format(os.environ['USERPROFILE']),"r")
			pokelines = pokelog.readlines()
		else:
			pokelog = open('{}\\pokelog.txt'.format(os.environ['USERPROFILE']),"w")
			pokelines = ""
		pokelog.close()
		for x in pokelines:
		  pokemon_list.remove(x.strip())
		if len(pokemon_list) != 0:
			pokechoice = random.randint(0,len(pokemon_list)-1)
			pokemon = pokemon_list[pokechoice]
			for index in range(len(original_pokemon_list)):
				if original_pokemon_list[index] == pokemon:
					poke_number = index
					original_logo = logo
					logo = logo +"  A wild {} appeared!\n\n  Type 'pokeball' to throw a pokeball or 'pokedex' to see your box.\n\n".format(pokemon)
		else:
			logo = logo +"  YOU CAUGHT ALL 151 POKEMON!\n\n".format(pokemon)
	else:
		logo = logo +"  "+one_liners[random.randint(0, len(one_liners)-1)]+"\n\n "
while True:
	if flag == "":
		prompt_mapping_category()
	prompt_query_criteria()
	url = setUrls()
	scrape = urllib.urlopen(url)
	html = scrape.read()
	parseData(html)
	cloneMappings()
