---
layout: post
title: Research Spotlight: How University Science Powers Your Classroom with Cell Collective
date: 2025-12-01
categories: [Behind the Science]
image: /assets/images/week5-hero.jpg
author: Dr. Marie & Charles Martin
excerpt: University research doesn’t just live in journals—it can supercharge your NGSS-aligned lessons tomorrow. See how Cell Collective’s peer-reviewed models bring real science to student hands.
---

If you’ve ever wondered, “Can I really trust this simulation?” this post is for you. Today we pull back the curtain on the university research behind Cell Collective—the modeling platform that lets students develop and use real biological models in minutes, not months. You’ll see exactly how academic research validates the classroom tools you use, what “research-validated” actually means, and how to run a ready-to-teach, NGSS-aligned mini-lesson with a peer-reviewed model tomorrow.

Section 1: The research engine behind Cell Collective
- Who builds Cell Collective? Cell Collective originated in the lab of Dr. Tomáš Helikar at the University of Nebraska–Lincoln (UNL). For more than 15 years, the Helikar group and collaborators have advanced logic-based, network-level modeling of biological systems and made those capabilities accessible through Cell Collective.
- How deep is the research base? The platform is grounded in 50+ peer-reviewed publications spanning systems biology, computational modeling, immunology and cell signaling, and biology education research. That means the methods, models, and learning applications have all been examined by the scientific community.
- What kinds of problems do these models address? Published Cell Collective models have been used to study:
  - Immune signaling (e.g., T cell activation networks)
  - Cell fate decisions (e.g., apoptosis pathways)
  - Growth factor signaling (e.g., EGFR/MAPK pathway dynamics)
  - Cell cycle regulation
  - Metabolic switches and stress responses
  - Microbial signaling and host–pathogen interactions
- Why this matters to K–12: When you open a public model in Cell Collective, you’re not launching a cartoon. You’re engaging students with a scientific representation built from literature-based interactions, tested against known perturbations, and described with citations you can read.

Section 2: What “validated model” means in biology (and how that reaches your classroom)
Cell Collective’s scientific models follow a validation process that mirrors how research is done:

- Literature curation
  - Researchers gather experimental findings from peer-reviewed articles (e.g., whether Protein A activates Protein B, under what conditions).
  - Interactions and assumptions are documented with citations.
- Model construction
  - Biological mechanisms are encoded as a logic-based network (multi-level nodes and regulatory rules) that captures how signals flow and integrate in a system.
  - Each connection (activation or inhibition) is annotated so users can trace the evidence.
- Behavior expectations and unit tests
  - Known system behaviors (e.g., “If receptor X is active and Y is inhibited, outcome Z increases”) are formalized as test cases.
  - Modelers check whether the model reproduces these behaviors under appropriate inputs.
- Perturbation testing
  - The model is challenged with simulated knockouts, overexpression, or pathway inhibitors to see if it predicts qualitative outcomes consistent with published experimental data.
- Sensitivity and robustness analysis
  - Researchers examine how changes to assumptions or parameters influence outputs, ensuring predictions are not artifacts of fragile settings.
- Peer review and dissemination
  - Results are submitted to journals for peer review in systems biology or biology education, adding an external layer of scrutiny.
- Public release with documentation
  - Validated models, their logic, and references are shared in Cell Collective’s public library.
  - Many are available in community formats (e.g., SBML-qual) for reproducibility.

What you see in class
- A transparent network diagram with labeled interactions
- An evidence panel showing references for specific edges or rules
- Simulation controls (inputs, perturbations) and time-course outputs
- Versioned models that can be duplicated, modified, and shared

Section 3: From peer-reviewed research to K–12—what stays, what shifts
Moving from a research-grade model to a classroom-ready experience involves careful adaptation without losing scientific integrity.

What stays the same
- Causal structure: The “who activates whom” relationships and feedback loops are kept intact.
- Evidence: Citations and notes remain attached to nodes and interactions.
- Predictive capability: Students can run genuine what-if experiments (e.g., knock out a gene, activate a receptor) and observe system-level effects.

What changes to support learning
- Scope: Large research models may be trimmed to essential subsystems so students can reason about them in a class period.
- Language: Node names and tooltips may include grade-appropriate descriptions.
- Scaffolds: Preset scenarios, guiding questions, and simplified outputs help students connect mechanisms to phenomena.

Bottom line: The science remains authentic, while the interface and scaffolds meet students where they are.

