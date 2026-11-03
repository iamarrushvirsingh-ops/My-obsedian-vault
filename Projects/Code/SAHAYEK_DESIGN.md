# SAHAYEK_DESIGN.md

## Project Overview

**Project Name:** Sahayek  
**Working Directory:** `/home/arrush/Desktop/Notes/Projects/Code`  
**Repository:** Git repo (no commits yet on branch `master`)  
**Status:** Early/skeleton implementation

Sahayek appears to be intended as a web-based complaint/case monitoring dashboard (based on the problem statement and dependencies). The current codebase contains only a minimal Flask application skeleton with core dependencies declared but no models, routes, templates, static assets, or business logic implemented.

## Main Problem Statement and Description

**Problem Statement ID:** 26264

**Problem Statement Title:** Integrated Dashboard for Monitoring and Tracking Institution-Related Complaint Cases Across AICTE Bureaus/Cells

### Problem Statement

The All India Council for Technical Education (AICTE) receives various complaints and grievances related to technical education institutions from students, faculty members, stakeholders, and other concerned parties. These complaints are handled by different Bureaus/Cells, including the Regulation Bureau (RB) and the Public Grievance Redressal Cell (PGRC). At present, cases relating to the same institution may be received and processed by different Bureaus/Cells. Due to the absence of a centralized, real-time mechanism for monitoring the status of such cases, there is a possibility of overlapping actions, duplication of efforts, delays in disposal, and difficulty in identifying which Bureau/Cell is currently dealing with a particular institution/case.

There is therefore a need to develop an Integrated Institution Complaint Monitoring and Status Dashboard that provides a consolidated view of all institution-related complaint cases across AICTE Bureaus/Cells.

### Objective

The proposed solution should provide a single-window dashboard through which authorized AICTE officials can:

- View all institution-related complaint/grievance cases in one place.
- Identify the Bureau/Cell currently handling each case.
- Track the complete status and movement of a complaint/case.
- Identify cases where RB and PGRC actions overlap or where multiple Bureaus/Cells are dealing with the same institution.
- Avoid duplication of action and ensure proper coordination between concerned Bureaus/Cells.
- Monitor pending, disposed, under-process, transferred, and escalated cases.
- Generate institution-wise, region-wise, Bureau/Cell-wise and status-wise reports.
- Provide alerts for pending cases and cases approaching prescribed timelines.

### Key Features Expected

#### 1. Centralized Institution Profile
- Unique Institution ID/AICTE Permanent ID.
- Institution name, address, region and other relevant details.
- Consolidated history of complaints/cases related to the institution.

#### 2. Complaint/Case Tracking
- Unique Complaint/Case ID.
- Date of receipt.
- Nature/category of complaint.
- Current status.
- Presently assigned Bureau/Cell.
- Assigned officer/official.
- Last action taken.
- Next action required.
- Date of last action and expected disposal date.

#### 3. Cross-Bureau/Cell Overlap Detection
- Automatically identify when complaints concerning the same institution are being handled by RB, PGRC or other Bureaus/Cells.
- Provide an overlap alert to authorized officials.
- Enable linking/mapping of related complaints and cases.

#### 4. Real-Time Dashboard
The dashboard should display:
- Total complaints/cases received.
- Pending cases.
- Cases under process.
- Cases disposed.
- Cases transferred.
- Cases pending beyond prescribed timelines.
- Institution-wise case status.
- Bureau/Cell-wise workload.

#### 5. Workflow and Action History
- Complete chronological history of actions taken.
- Officer/Bureau responsible for each action.
- Date and time stamp.
- Remarks and supporting documents.
- Transfer/escalation history.

#### 6. Search and Filters
Users should be able to search by:
- Institution Name.
- AICTE Permanent ID.
- Complaint/Case ID.
- Bureau/Cell.
- Region.
- Complaint category.
- Status.
- Date range.

