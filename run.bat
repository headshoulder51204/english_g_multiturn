@echo off
chcp 65001 > nul
echo ========================================================
echo   TalkieTown US - Kids Spoken English Game Demo
echo ========================================================
echo.
echo [1/2] 로컬 개발 서버를 실행합니다 (http://localhost:3000)...
echo [2/2] 기본 웹 브라우저에서 게임 데모를 자동으로 엽니다.
echo.
echo 브라우저에서 마이크 권한을 허용하시면 음성 인식(STT)이 활성화됩니다.
echo 종료하려면 창을 닫거나 Ctrl+C 를 누르세요.
echo.

start "" http://localhost:3000
python -m http.server 3000
