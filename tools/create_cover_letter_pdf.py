from pathlib import Path
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

out = Path(r"C:\Users\syesudasan\OneDrive - University of New Haven\RESEARCH\2. Journals\in preparation\0. Review paper Sumith\manuscript\submission\Cover_Letter_Seminars_in_Thrombosis_and_Hemostasis.pdf")
styles = getSampleStyleSheet()
body = ParagraphStyle("Body", parent=styles["Normal"], fontName="Helvetica", fontSize=10.2, leading=13.0, spaceAfter=7)
small = ParagraphStyle("Small", parent=body, fontSize=9.4, leading=11.5, textColor=HexColor("#555555"), spaceAfter=1)
name = ParagraphStyle("Name", parent=body, fontName="Helvetica-Bold", fontSize=16, leading=18, textColor=HexColor("#1F4D78"), spaceAfter=3)
footer = ParagraphStyle("Footer", parent=body, fontSize=8.2, textColor=HexColor("#777777"), alignment=TA_CENTER)

doc = SimpleDocTemplate(str(out), pagesize=letter, leftMargin=0.9*inch, rightMargin=0.9*inch, topMargin=0.55*inch, bottomMargin=0.5*inch,
                        title="Cover Letter - Seminars in Thrombosis and Hemostasis", author="Sumith Yesudasan")
s=[]
s += [Paragraph("SUMITH YESUDASAN", name),
      Paragraph("<b>Department of Mechanical and Industrial Engineering</b>", body),
      Paragraph("University of New Haven | 300 Boston Post Road | West Haven, CT 06516, USA", small),
      Paragraph("syesudasan@newhaven.edu", small), Spacer(1,10),
      Paragraph("July 19, 2026", body), Spacer(1,4),
      Paragraph("Emmanuel J. Favaloro, PhD, FFSc (RCPA)<br/>Editor-in-Chief<br/><i>Seminars in Thrombosis and Hemostasis</i><br/>Institute of Clinical Pathology and Medical Research<br/>Westmead Hospital<br/>Westmead, New South Wales, Australia", body), Spacer(1,4),
      Paragraph("Dear Professor Favaloro:", body),
      Paragraph("<b>Re: Submission of the Review Article, <i>Multiscale Computational Modeling of Fibrin Polymerization: Molecular Mechanisms, Network Assembly, and Emerging Challenges</i></b>", body),
      Paragraph("Please consider the enclosed manuscript for publication as a Review Article in <i>Seminars in Thrombosis and Hemostasis</i>. The article critically evaluates computational approaches to fibrin formation across atomistic, coarse-grained, mesoscopic, fiber-network, and continuum scales.", body),
      Paragraph("The review is organized around a central question: when can a multiscale fibrin model be considered predictive rather than merely representational? It examines parameter provenance, thermodynamic and kinetic consistency, hierarchical validation, uncertainty transfer, and the treatment of pathological perturbations. The manuscript also distinguishes thrombin-mediated activation, reversible knob-hole recognition, lateral association, factor XIIIa-mediated crosslinking, mechanical damage, and fibrinolytic degradation as separate mechanisms.", body),
      Paragraph("This synthesis should be relevant to the journal's readership because it connects molecular mechanisms of fibrin polymerization with clot architecture, mechanics, permeability, fibrinolysis, and failure, while identifying practical priorities for experimentally constrained computational modeling.", body),
      Paragraph("The manuscript is original, has not been published previously, and is not under consideration by another journal. I am the sole author, have approved the submitted version, and declare no competing interests. No new experimental data were generated for this review.", body),
      Paragraph("Thank you for considering this manuscript. I would be grateful for the opportunity to have it evaluated for publication in <i>Seminars in Thrombosis and Hemostasis</i>.", body),
      Spacer(1,5), Paragraph("Sincerely,", body), Spacer(1,9),
      Paragraph("<b>Sumith Yesudasan</b><br/>Department of Mechanical and Industrial Engineering<br/>University of New Haven<br/>syesudasan@newhaven.edu", body)]

def add_footer(canvas, document):
    canvas.saveState(); canvas.setFont("Helvetica",8.2); canvas.setFillColor(HexColor("#777777"));
    canvas.drawCentredString(letter[0]/2, 0.28*inch, "Cover Letter | Seminars in Thrombosis and Hemostasis"); canvas.restoreState()

doc.build(s, onFirstPage=add_footer)
print(out)
