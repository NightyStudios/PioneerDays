import time
import tkinter as tk
from PIL import Image, ImageTk
import requests
import json
from threading import Timer
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()

control = 'concentration'
global count
count = 0
global count1
count1 = 0
global count2
count2 = 0
global count3
count3 = 0
time_left = 60
time_zhar = 60
time_school = 45
global bio
bio = ""

try:
    class RepeatTimer(Timer):
        def run(self):
            while not self.finished.wait(self.interval):
                self.function(*self.args, **self.kwargs)


    def query():
        response = requests.get('http://127.0.0.1:2336/bci')
        response.raise_for_status()
        data = json.loads(response.content)
        if data['result'] is True:
            value = data[control]
            # Обновляем метку tkinter
            # Проверяем, достиг ли порог концентрации
            show_emotion(value)
            # Обновляем график
            update_plot(value)
            return value
        else:
            print("No device")


    # класс, в котором хранится история
    class VisualNovel:
        # класс инициализации, который загружается при вызове класса
        def __init__(self, root):
            self.root = root
            self.root.title("Pioneer's Days")
            self.label = tk.Label(root,
                                  text="Добро пожаловать! Выбери свой возраст. (Кстати, пока просто расслабься)",
                                  wraplength=400, font=("Arial", 24))
            self.label.pack()

            self.button1 = tk.Button(root, text="1-4 класс", command=self.younger, font=("Arial", 24))
            self.button1.pack()
            self.button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
            self.button2 = tk.Button(root, text="5-9 класс", command=self.older, font=("Arial", 24))
            self.button2.pack()
            self.button2.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
            self.label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)

        def younger(self):
            self.button2.place_forget()
            self.button2.pack_forget()
            global bio
            bio = "окружающий мир"
            self.button1.config(text="Продолжить", command=self.gameinit)

        def older(self):
            self.button2.place_forget()
            self.button2.pack_forget()
            global bio
            bio = "биология"
            self.button1.config(text="Продолжить", command=self.gameinit)

        # загрузка картинок и первое задание
        def gameinit(self):
            ultrachecking.start()
            self.bedroom_image = ImageTk.PhotoImage(Image.open("son.jpg"))
            self.kitchen_image = ImageTk.PhotoImage(Image.open("zhar.jpg"))
            self.school_image = ImageTk.PhotoImage(Image.open("school.jpg"))

            # функция для отсчета и отображения времени
            def countdown():
                value = query()
                global time_left
                if time_left > 0 and value < 80:
                    time_left -= 1

                    self.label.config(
                        text=f"Доброе утро, пионер! Твоя задача - сконцентрироваться до 80 очков, чтобы проснуться {time_left}",
                        wraplength=400, font=("Arial", 24))
                    self.label.after(1000, countdown)  # Обновление каждую секунду
                else:
                    print("no err")

            countdown()
            self.bedroom_label = tk.Label(root, image=self.bedroom_image)

            self.bedroom_label.place(rely=0.55, relx=0.5, anchor=tk.CENTER)
            self.label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.label.pack()

        # второе задание: приготовление яичницы
        def zharka(self):
            chechegg.start()
            self.bedroom_label.place_forget()
            self.kitchen_image = ImageTk.PhotoImage(Image.open("zhar.jpg"))
            self.kitchen_label = tk.Label(root, image=self.kitchen_image)
            self.kitchen_label.place(rely=0.55, relx=0.5, anchor=tk.CENTER)
            for i in range(60):
                global time_zhar
                self.label.config(
                    text=f"Отлично! Самая сложная часть пути пройдена! Теперь нужно позавтракать, как насчет яичницы? Чтобы ее приготовить нужно 90 единиц концентрации, справишься? {time_zhar}",
                    wraplength=400, font=("Arial", 24))

                time.sleep(1)
                time_zhar -= 1
            self.kitchen_label.place(rely=0.55, relx=0.5, anchor=tk.CENTER)
            self.label.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.label.pack()

        # финальное задание: школа
        def at_the_school(self):
            tortimes.start()
            global bio
            self.kitchen_label.place_forget()
            self.kitchen_label.pack_forget()
            self.label.pack_forget()
            self.label.place_forget()
            # здесь можно было бы в поле текста поставить любой, но я поставил смайлик :)
            self.bossfight = tk.Label(root,
                                      text=":)",
                                      wraplength=400, font=("Arial", 24))
            self.bossfight.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.bossfight.pack()
            self.kitchen_label.place_forget()
            self.school_image = ImageTk.PhotoImage(Image.open("school.jpg"))
            self.school_label = tk.Label(root, image=self.school_image)
            self.school_label.place(rely=0.55, relx=0.5, anchor=tk.CENTER)
            for i in range(45):
                global time_school
                self.bossfight.config(
                    text=f"Фух, вот ты и в школе. Первый предмет - {bio}. Сосредоточься до максимума (100 очков) за 45 секунд! {time_school}",
                    wraplength=400, font=("Arial", 24))

                time.sleep(1)
                time_school -= 1

        # плохая концовка
        def bad_end(self):
            self.button1.pack_forget()
            self.button1.place_forget()
            self.button2.pack_forget()
            self.button2.place_forget()
            self.kitchen_label.pack_forget()
            self.kitchen_label.place_forget()
            self.bossfight.place_forget()
            self.bossfight.pack_forget()
            self.label.place_forget()
            self.label.pack_forget()
            self.school_label.pack_forget()
            self.school_label.place_forget()
            self.bend = tk.Label(root,
                                 text="Твой день не задался: либо чуть не проспал, либо яичница слишком долго жарилась, либо учителя сложными вопросами завалили. Поэтому сейчас тебе приходится сидеть на продлёнке и делать дополнительные задания. Плохая концовка",
                                 wraplength=400, font=("Arial", 24))
            self.bend.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.bend.pack()

        # хорошая концовка
        def good_end(self):
            self.button1.pack_forget()
            self.button1.place_forget()
            self.button2.pack_forget()
            self.button2.place_forget()
            self.kitchen_label.pack_forget()
            self.kitchen_label.place_forget()
            self.bossfight.place_forget()
            self.bossfight.pack_forget()
            # self.bend.place_forget()
            # self.bend.pack_forget()
            self.label.place_forget()
            self.label.pack_forget()
            self.school_label.pack_forget()
            self.school_label.place_forget()

            self.gend = tk.Label(root,
                                 text="Вот и закончился школьный день! Ты отлично выспался, вкусно поел и заработал много пятерок в школе, поэтому теперь ты с чистой совестью идешь гулять с друзьями, спасибо за игру!",
                                 wraplength=400, font=("Arial", 24))
            self.gend.place(relx=0.5, rely=0.25, anchor=tk.CENTER)
            self.gend.pack()


    def show_emotion(value):
        # Определяем, какое изображение эмоции показывать в зависимости от значения концентрации

        emotion_images = {
            20: "emo1.png",
            40: "emo2.png",
            60: "emo3.png",
            80: "emo4.png",
            95: "emo5.png"
        }

        emotion_image_path = next((v for k, v in emotion_images.items() if value < k), "emo5.png")

        # Открываем иконку эмоции пионера
        emotion_image = Image.open(emotion_image_path)

        emotion_photo = ImageTk.PhotoImage(emotion_image)
        # Обновляем метку для отображения эмоции
        image_label.config(image=emotion_photo)
        image_label.image = emotion_photo
        # Размещаем метку с эмоцией в нижнем правом углу
        image_label.place(relx=1.0, rely=1.0, anchor='se')


    # очень страшный скрипт который динамически обновляет график
    def update_plot(value):
        # Добавляем новые данные в график
        y_values.append(value)
        x_values.append(len(y_values))

        # Очищаем предыдущий график
        ax.clear()

        ax.patch.set_alpha(0)
        fig.patch.set_alpha(0)

        # Строим новый график
        ax.plot(x_values, y_values)
        ax.set_xlabel('Time')
        ax.set_ylabel('Concentration')

        # Обновляем размеры графика, размеры меняются, изменяя значения
        #                                    тут ↓                            и тут ↓
        fig.set_size_inches(root.winfo_width() / 4 / fig.dpi, root.winfo_height() / 4 / fig.dpi)
        #                                        ↑                                  ↑
        ax.patch.set_alpha(0.0)
        plt.subplots_adjust(bottom=0.19)
        canvas.draw()


    # серия функций, которые работают как таймер и переход на другую "сцену"
    def checcky():
        global count
        value = query()
        if value > 80 and count < 60:
            visual_novel.zharka()
            ultrachecking.cancel()
        elif value < 80 and count == 60:
            visual_novel.at_the_school()
            ultrachecking.cancel()
        elif value < 80 and count < 60:
            print(60 - count)
        count += 1


    def check_egg():
        global count1
        value = query()
        if value > 90 and count1 < 60:
            visual_novel.at_the_school()
            chechegg.cancel()
        elif value < 90 and count1 == 60:
            visual_novel.at_the_school()
            chechegg.cancel()
        elif value < 90 and count1 < 60:
            print(60 - count1)
        count1 += 1


    def school_torture():
        global count2
        value = query()
        if value > 98 and count2 < 45:
            visual_novel.good_end()
            tortimes.cancel()
        elif value < 100 and count2 == 45:
            visual_novel.bad_end()
            tortimes.cancel()
        elif value < 100 and count2 < 45:
            print(45 - count2)
        count2 += 1


    # Опрос 5 раз в секунду (каждые 200 мс)
    timer = RepeatTimer(0.2, query)
    # опросы соответствующих функций :D
    ultrachecking = RepeatTimer(1, checcky)
    chechegg = RepeatTimer(1, check_egg)
    tortimes = RepeatTimer(1, school_torture)

    # Создаем окно tkinter

    # Работа над названием в процессе...
    # root.title("Пионерские будни")
    visual_novel = VisualNovel(root)

    # Метка для отображения изображения эмоции
    image_label = tk.Label(root)
    image_label.pack()

    # Создаем график
    fig, ax = plt.subplots()

    # списки для графика
    x_values = []
    y_values = []

    # Встраиваем график в окно tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(relx=0.2, rely=1.228, anchor='s')

    # Устанавливаем цвет фона графика (такой же, как окно tkinter)
    canvas.get_tk_widget().config(bg='#f0f0f0')


    # Обновляем размеры графика при изменении размеров окна
    def on_resize(event):
        # Устанавливаем размеры графика в процентах от размеров окна
        # Тут что-то необъяснимое, но работает (шутка)
        fig_width_percent = 0
        fig_height_percent = 0
        fig.set_size_inches(fig_width_percent * root.winfo_width() / fig.dpi,
                            fig_height_percent * root.winfo_height() / fig.dpi)
        canvas.draw()


    root.bind('<Configure>', on_resize)


    # пуск основного потока
    def main():
        timer.start()
        root.mainloop()


    # цикл запуска программы
    if __name__ == "__main__":
        main()

except RuntimeError:
    print("")
except AttributeError:
    print("")
except tk._tkinter.TclError:
    print("")
