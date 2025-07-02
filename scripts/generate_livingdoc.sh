#!/usr/bin/env bash
set -euo pipefail
export DOTNET_CLI_TELEMETRY_OPTOUT=1
export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1

if ! command -v livingdoc &> /dev/null; then
  dotnet tool install --global SpecFlow.Plus.LivingDoc.CLI
  export PATH="$PATH:$HOME/.dotnet/tools"
fi

dotnet build tests/HighLevelTests/HighLevelTests.csproj --configuration Debug
dotnet test tests/HighLevelTests/HighLevelTests.csproj --no-build --configuration Debug --logger "trx;LogFileName=TestResults.trx"
mkdir -p docs
livingdoc test-assembly --test-assembly tests/HighLevelTests/bin/Debug/net8.0/HighLevelTests.dll --output docs/livingdoc.html
echo "LivingDoc generated at docs/livingdoc.html"