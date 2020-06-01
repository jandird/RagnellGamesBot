import store_token
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

question_cards = [
    'Hide! \n'
    'The team that draws this card has 20 seconds to hide. The other three teams must seek. The seekers have '
    'two minutes to find the hider. First seeking team to find hider wins 100 bells. If hider is not found after '
    'one minute the hiding team wins 200 bells',

    'Seek! \n'
    'The team that draws this card must give all other teams 20 seconds to hide. The team then has 2 minutes to seek '
    'for every team. Every time a player on an opposing team is caught they can also begin to seek, and deny the team '
    'that drew this card bells. Each hiding team to not be found wins 100 bells. The seeking team wins 100 bells for '
    'each team found.',

    'Death Hop! \n'
    'Make your way to death hop!',

    'Clam Rush \n'
    'All teams must go hunt manila clams. The first team to collect two clams wins 200 bells',

    'Roll Again \n'
    '... roll again.',

    'Swap! \n'
    'The team that draws this card has the option to switch spots with any other team. However, if you choose to swap '
    'you must play off of that new location.',

    'Villager Hunt! \n'
    'All teams must search for a randomly chosen villager. First team to find the chosen villager wins 200 bells. '
    'Teams may choose to guess that the villager is at home, and if they are correct they are awarded 100 bells',

    'Hole Vaulting \n'
    'The team who drew this card must do 1 round of hole vaulting. Each opposing team gets to dig 1 hole. If the '
    'vaulting team lands in one of the holes the respective team wins 200 bells. Otherwise the vaulting team wins '
    '200 bells. ',

    'Shake it Off \n'
    'Each team must pick a tree at the orchard. Each team takes turns shaking their tree until a team receives a '
    'branch. The winning team(s) wins 100 bells. Note: Each team gets equal shakes and there can be multiple winners.',
    
    'Biggest Catch \n'
    'Each team has one minute to catch a single fish. The team with the most valuable fish wins 200 bells.'
]

star_cards = [
    # Hold On Cards
    '+1-3 \n'
    'Keep this card! On a future roll this card will allow you to add between 1-3 to your roll.',
    
    'Sabotage! \n'
    'Keep this card! During a future 1v1 of either fishing for bug catching you are allowed to choose one of the teams '
    'and follow them to try and steal their catches. Note: You are not allowed to scare away the fish or critters and '
    'doing so will result in having to pay the opponent 100 bells.',
    
    'Alchemy! \n'
    'Keep this card! If you receive a material when digging, you can use this cards to turn its negative value into an '
    'equivalent positive value.',

    'Reverse Stomp \n'
    'Keep this card! If an opponent lands on you to send you home, you can use this card to send them home and steal '
    '100 from them instead.',

    # Normal Cards
    'Planted Flowers \n'
    'You took the time to plant and tend to your flowers. Receive 100 bells.',

    'Visited Neighbours \n'
    'You took the time to visit and check up on your neighbours. Receive 200 bells.',

    'Payed off Mortgage \n'
    'Congrats! You have officially payed off your mortgage. Receive 300 bells.',

    'Steal 100 \n'
    'You\'re a snake, steal 100 bells from the player of your choice.',

    'Steal 200 \n'
    'You\'re a huge snake, steal 200 bells from the player of your choice.',

    'High Turnip Prices \n'
    'You have huge turnip prices, everyone wants to sell! Take 100 bells from each opponent.',

    'Home Run! \n'
    'Go straight home. Collect 100 bells and an additional 100 bells for every opponent you pass.',

    'Questioning Thief \n'
    'You have become the questioning thief. If you ask a question and an opponent answers it, you steal 100 bells from '
    'them. You only use this power on each opponent once, and you lose this power at the beginning of your next turn.'
]

