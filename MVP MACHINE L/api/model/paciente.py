from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base



class Paciente(Base):
    __tablename__ = 'pacientes'
    
    id = Column(Integer, primary_key=True)
    name= Column("Name", String(50))
    age= Column("age", Float)
    sex = Column("sex", Float)
    cp = Column("cp", Float)                         
    trestbpd = Column("trestbpd", Float)
    chol = Column("chol", Float)    
    fbs = Column("fbs", Float)                                 
    restecg = Column("restecg", Float)
    thalach = Column("thalach", Float)
    exang = Column("exang", Float)
    oldpeak = Column("oldpeak", Float)
    slope = Column("slope", Float)
    ca = Column("ca", Float)
    thal = Column("thal", Float)
    num = Column("num", Float)
    
    data_insercao = Column(DateTime, default=datetime.now())
    
    def __init__(self, age:float, name:str, sex:float, cp:float, trestbpd:float,
                 chol:float, fbs:float, restecg:float, 
                 thalach:float, exang:float, oldpeak:float,
                 slope:float, ca:float, thal:float, num:float, 
                 data_insercao:Union[DateTime, None] = None):
        
        
        """
       
        """
        self.name=name
        self.age = age
        self.sex = sex
        self.cp = cp
        self.trestbpd = trestbpd
        self.chol = chol
        self.fbs = fbs
        self.restecg = restecg
        self.thalach = thalach
        self.exang = exang
        self.oldpeak = oldpeak
        self.slope = slope
        self.ca = ca
        self.thal = thal
        self.num = num                      
        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao