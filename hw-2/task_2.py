# RBAC — Role-Based Access Control
import itertools

import pandas as pd


def is_base_user(is_employee, is_verified, is_premium, is_admin, is_banned):
    return is_employee and is_verified and not is_banned

def is_premium_user(is_employee, is_verified, is_premium, is_admin, is_banned):
    return (is_employee or is_premium) and is_verified and not is_banned

def is_admin_user(is_employee, is_verified, is_premium, is_admin, is_banned):
    return is_admin and is_verified and not is_banned

def is_secret_user(is_employee, is_verified, is_premium, is_admin, is_banned):
    return (is_admin or (is_employee and is_premium)) and is_verified and not is_banned

def check_access(is_employee, is_verified, is_premium, is_admin, is_banned):
    return {
        'Base': is_base_user(is_employee, is_verified, is_premium, is_admin, is_banned),
        'Premium': is_premium_user(is_employee, is_verified, is_premium, is_admin, is_banned),
        'Admin': is_admin_user(is_employee, is_verified, is_premium, is_admin, is_banned),
        'Secret': is_secret_user(is_employee, is_verified, is_premium, is_admin, is_banned)
    }

input_columns = [
    'is_Employee',
    'is_Verified',
    'is_Premium',
    'is_Admin',
    'is_Banned',
]

rows = []
test_data = itertools.product([True, False], repeat=5)
for data in test_data:
    row = dict(zip(input_columns, data))
    row.update(check_access(*data))
    rows.append(row)

access_table = pd.DataFrame(rows)
access_table = access_table.replace({True: 1, False: 0})

print(access_table)