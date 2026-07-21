# Graph Report - .  (2026-07-20)

## Corpus Check
- Corpus is ~20,441 words - fits in a single context window. You may not need a graph.

## Summary
- 292 nodes · 486 edges · 17 communities (12 shown, 5 thin omitted)
- Extraction: 89% EXTRACTED · 10% INFERRED · 0% AMBIGUOUS · INFERRED: 50 edges (avg confidence: 0.8)
- Token cost: 0 input · 172,243 output

## Community Hubs (Navigation)
- Project Architecture Overview
- Forecast API & Data Merge
- Alarm Data Processing
- Deployment & Frontend Docs
- Frontend Dependencies
- Telegram NLP Features
- Telegram Scraping & Storage
- ISW Report Scraping & Storage
- Tactical Map UI Page
- Weather Scraping & Storage
- Frontend Icon Sprite
- Frontend Root Layout
- Frontend Path Config
- LightGBM Inference Module
- Next.js Config
- PostCSS Config
- Favicon Icon

## God Nodes (most connected - your core abstractions)
1. `Python Dependency Manifest (requirements.txt)` - 30 edges
2. `preprocess_messages()` - 14 edges
3. `Database` - 14 edges
4. `InvalidUsage` - 14 edges
5. `generate_forecast()` - 12 edges
6. `AlarmsDb` - 11 edges
7. `IswDb` - 11 edges
8. `TelegramDb` - 11 edges
9. `WeatherDb` - 11 edges
10. `TacticalDashboard()` - 11 edges

## Surprising Connections (you probably didn't know these)
- `PyYAML==6.0.3` --conceptually_related_to--> `Air Raid Alarm Prediction System`  [AMBIGUOUS]
  requirements.txt → README.md
- `langchain==0.3.28` --conceptually_related_to--> `Feature Engineering Layer`  [AMBIGUOUS]
  requirements.txt → README.md
- `numpy==2.4.2` --conceptually_related_to--> `Feature Engineering Layer`  [INFERRED]
  requirements.txt → README.md
- `pandas==3.0.1` --conceptually_related_to--> `Feature Engineering Layer`  [INFERRED]
  requirements.txt → README.md
- `scikit-learn==1.8.0` --conceptually_related_to--> `Model Training and Inference Layer`  [INFERRED]
  requirements.txt → README.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Data Flow Pipeline (7 Stages)** — readme_pipeline_data_ingestion, readme_pipeline_persistence, readme_pipeline_feature_engineering, readme_pipeline_preprocessing, readme_pipeline_inference, readme_pipeline_api_serving, readme_pipeline_frontend_rendering [EXTRACTED 1.00]
- **System Architecture Layers** — readme_data_ingestion_and_persistence_layer, readme_feature_engineering_layer, readme_model_training_and_inference_layer, readme_production_backend_layer, readme_frontend_presentation_layer [EXTRACTED 1.00]
- **AWS EC2 Backend Deployment Components** — readme_backend_setup_on_ec2, app_api_alarm_forecast_module, readme_prediction_automation, readme_retraining_automation, readme_uwsgi [INFERRED 0.85]
- **Tactical-map footer/nav icon set (social, docs, code links)** — frontend_tactical_map_public_icons_bluesky_icon, frontend_tactical_map_public_icons_discord_icon, frontend_tactical_map_public_icons_documentation_icon, frontend_tactical_map_public_icons_github_icon, frontend_tactical_map_public_icons_social_icon, frontend_tactical_map_public_icons_x_icon [EXTRACTED 1.00]

## Communities (17 total, 5 thin omitted)

### Community 0 - "Project Architecture Overview"
Cohesion: 0.07
Nodes (52): lgbm_retrain.py (Retraining Script), app/core/scraping/ (Scraping Modules), database.db (SQLite Database), eda/ (Exploratory Data Analysis Directory), machine learning/ (ML Experimentation Directory), lgbm_pipeline.joblib (Serialized LightGBM Model), Air Raid Alarm Prediction System, Data Ingestion and Persistence Layer (+44 more)

### Community 1 - "Forecast API & Data Merge"
Cohesion: 0.10
Nodes (22): forecast(), generate_forecast_endpoint(), add_neighbor_alarm_count(), Додає колонку 'neighbor_alarm_count' до датафрейму.       Параметри:, create_features_isw(), merge_all_data(), DataFrame, add_region_ids() (+14 more)

