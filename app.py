Jeder Abschnitt hat seinen eigenen Zweck und ist klar getrennt.
        """,
        task="Strukturiere diesen chaotischen Prompt mit XML-Tags, um eine klare Email-Klassifikation zu erstellen.",
        initial_prompt="Schau ob das eine Support-Anfrage oder Beschwerde oder Lob ist: Hilfe, mein Produkt funktioniert nicht!",
        validation_func=validate_xml_classification,
        solution_prompt="""<instruction>
Klassifiziere die folgende Email in eine der vorgegebenen Kategorien.
</instruction>

<categories>
- Support-Anfrage: Kunde braucht Hilfe bei einem Problem
- Beschwerde: Kunde ist unzufrieden 
- Lob: Positive Rückmeldung
- Allgemeine Anfrage: Sonstige Fragen
</categories>

<examples>
Email: "Das Produkt ist kaputt angekommen!"
Kategorie: Beschwerde

Email: "Wie kann ich mein Passwort zurücksetzen?"
Kategorie: Support-Anfrage

Email: "Ihr Service ist fantastisch!"
Kategorie: Lob
</examples>

<task>
Klassifiziere diese Email:
</task>""",
        test_input='Email: "Hilfe, mein Produkt funktioniert nicht!"',
        hints=[
            "Verwende XML-Tags um Anweisungen, Beispiele und Aufgabe zu trennen",
            "Strukturiere mit <instruction>, <examples>, <task> oder ähnlichen Tags",
            "Die Tags sollten semantisch sinnvoll sein",
            "Vergiss nicht die schließenden Tags (</...>)"
        ]
    )
    
    # Exercise 4: Complex XML Analysis
    exercise_box(
        exercise_id="xml_complex",
        title="Übung 4: Komplexe Datenanalyse mit Multi-Level XML",
        concept="Verschachtelte XML-Struktur für komplexe Aufgaben",
        description="""
        **Komplexe Prompts brauchen tiefere Struktur:**
        
        ```xml
        <analysis_context>
            <data_source>Verkaufsdaten Q4</data_source>
            <time_period>Oktober-Dezember</time_period>
        </analysis_context>
        
        <requirements>
            <must_include>
                - Trends
                - Top-Produkte
                - Empfehlungen
            </must_include>
        </requirements>
        ```
        
        Verschachtelung macht komplexe Anforderungen kristallklar.
        """,
        task="Erstelle einen strukturierten Analyse-Prompt mit mindestens 3 verschiedenen XML-Sektionen für eine Verkaufsdatenanalyse.",
        initial_prompt="Analysiere diese Verkaufsdaten und gib mir Insights.",
        validation_func=validate_xml_complex,
        solution_prompt="""<analysis_context>
    <data_type>Monatliche Verkaufsdaten</data_type>
    <period>Q4 2024</period>
    <focus>Trend-Analyse und Strategieempfehlungen</focus>
</analysis_context>

<requirements>
    <analysis_points>
        - Identifiziere die Top 3 Verkaufstrends
        - Analysiere saisonale Muster
        - Vergleiche mit Vorjahresperiode
        - Erkenne Ausreißer oder Anomalien
    </analysis_points>
    
    <deliverables>
        - Executive Summary (3-4 Sätze)
        - Detaillierte Trendanalyse
        - Konkrete Handlungsempfehlungen
        - Risiken und Chancen
    </deliverables>
</requirements>

<output_format>
    <structure>
        1. Haupterkenntnisse (Bullet Points)
        2. Detailanalyse (Prosa)
        3. Empfehlungen (Nummerierte Liste)
        4. Nächste Schritte (Aktionspunkte)
    </structure>
    
    <tone>Professionell, datengetrieben, handlungsorientiert</tone>
</output_format>

<task>
Analysiere die folgenden Verkaufsdaten:
</task>""",
        test_input='Verkaufsdaten: Oktober: 125k€, November: 145k€, Dezember: 198k€ | Top-Produkte: Elektronik (+45%), Mode (+23%), Home (-12%)',
        hints=[
            "Nutze verschiedene XML-Sektionen für Context, Requirements, Format etc.",
            "Verschachtele Tags für mehr Struktur (z.B. <requirements><must_include>...)",
            "Semantische Tag-Namen machen den Prompt verständlicher",
            "Je komplexer die Aufgabe, desto mehr Struktur ist hilfreich"
        ]
    )

# TAB 4: Advanced Techniques
with tab4:
    st.header("🧠 Fortgeschrittene Techniken")
    
    st.markdown("""
    Lerne fortgeschrittene Prompt-Engineering-Techniken, die professionelle Ergebnisse liefern.
    """)
    
    # Exercise 5: Chain of Thought
    exercise_box(
        exercise_id="cot_reasoning",
        title="Übung 5: Chain-of-Thought Reasoning",
        concept="Schrittweises Denken fördern",
        description="""
        **Chain-of-Thought (CoT) Prompting:**
        
        Fördere schrittweises, logisches Denken mit Triggern wie:
        - "Denke Schritt für Schritt"
        - "Lass uns das durchdenken"
        - "Erkläre deine Überlegungen"
        
        Dies führt zu:
        1. Transparenteren Gedankengängen
        2. Weniger Fehlern bei komplexen Aufgaben
        3. Nachvollziehbaren Lösungswegen
        
        Besonders wichtig bei: Mathe, Logik-Rätseln, komplexen Analysen
        """,
        task="Ergänze den Prompt so, dass Claude das Logik-Rätsel Schritt für Schritt löst und seine Gedankengänge erklärt.",
        initial_prompt="Löse dieses Rätsel.",
        validation_func=validate_zero_shot_cot,
        solution_prompt="""Lass uns dieses Logik-Rätsel Schritt für Schritt durchdenken.

Erkläre dabei:
1. Was wir wissen
2. Welche Schlüsse wir ziehen können  
3. Wie wir zur Antwort kommen

Denke laut und zeige jeden Zwischenschritt.

