from mac import parser


def get_name_of_mac(mac: str) -> str:
    return parser.open_cached_file()[mac]
