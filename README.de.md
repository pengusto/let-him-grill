# Let Him Grill

[English](README.md) · **Deutsch**

**Stoppe das Babysitten von Codex. Lass es umkehrbare Entscheidungen lösen und
dich unterbrechen, wenn dein Urteil das Ergebnis verändert.**

Coding-Agenten stoppen oft für Entscheidungen, die sie sicher selbst treffen
könnten. Let Him Grill untersucht Repository und Dokumentation, empfiehlt und
löst risikoarme, umkehrbare Optionen, hält den Entscheidungspfad fest und
stoppt bei Architektur-, Produkt-, Sicherheits-, Kosten- und anderen
wesentlichen Human-Gates.

## Demo

![Let Him Grill löst fünf umkehrbare Entscheidungen, stoppt an einem Human-Gate und hält den aktuellen Pfad nach der Neubewertung bereit.](docs/demo-poster.png)

Sechs Entscheidungen bewertet · fünf autonom gelöst · ein Human-Gate. Vergleiche
den [Ausgangszustand](docs/demo.png) mit dem [Poster nach der Neubewertung](docs/demo-poster.png)
lies die [dokumentierte Neubewertung eines Zweigs](docs/examples/feature-planning/reassessment.md)
oder öffne ein [vollständiges portables Entscheidungsartefakt](docs/examples/README.md).

Das ist keine pauschale `continue autonomously`-Anweisung. Let Him Grill legt
eine Entscheidungsgrenze fest, hält die portable Source of Truth in
`.grill/decisions.json` und erklärt abhängige Zweige ungültig, wenn sich eine
frühere Auswahl ändert.

## Installation

```bash
npx skills add pengusto/let-him-grill -g -a codex -y
```

Starte nach der Installation einen neuen Codex-Task und rufe anschließend
`$let-him-grill` auf.

## Vorher und nachher

In fünf skriptgesteuerten paarweisen Planungsdurchläufen sank die mediane Zeit
bis zu einem nutzbaren Plan von 455 auf 54 Sekunden. Die finalen Pläne von Let
Him Grill zeigten sieben normalisierte wesentliche menschliche
Entscheidungspunkte und stellten eine unmittelbar zu beantwortende Frage. Siehe
[Protokoll, Rohtranskripte und Einschränkungen](docs/benchmark/RESULTS.md). Die
Zeitmessung enthält Codex-Ausführung und Benchmark-Controller-Latenz; sie ist
Produktnachweis, kein kontrollierter Modell-Performance-Benchmark.

Die [Clean-Install-Validierung](docs/validation/cross-agent-install/README.md)
dokumentiert Codex-Erkennung und Resume-Verhalten sowie die Claude-
Paketinstallation; ein echter Claude-Aufruf bleibt unbestätigt.

## Warum nicht einfach „continue autonomously“ sagen?

Diese Anweisung sagt dem Agenten, weiterzumachen, aber nicht, wann er stoppen
oder wie er nach einer geänderten früheren Auswahl fortfahren soll. Let Him
Grill macht die Grenzen explizit: Entscheidungen werden klassifiziert,
risikoarme umkehrbare Optionen automatisch gelöst, echte Human-Gates bleiben
beim Menschen und der portable Zustand kann in einem späteren Task fortgesetzt
werden.

## Funktionsweise

![Übersicht im Excalidraw-Stil über den Entscheidungs- und Darstellungsworkflow von Let Him Grill und Codex.](docs/how-it-works.svg)

- untersucht Repository-Code und Dokumentation, bevor Fragen gestellt werden
- empfiehlt für jede echte Entscheidung eine Antwort
- bewertet jede Option nach Eignung, Risiko, Aufwand und Umkehrbarkeit
- trifft umkehrbare Entscheidungen mit geringem Risiko automatisch
- stoppt bei Architektur-, Produkt-, Sicherheits-, Kosten- und anderen
  menschlichen Entscheidungspunkten
- erklärt abhängige Entscheidungen für ungültig, wenn sich eine frühere Auswahl
  ändert
- unterstützt kompakte Textausgabe und einen dauerhaften interaktiven
  Entscheidungsbaum

## Manuelle Installation

Nutze Git als Ausweichlösung, wenn die `skills`-CLI nicht verfügbar ist. Beide
Modi verwenden dieselbe Installation; der Modus wird beim Aufruf des Skills
gewählt.

### Globale Installation

Für den aktuellen Benutzer in jedem Codex-Projekt verfügbar:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/pengusto/let-him-grill.git \
  ~/.agents/skills/let-him-grill
```

PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
git clone https://github.com/pengusto/let-him-grill.git `
  "$HOME\.agents\skills\let-him-grill"
