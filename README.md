# 🚀 URL Shortener API (Mid-Term Final Checklist)

## Project Members

Pooriya Morajab implemented : Redirect, Delete, TTL, Cleanup

Morteza Maddah implemented : Create short links, List shortened Links

---

## 1. API Test Coverage Table

Fill in the second column with the name of the student who implemented

and tested each API.

| # | API Endpoint / Feature                         | Implemented & Tested By (Student Name) |
|---|-----------------------------------------------|----------------------------------------|
| 1 | Create Short Link – POST /urls                 | Morteza                                |
| 2 | Redirect to Original URL – GET /u/{code}       | Pooriya                                |
| 3 | Get All Shortened Links – GET /urls            | Morteza                                |
| 4 | Delete Short Link – DELETE /urls/{code}        | Pooriya                                |

---

## 2. Code Generation Method 

Check the method you used to generate the short code:

- [ ] 1. Random Generation

- [x] 2. ID → Base62 Conversion

- [ ] 3. Hash-based Generation

(Only select the one you actually implemented.)

Verification: The project uses the ID-based method where the database ID is encoded into a Base62 string using the encode_base62 function.

---

## 3. Bonus User Story: TTL (Expiration Time) for Shortened Links)

If you implemented the bonus user story, mark the box and complete the

required details.

- [x] TTL Feature Implemented

Verification: The TTL feature is implemented via delete_expired in the URLRepository and exposed via delete_expired_urls in URLService.

If checked, fill in the following information:

ENV variable or config key used:

```env
APP_TTL_MINUTES=1
```
---

### Location of TTL Logic (File + Function):

File : url_shortner/repositories/url_repository.py 

Function : delete_expired()

---

### How TTL cleanup is triggered:

You must write a Command that removes expired links (created_at + TTL < now()).

Inorder to remove expired links we can run this command in the terminal:

```env
python commands/cleanup.py
```

It basically deletes all urls where :
```env
URL.created_at < expiration_time
```

---

## 4. Postman Collection (Required)

A Postman Collection has been created and includes all four API routes:

- POST /urls 
- GET /u/{code} 
- GET /urls 
- DELETE /urls/{code} 

---

### Screenshots (included in GitHub)

For each route, two screenshots have been added:

- Successful response (2xx)
- Error-handled response (4xx)

Screenshots are located in:

```env
/postman
```
---

### Naming Example:

postman/
```env
post-urls-201-success.png
post-urls-400-invalid-url.png
get-u-code-307-redirect.png
get-u-code-404-not-found.png
get-urls-200-success.png
delete-urls-code-204-success.png
delete-urls-code-404-not-found.png
Filenames must clearly show:
```
- Route

- HTTP status

- Success or error














