from argparse import ArgumentParser

pitch_names = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
standard_tuning = ['E4', 'B3', 'G3', 'D3', 'A2', 'E2']
def num_to_pitch(num) -> str:
    return pitch_names[num % 12] + str(num // 12 - 1)

def pitch_to_num(pitch) -> int:
    return pitch_names.index(pitch[:-1]) + (int(pitch[-1]) + 1) * 12

def tab_to_pitch(tab: list[str], capo=0) -> list[str]:
    ret = []
    if len(tab) != 6:
        raise ValueError('Tab must have 6 strings')
    for i in range(6):
        if tab[i] == 'x':
            ret.append('x ')
        else:
            ret.append(num_to_pitch(pitch_to_num(standard_tuning[i]) + int(tab[i]) + capo))
    return ret


def main():
    parser = ArgumentParser()
    parser.add_argument('tab', help='tab to convert. Type `x` to skip a string', nargs=6, metavar='pos')
    parser.add_argument('-c', '--capo', help='capo fret (default: 0)', type=int, default=0)
    

    args = parser.parse_args()

    print('Pitches:')
    print('\n'.join(list(map(lambda x: '  ' + x, tab_to_pitch(args.tab, args.capo)))))

if __name__ == '__main__':
    main()