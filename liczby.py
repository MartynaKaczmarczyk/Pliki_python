on: 
  push:
    branches: [master]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: "3.x"
      - name: install
        run: |
          pip install -U pytest
      - run: python3 -m pytest tests.py

suma = 2 + 5
print(suma)
