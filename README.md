# bug-tracking-system
A lightweight console-based bug tracking system built with Python. Features bug creation, status management, and JSON persistence. 
# 🐛 Bug Tracking System

A simple yet powerful console-based bug tracking application for managing software defects efficiently.

## ✨ Features
- 📝 Create and manage bug reports
- 📊 List and view bug details
- 🔄 Update bug status and priority
- 💾 Persistent JSON storage
- 🎯 Clean, intuitive CLI interface

## 🚀 Quick Start
```bash
python bug_tracker.py
```

## 📋 Requirements
- Python 3.8+
- No external dependencies

## 🎯 Use Cases
- Small development teams
- Personal project tracking
- Learning SDLC concepts
- Quick bug documentation

## 📖 Documentation
Complete SDLC documentation included covering requirements, design, testing, and deployment.

## 🔮 Future Features
- Search & filter functionality
- CSV/PDF export
- Multi-user support
- Web interface

---
**License:** MIT | **Version:** 1.0.0
```

**GitHub Topics/Tags to add:**
```
bug-tracker, python, console-app, sdlc, project-management, 
bug-management, cli-tool, json-storage, python3, software-development

# Bug Tracking System
## Software Development Life Cycle (SDLC) Documentation

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [SDLC Phases](#sdlc-phases)
3. [System Requirements](#system-requirements)
4. [Installation Guide](#installation-guide)
5. [User Manual](#user-manual)
6. [Technical Documentation](#technical-documentation)
7. [Testing Documentation](#testing-documentation)
8. [Future Enhancements](#future-enhancements)

---

## 1. Project Overview

### 1.1 Project Title
**Console-Based Bug Tracking System**

### 1.2 Project Description
A lightweight, console-based bug tracking application designed to help development teams log, monitor, and manage software bugs efficiently. The system provides core functionality for adding bugs, viewing bug lists, and updating bug statuses.

### 1.3 Project Objectives
- Provide a simple interface for bug management
- Enable tracking of bug status throughout development lifecycle
- Maintain historical records of all reported bugs
- Offer easy-to-use command-line interface

### 1.4 Scope
**In Scope:**
- Bug creation with title and description
- Bug listing and viewing
- Bug status updates
- Persistent data storage

**Out of Scope:**
- Multi-user authentication
- Web-based interface
- Email notifications
- Advanced reporting and analytics

---

## 2. SDLC Phases

### 2.1 Phase 1: Requirements Analysis

#### 2.1.1 Functional Requirements
1. **Bug Creation**: System shall allow users to create new bug reports with title and description
2. **Bug Listing**: System shall display all bugs with key information (ID, title, status, creation date)
3. **Status Updates**: System shall allow modification of bug status
4. **Data Persistence**: System shall save bug data to persistent storage
5. **User Interface**: System shall provide menu-driven console interface

#### 2.1.2 Non-Functional Requirements
1. **Performance**: System shall respond to user actions within 1 second
2. **Usability**: Interface shall be intuitive for non-technical users
3. **Reliability**: System shall prevent data loss during normal operation
4. **Maintainability**: Code shall follow Python best practices and include documentation
5. **Portability**: System shall run on Windows, Linux, and macOS

#### 2.1.3 Stakeholder Requirements
- **Developers**: Need quick bug logging during testing
- **Project Managers**: Need overview of all bugs and their statuses
- **QA Team**: Need ability to track bug resolution progress

### 2.2 Phase 2: System Design

#### 2.2.1 System Architecture
```
┌─────────────────────────────────────┐
│     User Interface Layer            │
│   (Console Menu System)             │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Business Logic Layer             │
│   (BugTracker Class)                │
│   - add_bug()                       │
│   - list_bugs()                     │
│   - update_bug_status()             │
│   - view_bug()                      │
│   - delete_bug()                    │
└──────────────┬──────────────────────┘
               │
┌──────────────▼──────────────────────┐
│    Data Persistence Layer           │
│   (JSON File Storage)               │
│   - save_bugs()                     │
│   - load_bugs()                     │
└─────────────────────────────────────┘
```

#### 2.2.2 Data Model
```python
Bug Entity:
{
    'id': Integer (Primary Key, Auto-increment),
    'title': String (Required),
    'description': String (Required),
    'status': String (Default: 'Open'),
    'priority': String (Default: 'Medium'),
    'created': DateTime (Auto-generated),
    'updated': DateTime (Auto-updated)
}
```

#### 2.2.3 Class Diagram
```
┌─────────────────────────────┐
│      BugTracker             │
├─────────────────────────────┤
│ - bugs: List                │
│ - bug_id_counter: Integer   │
├─────────────────────────────┤
│ + __init__()                │
│ + add_bug()                 │
│ + list_bugs()               │
│ + update_bug_status()       │
│ + view_bug()                │
│ + delete_bug()              │
│ + save_bugs()               │
│ + load_bugs()               │
│ + run()                     │
└─────────────────────────────┘
```

### 2.3 Phase 3: Implementation

#### 2.3.1 Technology Stack
- **Programming Language**: Python 3.8+
- **Data Storage**: JSON
- **Libraries**: 
  - datetime (built-in)
  - json (built-in)
  - os (built-in)

#### 2.3.2 Development Environment
- **IDE**: Any Python-compatible IDE (VS Code, PyCharm, etc.)
- **Version Control**: Git
- **Operating System**: Cross-platform (Windows/Linux/macOS)

#### 2.3.3 Coding Standards
- Follow PEP 8 style guidelines
- Use meaningful variable and function names
- Include docstrings for all methods
- Implement error handling for all user inputs
- Comment complex logic sections

### 2.4 Phase 4: Testing

#### 2.4.1 Test Plan Overview
Testing will cover functional, integration, and user acceptance testing to ensure system reliability and usability.

#### 2.4.2 Unit Testing
| Test Case ID | Description | Input | Expected Output | Status |
|--------------|-------------|-------|-----------------|--------|
| UT-01 | Add new bug | Title: "Login fails", Description: "Cannot login" | Bug added with ID 1 | Pass |
| UT-02 | List empty bugs | No bugs in system | "No bugs found." | Pass |
| UT-03 | List existing bugs | 2 bugs in system | Display 2 bugs | Pass |
| UT-04 | Update valid bug status | Bug ID: 1, Status: "Closed" | Status updated successfully | Pass |
| UT-05 | Update invalid bug status | Bug ID: 999 | "Bug 999 not found." | Pass |
| UT-06 | View bug details | Bug ID: 1 | Display all bug fields | Pass |
| UT-07 | Delete bug | Bug ID: 1 | Bug deleted successfully | Pass |

#### 2.4.3 Integration Testing
| Test Case ID | Description | Steps | Expected Result | Status |
|--------------|-------------|-------|-----------------|--------|
| IT-01 | Data persistence | Add bug, restart app, list bugs | Bug persists after restart | Pass |
| IT-02 | Multiple operations | Add, update, delete in sequence | All operations succeed | Pass |
| IT-03 | Concurrent bug addition | Add 5 bugs consecutively | All bugs saved with unique IDs | Pass |

#### 2.4.4 User Acceptance Testing
| Test Case ID | Scenario | User Action | Expected Outcome | Status |
|--------------|----------|-------------|------------------|--------|
| UAT-01 | First-time user | Navigate menu, add bug | User completes task without confusion | Pass |
| UAT-02 | Invalid input handling | Enter letters for bug ID | Clear error message displayed | Pass |
| UAT-03 | Exit application | Select exit option | Application closes gracefully | Pass |

### 2.5 Phase 5: Deployment

#### 2.5.1 Deployment Steps
1. Ensure Python 3.8+ is installed on target system
2. Copy `bug_tracker.py` to desired directory
3. Run: `python bug_tracker.py`
4. System creates `bugs.json` automatically on first use

#### 2.5.2 System Requirements
- **Minimum**: Python 3.8, 50MB disk space, 256MB RAM
- **Recommended**: Python 3.10+, 100MB disk space, 512MB RAM

### 2.6 Phase 6: Maintenance

#### 2.6.1 Maintenance Activities
- **Corrective**: Bug fixes based on user reports
- **Adaptive**: Updates for new Python versions
- **Perfective**: Performance improvements and feature additions
- **Preventive**: Code refactoring and optimization

#### 2.6.2 Version Control
- Version numbering: MAJOR.MINOR.PATCH
- Current version: 1.0.0
- Maintain changelog for all updates

---

## 3. System Requirements

### 3.1 Hardware Requirements
- **Processor**: Any modern CPU (Intel/AMD/ARM)
- **RAM**: Minimum 256MB available
- **Storage**: 50MB free disk space
- **Display**: Any console/terminal capable display

### 3.2 Software Requirements
- **Operating System**: Windows 7+, Linux (any recent distribution), macOS 10.12+
- **Python**: Version 3.8 or higher
- **Additional Software**: None (uses only Python standard library)

---

## 4. Installation Guide

### 4.1 Installing Python
#### Windows:
1. Download Python from python.org
2. Run installer and check "Add Python to PATH"
3. Verify: Open Command Prompt and type `python --version`

#### Linux/macOS:
```bash
# Most systems have Python pre-installed
python3 --version

# If not installed (Ubuntu/Debian):
sudo apt update
sudo apt install python3

# macOS (using Homebrew):
brew install python3
```

### 4.2 Installing Bug Tracker
1. Download `bug_tracker.py`
2. Place in desired directory
3. No additional installation required

### 4.3 First Run
```bash
# Navigate to directory
cd /path/to/bug_tracker

# Run the application
python bug_tracker.py
```

---

## 5. User Manual

### 5.1 Starting the Application
Open your terminal/command prompt and run:
```bash
python bug_tracker.py
```

### 5.2 Main Menu Options

#### Option 1: Add a New Bug
1. Select option `1` from main menu
2. Enter bug title when prompted
3. Enter bug description when prompted
4. System confirms bug creation with assigned ID

**Example:**
```
Enter your choice (1-6): 1
Enter bug title: Login button not responding
Enter bug description: Clicking login does nothing on Firefox
Enter priority (Low/Medium/High/Critical): High
Bug 1 added successfully.
```

#### Option 2: List All Bugs
- Select option `2` to view all bugs
- Displays: ID, Title, Status, Priority, Creation Date

#### Option 3: View Bug Details
1. Select option `3`
2. Enter bug ID
3. View complete bug information

#### Option 4: Update Bug Status
1. Select option `4`
2. Enter bug ID to update
3. Enter new status (Open/In Progress/Resolved/Closed/Wontfix)

#### Option 5: Delete Bug
1. Select option `5`
2. Enter bug ID to delete
3. Confirm deletion

#### Option 6: Exit
- Select option `6` to close application
- All data is automatically saved

### 5.3 Status Definitions
- **Open**: Newly reported, not yet addressed
- **In Progress**: Currently being worked on
- **Resolved**: Fix implemented, awaiting verification
- **Closed**: Verified as fixed
- **Wontfix**: Not going to be addressed

### 5.4 Priority Levels
- **Critical**: System crash, data loss, security issue
- **High**: Major functionality broken
- **Medium**: Feature not working as expected
- **Low**: Minor issue, cosmetic problem

---

## 6. Technical Documentation

### 6.1 Source Code Structure
```
bug_tracker.py
├── Imports (datetime, json, os)
├── BugTracker Class
│   ├── __init__(): Initialize tracker
│   ├── load_bugs(): Load from JSON
│   ├── save_bugs(): Save to JSON
│   ├── add_bug(): Create new bug
│   ├── list_bugs(): Display all bugs
│   ├── view_bug(): Show bug details
│   ├── update_bug_status(): Modify status
│   ├── delete_bug(): Remove bug
│   └── run(): Main application loop
└── Main Execution Block
```

### 6.2 Data Storage Format
Bugs are stored in `bugs.json`:
```json
[
  {
    "id": 1,
    "title": "Login fails",
    "description": "Cannot login with valid credentials",
    "status": "Open",
    "priority": "High",
    "created": "2025-01-21 14:30:00",
    "updated": "2025-01-21 14:30:00"
  }
]
```

### 6.3 Key Algorithms

#### Bug ID Generation
- Auto-incrementing counter
- Persists across sessions
- Calculated as: `max(existing_bug_ids) + 1`

#### Data Persistence
- Saves to JSON after each modification
- Loads on application startup
- Creates new file if none exists

---

## 7. Testing Documentation

### 7.1 Test Coverage
- **Unit Tests**: 7 test cases (100% method coverage)
- **Integration Tests**: 3 test cases
- **User Acceptance Tests**: 3 test scenarios

### 7.2 Known Issues
- None at current version (1.0.0)

### 7.3 Bug Reporting
To report bugs in the Bug Tracker itself:
1. Document the issue with steps to reproduce
2. Include error messages if any
3. Note your Python version and OS
4. Contact development team

---

## 8. Future Enhancements

### 8.1 Planned Features (Version 2.0)
- Search functionality by title/description
- Filter bugs by status/priority
- Export bugs to CSV/PDF
- Assign bugs to team members
- Add comments/notes to bugs
- Track time spent on bugs

### 8.2 Long-term Roadmap
- **Version 3.0**: Web-based interface
- **Version 4.0**: Multi-user support with authentication
- **Version 5.0**: Integration with version control systems

---

## 9. Appendices

### Appendix A: Glossary
- **Bug**: A software defect or error
- **SDLC**: Software Development Life Cycle
- **JSON**: JavaScript Object Notation (data format)
- **CLI**: Command Line Interface
- **CRUD**: Create, Read, Update, Delete

### Appendix B: References
- Python Documentation: https://docs.python.org
- PEP 8 Style Guide: https://pep8.org
- JSON Format: https://www.json.org

### Appendix C: Contact Information
- **Project Name**: Bug Tracking System
- **Version**: 1.0.0
- **Release Date**: January 2025


---

## 10. Conclusion

This Bug Tracking System provides a solid foundation for managing software defects in a simple, efficient manner. The console-based approach ensures lightweight operation and ease of deployment. Future versions will expand functionality based on user feedback and organizational needs.

---

**Document Version**: 1.0  
**Last Updated**: January 21, 2025  
**Document Status**: Final  
**Prepared By**: Chukwu Great Ikechukwu  

---
