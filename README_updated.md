
# Persistent Retroactive Banking System

## Overview

This is a Django-based web application that simulates a fully retroactive and partially persistent banking system. It allows users to:

- Create accounts with an initial balance  
- Perform deposits, withdrawals, and transfers  
- Add operations retroactively by specifying a timestamp  
- View balances at any past version (timestamp)  
- Retroactively insert or rollback operations by timestamp and type  

The backend is powered by a custom `PersistentRetroactiveAccountSystem` class that simulates partial persistence and partial retroactivity in memory.

---

## Implementation

### Backend Class: `PersistentRetroactiveAccountSystem`

- Maintains an operations list of tuples: `(timestamp, operation_type, data)`  
- All operations (create, deposit, withdraw, transfer, rollback) are versioned  
- Balances are recalculated using historical simulation via `get_balance()`  
- Rollback removes only the specified operation  

### Web Interface

- Built using Django  
- Views handle GET requests with optional timestamps  
- Balances are dynamically computed using versioned history  

---

## Steps to Import and Run the Application

### 1. Clone the Repository

```bash
git clone https://github.com/Abhijeet399/Project_ADS_Persistance_Retroactive.git
cd persistent-retroactive-transactions
```

### 2. Installation Instructions

Install Django (preferably version >= 4):

```bash
pip install Django
```

### 3. Run the Web Application

Run migrations:

```bash
python manage.py migrate
```

Start the development server:

```bash
python manage.py runserver
```

Open your browser and go to:  
[http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Sample Use Case to Try

### Create Accounts

- Create `user1` with a balance of 120 at `t0`  
- Create `user2` with a balance of 520 at `t1`  

### Deposit to user1

- Deposit 120 to `user1` at `t2`

### Withdraw from user2

- Withdraw 30 from `user2` at `t3`

### Transfer

- Transfer 50 from `user2` to `user1` at `t4`

### Retroactive Operation

- Withdraw 50 from `user1` at `t2` (retroactively)

### View Balance

- Go to **View Balances** and enter timestamp `2`  
  You should see:

```
user1: 120 (initial) + 120 (deposit) - 50 (withdraw) = 190  
user2: 520 (no change by t2) = 520  
```

### Rollback a Specific Operation

- Enter:  
  **Timestamp:** 2  
  **Operation:** withdraw  

This will undo **only** the withdraw operation at `t2` without affecting future operations.
