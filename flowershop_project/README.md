# Flower Shop Management System

A Django-based web application for managing a flower shop's inventory, sales, and suppliers.

## Features

- **User Authentication**: Login, registration, and user dashboard
- **Inventory Management**: Track flowers, stock levels, and reorder alerts
- **Supplier Management**: Manage supplier information and contacts
- **Sales Tracking**: Record sales transactions and generate reports
- **Responsive Design**: Bootstrap-powered UI that works on all devices

## Tech Stack

- **Backend**: Django 4.2
- **Database**: PostgreSQL (Production), SQLite (Development)
- **Frontend**: Bootstrap 4, Crispy Forms
- **Deployment**: Render

## Local Development Setup

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)
- Git

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd flowershop_project
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create .env file**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**
   ```bash
   python manage.py runserver
   ```

9. **Access the application**
   - Open your browser and go to `http://localhost:8000`
   - Admin panel: `http://localhost:8000/admin`

## Deployment to Render

### Method 1: Using Render Dashboard (Recommended)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Create a new Web Service on Render**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure the service:
     - **Name**: flowershop (or your preferred name)
     - **Environment**: Python 3
     - **Build Command**: `./build.sh`
     - **Start Command**: `gunicorn flowershop_project.wsgi:application`

3. **Create a PostgreSQL Database**
   - Click "New +" → "PostgreSQL"
   - Name it `flowershop_db`
   - Select a plan (Free tier available)

4. **Set Environment Variables**
   In your Web Service settings, add:
   - `SECRET_KEY`: Generate a secure random string (you can use Django's `get_random_secret_key()`)
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: Your Render URL (e.g., `flowershop.onrender.com`)
   - `DATABASE_URL`: Copy from your PostgreSQL database (should auto-populate)

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Wait for the build to complete

### Method 2: Using render.yaml (Blueprint)

1. **Update render.yaml**
   - Ensure `render.yaml` is configured correctly
   - The file is already set up in this project

2. **Deploy from Dashboard**
   - Go to Render Dashboard
   - Click "New +" → "Blueprint"
   - Connect your GitHub repository
   - Render will automatically create the web service and database

### Post-Deployment Steps

1. **Create a superuser** (via Render Shell)
   - Go to your Web Service → "Shell"
   - Run:
     ```bash
     python manage.py createsuperuser
     ```

2. **Access your application**
   - Your app will be available at: `https://your-service-name.onrender.com`

## Environment Variables

Required environment variables for production:

- `SECRET_KEY`: Django secret key (generate a secure random string)
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Your domain name(s), comma-separated
- `DATABASE_URL`: PostgreSQL connection string (provided by Render)

## Project Structure

```
flowershop_project/
├── accounts/               # User authentication app
├── inventory/              # Flower and supplier management
├── sales/                  # Sales tracking and reporting
├── flowershop_project/     # Main project settings
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── build.sh              # Render build script
├── render.yaml           # Render deployment config
└── runtime.txt           # Python version specification
```

## Common Issues and Solutions

### Issue: Static files not loading
**Solution**: Run `python manage.py collectstatic` and ensure `STATIC_ROOT` is set correctly.

### Issue: Database connection error
**Solution**: Verify `DATABASE_URL` environment variable is set correctly in Render.

### Issue: SECRET_KEY error
**Solution**: Generate a new secret key and add it to environment variables.

### Issue: ALLOWED_HOSTS error
**Solution**: Add your Render domain to the `ALLOWED_HOSTS` environment variable.

## Security Notes

- Never commit `.env` files or expose `SECRET_KEY`
- Always set `DEBUG=False` in production
- Use strong passwords for database and admin accounts
- Keep dependencies updated: `pip install --upgrade -r requirements.txt`

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License.

## Support

For issues and questions, please open an issue on GitHub or contact the development team.

## Acknowledgments

- Django Framework
- Bootstrap
- Django Crispy Forms
- Render Platform
