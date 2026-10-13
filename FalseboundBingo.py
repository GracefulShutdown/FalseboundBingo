# Falsebound Kingdom Bingo Question Generator by GracefulShutdown
# Used to generate JSON for https://bingosync.com/

#BingoSync Fields:
## Room name - The name of your room
## Password - Some password to share with others
## Nickname - Your display name (probably username)
## Game - Use "Custom (Advanced)" until there's an actual
## Variant - Fixed Board is fine for us here.
## Board - This is where you paste out the JSON result of this script
## Mode - Where you select to enable lockout mode, which prevents other players from selecting the objective
## Seed - Not needed for this 
## Hide Card initially - Use to hide the card ahead of time.

##monster_list = ["Blue-Eyes White Dragon Azrael", "Blue-Eyes White Dragon Ibris", "Blue-Eyes White Dragon Djibril", "Seiyaryu", "Blue-Eyes Ultimate Dragon", "Kaiser Dragon", "Blackland Fire Dragon", "Curse of Dragon", "Red-Eyes Black Dragon", "Black Skull Dragon", "Serpent Night Dragon", "Meteor Black Dragon", "Crawling Dragon", "Meteor Dragon", "Baby Dragon", "Winged Dragon", "Guardian of the Fortress #1", "Gaia the Dragon Champion", "Thousand Dragon", "Parrot Dragon", "Harpie's Pet Dragon", "Two Headed King Rex", "Megazowler", "Uraby", "Kairyu-Shin", "Aqua Dragon", "Sea King Dragon", "Spike Seadra", "Thunder Dragon", "Twin-Headed Thunder Dragon", "Mystical Elf", "Time Wizard", "Rogue Doll", "Magician of Faith", "Dark Magician", "Dark Magician Girl", "Magician of Black Chaos", "Saggi the Dark Clown", "Illusionist Faceless Mage", "Skull Knight", "Cosmo Queen", "Dark Elf", "Lord of D.", "Invitation To A Dark Sleep", "The Illusory Gentleman", "Tao the Chanter", "Aqua Madoor", "Water Girl", "Dragon Piper", "Gemini Elf Kachua", "Gemini Elf Lora", "Dark Magician #2", "Giltia the D. Knight", "Black Luster Soldier", "Swordstalker", "Flame Swordsman", "Lava Battleguard", "Swamp Battleguard", "Judge Man", "Gaia the Fierce Knight", "Celtic Guardian", "Axe Raider", "Zanki", "Ansatsu", "Kanan the Swordmistress", "Monster Tamer", "Swordsman from a Foreign Land", "Garoozis", "Hitotsu-Me Giant", "Battle Ox", "Beaver Warrior", "Mountain Warrior", "Tiger Axe", "Rabid Horseman", "Sengenjin", "Panther Warrior", "Mystic Horseman", "Buster Blader", "Stuffed Animal", "Dark Rabbit", "Silver Fang", "Gazelle the King of Mythical Beasts", "Chimera the Flying Mythical Beast", "Crimson Sunbird", "Mavelus", "Wing Eagle", "Big Insect", "Basic Insect", "Hercules Beetle", "Larvae Moth", "Perfectly Ultimate Great Moth", "Dungeon Worm", "Man-Eater Bug", "Hunter Spider", "Armored Lizard", "Fiend Kraken", "Jellyfish", "Octoberser", "Beastking of the Swamps", "Giant Red Sea Snake", "Kanikabuto", "Zarigun", "Penguin Soldier", "Harpie Lady Airo", "Harpie Lady Ocupete", "Harpie Lady Keraino", "Sanga of the Thunder", "Kazejin", "Suijin", "Gate Guardian", "Insect Queen", "Fairy's Gift", "Hane-Hane", "Gyakuteno Megami", "Orion the Battle King", "Dark Witch", "Dancing Elf", "Enchanting Mermaid", "Flame Cerebus", "Giant Soldier of Stone", "Millennium Golem", "Dark Plant", "Queen of Autumn Leaves", "Moisture Creature", "Dunames Dark Witch", "Embodiment of Apophis", "Mystical Beast Serket", "Phantom Dewan", "Shadow Specter", "Zombie Warrior", "The Snake Hair", "Armored Zombie", "Dragon Zombie", "Pumpking the King of Ghosts", "Shadow Ghoul", "Ghoul with an Appetite", "Feral Imp", "Summoned Skull", "Horn Imp", "Kuriboh", "Castle of Dark Illusions", "Reaper of the Cards", "King of Yamimakai", "Dark Chimera", "Dark King of the Abyss", "Midnight Fiend", "Ryu-Kishin Powered", "Bickuribox", "Zoa", "Dragon Seeker", "Neck Hunter", "Three-Headed Geedo", "Kryuel", "Beast of Gilfer", "Berfomet", "Fortress Whale", "Labyrinth Tank", "Metalzoa", "Cyber Soldier", "Cyber Commander", "Dharma Cannon", "Red-Eyes Black Metal Dragon", "Barrel Dragon", "Slot Machine", "Launcher Spider", "Robotic Knight", "Machine King", "Giant Mech Soldier", "Jinzo", "Alpha The Magnet Warrior", "Beta The Magnet Warrior", "Gamma The Magnet Warrior", "Valkyrion The Magnet Warior", "Cyber Saurus", "Rocket Warrior", "Obelisk the Tormentor", "Slifer the Sky Dragon", "The Winged Dragon Of Ra"]

