from urllib.parse import urlparse
import ipaddress


SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "secure",
    "account",
    "update",
    "bank",
    "signin",
    "confirm",
    "password",
    "payment",
]


def has_ip_address(domain):
    try:
        ipaddress.ip_address(domain)
        return True
    except ValueError:
        return False


def analyze_url(url):
    score = 0
    reasons = []

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    parsed = urlparse(url)
    domain = parsed.netloc.lower()
    full_url = url.lower()

    if parsed.scheme != "https":
        score += 1
        reasons.append("URL does not use HTTPS")

    if has_ip_address(domain.split(":")[0]):
        score += 2
        reasons.append("URL uses an IP address instead of a domain name")

    if len(url) > 75:
        score += 1
        reasons.append("URL is unusually long")

    if "@" in url:
        score += 2
        reasons.append("URL contains the @ symbol")

    if domain.count(".") >= 3:
        score += 1
        reasons.append("Domain contains many subdomains")

    keyword_matches = []
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in full_url:
            keyword_matches.append(keyword)

    if keyword_matches:
        score += 1
        reasons.append(
            "Suspicious keywords found: " + ", ".join(keyword_matches)
        )

    if score >= 5:
        risk = "HIGH"
    elif score >= 3:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    return risk, score, reasons


def main():
    print("Phishing URL Detector")
    print("-" * 40)

    url = input("Enter a URL to analyze: ").strip()

    risk, score, reasons = analyze_url(url)

    print("\nAnalysis Result")
    print("-" * 40)
    print(f"Risk Level: {risk}")
    print(f"Risk Score: {score}")

    if reasons:
        print("\nIndicators Found:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("\nNo common phishing indicators were detected.")

    print(
        "\nNote: This tool uses basic heuristic checks and cannot guarantee "
        "whether a website is safe or malicious."
    )


if __name__ == "__main__":
    main()
