#!/usr/bin/env bash
# secrets_setup.sh — Adds GitHub Secrets for CI/CD via gh CLI.
# Requires: gh CLI (brew install gh) + gh auth login
# Usage: chmod +x secrets_setup.sh && ./secrets_setup.sh

set -e
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}  TripleTen QA — GitHub Secrets Setup${NC}"

if ! command -v gh &>/dev/null; then
  echo -e "${RED}ERROR: gh CLI not installed. Run: brew install gh${NC}"; exit 1
fi
if ! gh auth status &>/dev/null; then
  echo -e "${RED}ERROR: Run: gh auth login${NC}"; exit 1
fi
echo -e "${GREEN}✓ GitHub CLI authenticated${NC}"

[ ! -f ".env" ] && echo -e "${RED}ERROR: .env not found.${NC}" && exit 1
set -o allexport; source .env; set +o allexport

[[ "$URBAN_ROUTES_URL" == *"YOUR-SANDBOX-ID"* ]] && echo -e "${RED}ERROR: Update URBAN_ROUTES_URL in .env first.${NC}" && exit 1

REPO=$(gh repo view --json nameWithOwner -q .nameWithOwner)
echo -e "${GREEN}✓ Repo: ${REPO}${NC}"

set_secret() { [ -n "$2" ] && echo "$2" | gh secret set "$1" --repo "$REPO" && echo -e "${GREEN}  ✓ $1${NC}"; }

set_secret URBAN_ROUTES_URL    "$URBAN_ROUTES_URL"
set_secret TEST_FROM_ADDRESS   "$TEST_FROM_ADDRESS"
set_secret TEST_TO_ADDRESS     "$TEST_TO_ADDRESS"
set_secret TEST_PHONE          "$TEST_PHONE"
set_secret TEST_CARD_NUMBER    "$TEST_CARD_NUMBER"
set_secret TEST_CARD_CVV       "$TEST_CARD_CVV"
set_secret TEST_SMS_CODE       "$TEST_SMS_CODE"
set_secret TEST_DRIVER_COMMENT "$TEST_DRIVER_COMMENT"

echo -e "${GREEN}✓ ALL SECRETS SET${NC}"
gh workflow run tests.yml --repo "$REPO" && echo -e "${GREEN}✓ CI triggered${NC}" || echo "Go to Actions tab and re-run manually."
echo "Live: https://github.com/${REPO}/actions"
