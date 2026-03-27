import smtplib
from email.mime.text import MIMEText
import os
from datetime import datetime

def send_otp_email(recipient, otp_code):
    """Send OTP using simple SMTP"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp-relay.brevo.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        subject = "🔐 Password Reset OTP - Smart Pantry"
        body = f"""
Hello,

Your OTP for password reset is: {otp_code}

This OTP expires in 10 minutes.

If you didn't request this, please ignore this email.

- Smart Pantry System
"""
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        
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
    """Send expiry notification - simplified"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp-relay.brevo.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        subject = "⚠️ Item Expiring Soon!" if status == 'expiring' else "❌ Item Expired!"
        body = f"""
Item: {item.get('name', 'Unknown')}
Quantity: {item.get('quantity', 0)}
Expiry Date: {item.get('expiry_date', 'Unknown')}
Location: {item.get('profile_id', 'Unknown')}
Status: {'Expiring Soon' if status == 'expiring' else 'Expired'}

Please check your pantry and take necessary action.

- Smart Pantry System
"""
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        
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
    """Send low stock notification - simplified"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp-relay.brevo.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        subject = "📦 Low Stock Alert - Smart Pantry"
        body = f"""
Item: {item.get('name', 'Unknown')}
Quantity: {item.get('quantity', 0)}
Location: {item.get('profile_id', 'Unknown')}

This item is running low. Consider adding it to your shopping list!

- Smart Pantry System
"""
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        
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
    """Send shopping list - simplified"""
    try:
        smtp_server = os.getenv('MAIL_SERVER', 'smtp-relay.brevo.com')
        port = int(os.getenv('MAIL_PORT', 587))
        username = os.getenv('MAIL_USERNAME')
        password = os.getenv('MAIL_PASSWORD')
        sender = os.getenv('MAIL_DEFAULT_SENDER', username)
        
        # Build items list
        items_text = ""
        for idx, item in enumerate(items, 1):
            reason_icon = {
                'Expired': '🔴',
                'Low Stock': '🟡',
                'Out of Stock': '⚫'
            }.get(item.get('status', ''), '📦')
            items_text += f"{idx}. {reason_icon} {item.get('item_name', 'Unknown')} - Qty: {item.get('quantity', 0)}"
            if item.get('expiry_date'):
                items_text += f" - Expires: {item.get('expiry_date')}"
            if item.get('status'):
                items_text += f" - Status: {item.get('status')}"
            items_text += "\n"
        
        subject = "🛒 Your Shopping List - Smart Pantry"
        body = f"""
Shopping List for {profile_name}
Date: {datetime.now().strftime('%B %d, %Y')}
Total Items: {len(items)}
{'=' * 40}

{items_text}
{'=' * 40}

Shopping Tips:
• 🔴 Expired items - Replace immediately
• 🟡 Low stock - Restock soon
• ⚫ Out of stock - Add to cart
• Check expiry dates before purchasing

- Smart Pantry System
"""
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient
        
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
