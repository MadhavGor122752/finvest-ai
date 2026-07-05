# FinVest AI Database Design

Version: 1.0

---

# Database Philosophy

The FinVest AI database is designed using Domain-Driven Design (DDD).

Every table exists because it represents a real business concept.

The database follows these principles:

- UUID primary keys
- Soft deletion where appropriate
- Audit timestamps
- Normalized schema
- Future scalability
- AI-first architecture
- Security-first authentication

# Authentication Domain

Purpose:

Manage user identity, authentication, authorization, and session management.

Responsibilities:

- Register users
- Authenticate users
- Manage login sessions
- Verify email
- Reset passwords
- Issue JWT tokens
- Support guest-to-user conversion