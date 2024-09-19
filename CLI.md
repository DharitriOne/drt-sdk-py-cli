# Command Line Interface

## Overview

**drtpy** exposes a number of CLI **commands**, organized within **groups**.

```
$ drtpy --help
usage: drtpy [-h] [-v] [--verbose] COMMAND-GROUP [-h] COMMAND ...

-----------
DESCRIPTION
-----------
drtpy is part of the drt-sdk and consists of Command Line Tools and Python SDK
for interacting with the Blockchain (in general) and with Smart Contracts (in particular).

drtpy targets a broad audience of users and developers.

See:
 - https://docs.dharitri.com/sdk-and-tools/sdk-py
 - https://docs.dharitri.com/sdk-and-tools/sdk-py/drtpy-cli


COMMAND GROUPS:
  {contract,tx,validator,account,ledger,wallet,deps,config,localnet,data,staking-provider,dns}

TOP-LEVEL OPTIONS:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  --verbose

----------------------
COMMAND GROUPS summary
----------------------
contract                       Build, deploy, upgrade and interact with Smart Contracts
tx                             Create and broadcast Transactions
validator                      Stake, UnStake, UnBond, Unjail and other actions useful for Validators
account                        Get Account data (nonce, balance) from the Network
ledger                         Get Ledger App addresses and version
wallet                         Create wallet, derive secret key from mnemonic, bech32 address helpers etc.
deps                           Manage dependencies or drt-sdk modules
config                         Configure drt-sdk (default values etc.)
localnet                       Set up, start and control localnets
data                           Data manipulation omnitool
staking-provider               Staking provider omnitool
dns                            Operations related to the Domain Name Service

```

## Group **Contract**

```
$ drtpy contract --help
usage: drtpy contract COMMAND [-h] ...

Build, deploy, upgrade and interact with Smart Contracts

COMMANDS:
  {new,templates,build,clean,test,report,deploy,call,upgrade,query,verify,reproducible-build}

OPTIONS:
  -h, --help            show this help message and exit

----------------
COMMANDS summary
----------------
new                            Create a new Smart Contract project based on a template.
templates                      List the available Smart Contract templates.
build                          Build a Smart Contract project.
clean                          Clean a Smart Contract project.
test                           Run scenarios (tests).
report                         Print a detailed report of the smart contracts.
deploy                         Deploy a Smart Contract.
call                           Interact with a Smart Contract (execute function).
upgrade                        Upgrade a previously-deployed Smart Contract.
query                          Query a Smart Contract (call a pure function)
verify                         Verify the authenticity of the code of a deployed Smart Contract
reproducible-build             Build a Smart Contract and get the same output as a previously built Smart Contract

```

### Contract.New

```
$ drtpy contract new --help
usage: drtpy contract new [-h] ...

Create a new Smart Contract project based on a template.

options:
  -h, --help           show this help message and exit
  --name NAME          The name of the contract. If missing, the name of the template will be used.
  --template TEMPLATE  the template to use
  --tag TAG            the framework version on which the contract should be created
  --path PATH          the parent directory of the project (default: current directory)

```

### Contract.Templates

```
$ drtpy contract templates --help
usage: drtpy contract templates [-h] ...

List the available Smart Contract templates.

options:
  -h, --help  show this help message and exit
  --tag TAG   the sc-meta framework version referred to

```

### Contract.Build

```
$ drtpy contract build --help
usage: drtpy contract build [-h] ...

Build a Smart Contract project.

options:
  -h, --help                 show this help message and exit
  --path PATH                the project directory (default: current directory)
  --no-wasm-opt              do not optimize wasm files after the build (default: False)
  --wasm-symbols             for rust projects, does not strip the symbols from the wasm output. Useful for analysing
                             the bytecode. Creates larger wasm files. Avoid in production (default: False)
  --wasm-name WASM_NAME      for rust projects, optionally specify the name of the wasm bytecode output file
  --wasm-suffix WASM_SUFFIX  for rust projects, optionally specify the suffix of the wasm bytecode output file
  --target-dir TARGET_DIR    for rust projects, forward the parameter to Cargo
  --wat                      also generate a WAT file when building
  --mir                      also emit MIR files when building
  --llvm-ir                  also emit LL (LLVM) files when building
  --ignore IGNORE            ignore all directories with these names. [default: target]
  --no-imports               skips extracting the EI imports after building the contracts
  --no-abi-git-version       skips loading the Git version into the ABI
  --twiggy-top               generate a twiggy top report after building
  --twiggy-paths             generate a twiggy paths report after building
  --twiggy-monos             generate a twiggy monos report after building
  --twiggy-dominators        generate a twiggy dominators report after building

```