#### 7. Alerts and Notifications
- Duplicate/overlapping case alerts.
- Pending case reminders.
- Escalation alerts.
- Timeline/SLA alerts.

#### 8. Reports and Analytics
- Bureau-wise reports.
- Region-wise reports.
- Institution-wise complaint history.
- Pending case ageing analysis.
- Disposal rate.
- Overlapping/duplicate cases.
- Monthly/quarterly performance reports.

### Innovation Expected

The proposed system should use data matching, rule-based logic and/or AI-assisted analytics to identify complaints relating to the same institution even when the complaint descriptions or case references are different.

For example:
- Institution A → Complaint received by PGRC → Case under process
- Institution A → Complaint received by RB → Action initiated

The system should automatically identify the common institution and display:
**“Potential Overlapping Cases – Coordination Required”**

This will enable the concerned Bureaus/Cells to coordinate and decide the appropriate course of action.

### Expected Outcome

The proposed dashboard will establish a single source of truth for institution-related complaints and regulatory actions, thereby:
- Reducing duplication of work.
- Preventing conflicting or parallel actions.
- Improving coordination between RB, PGRC and other Bureaus/Cells.
- Ensuring timely disposal of complaints.
- Improving accountability and transparency.
- Enabling management to monitor the status of institutions and complaints in real time.
- Supporting data-driven decision-making by AICTE.

### Target Users

- AICTE Regulation Bureau (RB).
- Public Grievance Redressal Cell (PGRC).
- Other concerned AICTE Bureaus/Cells.
- Regional Offices/Centres.
- Authorized officers and senior management.
- Competent Authority/AICTE administration.

### Organization Details

- **Organization:** AICTE
- **Department:** Regulation Bureau
- **Category:** Software
- **Theme:** Smart Automation


## Project Scope and Objectives

### Scope (as inferred from problem statement and dependencies)
The intended scope is to build an integrated dashboard for AICTE to monitor institution-related complaint cases across multiple Bureaus/Cells (notably RB and PGRC), with cross-bureau overlap detection, case tracking, workflows, alerts, and reports. 

### Objectives (from problem statement)
As listed above in the Objectives section. 

### Scope Status vs. Current Implementation
- **Current implementation scope:** Minimal Flask app returning plain text at `/`. 
- **Gap:** Nearly all expected features are not implemented; the codebase is at skeleton/inception stage.

## Target Users and Roles

**Expected (from problem statement):**
- AICTE Regulation Bureau (RB)
- Public Grievance Redressal Cell (PGRC)
- Other concerned AICTE Bureaus/Cells
- Regional Offices/Centres
- Authorized officers and senior management
- Competent Authority/AICTE administration

**Implemented:** Could not be determined from current codebase. No authentication/authorization logic found (`Flask-Login` is listed in dependencies but not used in current code).

## Application Architecture Overview

### Architecture Pattern
- **Type:** Web application (Flask-based)
- **Structure:** Traditional server-rendered Flask app with `templates/` and `static/` directories
- **Entry point:** `app.py` defines Flask app instance

### Current Architecture State
- App only defines `app` and route `/` returning static text. No blueprints, no models imported/used, no database configuration visible. Empty files suggest intended modules: `models.py` (data models), `overlap.py` (overlap detection logic), `seed.py` (data seeding).

## Technology Stack

