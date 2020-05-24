from docx import Document

document = Document('test.docx')

result = [p.text for p in document.paragraphs]

print(result)

opfile = open("output.txt","w+")
for line in result:
    opfile.write(line+"\n")


opfile.close()