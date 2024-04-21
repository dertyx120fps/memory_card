from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QLabel, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QButtonGroup)
from random import shuffle, randint
    

app = QApplication([]) 
window = QWidget() 
window.setWindowTitle("Memo Card")
 #Панель вопроса 
btn_OK = QPushButton("Ответить") 
lb_Question = QLabel("В каком году была основана Москва") 
RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton("Вариант1") 
rbtn_2 = QRadioButton("Вариант2") 
rbtn_3 = QRadioButton("Вариант3") 
rbtn_4 = QRadioButton("Вариант4") 

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)


layou_ans_1 = QHBoxLayout() 
layou_ans_2 = QVBoxLayout() 
layou_ans_3 = QVBoxLayout() 
layou_ans_2.addWidget(rbtn_1)
#Два ответа в первый столбец 
layou_ans_2.addWidget(rbtn_2) 
layou_ans_3.addWidget(rbtn_3)
#Два ответа в второй столбец 
layou_ans_3.addWidget(rbtn_4) 
layou_ans_1.addLayout(layou_ans_2) 
layou_ans_1.addLayout(layou_ans_3) 
RadioGroupBox.setLayout(layou_ans_1) 
AnsGroupBox = QGroupBox("Результаты теста") 
lb_Res = QLabel("Прав ты или нет?") 
lb_Corr = QLabel("Ответ будет указан тут:") 
layout_res = QVBoxLayout() 
layout_res.addWidget(lb_Res, alignment = (Qt.AlignLeft | Qt.AlignTop)) 
layout_res.addWidget(lb_Corr, alignment = Qt.AlignCenter , stretch = 2)

AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout() 
layout_line2 = QHBoxLayout() 
layout_line3 = QHBoxLayout() 
layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter )) 
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(2) 
layout_line3.addWidget(btn_OK, stretch = 2) 
layout_line3.addStretch(2) 
layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch = 2) 
layout_card.addLayout(layout_line2, stretch = 8) 
layout_card.addStretch(1) 
layout_card.addLayout(layout_line3, stretch = 1) 
layout_card.addStretch(1) 
layout_card.addStretch(5) 



class Question():
    def __init__(self, quesion, right_answer, wrong1, wrong2, wrong3):
        self.quesion = quesion
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


q_list = []
q_list.append(Question('Чему равно число пи?','3,14...','12,2','0,33','такого нету)'))
q_list.append(Question('Первый признак равенства треугольников?','угол и 2 стороны','сторона и 2 угла','3 стороны','3 угла'))
q_list.append(Question('Второй признак равенства треугольников?','сторона и 2 угла','угол и 2 стороны','3 стороны','3 угла'))
q_list.append(Question('Третий признак равенства треугольников?','3 стороны','сторона и 2 угла','угол и 2 стороны','3 угла'))
q_list.append(Question('К какому типу оружия относится М40 в стендофф2?','снайперские винтовки','винтовки','пистолеты-пулеметы','тяжелое оружие'))



def show_qestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)



answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.quesion)
    lb_Corr.setText(q.right_answer)
    show_qestion()

def show_correct(res):
    lb_Res.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n-всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
        print('Рейтинг: ', (window.score/window.total*100),'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
            print('Рейтинг: ', (window.score/window.total*100),'%')
    

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос:')

def next_question():
    window.total += 1
    print('Статистика\n-всего вопросов: ', window.total, '\n-Правильных ответов: ', window.score)
    cur_question = randint(0,len(q_list)-1)
    q = q_list[cur_question]
    ask(q)

def click_OK():
    if btn_OK.text() == 'Ответить':
        check_answer()
    else:
        next_question()


window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')

window.cur_question = -1

window.score = 0
window.total = 0

btn_OK.clicked.connect(click_OK)
next_question()

window.resize(400,300)
window.show() 
app.exec()
# 2 БЛОК













