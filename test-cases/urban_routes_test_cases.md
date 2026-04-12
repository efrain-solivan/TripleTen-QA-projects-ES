# Urban Routes — Manual Test Cases
**Project:** TripleTen QA Engineering Apprenticeship  
**App:** Urban Routes — Ride-Hailing Web Application  
**Author:** Efrain Solivan  
**Jira Project:** ESP3  
**Format:** ID · Title · Preconditions · Steps · Expected Result · Actual Result · Status

---

## Sprint 1 — Map & Address Behavior

---

### TC-S1-01: Enter a valid origin address in the "From" field

| Field | Detail |
|---|---|
| **ID** | TC-S1-01 |
| **Title** | Enter a valid origin address in the "From" field |
| **Priority** | High |
| **Type** | Positive |

**Preconditions:**  
- Urban Routes is open in a supported browser  
- The main map screen is displayed  

**Steps:**  
1. Click the "From" input field  
2. Type "123 Main St"  
3. Select the first suggestion from the autocomplete dropdown  

**Expected Result:**  
The "From" field displays "123 Main St" and a pin is placed on the map at the corresponding location.  

**Actual Result:** Field auto-populates a random address when clicked (before user input).  
**Status:** FAIL — Bug ESP3-1

---

### TC-S1-02: Enter a valid destination address in the "To" field

| Field | Detail |
|---|---|
| **ID** | TC-S1-02 |
| **Title** | Enter a valid destination address in the "To" field |
| **Priority** | High |
| **Type** | Positive |

**Preconditions:**  
- "From" address is already set  

**Steps:**  
1. Click the "To" input field  
2. Type "Times Square"  
3. Select the first autocomplete suggestion  

**Expected Result:**  
The "To" field displays "Times Square" and a route line appears on the map connecting origin to destination.  

**Actual Result:** Field auto-populates an address without user input.  
**Status:** FAIL — Bug ESP3-13

---

### TC-S1-03: Search for "Subway" station in the "To" field

| Field | Detail |
|---|---|
| **ID** | TC-S1-03 |
| **Title** | Typing "Subway" shows subway station suggestions |
| **Priority** | High |
| **Type** | Positive |

**Preconditions:**  
- Map screen is loaded  

**Steps:**  
1. Click the "To" field  
2. Type "Subway"  
3. Wait for autocomplete suggestions  

**Expected Result:**  
A list of nearby subway stations appears in the dropdown.  

**Actual Result:** No subway station list appears.  
**Status:** FAIL — Bug ESP3-2

---

### TC-S1-04: Map zooms after address is entered

| Field | Detail |
|---|---|
| **ID** | TC-S1-04 |
| **Title** | Map zooms to address pin after user inputs an address |
| **Priority** | Low |
| **Type** | Positive |

**Preconditions:**  
- A valid address has been entered in the "From" field  

**Steps:**  
1. Enter a valid address in the "From" field  
2. Observe the map behavior  

**Expected Result:**  
The map zooms to center on the address pin.  

**Actual Result:** Map does not zoom to the address pin.  
**Status:** FAIL — Bug ESP3-4

---

## Sprint 2 — Payment Card Validation

---

### TC-S2-01: Add a valid 12-digit card number

| Field | Detail |
|---|---|
| **ID** | TC-S2-01 |
| **Title** | Card number field accepts exactly 12 digits |
| **Priority** | High |
| **Type** | Positive |

**Preconditions:**  
- User has selected a route and tariff  
- Payment modal is open  

**Steps:**  
1. Open the payment modal  
2. Click "Add card"  
3. Enter "123400005678" (12 digits)  
4. Enter CVV "12"  
5. Click "Add"  

**Expected Result:**  
Card is added successfully and displayed in the payment method list.  

**Actual Result:** Card accepted.  
**Status:** PASS

---

### TC-S2-02: Card number field rejects fewer than 12 digits

| Field | Detail |
|---|---|
| **ID** | TC-S2-02 |
| **Title** | Card number field rejects input with fewer than 12 digits |
| **Priority** | High |
| **Type** | Negative (boundary) |

