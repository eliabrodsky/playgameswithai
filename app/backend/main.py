from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import SQLModel, Session, create_engine, select
from typing import List
from datetime import datetime
from .models import Patient, Contact, Assignment, User, AuditLog
from .database import get_session, init_db

app = FastAPI(title="Medicaid Outreach API", version="0.1.0")

@app.on_event("startup")
def on_startup():
    init_db()

@app.post("/patients", response_model=Patient)
def create_patient(patient: Patient, session: Session = Depends(get_session)):
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

@app.get("/patients", response_model=List[Patient])
def list_patients(skip: int = 0, limit: int = 100, session: Session = Depends(get_session)):
    patients = session.exec(select(Patient).offset(skip).limit(limit)).all()
    return patients

@app.get("/patients/{patient_id}", response_model=Patient)
def get_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.put("/patients/{patient_id}", response_model=Patient)
def update_patient(patient_id: int, data: Patient, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    for field, value in data.dict(exclude_unset=True).items():
        setattr(patient, field, value)
    patient.updated_at = datetime.utcnow()
    session.add(patient)
    session.commit()
    session.refresh(patient)
    return patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, session: Session = Depends(get_session)):
    patient = session.get(Patient, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    session.delete(patient)
    session.commit()
    return {"ok": True}

