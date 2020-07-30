FUNCTIONS

Building Our Own Functions
Quando você usa uma função é para você lembrar e deixar guardado, ele não vai rodar o programa

example 01.01
x=5
print('Hello')

def print_lyrics():
    print('Im a lumberjack, and Im okay')
    print('I sleep all night  and I work all day')

print('yo')
x=x+2
print(x)

OUTPUT
Hello
yo
7

------------
example 01.02
x=5
print('Hello')

def print_lyrics():
    print('I'm a lumberjack, and I'm okay')
    print('I sleep all night  and I work all day')

print('yo')
print_lyrics
x=x+2
print(x)

OUTPUT
Hello
I'm a lumberjack, and I'm okay
I sleep all night  and I work all day # o legal é que fazendo print cada linha, ai fica representado a lyric em cada linha
yo
7
