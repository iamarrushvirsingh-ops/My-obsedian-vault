# Integrated Complaint Monitoring and Status Dashboard

*Design document · Smart India Hackathon 2026 · Version 1.0 (as built) · 28 October 2026*

Problem statement: Integrated Dashboard for Monitoring and Tracking Institution-Related Complaint Cases Across AICTE Bureaus/Cells.

## 1. Overview

### 1.1 Problem

AICTE receives complaints about technical institutions from students, faculty and other stakeholders. These are handled by different Bureaus/Cells, mainly the Regulation Bureau (RB) and the Public Grievance Redressal Cell (PGRC). Cases about the same institution can sit with different units at the same time, and there is no central, real-time view. The result is duplicated effort, conflicting or parallel actions, delays in disposal, and no easy way to tell which unit is dealing with which institution.

### 1.2 Solution

A single-window web dashboard where authorized officials can:

- see all institution-related complaint cases in one place
- see which Bureau/Cell and officer currently hold each case
- follow the complete history and movement of every case
- be warned automatically when more than one unit is dealing with the same institution
- monitor pending, under-process, disposed, transferred, escalated and overdue cases
- search, filter and download reports

### 1.3 Key idea

An overlap-detection engine finds complaints about the same institution handled by different units, even when the institution name is spelled differently or the case references differ. It shows the message **“Potential Overlapping Cases – Coordination Required”** and links the cases, so the units can coordinate instead of acting separately.

### 1.4 Expected outcomes

One source of truth for complaints, less duplicated work, no conflicting parallel actions, better coordination between units, timely disposal, and more accountability and transparency.

## 2. Scope

### In scope (prototype)

- Role-based login
- Institution and case records with a permanent action history
- Case creation, status change, transfer and escalation
- Overlap detection with alerts and case linking
- Live dashboard (KPI cards and charts)
- Search and filters
- Deadline (SLA) and pending-case alerts
- CSV reports
- A responsive, minimal interface with a collapsible sidebar
- Generated demo data

### Out of scope for the prototype

- Real AICTE data and live integration with AICTE systems
- Document upload and storage
- Email, SMS and WhatsApp notifications
- Single sign-on, production hosting and HTTPS

See section 17 for future scope.

## 3. Users and Roles

| Role | Who | Main permissions |
| --- | --- | --- |
| Admin | System administrator | Full access to all cases, dashboards and reports |
| Bureau Officer | Staff of RB, PGRC or another Bureau/Cell | Create and update cases of their own unit, transfer, escalate, see overlap alerts |
| Regional Officer | Regional Office/Centre staff | Works with institutions of their region |
| Senior Management | Competent Authority and senior officials | Monitoring: dashboards, escalations, reports |

Only logged-in users can see any page. Every user has one role, and Bureau Officers belong to one Bureau/Cell.

## 4. System Architecture

```
[ Browser: HTML + Bootstrap + Chart.js ]
                  |
                  v
[ Flask web app: routes, login, role checks ]
                  |
        +---------+----------+
        |                    |
        v                    v
[ Overlap engine ]    [ Alert and deadline checks ]
  overlap.py            (scheduled and on demand)
        |                    |
        +---------+----------+
                  v
[ SQLite database via SQLAlchemy ]
```

- **Browser layer** renders pages from templates and draws charts.
- **Flask layer** receives requests, checks who is logged in, runs the logic and returns pages.
- **Logic layer** holds the overlap engine and the alert rules, kept apart from the page code so they are easy to test and explain.
- **Data layer** stores everything in one SQLite file. The same models work on PostgreSQL with a configuration change.

## 5. Technology Stack

| Layer | Tool | Reason |
| --- | --- | --- |
| Language and backend | Python, Flask | Simple, quick to build, easy to explain |
| Database | SQLite (prototype), PostgreSQL (production) | No setup now, scalable later |
| Database access | Flask-SQLAlchemy | Python code instead of hand-written SQL, and protection against SQL injection |
| Login | Flask-Login | Standard session handling |
| Form safety | Flask-WTF | CSRF protection for forms |
| Password security | Werkzeug password hashing | Passwords are never stored as plain text |
| Pages | Jinja2 templates, HTML, Bootstrap 5.3 | Ready-made responsive components |
| Icons and fonts | Bootstrap Icons, IBM Plex Sans and Mono, Source Serif 4 | Clean, consistent look |
| Charts | Chart.js | Lightweight dashboard charts |
| Similar-name matching | RapidFuzz | Fast fuzzy text comparison |
| Timed checks | APScheduler | Runs deadline and reminder checks automatically |
| Reports | pandas | CSV export |
| Demo data | Faker | Realistic dummy institutions and complaints |
| Version control | Git and GitHub | Shared code and safe rollback |

