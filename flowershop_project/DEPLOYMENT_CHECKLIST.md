# Render Deployment Checklist

## Pre-Deployment Checklist

- [ ] All code is committed to Git
- [ ] Repository is pushed to GitHub
- [ ] `.env` file is in `.gitignore` (DO NOT commit)
- [ ] `requirements.txt` is up to date
- [ ] `build.sh` is executable (`chmod +x build.sh`)
- [ ] Static files directory exists
- [ ] Database migrations are created

## Render Setup Steps

### Step 1: Create Render Account
1. Go to https://render.com/
2. Sign up or log in
3. Connect your GitHub account

### Step 2: Create PostgreSQL Database
1. Click "New +" → "PostgreSQL"
2. Name: `flowershop_db`
3. Database: `flowershop_db` (auto-filled)
4. User: `flowershop_db_user` (auto-filled)
5. Region: Choose closest to your users
6. Plan: Select Free or paid tier
7. Click "Create Database"
8. **SAVE the Internal Database URL** - you'll need this!

### Step 3: Create Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure:
   - **Name**: `flowershop` (or your choice)
   - **Region**: Same as database
   - **Branch**: `main` (or your default branch)
   - **Root Directory**: Leave blank
   - **Environment**: `Python 3`
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn flowershop_project.wsgi:application`
   - **Plan**: Free or paid tier

### Step 4: Set Environment Variables
In the Web Service, go to "Environment" tab and add:

```
SECRET_KEY = <generate-random-50-char-string>
DEBUG = False
ALLOWED_HOSTS = your-app-name.onrender.com
DATABASE_URL = <paste-from-postgres-internal-url>
```

**To generate SECRET_KEY:**
```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

Or use: https://djecrety.ir/

### Step 5: Deploy
1. Click "Create Web Service"
2. Wait for build to complete (5-10 minutes first time)
3. Check logs for any errors

### Step 6: Post-Deployment
1. Go to your service → "Shell" tab
2. Create superuser:
   ```bash
   python manage.py createsuperuser
   ```
3. Follow prompts to create admin account

### Step 7: Test Your Application
- [ ] Visit `https://your-app-name.onrender.com`
- [ ] Test user registration
- [ ] Test user login
- [ ] Access admin panel: `https://your-app-name.onrender.com/admin`
- [ ] Test inventory features
- [ ] Test sales features
- [ ] Check static files are loading

## Troubleshooting

### Build Failed
**Check build logs for errors:**
- Missing dependencies? Update `requirements.txt`
- Python version issues? Check `runtime.txt`
- Permission issues? Ensure `build.sh` is executable

### Application Error
**Common fixes:**
1. Check environment variables are set correctly
2. Verify `ALLOWED_HOSTS` includes your Render URL
3. Check database connection (DATABASE_URL)
4. Review application logs in Render dashboard

### Static Files Not Loading
1. Check `STATIC_ROOT` in settings.py
2. Verify `collectstatic` ran in build.sh
3. Check WhiteNoise middleware is installed
4. Clear browser cache

### Database Connection Issues
1. Verify DATABASE_URL is correct
2. Check database is running in Render
3. Ensure database and web service are in same region
4. Check database connection limits

### 502 Bad Gateway
1. Check if application is starting correctly
2. Review logs for Python errors
3. Verify gunicorn is running
4. Check memory limits aren't exceeded

## Important Notes

### Free Tier Limitations
- Web service spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- Database has storage limits
- Consider upgrading for production use

### Security Best Practices
- ✅ Never commit `.env` or secrets to Git
- ✅ Use strong, unique SECRET_KEY
- ✅ Set DEBUG=False in production
- ✅ Keep dependencies updated
- ✅ Use HTTPS (Render provides this)
- ✅ Regular database backups

### Updating Your App
1. Make changes locally
2. Test thoroughly
3. Commit and push to GitHub
4. Render auto-deploys on push (if enabled)
5. Or manually deploy from Render dashboard

## Monitoring

### Check Application Health
- [ ] Monitor Render dashboard for errors
- [ ] Set up uptime monitoring (UptimeRobot, etc.)
- [ ] Review logs regularly
- [ ] Monitor database size

### Performance Optimization
- [ ] Enable caching if needed
- [ ] Optimize database queries
- [ ] Compress static files
- [ ] Use CDN for media files (if applicable)

## Backup Strategy

### Database Backups
1. Render provides automated backups (paid plans)
2. Manual backups via Render dashboard
3. Export data regularly:
   ```bash
   python manage.py dumpdata > backup.json
   ```

### Code Backups
- Always use Git
- Keep GitHub repository updated
- Tag releases: `git tag -a v1.0 -m "Version 1.0"`

## Support Resources

- Render Documentation: https://render.com/docs
- Django Documentation: https://docs.djangoproject.com/
- Project Issues: [Your GitHub Issues URL]

## Success Checklist

- [ ] Application is accessible via HTTPS
- [ ] Admin panel is working
- [ ] Users can register and login
- [ ] All features are functional
- [ ] Static files are loading correctly
- [ ] Database is connected and working
- [ ] No errors in application logs
- [ ] Superuser account created
- [ ] Environment variables configured
- [ ] SSL/HTTPS is working
- [ ] Application is secure (DEBUG=False)

## Next Steps After Deployment

1. **Custom Domain** (Optional)
   - Purchase domain
   - Add to Render
   - Update DNS settings
   - Update ALLOWED_HOSTS

2. **Email Configuration** (Optional)
   - Set up SMTP settings
   - Configure email backend
   - Test password reset emails

3. **Monitoring & Analytics**
   - Set up error tracking (Sentry)
   - Add Google Analytics
   - Configure uptime monitoring

4. **Performance**
   - Enable caching
   - Optimize database queries
   - Consider CDN for static files

Congratulations! Your Flower Shop application is now live! 🎉
