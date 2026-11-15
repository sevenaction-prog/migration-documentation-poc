#!/usr/bin/env python3
"""Generate fictional, public-safe Office templates from text-native sources."""
from pathlib import Path
import csv
from collections import Counter, defaultdict
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "templates"
BLUE = "173747"
GREEN = "127569"
GOLD = "C7A66F"
PALE = "EAF2F0"

def read_csv(filename):
    with (SRC / filename).open("r", encoding="utf-8-sig", newline="") as stream:
        rows = list(csv.reader(stream))
    return rows[0], [r + [""] * max(0, len(rows[0]) - len(r)) for r in rows[1:] if any(c.strip() for c in r)]

def style_sheet(ws, widths=None):
    ws.sheet_view.showGridLines = False
    ws.freeze_panes = "A2"
    ws.row_dimensions[1].height = 34
    for cell in ws[1]:
        cell.fill = PatternFill("solid", fgColor=BLUE)
        cell.font = Font(name="Aptos", size=10, bold=True, color="FFFFFF")
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    for row in ws.iter_rows(min_row=2):
        for c in row:
            c.font = Font(name="Aptos", size=10, color=("127569" if c.column in (3, 6) else "344D55"))
            c.alignment = Alignment(vertical="top", wrap_text=True)
            if c.row % 2 == 0:
                c.fill = PatternFill("solid", fgColor="F5F8F7")
    for i in range(1, ws.max_column + 1):
        width = (widths or {}).get(i, 22)
        ws.column_dimensions[get_column_letter(i)].width = width
    ws.auto_filter.ref = ws.dimensions

def populate(ws, headers, rows, widths=None):
    ws.append(headers)
    for row in rows:
        ws.append(list(row[:len(headers)]) + [""] * max(0, len(headers)-len(row)))
    style_sheet(ws, widths)

def readme_sheet(wb, title, note, source_file):
    ws = wb.active
    ws.title = "00_Guide"
    populate(ws, ["Champ", "Description"], [
        ["Modèle", title],
        ["Statut", "EXEMPLE SYNTHÉTIQUE - aucune donnée client"],
        ["Objet", note],
        ["Source de structure", source_file],
        ["Règle de preuve", "CONFIRMED = observation ou décision ; RECOMMENDED = proposition ; TO VALIDATE = arbitrage"],
        ["Sécurité", "Évaluer droits, conservation et données personnelles avant chaque migration"],
        ["Mode d'emploi", "Remplacer toutes les lignes d'exemple par un inventaire autorisé, en environnement contrôlé"],
    ], {1:28,2:110})
    ws.auto_filter.ref = None

def make_csv_template(n, source, dest, title):
    headers, rows = read_csv(source)
    wb = Workbook()
    readme_sheet(wb, title, "Reprendre ce modèle et personnaliser la qualification métier.", source)
    ws = wb.create_sheet("01_Mapping")
    populate(ws, headers, rows, {i: (52 if any(k in h.lower() for k in ("path", "location", "justification", "evidence")) else 28 if len(h)>16 else 22) for i, h in enumerate(headers, 1)})
    wb.properties.title = "Document Atlas | " + title
    wb.properties.creator = "Document Atlas - Fictional Templates"
    wb.properties.description = "Synthetic reusable template, no real people or client data"
    wb.save(SRC / dest)

