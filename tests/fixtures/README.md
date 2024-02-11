# Note about test fixtures

In all test fixtures scraped from non-public sources, all non-public
identifiers (such as secret URLs and tokens) have been stripped and
replaced with random fake data.

For example, all `/download/…` paths have been replaced by fake data,
which was generated using the following shell command line:

```bash
python -c 'import random; print(random.randbytes(30).hex())' \
  | xxd -r -p \
  | base64 \
  | tr +/ -_
```
