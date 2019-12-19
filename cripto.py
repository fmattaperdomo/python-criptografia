import sys

KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'L': '2',
    'M': '9',
    'N': 'A',
    'O': '5',
    'P': '4',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
}

def cypher(message):
    words = message.split(' ')
    cipher_message = []
    for word in words:
        cipher_word = ''
        for letter in word:
            cipher_word += KEYS[letter]
        
        cipher_message.append(cipher_word)
    
    return ' '.join(cipher_message)

def decipher(message):
    words = message.split(' ')
    decipher_message = []
    for word in words:
        decipher_word = ''
        for letter in word:
            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key
        
        decipher_message.append(decipher_word)
    
    return ' '.join(decipher_message)

def run():
    while True:
        command = str(input('''
            -------------------------------------------------
            C R I P T O G R A F I A
            -------------------------------------------------
            [c]ifrar mensaje
            [d]escifrar mensaje
            [s]alir

            Seleccione una opcion: 
        '''))
        if command == 'c':
            message = str (input("Escribe tu mensaje a cifrar: "))
            cypher_message = cypher(message)
            print(cypher_message)
        elif command == 'd':
            message = str (input("Escribe tu mensaje cifrado: "))
            decipher_message = decipher(message)
            print(decipher_message)
        elif command == 's':
            sys.exit()
        else:
            print('Opción no encontrada!!')

if __name__ == '__main__':
    run()

