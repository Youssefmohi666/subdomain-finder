# Zero Byte Subdomain Discovery Tool

![Zero Byte Banner](https://img.shields.io/badge/Zero%20Byte-Subdomain%20Finder-cyan?style=for-the-badge&logo=python)

A professional, high-performance subdomain discovery tool developed by **Yusef Mohey** as part of the Zero Byte Cybersecurity project. This tool uses DNS resolution to identify live subdomains for a target domain, providing a clean and intuitive CLI interface with real-time feedback.

---

## 🚀 Features

- **DNS Resolution**: Rapidly checks subdomains using specialized DNS queries.
- **Rich CLI**: Uses the `rich` library for a beautiful, color-coded terminal experience.
- **Internal Wordlist**: Comes with a built-in list of common subdomains as a fallback.
- **Custom Wordlists**: Supports external wordlist files for more exhaustive searches.
- **Liveness Verification**: Automatically checks if the target domain is live before scanning.
- **Force Mode**: Option to bypass initial liveness checks for deeper investigation.

---

## 🛠 Prerequisites

Ensure you have Python 3.x installed. The tool depends on the following libraries:

```bash
pip install dnspython requests rich
```

---

## 📦 Installation

1. Clone the repository or navigate to the tool directory:
   ```bash
   cd tools/subdomain-finder
   ```
2. Ensure you have a `wordlist.txt` in the same directory (optional, but recommended).

---

## 📖 Usage

### Basic Scan
Perform a scan using the default fallback list or `wordlist.txt`:
```bash
python main.py -d example.com
```

### Custom Wordlist
Use a specific wordlist for more comprehensive discovery:
```bash
python main.py -d example.com -w my_wordlist.txt
```

### Force Scan
If the base domain is not responding to DNS but you still want to check subdomains:
```bash
python main.py -d example.com -f
```

---

## ⚙️ Options

| Argument | Long Flag | Description |
| :--- | :--- | :--- |
| `-d` | `--domain` | **Target Domain** (e.g., example.com) |
| `-w` | `--wordlist`| Path to **Wordlist File** (Default: `wordlist.txt`) |
| `-f` | `--force` | **Force scan** even if base domain appears down |
| `-v` | `--version`| Show tool version |
| `-h` | `--help` | Show help message |

---

## 👤 Author

Developed by **Yusef Mohey**
*Build for the Zero Byte Cybersecurity Academy*

---

> [!TIP]
> For best results, use a high-quality wordlist like `subdomains-top1mil-5000.txt` from SecLists.
