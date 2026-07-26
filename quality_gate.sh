clear
echo "Starting quality gate"
echo ""
echo "Formatting"
echo "-------------------------------------------------------------------"
echo ""
uv run ruff format .

echo ""
echo "Type Checking"
echo "-------------------------------------------------------------------"
echo ""
uv run ruff check .

echo ""
echo "Running Tests"
echo "-------------------------------------------------------------------"
echo ""
uv run pytest

