# Classroom Scheduler - Complete Setup Guide

## 🚀 Quick Start (Automated Setup)

### Option 1: Batch File (Recommended for Windows)
1. Double-click `auto_mysql_setup.bat` in the project root
2. Follow the on-screen instructions
3. If automated setup fails, follow manual steps below

### Option 2: PowerShell Script
1. Right-click `setup_mysql.ps1` and select "Run with PowerShell" (as Administrator)
2. Follow the on-screen instructions

## 🔧 Manual Setup Instructions

If the automated scripts fail, follow these steps:

### Step 1: Install MySQL
If you don't have MySQL installed:
1. Download MySQL from: https://dev.mysql.com/downloads/mysql/
2. Install with default settings
3. Remember the root password you set during installation

### Step 2: Start MySQL Service
1. Open Windows Services (`services.msc`)
2. Find "MySQL" or "MySQL80" service
3. Right-click and select "Start"

### Step 3: Configure Database
1. Open Command Prompt as Administrator
2. Run: `mysql -u root -p`
3. Enter your MySQL root password (or press Enter if no password)
4. Run these commands:

```sql
-- Create database
CREATE DATABASE IF NOT EXISTS classroom_scheduler;

-- Create user
CREATE USER IF NOT EXISTS 'classroom_user'@'localhost' IDENTIFIED BY 'classroom123';

-- Grant permissions
GRANT ALL PRIVILEGES ON classroom_scheduler.* TO 'classroom_user'@'localhost';

-- Apply changes
FLUSH PRIVILEGES;

-- Exit MySQL
EXIT;
```

### Step 4: Setup Environment
1. Create a `.env` file in the `backend` folder with:
```
DB_HOST=localhost
DB_USER=classroom_user
DB_PASSWORD=classroom123
DB_NAME=classroom_scheduler
DB_PORT=3306
```

### Step 5: Install Dependencies & Setup Database
```bash
# Navigate to project root
cd "C:\Users\MY\OneDrive\Projects\SE PROJECT"

# Activate virtual environment
.venv\Scripts\activate

# Install Python dependencies
pip install -r backend/requirements.txt

# Navigate to backend
cd backend

# Test connection
python test_connection.py

# Setup database tables
python setup_database.py
```

### Step 6: Run the Application
```bash
# Start the Flask server
python app.py
```

### Step 7: Access the Application
1. Open your web browser
2. Go to: `frontend/index.html`
3. Login with:
   - Username: `admin`
   - Password: `admin`

## 📁 Project Structure
```
SE PROJECT/
├── backend/                 # Flask API server
│   ├── app.py              # Main application
│   ├── config.py           # Configuration
│   ├── requirements.txt    # Python dependencies
│   ├── controllers/        # Business logic
│   ├── models/            # Data models
│   ├── routes/            # API endpoints
│   ├── utils/             # Utilities (DB, auth, etc.)
│   └── database/          # Database schema
├── frontend/               # HTML/CSS/JS client
│   ├── index.html         # Main page
│   ├── dashboard.html     # Dashboard
│   ├── style.css          # Styles
│   └── js/                # JavaScript files
├── auto_mysql_setup.bat   # Automated setup (Windows)
└── setup_mysql.ps1        # Automated setup (PowerShell)
```

## 🔑 Default Credentials
- **Admin**: username: `admin`, password: `admin`
- **Faculty**: username: `faculty1`, password: `faculty1`

## 🛠 Troubleshooting

### MySQL Connection Issues
1. Make sure MySQL service is running
2. Check if the user credentials in `.env` match what you created
3. Try connecting manually: `mysql -u classroom_user -p` (password: classroom123)

### Port Already in Use
If port 5000 is busy:
1. Kill the process: `netstat -ano | findstr :5000`
2. Or change the port in `backend/app.py`

### Python Import Errors
1. Make sure you're in the virtual environment
2. Install missing packages: `pip install -r backend/requirements.txt`

## 📊 Features
- ✅ User authentication (admin/faculty)
- ✅ Classroom management
- ✅ Schedule creation with conflict detection
- ✅ Availability checking
- ✅ Permanent data storage with MySQL
- ✅ Responsive web interface

## 🎯 What's Working Now
- All CRUD operations for classrooms and schedules
- User authentication
- Conflict detection for overlapping schedules
- Data persistence across server restarts
- Complete frontend-backend integration

Your classroom scheduling system is now fully functional with permanent data storage! 🎉
   FLUSH PRIVILEGES;
   EXIT;
   ```

4. **Update `.env` file:**
   ```env
   DB_USER=classroom_user
   DB_PASSWORD=classroom123
   ```

5. **Test and setup:**
   ```bash
   python test_connection.py
   python setup_database.py
   ```

## Quick Start

1. **Install dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Configure MySQL:**
   - Edit `backend/.env` with your MySQL credentials
   - Test connection: `python test_connection.py`

3. **Setup database:**
   ```bash
   python setup_database.py
   ```

4. **Run the application:**
   ```bash
   python app.py
   ```

5. **Open frontend:**
   - Open `frontend/index.html` in browser

## Default Login Credentials

- **Admin:** username: `admin`, password: `admin`
- **Faculty:** username: `faculty1`, password: `faculty1`

## Installation

1. **Clone or download the project**
   ```bash
   cd backend
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure MySQL Database**

   Copy the environment template:
   ```bash
   cp .env.example .env
   ```

   Edit `.env` file with your MySQL settings:
   ```env
   DB_HOST=localhost
   DB_USER=your_mysql_username
   DB_PASSWORD=your_mysql_password
   DB_NAME=classroom_scheduler
   DB_PORT=3306
   ```

4. **Setup Database**

   Run the database setup script:
   ```bash
   python setup_database.py
   ```

   This will:
   - Create the `classroom_scheduler` database
   - Create all necessary tables
   - Insert default users

## Running the Application

1. **Start the Flask backend:**
   ```bash
   python app.py
   ```

2. **Open the frontend:**
   - Open `frontend/index.html` in your web browser
   - Or serve the frontend files with a web server

## Default Login Credentials

- **Admin:** username: `admin`, password: `admin`
- **Faculty:** username: `faculty1`, password: `faculty1`

## API Endpoints

### Authentication
- `POST /auth/login` - User login

### Classrooms
- `POST /classroom/add-room` - Add classroom
- `GET /classroom/get-rooms` - Get all classrooms
- `PUT /classroom/update-room/<id>` - Update classroom
- `DELETE /classroom/delete-room/<id>` - Delete classroom

### Schedules
- `POST /schedule/schedule` - Create schedule
- `GET /schedule/get-schedule` - Get all schedules

### Availability
- `POST /availability/check-availability` - Check room availability

## Database Schema

The application uses MySQL with the following tables:

- `users` - User accounts and authentication
- `classrooms` - Classroom information
- `schedules` - Lecture schedules with foreign key to classrooms

## Development

The application includes:
- Input validation
- Conflict detection (room and faculty conflicts)
- Error handling
- CORS support for frontend integration

## Troubleshooting

1. **Database connection issues:**
   - Verify MySQL server is running
   - Check `.env` file configuration
   - Ensure user has proper permissions

2. **Port conflicts:**
   - Flask runs on port 5000 by default
   - Change port in `app.py` if needed

3. **Permission errors:**
   - Ensure MySQL user has CREATE, INSERT, SELECT, UPDATE, DELETE permissions

## License

This project is for educational purposes.