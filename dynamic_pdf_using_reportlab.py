import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

def mypdf(request):
    # Create a BytesIO buffer
    buffer = io.BytesIO()
    
    # Create a PDF canvas
    c = canvas.Canvas(buffer)
    c.drawString(100, 100, "Hello World!")  # Corrected method name to drawString
    c.showPage()
    c.save()
    
    # Reset buffer position to the beginning
    buffer.seek(0)
    
    # Return the response with the PDF file
    response = FileResponse(buffer, as_attachment=True, filename="mypdffile.pdf", content_type='application/pdf')
    
    return response
