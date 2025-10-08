import streamlit as st
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
if 'show_hints' not in st.session_state:
    st.session_state.show_hints = {}
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# Custom CSS for better styling
st.markdown("""
<style>
.success-box {
    background-color: #d4edda;
    border: 2px solid #28a745;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
}
.stTextArea > div > div > textarea {
    font-family: 'Courier New', monospace;
}
.progress-container {
    background-color: #f0f0f0;
    border-radius: 10px;
    padding: 5px;
    margin: 10px 0;
}
.progress-bar {
    background-color: #28a745;
    height: 20px;
    border-radius: 5px;
    transition: width 0.3s ease;
}
.hint-box {
    background-color: #fff3cd;
    border: 1px solid #ffc107;
    border-radius: 5px;
    padding: 10px;
    margin: 10px 0;
}
</style>
""", unsafe_allow_html=True)

# Title and Introduction
st.title("🎓 Prompt Engineering Workshop")
st.markdown("### Lerne bessere Prompts mit Few-Shot Learning und XML Tags zu schreiben")

# Sidebar with API Key and Progress
with st.sidebar:
    st.header("⚙️ Konfiguration")
    
    # API Key Input
    api_key_input = st.text_input(
        "Claude API Key eingeben:",
        type="password",
        value=st.session_state.api_key,
        help="Dein API-Key wird nur für diese Session gespeichert"
    )
    
    if api_key_input:
        st.session_state.api_key = api_key_input
        # Test API key validity
        try:
            client = anthropic.Anthropic(api_key=api_key_input)
            # Quick test call with minimal tokens
            test_response = client.messages.create(
                model="claude-3-5-haiku-20241022",
                max_tokens=10,
                messages=[{"role": "user", "content": "Hi"}]
            )
            st.success("✅ API Key ist gültig!")
        except Exception as e:
            st.error(f"❌ API Key ungültig: {str(e)[:50]}...")
    else:
        st.warning("⚠️ Bitte API Key eingeben")
    
    # Progress Display
    st.header("📊 Fortschritt")
    total_exercises = 4
    completed = len([k for k, v in st.session_state.exercise_status.items() if v])
    progress = completed / total_exercises
    
    st.progress(progress)
    st.text(f"{completed}/{total_exercises} Übungen abgeschlossen")
    
    # Reset Button
    if st.button("🔄 Fortschritt zurücksetzen", type="secondary"):
        st.session_state.exercise_status = {}
        st.session_state.show_hints = {}
        st.session_state.responses = {}
        st.rerun()

