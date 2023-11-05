import random
from kivy.graphics import Color, Rectangle

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


words = ['Каришка','Алиса','Вася','Буся','Тильда','Мария ду Соккору','Розана','Бразилия','Густаву Лима',
         'Бильбо Бэггинс','Сом']



class NewsApp(App):

    def random_choice(self, instance):
        new_text = f'{str(instance.text)}: {random.choice(words)}'
        # print(new_text)
        self.screen.text = new_text

    def build(self):


        bl = BoxLayout(orientation='vertical')

        with bl.canvas.before:
            Color(1, 1, 0, .25)  # green; colors range from 0-1 instead of 0-255
            self.rect = Rectangle(size=[9000, 9000],
                                  pos=bl.pos)

        self.screen = Label(text='Здесь будут появляться новости', color = [1, 0, 0, 1], font_size = 30)
        choice = GridLayout(cols=3, spacing = [9, 9], padding = 15)
        but1 = Button(text='Кто сегодня хорошо покушает', on_press = self.random_choice)
        but2 = Button(text='Кто сегодня выспится', on_press = self.random_choice)
        but3 = Button(text='Кто сегодня развлечётся', on_press = self.random_choice)
        but4 = Button(text='Кому придётся поработать', on_press = self.random_choice)
        but5 = Button(text='Кто будет мыть посуду', on_press = self.random_choice)
        but6 = Button(text='Кому идти в магазин', on_press = self.random_choice)

        choice.add_widget(but1)
        choice.add_widget(but2)
        choice.add_widget(but3)
        choice.add_widget(but4)
        choice.add_widget(but5)
        choice.add_widget(but6)

        bl.add_widget(self.screen)
        bl.add_widget(choice)







        return bl

if __name__ == "__main__":
    NewsApp().run()
