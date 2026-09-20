#!/usr/bin/env bash
echo "========================================================"
echo "  TalkieTown US - Kids Spoken English Game Demo"
echo "========================================================"
echo ""
echo "[1/2] Starting local web server at http://localhost:3000..."
echo "[2/2] Opening default browser..."
echo ""

if which xdg-open > /dev/null; then
  xdg-open http://localhost:3000 &
elif which open > /dev/null; then
  open http://localhost:3000 &
fi

python3 -m http.server 3000 || python -m http.server 3000
