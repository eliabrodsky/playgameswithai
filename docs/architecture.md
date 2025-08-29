# Architecture

## Overview
The application uses a FastAPI backend with a PostgreSQL database and a React frontend.
Authentication can be provided by an external OIDC provider. All network traffic uses TLS.

```mermaid
flowchart LR
  Browser -->|HTTPS| Frontend
  Frontend -->|REST| Backend
  Backend -->|SQL| Database
  Backend --> AuditLog
```

## Data Flow (Sequence)
```mermaid
sequenceDiagram
  participant U as User
  participant F as Frontend
  participant B as Backend
  participant DB as Database
  participant A as Audit

  U->>F: Submit request
  F->>B: Authenticated API call
  B->>DB: Read/Write
  B->>A: Record audit
  B-->>F: Response
```

## ER Diagram
```mermaid
erDiagram
  PATIENT ||--o{ CONTACT : has
  PATIENT ||--o{ ASSIGNMENT : has
  USER ||--o{ ASSIGNMENT : assigned
  USER ||--o{ AUDIT_LOG : acts
  PATIENT {
    int id
    string first_name
    string last_name
    date dob
    string last4_ssn
    string address
    string phone
    string email
    bool consent_contact
    datetime created_at
    datetime updated_at
  }
  CONTACT {
    int id
    int patient_id
    string contact_method
    string contacted_by
    datetime contacted_at
    string notes
  }
  USER {
    int id
    string email
    string role
    string password_hash
  }
  ASSIGNMENT {
    int id
    int patient_id
    int assigned_to
    datetime assigned_at
    string status
  }
  AUDIT_LOG {
    int id
    int actor_id
    string action
    string resource
    datetime timestamp
  }
```

## Security Notes
- Role-based access (Admin, Care Coordinator, ReadOnly).
- Only last4 SSN stored; full SSN encrypted if ever required.
- At-rest encryption via database features (e.g., pgcrypto) and volume encryption.
- Secrets stored in environment variables and rotated regularly.
- Access logs omit PHI.
