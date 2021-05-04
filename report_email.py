#!/usr/bin/env python3
import os
import datetime
import reports
import emails

dt = datetime.date.today().strftime("%B  %d, %Y")
date = "Processed Update on " + dt
names = []
weights = []
path = "./supplier-data/descriptions/"
for file in os.listdir(path):
    with open(path + file) as f:
        for line in f:
            if "lbs" in line:
                weights.append("weight: " + line)
            elif len(line.split())==1: #checks if its a description or just a fruitname
                names.append("name: " + line)
            else:
                continue

summary = ""
for name, weight in zip(names, weights):
    summary += '<br />' + name + '<br />' + weight + '<br />' 

if __name__ == "__main__":
    reports.generate_report("/tmp/processed.pdf", date, summary)
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)