death_cards = [
    # Hold on Cards
    'Bad Eye \n'
    'Keep this card! If you receive a material when digging lose an additional 100 bells. If you receive bells discard '
    'this card.',

    # Normal Cards
    'Caught a Sea Bass \n'
    'Should have caught a C+ Bass. Lose 100 Bells',

    'Stung by Wasps \n'
    'Your villagers are now roasting you. Lose 200 Bells',

    'Killed by Tarantula \n'
    'You managed to be bad at Animal Crossing. Lose 300 Bells',

    'Infamous Lumberjack \n'
    'You got caught cutting down your friends trees. Pay each opposing team 100 Bells',

    'Death Roll! \n'
    'Roll the dice. You lose 400 - 100*(Roll_Value). Negative value means you lose nothing',

    'Corrupt \n'
    'This card is corrupt. You lose nothing. Congrats.',

    'Wicked Hole Vaulting \n'
    'The team that drew this card must do 1 round of hole vaulting. The opposing teams get to dig 2 holes. If the '
    'vaulting team lands in one of the holes, they must pay each of opposing teams 100 bells',

    'Hide or Die \n'
    'The team that drew this card must have a player hide. The player has 20 seconds to hide. The opposing teams have '
    'one minute to seek. If the hiding player is found the hiding team must 100 bells to the team that found them.',

    'Where is the Villager? \n'
    'The team that drew this card must guess if a villager is at home or outside. If the guess is incorrect they lose '
    '200 bells.',
    
    'Minefield! \n'
    'The team that drew this card must try standing on one of the pitfall locations. If they fall in they lose 200 '
    'bells. However if they do not fall in they can dig that spot up and take their prize.'
]

villagers = [
    'Marshall - White Squirrel',
    'Tank - Blue Rhino',
    'Phil - Blue Ostrich',
    'Reneigh - Brown Horse',
    'Ken - Black Chicken',
    'Dizzy - Blue Elephant',
    'Keaton - Yellow Eagle',
    'Bianca - White Tiger',
    'Bangle - Brown Tiger'
]

questions = []
stars = []
deaths = []


@bot.event
async def on_ready():
    global question_cards, questions, death_cards, deaths, star_cards, stars

    questions = list(question_cards)
    stars = list(star_cards)
    deaths = list(death_cards)

    print("Bot is Ready")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def rules(ctx):
    await ctx.send('Welcome to the Ragnell Games, thank you for playing! \n \n'
                   'Objective: Be the first team to fill your coin field with 16 coins. \n'
                   'Turns: Each team takes turns rolling the die, and moves the number of spaces specified by the die. '
                   'The following things can occur after moving. \n'
                   '\t - Land on Fish / Caterpie: 1v1 Fishing / Bug Catching tournament. The moving team has 3 options:'
                   '\n'
                   '\t \t - Win 100. Face the team directly in front of you. \n'
                   '\t \t - Win 200. Face the team directly in front of you. However if you lose the opposing team '
                   'wins 100. \n'
                   '\t \t - Steal 200. Face any team of your choosing. If you win you steal 200 from the opposing '
                   'team. If you lose the opposing team steals 100 from you. \n'
                   '\t - Land on Shovel: Dig 1 area from the dig sites. If you get bells you win the respective '
                   'amount. If you get a material you lose the following amounts: Stone - 100, Clay - 200, Iron - 300.'
                   '\n'
                   '\t - Land on Question: Draw a question card (!q) \n'
                   '\t - Land on Star: Draw a star card (!s) \n'
                   '\t - Land on Death: Draw a death card (!d) \n'
                   '\t - Pass Home: Gain 100 \n'
                   '\t - Land on Home: Gain 200 \n'
                   '\t - Land on Opposing Team Home: Opposing team steals 100 \n'
                   '\t - Land on Opposing Team (STOMP): Send opposing team home and steal 100. Play off landed square. '
                   '\n'
                   'Note: When opponents are fishing or catching bugs you are allowed to follow. However you cannot '
                   'catch or scare anything away. If this occurs: Direct Opponent - Forfeit Round, Indirect Opponent - '
                   'Give up 100 to opponent'
                   '\n MOST IMPORTANT RULE: Have Fun :)')


@bot.command()
async def r(ctx):
    await ctx.send(random.randint(1, 6))


@bot.command()
async def q(ctx):
    global questions, question_cards
    if len(questions) == 0:
        questions = list(question_cards)

    card = random.choice(questions)
    questions.remove(card)
    await ctx.send(card)


@bot.command()
async def s(ctx):
    global stars, star_cards
    if len(stars) == 0:
        stars = list(star_cards)

    card = random.choice(stars)
    stars.remove(card)
    await ctx.send(card)


@bot.command()
async def d(ctx):
    global deaths, death_cards
    if len(deaths) == 0:
        deaths = list(death_cards)

    card = random.choice(deaths)
    deaths.remove(card)
    await ctx.send(card)


@bot.command()
async def villager(ctx):
    animal = random.choice(villagers)
    await ctx.send(animal)


@bot.command()
async def missmyex(ctx):
    await ctx.send("It's okay Andrew, you're the best, I love you <3")


@bot.command()
async def anime(ctx):
    animes = ["AOT", "MHA", "DN"]
    await ctx.send(random.choice(animes))

bot.run(store_token.get_token())