Rätsel:""",
        test_input="""In einem Raum sind 3 Personen. 
Jede Person gibt jeder anderen Person genau einmal die Hand.
Dann kommt eine vierte Person und gibt auch jedem die Hand.
Wie viele Personen sind jetzt im Raum?""",
        hints=[
            "Füge eine klare Anweisung für schrittweises Denken hinzu",
            "Phrasen wie 'Denke Schritt für Schritt' oder 'Lass uns das durchdenken' helfen",
            "Fordere explizit Erklärungen der Gedankengänge",
            "Die Antwort sollte 4 Personen sein - mit klarer Herleitung"
        ]
    )
    
    # Exercise 6: Role-Based Prompting
    exercise_box(
        exercise_id="role_expert",
        title="Übung 6: Experten-Rolle definieren",
        concept="Role Prompting für Expertise",
        description="""
        **Role Prompting - Definiere Expertise:**
        
        Gib der KI eine spezifische Rolle:
        - "Du bist ein erfahrener Datenanalyst..."
        - "Als Marketing-Experte..."
        - "In deiner Rolle als Finanzberater..."
        
        Vorteile:
        - Fachspezifische Terminologie
        - Passender Ton und Stil
        - Fokussierte Perspektive
        - Professionellere Outputs
        """,
        task="Definiere eine Experten-Rolle für eine professionelle Datenanalyse. Der Output sollte Fachterminologie und strukturierte Insights zeigen.",
        initial_prompt="Schau dir diese Zahlen an und sag mir was du siehst.",
        validation_func=validate_role_prompt,
        solution_prompt="""Du bist ein erfahrener Datenanalyst mit 10+ Jahren Expertise in Business Intelligence und statistischer Analyse.

Deine Aufgabe:
Analysiere die folgenden Geschäftsdaten mit deinem Fachwissen. Identifiziere:
- Statistisch signifikante Trends
- Kritische Muster und Anomalien  
- Datenbasierte Handlungsempfehlungen
- Potenzielle Risiken und Chancen

Verwende dabei professionelle Fachterminologie und strukturiere deine Analyse nach Best Practices der Datenanalyse.

Präsentiere deine Erkenntnisse in einem Executive-Format mit:
• Haupterkenntnisse (Key Insights)
• Detaillierte Analyse
• Empfehlungen mit Priorisierung
• Next Steps

Daten:""",
        test_input="Umsatz Q1: 450k€, Q2: 380k€, Q3: 420k€, Q4: 510k€ | Kundenanzahl: Q1: 1200, Q2: 950, Q3: 1100, Q4: 1450",
        hints=[
            "Definiere eine spezifische Rolle (z.B. 'Du bist ein Datenanalyst...')",
            "Erwähne relevante Expertise oder Erfahrung",
            "Fordere Fachterminologie und professionelle Struktur",
            "Die Rolle sollte zum gewünschten Output-Stil passen"
        ]
    )

# Footer with summary
st.markdown("---")

# Summary section
if any(st.session_state.exercise_status.values()):
    st.header("📊 Deine Lernerfolge")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        completed_exercises = [k for k, v in st.session_state.exercise_status.items() if v]
        if completed_exercises:
            st.metric("Abgeschlossene Übungen", len(completed_exercises))
            for ex_id in completed_exercises:
                exercise_names = {
                    "fs_sentiment": "Sentiment-Analyse",
                    "fs_extraction": "Datenextraktion",
                    "xml_basic": "XML-Klassifikation",
                    "xml_complex": "Komplexe XML-Analyse",
                    "cot_reasoning": "Chain-of-Thought",
                    "role_expert": "Experten-Rolle"
                }
                st.write(f"✅ {exercise_names.get(ex_id, ex_id)}")
    
    with col2:
        techniques_learned = []
        if "fs_sentiment" in completed_exercises or "fs_extraction" in completed_exercises:
            techniques_learned.append("Few-Shot Learning")
        if "xml_basic" in completed_exercises or "xml_complex" in completed_exercises:
            techniques_learned.append("XML-Strukturierung")
        if "cot_reasoning" in completed_exercises:
            techniques_learned.append("Chain-of-Thought")
        if "role_expert" in completed_exercises:
            techniques_learned.append("Role Prompting")
        
        if techniques_learned:
            st.metric("Gelernte Techniken", len(techniques_learned))
            for tech in techniques_learned:
                st.write(f"🎯 {tech}")
    
    with col3:
        completion_rate = len(completed_exercises) / 6 * 100
        st.metric("Abschlussrate", f"{completion_rate:.0f}%")
        
        if completion_rate == 100:
            st.success("🏆 **Prompt Engineering Master!**")
            st.write("Du hast alle Techniken gemeistert!")
        elif completion_rate >= 66:
            st.info("🥈 **Fast geschafft!**")
            st.write("Noch ein paar Übungen bis zum Meister!")
        else:
            st.warning("🎯 **Weiter so!**")
            st.write("Entdecke noch mehr Techniken!")

# Final footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: #666;'>
    <p><strong>🎓 Prompt Engineering Workshop</strong></p>
    <p>Entwickelt für KI & Kreativität | Powered by Claude API & Streamlit</p>
    <p style='font-size: 0.9em; margin-top: 10px;'>
        💡 <em>Tipp: Die besten Prompts kombinieren mehrere Techniken!</em>
    </p>
</div>
""", unsafe_allow_html=True)        Jeder Abschnitt hat seinen eigenen Zweck und ist klar getrennt.schnitt hat seinen eigenen Zweck und ist klar getrennt.
        """,
        task="Strukturiere diesen chaotischen Prompt mit XML-Tags, um eine klare Email-Klassifikation zu erstellen.",
        initial_prompt="Schau ob das eine Support-Anfrage oder Beschwerde oder Lob ist: Hilfe, mein Produkt funktioniert nicht!",
        validation_func=validate_xml_classification,
        solution_prompt="""<instruction>
