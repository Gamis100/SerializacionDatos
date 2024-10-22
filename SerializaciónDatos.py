from flask  import Flask,jsonify, request
from flask_restful import Api
import basicauth
from flask import Flask, jsonify, make_response, request
import json
from dicttoxml import dicttoxml
import yaml
from functools import partial
from xml.dom.minidom import parseString
app=Flask(__name__)

class Persona(object):
    def __init__(self, nombre:str , apellido:str,fecha_nacimiento:str, telefono :str, email:str):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.telefono = telefono
        self.email = email

#formato json
@app.route('/persona_json',methods=['GET'])
def Personajson():
    person = Persona(nombre="Gabriela", apellido="Pacco",fecha_nacimiento="12/11/20",telefono="903249587",email="gabriela@gmail.com") 
    json_data = json.dumps(person.__dict__) 
    return(json_data) 
    #return(Persona(**json.loads(json_data))) 

# formato xml
@app.route('/persona_xml',methods=['GET'])
def Personaxml():
    person = {"nombre":"Gabriela", "apellido":"Pacco" ,"fecha_nacimiento":"12/11/20","telefono":"903249587","email":"gabriela@gmail.com"}
    xml=dicttoxml(person)
    xml=xml.decode()
    dom = parseString(xml)
    return(dom.toprettyxml())
    #return (xml)


person = {"nombre":"Gabriela", "apellido":"Pacco" ,"fecha_nacimiento":"12/11/20","telefono":"903249587","email":"gabriela@gmail.com"}
xml=dicttoxml(person)
xml=xml.decode()
dom = parseString(xml)
print(dom.toprettyxml())


# formato yaml
@app.route('/persona_yaml',methods=['GET'])
def Personayaml():
    person = {"nombre":"Gabriela", "apellido":"Pacco" ,"fecha_nacimiento":"12/11/20","telefono":"903249587","email":"gabriela@gmail.com"}
    with open("person.yaml", "w") as fh:  
        yaml.dump(person, fh)
    return(yaml.dump(person, sort_keys=False))


if __name__=='__main__':

    app.run(debug=True,port=4000)