### Contract.Clean

```
$ drtpy contract clean --help
usage: drtpy contract clean [-h] ...

Clean a Smart Contract project.

options:
  -h, --help   show this help message and exit
  --path PATH  the project directory (default: current directory)

```

### Contract.Deploy

```
$ drtpy contract deploy --help
usage: drtpy contract deploy [-h] ...

Deploy a Smart Contract.

Output example:
===============
{
    "emittedTransaction": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "emittedTransactionData": "the transaction data, not encoded",
    "emittedTransactionHash": "the transaction hash",
    "contractAddress": "the address of the contract",
    "transactionOnNetwork": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "simulation": {
        "execution": {
            "...": "..."
        },
        "cost": {
            "...": "..."
        }
    }
}

options:
  -h, --help                                      show this help message and exit
  --bytecode BYTECODE                             the file containing the WASM bytecode
  --metadata-not-upgradeable                      ‼ mark the contract as NOT upgradeable (default: upgradeable)
  --metadata-not-readable                         ‼ mark the contract as NOT readable (default: readable)
  --metadata-payable                              ‼ mark the contract as payable (default: not payable)
  --metadata-payable-by-sc                        ‼ mark the contract as payable by SC (default: not payable by SC)
  --outfile OUTFILE                               where to save the output (default: stdout)
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --proxy PROXY                                   🔗 the URL of the proxy
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --arguments ARGUMENTS [ARGUMENTS ...]           arguments for the contract transaction, as [number, bech32-address,
                                                  ascii string, boolean] or hex-encoded. E.g. --arguments 42 0x64 1000
                                                  0xabba str:TOK-a1c2ef true moa1[..]
  --wait-result                                   signal to wait for the transaction result - only valid if --send is
                                                  set
  --timeout TIMEOUT                               max num of seconds to wait for result - only valid if --wait-result is
                                                  set
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### Contract.Call

```
$ drtpy contract call --help
usage: drtpy contract call [-h] ...

Interact with a Smart Contract (execute function).

Output example:
===============
{
    "emittedTransaction": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "emittedTransactionData": "the transaction data, not encoded",
    "emittedTransactionHash": "the transaction hash",
    "contractAddress": "the address of the contract",
    "transactionOnNetwork": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "simulation": {
        "execution": {
            "...": "..."
        },
        "cost": {
            "...": "..."
        }
    }
}

positional arguments:
  contract                                        🖄 the address of the Smart Contract

options:
  -h, --help                                      show this help message and exit
  --outfile OUTFILE                               where to save the output (default: stdout)
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --proxy PROXY                                   🔗 the URL of the proxy
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --function FUNCTION                             the function to call
  --arguments ARGUMENTS [ARGUMENTS ...]           arguments for the contract transaction, as [number, bech32-address,
                                                  ascii string, boolean] or hex-encoded. E.g. --arguments 42 0x64 1000
                                                  0xabba str:TOK-a1c2ef true moa1[..]
  --token-transfers TOKEN_TRANSFERS [TOKEN_TRANSFERS ...]
                                                  token transfers for transfer & execute, as [token, amount] E.g.
                                                  --token-transfers NFT-123456-0a 1 DCDT-987654 100000000
  --wait-result                                   signal to wait for the transaction result - only valid if --send is
                                                  set
  --timeout TIMEOUT                               max num of seconds to wait for result - only valid if --wait-result is
                                                  set
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --relay                                         whether to relay the transaction (default: False)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### Contract.Upgrade