### Community 2 - "Alarm Data Processing"
Cohesion: 0.14
Nodes (19): explode_by_hour(), fix_regions(), get_correct_regions(), merge_alarms(), _merge_intervals(), _parse_dt(), DataFrame, date (+11 more)

### Community 3 - "Deployment & Frontend Docs"
Cohesion: 0.08
Nodes (28): alarm_forecast.py (Flask REST API), app/core/features/ (Feature Engineering Modules), lgbm_predict.py (Inference Script), alarm_predictions.json (Inference Output), frontend/tactical-map (Next.js Tactical Map App), app/page.js (Entry Page), create-next-app, Tactical Map Frontend README (+20 more)

### Community 4 - "Frontend Dependencies"
Cohesion: 0.07
Nodes (27): framer-motion, dependencies, framer-motion, lucide-react, next, prop-types, react, react-dom (+19 more)

### Community 5 - "Telegram NLP Features"
Cohesion: 0.14
Nodes (25): _add_nlp_features(), _add_rolling_features(), _add_text_length(), _add_time_features(), _apply_text_pipeline(), _build_hourly_dataframe(), clean_text(), _drop_missing_and_duplicates() (+17 more)

### Community 6 - "Telegram Scraping & Storage"
Cohesion: 0.16
Nodes (9): _ensure_event_loop(), fetch_messages(), DataFrame, datetime, Збирає повідомлення з вказаних каналів від start_date до поточного моменту., datetime, Path, Row (+1 more)

### Community 7 - "ISW Report Scraping & Storage"
Cohesion: 0.22
Nodes (9): _get_last_date_from_json(), _parse_date(), date, datetime, Path, _run_scraper_range(), scrape_isw(), IswDb (+1 more)

### Community 8 - "Tactical Map UI Page"
Cohesion: 0.25
Nodes (13): ALWAYS_RED_REGIONS, buildTimeSlots(), fetchPredictions(), generateMockPredictions(), LEGEND_ITEMS, probToBarColor(), probToFill(), probToHoverFill() (+5 more)

### Community 9 - "Weather Scraping & Storage"
Cohesion: 0.24
Nodes (5): format_forecast(), get_forecast(), get_formated_forecast(), Row, WeatherDb

### Community 10 - "Frontend Icon Sprite"
Cohesion: 0.38
Nodes (7): Bluesky Icon, Discord Icon, Documentation Icon, GitHub Icon, Social/Contacts Icon, icons.svg (UI Icon Sprite), X (Twitter) Icon

### Community 11 - "Frontend Root Layout"
Cohesion: 0.40
Nodes (3): geistMono, geistSans, metadata

## Ambiguous Edges - Review These
- `Air Raid Alarm Prediction System` → `PyYAML==6.0.3`  [AMBIGUOUS]
  requirements.txt · relation: conceptually_related_to
- `Feature Engineering Layer` → `langchain==0.3.28`  [AMBIGUOUS]
  requirements.txt · relation: conceptually_related_to

## Knowledge Gaps
- **36 isolated node(s):** `paths`, `nextConfig`, `name`, `version`, `private` (+31 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `Air Raid Alarm Prediction System` and `PyYAML==6.0.3`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Feature Engineering Layer` and `langchain==0.3.28`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **Why does `Database` connect `Forecast API & Data Merge` to `Weather Scraping & Storage`, `Alarm Data Processing`, `Telegram Scraping & Storage`, `ISW Report Scraping & Storage`?**
  _High betweenness centrality (0.040) - this node is a cross-community bridge._
- **Why does `preprocess_messages()` connect `Telegram NLP Features` to `Telegram Scraping & Storage`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Why does `TelegramDb` connect `Telegram Scraping & Storage` to `Forecast API & Data Merge`?**
  _High betweenness centrality (0.031) - this node is a cross-community bridge._
- **Are the 4 inferred relationships involving `Database` (e.g. with `AlarmsDb` and `IswDb`) actually correct?**
  _`Database` has 4 INFERRED edges - model-reasoned connections that need verification._
- **What connects `paths`, `nextConfig`, `name` to the rest of the system?**
  _36 weakly-connected nodes found - possible documentation gaps or missing edges._