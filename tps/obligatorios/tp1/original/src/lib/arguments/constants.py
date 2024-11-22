from ..verbose import Verbose

DOWNLOAD_CLIENT: str = "download.py"
UPLOAD_CLIENT: str = "upload.py"
SERVER: str = "start-server.py"

DEFAULT_VERBOSE: bool = Verbose.DEFAULT
DEFAULT_ALGORITHM: str = "sw"
DEFAULT_TIMEOUT: int = 1000

DEFAULT_SERVER_HOST: str = "127.0.0.1"
DEFAULT_SERVER_PORT: int = 8080
DEFAULT_SERVER_STORAGE_DIR_PATH: str = "~/server-storage"

DEFAULT_DOWNLOAD_DESTINATION_PATH: str = "~/Downloads"

HEADER_SIZE_SW = 8
MAX_PAYLOAD_SIZE = (2**10) * 5

MAX_PACKET_SIZE_SW = HEADER_SIZE_SW + MAX_PAYLOAD_SIZE

FIXED_HEADER_SIZE_SACK = 16
MAX_VARIABLE_HEADER_SIZE_SACK = 4 * 2**16
MAX_PAYLOAD_SIZE_SACK = (2**10) * 5

MAX_PACKET_SIZE_SACK = (
    FIXED_HEADER_SIZE_SACK + MAX_VARIABLE_HEADER_SIZE_SACK + MAX_PAYLOAD_SIZE_SACK
)

MAX_TIMEOUT_COUNT: int = 60