all = 500
DB = 85
NET = 60
DB_NET = 35

DB_prob = DB / all
DB_or_NET_prob = (DB + NET - DB_NET) / all
DB_and_not_NET_prob = (DB - DB_NET) / all

print(f"Ймовірність помилки DB: {DB_prob*100:.2f}%")
print(f"Ймовірність помилки DB або NET: {DB_or_NET_prob*100:.2f}%")
print(f"Ймовірність помилки DB, але не NET: {DB_and_not_NET_prob*100:.2f}%")