```
$ drtpy contract upgrade --help
usage: drtpy contract upgrade [-h] ...

Upgrade a previously-deployed Smart Contract.

Output example:
===============
{
    "emittedTransaction": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "emittedTransactionData": "the transaction data, not encoded",
    "emittedTransactionHash": "the transaction hash",
    "contractAddress": "the address of the contract",
    "transactionOnNetwork": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "simulation": {
        "execution": {
            "...": "..."
        },
        "cost": {
            "...": "..."
        }
    }
}

positional arguments:
  contract                                        🖄 the address of the Smart Contract

options:
  -h, --help                                      show this help message and exit
  --outfile OUTFILE                               where to save the output (default: stdout)
  --bytecode BYTECODE                             the file containing the WASM bytecode
  --metadata-not-upgradeable                      ‼ mark the contract as NOT upgradeable (default: upgradeable)
  --metadata-not-readable                         ‼ mark the contract as NOT readable (default: readable)
  --metadata-payable                              ‼ mark the contract as payable (default: not payable)
  --metadata-payable-by-sc                        ‼ mark the contract as payable by SC (default: not payable by SC)
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --proxy PROXY                                   🔗 the URL of the proxy
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --arguments ARGUMENTS [ARGUMENTS ...]           arguments for the contract transaction, as [number, bech32-address,
                                                  ascii string, boolean] or hex-encoded. E.g. --arguments 42 0x64 1000
                                                  0xabba str:TOK-a1c2ef true moa1[..]
  --wait-result                                   signal to wait for the transaction result - only valid if --send is
                                                  set
  --timeout TIMEOUT                               max num of seconds to wait for result - only valid if --wait-result is
                                                  set
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### Contract.Query

```
$ drtpy contract query --help
usage: drtpy contract query [-h] ...

Query a Smart Contract (call a pure function)

positional arguments:
  contract                               🖄 the address of the Smart Contract

options:
  -h, --help                             show this help message and exit
  --proxy PROXY                          🔗 the URL of the proxy
  --function FUNCTION                    the function to call
  --arguments ARGUMENTS [ARGUMENTS ...]  arguments for the contract transaction, as [number, bech32-address, ascii
                                         string, boolean] or hex-encoded. E.g. --arguments 42 0x64 1000 0xabba
                                         str:TOK-a1c2ef true moa1[..]

```

### Contract.Report

```
$ drtpy contract report --help
usage: drtpy contract report [-h] ...

Print a detailed report of the smart contracts.

options:
  -h, --help                                      show this help message and exit
  --skip-build                                    skips the step of building of the wasm contracts
  --skip-twiggy                                   skips the steps of building the debug wasm files and running twiggy
  --output-format {github-markdown,text-markdown,json}
                                                  report output format (default: text-markdown)
  --output-file OUTPUT_FILE                       if specified, the output is written to a file, otherwise it's written
                                                  to the standard output
  --compare report-1.json [report-2.json ...]     create a comparison from two or more reports
  --path PATH                                     the project directory (default: current directory)
  --no-wasm-opt                                   do not optimize wasm files after the build (default: False)
  --wasm-symbols                                  for rust projects, does not strip the symbols from the wasm output.
                                                  Useful for analysing the bytecode. Creates larger wasm files. Avoid in
                                                  production (default: False)
  --wasm-name WASM_NAME                           for rust projects, optionally specify the name of the wasm bytecode
                                                  output file
  --wasm-suffix WASM_SUFFIX                       for rust projects, optionally specify the suffix of the wasm bytecode
                                                  output file
  --target-dir TARGET_DIR                         for rust projects, forward the parameter to Cargo
  --wat                                           also generate a WAT file when building
  --mir                                           also emit MIR files when building
  --llvm-ir                                       also emit LL (LLVM) files when building
  --ignore IGNORE                                 ignore all directories with these names. [default: target]
  --no-imports                                    skips extracting the EI imports after building the contracts
  --no-abi-git-version                            skips loading the Git version into the ABI
  --twiggy-top                                    generate a twiggy top report after building
  --twiggy-paths                                  generate a twiggy paths report after building
  --twiggy-monos                                  generate a twiggy monos report after building
  --twiggy-dominators                             generate a twiggy dominators report after building

```

## Group **Transactions**

```
$ drtpy tx --help
usage: drtpy tx COMMAND [-h] ...

Create and broadcast Transactions

COMMANDS:
  {new,send,get,sign}

OPTIONS:
  -h, --help           show this help message and exit

----------------
COMMANDS summary
----------------
new                            Create a new transaction.
send                           Send a previously saved transaction.
get                            Get a transaction.
sign                           Sign a previously saved transaction.

```

### Transactions.New

```
$ drtpy tx new --help
usage: drtpy tx new [-h] ...

Create a new transaction.

Output example:
===============
{
    "emittedTransaction": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "emittedTransactionData": "the transaction data, not encoded",
    "emittedTransactionHash": "the transaction hash"
}