## 6. Project Structure

The project uses a flat structure to keep it easy to navigate and debug.

```
complaint-dashboard/
  app.py              Flask app, routes, login, alert checks
  models.py           Database tables
  overlap.py          Overlap detection engine
  seed.py             Creates demo data
  requirements.txt    Installed packages
  .gitignore
  templates/
    base.html         Layout, sidebar, flash messages
    login.html
    dashboard.html
    cases.html        Case list with search and filters
    case_detail.html  One case, history, overlap banner, actions
    case_new.html     New complaint form
    alerts.html
    reports.html
  static/
    theme.css         All colours and layout
  instance/
    complaints.db     SQLite database (created by seed.py)
```

## 7. Data Model

PK is a primary key (a unique ID for each row). FK is a foreign key (a pointer to a row in another table).

**bureaus**: id (PK), code (unique, for example RB or PGRC), name.

**users**: id (PK), name, email (unique), password\_hash, role (admin, officer, regional, senior), bureau\_id (FK, optional), region (optional).

**institutions**: id (PK, the AICTE Permanent ID), name, city, state, region.

**cases**

| Column | Meaning |
| --- | --- |
| id (PK) | Case ID, for example CMP-2026-0001 |
| institution\_id (FK) | The institution the complaint is about |
| category | Nature of complaint |
| description | Complaint text |
| received\_on | Date of receipt |
| status | Received, Under Process, Pending, Transferred, Escalated or Disposed |
| current\_bureau\_id (FK) | Bureau/Cell presently handling the case |
| assigned\_officer\_id (FK) | Presently assigned officer |
| last\_action\_summary, last\_action\_on | What was last done, and when |
| next\_action\_required | What must happen next |
| expected\_disposal\_on | Deadline, set from the category |
| is\_escalated | True if escalated |
| overlap\_flag | True if the case has an active overlap |

**case\_actions** (the permanent history): id (PK), case\_id (FK), action\_type, from\_bureau\_id and to\_bureau\_id (FK, for transfers), performed\_by (FK), performed\_at, remarks. Rows are only ever added. There is no screen or route to edit or delete them.

**case\_links**: id (PK), case\_a\_id and case\_b\_id (FK), link\_type, match\_score, reason, review\_state (suggested, confirmed or dismissed), created\_at.

**alerts**: id (PK), alert\_type, case\_id (FK), institution\_id (FK), target\_bureau\_id (FK), message, severity, created\_at, is\_read.

**How the tables connect:** one institution has many cases; one case has many actions and alerts; cases are connected to each other through case\_links. Deadlines by category are applied in the application code, not stored in a separate table.

## 8. Case Lifecycle

| Status | Meaning |
| --- | --- |
| Received | Logged, not yet picked up |
| Under Process | An officer is working on it |
| Pending | Waiting for information or a reply |
| Transferred | Handed to another Bureau/Cell |
| Escalated | Sent to higher authority |
| Disposed | Closed with a final remark |

All statuses except Disposed count as open.

**Flow**

1. A case is created with its institution, category and description. The receiving unit is the creating officer’s unit, and the expected disposal date is set from the category.
2. A “received” action is recorded and the overlap check runs.
3. Officers add remarks, change status, transfer or escalate. Each change records who, when, from-unit, to-unit and remarks, and updates the case’s last-action fields.
4. After a transfer the overlap check runs again, because moving a case to another unit can create a new overlap.
5. The case is disposed with a final remark. It stays searchable.

## 9. Overlap Detection

This is the core of the project.

**When it runs.** When a case is created, after a transfer, and across all cases when demo data is loaded.

**What it compares.** For one case, it looks at all other open cases handled by a **different** Bureau/Cell.

| Check | Method | Score |
| --- | --- | --- |
| Same Institution ID | Exact match | 100 |
| Similar institution name and same city | Fuzzy match on cleaned names (RapidFuzz token set ratio of 90 or more) | 70 to 85 |

**Name cleaning.** Names are lowercased, punctuation is removed, short forms are expanded (inst to institute, tech to technology, engg to engineering, univ to university, coll to college, mgmt to management) and the word “the” is dropped. So “A.B.C. Inst. of Tech.” becomes “abc institute of technology”. This is what lets the system match the same institution under different spellings and different IDs.

**What happens on a match**

