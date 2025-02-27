import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle

def generate_invoice(cursor, invoice_number, date, customer, customerAddress, customerComapnyName, customerEmail, customerPhoneNum, customerGSTIN, items, gst_rate, discount, filename):
    address = "LS.NO 204, P1, THORDI, MAHUVA BHAVNAGAR HEY,\nThordi Branch Post Office, BHUDEL, Thordi, Bhavnagar,\nGujarat\nPhone no.: 9601556225\nEmail: pareshchopda2381@gmail.com\nGSTIN: 24ATJPC2927Q1ZE\nState: 24-Gujarat"
    companyName = "Radhe Enterprise"
    bank_details = "Bank Name: AXIS BANK, WAGHAVADI\nBank Account No.: 923020014346110\nBank IFSC code: UTIB0000200\nAccount Holder's Name: Paresh Chopda"

    customerDetails = f"{customer}\nPhone No.: {customerPhoneNum}\nEmail: {customerEmail}\nGSTIN: {customerGSTIN}\nAddress: {customerAddress}"

    # Ensure the invoice folder exists
    invoice_folder = "invoice"
    if not os.path.exists(invoice_folder):
        os.makedirs(invoice_folder)
    
    # Full path for the invoice file
    full_path = os.path.join(invoice_folder, filename)

    c = canvas.Canvas(full_path, pagesize=A4)
    width, height = A4
    
    # Use a built-in font that supports the rupee sign
    c.setFont("Helvetica", 16)
    
    # Invoice Header
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 40, companyName)
    c.setFont("Helvetica", 10)
    text = c.beginText(50, height - 60)
    for line in address.split('\n'):
        text.textLine(line)
    c.drawText(text)
    
    c.setFont("Helvetica-Bold", 14)
    c.drawString(250, height - 160, "Tax Invoice")
    
    # Bill To and Invoice Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 190, "Bill To")
    c.drawString(400, height - 190, "Invoice Details")
    c.drawString(50, height - 210, customerComapnyName)
    
    c.setFont("Helvetica", 10)
    text = c.beginText(50, height - 230)
    # text.textLine(customer)
    c.setFont("Helvetica-Bold", 10)
    for line in customerDetails.split('\n'):
        text.textLine(line)
        c.setFont("Helvetica", 10)
    c.drawText(text)
    
    text = c.beginText(400, height - 230)
    text.textLine(f"Invoice No.: {invoice_number}")
    text.textLine(f"Date: {date}")
    c.drawText(text)
    
    # Table Data
    table_data = [["#", "Item Name", "HSN/SAC", "Quantity", "Unit", "Price/Unit (₹)", "GST", "Amount (₹)"]]
    count = 1
    subtotal = 0
    for productId, quantity in items:
        cursor.execute("SELECT productName, price FROM stock WHERE id=%s", (productId,))
        product = cursor.fetchone()
        item = product[0]
        price = product[1]
        total = price * quantity
        subtotal += total
        table_data.append([count, item, "2508", quantity, "tonne", f"{price:.2f}", f"{(price * gst_rate / 100):.2f} ({gst_rate:.1f}%)", f"{total:.2f}"])
        count += 1
    
    gst_amount = (subtotal * gst_rate) / 100
    total_after_discount = subtotal - discount
    final_total = total_after_discount + gst_amount
    
    table_data.append(["", "Total", "", "", "", "", "", f"{subtotal:.2f}"])
    
    table = Table(table_data, colWidths=[30, 150, 70, 50, 50, 70, 70, 80])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.steelblue),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    
    # Draw Table
    table.wrapOn(c, width, height)
    table.drawOn(c, 20, height - 440)  # Adjusted position
    
    # Amount Summary
    c.setFont("Helvetica-Bold", 12)
    c.drawString(400, height - 460, "Sub Total: ")
    c.drawString(500, height - 460, f"\u20B9{subtotal:.2f}")
    c.drawString(400, height - 480, f"IGST@{gst_rate}%: ")
    c.drawString(500, height - 480, f"\u20B9{gst_amount:.2f}")
    c.drawString(400, height - 500, "Total: ")
    c.drawString(500, height - 500, f"\u20B9{final_total:.2f}")
    
    # Bank Details
    c.setFont("Helvetica-Bold", 12)
    c.drawString(50, height - 540, "Pay To:")
    c.setFont("Helvetica", 10)
    text = c.beginText(50, height - 560)
    for line in bank_details.split('\n'):
        text.textLine(line)
    c.drawText(text)
    
    # Authorized Signatory
    c.setFont("Helvetica-Bold", 12)
    c.drawString(400, height - 590, "Authorized Signatory")
    
    c.save()
    print(f"Invoice {filename} generated successfully!")
