# Software Requirements Specification (SRS)

# Project Title
SIP & Mutual Fund Management System

# Product Name
FinVest AI

# Version
1.0

# Document Status
Draft

# Prepared By
Madhav Gor

# 1. Introduction

## 1.1 Purpose

The purpose of this project is to develop a production-quality AI-powered Mutual Fund Investment Platform that enables investors to discover mutual funds, invest through SIPs and lump-sum investments, monitor portfolio performance using live market data, and receive AI-driven financial insights and recommendations.

The system is designed to simulate a real-world fintech platform where users can manage their investments while administrators oversee the platform, mutual funds, analytics, and operations.

Rather than functioning as a simple academic project, the application aims to demonstrate how modern investment platforms are architected using scalable software engineering practices, secure backend services, responsive web technologies, and artificial intelligence.

## 1.2 Vision

To build a modern fintech platform that provides intelligent investment management using real-time mutual fund data, AI-powered recommendations, portfolio analytics, and secure financial services while following industry-standard software architecture.

The final product should resemble the experience offered by professional investment platforms such as Groww, Zerodha Coin, and ET Money, while remaining an original implementation developed specifically for this project.

# 2. Stakeholders & User Roles

## 2.1 Stakeholders

The primary stakeholders of the system are:

- Investors
- Platform Administrators
- Mutual Fund Companies (Data Source)
- Financial Data Providers
- System Developers

---

## 2.2 User Roles

### Investor

The Investor is the primary user of the platform.

Responsibilities:

- Register and Login
- Complete Risk Profile
- Browse Mutual Funds
- Search and Filter Funds
- View Fund Details
- Invest in Mutual Funds
- Create SIPs
- Modify or Cancel SIPs
- Track Portfolio
- View Transactions
- Set Financial Goals
- Receive AI Recommendations
- Use AI Investment Assistant
- Receive Notifications
- Manage Profile

---

### Administrator

The Administrator manages the complete platform.

Responsibilities:

- Dashboard Monitoring
- User Management
- Mutual Fund Database Management
- Platform Analytics
- AI Monitoring
- Notification Management
- Revenue Monitoring
- Investment Monitoring
- Platform Configuration
- System Logs
- Security Monitoring

---

## 2.3 Future Expansion

The architecture should allow future support for additional roles such as:

- Financial Advisor
- Customer Support Executive
- Compliance Officer
- Super Administrator

# 3. Platform Modules

The platform is divided into multiple independent modules.

Each module communicates with the backend through secure REST APIs.

---

## Module 1 — Authentication

Features

- Register
- Login
- Logout
- Forgot Password
- Reset Password
- Email Verification
- JWT Authentication
- Refresh Tokens

---

## Module 2 — User Profile

Features

- Personal Information
- Bank Details
- PAN Verification
- KYC Status
- Risk Profile
- Investment Preferences

---

## Module 3 — Mutual Fund Explorer

Features

- Browse Funds
- Search Funds
- Filter Funds
- Sort Funds
- Category Wise Funds
- AMC Wise Funds
- Fund Details
- Historical NAV

---

## Module 4 — Portfolio

Features

- Holdings
- Portfolio Allocation
- Total Investment
- Current Value
- Profit/Loss
- XIRR
- Returns Graph

---

## Module 5 — SIP Management

Features

- Create SIP
- Pause SIP
- Resume SIP
- Cancel SIP
- Upcoming Installments
- SIP Calendar

---

## Module 6 — One Time Investment

Features

- Lump Sum Investment
- Redemption
- Switch Funds
- Additional Purchase

---

## Module 7 — Transactions

Features

- Investment History
- SIP History
- Orders
- Statements
- Download Reports

---

## Module 8 — Dashboard

Features

- Live Portfolio
- Today's Gain/Loss
- Market Overview
- Investment Summary
- Recent Transactions
- Notifications

## Module 9 — AI Investment Advisor

Features

- Portfolio Analysis
- Risk Analysis
- Diversification Score
- AI Fund Recommendation
- Goal Recommendation
- SIP Optimization

---

## Module 10 — AI Chat Assistant

Features

- Investment Questions
- Mutual Fund Education
- Portfolio Explanation
- Tax Guidance
- SIP Guidance
- Financial Goal Planning

---

## Module 11 — Market Intelligence

Features

- Live Market Overview
- NIFTY
- SENSEX
- Top Gainers
- Top Losers
- Mutual Fund News
- Economic Events

---

## Module 12 — Goals

Features

- Retirement Goal
- Car Goal
- House Goal
- Education Goal
- Vacation Goal
- Custom Goal

---

## Module 13 — Notifications

Features

- SIP Reminder
- Order Updates
- AI Alerts
- Market Alerts
- Goal Alerts

---

## Module 14 — Admin Panel

Features

- User Management
- Investment Monitoring
- Revenue Analytics
- Platform Analytics
- AI Monitoring
- Audit Logs

---

## Module 15 — Reports

Features

- Portfolio Reports
- Tax Reports
- Annual Statements
- SIP Reports
- Performance Reports

