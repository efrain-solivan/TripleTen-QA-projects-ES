#!/usr/bin/env bash
# push.sh — Automates the TripleTen QA repo push process.
# Usage: chmod +x push.sh && ./push.sh

set -e
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  TripleTen QA — Repo Push Setup${NC}"
echo -e "${BLUE}========================================${NC}"

echo -e "${YELLOW}[1/5] Checking git repository...${NC}"
if ! git rev-parse --is-inside-work-tree &>/dev/null; then
  echo -e "${RED}ERROR: Not inside a git repository.${NC}"; exit 1
fi
echo -e "${GREEN}      ✓ Inside repo: $(basename $(git rev-parse --show-toplevel))${NC}"

echo -e "${YELLOW}[2/5] Checking .env configuration...${NC}"
if [ ! -f ".env" ]; then
  echo -e "${RED}ERROR: .env not found. Run: cp .env.example .env${NC}"; exit 1
fi
SANDBOX_URL=$(grep "^URBAN_ROUTES_URL=" .env | cut -d'=' -f2-)
if [[ "$SANDBOX_URL" == *"YOUR-SANDBOX-ID"* ]]; then
  echo -e "${RED}ERROR: Set URBAN_ROUTES_URL in .env first.${NC}"; exit 1
fi
echo -e "${GREEN}      ✓ URBAN_ROUTES_URL is set${NC}"

echo -e "${YELLOW}[3/5] Status:${NC}"
git status --short

echo -e "${YELLOW}[4/5] Installing dependencies...${NC}"
pip3 install -r requirements.txt --quiet 2>/dev/null || pip install -r requirements.txt --quiet
echo -e "${GREEN}      ✓ Dependencies installed${NC}"

echo -e "${YELLOW}[5/5] Committing and pushing...${NC}"
git add config.py .env.example .gitignore pytest.ini requirements.txt CONTRIBUTING.md push.sh secrets_setup.sh reports/.gitkeep screenshots/.gitkeep .github/workflows/tests.yml selenium/conftest.py selenium/test_urban_routes.py selenium/pages/__init__.py selenium/pages/urban_routes_page.py
git commit -m "refactor(selenium): add POM, CI/CD, env config, negative tests"
git push origin main

echo -e "${GREEN}✓ PUSH COMPLETE${NC}"
echo "Next: Run ./secrets_setup.sh to configure GitHub Secrets"
