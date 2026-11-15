const pptxgen=require("pptxgenjs");
const pptx=new pptxgen();
pptx.layout="LAYOUT_WIDE";
pptx.author="Document Atlas";
pptx.subject="Reusable decision-maker workshop, synthetic examples only";
pptx.title="Decision Workshop - Process Validation";
pptx.lang="fr-BE";
pptx.theme={headFontFace:"Aptos Display",bodyFontFace:"Aptos",lang:"fr-BE"};
const C={navy:"172E39",navy2:"254550",gold:"C5A16E",white:"FFFFFF",pale:"F3F6F4",ink:"203B46",muted:"5E737C",green:"15776D"};
const SW=13.333,SH=7.5;
function title(slide,n,name,sub){
slide.background={color:C.pale};
slide.addShape(pptx.ShapeType.rect,{x:0,y:0,w:SW,h:.88,fill:{color:C.navy},line:{color:C.navy}});
slide.addText("DOCUMENT ATLAS  /  ATELIER DE VALIDATION",{x:.55,y:.20,w:5.7,h:.26,fontFace:"Aptos",fontSize:10,color:C.gold,bold:true,charSpacing:1.0,margin:0});
slide.addText(name,{x:.60,y:1.13,w:12.1,h:.58,fontFace:"Aptos Display",fontSize:28,color:C.navy,bold:true,margin:0});
slide.addText(sub,{x:.62,y:1.82,w:12.0,h:.45,fontFace:"Aptos",fontSize:13,color:C.muted,margin:0,breakLine:false});
slide.addText("EXEMPLE FICTIF · À ADAPTER AU PÉRIMÈTRE",{x:.62,y:7.17,w:7.0,h:.18,fontSize:8,color:"819197",margin:0});
slide.addText(String(n).padStart(2,"0"),{x:12.22,y:7.10,w:.45,h:.22,fontSize:10,color:C.green,bold:true,align:"right",margin:0});
}
function card(slide,x,y,w,h,head,body,accent=C.green){
slide.addShape(pptx.ShapeType.roundRect,{x,y,w,h,rectRadius:.12,fill:{color:C.white},line:{color:"DBE4E2",width:1},radius:.10});
slide.addShape(pptx.ShapeType.rect,{x:x+.18,y:y+.25,w:.07,h:h-.50,fill:{color:accent},line:{color:accent}});
slide.addText(head,{x:x+.41,y:y+.26,w:w-.57,h:.33,fontSize:16,color:C.navy,bold:true,margin:0,breakLine:false});
slide.addText(body,{x:x+.41,y:y+.71,w:w-.57,h:h-.86,fontSize:12,color:C.muted,margin:0,breakLine:false, valign:"top",breakLine:false});
}
function tag(slide,x,y,w,text){
slide.addShape(pptx.ShapeType.roundRect,{x,y,w,h:.48,rectRadius:.09,fill:{color:"E2ECE8"},line:{color:"E2ECE8"}});
slide.addText(text,{x:x+.1,y:y+.11,w:w-.2,h:.23,fontSize:12,color:C.navy,bold:true,align:"center",margin:0});
}
function footnote(slide,body){slide.addText(body,{x:.6,y:6.45,w:12.1,h:.42,fontSize:11,italic:true,color:C.green,margin:0});}
let s=pptx.addSlide();s.background={color:C.navy};
s.addShape(pptx.ShapeType.arc,{x:9.0,y:.6,w:5.1,h:5.1,rotate:20,adjustPoint:.4,line:{color:C.gold,width:2,transparency:40},fill:{color:C.navy,transparency:100}});
s.addText("DOCUMENT ATLAS",{x:.72,y:.62,w:7,h:.35,fontSize:15,charSpacing:2.5,color:C.gold,bold:true,margin:0});
s.addText("VALIDATION DES\nPROCESSUS",{x:.75,y:1.65,w:10.1,h:2.1,fontSize:48,bold:true,color:C.white,margin:0,breakLine:false});
s.addText("Workshop décisionnaire · 60 minutes",{x:.78,y:4.18,w:9.5,h:.43,fontSize:20,color:"D5E4E1",margin:0});
s.addText("Un canevas de décision basé sur des données entièrement fictives.",{x:.78,y:5.12,w:10.9,h:.55,fontSize:15,color:"C3D4D1",margin:0});
s.addNotes("Source : Document Atlas, canevas méthodologique générique; aucune donnée réelle.");
s=pptx.addSlide();title(s,2,"Pourquoi cette validation ?","Le modèle de classification est disponible, la décision métier reste à formaliser.");
card(s,.65,2.56,3.88,2.8,"AVANT L’ATELIER","Les familles documentaires sont inventoriées et les rattachements sont proposés.");
card(s,4.72,2.56,3.88,2.8,"NOUVELLE RÉFÉRENCE","Une taxonomie de processus générique est mise à disposition.");
card(s,8.79,2.56,3.88,2.8,"À DÉCIDER","Confirmer le processus principal, ses interfaces et les exceptions.",C.gold);
footnote(s,"Principe : une taxonomie connue ne constitue pas une décision automatique.");
s=pptx.addSlide();title(s,3,"Notre périmètre de validation","Les métriques et exemples ci-dessous sont volontairement synthétiques.");
const metrics=[["20","documents fictifs"],["5","familles candidates"],["6","sous-processus génériques"],["0","donnée réelle"]];
metrics.forEach((v,i)=>{let x=.66+i*3.19;s.addShape(pptx.ShapeType.roundRect,{x,y:2.55,w:2.99,h:1.8,rectRadius:.13,fill:{color:C.white},line:{color:"DDE6E1"}});s.addText(v[0],{x:x+.2,y:2.81,w:2.55,h:.72,fontSize:39,color:C.navy,bold:true,align:"center",margin:0});s.addText(v[1],{x:x+.12,y:3.60,w:2.75,h:.32,fontSize:12,color:C.muted,align:"center",margin:0});});
card(s,.68,4.68,5.95,1.48,"HOLD / ARCHIVE","Retarder la décision définitive avant confirmation des règles.");
card(s,6.82,4.68,5.82,1.48,"SÉCURITÉ","Tester les droits d’accès séparément de la classification.",C.gold);
s=pptx.addSlide();title(s,4,"Référentiel de processus fictif","Six sous-processus d’illustration : à remplacer par le référentiel autorisé du client.");
const ref=[["PROC-01","Veille & cadre"],["PROC-02","Objectifs"],["PROC-03","Organisation"],["PROC-04","Opérations"],["PROC-05","Performance"],["PROC-06","Communication"]];
ref.forEach((v,i)=>card(s,.67+(i%3)*4.2,2.44+Math.floor(i/3)*1.95,3.92,1.62,v[0],v[1],i%2?C.gold:C.green));
s=pptx.addSlide();title(s,5,"Proposition de rattachement principal","Une hypothèse à challenger par le décideur métier.");
const labels=[["PROC-01","Veille réglementaire"],["PROC-02","Objectifs & politique"],["PROC-03","Gouvernance & standards"],["PROC-04","Activités & incidents"],["PROC-05","Audits & reporting"],["PROC-06","Sensibilisation"]];
labels.forEach((v,i)=>card(s,.67+(i%2)*6.28,2.4+Math.floor(i/2)*1.32,6.0,1.17,v[0],v[1],i%2?C.gold:C.green));
footnote(s,"Statut : RECOMMANDÉ / À VALIDER — aucune affectation réelle n’est affirmée.");
s=pptx.addSlide();title(s,6,"Interfaces à valider","Une interface contributrice n’est pas nécessairement un processus principal.");
tag(s,4.63,2.56,4.0,"PROCESSUS PRINCIPAL");
[["PEOPLE","Formation / personnel"],["RISK","Crise / continuité"],["FACILITY","Équipements"],["LEGAL","Conformité"]].forEach((v,i)=>{let x=.8+(i%2)*6.28,y=3.55+Math.floor(i/2)*1.40;card(s,x,y,5.95,1.17,v[0],v[1]);});
s=pptx.addSlide();title(s,7,"Cinq arbitrages prioritaires","Le reste peut être validé par lots homogènes.");
[["01","Gouvernance","Qui est le Process Owner ?"],["02","Crise","Quel lien avec la gestion des risques ?"],["03","Équipements","Quelle part relève des services généraux ?"],["04","Dossiers sensibles","Quelles restrictions et durées ?"],["05","Hors cœur","Quel arbitrage pour les exceptions ?"]].forEach((v,i)=>{let y=2.32+i*.80;s.addShape(pptx.ShapeType.roundRect,{x:.73,y,w:11.89,h:.67,rectRadius:.08,fill:{color:i%2?"EAF0ED":"FFFFFF"},line:{color:"DDE6E2"}});s.addText(v[0],{x:.95,y:y+.15,w:.5,h:.25,fontSize:14,color:C.gold,bold:true,margin:0});s.addText(v[1],{x:1.55,y:y+.16,w:2.9,h:.25,fontSize:14,color:C.navy,bold:true,margin:0});s.addText(v[2],{x:4.75,y:y+.16,w:7.3,h:.25,fontSize:13,color:C.muted,margin:0});});
s=pptx.addSlide();title(s,8,"Ce qui restera hors décision aujourd’hui","Ne pas confondre validation métier et autorisation de migration.");
card(s,.68,2.40,5.91,1.65,"HOLD","Les zones non libérées restent suspendues.",C.gold);
card(s,6.76,2.40,5.91,1.65,"SÉCURITÉ","Permissions, conservation et confidentialité à confirmer.");
card(s,.68,4.27,5.91,1.65,"TECHNIQUE","Les outils et workflows sont instruits séparément.");
card(s,6.76,4.27,5.91,1.65,"ARCHIVES","Réévaluer la valeur probante avant exclusion.",C.gold);
s=pptx.addSlide();title(s,9,"Agenda de l’atelier — 60 minutes","Une séquence de décision courte, avec propriétaire et prochaines actions.");
const agenda=[["00–05","Cadrage"],["05–15","Référentiel"],["15–35","Mapping principal"],["35–50","Arbitrages"],["50–55","Interfaces"],["55–60","Clôture"]];
agenda.forEach((v,i)=>{let x=.62+i*2.11;s.addShape(pptx.ShapeType.roundRect,{x,y:2.76,w:1.97,h:2.24,rectRadius:.1,fill:{color:i===3?"E7EFE7":C.white},line:{color:"DDE6E2"}});s.addText(v[0],{x:x+.10,y:3.12,w:1.75,h:.41,fontSize:22,color:C.navy,bold:true,align:"center",margin:0});s.addText(v[1],{x:x+.13,y:4.06,w:1.70,h:.55,fontSize:13,color:C.muted,align:"center",margin:0});});
footnote(s,"Support de décision : matrice Excel à compléter en direct.");
s=pptx.addSlide();title(s,10,"Livrables attendus","Le succès se mesure à la traçabilité des choix.");
card(s,.70,2.4,5.85,1.61,"1. STATUT","Confirmer / Modifier / À analyser");
card(s,6.75,2.4,5.85,1.61,"2. PROCESSUS","Processus principal + interfaces");
card(s,.70,4.31,5.85,1.61,"3. RESPONSABLE","Owner, commentaire et preuve");
card(s,6.75,4.31,5.85,1.61,"4. MISE À JOUR","Workbook et cahier des charges");
footnote(s,"Décider le rattachement des documents, pas l’architecture M365.");
pptx.writeFile({fileName:"templates/09_decision_workshop_process_validation.pptx"});
