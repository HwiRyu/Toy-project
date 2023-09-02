import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget,QTextEdit,QLineEdit
from PyQt5.QtCore import QDate, Qt, QTime, QTimer
from PyQt5.QtGui import QFont
import reader
from datetime import datetime, timedelta

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.showtime()
        self.first_show()
        self.first_show_on, self.second_show_on = True, False  # 처음에는 first_show가 꺼져있다고 가정
        self.today = 0
        self.end = False
        self.lineempty = False
        self.enter = False

    def showtime(self):
        self.status_bar = self.statusBar()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.updateTime()

    def initUI(self):
        neo_font = QFont("NeoDunggeunmo", 15)
        # 제목 및 글꼴 설정
        self.setWindowTitle('Schedule Assist')
        #창 위치
        self.setFont(neo_font)  # 모든 위젯에 대한 기본 폰트 설정

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)  # 클래스 변수로 layout 설정

        self.setFixedSize(500,500)

        self.show()

    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter):
            if self.second_show_on == False:
                self.clear()
                self.first_show_on = False
                self.second_show_on = True
                self.second_show()
            elif self.second_show_on == True and not self.lineempty:
                self.status_input.setFocus()  # 활성화된 입력 필드에 포커스를 줍니다.
                self.lineempty = True
            elif self.enter == True:
                self.lineempty = False

        elif event.key() == Qt.Key_Escape and self.end == False:
            self.end = True
            self.clear()

            label = TypingLabel("Good Bye.", self)  # 수정된 부분
            label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(label)  # 클래스 변수로 설정된 layout 사용
            timer = QTimer(self)
            timer.singleShot(1000, self.quit)

        elif event.key() == Qt.Key_Left and self.second_show_on == True:
            self.clear()
            self.today += 1
            self.second_show()

        elif event.key() == Qt.Key_Right and self.second_show_on == True:
            self.clear()
            self.today -= 1
            self.second_show()

    def updateTime(self):
        current_date = QDate.currentDate()
        current_time = QTime.currentTime()
        self.status_bar.showMessage(current_date.toString(Qt.ISODate) + " " + current_time.toString())

    def first_show(self):
        self.first_show_on = True

        label = TypingLabel(reader.first, self)  # 수정된 부분
        label.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(label)  # 클래스 변수로 설정된 layout 사용

    def second_show(self):
        reader.now = self.today

        datetype = TypingLabel(reader.super(self.today), self)
        datetype.speed = 1# 수정된 부분
        datetype.setAlignment(Qt.AlignLeft)
        self.layout.addWidget(datetype)  # 클래스 변수로 설정된 layout 사용

        self.line_txt()

    def line_txt(self):
        # 하단에 라인 입력 위젯 추가
        self.status_input = QLineEdit(self)
        with open('date.txt', 'r') as file:
            f = file.read()
            god = reader.second_data(f, self.today)
            good = god[8]

        self.status_input.setText(good)

        self.layout.addWidget(self.status_input)

        # 중심 위젯 생성 및 레이아웃 설정
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)


        # 입력 필드에서 Enter 키를 눌렀을 때 호출될 이벤트 핸들러 설정

        self.status_input.returnPressed.connect(self.process_input)


    def process_input(self):
        # 입력 필드에서 텍스트 가져오기
        input_text = self.status_input.text().strip()  # 앞뒤 공백 제거

        if input_text == "":
            self.status_input.clearFocus()
            self.enter = True
        else:
            # 입력 필드 초기화
            self.status_input.clear()
            self.status_input.clearFocus()
            self.enter = True

        today = (datetime.now() - timedelta(days=self.today)).strftime('%Y-%m-%d')

        # 파일을 읽기 모드('r')로 열고 데이터 읽기
        with open('date.txt', 'r') as date_file:
            lines = date_file.readlines()

        # 수정된 내용을 저장할 리스트
        new_lines = []

        # 각 줄을 처리하며 수정 또는 추가
        for line in lines:
            if today in line:
                # 날짜와 일치하는 줄을 찾았을 때, 오른쪽에 텍스트를 추가 또는 수정
                line = today + '\'' + input_text + '\'' + '\n'
            new_lines.append(line)

        # 파일을 쓰기 모드('w')로 열고 수정된 내용 저장
        with open('date.txt', 'w') as date_file:
            date_file.writelines(new_lines)

        self.clear()
        self.second_show()

    def clear(self):
        for i in reversed(range(self.layout.count())):
            widget = self.layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

    def quit(self):
        QApplication.quit()

class TypingLabel(QLabel):  # 추가된 클래스

    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setFont(QFont("NeoDunggeunmo", 14))
        self.setAlignment(Qt.AlignCenter)
        self.text = text
        self.current_text = ""
        self.typing_timer = QTimer(self)
        self.typing_timer.timeout.connect(self.updateText)
        self.multiplier = 1
        self.currentIndex = 0
        self.speed = 30
        self.updateInterval()  # 초기 간격 설정
        self.typing_timer.start()

    def updateText(self):
        if self.currentIndex < len(self.text):
            if self.text[self.currentIndex] in ',!.\'?':
                self.multiplier = 3
            else:
                self.multiplier = 1

            self.current_text += self.text[self.currentIndex]
            self.setText(self.current_text)
            self.currentIndex += 1

            self.updateInterval()  # 타이머 간격을 업데이트

        else:
            self.typing_timer.stop()

    def updateInterval(self):
        self.typing_timer.setInterval(self.speed * self.multiplier)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
