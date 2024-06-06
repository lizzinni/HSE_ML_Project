# Flood probability prediction

Link to the [presentation](https://docs.google.com/presentation/d/1IcRXBWVmZpbf1igzLZHawVQNMQRx6YYTc-NasQF55ms/edit?usp=sharing)

To predict flood probability we used this [dataset](https://www.kaggle.com/competitions/playground-series-s4e5/data?select=train.csv)

Instructions to Run the Bot:
```shell
git clone <repository_url>
cd <repository_directory>
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN='your_telegram_bot_token'
cd bot
python tgbot.py
```

In file `model/flood_model.cbm` we have a fitted CatBoostRegressor

All notebooks are in `notebooks/`
