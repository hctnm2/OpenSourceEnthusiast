import pyjokes
def get_jokes(n):
    print("Enter the language to begin with: ")
    print("Press:\n1. English\n2. Spanish\n3. Italian\n4. German\n5. Galician\n6. Basque")
    ch = int(input())
    lang = ''
    if (ch == 1):
        lang = 'en'
    elif (ch == 2):
        lang = 'es'
    elif (ch == 3):
        lang = 'it'
    elif (ch == 4):
        lang = 'de'
    elif (ch == 5):
        lang = 'gl'
    elif (ch == 6):
        lang = 'eu'
    else:
        lang = 'en'

    print("\nEnter the category of jokes:\n1. Geeky Jokes\n2. Chuck Norris Jokes\n3. All types of jokes\n4. Twister jokes but only for German Language")
    ch2 = int(input())
    cat = ''
    if (ch2 == 1):
        cat = 'neutral'
    elif (ch2 == 2):
        cat = 'chuck'
    elif (ch2 == 3):
        cat = 'all'
    elif (ch2 == 4):
        cat = 'twister'
    else:
        cat = 'neutral'

    jokes = pyjokes.get_jokes(language=lang, category=cat)
    print("\n")
    for i in range(n):
        print("{}. {}".format(i+1, jokes[i]))


print("Enter the number of jokes to display: ")
n = int(input())
get_jokes(n)

