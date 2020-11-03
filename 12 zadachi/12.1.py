def mood_today(mood:str):
    if mood == 'happy':
        return f'today, i am feeling {mood}'
    elif mood == 'sad':
        return f'today, i am feeling {mood}'
    else:
        f'today, i am feeling neitral'
print(mood_today('happy'))