options:
  -h, --help                                      show this help message and exit
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --receiver RECEIVER                             🖄 the address of the receiver
  --receiver-username RECEIVER_USERNAME           🖄 the username of the receiver
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --value VALUE                                   the value to transfer (default: 0)
  --data DATA                                     the payload, or 'memo' of the transaction (default: )
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --data-file DATA_FILE                           a file containing transaction data
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --relay                                         whether to relay the transaction (default: False)
  --proxy PROXY                                   🔗 the URL of the proxy
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --wait-result                                   signal to wait for the transaction result - only valid if --send is
                                                  set
  --timeout TIMEOUT                               max num of seconds to wait for result - only valid if --wait-result is
                                                  set

```

### Transactions.Send

```
$ drtpy tx send --help
usage: drtpy tx send [-h] ...

Send a previously saved transaction.

Output example:
===============
{
    "emittedTransaction": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    },
    "emittedTransactionData": "the transaction data, not encoded",
    "emittedTransactionHash": "the transaction hash"
}

options:
  -h, --help         show this help message and exit
  --infile INFILE    input file (a previously saved transaction)
  --outfile OUTFILE  where to save the output (the hash) (default: stdout)
  --proxy PROXY      🔗 the URL of the proxy

```

### Transactions.Get

```
$ drtpy tx get --help
usage: drtpy tx get [-h] ...

Get a transaction.

Output example:
===============
{
    "transactionOnNetwork": {
        "nonce": 42,
        "sender": "alice",
        "receiver": "bob",
        "...": "..."
    }
}

options:
  -h, --help                 show this help message and exit
  --hash HASH                the hash
  --sender SENDER            the sender address
  --with-results             will also return the results of transaction
  --proxy PROXY              🔗 the URL of the proxy
  --omit-fields OMIT_FIELDS  omit fields in the output payload (default: [])

```

## Group **Validator**

```
$ drtpy validator --help
usage: drtpy validator COMMAND [-h] ...

Stake, UnStake, UnBond, Unjail and other actions useful for Validators

COMMANDS:
  {stake,unstake,unjail,unbond,change-reward-address,claim,unstake-nodes,unstake-tokens,unbond-nodes,unbond-tokens,clean-registered-data,restake-unstaked-nodes}

OPTIONS:
  -h, --help            show this help message and exit

----------------
COMMANDS summary
----------------
stake                          Stake value into the Network
unstake                        Unstake value
unjail                         Unjail a Validator Node
unbond                         Unbond tokens for a bls key
change-reward-address          Change the reward address
claim                          Claim rewards
unstake-nodes                  Unstake-nodes will unstake nodes for provided bls keys
unstake-tokens                 This command will un-stake the given amount (if value is greater than the existing topUp value, it will unStake one or several nodes)
unbond-nodes                   It will unBond nodes
unbond-tokens                  It will unBond tokens, if provided value is bigger that topUp value will unBond nodes
clean-registered-data          Deletes duplicated keys from registered data
restake-unstaked-nodes         It will reStake UnStaked nodes

```

### Validator.Stake

```
$ drtpy validator stake --help
usage: drtpy validator stake [-h] ...

Stake value into the Network

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --reward-address REWARD_ADDRESS                 the reward address
  --validators-file VALIDATORS_FILE               a JSON file describing the Nodes
  --top-up                                        Stake value for top up

```

### Validator.Unstake

```
$ drtpy validator unstake --help
usage: drtpy validator unstake [-h] ...

Unstake value

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --nodes-public-keys NODES_PUBLIC_KEYS           the public keys of the nodes as CSV (addrA,addrB)

```

### Validator.Unjail

```
$ drtpy validator unjail --help
usage: drtpy validator unjail [-h] ...

Unjail a Validator Node

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --nodes-public-keys NODES_PUBLIC_KEYS           the public keys of the nodes as CSV (addrA,addrB)

```

### Validator.Unbond

```
$ drtpy validator unbond --help
usage: drtpy validator unbond [-h] ...

Unbond tokens for a bls key

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --nodes-public-keys NODES_PUBLIC_KEYS           the public keys of the nodes as CSV (addrA,addrB)

```

### Validator.ChangeRewardAddress

```
$ drtpy validator change-reward-address --help
usage: drtpy validator change-reward-address [-h] ...

Change the reward address

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --reward-address REWARD_ADDRESS                 the new reward address

```

### Validator.Claim

```
$ drtpy validator claim --help
usage: drtpy validator claim [-h] ...

Claim rewards

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

## Group **StakingProvider**

```
$ drtpy staking-provider --help
usage: drtpy staking-provider COMMAND [-h] ...

Staking provider omnitool

COMMANDS:
  {create-new-delegation-contract,get-contract-address,add-nodes,remove-nodes,stake-nodes,unbond-nodes,unstake-nodes,unjail-nodes,change-service-fee,modify-delegation-cap,automatic-activation,redelegate-cap,set-metadata}

OPTIONS:
  -h, --help            show this help message and exit

```

