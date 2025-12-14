---
title: 6 Advanced ModelIt K12 Features Power Users Love: Custom Builder, 1000+ Model Library, Precision Simulations, Data Exports, Collaboration, and Assessments
date: 2025-11-24
categories: ["Platform Features"]
hero_image: /assets/images/week4-hero.jpg
author: "Dr. Marie & Charles Martin"
excerpt: Ready to go beyond the basics? This deep dive shows exactly how ModelIt K12 (powered by the Cell Collective platform) helps you build custom models, tap into 1,000+ validated models, run precise simulations with perturbations, export data, enable student collaboration, and integrate assessments—step by step, with NGSS alignment.
tags: ["ModelIt K12", "Cell Collective", "NGSS Practice 2", "STEM", "Simulation", "Assessment", "Collaboration"]
---

Week 4 of our Platform Deep Dive is for power users—the teachers who want to unlock everything ModelIt K12 can do in the classroom tomorrow. If you’ve dabbled with models and simulations already, this is your springboard into advanced workflows you can trust. We’ll walk through six verified, high-impact features, show you what you’ll actually see on screen, and give you practical, step-by-step guides to make it happen with students.

Two promises up front:
- Research you can stand on: ModelIt K12 is built on the Cell Collective research platform, a foundation with 15+ years of development and 50+ peer-reviewed publications underpinning the modeling and simulation approach you see in class.
- NGSS alignment you can show your admin: Every feature here supports NGSS Science and Engineering Practice 2 (Developing and Using Models) in concrete, assessable ways.

What’s inside:
1) Custom Model Building Interface  
2) Pre-built Cell Collective Model Library (1000+ validated models)  
3) Simulation Controls & Perturbation Testing  
4) Data Export & Visualization Tools  
5) Student Collaboration Features  
6) Assessment Integration Capabilities

Let’s get into it.

Feature 1: Custom model building interface
What you’ll actually see
- A Build workspace with a draggable canvas for components (genes, proteins, molecules, or system variables), plus a left panel to add components and regulators.
- Component nodes with editable names, descriptions, and logical update rules (e.g., how A and B jointly regulate C).
- A rule editor that supports logic-based modeling (common in systems biology), with options to set default states and initial activities.
- Toolbar options for Save, Version, and Share so you retain full control of copies and collaboration.
- Visual cues: arrows for regulatory relationships; colored highlights for selected nodes; validation checks when rules are incomplete.

Step-by-step: Build a custom model in 15 minutes
1) Start a new model: Click Create Model (top right). Give it a clear name (e.g., “Lac Operon—Regulation & Perturbations”) and short description for students.  
2) Add components: In the left panel, choose Add Component and create your key variables (e.g., LacI, Operator, RNA Polymerase, Lactose, mRNA).  
3) Define relationships: Select a component (e.g., mRNA), click Add Regulator, and choose the upstream components that influence it.  
4) Write update rules: Open the rule editor for mRNA and define how regulators affect it (e.g., “RNA Polymerase AND NOT LacI” to require polymerase while repressing under LacI).  
5) Set initial states: In the Build workspace, set initial activity for key variables (e.g., Lactose = OFF). This determines how your first simulation begins.  
6) Use notes: Add component descriptions (left properties panel) so students can see definitions and context by clicking a node.  
7) Validate: Check for any nodes with missing rules (highlighted). Fill those in or set them to a constant if needed.  
8) Save and version: Click Save, then Create Version (or Save Version) to lock a “clean copy” you can revert to if students break things (intentionally or not!).  
9) Share (optional): Use Share to invite co-teachers or a student group with view or edit rights.  
10) Simulate: Click Simulate to test your model before releasing it to students.

NGSS Practice 2 alignment
- Develop and use models: Students co-construct the structure (components and relationships) and behavior (logic rules) of the system.  
- Represent systems and interactions: The directed network explicitly represents causal relationships.  
- Limitations and assumptions: Rule definitions and initial conditions make assumptions visible and discussable, paving the way for model revision.

Teacher pro tips
- Use naming conventions: Prefix inputs with “input_” or group related variables by color to make student navigation easier.  
- Scaffold the rule editor: Provide starter rules for one or two nodes; have students finish the rest, then compare outcomes.

Feature 2: Pre-built Cell Collective model library (1000+ validated models)
What you’ll actually see
- Library browser: Search by keyword (e.g., “MAPK,” “lac operon,” “immune response”), filter by topic, organism, or model size.  
- Model preview: View an overview page with description, components count, references/notes, and a visual network snapshot.  
- Validation cues: Clearly documented models (e.g., derived from published literature) include background and curated logic reflecting peer-reviewed sources.  
- Copy to workspace: One click to Clone or Open in My Models so you can run simulations immediately or customize for your class.

