# Price Checker and Email Notifier

## **Description**
A Python-based tool that tracks product prices from e-commerce website AMAZON, and sends an email notification when the price falls below a user-defined threshold. This project demonstrates web scraping, email automation, and condition-based notifications.

## **Features**
- **Price Monitoring:** Automatically check product prices from a given URL.
- **Email Alerts:** Notify users via email when the price meets their target.
- **Robust Web Scraping:** Handles missing product information gracefully.
- **Custom Target Price:** Set a specific price threshold for notifications.

## **Technologies Used**
- Python
- BeautifulSoup (for web scraping)
- smtplib (for email notifications)

## **Usage Instructions**
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Install dependencies (if required):
   ```bash
   pip install requests beautifulsoup4
   ```

3. Run the script:
   ```bash
   python price_checker.py
   ```

4. Enter the product URL and your target price when prompted.

5. If the product price is below or equal to your target, an email alert will be sent.

## **Security Note**
The current implementation uses hardcoded email credentials. To make it secure:
- Use environment variables or a configuration file to store email credentials securely.
- Avoid sharing your personal credentials in public repositories.

## **Example Output**
```
Enter the URL of the product: <Product URL>
Enter your target price (in rupees): 1500
Email has been sent!
```