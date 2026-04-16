import argparse
import dns.resolver
import requests
import sys
import threading
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TaskProgressColumn
from rich.live import Live
import subprocess
import os
console = Console()

SUB_DOMAINS_LIST=[
    "www","api","admin","app","cpanel","mail","ftp","ns1","ns2","ns3","ns4","ns5","ns6","ns7","ns8","ns9","ns10"
    "webadmin","info","test","dev","staging","prod","production","qa","uat","stage","staging","prod","production","qa","uat","stage"
]

def display_banner():
    banner = """
[subdomain-finder]
 ███████╗██╗   ██╗██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
 ██╔════╝██║   ██║██╔══██╗██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║
 ███████╗██║   ██║██████╗ ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗
 ╚════██║██║   ██║██╔══██╗██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║
 ███████║╚██████╔╝██████╔╝██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║
 ╚══════╝ ╚═════╝ ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝
[bold white]Zero Byte Subdomain Discovery Tool build by yusef mohey[/bold white]
    """
    console.print(Panel(banner, border_style="cyan"))

#  init params 
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--domain", help="Target domain (e.g., -d example.com)")
parser.add_argument("-w", "--wordlist", help="Wordlist file (e.g., -w wordlist.txt), default: wordlist.txt")
# parser.add_argument("-o", "--output", help="Output file (e.g., -o output.txt), default: output.txt")
parser.add_argument("-v","--version",action="version",version="zerobyte-subfinder 1.0.0")
parser.add_argument("-f","--force",action="store_true",help="Force to continue even if the domain is not live")
args = parser.parse_args()

def check_domain(domain):
    try:
        dns.resolver.resolve(domain, "A")
        return True
    except:
        return False


def get_subdomains(domain: str, wordlist_path: str) -> list:
    found_subdomains = []

    # load wordlist
    if os.path.exists(wordlist_path):
        with open(wordlist_path, "r") as f:
            subdomains = f.read().splitlines()
    else:
        console.print("[yellow][!] Wordlist not found, using default list[/yellow]")
        subdomains = SUB_DOMAINS_LIST

    for sub in subdomains:
        new_sub = f"{sub.strip()}.{domain.strip()}"

        try:
            dns.resolver.resolve(new_sub, "A")
            console.print(f"[green][+] {new_sub} is LIVE[/green]")
            found_subdomains.append(new_sub)

        except:
            console.print(f"[red][-] {new_sub} is NOT live[/red]")

    return found_subdomains


def search_for_subdomain():
    if not args.domain:
        console.print("[red][-] Domain is required[/red]")
        sys.exit(1)

    domain = args.domain
    wordlist = args.wordlist if args.wordlist else "wordlist.txt"

    if not args.force:
        if not check_domain(domain):
            console.print("[red][-] Domain is NOT live[/red]")
            console.print("[yellow][!] Use -f to force scan[/yellow]")
            sys.exit(1)

    console.print("[cyan][*] Starting subdomain scan...[/cyan]")
    results = get_subdomains(domain, wordlist)

    console.print(f"\n[bold green][✓] Found {len(results)} subdomains[/bold green]")


def main():
    print("HI , user ")
    print("\n")
    display_banner()
    search_for_subdomain()



if __name__ == "__main__":
    main()