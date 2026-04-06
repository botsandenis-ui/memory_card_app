print("Hello friends")

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
QHBoxLayout, QVBoxLayout,
QGroupBox, QRadioButton,
QPushButton, QLabel, QButtonGroup)

from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = []

question_list.append(Question("2+2?", "4", "421412", "112", "42424"))
question_list.append(Question("Best pokemon?", "Pikachu", 'Bulbasavr', 'Pegeot', "Ghost"))
question_list.append(Question("Best car?", "Toyota", 'BMW', 'Dacia', "Lanos"))
question_list.append(Question("How many days in a week?", "7", "5", "6", "8"))
question_list.append(Question("Capital of France?", "Paris", "London", "Berlin", "Rome"))
question_list.append(Question("Color of grass?", "green", "blue", "red", "yellow"))
question_list.append(Question("5*2?", "10", "8", "12", "15"))
question_list.append(Question("How many legs does a cat have?", "4", "2", "3", "5"))
question_list.append(Question("Which animal can fly?", "bird", "cat", "dog", "cow"))
question_list.append(Question("How many months in a year?", "12", "10", "11", "13"))


app = QApplication([])
window = QWidget()
window.resize(800, 500) 
window.setWindowTitle("Memory card") 


question = QLabel("переклади англійською") 
btn_ok = QPushButton("Answer")  


RadioGroupBox = QGroupBox("Варіанти відповідей")


rbtn1 = QRadioButton("Bus")
rbtn2 = QRadioButton("Car")
rbtn3 = QRadioButton("Tax")
rbtn4 = QRadioButton("Shu")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)


ans_hline = QHBoxLayout()   
ans_vline1 = QVBoxLayout()  
ans_vline2 = QVBoxLayout()  


ans_vline1.addWidget(rbtn1)
ans_vline1.addWidget(rbtn2)
ans_vline2.addWidget(rbtn3)
ans_vline2.addWidget(rbtn4)


ans_hline.addLayout(ans_vline1)
ans_hline.addLayout(ans_vline2)


RadioGroupBox.setLayout(ans_hline)


AnsGroupBox = QGroupBox("Test result") 
lb_Result = QLabel('Are you correct or not?')  
lb_Correct = QLabel('the answer will be here!')  


layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_res)


v_line = QVBoxLayout() 


h1_line = QHBoxLayout() 
h2_line = QHBoxLayout()  
h3_line = QHBoxLayout()  


h1_line.addWidget(question, alignment=Qt.AlignHCenter)  
h2_line.addWidget(RadioGroupBox)  
h2_line.addWidget(AnsGroupBox)    


AnsGroupBox.hide() 


h3_line.addStretch(1)                 
h3_line.addWidget(btn_ok, stretch=2) 
h3_line.addStretch(1)                 


v_line.addLayout(h1_line, stretch=2) 
v_line.addLayout(h2_line, stretch=8)  
v_line.addStretch(1)                 


v_line.addLayout(h3_line, stretch=1)  
v_line.addStretch(1)                 


v_line.addSpacing(5) 

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText("Наступне запитання")

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText("Answer")

    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)

    question.setText(q.question)
    
    lb_Correct.setText(q.right_answer)

    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct("Correct!")

        window.score += 1

        print('-Total questions: ', window.total, ' -Right answers: ', window.score)
        print('Rating: ', (window.score / window.total * 100), '%')

    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers:
            show_correct("Incorrect!!!!")
            print('Rating: ', (window.score / window.total * 100), '%')

def next_question():
    window.total += 1
    print('-Total questions: ', window.total, ' -Right answers: ', window.score)

    cur_question = randint(0, len(question_list) - 1)
    
    q = question_list[cur_question]
    ask(q)

def click_ok():
    
    if btn_ok.text() == "Answer":
        check_answer()
    else:
        next_question()

btn_ok.clicked.connect(click_ok)

window.score = 0
window.total = 0

next_question()

window.setLayout(v_line)

window.show()

app.exec()
