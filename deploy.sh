#!/usr/bin/env bash
# Deploy the A2A server to Cloud Run.
set -euo pipefail
: "${GOOGLE_CLOUD_PROJECT:?set GOOGLE_CLOUD_PROJECT}"
gcloud run deploy research-team-a2a \
  --source . --project "$GOOGLE_CLOUD_PROJECT" --region "${GOOGLE_CLOUD_LOCATION:-us-central1}" \
  --set-env-vars GOOGLE_GENAI_USE_VERTEXAI=TRUE,GOOGLE_CLOUD_PROJECT="$GOOGLE_CLOUD_PROJECT",GOOGLE_CLOUD_LOCATION="${GOOGLE_CLOUD_LOCATION:-us-central1}" \
  --no-allow-unauthenticated
