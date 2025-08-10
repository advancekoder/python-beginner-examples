@echo off
REM Usage: commit.bat [commit_message]
REM Commits and pushes changes to the GitHub repository with a default or provided message.
cd C:\Users\DELL-PC\Desktop\Charles Files\python-beginner-examples
if "%1"=="" (
    set COMMIT_MESSAGE="Added new Python exercises"
) else (
    set COMMIT_MESSAGE=%1
)
git add .
git commit -m "%COMMIT_MESSAGE%"
git push origin main
if %errorlevel% neq 0 (
    echo Push failed. Check error messages above (e.g., authentication or network issues).
) else (
    echo Push successful! Files are now on GitHub.
)
pause