```

### Projektlokale Installation

Versioniere den Skill zusammen mit einem Repository:

```bash
mkdir -p .agents/skills
git submodule add https://github.com/pengusto/let-him-grill.git \
  .agents/skills/let-him-grill
```

Starte nach der Installation einen neuen Codex-Task, damit der Skill erkannt
wird.

## Verwendung

### Kompaktmodus

Textorientiert. Status und Visualisierung werden nur erstellt, wenn sie durch
Verzweigungen oder erneut betrachtete Entscheidungen nützlich werden.

```text
Nutze $let-him-grill im Kompaktmodus, um diesen Plan einem Stresstest zu
unterziehen. Fahre autonom fort, bis meine Entscheidung erforderlich ist.
```

### Visueller Modus

Speichert Entscheidungen in `.grill/decisions.json` und zeigt den interaktiven
Baum an menschlichen Entscheidungspunkten sowie nach Änderungen.

```text
Nutze $let-him-grill im visuellen Modus, um diesen Plan einem Stresstest zu
unterziehen. Fahre autonom fort, bis meine Entscheidung erforderlich ist.
```

Der visuelle Modus verwendet nach Möglichkeit das Python-Backend aus der
Standardbibliothek und weicht andernfalls auf native Datei- und
Visualisierungswerkzeuge von Codex aus. Beide Backends befüllen dieselbe
mitgelieferte HTML-Vorlage, sodass die Oberfläche unabhängig vom Renderer
gleich bleibt. Explizite Auswahl:

```text
Nutze $let-him-grill im visuellen Modus mit dem Python-Backend.
```

```text
Nutze $let-him-grill im visuellen Modus mit dem nativen Codex-Fallback. Verwende
weder Python noch eine andere Laufzeitumgebung.
```

Codex zeigt vor der ersten Entscheidung `Visual mode · Python backend` oder
`Visual mode · Native Codex fallback` an.

### Entscheidungsartefakt fortsetzen

`.grill/decisions.json` ist die portable Source of Truth. In einem späteren
Task mit installiertem Let Him Grill kann der Agent diese Datei fortsetzen. Das
Python-Backend ermittelt die nächste Aktion deterministisch und ohne den Zustand
zu verändern:

```bash
python3 <skill-dir>/scripts/decision_state.py resume .grill/decisions.json
```

Beim Fortsetzen werden vorläufige KI-Entscheidungen gegen den aktuellen
Projektstand geprüft, widersprochene oder ungültige Zweige neu bewertet und der
Lauf autonom bis zum nächsten Human-Gate fortgeführt. HTML- und Markdown-Exporte
sind abgeleitete Ansichten und werden im neuen Workspace neu erzeugt.

### Automatische Modusauswahl

```text
Nutze $let-him-grill im am besten geeigneten Modus, um diesen Plan einem
Stresstest zu unterziehen, bis meine Entscheidung erforderlich ist.
```

Codex wählt den Kompaktmodus für kurze lineare Diskussionen und den visuellen
Modus für verzweigte oder erneut betrachtete Entscheidungen. Der gewählte Modus
wird einmal genannt. Ein Wechsel ist jederzeit möglich.

### Herunterladbare Referenzartefakte

Drei vollständige Bundles enthalten Startprompt, portablen JSON-Zustand,
interaktiven Baum, Markdown-Handoff und eine dokumentierte Neubewertung eines
Zweigs:

- [Feature-Planung](docs/examples/feature-planning/README.md)
- [Softwarearchitektur](docs/examples/software-architecture/README.md)
- [Release-Bereitschaft](docs/examples/release-readiness/README.md)

### Beispiel-Prompts

#### Finanzen

`Nutze $let-him-grill, um einen Budgetierungs- und Berichtsansatz für unser
SaaS-Unternehmen auszuwählen. Stoppe vor Compliance- oder Ausgabenentscheidungen.`

Beispielentscheidungen: finanzielle Priorität, Prognoserhythmus und
Ausgabenfreigaben.

![Finanzbeispiel mit Entscheidungen zu Runway, Prognosen und Freigabekontrollen.](docs/finance-example.png)

#### Softwarearchitektur

`Nutze $let-him-grill, um zu entscheiden, ob dieses B2B-Produkt als modularer
Monolith oder mit getrennten Services starten soll. Stoppe bei wesentlichen
Skalierungs- oder Verantwortungsabwägungen.`

Beispielentscheidungen: Systemstruktur, API-Verträge und Auslieferungsprozess.

![Beispiel für Softwarearchitektur mit Entscheidungen zu Systemstruktur, API-Verträgen und Auslieferung.](docs/software-architecture-example.png)

#### KI-Training

`Nutze $let-him-grill, um einen Trainingsworkflow für ein domänenspezifisches
Modell zu planen. Stoppe bei Datenschutz-, Lizenz- oder Budgetfragen.`

Beispielentscheidungen: messbares Ziel, Verwaltung der Evaluationsdaten und die
erste zu testende Anpassungsmethode.

![Beispiel für KI-Training mit Entscheidungen zu Zielen, Evaluationsdaten und Anpassungsmethoden.](docs/ai-training-example.png)

#### Spieleentwicklung

`Nutze $let-him-grill, um das Speichersystem und den Mehrspielerumfang dieses
Spielprototyps festzulegen. Stoppe, wenn Plattform-, Netzwerk- oder
Spielerlebnisziele voneinander abweichen.`

Beispielentscheidungen: zentrale Spielschleife, Speicherformat und Zeitpunkt
für den Mehrspielermodus.

![Beispiel für Spieleentwicklung mit Entscheidungen zu Spielschleife, Speicherständen und Mehrspielermodus.](docs/game-development-example.png)

#### Sprachtraining

`Nutze $let-him-grill, um einen zwölfwöchigen Sprachtrainingsplan zu erstellen.
Fahre fort, bis Motivation, Zertifizierung oder berufliche Prioritäten mein
Urteil erfordern.`

Beispielentscheidungen: primäres Lernziel, wöchentlicher Übungsrhythmus und
Zeitpunkt der Korrektur bei Sprechübungen.

![Beispiel für Sprachtraining mit Entscheidungen zu Zielen, Übungsplänen und Korrekturzeitpunkten.](docs/language-training-example.png)

#### Infrastruktur und Sicherheit

`Nutze $let-him-grill, um Deployment, Authentifizierung, Backups und
Beobachtbarkeit für dieses interne Portal auszuwählen. Stoppe, bevor
Sicherheitsrisiken oder laufende Kosten akzeptiert werden.`

Beispielentscheidungen: Deployment-Ziel, Mitarbeiterauthentifizierung und vor
dem Start erforderliche Wiederherstellungsnachweise.

![Beispiel für Infrastruktur und Sicherheit mit Entscheidungen zu Hosting, Authentifizierung und Wiederherstellung.](docs/infrastructure-security-example.png)

### Abschluss des Grills

Sobald ein gemeinsames Verständnis erreicht ist, fasst Codex bestätigte
menschliche Entscheidungen, vorläufige KI-Entscheidungen, Annahmen, verbleibende
Risiken oder Blocker sowie den geordneten Implementierungsplan zusammen. Vor der
Implementierung wird eine Bestätigung eingeholt.

Nach der Bestätigung aktualisiert Codex ein bestehendes maßgebliches Planungs-,
Spezifikations- oder Entscheidungsdokument, sofern das Repository bereits eines
verwendet oder Dokumentation angefordert wurde. Standardmäßig wird keine
doppelte Plandatei erstellt.

## Sicherheit und Voraussetzungen

- Codex mit Skill-Unterstützung
- Node.js mit `npx` für den primären Installationsbefehl
- Git nur für die manuelle Installation als Ausweichlösung
- Python 3 empfohlen für deterministische visuelle Statusaktualisierungen
- keine virtuelle Umgebung, kein `pip install`, kein Server und kein
  Netzwerkdienst

Let Him Grill erweitert die Begleit-Skills `grilling` und `domain-modeling`; sie
werden weder mitgeliefert noch verändert. Die Clean-Install-Nachweise prüfen
Erkennung und portablen Zustand dieses Repositorys, nicht jede Live-Kombination
aus Begleit-Skills und Host-Runtime.

Der Kompaktmodus funktioniert ohne Python. Der native visuelle Fallback wendet
über die Codex-Dateiwerkzeuge dieselben Status- und Invalidierungsregeln an,
bietet aber nicht die ausführbare Validierung des Python-Backends. Hosts ohne
Unterstützung für eingebettete Visualisierungen geben dieselben
Entscheidungsinhalte als Text aus.

## Aktualisierung

Globale Installation:

```bash
git -C ~/.agents/skills/let-him-grill pull --ff-only
```

Projektlokales Submodul:

```bash
git submodule update --remote --merge \
  .agents/skills/let-him-grill
```

## Entwicklung

```bash
python3 scripts/test_decision_state.py
```

Die Status-Engine verwendet ausschließlich die Python-Standardbibliothek.
Siehe [Roadmap](docs/ROADMAP.md) für den Start und weitere Arbeiten.
Benutzerrelevante Änderungen werden im [Changelog](CHANGELOG.md) dokumentiert.

## Namensnennung

Inspiriert von Matt Pococks
[Grill with Docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs)-Workflow.
Let Him Grill ist ein unabhängiges Projekt und weder mit Matt Pocock noch mit
OpenAI verbunden oder von ihnen unterstützt.

## Lizenz

[MIT](LICENSE)
