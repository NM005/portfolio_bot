import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
api_token='__________insert_your_token_here____________'

bot = telebot.TeleBot('__________insert_your_token_here____________')


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id, 'Привет! Чтобы получить доступ к данным введи пароль:')


@bot.message_handler(content_types=['text'])
def autorization(message):
    if message.text == '16':
        bot.send_message(message.chat.id, 'Пароль верный!')
        buttons(message)
        #bot.register_next_step_handler(msg, buttons)
    elif message.text == 'Current PNL':
        bot.send_message(message.chat.id, f'CURRENT PNL:\n\nBTC:  {round(((current_price("bitcoin")*18.5)/648479.5-1)*100,1)}%  {round(((current_price("bitcoin")*18.5)-648479.5)/1000,3)}$\nETH:  {round(((current_price("ethereum")*214.5)/537685.7-1)*100,1)}%  {round(((current_price("ethereum")*214.5)-537685.7)/1000,3)}$\nAR:  {round(((current_price("arweave")*525)/29977.5-1)*100,1)}%  {round(((current_price("arweave")*525)-29977.5)/1000,3)}$\nAXS:  {round(((current_price("axie-infinity")*459.64)/65001.98-1)*100,1)}%  {round(((current_price("axie-infinity")*459.64)-65001.98)/1000,3)}$\nATOM:  {round(((current_price("cosmos")*1405.37)/44999.1-1)*100,1)}%  {round(((current_price("cosmos")*1405.37)-44999.1)/1000,3)}$\nFLOW:  {round(((current_price("flow")*5107.4)/64903.66-1)/1000,3)}%  {round(((current_price("flow")*5107.4)-64903.66)/1000,3)}$\nMANA:  {round(((current_price("decentraland")*4000)/19887.47-1)*100,1)}%  {round(((current_price("decentraland")*4000)-19887.47)/1000,3)}$\nNEAR:  {round(((current_price("near")*3959.5)/44875.42-1)*100,1)}%  {round(((current_price("near")*3959.5)-44875.42)/1000,3)}$\nSAND:  {round(((current_price("the-sandbox")*4050)/30253.5-1)*100,1)}%  {round(((current_price("the-sandbox")*4050)-30253.5)/1000,3)}$\nSOL:  {round(((current_price("solana")*153.75)/29966.39-1)*100,1)}%  {round(((current_price("solana")*153.75)-29966.39)/1000,3)}$\nDOT:  {round(((current_price("polkadot")*880)/40612-1)*100,1)}%  {round(((current_price("polkadot")*880)-40612)/1000,3)}$\nDOGE:  {round(((current_price("dogecoin")*150000)/38940-1)*100,1)}%  {round(((current_price("dogecoin")*150000)-38940)/1000,3)}$\nMATIC:  {round(((current_price("matic-network")*23117.57)/40299.35-1)*100,1)}%  {round(((current_price("matic-network")*23117.57)-40299.35)/1000,3)}$\nXRP:  {round(((current_price("ripple")*32400)/40396.86-1)*100,1)}%  {round(((current_price("ripple")*32400)-40396.86)/1000,3)}$\nPOLS:  {round(((current_price("polkastarter")*10026)/22157.46-1)*100,1)}%  {round(((current_price("polkastarter")*10026)-22157.46)/1000,3)}$\nRAY:  {round(((current_price("raydium")*1547.78)/3467.03-1)*100,1)}%  {round(((current_price("raydium")*1547.78)-3467.03)/1000,3)}$\nTON:  {round(((current_price("the-open-network")*172550)/256040.53-1)*100,1)}%,  {round(((current_price("the-open-network")*172550)-256040.53)/1000,3)}$')
    elif message.text == 'Price Comparison':
        bot.send_message(message.chat.id, f'PRICE: curren VS entry\n\nBTC:  {round(current_price("bitcoin")/1000,3)}$ vs {35.052}$\nETH:  {round(current_price("ethereum")/1000,3)}$ vs {2.506}$\nAR:  {current_price("arweave")}$ vs {57.1}$\nAXS:  {current_price("axie-infinity")}$ vs {141.4}$\nATOM:  {current_price("cosmos")}$ vs {32.02}$\nFLOW:  {current_price("flow")}$ vs {12.71}$\nMANA:  {current_price("decentraland")}$ vs {4.97}$\nNEAR:  {current_price("near")}$ vs {11.33}$\nSAND:  {current_price("the-sandbox")}$ vs {7.47}$\nSOL:  {current_price("solana")}$ vs {194.9}$\nDOT:  {current_price("polkadot")}$ vs {46.15}$\nDOGE:  {current_price("dogecoin")}$ vs {0.26}$\nMATIC:  {current_price("matic-network")}$ vs {1.74}$\nXRP:  {current_price("ripple")}$ vs {1.25}$\nPOLS:  {current_price("polkastarter")}$ vs {2.21}$\nRAY:  {current_price("raydium")}$ vs {2.24}$\nTON:  {current_price("the-open-network")}$ vs {1.48}$')
    elif message.text == 'Position Value':
        bot.send_message(message.chat.id, f'POSITION: curren VS entry\n\nBTC:  {round(current_price("bitcoin")/1000*18.5,3)}$ vs {648.479}$\nETH:  {round(current_price("ethereum")/1000*214.5,3)}$ vs {537.685}$\nAR:  {round(current_price("arweave")*525/1000,3)}$ vs {29.977}$\nAXS:  {round(current_price("axie-infinity")*459.64/1000,3)}$ vs {65.002}$\nATOM:  {round(current_price("cosmos")*1405/1000,3)}$ vs {44.999}$\nFLOW:  {round(current_price("flow")*5107.4/1000,3)}$ vs {64.903}$\nMANA:  {round(current_price("decentraland")*4000/1000,3)}$ vs {19.887}$\nNEAR:  {round(current_price("near")*3959/1000,3)}$ vs {44.875}$\nSAND:  {round(current_price("the-sandbox")*4050/1000,3)}$ vs {30.253}$\nSOL:  {round(current_price("solana")*153.75/1000,3)}$ vs {29.966}$\nDOT:  {round(current_price("polkadot")*880/1000,3)}$ vs {40.612}$\nDOGE:  {round(current_price("dogecoin")*150000/1000,3)}$ vs {38.941}$\nMATIC:  {round(current_price("matic-network")*23117.57/1000,3)}$ vs {40.299}$\nXRP:  {round(current_price("ripple")*32400/1000,3)}$ vs {40.396}$\nPOLS:  {round(current_price("polkastarter")*10026/1000,3)}$ vs {22.157}$\nRAY:  {round(current_price("raydium")*1547.78/1000,3)}$ vs {3.467}$\nTON:  {round(current_price("the-open-network")*172550.09/1000,3)}$ vs {256.041}$')
    elif message.text == 'Total Performace':
        cur_pos = round((current_price("bitcoin")*18.5 + current_price("ethereum")*214.5 + current_price("arweave")*525 + current_price("axie-infinity")*459.64 + current_price("cosmos")*1405.37 + current_price("flow")*5107.4 + current_price("decentraland")*4000 + current_price("near")*3959.5 + current_price("the-sandbox")*4050 + current_price("solana")*153.75 + current_price("polkadot")*880 + current_price("dogecoin")*150000 + current_price("matic-network")*23117.57 + current_price("ripple")*32400 + current_price("polkastarter")*10026 + current_price("raydium")*1547.78 + current_price("the-open-network")*172550)/1000,3)
        bot.send_message(message.chat.id, f'TOTAL Performance:\n\nTotal Investments: {1957.943}$\nCurrent Position:  {cur_pos}$\n\nRETURN: {round(cur_pos - 1957.943,3)}$  {round((cur_pos/1957.943-1)*100,2)}%')
    elif message.text == 'Exit':
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Всего хорошего! Если хочешь войти снова нажми /start', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, 'Пароль неверен!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def buttons(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Current PNL')
    item2 = types.KeyboardButton('Price Comparison')
    item3 = types.KeyboardButton('Position Value')
    item4 = types.KeyboardButton('Total Performace')
    item5 = types.KeyboardButton('Exit')
    markup.add(item1, item2, item3, item4, item5)
    bot.send_message(message.chat.id, 'Какие данные ты хочешь посмотреть?', reply_markup=markup)


def current_price(name):
    data = cg.get_price(ids=name,  vs_currencies='usd')
    for price in data.values():
        for price in price.values():
            return price


if __name__ == "__main__":
    bot.polling(none_stop=True)