# Helper function to call Claude API
def call_claude(prompt: str, api_key: str) -> Tuple[str, bool]:
    """Call Claude API and return response with success status."""
    try:
        client = anthropic.Anthropic(api_key=api_key)
        message = client.messages.create(
            model="claude-3-5-haiku-20241022",
            max_tokens=512,
            temperature=0.3,  # Lower temperature for more consistent outputs
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text, True
    except anthropic.AuthenticationError:
        return "Fehler: API Key ist ungültig", False
    except anthropic.RateLimitError:
        return "Fehler: Rate Limit erreicht. Bitte kurz warten.", False
    except Exception as e:
        return f"Fehler: {str(e)}", False

# Validation functions with detailed feedback
def validate_sentiment(response: str) -> Tuple[bool, str]:
    """Validate sentiment classification response."""
    response_lower = response.lower()
    
    sentiments = ["positive", "positiv", "negative", "negativ", "neutral"]
    found = any(sentiment in response_lower for sentiment in sentiments)
    
    if not found:
        return False, "Der Output enthält keine klare Sentiment-Klassifikation (Positive/Negative/Neutral)"
    
    # Check if it's correctly classified as positive for the test case
    if "positive" in response_lower or "positiv" in response_lower:
        return True, "Perfekt! Die Sentiment-Klassifikation funktioniert."
    
    return False, "Die Klassifikation ist vorhanden, aber nicht korrekt für dieses Beispiel"

def validate_multi_label(response: str) -> Tuple[bool, str]:
    """Validate multi-label classification response."""
    response_lower = response.lower()
    
    categories = {
        "technical": ["technical", "technisch", "software", "bug"],
        "pricing": ["pricing", "preis", "price", "expensive", "teuer"],
        "customer_service": ["customer service", "support", "kundenservice"],
        "delivery": ["delivery", "shipping", "versand", "lieferung"]
    }
    
    found_categories = []
    for category, keywords in categories.items():
        if any(keyword in response_lower for keyword in keywords):
            found_categories.append(category)
    
    if len(found_categories) < 2:
        return False, f"Nur {len(found_categories)} Kategorie(n) gefunden. Es sollten mindestens 2 identifiziert werden."
    
    # For the test case, should find technical and pricing
    if "technical" in found_categories and "pricing" in found_categories:
        return True, "Ausgezeichnet! Alle relevanten Kategorien wurden erkannt."
    
    return False, f"Kategorien gefunden, aber nicht die korrekten für dieses Beispiel"

def validate_xml_basic(prompt: str) -> Tuple[bool, str]:
    """Validate basic XML structure in prompt."""
    xml_tags = ["<instruction>", "<article>", "<text>", "<content>", "<task>"]
    found_tags = [tag for tag in xml_tags if tag in prompt]
    
    if len(found_tags) == 0:
        return False, "Keine XML-Tags gefunden. Verwende Tags wie <instruction> und <article>"
    elif len(found_tags) == 1:
        return False, "Nur ein XML-Tag gefunden. Trenne Anweisung und Inhalt mit verschiedenen Tags"
    
    return True, "Super! Die XML-Struktur ist korrekt."

def validate_xml_advanced(prompt: str) -> Tuple[bool, str]:
    """Validate advanced XML structure."""
    required_sections = [
        ("<customer", "Kundendaten"),
        ("<analysis", "Analyse-Anforderungen"),
        ("<output", "Output-Format")
    ]
    
    missing = []
    for tag, description in required_sections:
        if tag not in prompt.lower():
            missing.append(description)
    
    if missing:
        return False, f"Folgende Sektionen fehlen: {', '.join(missing)}"
    
    return True, "Exzellent! Alle erforderlichen XML-Sektionen sind vorhanden."

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
    hints: list = None
):
    """Create an exercise box with enhanced features."""
    
    # Exercise header with completion status
    col1, col2 = st.columns([5, 1])
    with col1:
        st.subheader(title)
    with col2:
        if st.session_state.exercise_status.get(exercise_id, False):
            st.success("✅ Gelöst")
    
    st.markdown(description)
    
    # Task description
    with st.expander("📋 **Aufgabe**", expanded=True):
        st.info(task)
        if test_input:
            st.code(test_input, language="text")
    
    # Check if exercise is completed
    is_completed = st.session_state.exercise_status.get(exercise_id, False)
    
    # Prompt input with syntax highlighting hint
    prompt_label = "Dein Prompt:" if not is_completed else "Dein Prompt (Gelöst):"
    user_prompt = st.text_area(
        prompt_label,
        value=initial_prompt,
        height=200,
        key=f"prompt_{exercise_id}",
        disabled=is_completed,
        help="Tipp: Verwende die Beispiele aus der Erklärung als Vorlage"
    )
    
    # Action buttons
    col1, col2, col3 = st.columns([2, 2, 2])
    
    with col1:
        if st.button(
            "🚀 Prompt testen", 
            key=f"test_{exercise_id}",
            disabled=not st.session_state.api_key or is_completed,
            type="primary"
        ):
            if st.session_state.api_key:
                with st.spinner("Teste deinen Prompt..."):
                    # Combine user prompt with test input
                    full_prompt = user_prompt + "\n\n" + test_input if test_input else user_prompt
                    
                    # Call Claude API
                    response, success = call_claude(full_prompt, st.session_state.api_key)
                    
                    if success:
                        # Store response
                        st.session_state.responses[exercise_id] = response
                        
                        # Display response
                        st.markdown("**Claude's Antwort:**")
                        st.info(response)
                        
                        # Validate - check both prompt structure and response
                        if "xml" in exercise_id:
                            # For XML exercises, validate the prompt structure
                            is_valid, feedback = validation_func(user_prompt)
                        else:
                            # For other exercises, validate the response
                            is_valid, feedback = validation_func(response)
                        
                        if is_valid:
                            st.success(f"🎉 {feedback}")
                            st.session_state.exercise_status[exercise_id] = True
                            st.balloons()
                            st.rerun()
                        else:
                            st.error(f"❌ {feedback}")
                            st.warning("💡 Versuche deinen Prompt basierend auf dem Feedback zu verbessern.")
                    else:
                        st.error(response)
    
    with col2:
        # Hint system
        if hints and not is_completed:
            if st.button("💡 Hinweis", key=f"hint_{exercise_id}"):
                st.session_state.show_hints[exercise_id] = True
            
            if st.session_state.show_hints.get(exercise_id, False):
                with st.container():
                    st.markdown("**Hinweise:**")
                    for i, hint in enumerate(hints, 1):
                        st.warning(f"{i}. {hint}")
    
    with col3:
        if st.button("👁️ Lösung zeigen", key=f"solution_{exercise_id}"):
            st.markdown("**Beispiel-Lösung:**")
            st.code(solution_prompt, language="text")
            st.info("📝 Versuche die Lösung zu verstehen und dann selbst zu schreiben!")
    
    st.markdown("---")