1. A case link is created between the two cases, with the score and a plain-language reason (for example, “Same Institution ID, different Bureaus/Cells”).
2. A score of 90 or more is saved as confirmed with a high-severity alert. A lower score is saved as suggested with a medium-severity alert.
3. Both cases get their overlap flag set.
4. An alert is created for each case, addressed to its own unit, with the message “Potential Overlapping Cases – Coordination Required”.
5. If the two cases are already linked, nothing new is created. Dismissed links therefore never alert again.

**Worked example.** Institution A has a PGRC case under process. RB opens a new case for the same institution. The checker finds the same Institution ID in a different unit, scores 100, links both cases and alerts both units. Each officer can open the other’s case and see its status.

**Current limits.** The checker compares only cases in different units, so duplicates inside one unit are not detected. Fuzzy name matching needs the same city. It does not read complaint text yet. These are covered under future scope.

## 10. Alerts and Deadlines (SLA)

| Alert | Trigger | Addressed to |
| --- | --- | --- |
| Overlap | An overlap is found | The unit of each case involved |
| Pending reminder | No action for 7 days | The case’s unit |
| Approaching deadline | Expected disposal date within 3 days | The case’s unit |
| Deadline breached | Expected disposal date has passed | The case’s unit |
| Escalation | A case is escalated | The case’s unit |

The deadline checks run on a timer and can also be started with a Run checks now button on the Alerts page. Alerts are not duplicated for the same case and type, and can be marked as read.

**Deadline periods are assumptions.** They are placeholders until AICTE’s prescribed timelines are used.

| Category | Days allowed |
| --- | --- |
| Fee or refund | 30 |
| Faculty | 45 |
| Infrastructure | 45 |
| Approval or affiliation | 60 |
| Other | 30 |

## 11. Dashboard

**KPI cards:** total cases, pending, under process, disposed, transferred, escalated, overdue (past the expected disposal date and not disposed) and active overlaps.

**Charts:** status split (doughnut), Bureau/Cell-wise workload (bar) and monthly received versus disposed (line).

**Tables:** latest overlap alerts and the cases nearest to their deadline.

All figures are calculated live from the database, so they change as soon as a case changes.

## 12. Search, Filters and Reports

**Search and filters** on the case list: institution name, AICTE Permanent ID, case ID, Bureau/Cell, region, category, status and date range, combinable, with pagination.

**Reports** (CSV download): institution-wise case history, region-wise, Bureau/Cell-wise, status-wise, pending-case ageing, disposal rate per unit, and overlapping cases.

## 13. Screens

| Screen | Purpose |
| --- | --- |
| Login | Sign in. Shown without the sidebar |
| Dashboard | KPIs, charts, latest alerts, cases near deadline |
| Cases | Search, filter and open cases. The Case ID is a large boxed link, because it is the way into a case |
| Case detail | All fields, action history timeline, linked cases and overlap banner, and forms for remark, status change, transfer and escalation |
| New case | Create a complaint |
| Alerts | All alerts with mark-as-read and Run checks now |
| Reports | Download CSV reports |

The application routes are named dashboard, cases, case\_detail, new\_case, alerts, reports, login and logout.

## 14. Interface Design

**Direction.** Light and minimal: white surfaces, soft purples, thin borders, sharp square corners, no shadows, glows or hover animations. The aim is a calm, credible look rather than a decorative one.

**Palette**

| Use | Colour |
| --- | --- |
| Deep plum (headings, strong text) | #4C2365 |
| Main accent (buttons, active states) | #7F5D99 |
| Mid purple | #9E7EB5 |
| Light lavender (borders, soft fills) | #C4A4DA |
| Page background | #FBF9FD |
| Cards | #FFFFFF |
| Sidebar | #F3ECF8 |
| Body text | #2A1738 |

**Typography.** Source Serif 4 for page titles and the brand name, IBM Plex Sans for text, IBM Plex Mono for case IDs and numbers.

**Components**

- **Buttons:** primary is medium purple with white text, darkening to deep plum on hover. Secondary is white with a lavender outline.
- **Status badges:** soft fills with darker text. Received is lavender, Under Process is soft blue, Pending is amber, Transferred is purple, Escalated is soft red and Disposed is grey. Status colours are the only colours outside the purple family, because they carry meaning.
- **KPI cards:** white with one thin coloured stripe.
- **Overlap banner:** amber outline with a pale amber fill, so warnings stand out from the purple.
- **Timeline:** a vertical line with a square marker for each action.