Step-by-step: Find and adapt a model for classroom use
1) Open the library: From the main navigation, click Library (or Models).  
2) Search and filter: Type a topic (“cell cycle,” “insulin signaling”) and apply filters (size, complexity, curated status).  
3) Preview details: Open the model card to read the description and notes; scan the components list to judge fit for your students.  
4) Clone: Click Clone or Copy to My Models to create your editable copy.  
5) Trim for level: In Build, hide advanced nodes or lock rules you don’t want students to change yet.  
6) Add guiding notes: In component descriptions, add plain-language explanations (“This node increases when glucose is high”).  
7) Save a student-ready version: Version the model and clearly title it “Student Starter—Do Not Edit Rules” or similar.  
8) Pilot run: In Simulate, run a baseline to confirm all nodes update as expected.  
9) Publish to class: Share view-only with students or attach it to an assignment (see Feature 6).

NGSS Practice 2 alignment
- Use models to predict phenomena: Students leverage vetted models to test predictions under different conditions.  
- Compare and refine models: Have students compare outputs from the library model vs. their simplified version, then justify differences.

Teacher pro tips
- Start with mid-size: For younger learners or first-timers, aim for 10–30 components; older students can handle larger networks with structured guidance.  
- Connect to texts: Link specific nodes and rules to passages in your curriculum for evidence-based model adjustments.

Feature 3: Simulation controls and perturbation testing
What you’ll actually see
- Simulate workspace with:
  - Time series view: Line plots of component activity across iterations/steps.  
  - Heat map view: Matrix display of activity levels across components and time.  
  - Control panel: Number of iterations, update mode, initial state toggles, and output selection.  
- Perturbations panel:
  - Knockout (KO) toggles: Force a node OFF throughout the run.  
  - Overexpression/constant ON: Hold a node ON to simulate overactivation.  
  - Temporary vs. permanent: Choose whether a perturbation applies at a specific time window or entire run.  
  - Multi-perturbation sets: Save and load sets to compare scenarios.

Step-by-step: Run baseline and compare perturbations
1) Set outputs: In Simulate, select 3–8 key components to track (e.g., “mRNA,” “Protein,” “Repressor”).  
2) Choose duration: Set iterations (e.g., 25–50).  
3) Baseline run: Click Run to generate the control output. Label this trace “Baseline.”  
4) Create a perturbation: Open the Perturbations panel, set LacI = KO (OFF), save as “KO_LacI.”  
5) Run perturbed: Click Run again. Your new trace appears alongside baseline.  
6) Compare visually: Use the legend to toggle traces; switch to Heat Map for a class-wide overview.  
7) Add an overexpression: Set “Lactose = ON” permanently; save as “Lactose_ON.”  
8) Batch compare: Run both perturbation sets and compare peak times, steady-state levels, or oscillations.  
9) Document findings: Have students capture screenshots or use Export CSV (see Feature 4).  
10) Reset: Clear perturbations or load a saved set to demo a different scenario.

NGSS Practice 2 alignment
- Use models to test cause-and-effect: Perturbations make causal claims testable (e.g., “If LacI is knocked out, mRNA increases”).  
- Plan and carry out investigations with models: Parameterizing runs mirrors iterative experimental design.

Teacher pro tips
- Define comparison criteria: Have students specify what constitutes a “change” before running (e.g., “greater than 20% increase by step 15”).  
- Encourage replicability: Instruct students to name and save perturbation sets to ensure they can reproduce results.

Feature 4: Data export and visualization tools
What you’ll actually see
- Chart options: Toggle between line charts and heat maps; select nodes to display; adjust y-axis scaling for comparability.  
- Download controls:
  - Export CSV for time series or heat map data, with labeled columns for iteration and node activity.  
  - Export PNG of the current chart for reports or slides.  
  - Export network diagram as an image for documentation.  
  - Export model structure (e.g., to SBML-qual format) for advanced workflows and interoperability in compatible tools.
- Notes panel: Add captions and figure notes students can reference when writing up findings.

Step-by-step: Take data from simulation to student report
1) Choose visualization: In Simulate, select Time Series for detailed traces or Heat Map for class comparisons.  
2) Curate outputs: Check only the 5–10 nodes students must analyze; remove extraneous signals.  
3) Add a caption: In Notes, write a figure caption template students can copy and customize.  
4) Export data: Click Download CSV (top-right of the chart area).  
5) Analyze in Sheets or Excel: Import CSV; create a quick line chart for two conditions (Baseline vs. KO).  
6) Compute metrics: Have students calculate differences (Δ peak height, time to half-maximum).  
7) Export figures: Download PNG charts from ModelIt K12 or from the spreadsheet tool.  
8) Attach to submission: Students add their graphs and brief data interpretation to your assignment (Feature 6).  
9) Archive: Save the model version and exported files in your course folder for reuse and moderation.

