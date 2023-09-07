from PyQt5.QtWidgets import QApplication, QLabel

input_string = "This is underlined."

# 문자열을 밑줄로 쳐진 문자열로 바꾸기
underlined_string = f"<u>{input_string}</u>"

app = QApplication([])

label = QLabel()
label.setText(underlined_string)
label.show()

app.exec_()
