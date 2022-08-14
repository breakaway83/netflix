class Config:
    LOG_URL: str = "https://appsec-exercise.test.netflix.net/log/client_access"
    AFFECTED_URL: str = "http://appsec-exercise.test.netflix.net"
    HMAC_KEY: str = "supersecretpassphrase"
    PARTNER_KEY: str = "foobar"
    BATCH_FILE: str = "1-11-2015.txt"
    REQUEST_TIMEOUT: int = 5
    OPEN_CONNECTIONS: int = 100