Klassifiziere die folgende Email in eine der vorgegebenen Kategorien.
</instruction>

<categories>
- Support-Anfrage: Kunde braucht Hilfe bei einem Problem
- Beschwerde: Kunde ist unzufrieden 
- Lob: Positive Rückmeldung
- Allgemeine Anfrage: Sonstige Fragen
</categories>

<examples>
Email: "Das Produkt ist kaputt angekommen!"
Kategorie: Beschwerde

Email: "Wie kann ich mein Passwort zurücksetzen?"
Kategorie: Support-Anfrage

Email: "Ihr Service ist fantastisch!"
Kategorie: Lob
</examples>

<task>
Klassifiziere diese Email:
</task>""",
        test_input='Email: "Hilfe, mein Produkt funktioniert nicht!"',
        hints=[
            "Verwende XML-Tags um Anweisungen, Beispiele und Aufgabe zu trennen",
            "Strukturiere mit <instruction>, <examples>, <task> oder ähnlichen Tags",
            "Die Tags sollten semantisch sinnvoll sein",
            "Vergiss nicht die schließenden Tags (</...>)"
        ]
    )
    
    # Exercise 4: Complex XML Analysis
    exercise_box(
        exercise_id="xml_complex",
        title="Übung 4: Komplexe Datenanalyse mit Multi-Level XML",
        concept="Verschachtelte XML-Struktur für komplexe Aufgaben",
        description="""
        **Komplexe Prompts brauchen tiefere Struktur:**
        
        ```xml
        <analysis_context>
            <data_source>Verkaufsdaten Q4</data_source>
            <time_period>Oktober-Dezember</time_period>
        </analysis_context>
        
        <requirements>
            <must_include>
                - Trends
                - Top-Produkte
                - Empfehlungen
            </must_include>
        </requirements>
        ```
        
        Verschachtelung macht komplexe Anforderungen kristallklar.
        """,
        task="Erstelle einen strukturierten Analyse-Prompt mit mindestens 3 verschiedenen XML-Sektionen für eine Verkaufsdatenanalyse.",
        initial_prompt="Analysiere diese Verkaufsdaten und gib mir Insights.",
        validation_func=validate_xml_complex,
        solution_prompt="""<analysis_context>
    <data_type>Monatliche Verkaufsdaten</data_type>
    <period>Q4 2024</period>
    <focus>Trend-Analyse und Strategieempfehlungen</focus>
</analysis_context>

<requirements>
    <analysis_points>
        - Identifiziere die Top 3 Verkaufstrends
        - Analysiere saisonale Muster
        - Vergleiche mit Vorjahresperiode
        - Erkenne Ausreißer oder Anomalien
    </analysis_points>
    
    <deliverables>
        - Executive Summary (3-4 Sätze)
        - Detaillierte Trendanalyse
        - Konkrete Handlungsempfehlungen
        - Risiken und Chancen
    </deliverables>
</requirements>

<output_format>
    <structure>
        1. Haupterkenntnisse (Bullet Points)
        2. Detailanalyse (Prosa)
        3. Empfehlungen (Nummerierte Liste)
        4. Nächste Schritte (Aktionspunkte)
    </structure>
    
    <tone>Professionell, datengetrieben, handlungsorientiert</tone>
</output_format>

<task>
Analysiere die folgenden Verkaufsdaten:
</task>""",
        test_input='Verkaufsdaten: Oktober: 125k€, November: 145k€, Dezember: 198k€ | Top-Produkte: Elektronik (+45%), Mode (+23%), Home (-12%)',
        hints=[
            "Nutze verschiedene XML-Sektionen für Context, Requirements, Format etc.",
            "Verschachtele Tags für mehr Struktur (z.B. <requirements><must_include>...)",
            "Semantische Tag-Namen machen den Prompt verständlicher",
            "Je komplexer die Aufgabe, desto mehr Struktur ist hilfreich"
        ]
    )

# TAB 4: Advanced Techniques
with tab4:
    st.header("🧠 Fortgeschrittene Techniken")
    
    st.markdown("""
    Lerne fortgeschrittene Prompt-Engineering-Techniken, die professionelle Ergebnisse liefern.
    """)
    
    # Exercise 5: Chain of Thought
    exercise_box(
        exercise_id="cot_reasoning",
        title="Übung 5: Chain-of-Thought Reasoning",
        concept="Schrittweises Denken fördern",
        description="""
        **Chain-of-Thought (CoT) Prompting:**
        
        Fördere schrittweises, logisches Denken mit Triggern wie:
        - "Denke Schritt für Schritt"
        - "Lass uns das durchdenken"
        - "Erkläre deine Überlegungen"
        
        Dies führt zu:
        1. Transparenteren Gedankengängen
        2. Weniger Fehlern bei komplexen Aufgaben
        3. Nachvollziehbaren Lösungswegen
        
        Besonders wichtig bei: Mathe, Logik-Rätseln, komplexen Analysen
        """,
        task="Ergänze den Prompt so, dass Claude das Logik-Rätsel Schritt für Schritt löst und seine Gedankengänge erklärt.",
        initial_prompt="Löse dieses Rätsel.",
        validation_func=validate_zero_shot_cot,
        solution_prompt="""Lass uns dieses Logik-Rätsel Schritt für Schritt durchdenken.

Erkläre dabei:
1. Was wir wissen
2. Welche Schlüsse wir ziehen können  
3. Wie wir zur Antwort kommen

Denke laut und zeige jeden Zwischenschritt.

Rätsel:""",
        test_input="""In einem Raum sind 3 Personen. 
