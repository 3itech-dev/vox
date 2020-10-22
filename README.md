# 3i VOX python examples

###### Install the requirements
`python3 -m pip install -r requirements.txt`

### Run stream example

###### To receive only new chunks every request
`python3 3i_vox_stream.py --model=ru_telephony_071020_v2_8000 --file=test_stream.wav --only_new`

###### To receive all the chunks every request
`python3 3i_vox_stream.py --model=ru_telephony_071020_v2_8000 --file=test_stream.wav`
