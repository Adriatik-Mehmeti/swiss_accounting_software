# Swiss Accounting Software (Forked & Enhanced)

<p align="center">
  <img src="https://raw.githubusercontent.com/Adriatik-Mehmeti/swiss_accounting_software/refs/heads/version-15/swiss_accounting_software/public/img/logo.svg" alt="Swiss Accounting Software Logo" width="160">
</p>

## Description
Swiss Accounting Software is a Frappe app focused on Swiss requirements, including true-to-standard QR invoices.  
This repository is **forked** and **improved** for clearer invoice layouts, better documentation, and a smoother setup.

---

## Features
- QR-compliant Swiss invoices (SPC/QR-Bill) with clean, structured layout.
- Integrated payment slip (receipt) with scannable QR.
- Clear separation of header, reference, amount, due date, and payment details.
- Export for Abacus

---

## Example A4 Invoice

<p align="center">
  <a href="https://raw.githubusercontent.com/Adriatik-Mehmeti/swiss_accounting_software/refs/heads/version-15/swiss_accounting_software/public/img/Test.pdf.png" target="_blank">
    <img src="https://raw.githubusercontent.com/Adriatik-Mehmeti/swiss_accounting_software/refs/heads/version-15/swiss_accounting_software/public/img/Test.pdf.png" alt="Example Swiss QR Invoice (A4)" width="700">
  </a>
</p>

**Credits:**
- **fork:** Repo is forked and improved.


---

## Installation (Frappe/Bench, v15)

> **Prerequisites:** A working Frappe/Bench environment (v15) with Redis, MariaDB, Node.js, and Yarn.  
> If you don’t have Bench set up yet, follow the [official Frappe installation guide](https://frappeframework.com/docs/user/en/installation).

```bash
# 1) Go to your bench
cd ~/frappe-bench

# 2) Get the app (version-15 branch)
bench get-app
  https://github.com/Adriatik-Mehmeti/swiss_accounting_software.git --branch version-15

# 3) Create a site (if you don’t have one yet)
bench new-site mysite.local

# 4) Install the app on your site
bench --site mysite.local install-app swiss_accounting_software

# 5) Apply patches / build assets / restart
bench --site mysite.local migrate
bench build
bench restart
