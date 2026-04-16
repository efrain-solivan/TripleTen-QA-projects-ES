# Postman — Urban Routes API Test Collection

**Sprint:** 4 — APIs (TripleTen QA Engineering Apprenticeship)  
**Author:** Efrain Solivan  
**Collection file:** `urban_routes_api_collection.json`

---

## What this collection tests

The Urban Routes backend exposes a REST API for user management, kit configuration, product catalog, and fast-delivery cost calculation. This collection covers:

| Folder | Endpoints | Tests |
|--------|-----------|-------|
| Users | `POST /api/v1/users`, negative cases | 2 |
| Kits | `GET /api/v1/kits`, `POST /api/v1/kits/{id}/products` | 4 |
| Products | `GET /api/v1/products` | 1 |
| Orders | `POST /api/v1/orders`, `GET /api/v1/orders/{id}` | 2 |
| Fast Delivery | `POST /fast-delivery/v3.1.1/calculate-delivery` | 2 |

**Total: 11 requests with automated Postman test scripts**

Each request has `pm.test()` assertions checking:
- HTTP status code (201, 200, 400, 404, 500)
- Response body structure and field presence
- Business logic (e.g. `authToken` returned on user creation, delivery cost in valid range)

---

## How to import and run

**Option 1 — Postman Desktop**

1. Open Postman
2. Click **Import** → **File** → select `urban_routes_api_collection.json`
3. Set the `baseUrl` collection variable to your Urban Routes sandbox URL (see `.env.example` in the repo root)
4. Run individual requests or use **Collection Runner** to execute all 11 in sequence

**Option 2 — Newman (CLI)**

```bash
npm install -g newman
newman run postman/urban_routes_api_collection.json \
  --env-var "baseUrl=https://your-sandbox-url.tripleten-services.com"
```

---

## Collection variables

| Variable | Description | Example |
|----------|-------------|---------|
| `baseUrl` | Sandbox server root URL | `https://cnt-xxxxxxxx.containerhub.tripleten-services.com` |
| `userId` | Pre-seeded user ID for GET/DELETE tests | `1` |
| `kitId` | Kit ID used in product-add tests | `2` |
| `productId` | Product ID added to kit | `7` |

> The `authToken` variable is set automatically by the `POST /users` test script and used by downstream requests that require authentication.

---

## Key bugs found during Sprint 4

These defects were discovered while running this collection against the live sandbox (all logged in Jira ESP3):

| ID | Endpoint | Defect | Severity |
|----|----------|--------|----------|
| ESP3-25 | POST /kits/{id}/products | `quantity: 0` returns `200 OK` instead of `400` | High |
| ESP3-26 | POST /kits/{id}/products | Negative quantity returns `200 OK` instead of `400` | High |
| ESP3-27 | POST /kits/{id}/products | Non-existent product ID returns `200 OK` instead of `400` | High |
| ESP3-40 | POST /fast-delivery | `isItPossibleToDeliver: true` returned outside operating hours | Critical |
| ESP3-41 | POST /fast-delivery | Delivery cost stays at `6` instead of `7` past Band 6 threshold | High |

---

## Related files

- Full test design and execution report: [Sprint 4 Google Sheets](https://docs.google.com/spreadsheets/d/1wETfopGNtrBu2jTMhzAn4BkMcdOnzyEM2QrP4468LoQ/edit)
- Sprint 4 README: [`../sprint-4/README.md`](../sprint-4/README.md)
- Programmatic API tests (pytest): [`../api_db_validation/`](../api_db_validation/)