def md_to_docx(source, dest, title):
    doc = Document()
    sec = doc.sections[0]
    sec.top_margin = Inches(.78)
    sec.bottom_margin = Inches(.75)
    sec.left_margin = Inches(.9)
    sec.right_margin = Inches(.9)
    normal = doc.styles["Normal"]
    normal.font.name = "Aptos"
    normal.font.size = Pt(10)
    normal.font.color.rgb = RGBColor(40, 60, 68)
    normal.paragraph_format.space_after = Pt(6)
    for key, size in (("Title",25), ("Heading 1",16), ("Heading 2",12)):
        st = doc.styles[key]
        st.font.name = "Aptos Display"
        st.font.size = Pt(size)
        st.font.bold = True
        st.font.color.rgb = RGBColor(23,55,71)
    doc.add_heading(title, 0)
    p = doc.add_paragraph("MODÈLE PUBLIC · EXEMPLES FICTIFS · À ADAPTER AU PROJET")
    p.style = "Subtitle"
    p.runs[0].font.color.rgb = RGBColor(18, 117, 105)
    lines = (SRC / source).read_text(encoding="utf-8").splitlines()
    table_buffer = []
    def flush_table():
        nonlocal table_buffer
        if not table_buffer: return
        parsed = [[x.strip() for x in line.strip().strip("|").split("|")] for line in table_buffer]
        parsed = [r for r in parsed if not all(set(x.strip()) <= set("-: ") for x in r)]
        if parsed:
            cols = max(map(len, parsed))
            t = doc.add_table(rows=0, cols=cols)
            t.style = "Light Shading Accent 1"
            for i,row in enumerate(parsed):
                cells = t.add_row().cells
                for j,val in enumerate(row): cells[j].text = val
        table_buffer = []
    for line in lines:
        s = line.strip()
        if s.startswith("|"):
            table_buffer.append(s)
            continue
        flush_table()
        if not s:
            continue
        if s.startswith("# "):
            continue
        if s.startswith("## "):
            doc.add_heading(s[3:], level=1)
        elif s.startswith("### "):
            doc.add_heading(s[4:], level=2)
        elif s.startswith(("- ", "* ")):
            doc.add_paragraph(s[2:].replace("**",""), style="List Bullet")
        else:
            doc.add_paragraph(s.replace("**", ""))
    flush_table()
    footer = sec.footer.paragraphs[0]
    footer.text = "DOCUMENT ATLAS  •  Modèle générique  •  Aucune donnée réelle"
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.runs[0].font.size = Pt(8)
    doc.core_properties.author = "Document Atlas"
    doc.core_properties.title = title
    doc.save(SRC / dest)

def make_detailed_mapping():
    headers, rows = read_csv("08_detailed_document_level_mapping.csv")
    d = [dict(zip(headers, r)) for r in rows]
    wb = Workbook()
    readme_sheet(wb, "Mapping détaillé au niveau document", "Une ligne par pièce - qualification / preuve / processus / action.", "08_detailed_document_level_mapping.csv")
    ws = wb.create_sheet("01_Mapping_Documents")
    populate(ws, headers, rows, {i: (58 if any(k in h.lower() for k in ("location", "why", "source", "process")) else 30) for i,h in enumerate(headers,1)})
    ws = wb.create_sheet("02_Familles")
    f = Counter((r["Business scope candidate"], r["Business family / activity"]) for r in d)
    populate(ws, ["Scope", "Famille métier", "Nombre de lignes (exemple)"], [[a,b,c] for (a,b),c in sorted(f.items())], {1:30,2:48,3:25})
    ws = wb.create_sheet("03_Processus")
    p = Counter((r["Enterprise process"], r["Enterprise sub-process"],r["Official sub-process label"]) for r in d)
    populate(ws, ["Process", "Sous-processus", "Libellé générique", "Nombre"], [[a,b,c,n] for (a,b,c),n in sorted(p.items())],{1:20,2:22,3:45,4:16})
    ws = wb.create_sheet("04_Arbitrages")
    undecided = [r for r in d if "VALIDATE" in r["Mapping status"]]
    populate(ws, ["ID", "Document", "Statut", "Action proposée", "Owner", "Décision", "Commentaire"],[[r["ID"], r["Document name"],r["Mapping status"],r["Migration action candidate"],"TO VALIDATE","",""] for r in undecided],{1:18,2:42,3:30,4:50,5:22,6:22,7:44})
    ws = wb.create_sheet("05_Securite")
    populate(ws, ["ID", "Type de contenu", "Sensibilité candidate", "Restrictions d'accès", "Rétention à confirmer"],[[r["ID"],r["Document nature"],r["Sensitivity candidate"],"TO VALIDATE","TO VALIDATE"] for r in d],{1:18,2:33,3:30,4:30,5:32})
    ws = wb.create_sheet("06_Controles")
    populate(ws, ["Contrôle", "Résultat exemple", "Action"],[
       ["Fichiers inventoriés", len(d), "Réconcilier avec l'inventaire réel"],
       ["Candidats ROT / Techniques", sum(r["ROT / Technical"].lower()=="yes" for r in d), "Approuver exclusions avant suppression"],
       ["Archives candidates", sum(r["Archive candidate"].lower()=="yes" for r in d), "Confirmer la conservation"],
       ["Mappings à valider", len(undecided), "Soumettre au Business Owner"],
       ["Données réelles", 0, "Ne jamais publier de données client sur GitHub public"]],{1:42,2:25,3:58})
    wb.properties.title = "Document Atlas | Detailed document mapping"
    wb.properties.creator = "Document Atlas"
    wb.save(SRC / "08_detailed_document_level_mapping.xlsx")

