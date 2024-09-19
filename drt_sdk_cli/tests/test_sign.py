import json
from pathlib import Path
from drt_sdk_cli.cli import main


def test_sign_tx():
    parent = Path(__file__).parent
    unsigned_transaction = parent / "testdata" / "transaction.json"
    signed_transaction = parent / "testdata-out" / "signed_transaction.json"
    expected_signature = "13db840304d36b4a91fc754abafe35028f58ea2de031697630e92f56b5d9399b0864ca98264312f62ae808cbaa74cec2e53efdc16f1b9a2e6e455c33e0dd4302"

    main([
        "tx",
        "sign",
        "--pem",
        f"{parent}/testdata/testUser.pem",
        "--infile",
        f"{unsigned_transaction}",
        "--outfile",
        f"{signed_transaction}"
    ])

    with open(signed_transaction) as f:
        signed_tx = json.load(f)

    assert signed_tx["emittedTransaction"]["signature"] == expected_signature