**From `requirements.txt`:**
| Package | Version | Purpose (inferred) |
|---------|---------|-------------------|
| APScheduler | 3.11.3 | Task scheduling (likely for alerts/reminders/reports) |
| blinker | 1.9.0 | Signals |
| click | 8.5.0 | CLI utilities |
| Faker | 40.43.0 | Test data generation (seed) |
| Flask | 3.1.3 | Web framework |
| Flask-Login | 0.6.3 | Authentication/session management |
| Flask-SQLAlchemy | 3.1.1 | ORM/database integration |
| Flask-WTF | 1.3.0 | Forms/CSRF protection |
| itsdangerous | 2.2.0 | Secure tokens |
| Jinja2 | 3.1.6 | Template engine |
| MarkupSafe | 3.0.4 | Template escaping |
| numpy | 2.5.4 | Data processing |
| pandas | 3.1.0 | Data analysis/reporting |
| python-dateutil | 3.0.0 | Date utilities |
| RapidFuzz | 3.14.6 | Fuzzy string matching (relevant for overlap detection) |
| six | 1.17.0 | Compatibility |
| SQLAlchemy | 2.1.6 | ORM |
| typing_extensions | 4.16.0 | Typing |
| tzdata | 2026.5 | Timezone data |
| tzlocal | 5.4.5 | Local timezone |
| Werkzeug | 3.1.9 | WSGI utilities/security |
| WTForms | 3.3.1 | Form validation |

**Frontend:** Not explicitly listed; likely server-rendered HTML with Jinja templates and static CSS/JS (directories exist but empty).

**Backend/Runtime:** Python 3.12 (from pyc file).

## Route and Page Inventory

**Implemented routes:**
| Route | Method | Handler | Response | Source |
|-------|--------|---------|----------|--------|
| `/` | GET (implicit) | `home()` in `app.py:5-7` | Plain text: `"Complaint dashboard is running!"` | `app.py` |

**All other routes/pages:** None implemented. No HTML templates exist. 

## Detailed Page-by-Page UI Documentation

### Page 1: Home / Root (`/`)
- **Purpose:** Health/status check (minimal placeholder)
- **Route:** `/`
- **Source file:** `app.py` (lines 1-7)
- **Layout:** None (plain text response, no template rendering)
- **Sections:** None
- **UI Components:** None (no HTML/CSS)
- **Text:** `"Complaint dashboard is running!"`
- **Interactions:** None
- **Data displayed:** None
- **Status:** Implemented as a minimal stub only.

**All other pages from the problem statement (Dashboard, Institution Profile, Case Details, Reports, Alerts, etc.):** Not present in the current codebase. Could not be documented from implementation.

## Navigation and User Flows

- **Current navigation:** None (single route returning text).
- **Intended flows (from problem statement):** Dashboard-centric flow with institution profiles, case tracking, overlap detection, reports, alerts - not implemented.

## UI Components and Reusable Patterns

- **Implemented:** None found (no templates/components).
- **Dependencies suggest potential patterns:** WTForms for forms, Flask-Login for auth, Jinja templates for rendering, but none used yet.

## Design System and Styling

- **Colors/Typography/Spacing/Borders/Cards/Buttons/Icons:** Could not be determined - no CSS files, no style definitions found in static/ or templates/.
- **Responsive behavior:** Could not be determined.
- **Assets:** None present in `static/`.

## Forms, Tables, Filters, and Interactive Elements

- **Implemented:** None. (Flask-WTF/WTForms available but not used)
- **Expected per problem:** Extensive forms, tables, filters, modals - not present.

## Data Fields, Statuses, and Displayed Information

- **Implemented:** None.
- **Expected data model elements (from problem):** Institutions, Complaints/Cases, Bureaus/Cells, Officers, Actions/History, Statuses (pending, under-process, disposed, transferred, escalated), overlaps/alerts, reports - no schema implemented yet (`models.py` empty).

## API and Backend Dependencies, if identifiable

- **API endpoints:** Only `/` implemented (returns plain text). No JSON APIs found.
- **Backend dependencies used:** Flask core only in current app code.
- **Declared but unused:** Flask-SQLAlchemy, Flask-Login, Flask-WTF, APScheduler, pandas, numpy, RapidFuzz, Faker - suggest intended backend features not yet coded.

## Responsive Layout and Behavior

Could not be determined from current implementation.

## Assets and Their Usage

- `static/` directory exists but is empty.
- `templates/` directory exists but is empty.

## Implemented, Incomplete, and Placeholder Features

