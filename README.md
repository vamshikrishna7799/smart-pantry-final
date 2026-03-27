# Smart Pantry System

A web-based pantry management system with email notifications and shopping list generation.

## Features
- User registration and login (JWT authentication)
- Multiple pantry profiles
- Add items with decimal quantities (0.5 kg, 1.5 liters)
- Track expiry dates with status indicators
- Automatic shopping list generation
- Email OTP for password reset
- Email shopping list
- Download shopping list as HTML

## Live Demo
- Frontend: https://friendly-starship-8fbd86.netlify.app
- Backend API: https://smart-pantry-api-wptw.onrender.com

## Tech Stack
- Backend: Flask (Python)
- Frontend: HTML/CSS/JavaScript
- Database: MongoDB Atlas
- Email: Gmail SMTP
- Authentication: JWT with bcrypt

## Run Locally
1. Clone repository
2. Create virtual environment: `python -m venv venv`
3. Activate: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create `.env` file with MongoDB and email credentials
6. Run backend: `python app1.py`
7. Run frontend: `python -m http.server 5500`
8. Open: `http://127.0.0.1:5500/Entry.html`

## Environment Variables
Create `.env` file in backend folder: