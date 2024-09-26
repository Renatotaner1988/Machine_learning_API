from pydantic import BaseModel
from typing import Optional, List
from model.paciente import Paciente
import json
import numpy as np

class PacienteSchema(BaseModel):
    """ Define como um novo paciente a ser inserido deve ser representado
    """
    name: str = "Maria"
    age: float = 63.0
    sex: float = 1.0
    cp: float = 1.0
    trestbpd: float = 145.0
    chol: float = 233.0
    fbs: float = 1.0
    restecg: float = 2.0
    thalach: float = 150.0
    exang: float = 1.0
    oldpeak: float = 2.3
    slope: float = 3.0
    ca: float = 3.0
    thal: float = 6.0
    
    
    
class PacienteViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    id: int = 1
    name: str = "Maria"
    age: float = 63.0
    sex: float = 1.0
    cp: float = 1.0
    trestbpd: float = 145.0
    chol: float = 233.0
    fbs: float = 1.0
    restecg: float = 2.0
    thalach: float = 150.0
    exang: float = 1.0
    oldpeak: float = 2.3
    slope: float = 3.0
    ca: float = 3.0
    thal: float = 6.0
    num: float = None
    
        
class PacienteBuscaSchema(BaseModel):
    """Define como deve ser a estrutura que representa a busca.
    Ela será feita com base no nome do paciente.
    """
    name: str = "Maria"

class ListaPacientesSchema(BaseModel):
    """Define como uma lista de pacientes será representada
    """
    pacientes: List[PacienteSchema]

    
class PacienteDelSchema(BaseModel):
    """Define como um paciente para deleção será representado
    """
    name: str = "Maria"
    
# Apresenta apenas os dados de um paciente    
def apresenta_paciente(paciente: Paciente):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    return {
        "id": paciente.id,
        "name": paciente.name,
        "age": paciente.age,
        "sex": paciente.sex,
        "cp": paciente.cp,
        "trestbpd": paciente.trestbpd,
        "chol": paciente.chol,
        "fbs": paciente.fbs,
        "restecg": paciente.restecg,
        "thalach": paciente.thalach,
        "exang": paciente.exang,
        "oldpeak": paciente.oldpeak,
        "slope": paciente.slope,
        "ca": paciente.ca,
        "thal": paciente.thal,    
        "num": paciente.num
    }
    
# Apresenta uma lista de pacientes
def apresenta_pacientes(pacientes: List[Paciente]):
    """ Retorna uma representação do paciente seguindo o schema definido em
        PacienteViewSchema.
    """
    result = []
    for paciente in pacientes:
        result.append({
            "id": paciente.id,
            "name": paciente.name,
            "age": paciente.age,
            "sex": paciente.sex,
            "cp": paciente.cp,
            "trestbpd": paciente.trestbpd,
            "chol": paciente.chol,
            "fbs": paciente.fbs,
            "restecg": paciente.restecg,
            "thalach": paciente.thalach,
            "exang": paciente.exang,
            "oldpeak": paciente.oldpeak,
            "slope": paciente.slope,
            "ca": paciente.ca,
            "thal": paciente.thal,    
            "num": paciente.num
        })

    return {"pacientes": result}

