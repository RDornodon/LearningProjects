from random import choice,shuffle
import argparse


def get_random_password(*, charsets, length=16):
    if len(charsets) > length:
        raise ValueError('Password length set to low, could not choose from all charsets.')
    pw = [choice(cs) for cs in charsets]
    ap = []
    [ap.extend(cs)for cs in charsets]
    pw += [choice(ap) for _ in range(len(pw), length)]
    shuffle(pw)
    return ''.join(pw)


def charset_descriptions():
   return """
Available charsets: 
   lower           - all lowercase alphabets
   upper           - all uppercase alphabets
   number          - numbers from 0 to 9
   special         - most common special characters
"""

if __name__ == '__main__':
    available_charsets = {
        'lower': 'abcdefghijklmnopqrstuvwxyz',
        'upper': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'number': '0123456789',
        'special': '§'"+!%/=()~^`\\|[]$<>#&@{};*,.-?:_"}
    parser = argparse.ArgumentParser(
                        description='Generate random password. '
                                    'The password contains at least one character from each charsets.')
    parser.add_argument('--length', type=int, default=16, help='default length is 16')
    cs_group = parser.add_mutually_exclusive_group()
    cs_group.add_argument('--charsets', '-c', nargs='+',
                          metavar='',
                          choices=available_charsets,
                          default=available_charsets,
                          help='by default all charsets are used from: [lower,upper,number,special]')
    cs_group.add_argument('--charset_file', '-f', type=argparse.FileType('r'),metavar='FILE',
                          help='provide a file with each mandatory character sets in a separate line')
    args = parser.parse_args()

    try:
        if args.charset_file:
            active_charset = args.charset_file.readlines()
        else:
            active_charset = [v for k, v in available_charsets.items() if k in args.charsets]
        print(get_random_password(charsets=active_charset, length=args.length))
    except ValueError as e:
        print(e)