Section 4: Examples of published Cell Collective models students can use
These categories represent models that have appeared in the Cell Collective library and the peer-reviewed literature. Your students can open them, probe them, and reason from real, research-grounded behavior.

- Immune signaling: T cell activation
  - What students can explore:
    - Turn on a receptor input and observe downstream activation.
    - “Knock out” a kinase node and predict changes to cytokine output.
    - Compare baseline vs. perturbed time courses to explain cause and effect.
- Cell fate: Apoptosis (programmed cell death)
  - What students can explore:
    - Increase pro-apoptotic signals to trigger cell death cascades.
    - Disable an anti-apoptotic regulator and observe system tipping points.
    - Contrast extrinsic (receptor-mediated) vs. intrinsic (mitochondrial) pathways.
- Growth factor signaling: EGFR/MAPK pathway
  - What students can explore:
    - Apply a growth factor input and trace activation through Ras–MAPK.
    - Simulate a receptor inhibitor and predict effects on downstream transcription factors.
    - Discuss negative feedback and signal attenuation.
- Cell cycle control
  - What students can explore:
    - Manipulate checkpoints or cyclin activity.
    - Predict consequences for progression vs. arrest.
    - Analyze feedback loops that stabilize or destabilize cycles.
- Metabolic regulation: Glycolysis switch
  - What students can explore:
    - Increase nutrient availability and observe pathway flux changes.
    - Introduce an inhibitor and reason about compensation mechanisms.
- Microbial/host signaling (e.g., quorum sensing, infection response)
  - What students can explore:
    - Toggle signaling molecules and chart community-level activation.
    - Compare robust vs. fragile nodes using sensitivity analysis.

Because these models are built from literature and have been used in research, students are not just “watching an animation”—they are interrogating a scientific model that makes testable predictions.

Section 5: Research-validated vs. “educational” simulations—how to tell the difference
Use this checklist to quickly evaluate classroom tools:

Research-validated models (like Cell Collective)
- Evidence trail: Interactions cite peer-reviewed studies; references are visible per node/edge.
- Transparent logic: Rules can be viewed and edited; assumptions are documented.
- Predictive experiments: Knockouts, overexpression, and input manipulations change outputs in a causally consistent way.
- Reproducibility: Models can be exported (e.g., SBML-qual) and versioned.
- Peer-reviewed pedigree: The approach and/or the model has undergone scientific peer review.

Educational-only simulations (common pitfalls)
- Black box: No visible rules or citations—just inputs and animated outcomes.
- Fixed outcomes: Scenarios are pre-scripted; student changes don’t truly alter mechanisms.
- Limited transfer: Hard to connect to real data or literature evidence.
- No standards support: No export, version control, or documented assumptions.

Why this matters: NGSS expects students to develop and use models as evidence. That is far easier when your tool makes the mechanisms, assumptions, and sources visible.

Section 6: NGSS alignment—Practice 2: Developing and Using Models
Cell Collective maps tightly to NGSS Practice 2. Here’s how:

- Develop
  - Students construct or extend models by adding nodes, defining activations/inhibitions, and writing logic rules for interactions.
- Use
  - Students run simulations to predict relationships among variables under different conditions (e.g., “What happens to output Z if we knock out Y?”).
- Test and revise
  - Students compare predicted results to literature-based expectations or class claims and then revise rules or structures accordingly.
- Analyze and interpret
  - Students examine time-series graphs and output levels to identify patterns, thresholds, and feedback dynamics.
- Communicate
  - Students justify claims with model evidence, citing specific mechanisms and published references attached to the model.

Crosscutting concepts supported
- Systems and system models: Students reason about boundaries, components, and interactions.
- Cause and effect: Students connect perturbations to downstream consequences.
- Stability and change: Students explore feedback and robustness.

Section 7: Step-by-step—Run a peer-reviewed model tomorrow (15–20 minutes)
Use this quick, ready-to-go flow to launch your first research-backed modeling lesson.

Before class (5 minutes)
1) Create a free account or log into Cell Collective.
2) Open the Public Models library.
3) Pick a model category (e.g., Apoptosis or T Cell Activation) with a clear input and output.
4) Bookmark or copy the share link so students can open the same model.

In class (10–15 minutes)
1) Introduce the question
   - “What happens to this system if we disable [a key component]?”
