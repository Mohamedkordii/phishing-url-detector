# Phishing URL Detector

A Python-based cybersecurity tool that analyzes URLs for common phishing indicators and assigns a basic risk score.

This project was created to practice URL analysis, phishing detection concepts, and basic heuristic-based threat assessment.

## Features

- Analyzes URLs for common phishing indicators
- Checks whether HTTPS is being used
- Detects IP-address-based URLs
- Detects unusually long URLs
- Detects the `@` symbol in URLs
- Checks for excessive subdomains
- Searches for suspicious keywords such as:
  - login
  - verify
  - secure
  - account
  - password
  - bank
  - payment
- Assigns a basic risk score
- Classifies URLs as LOW, MEDIUM, or HIGH risk

## How It Works

The program asks the user to enter a URL.

It then performs several heuristic checks.

Each suspicious indicator increases the risk score.

Examples:

- No HTTPS: +1
- IP address used instead of a domain: +2
- Very long URL: +1
- `@` symbol detected: +2
- Many subdomains: +1
- Suspicious keywords detected: +1

The final score is classified as:

- LOW risk: score below 3
- MEDIUM risk: score from 3 to 4
- HIGH risk: score 5 or higher

## Project Files

- `phishing_detector.py` - Main Python phishing URL analysis tool
- `.gitignore` - Specifies files Git should ignore
- `README.md` - Project documentation

## Requirements

- Python 3

This project only uses Python standard libraries, so no additional packages are required.

## How to Run

Run the program from a terminal:

```bash
python3 phishing_detector.py
```

Then enter a URL when prompted.

Example:

```text
Phishing URL Detector
----------------------------------------
Enter a URL to analyze: http://192.168.1.10/login/verify-account

Analysis Result
----------------------------------------
Risk Level: MEDIUM
Risk Score: 4

Indicators Found:
- URL does not use HTTPS
- URL uses an IP address instead of a domain name
- Suspicious keywords found: login, verify, account
```

## Important Note

This tool uses simple heuristic checks.

A LOW risk score does not guarantee that a website is safe, and a HIGH risk score does not automatically mean that a website is malicious.

Real-world phishing detection may involve additional techniques such as:

- Domain reputation
- DNS analysis
- Certificate analysis
- Threat intelligence
- Machine learning
- Website content analysis

## Security & Ethical Use

This project is intended for educational and defensive cybersecurity purposes.

Do not use the tool to interact with or test systems without authorization.

## Skills Demonstrated

- Python
- Cybersecurity fundamentals
- Phishing awareness
- URL parsing
- Heuristic analysis
- Risk scoring
- Input validation
- IP address detection
- Basic threat detection

## Author

**Mohamed Kordi**  
Cybersecurity Engineering Student  
University of Sharjah