# Main content with tabs
tab1, tab2, tab3 = st.tabs(["📚 Einführung", "🎯 Few-Shot Learning", "🏷️ XML Tags"])

# TAB 1: Introduction
with tab1:
    st.header("Willkommen zum Prompt Engineering Workshop!")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Was ist Prompt Engineering?
        
        Prompt Engineering ist die Kunst, präzise und effektive Anweisungen an KI-Modelle zu formulieren.
        Ein gut strukturierter Prompt kann den Unterschied zwischen einer vagen und einer perfekten Antwort ausmachen.
        
        ### Warum ist es wichtig?
        
        - **Bessere Ergebnisse**: Präzise Prompts führen zu genaueren Antworten
        - **Zeitersparnis**: Weniger Nachfragen und Korrekturen nötig
        - **Konsistenz**: Strukturierte Prompts liefern vorhersagbare Outputs
        """)
    
    with col2:
        st.markdown("""
        ### Was du heute lernst:
        
        #### 1. Few-Shot Learning
        Zeige der KI Beispiele, damit sie das Muster versteht
        
        #### 2. XML Tags
        Strukturiere komplexe Prompts mit klaren Abschnitten
        
        ### Wie funktioniert der Workshop?
        
        1. **Lies die Erklärung** zu jedem Konzept
        2. **Löse die interaktiven Übungen**
        3. **Nutze Hinweise**, wenn du nicht weiterkommst
        4. **Vergleiche mit der Lösung** zum Lernen
        """)
    
    st.info("💡 **Tipp**: Beginne mit dem Tab 'Few-Shot Learning' und arbeite dich der Reihe nach durch!")

# TAB 2: Few-Shot Learning
with tab2:
    st.header("Few-Shot Learning")
    
    with st.expander("📖 **Konzept-Erklärung**", expanded=True):
        st.markdown("""
        ### Was ist Few-Shot Learning?
        
        Few-Shot Learning bedeutet, der KI **einige Beispiele** zu zeigen, bevor du ihr die eigentliche Aufgabe gibst.
        Die KI lernt aus diesen Beispielen das gewünschte Muster und wendet es auf neue Eingaben an.
        
        ### Warum funktioniert das?
        
        KI-Modelle sind sehr gut darin, Muster zu erkennen. Wenn du ihnen zeigst:
        - **Input → Output** (mehrmals)
        - Dann verstehen sie: **Neuer Input → ?** (gleiches Muster anwenden)
        
        ### Beispiel-Struktur:
        
        ```
        Beispiel 1: "Ich liebe dieses Produkt!" → Sentiment: Positiv
        Beispiel 2: "Totaler Müll!" → Sentiment: Negativ
        Beispiel 3: "Geht so." → Sentiment: Neutral
        
        Aufgabe: "Super Qualität!" → ?
        ```
        
        ### Best Practices:
        
        1. **Verwende 2-5 Beispiele** (zu viele können verwirren)
        2. **Beispiele sollten vielfältig sein** (verschiedene Fälle abdecken)
        3. **Konsistentes Format** (gleiche Struktur für alle Beispiele)
        4. **Klare Trennung** zwischen Beispielen und der eigentlichen Aufgabe
        """)
    
    st.markdown("### 🎯 Übungen")
    
    # Exercise 1: Basic Few-Shot
    exercise_box(
        exercise_id="fs_basic",
        title="Übung 1: Einfache Sentiment-Analyse",
        description="Verbessere den Prompt so, dass Claude Kundenrezensionen korrekt als Positiv, Negativ oder Neutral klassifiziert.",
        task="Der Prompt soll so angepasst werden, dass Claude die Rezension 'Great quality and fast shipping!' korrekt als positiv klassifiziert. Verwende Few-Shot Learning mit mindestens 2 Beispielen.",
        initial_prompt="Klassifiziere diese Rezension.",
        validation_func=validate_sentiment,
        solution_prompt="""Hier sind Beispiele für Rezensions-Klassifikationen:

