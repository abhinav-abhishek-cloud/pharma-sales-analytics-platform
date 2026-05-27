Target structure:

pipeline-pulse/
├── hawk_eye/          # main package
│   ├── connectors/          # CSV, Parquet, S3, DB connectors
│   ├── profiler/            # column profiling
│   ├── checks/              # DQ rule engine
│   ├── anomaly/             # ML anomaly detection
│   ├── ai/                  # LLM insights
│   ├── storage/             # metadata DB
│   ├── api/                 # FastAPI endpoints
│   └── dashboard/           # Streamlit app
├── config/                  # YAML configs
├── data/sample/             # sample data for demo only
├── tests/
├── docs/images/             # screenshots for README
├── notebooks/               # exploratory work
├── .github/workflows/       # CI/CD
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── LICENSE