### StakingProvider.CreateNewDelegationContract

```
$ drtpy staking-provider create-new-delegation-contract --help
usage: drtpy staking-provider create-new-delegation-contract [-h] ...

Create a new delegation system smart contract, transferred value must begreater than baseIssuingCost + min deposit value

options:
  -h, --help                                      show this help message and exit
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger
  --total-delegation-cap TOTAL_DELEGATION_CAP     the total delegation contract capacity
  --service-fee SERVICE_FEE                       the delegation contract service fee

```

### StakingProvider.GetContractAddress

```
$ drtpy staking-provider get-contract-address --help
usage: drtpy staking-provider get-contract-address [-h] ...

Get create contract address by transaction hash

options:
  -h, --help                       show this help message and exit
  --create-tx-hash CREATE_TX_HASH  the hash
  --sender SENDER                  the sender address
  --proxy PROXY                    🔗 the URL of the proxy

```

### StakingProvider.AddNodes

```
$ drtpy staking-provider add-nodes --help
usage: drtpy staking-provider add-nodes [-h] ...

Add new nodes must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --validators-file VALIDATORS_FILE               a JSON file describing the Nodes
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --using-delegation-manager                      whether delegation contract was created using the Delegation Manager
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.RemoveNodes

```
$ drtpy staking-provider remove-nodes --help
usage: drtpy staking-provider remove-nodes [-h] ...

Remove nodes must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --bls-keys BLS_KEYS                             a list with the bls keys of the nodes
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.StakeNodes

```
$ drtpy staking-provider stake-nodes --help
usage: drtpy staking-provider stake-nodes [-h] ...

Stake nodes must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --bls-keys BLS_KEYS                             a list with the bls keys of the nodes
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.UnbondNodes

```
$ drtpy staking-provider unbond-nodes --help
usage: drtpy staking-provider unbond-nodes [-h] ...

Unbond nodes must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --bls-keys BLS_KEYS                             a list with the bls keys of the nodes
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.UnstakeNodes

```
$ drtpy staking-provider unstake-nodes --help
usage: drtpy staking-provider unstake-nodes [-h] ...

Unstake nodes must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --bls-keys BLS_KEYS                             a list with the bls keys of the nodes
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.UnjailNodes

```
$ drtpy staking-provider unjail-nodes --help
usage: drtpy staking-provider unjail-nodes [-h] ...

Unjail nodes must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --bls-keys BLS_KEYS                             a list with the bls keys of the nodes
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.ChangeServiceFee

```
$ drtpy staking-provider change-service-fee --help
usage: drtpy staking-provider change-service-fee [-h] ...

Change service fee must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --service-fee SERVICE_FEE                       new service fee value
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.ModifyDelegationCap

```
$ drtpy staking-provider modify-delegation-cap --help
usage: drtpy staking-provider modify-delegation-cap [-h] ...

Modify delegation cap must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --delegation-cap DELEGATION_CAP                 new delegation contract capacity
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.AutomaticActivation

```
$ drtpy staking-provider automatic-activation --help
usage: drtpy staking-provider automatic-activation [-h] ...

Automatic activation must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --set                                           set automatic activation True
  --unset                                         set automatic activation False
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.RedelegateCap

```
$ drtpy staking-provider redelegate-cap --help
usage: drtpy staking-provider redelegate-cap [-h] ...

Redelegate cap must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --set                                           set redelegate cap True
  --unset                                         set redelegate cap False
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

### StakingProvider.SetMetadata

