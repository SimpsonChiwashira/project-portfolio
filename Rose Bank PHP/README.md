# Rose Bank Web Application

## Overview
A full-stack banking web application built with vanilla PHP that emulates real banking functionality including user authentication, account management, and appointment booking.

## Features
- **User Authentication**: Login and registration system
- **Account Management**: Balance checking, profile management
- **Appointment Booking**: Schedule appointments with bank staff
- **Admin Dashboard**: Admin panel for managing customers and appointments
- **Role-Based Access**: Separate interfaces for clients and administrators

## Technology Stack
- **Backend**: PHP (Vanilla)
- **Database**: MySQL
- **Frontend**: HTML, CSS, JavaScript
- **UI Framework**: Bootstrap (for responsive design)
- **Styling**: Custom CSS and SCSS

## Project Structure
```
rose-bank-webapp/
├── admin/                 # Admin panel
│   ├── adminhome.php     # Admin dashboard
│   ├── appoint.php       # Appointment management
│   ├── clientreg.php     # Client registration
│   └── ...               # Other admin functions
├── css/                  # Stylesheets
├── js/                   # JavaScript files
├── fonts/                # Font files
├── images/               # Image assets
├── index.php             # Landing page
├── login.php             # Login page
├── register.php          # Registration page
├── clienthome.php        # Client dashboard
├── profile.php           # User profile
├── appointment.php       # Appointment booking
├── rose_bank.sql         # Database schema
└── config.php            # Database configuration
```

## Installation

### Prerequisites
- PHP 7.0 or higher
- MySQL/MariaDB
- Web server (Apache/Nginx) or PHP built-in server

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd "Rose Bank WebApp using PHP"
   ```

2. **Database Setup**
   - Create a MySQL database named `rose_bank`
   - Import the database schema:
     ```bash
     mysql -u username -p rose_bank < rose_bank.sql
     ```

3. **Configure Database Connection**
   - Edit `config.php` with your database credentials:
     ```php
     $servername = "localhost";
     $username = "your_username";
     $password = "your_password";
     $dbname = "rose_bank";
     ```

4. **Run the Application**
   - Using PHP built-in server:
     ```bash
     php -S localhost:8000
     ```
   - Or configure with Apache/Nginx

5. **Access the Application**
   - Main page: `http://localhost:8000/index.php`
   - Admin panel: `http://localhost:8000/admin/adminhome.php`

## Usage

### Client Features
- Register a new account
- Login to access client dashboard
- View account balance
- Update profile information
- Book appointments

### Admin Features
- Access admin dashboard
- View and manage client accounts
- Manage appointments
- View customer care requests

## Academic Context
This project was developed as a learning exercise while mastering PHP web development. The frontend template was adapted from Colorlib (free template) with custom backend functionality implemented in vanilla PHP.

## Security Notes
- This is a learning project and may not include all security best practices
- In production, consider implementing:
  - Password hashing (bcrypt/Argon2)
  - CSRF protection
  - Input validation and sanitization
  - Secure session management
  - HTTPS enforcement

## Future Improvements
- Implement password hashing
- Add email verification
- Improve error handling
- Add transaction history
- Implement two-factor authentication
- Add API endpoints for mobile integration

## Author
Simpson Chiwashira

## License
This project is for educational purposes.