### Implemented
- Minimal Flask application with route `/` returning status text
- Project dependency manifest for full dashboard stack
- Directory structure prepared (`templates/`, `static/`, `models.py`, `overlap.py`, `seed.py`)

### Incomplete
- All functional features described in the problem statement (dashboard, case tracking, overlap detection, reports, auth, etc.)
- Data models (`models.py` is empty)
- Overlap detection logic (`overlap.py` is empty)
- Database seeding (`seed.py` is empty)
- UI/templates and static assets

### Placeholder
- `app.py` serves only a placeholder message
- Empty modules suggest planned but unimplemented functionality

## Source File Reference Map

| Path | Type | Description |
|------|------|-------------|
| `/home/arrush/Desktop/Notes/Projects/Code/app.py` | Python/Flask | App entry point; defines Flask app and minimal route `/` |
| `/home/arrush/Desktop/Notes/Projects/Code/requirements.txt` | Config | Python dependencies for full stack |
| `/home/arrush/Desktop/Notes/Projects/Code/.gitignore` | Config | Ignores `.venv/`, `__pycache__/`, `instance/`, `.env` |
| `/home/arrush/Desktop/Notes/Projects/Code/models.py` | Python (empty) | Intended for SQLAlchemy models |
| `/home/arrush/Desktop/Notes/Projects/Code/overlap.py` | Python (empty) | Intended for overlap/cross-bureau detection logic |
| `/home/arrush/Desktop/Notes/Projects/Code/seed.py` | Python (empty) | Intended for seeding test data |
| `/home/arrush/Desktop/Notes/Projects/Code/templates/` | Directory (empty) | Intended for Jinja HTML templates |
| `/home/arrush/Desktop/Notes/Projects/Code/static/` | Directory (empty) | Intended for CSS/JS/images |
| `/home/arrush/Desktop/Notes/Projects/Code/__pycache__/app.cpython-312.pyc` | Compiled | Compiled bytecode of current `app.py` |

## Constraints and Unresolved Details

- **No implementation of problem requirements:** The current codebase does not implement any of the expected dashboard functionality. All features described in the problem statement are unimplemented.
- **Empty core modules:** `models.py`, `overlap.py`, `seed.py` contain no code; schemas, relationships, and overlap logic cannot be verified.
- **No UI:** No templates or static files exist.
- **No auth/roles:** Flask-Login is available but not configured/used.
- **No database config:** No DB URI, migrations, or models visible.
- **No API structure:** Only a text route exists.
- **Cannot determine design details:** Colors, typography, layout, components, data structures all cannot be verified from current codebase - they would need to be inferred from requirements if building, but per instructions this document describes only what exists.
- **Git state:** No commits exist yet.

## Gap Analysis (Problem Statement vs Current Implementation)

| Expected Area | Problem Statement Expectation | Current State | Gap |
|---------------|-------------------------------|---------------|-----|
| Dashboard UI | Consolidated real-time dashboard with KPIs, workload, timelines | None | Not implemented |
| Institution Profiles | Centralized profiles with history | None (no models/templates) | Not implemented |
| Case Tracking | Full case lifecycle, officers, actions, history | None | Not implemented |
| Cross-Bureau Overlap Detection | Auto-detect same institution across RB/PGRC with alerts | `overlap.py` empty, RapidFuzz available but unused | Not implemented |
| Workflow/Action History | Chronological actions, transfers, remarks, docs | None | Not implemented |
| Search & Filters | Multi-field search with date ranges | None | Not implemented |
| Alerts/Notifications | Overlap, pending, escalation, SLA alerts (APScheduler available) | None | Not implemented |
| Reports & Analytics | Bureau/region/institution reports, ageing, disposal rate (pandas available) | None | Not implemented |
| Authentication/Roles | Role-based access for multiple user types | Flask-Login available but unused | Not implemented |
| Data Persistence | Structured storage for cases/institutions/actions | Flask-SQLAlchemy available but no models/config | Not implemented |