```
$ drtpy staking-provider set-metadata --help
usage: drtpy staking-provider set-metadata [-h] ...

Set metadata must be called by the contract owner

options:
  -h, --help                                      show this help message and exit
  --name NAME                                     name field in staking provider metadata
  --website WEBSITE                               website field in staking provider metadata
  --identifier IDENTIFIER                         identifier field in staking provider metadata
  --delegation-contract DELEGATION_CONTRACT       address of the delegation contract
  --proxy PROXY                                   🔗 the URL of the proxy
  --pem PEM                                       🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                           🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                               🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                             🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                        🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX     🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX     🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME               🖄 the username of the sender
  --nonce NONCE                                   # the nonce for the transaction
  --recall-nonce                                  ⭮ whether to recall the nonce when creating the transaction (default:
                                                  False)
  --gas-price GAS_PRICE                           ⛽ the gas price (default: 1000000000)
  --gas-limit GAS_LIMIT                           ⛽ the gas limit
  --estimate-gas                                  ⛽ whether to estimate the gas limit (default: 0)
  --value VALUE                                   the value to transfer (default: 0)
  --chain CHAIN                                   the chain identifier
  --version VERSION                               the transaction version (default: 2)
  --guardian GUARDIAN                             the address of the guradian
  --guardian-service-url GUARDIAN_SERVICE_URL     the url of the guardian service
  --guardian-2fa-code GUARDIAN_2FA_CODE           the 2fa code for the guardian
  --options OPTIONS                               the transaction options (default: 0)
  --send                                          ✓ whether to broadcast the transaction (default: False)
  --simulate                                      whether to simulate the transaction (default: False)
  --outfile OUTFILE                               where to save the output (signed transaction, hash) (default: stdout)
  --guardian-pem GUARDIAN_PEM                     🔑 the PEM file, if keyfile not provided
  --guardian-pem-index GUARDIAN_PEM_INDEX         🔑 the index in the PEM file (default: 0)
  --guardian-keyfile GUARDIAN_KEYFILE             🔑 a JSON keyfile, if PEM not provided
  --guardian-passfile GUARDIAN_PASSFILE           🔑 a file containing keyfile's password, if keyfile provided
  --guardian-ledger                               🔐 bool flag for signing transaction using ledger
  --guardian-ledger-account-index GUARDIAN_LEDGER_ACCOUNT_INDEX
                                                  🔐 the index of the account when using Ledger
  --guardian-ledger-address-index GUARDIAN_LEDGER_ADDRESS_INDEX
                                                  🔐 the index of the address when using Ledger

```

## Group **Account**

```
$ drtpy account --help
usage: drtpy account COMMAND [-h] ...

Get Account data (nonce, balance) from the Network

COMMANDS:
  {get}

OPTIONS:
  -h, --help  show this help message and exit

----------------
COMMANDS summary
----------------
get                            Query account details (nonce, balance etc.)

```

### Account.Get

```
$ drtpy account get --help
usage: drtpy account get [-h] ...

Query account details (nonce, balance etc.)

options:
  -h, --help                 show this help message and exit
  --proxy PROXY              🔗 the URL of the proxy
  --address ADDRESS          🖄 the address to query
  --balance                  whether to only fetch the balance
  --nonce                    whether to only fetch the nonce
  --username                 whether to only fetch the username
  --omit-fields OMIT_FIELDS  omit fields in the output payload (default: [])

```

## Group **Wallet**

```
$ drtpy wallet --help
usage: drtpy wallet COMMAND [-h] ...

Create wallet, derive secret key from mnemonic, bech32 address helpers etc.

COMMANDS:
  {new,convert,bech32,sign-message,verify-message}

OPTIONS:
  -h, --help            show this help message and exit

----------------
COMMANDS summary
----------------
new                            Create a new wallet and print its mnemonic; optionally save as password-protected JSON (recommended) or PEM (not recommended)
convert                        Convert a wallet from one format to another
bech32                         Helper for encoding and decoding bech32 addresses
sign-message                   Sign a message
verify-message                 Verify a previously signed message

```

### Wallet.New

```
$ drtpy wallet new --help
usage: drtpy wallet new [-h] ...

Create a new wallet and print its mnemonic; optionally save as password-protected JSON (recommended) or PEM (not recommended)

options:
  -h, --help                                      show this help message and exit
  --format {raw-mnemonic,keystore-mnemonic,keystore-secret-key,pem}
                                                  the format of the generated wallet file (default: None)
  --outfile OUTFILE                               the output path and base file name for the generated wallet files
                                                  (default: None)
  --address-hrp ADDRESS_HRP                       the human-readable part of the address, when format is keystore-
                                                  secret-key or pem (default: moa)

```

### Wallet.Convert

```
$ drtpy wallet convert --help
usage: drtpy wallet convert [-h] ...

Convert a wallet from one format to another

options:
  -h, --help                                      show this help message and exit
  --infile INFILE                                 path to the input file
  --outfile OUTFILE                               path to the output file
  --in-format {raw-mnemonic,keystore-mnemonic,keystore-secret-key,pem}
                                                  the format of the input file
  --out-format {raw-mnemonic,keystore-mnemonic,keystore-secret-key,pem,address-bech32,address-hex}
                                                  the format of the output file
  --address-index ADDRESS_INDEX                   the address index, if input format is raw-mnemonic, keystore-mnemonic
                                                  or pem (with multiple entries) and the output format is keystore-
                                                  secret-key or pem
  --address-hrp ADDRESS_HRP                       the human-readable part of the address, when the output format is
                                                  keystore-secret-key or pem (default: moa)

```

