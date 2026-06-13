
#BAD

def histogram(word: str):

    chart = {}
    count = []

    for alphabet in word:
        count.append(alphabet)
        chart[alphabet] = count.count(alphabet) * '*'
    
    for key, value in chart.items():
        print(key, value)

    print(chart)

histogram('statistically')


# GOOD

def histogram(word: str):
    chart = {}

    for letter in word:

        if letter not in chart:
            chart[letter] = 1
        
        else:
            chart[letter] += 1

    for key, value in chart.items():
        print(key, value * '*')
    
histogram('mississippi')