NGSS Practice 2 alignment
- Use models and data together: Students support claims with quantitative outputs from their own simulations.  
- Communicate information from models: Figures and captions convert model behavior into assessable evidence.

Teacher pro tips
- Standardize figure names: Encourage “Figure 1—Time Series (Baseline vs KO)” so grading is faster.  
- Build a class dataset: Merge all student CSVs into a single sheet to discuss variability and reproducibility.

Feature 5: Student collaboration features
What you’ll actually see
- Share controls: Invite collaborators by email or shareable link with role settings (view or edit).  
- Version history: Time-stamped versions with author attribution; restore any previous version when needed.  
- Comments/notes: Leave guidance inside the model; students can respond or resolve after changes.  
- Team copies: Duplicate a template model into multiple team-owned copies with consistent starting state.

Step-by-step: Run a collaborative modeling project
1) Prep a template: Build or clone a starter model and save a clean version (e.g., “Signal Pathway Starter—Template”).  
2) Create team copies: Use Duplicate to create one copy per team (e.g., “Team 3—Signal Pathway”).  
3) Share with roles: Invite each team with Edit access; keep co-teachers as Editors; set students outside the team to View only.  
4) Assign roles in class: Model architect (rules), Data lead (simulation runs), Recorder (notes), Reviewer (quality checks).  
5) Comment for checkpoints: Add comments, e.g., “Checkpoint A—Upload baseline CSV and write a 2-sentence claim.”  
6) Track progress: Check version history to confirm each team member’s contributions (and to spot accidental regressions).  
7) Merge best ideas: If two teams solve different parts well, open both versions side-by-side and integrate changes in a new shared version.  
8) Publish exemplars: Flip a strong team model to View-only and share with the class for critique (useful for model comparison writing).  
9) Lock final: When the project is over, Save Version “Final—Team 3” and switch access to View to preserve integrity.

NGSS Practice 2 alignment
- Collaboratively develop and refine models: Students share responsibility for structure, rules, tests, and revisions.  
- Argue from evidence using model outputs: Comment threads capture evidence-based critique and reasoning.

Teacher pro tips
- Use version naming discipline: “v1-baseline,” “v2-perturbations,” “v3-revisions” helps everyone stay coordinated.  
- Build peer feedback in: Require each team to leave two actionable comments on another team’s model.

Feature 6: Assessment integration capabilities
What you’ll actually see
- Assignment setup: Attach a model (template or library clone), add prompts, and define required artifacts (e.g., CSV export, chart image, written claim).  
- Submission capture: Students submit a link to their model version and upload requested files; the platform records time-stamped work products.  
- Rubric alignment: Attach a rubric that explicitly calls out NGSS Practice 2 skills (e.g., “Defines assumptions,” “Uses simulation data to support claim,” “Revises model based on evidence”).  
- Grading and export: Enter scores and feedback; export a CSV gradebook for import into your LMS.  
- Evidence trace: Access students’ version history and perturbation sets as evidence during grading or moderation.

Step-by-step: Create a model-based assessment you can grade fast
1) Start an assignment: Click Assignments > New. Title it clearly (e.g., “Enzyme Regulation—Model & Claim-Evidence-Reasoning”).  
2) Attach the model: Select your student-ready template from My Models.  
3) Add prompts: Include specific instructions (e.g., “Run Baseline and KO_Inhibitor; export both CSVs; paste a screenshot of your Time Series graph”).  
4) Define artifacts: Check boxes for required uploads (CSV, PNG) and a short response field.  
5) Add rubric: Use or adapt a Practice 2-aligned rubric with 3–4 criteria (Model structure, Use of data, Explanation/justification, Revision).  
6) Set due date and visibility: Publish to your class with clear deadlines.  
7) Student submission: Students follow the link, complete runs, export files, and submit.  
8) Grade efficiently: Open a student’s model version and compare to their uploaded data; enter rubric scores.  
9) Export gradebook: Download CSV for easy import into your LMS gradebook.  
10) Reflect and iterate: Note common issues (e.g., incomplete perturbation labeling) and adjust the next assignment template.

NGSS Practice 2 alignment
- Assess developing and using models directly: Rubrics target model building, testing, and revision with evidence.  
- Emphasize iteration: Students’ version history and perturbation sets show how models evolve with feedback.

Teacher pro tips
- Ask for named perturbation sets: Require students to submit “Baseline,” “KO_X,” “OE_X” with matching names in their graph legends.  
- Keep prompts concrete: “Show that C increases by step ≤15 when KO is ON” is faster to grade than open-ended generalities.

