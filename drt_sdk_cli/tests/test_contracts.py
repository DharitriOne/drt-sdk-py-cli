import logging
from pathlib import Path

import pytest
from Cryptodome.Hash import keccak
from drt_sdk_core.address import Address

from drt_sdk_cli import errors
from drt_sdk_cli.accounts import Account
from drt_sdk_cli.contract_verification import _create_request_signature
from drt_sdk_cli.contracts import (_interpret_as_number_if_safely,
                                          _prepare_argument,
                                          prepare_args_for_factory)

logging.basicConfig(level=logging.INFO)

testdata_folder = Path(__file__).parent / "testdata"


def test_playground_keccak():
    hexhash = keccak.new(digest_bits=256).update(b"").hexdigest()
    assert hexhash == "c5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470"


def test_prepare_argument():
    assert _prepare_argument('0x5') == '05'
    assert _prepare_argument('5') == '05'
    assert _prepare_argument('0x05f') == '005F'
    assert _prepare_argument('0xaaa') == '0AAA'
    assert _prepare_argument('str:a') == '61'
    assert _prepare_argument('str:aaa') == '616161'

    assert _prepare_argument(155) == '9B'
    assert _prepare_argument('155') == '9B'

    assert \
        _prepare_argument('moa1qr9av6ar4ymr05xj93jzdxyezdrp6r4hz6u0scz4dtzvv7kmllds5xyehg') == \
        '00CBD66BA3A93637D0D22C6426989913461D0EB716B8F860556AC4C67ADBFFDB'

    assert _prepare_argument('str:TOK-123456') == '544F4B2D313233343536'
    assert _prepare_argument('str:TOK-a1c2ef') == '544F4B2D613163326566'
    assert _prepare_argument('str:TokenName') == '546F6B656E4E616D65'
    assert _prepare_argument('str:/#%placeholder&*') == '2F2325706C616365686F6C646572262A'

    assert _prepare_argument(True) == "01"
    assert _prepare_argument(False) == "00"
    assert _prepare_argument("TrUe") == "01"
    assert _prepare_argument("fAlSe") == "00"

    with pytest.raises(errors.UnknownArgumentFormat):
        _ = _prepare_argument('0x05fq')

    assert _prepare_argument("str:") == ""
    assert _prepare_argument("0x") == ""


def test_contract_verification_create_request_signature():
    account = Account(pem_file=str(testdata_folder / "walletKey.pem"))
    contract_address = Address.from_bech32("moa1qqqqqqqqqqqqqpgqeyj9g344pqguukajpcfqz9p0rfqgyg4l396q5g8zyx")
    request_payload = b"test"
    signature = _create_request_signature(account, contract_address, request_payload)

    assert signature.hex() == "16f2cece69cd6b0cc811760beb0a072792d71ed4e2920912bd1e120e0b35a5bcffc98ea37a935e156641007bafe9a86c15ad13d46caff5f986a535774222d20f"


def test_interpret_as_number_if_safely():
    assert _interpret_as_number_if_safely("") == 0
    assert _interpret_as_number_if_safely("0x5") == 5
    assert _interpret_as_number_if_safely("FF") == 255


def test_prepare_args_for_factories():
    args = [
        "0x5", "123", "false", "true",
        "str:test-string",
        "moa1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssfq94h8"
    ]

    arguments = prepare_args_for_factory(args)
    assert arguments[0] == b"\x05"
    assert arguments[1] == 123
    assert arguments[2] == False
    assert arguments[3] == True
    assert arguments[4] == "test-string"
    assert arguments[5].to_bech32() == "moa1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssfq94h8"
