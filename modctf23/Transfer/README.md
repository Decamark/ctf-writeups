nmap -sV --version-all --version-trace 10.10.10.21

NSOCK INFO [11.9180s] nsock_trace_handler_callback(): Callback: WRITE SUCCESS for EID 27 [10.10.10.21:53]
NSOCK INFO [12.2230s] nsock_trace_handler_callback(): Callback: READ SUCCESS for EID 34 [10.10.10.21:53] (63 bytes): .=.............version.bind..................flag{yExjq2D72ASL}
Service scan match (Probe DNSVersionBindReqTCP matched with DNSVersionBindReq line 12424): 10.10.10.21:53 is domain.  Version: |||unknown banner: flag{yExjq2D72ASL}|
