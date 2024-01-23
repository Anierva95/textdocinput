from flask import Flask, request, jsonify
from docx import Document

app = Flask(__name__)

@app.route("/fill-document", methods=["POST"])
def create_doc():
    print(request.json)
    doc = Document("./document_template.docx")

    for paragraph in doc.paragraphs:
        print(paragraph.text)
        if "Lorum" in paragraph.text:
            print("Found em!")
    
    print(doc)
    return jsonify({'status': 'success', 'message': 'Form submitted successfully'})