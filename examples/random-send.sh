#!/bin/bash

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" &>/dev/null && pwd -P)

[[ -z "$1" ]] && echo "No chat id specified" && exit 1

chat_id="$1"

while :; do
    random_word="$(curl -s 'https://raw.githubusercontent.com/napolux/paroleitaliane/master/paroleitaliane/660000_parole_italiane.txt' | shuf -n 1)"
    echo "sending ${random_word}"
    python "${script_dir}/../main.py" --chat_id "$chat_id" --text "$random_word"
    sleep 20
done
