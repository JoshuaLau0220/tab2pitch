🎸 A very, very primitive tab-to-pitch converter.

# Usage

Just run `python3 tab2pitch.py` and enter the tab positions you want to convert. You may use 'x' for muted strings.
The program will output the corresponding pitches.

Supply the `-c|--capo` option to specify a capo position. The program will then output the corresponding pitches.
Negative capo positions are allowed to indicate dropped tunings.

If you have any suggestions, please file an issue or a pull request.

## Example 1: The good old C major chord

```bash
$ python3 tab2pitch.py 0 1 0 2 3 x

# output:
Pitches:
  E4
  C4
  G3
  E3
  C3
  x
```

## Example 2: Some chord with a capo

```bash
$ python3 tab2pitch.py --capo 1 x 6 7 7 x 6

# output:
Pitches:
  x
  F#4
  Eb4
  Bb3
  x
  B2
```

# License

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png)](http://creativecommons.org/publicdomain/zero/1.0/)

🆓 The author [Mu-Te Joshua Lau](https://github.com/JoshuaLau0220?tab=repositories) waives all rights to this work and places it in the public domain to the maximum extent permitted by law.
This work is provided "as is", without any warranty of any kind.