Jede Person gibt jeder anderen Person genau einmal die Hand.
Dann kommt eine vierte Person und gibt auch jedem die Hand.
Wie viele Personen sind jetzt im Raum?""",
        hints=[
            "Füge eine klare Anweisung für schrittweises Denken hinzu",
            "Phrasen wie 'Denke Schritt für Schritt' oder 'Lass uns das durchdenken' helfen",
            "Fordere explizit Erklärungen der Gedankengänge",
            "Die Antwort sollte 4 Personen sein - mit klarer Herleitung"
        ]
    )
    
    # Exercise 6: Role-Based Prompting
    exercise_box(
        exercise_id="role_expert",
        title="Übung 6: Experten-Rolle definieren",
        concept="Role Prompting für Expertise",
        description="""
        **Role Prompting - Definiere Expertise:**
        
        Gib der KI eine spezifische Rolle:
        - "Du bist ein erfahrener Datenanalyst..."
        - "Als Marketing-Experte..."
        - "In deiner Rolle als Finanzberater..."
        
        Vorteile:
        - Fachspezifische Terminologie
        - Passender Ton und Stil
        - Fokussierte Perspektive
        - Professionellere Outputs
        """,
        task="Definiere eine Experten-Rolle für eine professionelle Datenanalyse. Der Output sollte Fachterminologie und strukturierte Insights zeigen.",
        initial_prompt="Schau dir diese Zahlen an und sag mir was du siehst.",
        validation_func=validate_role_prompt,
        solution_prompt="""Du bist ein erfahrener Datenanalyst mit 10+ Jahren Expertise in Business Intelligence und statistischer Analyse.

Deine Aufgabe:
Analysiere die folgenden Geschäftsdaten mit deinem Fachwissen. Identifiziere:
- Statistisch signifikante Trends
- Kritische Muster und Anomalien  
- Datenbasierte Handlungsempfehlungen
- Potenzielle Risiken und Chancen

Verwende dabei professionelle Fachterminologie und strukturiere deine Analyse nach Best Practices der Datenanalyse.

Präsentiere deine Erkenntnisse in einem Executive-Format mit:
• Haupterkenntnisse (Key Insights)
• Detaillierte Analyse
• Empfehlungen mit Priorisierung
• Next Steps

Daten:""",
        test_input="Umsatz Q1: 450k€, Q2: 380k€, Q3: 420k€, Q4: 510k€ | Kundenanzahl: Q1: 1200, Q2: 950, Q3: 1100, Q4: 1450",
        hints=[
            "Definiere eine spezifische Rolle (z.B. 'Du bist ein Datenanalyst...')",
            "Erwähne relevante Expertise oder Erfahrung",
            "Fordere Fachterminologie und professionelle Struktur",
            "Die Rolle sollte zum gewünschten Output-Stil passen"
        ]
    )

# Footer with summary
st.markdown("---")

# Summary section
if any(st.session_state.exercise_status.values()):
    st.header("📊 Deine Lernerfolge")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        completed_exercises = [k for k, v in st.session_state.exercise_status.items() if v]
        if completed_exercises:
            st.metric("Abgeschlossene Übungen", len(completed_exercises))
            for ex_id in completed_exercises:
                exercise_names = {
                    "fs_sentiment": "Sentiment-Analyse",
                    "fs_extraction": "Datenextraktion",
                    "xml_basic": "XML-Klassifikation",
                    "xml_complex": "Komplexe XML-Analyse",
                    "cot_reasoning": "Chain-of-Thought",
                    "role_expert": "Experten-Rolle"
                }
                st.write(f"✅ {exercise_names.get(ex_id, ex_id)}")
    
    with col2:
        techniques_learned = []
        if "fs_sentiment" in completed_exercises or "fs_extraction" in completed_exercises:
            techniques_learned.append("Few-Shot Learning")
        if "xml_basic" in completed_exercises or "xml_complex" in completed_exercises:
            techniques_learned.append("XML-Strukturierung")
        if "cot_reasoning" in completed_exercises:
            techniques_learned.append("Chain-of-Thought")
        if "role_expert" in completed_exercises:
            techniques_learned.append("Role Prompting")
        
        if techniques_learned:
            st.metric("Gelernte Techniken", len(techniques_learned))
            for tech in techniques_learned:
                st.write(f"🎯 {tech}")
    
    with col3:
        completion_rate = len(completed_exercises) / 6 * 100
        st.metric("Abschlussrate", f"{completion_rate:.0f}%")
        
        if completion_rate == 100:
            st.success("🏆 **Prompt Engineering Master!**")
            st.write("Du hast alle Techniken gemeistert!")
        elif completion_rate >= 66:
            st.info("🥈 **Fast geschafft!**")
            st.write("Noch ein paar Übungen bis zum Meister!")
        else:
            st.warning("🎯 **Weiter so!**")
            st.write("Entdecke noch mehr Techniken!")

# Final footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 20px; color: #666;'>
    <p><strong>🎓 Prompt Engineering Workshop</strong></p>
    <p>Entwickelt für KI & Kreativität | Powered by Claude API & Streamlit</p>
    <p style='font-size: 0.9em; margin-top: 10px;'>
        💡 <em>Tipp: Die besten Prompts kombinieren mehrere Techniken!</em>
    </p>
</div>
""", unsafe_allow_html=True)import streamlit as st
import anthropic
import re
from typing import Callable, Tuple
import json