Rezension: "Absolut fantastisch! Würde ich wieder kaufen."
Sentiment: Positiv

Rezension: "Schlechteste Qualität die ich je gesehen habe."
Sentiment: Negativ

Rezension: "Okay, nichts Besonderes."
Sentiment: Neutral

Klassifiziere nun diese Rezension:""",
        test_input='Rezension: "Great quality and fast shipping!"',
        hints=[
            "Zeige Claude mindestens 2-3 Beispiele von Rezensionen mit ihrer Klassifikation",
            "Verwende ein konsistentes Format: Rezension: '...' → Sentiment: ...",
            "Stelle sicher, dass du Beispiele für Positiv, Negativ und Neutral gibst"
        ]
    )
    
    # Exercise 2: Advanced Few-Shot
    exercise_box(
        exercise_id="fs_advanced",
        title="Übung 2: Multi-Label Klassifikation",
        description="Erstelle einen Prompt, der ALLE relevanten Kategorien in Kundenfeedback identifiziert.",
        task="Das Feedback 'The software is buggy and overpriced. Support team was unhelpful.' soll in die Kategorien Technical, Pricing und Customer Service klassifiziert werden. Nutze Few-Shot Learning um das Muster zu zeigen.",
        initial_prompt="Was ist das Thema dieses Feedbacks?",
        validation_func=validate_multi_label,
        solution_prompt="""Identifiziere alle relevanten Kategorien für Kundenfeedback.
Mögliche Kategorien: Technical, Pricing, Customer Service, Delivery

Beispiele:

Feedback: "Die App stürzt ständig ab und der Support antwortet nicht."
Kategorien: Technical, Customer Service

Feedback: "Zu teuer für die gebotene Qualität. Lieferung dauerte ewig."
Kategorien: Pricing, Delivery

Feedback: "Installation war kompliziert, aber der Support war sehr hilfreich."
Kategorien: Technical, Customer Service

Analysiere dieses Feedback:""",
        test_input='Feedback: "The software is buggy and overpriced. Support team was unhelpful."',
        hints=[
            "Zeige Beispiele, die mehrere Kategorien gleichzeitig haben",
            "Liste alle möglichen Kategorien am Anfang auf",
            "Verwende klare Beispiele, die zeigen, dass mehrere Labels möglich sind"
        ]
    )

# TAB 3: XML Tags
with tab3:
    st.header("XML Tags für strukturierte Prompts")
    
    with st.expander("📖 **Konzept-Erklärung**", expanded=True):
        st.markdown("""
        ### Warum XML Tags verwenden?
        
        XML Tags helfen dabei, **komplexe Prompts zu strukturieren** und verschiedene Teile klar voneinander zu trennen.
        Das macht deine Prompts:
        - **Übersichtlicher** (für dich und die KI)
        - **Eindeutiger** (keine Verwechslungen möglich)
        - **Wiederverwendbar** (Template-Struktur)
        
        ### Basis-Struktur:
        
        ```xml
        <instruction>
        Hier steht, WAS die KI tun soll
        </instruction>
        
        <context>
        Hier steht der Kontext oder Hintergrund
        </context>
        
        <data>
        Hier stehen die zu verarbeitenden Daten
        </data>
        
        <format>
        Hier steht, WIE die Ausgabe aussehen soll
        </format>
        ```
        
        ### Vorteile gegenüber unstrukturierten Prompts:
        
        **Ohne XML:**
        "Analysiere diesen Text über Klimawandel und fasse ihn in 3 Punkten zusammen. Der Text ist: Der Klimawandel..."
        
        **Mit XML:**
        ```xml
        <instruction>
        Analysiere den folgenden Text und erstelle eine Zusammenfassung
        </instruction>
        
        <requirements>
        - Genau 3 Hauptpunkte
        - Jeder Punkt maximal 1 Satz
        </requirements>
        
        <text>
        Der Klimawandel...
        </text>
        ```
        
        ### Best Practices:
        
        1. **Semantische Tag-Namen**: Verwende beschreibende Namen wie `<customer_data>` statt `<data1>`
        2. **Hierarchie beachten**: Verschachtele Tags logisch
        3. **Konsistenz**: Verwende immer das gleiche Schema für ähnliche Aufgaben
        4. **Closing Tags**: Vergiss nie die schließenden Tags!
        """)
    
    st.markdown("### 🎯 Übungen")
    
    # Exercise 3: Basic XML
    exercise_box(
        exercise_id="xml_basic",
        title="Übung 3: Grundlegende XML-Strukturierung",
        description="Strukturiere einen Prompt mit XML-Tags, um Anweisung und Inhalt klar zu trennen.",
        task="Verwende XML-Tags um die Zusammenfassungs-Anweisung vom zu zusammenfassenden Artikel zu trennen. Die Tags sollten semantisch sinnvoll benannt sein.",
        initial_prompt="Fasse diesen Artikel zusammen: Der Klimawandel beeinflusst globale Temperaturen und Wettermuster. Die Durchschnittstemperatur steigt kontinuierlich an.",
        validation_func=validate_xml_basic,
        solution_prompt="""<instruction>