import random
import json
from collections import Counter

campaigns = ["Yugi", "Kaiba", "Joey"]

### MARSHALLS
yugi_marshalls = ["Yugi", "Joey", "Tristan", "Tea", "Mai", "Mako", "Espa Roba", "Bakura", "Fizdis", "Shimon"]
kaiba_marshalls = ["Kaiba", "Bonz", "Pegasus", "Labyrinth Ruler", "Weevil", "Rex Raptor", "Ishizu", "Mokuba", "Marthis"]
joey_marshalls = ["Joey", "Jussell", "Malairuka", "Tristan", "Mai", "Tea"]
yugi_wipeable_marshalls = ["Joey", "Tristan", "Tea", "Mai", "Mako", "Espa Roba", "Bakura", "Fizdis", "Shimon"]
kaiba_wipeable_marshalls = ["Bonz", "Pegasus", "Labyrinth Ruler", "Weevil", "Rex Raptor", "Ishizu", "Mokuba", "Marthis"]
joey_wipeable_marshalls = ["Jussell", "Malairuka", "Tristan", "Mai", "Tea"]

### MONSTERS
yugi_initial_monsters = ["Celtic Guardian", "Feral Imp", "Kuriboh", "Flame Swordsman", "Giltia the D. Knight", "Robotic Knight", "Gazelle the King of Mythical Beasts", "Swordsman from a Foreign Land", "Giant Soldier of Stone", "Dancing Elf", "Gyakutenno Megami", "Dark Witch", "Harpie Lady (Airo)", "Harpie's Pet Dragon", "Curse of Dragon", "Kairyu-Shin", "Fiend Kraken", "Jellyfish", "Jinzo", "Giant Mech-Soldier", "Cyber Saurus", "Ansatsu", "Beastking of the Swamps", "Stuffed Animal", "Horn Imp", "Kanikabuto", "Penguin Soldier", "Zombie Warrior", "Shadow Specter", "Beaver Warrior"]
yugi_unlockable_monsters = ["Silver Fang", "Blackland Fire Dragon", "Mystic Horseman", "Hane-Hane", "Man-Eater Bug", "Winged Dragon, Guardian of the Fortress #1", "Octoberser", "Enchanting Mermaid", "The Illusory Gentleman", "Beast of Gilfer", "Neck Hunter", "Summoned Skull", "Dark Magician", "Baby Dragon", "Sanga of the Thunder", "Harpie Lady (Ocupete)", "Dark Magician Girl", "Time Wizard", "Dark Elf", "Red-Eyes B. Dragon", "Panther Warrior", "Suijin", "Fortress Whale", "Aqua Dragon", "Dark Magician #2", "Labyrinth Tank", "Dragon Piper", "Machine King", "Beta The Magnet Warrior", "Millennium Golem", "Gaia The Fierce Knight", "Harpie Lady (Keraino)", "Alpha The Magnet Warrior"]
kaiba_initial_monsters = ["Crawling Dragon", "Hitotsu-Me Giant", "Saggi the Dark Clown", "The Snake Hair", "Phantom Dewan", "Midnight Fiend", "Bickuribox", "Dark Rabbit", "Parrot Dragon", "Shadow Ghoul", "Dark Chimera", "Zanki", "Hercules Beetle", "Basic Insect", "Big Insect", "Two-Headed King Rex", "Megazowler", "Uraby", "Dunames Dark Witch", "Orion the Battle King", "Magician of Faith", "Armored Lizard", "Three-Headed Geedo", "Zarigun", "Dark King of the Abyss", "Dark Plant", "Water Girl"]
kaiba_unlockable_monsters = ["Berfomet", "Ryu-Kishin Powered", "Gamma The Magnet Warrior", "Tiger Axe", "Garoozis", "Mountain Warrior", "Moisture Creature", "Sea King Dragon", "Giant Red Seasnake", "Spike Seadra", "Insect Queen", "Queen of Autumn Leaves", "Larvae Moth", "Barrel Dragon", "Slot Machine", "Launcher Spider", "Buster Blader", "Cyber Commander", "Thunder Dragon", "Meteor Dragon", "Seiyaryu", "Kaiser Dragon", "Judge Man", "Blue-Eyes White Dragon (Azrael)", "Blue-Eyes White Dragon (Ibris)", "Blue-Eyes White Dragon (Djibril)", "Lord of D.", "Zoa", "Kryuel", "Castle of Dark Illusions"]
joey_initial_monsters = ["Axe Raider", "Cyber Soldier", "Rocket Warrior", "Ghoul with an Appetite", "Illusionist Faceless Mage", "Dharma Cannon", "Embodiment of Apophis", "Fairy's Gift", "Tao the Chanter", "Monster Tamer", "Dungeon Worm", "Hunter Spider", "Wing Eagle", "Mavelus", "Kanan the Swordmistress", "Mystical Elf", "Rogue Doll", "Aqua Madoor"]
joey_unlockable_monsters = ["Serpent Night Dragon", "Invitation to a Dark Sleep", "Swordstalker", "Dragon Seeker", "Battle Ox", "Swamp Battleguard", "Sengenjin", "Flame Cerebrus", "Gemini Elf (Kachua)", "Mystical Beast Serket", "Skull Knight", "Kazejin", "Pumpking the King of Ghosts"]