2) Show the model
   - Display the network diagram. Briefly highlight a few major nodes and edges.
   - Open the Evidence/References panel for one interaction so students see the citation trail.
3) Set a baseline
   - Run a baseline simulation with default inputs; show the time-course graph for one or two outputs.
4) Apply a perturbation
   - Use the Interventions panel to knock out a node (set activity to 0) or apply constitutive activation to another node.
   - Re-run the simulation and compare curves.
5) Facilitate quick analysis
   - Ask students to describe the change using cause-and-effect language.
   - Have them locate at least one piece of evidence (a cited interaction) that supports their explanation.

Exit ticket (2 minutes)
- Prompt: “Claim, evidence, reasoning—How did knocking out [node] change [output], and why?”

What teachers can verify live
- Public Models library (searchable by keyword/category)
- Model diagram with labeled interactions
- Evidence/References panel tied to nodes/edges
- Interventions (knockout/overexpression toggles)
- Simulation outputs (time series, activity levels)
- Share/duplicate model functions

Section 8: Step-by-step—Have students “validate” a claim with the model (CER task)
Use research-backed modeling to strengthen scientific argumentation.

Set-up (5 minutes)
- Choose a claim tied to the model (e.g., “Inhibiting [kinase] reduces [transcription factor] activation”).
- Identify two or three interactions in the model that provide mechanistic support; note their citations.

Student task (15–20 minutes)
1) Predict
   - Students predict what should happen if the claim is true.
2) Test
   - Students run two simulations: baseline and with the relevant perturbation.
3) Gather evidence
   - Students capture output plots and list the model interactions (with citations) that explain the result.
4) Reason
   - Students connect the mechanism to the observed change and evaluate whether the claim holds under the tested conditions.

Optional extension
- Ask students to propose a second perturbation (e.g., overexpression of a downstream inhibitor) and explain how it could challenge or reinforce the claim.

Section 9: Step-by-step—Build a small, testable model from literature
Empower students to develop a model, not just use one.

Preparation (10 minutes)
- Select a simple regulatory motif from your current unit (e.g., a two-node feedback: A activates B; B inhibits A).
- Locate one short, grade-appropriate summary paragraph (textbook or review) describing the interactions.

Build (15–25 minutes)
1) Create a new model
   - Add nodes A and B on the canvas.
2) Define interactions
   - Draw an activation arrow from A to B.
   - Draw an inhibition bar from B to A.
3) Set logic rules
   - For B: “Active when A is active” (add any thresholds or weights as desired).
   - For A: “Reduced when B is active.”
4) Test behavior
   - Run baseline; then simulate an A “pulse” input and watch the time-course.
   - Ask: Does B increase when A increases? Does B’s inhibition of A produce a decrease after the pulse?
5) Iterate
   - Add a stabilizing input to A or a decay to B and re-test.
6) Document
   - In notes, cite the source describing A→B and B⊣A.

Debrief
- Discuss how the model captures the essence of the mechanism and what assumptions were necessary.

Section 10: What you can verify directly in Cell Collective (feature checklist)
Everything below is available for you to click and see:

- Public Models library
  - Browse and open published models across cell signaling, immunology, metabolism, and more.
- Model canvas and logic editor
  - Add nodes, draw activation/inhibition edges, and edit logic rules for each node.
- Evidence and references
  - Open the evidence panel to see literature references associated with specific interactions or rules (where provided in the model).
- Interventions
  - Apply knockouts (fix node activity at 0) or constitutive activation and observe system responses.
- Simulation outputs
  - View time-series graphs and activity levels; compare runs under different scenarios.
- Scenarios and presets
  - Use input sliders or defined scenarios to represent environmental or experimental conditions.
- Save, share, duplicate
  - Save your version, generate a share link for students, or duplicate a public model to create your class variant.
- Versioning and notes
  - Track changes and add notes so students and co-teachers see what was modified and why.
- Standards support
  - Import or export models in community formats (e.g., SBML-qual) for transparency and reproducibility.

Section 11: The research foundation—credibility by the numbers
- 15+ years of research and development
  - Cell Collective grew out of sustained university research at UNL focused on logic-based, network-level modeling of biological systems.
- 50+ peer-reviewed publications
  - The body of work includes:
    - Methodological advances in logic-based and rule-based modeling
    - Applications to immune, signaling, metabolic, and cell cycle networks
    - Validation studies comparing model predictions to experimental perturbations
    - Education research on modeling-based learning and student outcomes
