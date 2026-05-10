from fpdf import FPDF
import datetime

class SEO_PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'SEO Strategy & Optimization Report: Otunba Gbenga Lasore', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

def create_report():
    pdf = SEO_PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Date
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, f"Date: {datetime.date.today().strftime('%B %d, %Y')}", 0, 1)
    pdf.cell(0, 10, "Objective: To establish a dominant and professional digital presence for Otunba Gbenga Lasore.", 0, 1)
    pdf.ln(5)

    # Sections
    sections = [
        ("1. Executive Summary", "We have implemented a comprehensive 'Digital Identity' strategy for Otunba Gbenga Lasore. This project involved optimizing the official website, linking verified social media profiles, and integrating high-authority press articles to ensure a unified and professional appearance on Google."),
        ("2. Actions Taken", ""),
        ("A. Technical SEO", "- Domain Alignment: Updated all internal links and metadata to point to https://gbengalasore.vercel.app/.\n- Sitemap Creation: Generated a sitemap.xml file for complete indexing.\n- Crawler Instructions: Created a robots.txt file to guide search engine bots.\n- Google Verification: Integrated the verification file for direct indexing access."),
        ("B. Identity & Authority", "- Person Schema (JSON-LD): Implemented advanced structured data for AI-driven summaries.\n- Social Connectivity: Linked Instagram and Facebook profiles within the site's code.\n- Press Integration: Featured the Medium article 'The Alchemist of Enterprise' as a primary source."),
        ("C. Visual Optimization", "- Gallery Enhancement: Added 16 high-quality professional images.\n- Image Tagging: Every image now includes 'Alt Tags' featuring his name for Google Image Search."),
        ("3. The 5-Day Projection", "Day 1-2: Google bots will crawl the new sitemap and index the site.\nDay 3: 'Gbenga Lasore' will begin appearing as a top result.\nDay 4-5: AI will cluster social links and images into a unified identity.\nEnd of Week: A dominant search presence will be established."),
        ("4. Next Steps", "1. Request Indexing: Use Google Search Console to manually request a crawl.\n2. Share Links: Post the URL on social media to drive initial authority signals.")
    ]

    for title, content in sections:
        pdf.set_font("Arial", 'B', 12)
        pdf.cell(0, 10, title, 0, 1)
        pdf.set_font("Arial", size=11)
        if content:
            pdf.multi_cell(0, 8, content)
        pdf.ln(3)

    output_path = "/home/alash-studios/Downloads/SEO_Optimization_Report.pdf"
    pdf.output(output_path)
    print(f"PDF created at: {output_path}")

if __name__ == "__main__":
    create_report()