Implementation playbook: One week, six features, real outcomes
Use this sequence to translate the features above into a tight, high-impact week:

Day 1: Launch and baseline
- Clone a vetted model from the library and trim it for your level.  
- Students explore the Build workspace; identify components and relationships.  
- Homework: Short prompt—“List 3 assumptions in the current rules.”

Day 2: Custom edits
- Students modify one or two rules (scaffolded) and save a new version.  
- Run baseline simulations and export CSV for 3 target nodes.

Day 3: Perturbation testing
- Introduce perturbation sets (KO and OE).  
- Students compare Baseline vs KO, annotate differences, and add a caption in Notes.

Day 4: Collaboration
- Teams merge the best edits into one shared model; use comments to propose changes.  
- Teacher checks version history to confirm contribution balance.

Day 5: Assessment
- Students submit model link, CSV, figure, and CER paragraph.  
- Grade with the rubric and export CSV gradebook to your LMS.

Research foundation you can cite tomorrow
- 15+ years of development: The Cell Collective platform has been built and iteratively improved for well over a decade, originating in academic research settings to make complex biological systems computable and teachable.  
- 50+ peer-reviewed publications: The modeling approach, algorithms, and education implementations linked to the Cell Collective platform are documented across dozens of peer-reviewed papers, including studies of model structure, simulation techniques, interoperability (e.g., SBML-qual), and classroom impacts.  
- Why it matters: This foundation is why you can trust that a perturbation behaves the way logic dictates, that exported time series map to the model you built, and that students’ work is anchored in methods used by practicing scientists.

NGSS Practice 2: How each feature supports Developing and Using Models
- Custom builder: Students define components, relationships, and rules, making assumptions explicit and testable.  
- Library models: Students use validated models to generate predictions, compare with simplified or alternative models, and justify differences.  
- Simulation controls: Students plan and carry out investigations within a model, altering conditions and collecting evidence.  
- Perturbation testing: Students test cause-and-effect claims by systematically changing variables and interpreting outcomes.  
- Data export & visualization: Students analyze and communicate model-derived data using appropriate representations.  
- Collaboration & assessment: Students revise models based on feedback and evidence; teachers assess model-based reasoning transparently.

What teachers often ask (and quick answers)
- Can I lock parts of a model so students don’t change everything?  
  - Yes. Keep a “Template” version, share student copies with limited edit scope, and lock rules via instructions; version history helps you revert if needed.  
- Can students work in groups without overwriting each other?  
  - Yes. Create one copy per team and use version history to resolve conflicts. Comments guide coordination.  
- How do I know if a library model is trustworthy?  
  - Preview notes and references; curated models include documentation aligned with the literature so you can see where rules come from.  
- Can I get the data out for deeper analysis?  
  - Yes. Export CSV for time series and heat maps, and download images of charts and networks; advanced users can export model structure (e.g., SBML-qual) for use in compatible tools.  
- Will this help with my NGSS evidence during observations?  
  - Yes. Your assignments, rubrics, exported data, and student version histories provide direct evidence of NGSS Practice 2 in action.

Classroom-ready checklists
Before class
- Clone or build your model, run a clean baseline, and save a “Template” version.  
- Decide on 3–5 outputs for students to focus on.  
- Prepare a perturbation set with descriptive names.  
- Preload a rubric with NGSS Practice 2 criteria.

During class
- Project the Build view to discuss assumptions and limitations.  
- Model one complete run (Baseline, KO, compare).  
- Require teams to name versions and perturbation sets consistently.

After class
- Export student gradebook to your LMS.  
- Archive exemplar models for next year.  
- Note one change to your template based on this run (e.g., simplify a rule or add a guiding note).

Why these six features matter together
- Coherence across tasks: Students move from constructing to testing to communicating findings, mirroring authentic scientific practice.  
- Evidence trail for assessment: Every step—from rules to runs to exports—creates artifacts you can evaluate and moderate.  
- Scalability: Start small (5–10 nodes), then scale to richer systems with the same workflow and tools.  
- Accessibility: Visual networks, step-by-step perturbations, and focused outputs help more learners participate meaningfully.

Ready to try it?
- Request a platform demo: See the Build and Simulate workspaces live, browse the model library, and walk through assignment setup with our team. We’ll tailor the session to your course and standards.  
- Bring a unit you already teach: We’ll help you map it to the features above so you can deploy next week with confidence.

Coming next week
We’ll unpack the Cell Collective research that powers ModelIt K12—how 15+ years of development and 50+ peer-reviewed publications shaped the modeling approach, interoperability, and classroom impact you benefit from every day.

Call to action
- Want the walkthrough and templates from this post? Request a platform demo and we’ll send you a starter package with a sample model, perturbation sets, NGSS-aligned rubric, and a ready-to-use assignment shell.