# Page config
st.set_page_config(
    page_title="Prompt Engineering Workshop", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'api_key' not in st.session_state:
    st.session_state.api_key = ""
if 'exercise_status' not in st.session_state:
    st.session_state.exercise_status = {}
if 'show_response' not in st.session_state:
    st.session_state.show_response = {}
if 'show_hints' not in st.session_state:
    st.session_state.show_hints = {}
if 'show_solution' not in st.session_state:
    st.session_state.show_solution = {}
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Custom CSS for better styling
st.markdown("""
<style>
.success-prompt {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 15px;
    border-radius: 10px;
    margin: 10px 0;
    font-weight: bold;
}
.stTextArea > div > div > textarea {
    font-family: 'Courier New', monospace;
    font-size: 14px;
}
.hint-box {
    background-color: #fff3cd;
    border-left: 4px solid #ffc107;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}
.response-box {
    background-color: #f8f9fa;
    border-left: 4px solid #0066cc;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}
.solution-box {
    background-color: #d4edda;
    border-left: 4px solid #28a745;
    padding: 15px;
    margin: 15px 0;
    border-radius: 5px;
}
.error-feedback {
    background-color: #f8d7da;
    border-left: 4px solid #dc3545;
    padding: 10px;
    margin: 10px 0;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("🎓 Prompt Engineering Workshop")
st.markdown("### Meistere die Kunst des Prompt Engineering mit praktischen Übungen")

# Sidebar with API Key and Progress
with st.sidebar:
    st.header("⚙️ Konfiguration")
    
    # API Key Input
    api_key_input = st.text_input(
        "Claude API Key:",
        type="password",
        value=st.session_state.api_key,
        help="Dein API-Key wird nur für diese Session gespeichert"
    )
    
    if api_key_input:
        st.session_state.api_key = api_key_input
        # Test API key validity
        try:
            client = anthropic.Anthropic(api_key=api_key_input)
            test_response = client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=10,
                messages=[{"role": "user", "content": "Hi"}]
            )
            st.success("✅ API Key aktiv")
        except Exception as e:
            st.error("❌ API Key ungültig")
    else:
        st.warning("⚠️ Bitte API Key eingeben")
    
    st.divider()
    
    # Progress Display
    st.header("📊 Dein Fortschritt")
    total_exercises = 6
    completed = len([k for k, v in st.session_state.exercise_status.items() if v])
    progress = completed / total_exercises if total_exercises > 0 else 0
    
    st.progress(progress)
    st.metric("Abgeschlossen", f"{completed}/{total_exercises}")
    
    # Achievement badges
    if completed > 0:
        st.markdown("### 🏆 Errungenschaften")
        if completed >= 2:
            st.markdown("🥉 **Bronze**: Erste Schritte")
        if completed >= 4:
            st.markdown("🥈 **Silber**: Fortgeschritten")
        if completed == total_exercises:
            st.markdown("🥇 **Gold**: Prompt Master!")
    
    st.divider()
    
    # Reset Button
    if st.button("🔄 Fortschritt zurücksetzen", type="secondary"):
        for key in ['exercise_status', 'show_response', 'show_hints', 'show_solution', 'responses']:
            st.session_state[key] = {}
        st.rerun()

# Helper function to call Claude API
def call_claude(prompt: str, api_key: str) -> Tuple[str, bool]:
    """Call Claude API and return response with success status."""
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=512,
            temperature=0.2,  # Low temperature for consistent outputs
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text, True
    except anthropic.AuthenticationError:
        return "❌ API Key ist ungültig", False
    except anthropic.RateLimitError:
        return "⏳ Rate Limit erreicht. Bitte kurz warten.", False
    except Exception as e:
        return f"❌ Fehler: {str(e)}", False

# Validation functions with strict checking
def validate_sentiment_fewshot(prompt: str, response: str) -> Tuple[bool, str]:
    """Validate that prompt contains few-shot examples and response is correct."""
    prompt_lower = prompt.lower()
    response_lower = response.lower()
    
    # Check for few-shot examples in prompt
    example_indicators = [
        "beispiel", "example", 
        "review:", "rezension:", 
        "sentiment:", "bewertung:"
    ]
    example_count = sum(1 for indicator in example_indicators if prompt_lower.count(indicator) >= 2)
    
    if example_count < 2:
        return False, "Dein Prompt enthält keine oder zu wenige Beispiele. Few-Shot Learning braucht mindestens 2-3 Beispiele!"
    
    # Check if positive/negative/neutral examples are present
    has_positive = any(word in prompt_lower for word in ["positiv", "positive", "gut"])
    has_negative = any(word in prompt_lower for word in ["negativ", "negative", "schlecht"])
    
    if not (has_positive and has_negative):
        return False, "Deine Beispiele sollten verschiedene Sentiment-Klassen zeigen (Positiv, Negativ, Neutral)"
    
    # Check response correctness
    if "positiv" in response_lower:
        return True, "Perfekt! Dein Few-Shot Prompt funktioniert und klassifiziert korrekt als Positiv."
    
    return False, "Die Klassifikation funktioniert noch nicht richtig. Stelle sicher, dass deine Beispiele klar und konsistent sind."

def validate_format_extraction(prompt: str, response: str) -> Tuple[bool, str]:
    """Validate structured data extraction."""
    response_lower = response.lower()
    
    # Check if prompt has examples
    if "beispiel" not in prompt.lower() and "example" not in prompt.lower():
        return False, "Verwende Few-Shot Learning mit Beispielen, um das gewünschte Format zu zeigen"
    
    # Check if response contains the required structured format
    required_fields = ["produkt:", "kategorie:", "preis:", "bewertung:"]
    found_fields = sum(1 for field in required_fields if field in response_lower)
    
    if found_fields < 3:
        return False, f"Das Output-Format ist nicht korrekt. Es sollten mindestens 3 strukturierte Felder extrahiert werden."
    
    # Check if the values are correctly extracted for the test case
    has_laptop = "laptop" in response_lower or "thinkpad" in response_lower
    has_price = "1200" in response or "1.200" in response or "€" in response
    
    if has_laptop and has_price:
        return True, "Ausgezeichnet! Die Datenextraktion funktioniert perfekt mit dem strukturierten Format."
    
    return False, "Die Extraktion ist noch nicht vollständig korrekt. Achte darauf, dass alle relevanten Informationen extrahiert werden."

def validate_xml_classification(prompt: str, response: str) -> Tuple[bool, str]:
    """Validate XML-based prompt structure and response."""
    # Check for XML tags in prompt
    xml_patterns = [
        r'<\w+>', r'</\w+>',  # Basic XML tags
        '<instruction', '<task', '<beispiel', '<example', '<data', '<text'
    ]
    
    xml_count = sum(1 for pattern in xml_patterns if re.search(pattern, prompt, re.IGNORECASE))
    
    if xml_count < 2:
        return False, "Verwende XML-Tags um deinen Prompt zu strukturieren (z.B. <instruction>, <examples>, <task>)"
    
    # Check if response has correct classification
    response_lower = response.lower()
    
    # Should identify as "Anfrage" or "Frage" or "Support-Anfrage"
    if any(word in response_lower for word in ["anfrage", "frage", "support", "hilfe", "problem"]):
        return True, "Super! Die XML-Strukturierung führt zur korrekten Klassifikation."
    
    return False, "Die Klassifikation ist noch nicht korrekt. Strukturiere deine Anweisungen und Beispiele klarer mit XML-Tags."

def validate_xml_complex(prompt: str, response: str) -> Tuple[bool, str]:
    """Validate complex XML structure with multiple sections."""
    # Check for multiple XML sections
    required_sections = ["<", ">", "</"]
    xml_tag_count = prompt.count("<") + prompt.count(">")
    
    if xml_tag_count < 8:  # At least 4 opening and 4 closing tags
        return False, "Dein Prompt braucht mehr XML-Struktur. Verwende verschiedene Sektionen für Kontext, Anforderungen, Format etc."
    
    # Check for semantic tag names
    good_tags = ["context", "requirements", "format", "output", "task", "instruction", "data", "anforderung", "ziel"]
    has_semantic_tags = sum(1 for tag in good_tags if tag in prompt.lower())
    
    if has_semantic_tags < 2:
        return False, "Verwende semantisch sinnvolle XML-Tag-Namen wie <context>, <requirements>, <format>"
    
    # Check response quality - should have structured analysis
    response_lower = response.lower()
    
    # Check for multiple analysis points
    analysis_indicators = ["trend", "muster", "empfehlung", "analyse", "insight", "wichtig", "haupt"]
    found_indicators = sum(1 for ind in analysis_indicators if ind in response_lower)
    
    if found_indicators >= 3:
        return True, "Exzellent! Deine XML-Struktur führt zu einer umfassenden, gut strukturierten Analyse."
    
    return False, "Die Analyse könnte strukturierter sein. Nutze XML-Tags um klare Anforderungen und Output-Format zu definieren."

def validate_zero_shot_cot(prompt: str, response: str) -> Tuple[bool, str]:
    """Validate Chain-of-Thought reasoning."""
    prompt_lower = prompt.lower()
    response_lower = response.lower()
    
    # Check for reasoning triggers in prompt
    cot_triggers = [
        "schritt für schritt", "step by step", "denk", "think",
        "erkläre", "explain", "zeige deine", "show your",
        "lass uns", "let's", "überlege", "reason"
    ]
    
    has_cot_trigger = any(trigger in prompt_lower for trigger in cot_triggers)
    
    if not has_cot_trigger:
        return False, "Füge eine Anweisung hinzu, die schrittweises Denken fördert (z.B. 'Denke Schritt für Schritt')"
    
    # Check response for step-by-step reasoning
    reasoning_indicators = [
        "erst", "zunächst", "dann", "schritt", "also", "daher",
        "1.", "2.", "3.", "daraus folgt", "bedeutet"
    ]
    
    reasoning_count = sum(1 for ind in reasoning_indicators if ind in response_lower)
    
    # Check if final answer is 4
    has_correct_answer = "4" in response and ("personen" in response_lower or "leute" in response_lower)
    
    if reasoning_count >= 3 and has_correct_answer:
        return True, "Perfekt! Der Chain-of-Thought Prompt führt zu klarem, schrittweisem Denken und der richtigen Antwort."
    elif reasoning_count >= 3:
        return False, "Gute Reasoning-Struktur, aber die Antwort ist noch nicht korrekt. Verfeinere die Anweisung."
    else:
        return False, "Der Output zeigt noch kein klares schrittweises Denken. Verstärke die CoT-Anweisung."

def validate_role_prompt(prompt: str, response: str) -> Tuple[bool, str]:
    """Validate role-based prompting."""
    prompt_lower = prompt.lower()
    
    # Check for role definition
    role_indicators = [
        "du bist", "sie sind", "agiere als", "act as", "rolle",
        "experte", "expert", "spezialist", "analyst", "berater"
    ]
    
    has_role = any(role in prompt_lower for role in role_indicators)
    
    if not has_role:
        return False, "Definiere eine spezifische Rolle oder Expertise (z.B. 'Du bist ein Datenanalyst...')"
    
    # Check response quality - should show expertise
    response_lower = response.lower()
    
    technical_terms = [
        "trend", "analyse", "daten", "muster", "korrelation",
        "insight", "statistik", "prozent", "wachstum", "rückgang"
    ]
    
    technical_count = sum(1 for term in technical_terms if term in response_lower)
    
    # Check for structured output
    has_structure = any(indicator in response for indicator in ["•", "-", "1.", "2.", ":", "**"])
    
    if technical_count >= 3 and has_structure:
        return True, "Ausgezeichnet! Die Rollendefinition führt zu einer professionellen, fachkundigen Analyse."
    elif technical_count >= 2:
        return False, "Die Analyse zeigt etwas Expertise, könnte aber noch präziser und strukturierter sein."
    else:
        return False, "Die Antwort zeigt noch nicht genug Fachexpertise. Verstärke die Rollendefinition."

# Enhanced exercise component
def exercise_box(
    exercise_id: str,
    title: str,
    description: str,
    task: str,
    initial_prompt: str,
    validation_func: Callable,
    solution_prompt: str,
    test_input: str,
    hints: list = None,
    concept: str = ""
):
    """Create an exercise box with enhanced features."""
    
    # Exercise header
    col1, col2 = st.columns([5, 1])
    with col1:
        st.subheader(f"{title}")
        if concept:
            st.caption(f"🎯 Konzept: {concept}")
    with col2:
        if st.session_state.exercise_status.get(exercise_id, False):
            st.markdown('<p class="success-prompt">✅ Gelöst!</p>', unsafe_allow_html=True)
    
    # Task description
    st.info(f"**📋 Aufgabe:** {task}")
    
    # Test case preview
    if test_input:
        with st.expander("🔍 Test-Eingabe anzeigen"):
            st.code(test_input, language="text")
    
    # Check if exercise is completed
    is_completed = st.session_state.exercise_status.get(exercise_id, False)
    
    # Prompt input
    user_prompt = st.text_area(
        "✏️ **Dein Prompt:**",
        value=initial_prompt,
        height=150,
        key=f"prompt_{exercise_id}",
        disabled=is_completed,
        help="Verbessere diesen Prompt, um die Aufgabe zu lösen"
    )
    
    # Action buttons in a row
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        test_disabled = not st.session_state.api_key or is_completed
        if st.button("🚀 Testen", key=f"test_{exercise_id}", disabled=test_disabled, type="primary"):
            st.session_state.show_response[exercise_id] = True
            st.session_state.show_hints[exercise_id] = False
            st.session_state.show_solution[exercise_id] = False
            
            # Call API
            with st.spinner("Teste deinen Prompt..."):
                full_prompt = user_prompt + "\n\n" + test_input if test_input else user_prompt
                response, success = call_claude(full_prompt, st.session_state.api_key)
                
                if success:
                    st.session_state.responses[exercise_id] = response
                    
                    # Validate
                    is_valid, feedback = validation_func(user_prompt, response)
                    
                    if is_valid:
                        st.session_state.exercise_status[exercise_id] = True
                        st.balloons()
                else:
                    st.session_state.responses[exercise_id] = response
    
    with col2:
        if hints and not is_completed:
            if st.button("💡 Hinweis", key=f"hint_{exercise_id}"):
                st.session_state.show_hints[exercise_id] = True
                st.session_state.show_response[exercise_id] = False
                st.session_state.show_solution[exercise_id] = False
    
    with col3:
        if st.button("👁️ Lösung", key=f"solution_{exercise_id}"):
            st.session_state.show_solution[exercise_id] = True
            st.session_state.show_response[exercise_id] = False
            st.session_state.show_hints[exercise_id] = False
    
    with col4:
        if description:
            if st.button("📖 Erklärung", key=f"explain_{exercise_id}"):
                st.session_state[f"show_explain_{exercise_id}"] = not st.session_state.get(f"show_explain_{exercise_id}", False)
    
    # Show explanation if requested
    if st.session_state.get(f"show_explain_{exercise_id}", False):
        with st.expander("📖 **Konzept-Erklärung**", expanded=True):
            st.markdown(description)
    
    # Display response if test was clicked
    if st.session_state.show_response.get(exercise_id, False) and exercise_id in st.session_state.responses:
        st.markdown("---")
        st.markdown("### 🤖 Claude's Antwort:")
        
        response = st.session_state.responses[exercise_id]
        
        # Check if completed
        if st.session_state.exercise_status.get(exercise_id, False):
            st.success("🎉 **Perfekt gelöst!**")
            is_valid, feedback = validation_func(user_prompt, response)
            st.markdown(f'<div class="success-prompt">{feedback}</div>', unsafe_allow_html=True)
        else:
            # Validate and show feedback
            is_valid, feedback = validation_func(user_prompt, response)
            st.markdown(f'<div class="error-feedback">💭 <b>Feedback:</b> {feedback}</div>', unsafe_allow_html=True)
        
        # Show response in a nice box
        st.markdown('<div class="response-box">', unsafe_allow_html=True)
        st.markdown(response)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Display hints if requested
    if st.session_state.show_hints.get(exercise_id, False) and hints:
        st.markdown("---")
        st.markdown("### 💡 Hinweise:")
        for i, hint in enumerate(hints, 1):
            st.markdown(f'<div class="hint-box">{i}. {hint}</div>', unsafe_allow_html=True)
    
    # Display solution if requested
    if st.session_state.show_solution.get(exercise_id, False):
        st.markdown("---")
        st.markdown("### 👁️ Beispiel-Lösung:")
        st.markdown('<div class="solution-box">', unsafe_allow_html=True)
        st.code(solution_prompt, language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        st.caption("💡 Versuche die Lösung zu verstehen und dann selbst zu formulieren!")
    
    st.markdown("---")

# Main content with tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Einführung", "🎯 Few-Shot Learning", "🏷️ XML Strukturierung", "🧠 Fortgeschrittene Techniken"])

# TAB 1: Introduction
with tab1:
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Willkommen zum Prompt Engineering Workshop!")
        
        st.markdown("""
        ### Was erwartet dich?
        
        In diesem interaktiven Workshop lernst du die wichtigsten Techniken des Prompt Engineering:
        
        1. **Few-Shot Learning** - Zeige der KI Beispiele für bessere Ergebnisse
        2. **XML-Strukturierung** - Organisiere komplexe Prompts übersichtlich
        3. **Chain-of-Thought** - Fördere schrittweises Denken
        4. **Role Prompting** - Definiere Expertise für bessere Outputs
        
        ### Wie funktioniert es?
        
        - Jede Übung startet mit einem **schlechten Prompt** ❌
        - Deine Aufgabe: **Verbessere den Prompt** ✨
        - **Teste** deinen Prompt mit der Claude API 🚀
        - Erhalte **direktes Feedback** und lerne aus den Lösungen 📚
        
        ### Warum ist das wichtig?
        
        Gute Prompts sind der Schlüssel zu:
        - **Präzisen Antworten** statt vager Ausgaben
        - **Konsistenten Ergebnissen** bei wiederholter Nutzung
        - **Effizienter KI-Nutzung** ohne endlose Nachfragen
        """)
        
    with col2:
        st.markdown("""
        ### 🎮 Spielregeln
        
        1. **Starte** mit dem Tab "Few-Shot Learning"
        2. **Lies** die Aufgabe genau
        3. **Verbessere** den vorgegebenen Prompt
        4. **Teste** mit echten Daten
        5. **Lerne** aus dem Feedback
        
        ### 🏆 Ziele
        
        - 🥉 **2 Übungen** = Bronze
        - 🥈 **4 Übungen** = Silber  
        - 🥇 **6 Übungen** = Gold
        
        ### ⚡ Quick Tips
        
        - Nutze die **Hinweise** wenn du feststeckst
        - Schau dir **Lösungen** zum Lernen an
        - **Experimentiere** mit Variationen
        """)
    
    st.info("💡 **Tipp:** Beginne mit 'Few-Shot Learning' und arbeite dich der Reihe nach durch die Übungen!")

# TAB 2: Few-Shot Learning
with tab2:
    st.header("🎯 Few-Shot Learning")
    
    st.markdown("""
    Few-Shot Learning bedeutet, der KI **konkrete Beispiele** zu zeigen, damit sie das gewünschte Muster versteht.
    Statt nur zu sagen "Klassifiziere dies", zeigst du ihr: "Hier sind 3 Beispiele, jetzt mach es genauso."
    """)
    
    # Exercise 1: Sentiment Classification with Few-Shot
    exercise_box(
        exercise_id="fs_sentiment",
        title="Übung 1: Sentiment-Analyse mit Beispielen",
        concept="Few-Shot Learning für Klassifikation",
        description="""
        **Few-Shot Learning** nutzt Beispiele um Muster zu vermitteln:
        
        ```
        Review: "Tolles Produkt!" → Sentiment: Positiv
        Review: "Enttäuschend." → Sentiment: Negativ
        Review: "Geht so." → Sentiment: Neutral
        
        Jetzt du: Review: "Fantastisch!" → ?
        ```
        
        Die KI lernt aus den Beispielen das Klassifikationsschema.
        """,
        task="Verwandle diesen vagen Prompt in einen Few-Shot Prompt mit mindestens 3 Beispielen für Sentiment-Analyse (Positiv/Negativ/Neutral).",
        initial_prompt="Was ist das Sentiment?",
        validation_func=validate_sentiment_fewshot,
        solution_prompt="""Klassifiziere das Sentiment der folgenden Rezensionen:

Beispiele:
Review: "Absolut brillant! Beste Investition ever!"
Sentiment: Positiv

Review: "Totaler Reinfall. Geldverschwendung."
Sentiment: Negativ

Review: "Funktioniert, nichts Besonderes."
Sentiment: Neutral

Review: "Schlechteste Qualität die ich je gesehen habe."
Sentiment: Negativ

Jetzt klassifiziere diese Review:""",
        test_input='Review: "Fantastische Qualität, sehr zufrieden!"',
        hints=[
            "Few-Shot Learning braucht mehrere Beispiele (mindestens 2-3)",
            "Zeige Beispiele für ALLE Kategorien (Positiv, Negativ, Neutral)",
            "Halte das Format konsistent: Review: '...' → Sentiment: ...",
            "Die Beispiele sollten eindeutig und klar sein"
        ]
    )
    
    # Exercise 2: Data Extraction with Few-Shot
    exercise_box(
        exercise_id="fs_extraction",
        title="Übung 2: Strukturierte Datenextraktion",
        concept="Few-Shot Learning für Format-Vorgabe",
        description="""
        **Format durch Beispiele zeigen:**
        
        Statt die Struktur zu erklären, zeige einfach wie das Ergebnis aussehen soll:
        
        ```
        Text: "iPhone 13 für 899€"
        Extraktion:
        Produkt: iPhone 13
        Preis: 899€
        ```
        
        So lernt die KI das gewünschte Output-Format.
        """,
        task="Erstelle einen Few-Shot Prompt, der aus Produktbeschreibungen strukturierte Daten (Produkt, Kategorie, Preis, etc.) extrahiert.",
        initial_prompt="Extrahiere die Informationen.",
        validation_func=validate_format_extraction,
        solution_prompt="""Extrahiere strukturierte Daten aus den folgenden Produktbeschreibungen:

Beispiel 1:
Text: "Das Samsung Galaxy S21 (Smartphone) kostet nur 799€ und hat eine Bewertung von 4.5 Sternen."
Extraktion:
Produkt: Samsung Galaxy S21
Kategorie: Smartphone
Preis: 799€
Bewertung: 4.5 Sterne

Beispiel 2:
Text: "MacBook Pro 14 Zoll, Laptop der Premiumklasse für 2499€, durchschnittlich 4.8 Sterne"
Extraktion:
Produkt: MacBook Pro 14 Zoll
Kategorie: Laptop
Preis: 2499€
Bewertung: 4.8 Sterne

Nun extrahiere aus diesem Text:""",
        test_input='Text: "Lenovo ThinkPad X1 Business-Laptop für nur 1200€, Top-Bewertung mit 4.7 Sternen"',
        hints=[
            "Zeige 2-3 Beispiele mit dem exakten Format, das du möchtest",
            "Jedes Beispiel sollte alle gewünschten Felder enthalten",
            "Konsistente Struktur: Gleiche Felder in gleicher Reihenfolge",
            "Verwende klare Feldnamen wie 'Produkt:', 'Preis:', etc."
        ]
    )

# TAB 3: XML Structuring
with tab3:
    st.header("🏷️ XML-Strukturierung")
    
    st.markdown("""
    XML-Tags helfen dabei, **komplexe Prompts zu organisieren** und verschiedene Abschnitte klar zu trennen.
    Dies macht Prompts übersichtlicher und präziser.
    """)
    
    # Exercise 3: Basic XML Structure
    exercise_box(
        exercise_id="xml_basic",
        title="Übung 3: Email-Klassifikation mit XML",
        concept="XML-Tags für klare Struktur",
        description="""
        **XML-Tags strukturieren deinen Prompt:**
        
        ```xml
        <instruction>
        Was die KI tun soll
        </instruction>
        
        <examples>
        Beispiele hier
        </examples>
        
        <task>
        Die eigentliche Aufgabe
        </task>
        ```
        
        Jeder Abschnitt hat seinen eigenen Zweck und ist klar getrennt.