- Community impact
  - Models and methods have been used by researchers and educators across institutions, with open-access resources that support replication and classroom adaptation.

Section 12: Why research-backed matters for NGSS (practical classroom payoffs)
- Authentic evidence use
  - Students learn to back claims with mechanisms and references—not just patterns in graphs.
- Transferable reasoning
  - Students practice the same modeling moves used in research: define a system, identify variables, predict, test, revise.
- Equity of access
  - No coding is required. Drag-and-drop modeling and sliders lower the barrier while maintaining scientific rigor.
- Honest uncertainty
  - Because models are explicit about assumptions, students see how scientific knowledge is provisional and improvable—a core NGSS idea.

Section 13: How peer-reviewed models become classroom-ready (the translation pipeline)
- Identify a phenomenon that matters for your unit (e.g., cell communication in immunity).
- Select a published Cell Collective model covering the mechanism.
- Configure a lesson-sized subset (focus on a subnetwork and a few inputs/outputs).
- Build scaffolds:
  - A driving question
  - A prediction table (baseline vs. perturbation)
  - Space for claims, evidence (model outputs + citations), and reasoning
- Assess with model-based reasoning rather than recall.

Section 14: Future research directions (what’s next from the university–classroom partnership)
- Multi-scale integration
  - Connecting intracellular networks to tissue or organism-level models to bridge phenomena across scales.
- Data-enhanced modeling
  - Leveraging transcriptomics/proteomics and curated databases to refine logic rules and validate outputs.
- Interoperability and standards
  - Continued support for community formats (e.g., SBML-qual, COMBINE archives) to ensure reproducibility and reuse.
- Learning research in K–12 contexts
  - Designing and studying interventions that maximize gains in NGSS Practice 2, systems thinking, and causal explanation.
- User-centered enhancements
  - Investigating scaffolds that help novice modelers reason about uncertainty, assumptions, and sensitivity.

Section 15: Quick FAQ for busy teachers
- Do students need programming skills?
  - No. Cell Collective uses a visual, logic-based interface with drag-and-drop nodes, simple rule editors, and sliders.
- Is a model the “right answer”?
  - A model is a tested representation that can be wrong in useful ways. Students compare predictions to evidence and refine—exactly what NGSS expects.
- Can I see the sources?
  - Yes. Open the evidence/references panel in public models to view citations attached to interactions and mechanisms.
- How does this fit my time constraints?
  - Start with a preset scenario and a single perturbation. A 15–20 minute mini-investigation yields rich, model-based CER.

Section 16: Try this tomorrow—two ultra-fast launch options
Option A: One-perturbation warm-up (10 minutes)
- Open a published Apoptosis or T cell activation model.
- Baseline sim → knockout one node → re-simulate.
- Ask: “What changed? Which interaction in the model explains it?” Have students cite one piece of evidence from the model’s references.

Option B: Small-group claims test (15 minutes)
- Give each group a different perturbation (e.g., inhibitor vs. overexpression).
- Groups run sims, capture outputs, and present a 60-second CER with a cited mechanism.

Section 17: Research spotlight recap—what gives Cell Collective its edge
- University-built and maintained
  - Originating from Dr. Tomáš Helikar’s group at the University of Nebraska–Lincoln, Cell Collective is rooted in active research.
- Peer-reviewed foundation
  - 50+ publications inform the models, methods, and learning designs you use.
- Transparent and testable
  - Visible logic, literature citations, standards-based file formats, and reproducibility by design.
- K–12 ready
  - Purposeful scaffolds, zero coding, and NGSS-aligned workflows let you plug research into tomorrow’s lesson.

Call to Action: Explore the Cell Collective platform
- Open the Public Models library, pick a system you teach, and run a baseline-plus-perturbation demo.
- Click the evidence panel to show students how real science lives inside the model.
- Duplicate the model to create your own class version and share the link with students.

NGSS alignment highlight (Practice 2)
- Develop: Build or extend a model of a biological system.
- Use: Run simulations to predict outcomes under different conditions.
- Test/Revise: Compare predictions with expected behaviors; adjust mechanisms.
- Communicate: Justify claims with model outputs and cited interactions.

Preview: Coming next week
We’re sharing holiday-ready strategies to keep modeling momentum in short weeks—quick wins, low-prep activities, and festive phenomena that still hit NGSS targets. Don’t miss our holiday implementation guide!