import argparse
import sys

import requests

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('--owner', type=str, help='логин пользователя')
arg_parser.add_argument('--playlist_id', type=str, help='id плейлиста (https://music.yandex.ru/users/<owner>/playlists/<playlist_id>)')
arg_parser.add_argument('--output_file', type=str)

if __name__ == '__main__':
    args = arg_parser.parse_args(sys.argv[1:])
    res = requests.get(
        f'https://music.yandex.ru/handlers/playlist.jsx?owner='
        f'{args.owner}&kinds={args.playlist_id}'
    )

    tracks = res.json()['playlist']['tracks']
    with open(args.output_file, 'w') as f:
        for track in tracks:
            title = track['title']
            artists = [artist['name'] for artist in track['artists']]
            f.write(f'{title} {", ".join(artists)}\n')
