# -*- coding: utf-8 -*-
# Функция для выбора голоса #
import g4f
from g4f.Provider import (
HuggingChat,
#Сюда добавлять модели с g4f через запятую
)

model = HuggingChat #Выбираем модель нейросети


def voice_settings():
    voice_number = 3 # Измените этот параметр для смены голоса
    return voice_number

def voice_noise():
    noise = 5 # Регулирование уровня окружающего шума (Влияет на скорость и на качество распознования голоса)
    return noise


# Выполнение комманд #
def func(voice_input):
    try:
        #----Анализатор команды----# (Если вы хотите обработать какую-то свою команду пропишите сюда что надо узнать и что вывести)
        response = g4f.ChatCompletion.create(model=g4f.models.default,
                                        messages=[{"role": "user", "content": f'проанализируй текст и выведи в ответ только 1 слово, если человек просит узнать погоду выведи pogoda, если человек хочет узнать время выведи time, если в тексте есть слово загуглить выведи google, если человек просит открыть какуюто программу выведи prog, если человек хочет включить или послушать музыку выведи musik, если человек хочет помотреть ютуб выведи youtube, если ничего из списка не найдено выведи ant: {voice_input}'}],
                                        provider=model,
                                        auth=False)
        #----Анализатор команды----#

        #----Выполнение комманды time----#
        if response == 'time':
            import datetime
            '''43469e4fc908c9dbee08db97cd5660b4'''

            current_time = datetime.datetime.now().time()
            a=''
            for i in str(current_time):
                if str(i) == '.':
                    break
                else:
                    a+=str(i)
            print(current_time)
            output = f'Сейчас {a}'
            return output
        #----Выполнение комманды time----#

        #----Выполнение комманды pogoda----#
        if response == 'pogoda':
            response = g4f.ChatCompletion.create(model=g4f.models.default,

                                        messages=[{"role": "user", "content": f'проанализируй текст и выведи в ответ только название города: {voice_input}'}],
                                        provider=model,
                                        auth=False)
            import requests
            city = response
            url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=43469e4fc908c9dbee08db97cd5660b4'
            weather_data = requests.get(url).json()
            temperature = round(weather_data['main']['temp'])

            a = 'Сейчас в городе', city, str(temperature), '°C'
            return a       
        #----Выполнение комманды pogoda----#
         
        #----Выполнение комманды google---#    
        elif response == 'google':
            response = g4f.ChatCompletion.create(model=g4f.models.default,

                                        messages=[{"role": "user", "content": f'выведи только то что хочет загуглить человек: {voice_input}'}],
                                        provider=model,
                                        auth=True)
            import webbrowser
            a = response.replace(' ', '+')
            url =f'https://www.google.com/search?q={a}'
            webbrowser.open(url, new=0, autoraise=True)
            a = f'Открыла гугл с запросом:  {response}'
            return a
        #----Выполнение комманды google---#  

        #----Выполнение комманды musik---#  
        elif response == 'musik':
            import webbrowser
            url ='https://music.yandex.ru/home'
            a = f'Открываю Яндекс музыка'
            webbrowser.open(url, new=0, autoraise=True)
            return a
        #----Выполнение комманды musik---#

        #----Выполнение комманды youtube---#
        elif response == 'youtube':
            import webbrowser
            a = f'Открываю Youtube'
            url ='https://www.youtube.com/watch?v=wjI_iJyjiU8'
            webbrowser.open(url, new=0, autoraise=True)
            return a
        #----Выполнение комманды youtube---#

        #----Выполнение комманды ant---#
        elif response == 'ant':
            response = g4f.ChatCompletion.create(model=g4f.models.default,

                                        messages=[{"role": "user", "content": f'{voice_input}'}],
                                        provider=model,
                                        auth=False)
            print(response)
            a = response.replace('*','')
            return a
        #----Выполнение комманды ant---#

        

        """
        Если вы вписали свою команду в анализатор, то ваша функция должна выглядеть так:
        а = слово которое должен вывести анализатор на вашу комманду
        elif response == а:
            Ваш код тут...
        
            
        Если ваша команда не требует анализа, то ваша функция выглядит так:
        а = 'то что должен сказать человек для активации вашей функции'
        elif voice_input == а:
            Ваш код тут...
        """


    except:
        a = 'Ошибка запроса!'
        return a