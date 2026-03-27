import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

def send_otp_email(recipient, otp_code):
    """Send OTP using Gmail SMTP"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = "🔐 Password Reset OTP - Smart Pantry"
        
        html = f"""
        <div style="font-family: Arial, sans-serif;">
            <h2>🔐 Password Reset Request</h2>
            <p>Your OTP for password reset is: <strong>{otp_code}</strong></p>
            <p>This OTP expires in 10 minutes.</p>
            <p>If you didn't request this, please ignore this email.</p>
        </div>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ OTP email sent to {recipient}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send OTP: {e}")
        return False

def send_expiry_alert(recipient, item, status):
    """Send expiry notification email"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = "⚠️ Item Expiring Soon!" if status == 'expiring' else "❌ Item Expired!"
        
        html = f"""
        <div>
            <h2>Pantry Alert</h2>
            <p>Item: {item.get('name', 'Unknown')}</p>
            <p>Quantity: {item.get('quantity', 0)}</p>
            <p>Expiry Date: {item.get('expiry_date', 'Unknown')}</p>
            <p>Location: {item.get('profile_id', 'Unknown')}</p>
        </div>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Expiry alert sent to {recipient}")
        return True
        
    except Exception as e:
        print(f"❌ Failed to send expiry alert: {e}")
        return False

def send_low_stock_alert(recipient, item):
    """Send low stock notification email"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = "📦 Low Stock Alert - Smart Pantry"
        
        html = f"""
        <div>
            <h2>Low Stock Alert</h2>
            <p>Item: {item.get('name', 'Unknown')}</p>
            <p>Quantity: {item.get('quantity', 0)}</p>
            <p>Location: {item.get('profile_id', 'Unknown')}</p>
        </div>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Low stock alert sent to {recipient}")
        return True
        
    except Exception as e:
        print(f"❌ Low stock alert error: {e}")
        return False

def send_shopping_list_email(recipient, items, profile_name):
    """Send shopping list as email"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        items_html = ""
        for idx, item in enumerate(items, 1):
            items_html += f"""
            <tr>
                <td>{idx}</td>
                <td>{item.get('item_name', 'Unknown')}</td>
                <td>{item.get('quantity', 0)}</td>
                <td>{item.get('expiry_date', 'N/A')}</td>
                <td>{item.get('status', 'Unknown')}</td>
            </tr>
            """
        
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = recipient
        msg['Subject'] = "🛒 Your Shopping List - Smart Pantry"
        
        html = f"""
        <div>
            <h2>Shopping List - {profile_name}</h2>
            <table border="1">
                <tr><th>#</th><th>Item</th><th>Qty</th><th>Expiry</th><th>Status</th></tr>
                {items_html}
            </table>
            <p>Keep your pantry organized!</p>
        </div>
        """
        
        msg.attach(MIMEText(html, 'html'))
        
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(username, password)
        server.send_message(msg)
        server.quit()
        
        print(f"✅ Shopping list sent to {recipient}")
        return True
        
    except Exception as e:
        print(f"❌ Shopping list error: {e}")
        return False