**Preconditions:**  
- Payment modal → Add card screen is open  

**Steps:**  
1. Enter "12340000567" (11 digits) in the card number field  
2. Enter a valid CVV  
3. Click "Add"  

**Expected Result:**  
An error message appears indicating the card number must be 12 digits.  

**Actual Result:** Field accepts fewer than 12 characters — card is added without error.  
**Status:** FAIL — Bug ESP3-16

---

### TC-S2-03: Card number field rejects more than 12 digits

| Field | Detail |
|---|---|
| **ID** | TC-S2-03 |
| **Title** | Card number field rejects input with more than 12 digits |
| **Priority** | High |
| **Type** | Negative (boundary) |

**Preconditions:**  
- Payment modal → Add card screen is open  

**Steps:**  
1. Enter "1234000056789" (13 digits)  
2. Enter a valid CVV  
3. Click "Add"  

**Expected Result:**  
Input is truncated to 12 digits or an error message is shown.  

**Actual Result:** Field accepts more than 12 characters.  
**Status:** FAIL — Bug ESP3-17

---

### TC-S2-04: Card number field rejects alphabetical characters

| Field | Detail |
|---|---|
| **ID** | TC-S2-04 |
| **Title** | Card number field rejects letters |
| **Priority** | High |
| **Type** | Negative |

**Preconditions:**  
- Add card screen is open  

**Steps:**  
1. Enter "abcdefghijkl" in the card number field  
2. Click "Add"  

**Expected Result:**  
Error: card number must contain digits only.  

**Actual Result:** Field accepts alphabetical characters.  
**Status:** FAIL — Bug ESP3-18

---

### TC-S2-05: CVV field rejects fewer than 2 digits

| Field | Detail |
|---|---|
| **ID** | TC-S2-05 |
| **Title** | CVV field rejects fewer than 2 digits |
| **Priority** | High |
| **Type** | Negative (boundary) |

**Preconditions:**  
- Add card screen is open; valid card number already entered  

**Steps:**  
1. Enter "1" in the CVV field  
2. Click "Add"  

**Expected Result:**  
Error: CVV must be exactly 2 digits.  

**Actual Result:** CVV field accepts fewer than 2 digits.  
**Status:** FAIL — Bug ESP3-22

---

## Sprint 3 — API: Kits Endpoint

---

### TC-S3-01: POST /kits — Create kit with valid name (1–8 chars)

| Field | Detail |
|---|---|
| **ID** | TC-S3-01 |
| **Title** | POST /api/v1/kits creates a kit with a valid name |
| **Priority** | High |
| **Type** | Positive |

**Preconditions:**  
- Valid authToken obtained  
- Postman or equivalent REST client is available  

**Steps:**  
1. Send `POST /api/v1/kits` with body: `{"name": "My Kit"}`  
2. Include Authorization header with valid token  

**Expected Result:**  
`201 Created` — Response body contains the new kit's `id` and `name`.  

**Actual Result:** 201 returned with kit id.  
**Status:** PASS

---

### TC-S3-02: POST /kits/:id/products — quantity = 0 returns 400

| Field | Detail |
|---|---|
| **ID** | TC-S3-02 |
| **Title** | Adding product with quantity 0 should return 400 |
| **Priority** | High |
| **Type** | Negative |

**Preconditions:**  
- Valid kit id exists  
- Valid product id exists  

**Steps:**  
1. Send `POST /api/v1/kits/2/products`  
2. Body: `{"productsList": [{"id": 7, "quantity": 0}]}`  

**Expected Result:**  
`400 Bad Request` — quantity must be ≥ 1.  

**Actual Result:** Returns `200 OK` — product added with quantity 0.  
**Status:** FAIL — Bug ESP3-25

---

### TC-S3-03: POST /kits/:id/products — negative quantity returns 400

| Field | Detail |
|---|---|
| **ID** | TC-S3-03 |
| **Title** | Adding product with negative quantity should return 400 |
| **Priority** | High |
| **Type** | Negative |

**Preconditions:**  
- Valid kit id and product id exist  

