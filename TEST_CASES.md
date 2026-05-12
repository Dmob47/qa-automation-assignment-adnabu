# AdNabu QA Assignment — Manual Test Cases

This document contains manual test cases for the following modules:

- Product Search
- Add to Cart

The test cases include:
- Positive scenarios
- Negative scenarios
- Edge cases

---

# A) Product Search Test Cases

## PS-01 — Search Product Using Valid Keyword

### Type
Positive

### Steps
1. Open the website
2. Enter a valid product keyword (e.g., "Shoes")
3. Click on the Search button

### Expected Result
Relevant products matching the entered keyword are displayed successfully.

---

## PS-02 — Search Product Using Partial Keyword

### Type
Positive

### Steps
1. Open the website
2. Enter a partial keyword (e.g., "sho")
3. Click on the Search button

### Expected Result
Products containing matching text are displayed in the search results.

---

## PS-03 — Search Product Using Invalid Keyword

### Type
Negative

### Steps
1. Open the website
2. Enter an invalid keyword (e.g., "xyz123")
3. Click on the Search button

### Expected Result
A "No products found" message is displayed and no unrelated products appear.

---

## PS-04 — Search Product With Empty Search Field

### Type
Negative

### Steps
1. Open the website
2. Leave the search field empty
3. Click on the Search button

### Expected Result
A validation message is displayed OR all products are displayed without application failure.

---

## PS-05 — Search Product Using Special Characters

### Type
Edge Case

### Steps
1. Open the website
2. Enter special characters (e.g., "@#$%^&*")
3. Click on the Search button

### Expected Result
The application handles the input gracefully without crashing or breaking the UI.

---

## PS-06 — Search Product Using Leading and Trailing Spaces

### Type
Edge Case

### Steps
1. Open the website
2. Enter keyword with spaces (e.g., "   Shoes   ")
3. Click on the Search button

### Expected Result
Extra spaces are ignored and relevant products are displayed successfully.

---

# B) Add to Cart Test Cases

## AC-01 — Add Available Product to Cart

### Type
Positive

### Steps
1. Open a product page
2. Click on the "Add to Cart" button

### Expected Result
The product is added successfully and the cart count is updated correctly.

---

## AC-02 — Add Multiple Quantities of Same Product

### Type
Positive

### Steps
1. Open a product page
2. Add the same product multiple times
3. Open the cart

### Expected Result
The product quantity updates correctly in the cart.

---

## AC-03 — Add Out-of-Stock Product to Cart

### Type
Negative

### Steps
1. Open an out-of-stock product page
2. Click on the "Add to Cart" button

### Expected Result
The product is not added to the cart and an appropriate stock warning message is displayed.

---

## AC-04 — Remove Product From Cart

### Type
Positive

### Steps
1. Add a product to the cart
2. Open the cart
3. Remove the product from the cart

### Expected Result
The product is removed successfully and the cart updates correctly.

---

## AC-05 — Rapidly Click "Add to Cart" Multiple Times

### Type
Edge Case

### Steps
1. Open a product page
2. Rapidly click the "Add to Cart" button multiple times

### Expected Result
The application handles duplicate clicks properly without unexpected duplicate entries.

---

## AC-06 — Verify Cart Persistence After Page Refresh

### Type
Edge Case

### Steps
1. Add a product to the cart
2. Refresh the page
3. Open the cart

### Expected Result
The added product remains available in the cart after page refresh.

---

# Notes

- Test cases were designed to cover both functional and boundary scenarios.
- Positive, negative, and edge cases were included as per assignment requirements.
- Expected results were intentionally kept concise and clear for readability.