**Sidebar.** Fixed on desktop, with the brand, five links (Dashboard, Cases, New Case, Alerts, Reports), the logged-in user and Logout, all visible without scrolling. A button collapses it to icons only. The choice is remembered between pages and the main area widens automatically. On phones and tablets the sidebar becomes a top bar with a menu button.

## 15. Security and Accountability

- Passwords are stored only as hashes.
- Every page except login requires a logged-in user, and actions check the user’s role.
- Forms use CSRF protection.
- Database access goes through the ORM, which prevents SQL injection.
- The action history is append-only, giving a permanent audit trail of who did what and when.

**Prototype limits.** The secret key is a placeholder and must be replaced with a secret stored outside the code. Demo accounts share one simple password. There is no HTTPS or production hosting.

## 16. Demo Data and Testing

### Demo data

The seed script rebuilds the database from scratch with 5 Bureaus/Cells (RB, PGRC, and three example units), 13 users (1 admin, 1 senior official, 1 regional officer and 2 officers per unit), 31 institutions and 204 cases across all statuses. Every ordinary institution is handled by one unit, so overlaps come only from planted cases:

- Greenfield College of Engineering has one PGRC case and one RB case with the same ID, giving an exact-ID overlap.
- “ABC Institute of Technology” (RB) and “A.B.C. Inst. of Tech.” (PGRC) have different IDs, giving a similar-name overlap.

Expected result after seeding: 2 overlap links and 4 alerts.

Demo logins use the pattern admin@demo.com, senior@demo.com, regional@demo.com, and rb1@demo.com or pgrc1@demo.com for unit officers, all with the password demo123. These are demo accounts only.

### Test scenarios

| # | Scenario | Expected result |
| --- | --- | --- |
| 1 | Open the Greenfield cases | Overlap banner shows both units and linked cases |
| 2 | Open the ABC and A.B.C. cases | Similar-name overlap with its reason |
| 3 | Create a case for an institution with an open case in another unit | Overlap is raised immediately |
| 4 | Transfer a case into a unit that already has a case for the same institution | New overlap appears after the transfer |
| 5 | View a transferred case’s history | Both units, time, officer and reason are shown |
| 6 | Run the deadline checks | Overdue and near-deadline alerts appear, with no duplicates |
| 7 | Search and filter by several fields | Results match and pagination works |
| 8 | Download each report | Each CSV opens correctly |
| 9 | Open a page while logged out | Redirected to login |
| 10 | Collapse the sidebar and move between pages | State is remembered and the layout adjusts |

## 17. Limitations and Future Scope

### Known limitations

- All data is generated. Real AICTE records are not used.
- Deadline periods are assumptions.
- Overlap detection compares institutions only. It does not yet read complaint descriptions.
- Documents cannot be uploaded to a case.
- Notifications appear inside the application only.

### Future scope

- Officer review of suggested overlaps (confirm or dismiss) with a recorded reason
- Text similarity on complaint descriptions, and support for Hindi and regional-language complaints
- Detection of duplicate complaints inside the same unit
- Document upload and supporting evidence on each action
- Email, SMS and WhatsApp notifications
- Region-restricted views for Regional Officers and PDF reports
- A full re-scan of all cases on a schedule
- PostgreSQL, secure government cloud hosting, backups and HTTPS
- Single sign-on with AICTE staff accounts
- Live integration with AICTE’s grievance and approval portals, so cases flow in automatically
- Predictive analytics: which institutions are likely to receive repeat complaints

## 18. Setup and Run

1. Install Python 3.11 or newer and create a virtual environment: `python -m venv .venv`, then activate it.
2. Install the packages: `pip install -r requirements.txt`.
3. Create the demo database: `python seed.py`. It should report 204 cases, 2 overlap links and 4 alerts.
4. Start the app: `flask --app app run --debug`, then open http://127.0.0.1:5000.
5. After any change, save with Git: `git add .`, `git commit -m “message”`, `git push`.

Running `python seed.py` again rebuilds the database and removes any changes made by hand.

## 19. Glossary

| Term | Plain meaning |
| --- | --- |
| Bureau/Cell | An AICTE unit that handles complaints, such as RB or PGRC |
| Overlap | Two or more units handling cases for the same institution |
| SLA | The prescribed time limit for disposing of a case |
| Ageing | How many days a case has been open |
| Fuzzy matching | Finding texts that are almost the same |
| Audit trail | A permanent record of who did what and when |
| Primary key and foreign key | A unique ID for a row, and a pointer to a row in another table |
| ORM | A translator that lets Python code talk to the database |
| CSRF | An attack that tricks a logged-in user’s browser into sending an unwanted request. Form protection blocks it |
