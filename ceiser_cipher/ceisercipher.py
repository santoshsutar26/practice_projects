import art
a = art.logo
print(a)
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

conitnue = True
while conitnue:
    direction = input("type 'encode' to encrypt,type 'decode' to decrypt:\n")

    text = input('enter your message:\n').lower()
    shift = int(input('type the shift number:\n'))


    def ceiser(strt_text, shift_amout, direction):
        end_text = ''
        if direction == 'decode':
            shift_amout *= -1
        for char in strt_text:
            if char in alphabet:
                possition = alphabet.index(char)

                new_possition = possition + shift_amout
                end_text += alphabet[new_possition]
            else:
                end_text += char

        print(f'the {direction}d message is {end_text}')


    shift = shift % 26
    ceiser(strt_text=text, shift_amout=shift, direction=direction)
    result = input('type "yes" to continue, or else type "no" to end:\n')
    if result == 'no':
        conitnue = False
        print('goodbye!')




