# Findme - 500 Points

## Challenge

Find me! Challenge created by Security Risk Advisors for RITSEC CTF

Attached File:  findme.pcap

## Solution

We load the pcap in wireshark, follow the tcp stream on packet 40 and get the following base64:

```
H4sIAFSZx10AA+3OMQuCQBiH8Zv9FPcFgrvUcw2kIWgydzG1EkQPvZui757S0lSTRPD8lmd43+F/
6cqrWJmaGRMt1Ums3vtitkKHsdGJDqNtKJSeGwup1h628JMrRymFP/ve+Q9/X+5/Kjvkp316t1Vp
p0KNReuKuq17V9x21jb9IwjSPDtuKukGWXXD1AS/XgwAAAAAAAAAAAAAAAAAWDwB38XEewAoAAA=
```

This decodes to a compressed file, which reveals the flag after unzipping it.

RITSEC{pcaps_0r_it_didnt_h@ppen}