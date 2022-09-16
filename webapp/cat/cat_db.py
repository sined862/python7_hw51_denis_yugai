from random import randint

class CatDb:
    stats = {
        'name': 'No name',
        'age': 1,
        'happiness': 10,
        'satiety': 10,
        'state': 'sleep',
        'img': 'media/pleased.jpg'
    }

    @staticmethod
    def edit(name):
        CatDb.stats['name'] = name


    @staticmethod
    def get_img(happiness):
        if CatDb.stats['state'] != 'sleep':
            if 0 < happiness <= 10:
                img = 'media/scared.jpg'
                CatDb.stats['img'] = img
            elif 10 < happiness <= 20:
                img = 'media/neutral.jpg'
                CatDb.stats['img'] = img
            elif 20 < happiness <= 40:
                img = 'media/pleased.jpg'
                CatDb.stats['img'] = img
            elif happiness >= 40:
                img = 'media/confused.jpg'
                CatDb.stats['img'] = img
            elif happiness <= 0:
                img = 'media/angry.jpg'
                CatDb.stats['img'] = img
        else:
            img = 'media/pleased.jpg'
            CatDb.stats['img'] = img


    @staticmethod
    def actions(action):
        if action == '1':
            if CatDb.stats['state'] == 'sleep':
                CatDb.stats['state'] = 'awake'
                CatDb.stats['happiness'] -= 5
            else: 
                random = randint(1,3)
                if random != 1:
                    CatDb.stats['happiness'] += 15
                    CatDb.stats['satiety'] -= 10
                else:
                    if CatDb.stats['happiness'] > 0:
                        CatDb.stats['happiness'] = 0
        elif action == '2':
            if CatDb.stats['satiety'] < 50:
                if CatDb.stats['state'] == 'awake':
                    CatDb.stats['satiety'] += 15
                    CatDb.stats['happiness'] += 5
            else:
                CatDb.stats['happiness'] -= 30
        elif action == '3':
            if CatDb.stats['state'] == 'awake':
                CatDb.stats['state'] = 'sleep'


