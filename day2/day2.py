score = 0
score2 = 0

outcomes = {
    'A': { # Rock
        'X': 1 + 3,# Rock
        'Y': 2 + 6,# Paper
        'Z': 3 + 0,# Scissor
    },
    'B': { # Paper
        'X': 1 + 0,# Rock
        'Y': 2 + 3,# Paper
        'Z': 3 + 6,# Scissor
    },
    'C': { # Scissor
        'X': 1 + 6,# Rock
        'Y': 2 + 0,# Paper
        'Z': 3 + 3,# Scissor
    }
}
outcomes2 =  {
    'A': { # Rock
        'X': 3 + 0,# Lose scissors
        'Y': 1 + 3,# Draw rock
        'Z': 2 + 6,# Win paper
    },
    'B': { # Paper
        'X': 1 + 0,# Lose rock
        'Y': 2 + 3,# Draw paper
        'Z': 3 + 6,# Win scissors
    },
    'C': { # Scissor
        'X': 2 + 0,# Lose paper
        'Y': 3 + 3,# Draw scissors
        'Z': 1 + 6,# Win rock
    }
}

with open('./input') as fp:
    for line in fp:
        data = line.split()
        score += outcomes[data[0]][data[1]]
        score2 += outcomes2[data[0]][data[1]]

print("part 1: "+ str(score))
print("part 1: "+ str(score2))