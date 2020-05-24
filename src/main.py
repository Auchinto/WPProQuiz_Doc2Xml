import xml.etree.ElementTree as ET
from docx import Document
import sys

inputPath = sys.argv[1]
outFileName = sys.argv[2]
outAddress = sys.argv[3]
startIndex = int(sys.argv[4])

document = Document(inputPath)

lineSequences = [p.text for p in document.paragraphs]

def mapToXMLTree(index, content, qType, mark, hint, correct, wrong, ansList):
    question = ET.SubElement(questions, 'question')

    q_name = ET.SubElement(question, 'q_name')
    q_name.text = "Question " + str(index) + ":"

    q_content = ET.SubElement(question, 'q_content')
    q_content.text = content

    q_type = ET.SubElement(question, 'q_type')
    q_type.text = qType

    q_mark = ET.SubElement(question, 'q_mark')
    q_mark.text = mark

    q_hint = ET.SubElement(question, 'q_hint')
    q_hint.text = hint

    q_correct = ET.SubElement(question, 'q_correct')
    q_correct.text = correct

    q_wrong = ET.SubElement(question, 'q_wrong')
    q_wrong.text = wrong

    answers = ET.SubElement(question, 'answers')

    for answerIndex in range(len(ansList)):
        q_ans = ET.SubElement(answers, 'q_ans')
        q_ans.set('q_ans_correct', 'yes' if ansList[answerIndex][1] == 1 else 'no')
        q_ans.set('q_ans_mark', str(ansList[answerIndex][1]))
        q_ans.text = ansList[answerIndex][0]

        
ET.register_namespace('wow',"http://www.example.com/ns/1.0")
questions = ET.Element('{http://www.example.com/ns/1.0}questions')

i = 0
questionIndex = startIndex
while i < len(lineSequences):
    line = lineSequences[i]
    if line.startswith("@"):
        #Beginning of the question
        content = line[1:]
        ansList = []
        i+=1
        while i < len(lineSequences):
            line = lineSequences[i]
            if line.startswith("&"): break
            if line.startswith("$"):
                ansList.append((line[1:],1))
            else:
                ansList.append((line,0))
            i+=1
        mapToXMLTree(questionIndex, content, "MC", "0", "", "", "", ansList)
        questionIndex += 1
    i+=1

        
data = ET.tostring(questions, encoding="UTF-8")
file = open(outAddress + "/" + outFileName, "w")
file.write(data)