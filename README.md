# flask_development
A collection of backend-focused Flask projects exploring API design, CRUD operations, and server-side data handling. Built as part of continuous learning and practical experimentation with backend development concepts.


## Jinja2 Template Rendering & Data Grouping

This module demonstrates server-side data handling and dynamic template rendering using Flask and Jinja2.  
Structured input data is grouped into student and course entities, and templates are rendered conditionally based on command-line input. Course data is additionally visualized using charts to illustrate variations.

Concepts covered:
- Jinja2 template rendering
- Data grouping and structuring on the server side
- Conditional rendering logic
- Backend-to-template data flow


## Student Performance Analytics Dashboard

A Flask-based web application that provides insights into student enrollment and course performance metrics.

**Key Features:**
- **Student Lookup**: Query by Student ID to view all enrolled courses
- **Course Analytics**: Query by Course ID to display:
  - Maximum score achieved
  - Average class performance
  - Grade distribution visualization (frequency chart)
 
## Student Information Management System - CRUD application 

A full-stack Flask application with comprehensive CRUD operations for managing student records, course catalogs, and enrollment data.

**Key Features:**
- **Multi-table Relational Database**: Students, Courses, and Enrollments with proper foreign key relationships
- **Complete CRUD Operations**: 
  - Create new student records
  - Read/display student information
  - Update existing data via form inputs
  - Delete student records from database
- **Database Migration Management**: Implemented Flask-Migrate for version-controlled schema changes
- **RESTful API Controllers**: Organized endpoints for handling form data and database operations
- **Test-Driven Development**: Comprehensive pytest suite covering all application functionalities

**Tech Stack:** Flask, SQLAlchemy, Flask-Migrate, pytest, HTML forms

**Testing:** Implemented unit tests for each controller to ensure data integrity and proper CRUD functionality.
