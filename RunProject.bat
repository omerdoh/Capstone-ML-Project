@echo off

REM Check if pip is installed
echo Checking pip is installed or not!
where pip >nul 2>nul
if %errorlevel% neq 0 (
  echo pip is not installed. Installing now...
  powershell -Command "Set-ExecutionPolicy Unrestricted; iex ((New-Object System.Net.WebClient).DownloadString('https://bootstrap.pypa.io/get-pip.py'))"
)

echo pip is now ready to use.

@echo off

REM Check if TensorFlow and other packages are already installed
python -c "import tensorflow, cv2, matplotlib, google.protobuf" 2>nul
if %errorlevel% equ 0 (
    echo TensorFlow and other required packages are already installed.
) else (
    echo Installing TensorFlow and other required packages...
    pip install tensorflow==2.8 opencv-python matplotlib protobuf==3.19.1
)

echo Checking python librarie are available or not!
REM Check if pandas, flask, and flask_cors are installed
pip show pandas >nul 2>nul
if %errorlevel% neq 0 (
  echo pandas is not installed. Installing now...
  pip install pandas
)
pip show flask >nul 2>nul
if %errorlevel% neq 0 (
  echo flask is not installed. Installing now...
  pip install flask
)
pip show flask_cors >nul 2>nul
if %errorlevel% neq 0 (
  echo flask_cors is not installed. Installing now...
  pip install flask_cors
)

pip install fitz
pip install frontend
pip install PyMuPdf
echo python libraries are ready to use.

REM Change directory back to the root directory
cd .\capstone-backend

echo ************           RUNNING PYTHON SERVER           ************
REM Run your Python file
start cmd /K "Python Backend.py"

REM Change directory to your React app
cd ..\capstone-frontend  

REM Check if npm is installed
where npm >nul 2>nul
if %errorlevel% neq 0 (
  echo npm is not installed. Installing now...
  choco install nodejs-lts -y
  npm install
)

echo Installing react-scripts...
npm install react-scripts

echo ************           STARTING REACT PAGE           ************
REM Build your React app
npm run start

REM Pause so the user can see any output before the window closes
pause