**Steps:**  
1. Send `POST /api/v1/kits/10/products`  
2. Body: `{"productsList": [{"id": 7, "quantity": -1}]}`  

**Expected Result:**  
`400 Bad Request`  

**Actual Result:** Returns `200 OK`  
**Status:** FAIL — Bug ESP3-26

---

## Sprint 4 — API: Fast Delivery

---

### TC-S4-01: POST /fast-delivery — eligible order (≤6kg, ≤6 items)

| Field | Detail |
|---|---|
| **ID** | TC-S4-01 |
| **Title** | Fast delivery returns isItPossibleToDeliver: true for eligible order |
| **Priority** | High |
| **Type** | Positive |

**Preconditions:**  
- API is reachable in sandbox environment  

**Steps:**  
1. Send `POST /fast-delivery/v3.1.1/calculate-delivery`  
2. Body: `{"dlvType": "fast", "productsCount": 2, "productsWeight": 3}`  
3. Current time is within operating hours (08:00–22:00)  

**Expected Result:**  
`200 OK` — `{"isItPossibleToDeliver": true, "deliveryCost": <valid cost>}`  

**Actual Result:** Returns correct response.  
**Status:** PASS

---

### TC-S4-02: POST /fast-delivery — request outside operating hours returns false

| Field | Detail |
|---|---|
| **ID** | TC-S4-02 |
| **Title** | isItPossibleToDeliver should be false outside operating hours |
| **Priority** | Critical |
| **Type** | Negative |

**Preconditions:**  
- API accessible; currentTime set to 03:00 (outside 08:00–22:00 window)  

**Steps:**  
1. Send `POST /fast-delivery/v3.1.1/calculate-delivery`  
2. Body: `{"dlvType": "fast", "productsCount": 2, "productsWeight": 3, "currentTime": "03:00"}`  

**Expected Result:**  
`{"isItPossibleToDeliver": false}`  

**Actual Result:** Returns `{"isItPossibleToDeliver": true}` — delivery offered outside operating hours.  
**Status:** FAIL — Bug ESP3-40

---

## Sprint 5 — UI Automation (Selenium)

---

### TC-S5-01: Set route via Selenium

| Field | Detail |
|---|---|
| **ID** | TC-S5-01 |
| **Title** | Automated test sets origin and destination |
| **Priority** | High |
| **Type** | Positive / Automated |

**Preconditions:**  
- ChromeDriver matches installed Chrome  
- `pytest` and `selenium` installed  
- TripleTen sandbox URL reachable  

**Steps:**  
1. Run `pytest selenium/test_urban_routes.py::TestOrderFlow::test_set_route -v`  

**Expected Result:**  
Test passes — "From" and "To" fields display the correct addresses.  

**Actual Result:** PASS  
**Status:** PASS

---

### TC-S5-02: Automated full order flow

| Field | Detail |
|---|---|
| **ID** | TC-S5-02 |
| **Title** | Full taxi order flow completes via automation |
| **Priority** | High |
| **Type** | End-to-End / Automated |

**Preconditions:**  
- Same as TC-S5-01  

**Steps:**  
1. Run `pytest selenium/test_urban_routes.py -v`  
2. Steps execute: set route → Comfort tariff → phone → card → comment → blanket → ice cream → order  

**Expected Result:**  
All 9 tests pass; order confirmation modal and driver info panel appear.  

**Actual Result:** PASS (with sandbox SMS code caveat)  
**Status:** PASS

---

## Test Summary

| Sprint | Total TCs | Pass | Fail | Blocked |
|---|---|---|---|---|
| Sprint 1 — Map & Address | 4 | 0 | 4 | 0 |
| Sprint 2 — Card Validation | 5 | 1 | 4 | 0 |
| Sprint 3 — API: Kits | 3 | 1 | 2 | 0 |
| Sprint 4 — API: Fast Delivery | 2 | 1 | 1 | 0 |
| Sprint 5 — UI Automation | 2 | 2 | 0 | 0 |
| **Total** | **16** | **5** | **11** | **0** |

> All defects are logged in Jira under project **ESP3**.
