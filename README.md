# weather_getter #

Программа запрашивает погоду в Лондоне, Череповце и аэропорте Шереметьево с сайта [wttr.in](https://wttr.in).
Полученный результат выводится в консоль.

## Установка ##
Python3 должен быть уже установлен. Затем используйте pip для установки зависимостей.
```
pip install -r requirements.txt
```

Для старта запустить файл [main.py](https://github.com/MartynMartynuk/weather_getter/blob/master/main.py).

**Результат работы программы**
```
python3 main.py
>>
Лондон

      \   /     Солнечно
       .-.      +7(6) °C       
    ― (   ) ―   ↑ 9 km/h       
       `-’      6 km           
      /   \     0.0 mm         
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 10 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│  _`/"".-.     Местами дождь  │
│  _ /"".-.     +7(6) °C       │   ,\_(   ).   +7(5) °C       │
│    \_(   ).   ↑ 6-9 km/h     │    /(___(__)  ↖ 9-14 km/h    │
│    /(___(__)  10 km          │      ‘ ‘ ‘ ‘  10 km          │
│               0.0 mm | 0%    │     ‘ ‘ ‘ ‘   0.1 mm | 70%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 11 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Дымка          │      .-.      Слабая морось  │
│  _ - _ - _ -  8 °C           │     (   ).    +7(4) °C       │
│   _ - _ - _   ↗ 5-8 km/h     │    (___(__)   ↓ 12-17 km/h   │
│  _ - _ - _ -  2 km           │     ‘ ‘ ‘ ‘   2 km           │
│               0.0 mm | 0%    │    ‘ ‘ ‘ ‘    0.2 mm | 56%   │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 12 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │     \   /     Ясно           │
│      .-.      7 °C           │      .-.      4 °C           │
│   ― (   ) ―   ↓ 4 km/h       │   ― (   ) ―   → 1-3 km/h     │
│      `-’      10 km          │      `-’      10 km          │
│     /   \     0.0 mm | 0%    │     /   \     0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Шереметьево

       .-.      Сильный снег
      (   ).    -2(-6) °C      
     (___(__)   ↖ 10 km/h      
     * * * *    2 km           
    * * * *     0.6 mm         
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 10 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│      .-.      Сильный снег   │               Пасмурно       │
│     (   ).    -3(-7) °C      │      .--.     -2(-6) °C      │
│    (___(__)   ↖ 11-14 km/h   │   .-(    ).   → 12-16 km/h   │
│    * * * *    2 km           │  (___.__)__)  10 km          │
│   * * * *     2.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 11 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Облачно        │               Пасмурно       │
│      .--.     -10(-17) °C    │      .--.     -14(-21) °C    │
│   .-(    ).   ↓ 15-21 km/h   │   .-(    ).   ↓ 15-25 km/h   │
│  (___.__)__)  10 km          │  (___.__)__)  10 km          │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 12 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│  _`/"".-.     Небольшой снег │      .-.      Сильный снег   │
│   ,\_(   ).   -13(-21) °C    │     (   ).    -10(-16) °C    │
│    /(___(__)  ↓ 16-21 km/h   │    (___(__)   ↘ 14-21 km/h   │
│      *  *  *  10 km          │    * * * *    2 km           │
│     *  *  *   0.1 mm | 0%    │   * * * *     0.4 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘

Череповец

                Дымка
   _ - _ - _ -  -12(-17) °C    
    _ - _ - _   ↓ 9 km/h       
   _ - _ - _ -  2 km           
                0.0 mm         
                        ┌─────────────┐                        
┌───────────────────────┤ Пн. 10 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│               Переохлажденны…│    \  /       Переменная обл…│
│  _ - _ - _ -  -12(-17) °C    │  _ /"".-.     -15(-23) °C    │
│   _ - _ - _   ↓ 9-16 km/h    │    \_(   ).   ↓ 14-25 km/h   │
│  _ - _ - _ -  0 km           │    /(___(__)  10 km          │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Вт. 11 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│    \  /       Переменная обл…│               Переохлажденны…│
│  _ /"".-.     -15(-23) °C    │  _ - _ - _ -  -20(-27) °C    │
│    \_(   ).   ↓ 17-26 km/h   │   _ - _ - _   ↓ 10-21 km/h   │
│    /(___(__)  10 km          │  _ - _ - _ -  0 km           │
│               0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
                        ┌─────────────┐                        
┌───────────────────────┤ Ср. 12 янв. ├───────────────────────┐
│             День      └──────┬──────┘       Ночь            │
├──────────────────────────────┼──────────────────────────────┤
│     \   /     Солнечно       │               Дымка          │
│      .-.      -18(-22) °C    │  _ - _ - _ -  -24(-28) °C    │
│   ― (   ) ―   ↓ 5-10 km/h    │   _ - _ - _   ↖ 5-10 km/h    │
│      `-’      10 km          │  _ - _ - _ -  2 km           │
│     /   \     0.0 mm | 0%    │               0.0 mm | 0%    │
└──────────────────────────────┴──────────────────────────────┘
```
