import os
import json
import traceback
import PyPDF2

def get_data(file):

    if file.name.endswith(".pdf"):
        try:
            Pdf_Reader = PyPDF2.PdfFileReader(file)
            text = ""
            for page in Pdf_Reader.pages:
                text += page.extract_text()
            
            return text
        except Exception as e:
            raise Exception("Couldn't read PDF file")
        
    elif file.name.endswith(".txt"):
        return file.read()
    
    else:
        raise Exception(
            "Unsupported format: Please upload a PDF or a TXT file"
        )
    

def get_table_data(quiz):
    try:
        quiz_table_data = []
        for key, value in quiz.items():
            mcq = value["mcq"]
            options = " | ".join(
                [
                    f"{option}: {option_value}"
                    for option, option_value in value["options"].items()
                    ]
                )
            correct = value["correct"]
            quiz_table_data.append({"MCQ": mcq, "Choices": options, "Correct": correct})
    except Exception:
        raise Exception("Cant convert it to table data")

        