### MONSTER TYPES
monster_types = ["Dragon", "Spellcaster", "Warrior", "Beast", "Darklands", "Spirit", "Machine"]

### ITEMS
consumable_items = ["Blue Medicine", "Dark Energy", "Destruction Punch", "Dian Keto the Cure Master", "Dragon Capture Jar", "Dragonic Fury", "Goblin's Secret Remedy", "Monster Reborn", "Polymerization", "Power of Nature", "Red Medicine", "Riryoku", "Snake Fang", "Super Rejuvenation", "Violet Crystal"]
equippable_items = ["Beast Fangs", "Black Pendant", "Book of Secret Arts", "Cyber Shield", "Deal of Phantom", "Dragonic Attack", "Electro-Whip", "Enchanted Javelin", "Laser Cannon Armor", "Legendary Sword", "Multiply", "Shock Shell", "Silver Bow and Arrow", "Sword of Dragon's Soul"]
magic_items = ["Black Shield", "Bless of Moonlight", "Chaos Blaze", "Dragon Treasure", "Final Flame", "Germ Infection", "Gift of the Mystical Elf", "Gravity Bind", "Hinotama", "Mage Power", "Magic Jammer", "Mesmeric Control", "Mirror Force", "Mirror Wall", "Quick Attack", "Raigeki", "Raimei", "Shadow Spell", "Solar Shine", "Sparks", "Spellbinding Circle", "Swords of Revealing Light", "Yami"]
ritual_items = ["Black Luster Ritual", "Call of the Grave", "Cocoon of Evolution", "Metalmorph"]
god_items = ["Eye of Ra", "Slifer's Orb", "Soul of Obelisk"]
all_items = consumable_items + equippable_items + magic_items + ritual_items + god_items

# MISC
funny_numbers = [0, 69, 420, 1337, 8008]
lose_conditions = ["main character defeat", "main base capture", "timeout"]

#================
"""# Extract the first characters from each string and create a list
first_chars = [s[0] for s in available_monsters]
# Count the occurrences of each character
char_count = Counter(first_chars)

# Find the most common first character
most_common_char, count = char_count.most_common(1)[0]

print(f"The most common first character is '{most_common_char}' with {count} occurrences.")"""
#================
campaign = "Yugi"

if campaign == "Yugi":
    available_monsters = yugi_initial_monsters + yugi_unlockable_monsters
    available_marshalls = yugi_marshalls
    available_wipeable_marshalls = yugi_wipeable_marshalls
    #print(available_monsters)
elif campaign == "Kaiba":
    available_monsters = kaiba_initial_monsters + kaiba_unlockable_monsters
    available_marshalls = kaiba_marshalls
    available_wipeable_marshalls = kaiba_wipeable_marshalls
    #print(available_monsters)
elif campaign == "Joey":
    available_monsters = joey_initial_monsters + joey_unlockable_monsters
    available_marshalls = joey_marshalls
    available_wipeable_marshalls = joey_wipeable_marshalls
    #print(available_monsters)
else:
    print("Invalid")
#print (len(available_monsters))
#print (random.sample(available_monsters,25))

