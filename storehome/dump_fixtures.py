import subprocess
import sys

# result = subprocess.run([sys.executable, 'manage.py', 'dumpdata', 'goods.Categories'],
#                        capture_output=True, text=True, encoding='utf-8')

# with open('fixtures/goods/cats.json', 'w', encoding='utf-8') as f:
#     f.write(result.stdout)

with open('fixtures/goods/cats.json', 'r', encoding='utf-8') as f:
    data = f.read()
with open('fixtures/goods/cats.json', 'w', encoding='utf-8') as f:
    f.write(data)