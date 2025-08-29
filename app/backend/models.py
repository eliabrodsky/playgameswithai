from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, date
from typing import Optional, List

class Patient(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    dob: date
    last4_ssn: Optional[str] = Field(default=None, index=True)
    address: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    consent_contact: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    contacts: List["Contact"] = Relationship(back_populates="patient")
    assignments: List["Assignment"] = Relationship(back_populates="patient")

class Contact(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patient.id")
    contact_method: str
    contacted_by: Optional[str] = None
    contacted_at: datetime = Field(default_factory=datetime.utcnow)
    notes: Optional[str] = None

    patient: Optional[Patient] = Relationship(back_populates="contacts")

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True)
    role: str
    password_hash: str

class Assignment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    patient_id: int = Field(foreign_key="patient.id")
    assigned_to: int = Field(foreign_key="user.id")
    assigned_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = Field(default="pending")

    patient: Optional[Patient] = Relationship(back_populates="assignments")

class AuditLog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    actor_id: Optional[int] = Field(foreign_key="user.id")
    action: str
    resource: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    before: Optional[str] = None
    after: Optional[str] = None
