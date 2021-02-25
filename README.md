# 3i VOX python examples

###### Install the requirements
`python3 -m pip install -r requirements.txt`

###### Generate access_token at 3i-vox.ru
Request:\
`curl -X POST "https://3i-vox.ru/oauth/token" \
  -H "Content-Type: application/json" \
  -d '{"grant_type":"password","username":"<USERNAME>","password":"<PASSWORD>","client_id":"<CLIENT_ID>","client_secret":"<CLIENT_SECRET>"}'`\
`<USERNAME>`, `<PASSWORD>` - your 3i-vox.ru login credentials.\
`<CLIENT_ID>`, `<CLIENT_SECRET>` - you can get in your account settings at 3i-vox.ru.

Response:\
`{"token_type":"Bearer","access_token":"<ACCESS_TOKEN>","scope":"vox"}`\
`<ACCESS_TOKEN>` - access token for further commands

### Run asr stream example

```
usage: 3i_vox_stream.py [-h] --model MODEL --file FILE [--only_new]
                        [--token TOKEN] [--punctuation]

optional arguments:
  -h, --help     show this help message and exit
  --model MODEL  Model name
  --file FILE    File name
  --only_new     Receive only new results
  --token TOKEN  OAuth access token
  --punctuation  Enable automatic punctuation
```

###### To receive only new chunks every request
`python3 3i_vox_stream.py --token=<ACCESS_TOKEN> --model=ru_telephony_2021.02.24_v4_8000 --file=test_stream.wav --only_new`

###### To receive all the chunks every request
`python3 3i_vox_stream.py --token=<ACCESS_TOKEN> --model=ru_telephony_2021.02.24_v4_8000 --file=test_stream.wav`
