import xml.etree.ElementTree as ET
import sys

def parse_evtx(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as file:
        content = file.read()

    events = content.split("</Event>")
    for raw_event in events:
        if "<EventID>" in raw_event:
            try:
                event_id = raw_event.split("<EventID>")[1].split("</EventID>")[0]
                time_created = raw_event.split("<TimeCreated SystemTime=\"")[1].split("\"")[0]
                computer = raw_event.split("<Computer>")[1].split("</Computer>")[0]
                if event_id == "4625":
                    print(f"[FAILED LOGIN] {time_created} - {computer}")
                elif event_id == "4624":
                    print(f"[SUCCESSFUL LOGIN] {time_created} - {computer}")
                elif event_id == "4740":
                    print(f"[ACCOUNT LOCKOUT] {time_created} - {computer}")
            except Exception:
                continue

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <log_file.evtx.xml>")
        sys.exit(1)

    parse_evtx(sys.argv[1])
