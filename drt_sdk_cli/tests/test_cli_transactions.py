import json
from pathlib import Path
from typing import Any

from drt_sdk_cli.cli import main

testdata_path = Path(__file__).parent / "testdata"


def test_relayed_v1_transaction(capsys: Any):
    multi_user_pem = testdata_path / "multiple_addresses.pem"
    address_index = 1

    return_code = main([
        "tx", "new",
        "--pem", str(multi_user_pem),
        "--pem-index", str(address_index),
        "--receiver", "moa1qqqqqqqqqqqqqqqpqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqzllls29jpxv",
        "--nonce", "198",
        "--gas-limit", "60000000",
        "--data", "getContractConfig",
        "--version", "1",
        "--chain", "T",
        "--relay"
    ])
    assert False if return_code else True

    relayed_tx = _read_stdout(capsys)
    assert relayed_tx == "relayedTx@7b226e6f6e6365223a3139382c2273656e646572223a2267456e574f65576d6d413063306a6b71764d354241707a61644b46574e534f69417643575163776d4750673d222c227265636569766572223a22414141414141414141414141415141414141414141414141414141414141414141414141414141432f2f383d222c2276616c7565223a302c226761735072696365223a313030303030303030302c226761734c696d6974223a36303030303030302c2264617461223a225a3256305132397564484a68593352446232356d6157633d222c227369676e6174757265223a2276414f36414958687677774b4930767270665471643854567463597268456630714e6e324539734a4e6c6b315268326b2b37725a69344d48492b7133696c54366d3649302f63457554314d6b6f6d4e314775676c44513d3d222c22636861696e4944223a2256413d3d222c2276657273696f6e223a317d"


def test_create_tx_and_sign_by_hash(capsys: Any):
    return_code = main([
        "tx", "new",
        "--pem", str(testdata_path / "alice.pem"),
        "--receiver", "moa1spyavw0956vq68xj8y4tenjpq2wd5a9p2c6j8gsz7ztyrnpxrruq0yu4wk",
        "--nonce", "89",
        "--gas-limit", "50000",
        "--version", "2",
        "--options", "1",
        "--chain", "integration tests chain ID",
    ])
    assert False if return_code else True

    tx = _read_stdout(capsys)
    tx_json = json.loads(tx)
    signature = tx_json["emittedTransaction"]["signature"]
    assert signature == "e55e641a75b4357269bb576ec597aac8ef9650c8d37a75d4fc6c67ef78703e9dc8de17dca8a3b207610e202a3faea80f92f6e5b7b95d4fb91136d97c9167dc08"


def _read_stdout(capsys: Any) -> str:
    return capsys.readouterr().out.strip()