#List of questions that apply to ANY campaign
generic_question_list = [f"{random.sample(all_items,1)[0]} available for sale in shop.",
                         f"{random.sample(available_monsters,1)[0]} unlocked for team.",
                         f"Defeat a mission with {random.sample(available_monsters,1)[0]} on your team.",
                         "Survive a battle with under 69 health on a monster. Nice.",
                         f"Defeat a team with only {random.sample(monster_types,1)[0]} monsters on your team.",
                         "Win a battle on points",
                         f"Ritual summon a monster using {random.sample(ritual_items,1)[0]}",
                         "Fusion Summon a Monster",
                         "Get Confused at any point of the run.",
                         f"Wipe {random.sample(available_wipeable_marshalls,1)[0]} in one mission",
                         f"Buy {random.sample(all_items,1)[0]} from a shop",
                         "Capture a base after taking damage from its cannon",
                         "Win a wild monster encounter without dealing damage to the monster(s)",
                         "Fail to recruit a wild monster",
                         "Win a mission without capturing the opponent's main base",
                         f"Lose a mission via {random.sample(lose_conditions,1)[0]}",
                         f"Have exactly {random.sample(funny_numbers,1)[0]} Gold at some point in the game",
                         "Win a mission with 8 enemy marshalls using only your main character",
                         "Attack a Air and Ground cannon-defended base with a Swimming monster",
                         "Have the enemy take four turns at any point before you move again",
                         "Attack the enemy four turns before they get another turn",
                         "Use a team with only beam attackers in a mission",
                         "Use a team with only physical attackers in a mission",
                         "Have all 8 marshall teams deliver a killing blow to an enemy team",
                         "Have 5+ marshalls kill a team after encountering with full health",
                         "Kill a team with all unlockable marshalls in the campaign at least once in the playthrough",
                         "Attack an occupied enemy base with a marshall with only one monster",
                         "Fight 20 respawns over the course of this game",
                         "Use the money cheat when you already have over 30,000 gold",
                         "Build a Watch Tower",
                         "Build a healer at a base and don't use it for the rest of the mission",
                         "Follow a developer-intended pathway at least halfway across a map",
                         f"Use a Level {random.randint(1, 5)} magic spell",
                         "Use magic attacks from at least three unique levels"
                         "Fight an enemy on the bridge terrain",
                         "Miss the enemy 5 times in a single battle",
                         "Wait 10 times after an enemy has run out of AP.",
                         "Defeat a monster based on an animal in real life.",
                         f"Defeat a {random.sample(monster_types,1)[0]} monster with a {random.sample(monster_types,1)[0]} monster.",
                         "Beat a mission with the first letters of each monster's name on the team spelling a word",
                         "Buy 30 copies of one item in a shop",
                         "Cause damage to your own monster with item or monster ability",
                         "Build every equip type at one base",
                         "Revive the same monster three times",
                         "Three monsters on the same team with the same orb color.",
                         f"Level up a monster to level {random.randint(30, 45)}",
                         "Defeat a Lv. 99 Monster",
                         "Use a team with three swimming monsters to capture the enemy base",
                         "Capture 25 Neutral Bases",
                         "Use a Z-ability",
                         "Escape a battle on your final turn.",
                         "Allow the clock to rotate 12 hours",
                         "Finish a mission at 4:20 on the game clock",
                         "Allow one team to be killed by three unique marshalls",
                         "Defeat a fusion monster in battle",
                         "Have an enemy run out of Blue Medicines",
                         "Fight the enemy in at least 7 different terrains",
                         "Land the killing blow to a monster with over 1000HP with a monster with less than 600 HP",
                         "Buff an enemy monster"
                         ]

randomizer_question_list = ["Make an entire team out of Fusion monsters",
                            ]
yugi_question_list = ["Beat 'Refugees' without running away",
                      "Wait for Mai to show up in 'Crucial Battle'",
                      "Fight the tutorial soldier battle in 'War Campaign'",
                      "Wait for the trap to be set in 'Strategy'",
                      ]

kaiba_question_list = ["Beat 'Going the Distance' by survival"]

#campaign = input("Which campaign? ").title()
if campaign == "Yugi":
    bingo_list = generic_question_list + yugi_question_list
elif campaign == "Kaiba":
    bingo_list = generic_question_list + kaiba_question_list
elif campaign == "Joey":
    bingo_list = generic_question_list
else:
    print("Invalid")

bingo_list = random.sample(generic_question_list,25)
bingo_json = []
for item in bingo_list:
    bingo_json.append({'name':item})

print (json.dumps(bingo_json, indent=1))

#print (bingo_list)
monster_catch = """
for line in f:
    print (line)

for item in monster_list:
    print (item)
"""
