
# Troubleshooting Notes

This file contains the most important issues I encountered and how I fixed them.

---

## ❗ Problem: "Python was not found"

### Cause:
Windows App Execution Alias conflict.

### Fix:
1. Go to Settings → Apps → Advanced app settings → App execution aliases  
2. Turn OFF:
   - python.exe
   - python3.exe
3. Reinstall Python with "Add to PATH"

---

## ❗ Problem: "pytest is not recognized"

### Cause:
pytest was not installed or PATH incorrect.

### Fix:
Use:
python -m pip install pytest
python -m pytest tests/ 
---

## ❗ Problem: Git identity unknown

Git required a username and email.

### Fix:git config --global user.name "AmirAshraf123"
git config --global user.email "amirashrafbinmohdandy@gmail.com"
---

## ❗ Problem: “src refspec main does not match any”

### Cause:
Commit failed → branch had no commits.

### Fix:
git add .
git commit -m "initial commit"
git branch -M main
git push -u origin main
---

## ❗ Problem: Can't push to GitHub (needs token)

GitHub removed password authentication.

### Fix:
Create a Personal Access Token and use it when Git asks for a password.

---

## ✔ These issues are now fully resolved.