def make_traceability():
    source=(SRC/"07_detailed_architecture_traceability.md").read_text()
    wb=Workbook()
    readme_sheet(wb,"Architecture et traçabilité","Source → Décision → BRQ → Feature → Rule → Process → Acceptance → Story","07_detailed_architecture_traceability.md")
    import re
    sections=re.split(r"^##\s+",source,flags=re.M)[1:]
    for part in sections:
        lines=part.splitlines()
        title=lines[0].strip()
        data=[r.strip()[2:] for r in lines[1:] if r.strip().startswith("- ")]
        if not data:
            data=["ID","Description","Statut","Responsable"]
        sheet_name=re.sub(r"[^A-Za-z0-9_]", "_", title)[:28]
        ws=wb.create_sheet(sheet_name)
        populate(ws,data,[],{i:32 for i in range(1,len(data)+1)})
        for i in range(2,7):
            for j in range(1,len(data)+1):
                ws.cell(row=i,column=j).value=""
    wb.properties.creator = "Document Atlas"
    wb.save(SRC/"07_detailed_architecture_traceability.xlsx")

def main():
    md_to_docx("01_target_sharepoint_architecture.md","01_target_sharepoint_architecture.docx","Target SharePoint Architecture")
    md_to_docx("02_migration_requirements_template.md","02_migration_requirements_template.docx","Migration Requirements Template")
    for n,stem,title in [
        ("03","solution_target_top7_metadata","Target Solution - Top 7 Metadata"),
        ("04","simple_category_family_library_mapping","Category / Family / Library Mapping"),
        ("05","source_to_target_mapping","Source-to-Target Mapping"),
        ("06","workshop_before_after_comparison","Before / After Workshop Comparison"),
    ]:
        make_csv_template(n,n+"_"+stem+".csv",n+"_"+stem+".xlsx",title)
    make_traceability()
    make_detailed_mapping()
    # Sector-specific fictitious cases inspired by prior domains (never historical client deliverables).
    md_to_docx("10_eu_institution_integration_guide.md",
                "10_eu_institution_integration_guide.docx",
                "Institutional financial integration - BA/FA guide")
    md_to_docx("14_consumer_credit_api_governance_guide.md",
                "14_consumer_credit_api_governance_guide.docx",
                "Consumer credit - reference data and API governance")
    for n,stem,title in [
        ("11","institutional_field_mapping","Financial Integration - Field Mapping"),
        ("12","institutional_rules_traceability","Financial Integration - Rules and Traceability"),
        ("13","institutional_handover_register","Financial Integration - Handover Register"),
        ("15","consumer_credit_product_vehicle_api","Consumer Credit - Product Vehicle API Mapping"),
        ("16","consumer_credit_agile_backlog","Consumer Credit - Agile Backlog"),
        ("17","consumer_credit_dms_control","Consumer Credit - DMS Control"),
    ]:
        make_csv_template(n,n+"_"+stem+".csv",n+"_"+stem+".xlsx",title)
    # Public-safe templates reconstructed from the three uploaded POC families.
    for n,stem,title in [
        ("18","ai_delivery_14_phase_guide","AI Delivery - 14 Phase Method"),
        ("21","ai_prompt_rag_eval_spec","AI - Prompt RAG Evaluation Specification"),
        ("24","junior_document_discovery_workshop","Junior BA - Documentary Workshop Guide"),
        ("27","payment_assurance_functional_spec","Payment Control Assurance - Functional Requirements"),
    ]:
        md_to_docx(n+"_"+stem+".md",n+"_"+stem+".docx",title)
    for n,stem,title in [
        ("19","ai_use_case_roi_canvas","AI - Use Case and ROI Canvas"),
        ("20","ai_eval_hitl_risk_register","AI - Evals HITL and Risk"),
        ("22","junior_discovery_repository_document","Junior BA - Repositories and Documents"),
        ("23","junior_workflow_interface_decisions","Junior BA - Workflow and Decisions"),
        ("25","payment_control_mapping","Payment - Control Mapping"),
        ("26","payment_test_evidence_chain","Payment - Evidence and Reperformance"),
        ("28","payment_claims_validation","Payment - Claims Validation Register"),
    ]:
        make_csv_template(n,n+"_"+stem+".csv",n+"_"+stem+".xlsx",title)
    print("Office templates generated:", sorted(x.name for x in SRC.glob("*.xlsx")) + sorted(x.name for x in SRC.glob("*.docx")))

if __name__ == "__main__":
    main()
