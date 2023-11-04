import smtplib
from email.message import EmailMessage
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext


# Function to send the email
def send_email(receiver_email, subject, body, sender_email, password):
    smtp_server = 'smtp.gmail.com'  # Gmail's SMTP server
    port = 587  # Port number for TLS

    # Create the email message
    email = EmailMessage()
    email['From'] = sender_email
    email['To'] = receiver_email
    email['Subject'] = subject
    email.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, password)
            server.send_message(email)
            messagebox.showinfo("Success", "Email sent successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Function to create the email GUI after successful login
def create_email_gui(sender_email, password):
    def send_action():
        # Collecting the email data and sending the email
        receiver_email = receiver_email_entry.get()
        subject = subject_entry.get()
        body = body_text.get("1.0", tk.END)
        send_email(receiver_email, subject, body, sender_email, password)

    # Email GUI setup
    email_root = tk.Toplevel()
    email_root.title("Email Sender App")

    tk.Label(email_root, text="To Email:").grid(row=0, column=0)
    receiver_email_entry = tk.Entry(email_root)
    receiver_email_entry.grid(row=0, column=1)

    tk.Label(email_root, text="Subject:").grid(row=1, column=0)
    subject_entry = tk.Entry(email_root)
    subject_entry.grid(row=1, column=1)

    tk.Label(email_root, text="Email Body:").grid(row=2, column=0)
    body_text = scrolledtext.ScrolledText(email_root, height=10, width=50)
    body_text.grid(row=2, column=1)

    send_button = tk.Button(email_root, text="Send Email", command=send_action)
    send_button.grid(row=3, column=0, columnspan=2)


# Login function to prompt for username and password
def login():
    sender_email = simpledialog.askstring("Login", "Enter your email:")
    password = simpledialog.askstring("Login", "Enter your password:", show="*")

    if sender_email and password:
        create_email_gui(sender_email, password)
    else:
        messagebox.showerror("Error", "Email and password are required to login.")


# Main application window (initially just a login button)
root = tk.Tk()
root.title("Email Login")

login_button = tk.Button(root, text="Login to Email", command=login)
login_button.pack(pady=20)

root.mainloop()
