from drt_sdk_core import Address
from drt_sdk_network_providers.proxy_network_provider import \
    ProxyNetworkProvider

from drt_sdk_cli.accounts import Account
from drt_sdk_cli.cli import main


def test_get_account():
    result = main(
        [
            "account",
            "get",
            "--address",
            "moa1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssfq94h8",
            "--proxy",
            "https://testnet-api.dharitri.com"
        ]
    )
    assert False if result else True


def test_sync_nonce():
    account = Account(address=Address.new_from_bech32("moa1qyu5wthldzr8wx5c9ucg8kjagg0jfs53s8nr3zpz3hypefsdd8ssfq94h8"))
    proxy = ProxyNetworkProvider("https://testnet-api.dharitri.com")
    account.sync_nonce(proxy)
    assert True if account.nonce else False


def test_query_contract():
    result = main(
        [
            "contract",
            "query",
            "moa1qqqqqqqqqqqqqpgq6qr0w0zzyysklfneh32eqp2cf383zc89d8ssxtssxl",
            "--function",
            "getSum",
            "--proxy",
            "https://devnet-api.dharitri.com",
        ]
    )
    assert False if result else True


def test_get_transaction():
    result = main(
        [
            "tx",
            "get",
            "--proxy",
            "https://devnet-api.dharitri.com",
            "--hash",
            "06f381ee88ed27ba08a35f995f17dceb737e1a99c5c4da0c247bbe7aa1d18551",
        ]
    )
    assert False if result else True
