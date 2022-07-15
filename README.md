# telegram-flooder

## Disclaimer
This project was created only for educational purposes and without any warranty. Use it at your own risk and respecting others. 

## Generate telegram config codes
Generate `app_id` and `app_hash` codes visiting `https://my.telegram.org/apps`.

## Use generated codes 
You can put generated codes in `config.json` like in the following example:
```python
api_id = '12679118'
api_hash = '07e16677bf054aa454f31b37e5f81cd1'
phone = '393204956075'
```
If you are interested to run the script using docker create instead a `.env` file like in the following example:
```shell
TELEGRAM_FLOODER_API_ID=12679118
TELEGRAM_FLOODER_API_HASH=07e16677bf054aa454f31b37e5f81cd1
TELEGRAM_FLOODER_PHONE=393204956075
```

## Install dependencies
It is recommended to use a `virtualenv` to install dependencies:
```shell
python -m virtualenv venv
source /venv/bin/activate
```
Install dependency using `pip`
```shell
pip install -r requirements.txt
```

## Run the script
First of all, you can simply run the script without any flag to get the target `chat_id` 
```shell
python main.py
```
The command above prints chat titles and chat ids to choose a target `chat_id`.
Use the target `chat_id` to flood that chat of messages:
```shell
python main.py --chat_id {{CHAT_ID}} --text "{{TEXT}}" --repeat {{REPEAT_NUMBER}}
```

In alternative you can run the scripts using `docker-compose`
```shell
 docker-compose run app --chat_id {{CHAT_ID}} --text "{{TEXT}}" --repeat {{REPEAT_NUMBER}}
```
