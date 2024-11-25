import win32com.client


def get_inbox_emails(namespace):
    # Access the inbox folder
    inbox = namespace.GetDefaultFolder(6)  # 6 = Inbox folder
    messages = inbox.Items
    print(f"Total messages in folder:{len(messages)}")

    # Print subject of the first 5 emails
    for i in range(min(5, len(messages))):
        message = messages[i]
        print(f"Subject: {message.Subject}\n")
        print(f"Sender: {message.SenderName}\n")
        print(f"Received: {message.ReceivedTime}\n")


# Example usage
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
get_inbox_emails(namespace)