### Wallet.Bech32

```
$ drtpy wallet bech32 --help
usage: drtpy wallet bech32 [-h] ...

Helper for encoding and decoding bech32 addresses

positional arguments:
  value       the value to encode or decode

options:
  -h, --help  show this help message and exit
  --encode    whether to encode
  --decode    whether to decode

```

### Wallet.SignMessage

```
$ drtpy wallet sign-message --help
usage: drtpy wallet sign-message [-h] ...

Sign a message

options:
  -h, --help                                   show this help message and exit
  --message MESSAGE                            the message you want to sign
  --pem PEM                                    🔑 the PEM file, if keyfile not provided
  --pem-index PEM_INDEX                        🔑 the index in the PEM file (default: 0)
  --keyfile KEYFILE                            🔑 a JSON keyfile, if PEM not provided
  --passfile PASSFILE                          🔑 a file containing keyfile's password, if keyfile provided
  --ledger                                     🔐 bool flag for signing transaction using ledger
  --ledger-account-index LEDGER_ACCOUNT_INDEX  🔐 the index of the account when using Ledger
  --ledger-address-index LEDGER_ADDRESS_INDEX  🔐 the index of the address when using Ledger
  --sender-username SENDER_USERNAME            🖄 the username of the sender

```

### Wallet.VerifyMessage

```
$ drtpy wallet verify-message --help
usage: drtpy wallet verify-message [-h] ...

Verify a previously signed message

options:
  -h, --help             show this help message and exit
  --address ADDRESS      the bech32 address of the signer
  --message MESSAGE      the previously signed message(readable text, as it was signed)
  --signature SIGNATURE  the signature in hex format

```

## Group **Localnet**

```
$ drtpy localnet --help
usage: drtpy localnet COMMAND [-h] ...

Set up, start and control localnets

COMMANDS:
  {setup,new,prerequisites,build,start,config,clean}

OPTIONS:
  -h, --help            show this help message and exit

```

### Localnet.Setup

```
$ drtpy localnet setup --help
usage: drtpy localnet setup [-h] ...

Set up a localnet (runs 'prerequisites', 'build' and 'config' in one go)

options:
  -h, --help               show this help message and exit
  --configfile CONFIGFILE  An optional configuration file describing the localnet

```

### Localnet.New

```
$ drtpy localnet new --help
usage: drtpy localnet new [-h] ...

Create a new localnet configuration

options:
  -h, --help               show this help message and exit
  --configfile CONFIGFILE  An optional configuration file describing the localnet

```

### Localnet.Prerequisites

```
$ drtpy localnet prerequisites --help
usage: drtpy localnet prerequisites [-h] ...

Download and verify the prerequisites for running a localnet

options:
  -h, --help               show this help message and exit
  --configfile CONFIGFILE  An optional configuration file describing the localnet

```

### Localnet.Build

```
$ drtpy localnet build --help
usage: drtpy localnet build [-h] ...

Build necessary software for running a localnet

options:
  -h, --help                                      show this help message and exit
  --configfile CONFIGFILE                         An optional configuration file describing the localnet
  --software {node,seednode,proxy} [{node,seednode,proxy} ...]
                                                  The software to build (default: ['node', 'seednode', 'proxy'])

```

### Localnet.Config

```
$ drtpy localnet config --help
usage: drtpy localnet config [-h] ...

Configure a localnet (required before starting it the first time or after clean)

options:
  -h, --help               show this help message and exit
  --configfile CONFIGFILE  An optional configuration file describing the localnet

```

### Localnet.Start

```
$ drtpy localnet start --help
usage: drtpy localnet start [-h] ...

Start a localnet

options:
  -h, --help                               show this help message and exit
  --configfile CONFIGFILE                  An optional configuration file describing the localnet
  --stop-after-seconds STOP_AFTER_SECONDS  Stop the localnet after a given number of seconds (default: 31536000)

```

### Localnet.Clean

```
$ drtpy localnet clean --help
usage: drtpy localnet clean [-h] ...

Erase the currently configured localnet (must be already stopped)

options:
  -h, --help               show this help message and exit
  --configfile CONFIGFILE  An optional configuration file describing the localnet

```