Erstelle eine prägnante Zusammenfassung des folgenden Artikels in 2-3 Sätzen.
</instruction>

<article>
Der Klimawandel beeinflusst globale Temperaturen und Wettermuster. Die Durchschnittstemperatur steigt kontinuierlich an.
</article>""",
        test_input="",
        hints=[
            "Trenne die Anweisung (was zu tun ist) vom Inhalt (der Artikel)",
            "Verwende semantische Tag-Namen wie <instruction> und <article>",
            "Schließe alle geöffneten Tags ordnungsgemäß"
        ]
    )
    
    # Exercise 4: Advanced XML
    exercise_box(
        exercise_id="xml_advanced",
        title="Übung 4: Komplexe Multi-Section Struktur",
        description="Erstelle eine komplexe Prompt-Struktur mit mehreren XML-Sektionen für eine Kundenanalyse.",
        task="Strukturiere eine Kundenanalyse-Anfrage mit separaten Sektionen für Kundendaten, Analyse-Anforderungen und Output-Format. Verwende mindestens 3 verschiedene XML-Tag-Paare.",
        initial_prompt="Analysiere diesen Kunden: Max Müller, 35 Jahre, hat 5 Elektronik-Artikel gekauft. Erkläre sein Kaufverhalten und schlage Produkte vor. Mach eine Liste.",
        validation_func=validate_xml_advanced,
        solution_prompt="""<customer_data>
Name: Max Müller
Alter: 35 Jahre
Kaufhistorie: 5 Artikel in der Elektronik-Kategorie
Kunde seit: 2022
</customer_data>

<analysis_requirements>
1. Kaufverhalten-Muster identifizieren
2. Kundensegment bestimmen
3. Zukünftige Kaufwahrscheinlichkeiten einschätzen
4. Passende Produktempfehlungen generieren
</analysis_requirements>

<output_format>
Strukturiere deine Analyse wie folgt:
- Kundenprofil (1 Absatz)
- Verhaltensanalyse (Stichpunkte)
- Produktempfehlungen (nummerierte Liste mit Begründung)
- Handlungsempfehlung für Marketing
</output_format>""",
        test_input="",
        hints=[
            "Erstelle separate Sektionen für Daten, Anforderungen und Format",
            "Verwende beschreibende Tag-Namen wie <customer_data>, <analysis_requirements>",
            "Strukturiere auch innerhalb der Tags mit Listen oder Unterpunkten",
            "Denke an alle drei Hauptbereiche: Input-Daten, Was analysiert werden soll, Wie das Ergebnis aussehen soll"
        ]
    )

# Footer
st.markdown("---")
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown("""
    <div style='text-align: center; color: #666;'>
        <p><strong>Prompt Engineering Workshop</strong></p>
        <p>Erstellt für die KI & Kreativität Vorlesung</p>
        <p>Powered by Claude API & Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

# Debug info (only in development)
if st.checkbox("🔧 Debug-Modus", value=False):
    st.json({
        "API Key gesetzt": bool(st.session_state.api_key),
        "Gelöste Übungen": st.session_state.exercise_status,
        "Angezeigte Hinweise": st.session_state.show_hints,
    })
