import math

txt = 'The quick brown fox jumps over the lazy dog.'
bio = ''

def bold(word):
    bold_num = math.ceil(len(word)/2)
    if bold_num == 1:
        bold_num += 1
    return '\033[1m' + word[0:bold_num] + '\033[0m' + word[bold_num:]


for i in txt.split(' '):
    bio += bold(i) + ' '

print(bio)