def warn_the_sheep(queue):  #Maja
    rew=queue[::-1]
    if rew[0]=='wolf':
        call='Pls go away and stop eating my sheep'
    else:
        n=rew.index('wolf')
        call=f'Oi! Sheep number {n}! You are about to be eaten by a wolf!'
    return call
#################################################################################
def warn_the_sheep(queue):
    n = len(queue) - queue.index('wolf') - 1
    return f'Oi! Sheep number {n}! You are about to be eaten by a wolf!' if n else 'Pls go away and stop eating my sheep'
#####################################################################
def warn_the_sheep(queue):
    i = queue[::-1].index('wolf')
    if i == 0:
        return 'Pls go away and stop eating my sheep'
    return f'Oi! Sheep number {i}! You are about to be eaten by a wolf!'
##########################################################################
def warn_the_sheep(queue):
    queue.reverse()
    return 'Pls go away and stop eating my sheep' if queue[0] == 'wolf' else 'Oi! Sheep number {}! You are about to be eaten by a wolf!'.format(queue.index('wolf'))
######################################################################


print(warn_the_sheep(['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep'])) # 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
print(warn_the_sheep(['sheep', 'sheep', 'wolf']))  # 'Pls go away and stop eating my sheep')


# (['sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'wolf', 'sheep', 'sheep']), 'Oi! Sheep number 2! You are about to be eaten by a wolf!')
# (['sheep', 'wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 5! You are about to be eaten by a wolf!')
# (['wolf', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep', 'sheep']), 'Oi! Sheep number 6! You are about to be eaten by a wolf!')
# (['sheep', 'wolf', 'sheep']), 'Oi! Sheep number 1! You are about to be eaten by a wolf!')
# (['sheep', 'sheep', 'wolf']), 'Pls go away and stop eating my sheep')

