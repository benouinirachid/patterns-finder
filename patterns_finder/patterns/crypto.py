from . import Pattern
# crypto

__name = "([^a-zA-Z0-9])(Bitcoin|Ethereum|Tether|Cardano|XRP|Solana|Polkadot|Dogecoin|Dai|Litecoin|Algorand|Bitcoin|ECOMI|Internet|Ethereum|Monero|Tezos|Iota|EOS|Bitcoin|Maker|Zcash|Dash|Nano|Augur|Steem)([^a-zA-Z0-9])"
__name_label = "CRYPTO-NAME"
name = Pattern(__name, __name_label)

__symbol = "([^a-zA-Z0-9])(BTC|ETH|USDT|ADA|XRP|SOL|DOT|DOGE|DAI|LTC|ALGO|BCH|OMI|ICP|ETC|XMR|XTZ|MIOTA|EOS|BSV|MKR|ZEC|DASH|XNO|REP|STEEM)([^a-zA-Z0-9])"
__symbol_label = "CRYPTO-SYMBOL"
symbol = Pattern(__symbol, __symbol_label)

__unicode = "([^a-zA-Z0-9])(₿|Ξ|₮|₳|✕|◎|●|Ð|◈|Ł|Ⱥ|Ƀ|Ο|∞|ξ|ɱ|ꜩ|ɨ|ε|Ɓ|Μ|ⓩ|Đ|Ӿ|Ɍ|ȿ)([^a-zA-Z0-9])"
__unicode_label = "CRYPTO-UNICODE"
unicode = Pattern(__unicode, __unicode_label)