## Group **Dependencies**

```
$ drtpy deps --help
usage: drtpy deps COMMAND [-h] ...

Manage dependencies or drt-sdk modules

COMMANDS:
  {install,check}

OPTIONS:
  -h, --help       show this help message and exit

----------------
COMMANDS summary
----------------
install                        Install dependencies or drt-sdk modules.
check                          Check whether a dependency is installed.

```

### Dependencies.Install

```
$ drtpy deps install --help
usage: drtpy deps install [-h] ...

Install dependencies or drt-sdk modules.

positional arguments:
  {all,rust,golang,vmtools,testwallets}  the dependency to install

options:
  -h, --help                             show this help message and exit
  --overwrite                            whether to overwrite an existing installation

```

### Dependencies.Check

```
$ drtpy deps check --help
usage: drtpy deps check [-h] ...

Check whether a dependency is installed.

positional arguments:
  {all,rust,golang,vmtools,testwallets}  the dependency to check

options:
  -h, --help                             show this help message and exit

```

## Group **Configuration**

```
$ drtpy config --help
usage: drtpy config COMMAND [-h] ...

Configure drt-sdk (default values etc.)

COMMANDS:
  {dump,get,set,delete,new,switch,list,reset}

OPTIONS:
  -h, --help            show this help message and exit

----------------
COMMANDS summary
----------------
dump                           Dumps configuration.
get                            Gets a configuration value.
set                            Sets a configuration value.
delete                         Deletes a configuration value.
new                            Creates a new configuration.
switch                         Switch to a different config
list                           List available configs
reset                          Deletes the config file. Default config will be used.

```

### Configuration.Dump

```
$ drtpy config dump --help
usage: drtpy config dump [-h] ...

Dumps configuration.

options:
  -h, --help  show this help message and exit
  --defaults  dump defaults instead of local config

```

### Configuration.Get

```
$ drtpy config get --help
usage: drtpy config get [-h] ...

Gets a configuration value.

positional arguments:
  name        the name of the configuration entry

options:
  -h, --help  show this help message and exit

```

### Configuration.Set

```
$ drtpy config set --help
usage: drtpy config set [-h] ...

Sets a configuration value.

positional arguments:
  name        the name of the configuration entry
  value       the new value

options:
  -h, --help  show this help message and exit

```

### Configuration.New

```
$ drtpy config new --help
usage: drtpy config new [-h] ...

Creates a new configuration.

positional arguments:
  name                 the name of the configuration entry

options:
  -h, --help           show this help message and exit
  --template TEMPLATE  template from which to create the new config

```

### Configuration.Switch

```
$ drtpy config switch --help
usage: drtpy config switch [-h] ...

Switch to a different config

positional arguments:
  name        the name of the configuration entry

options:
  -h, --help  show this help message and exit

```

### Configuration.List

```
$ drtpy config list --help
usage: drtpy config list [-h] ...

List available configs

options:
  -h, --help  show this help message and exit

```

### Configuration.Reset

```
$ drtpy config reset --help
usage: drtpy config reset [-h] ...

Deletes the config file. Default config will be used.

options:
  -h, --help  show this help message and exit

```

## Group **Data**

```
$ drtpy data --help
usage: drtpy data COMMAND [-h] ...

Data manipulation omnitool

COMMANDS:
  {parse,store,load}

OPTIONS:
  -h, --help          show this help message and exit

----------------
COMMANDS summary
----------------
parse                          Parses values from a given file
store                          Stores a key-value pair within a partition
load                           Loads a key-value pair from a storage partition

```

### Data.Dump

```
$ drtpy data parse --help
usage: drtpy data parse [-h] ...

Parses values from a given file

options:
  -h, --help               show this help message and exit
  --file FILE              path of the file to parse
  --expression EXPRESSION  the Python-Dictionary expression to evaluate in order to extract the data

```

### Data.Store

```
$ drtpy data store --help
usage: drtpy data store [-h] ...

Stores a key-value pair within a partition

options:
  -h, --help             show this help message and exit
  --key KEY              the key
  --value VALUE          the value to save
  --partition PARTITION  the storage partition (default: *)
  --use-global           use the global storage (default: False)

```

### Data.Load

```
$ drtpy data load --help
usage: drtpy data load [-h] ...

Loads a key-value pair from a storage partition

options:
  -h, --help             show this help message and exit
  --key KEY              the key
  --partition PARTITION  the storage partition (default: *)
  --use-global           use the global storage (default: False)

```
