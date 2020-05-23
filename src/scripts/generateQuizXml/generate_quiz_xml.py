import xml.etree.ElementTree as ET


ET.register_namespace('wow',"http://www.example.com/ns/1.0")
questions = ET.Element('{http://www.example.com/ns/1.0}questions')

question = ET.SubElement(questions, 'question')

q_name = ET.SubElement(question, 'q_name')
q_name.text = "Question 1:"

q_content = ET.SubElement(question, 'q_content')
q_content.text = "The present value of multiple cash flows is"

q_type = ET.SubElement(question, 'q_type')
q_type.text = "MC"

q_mark = ET.SubElement(question, 'q_mark')
q_mark.text = "0"

q_hint = ET.SubElement(question, 'q_hint')

q_correct = ET.SubElement(question, 'q_correct')

q_wrong = ET.SubElement(question, 'q_wrong')

answers = ET.SubElement(question, 'answers')

q_ans_1 = ET.SubElement(answers, 'q_ans')
q_ans_1.set('q_ans_correct', 'no')
q_ans_1.set('q_ans_mark', '0')
q_ans_1.text = "greater than the sum of the cash flows. "

q_ans_2 = ET.SubElement(answers, 'q_ans')
q_ans_2.set('q_ans_correct', 'no')
q_ans_2.set('q_ans_mark', '0')
q_ans_2.text = "none of the above ."

q_ans_3 = ET.SubElement(answers, 'q_ans')
q_ans_3.set('q_ans_correct', 'no')
q_ans_3.set('q_ans_mark', '0')
q_ans_3.text = "equal to the sum of all the cash flows."

q_ans_4 = ET.SubElement(answers, 'q_ans')
q_ans_4.set('q_ans_correct', 'yes')
q_ans_4.set('q_ans_mark', '1')
q_ans_4.text = "less than the sum of the cash flows. "

data = ET.tostring(questions, encoding = "UTF-8")
file = open("test_questions.xml", "w")
file.write(data)