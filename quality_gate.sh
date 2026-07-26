clear
echo "Starting quality gate"
echo ""
echo "Formatting"
echo "-------------------------------------------------------------------"
echo ""
uv run ruff format .

echo ""
echo "Linting"
echo "-------------------------------------------------------------------"
echo ""
uv run ruff check .

echo ""
echo "Type Checking"
echo "-------------------------------------------------------------------"
echo ""
uv run ty check .


echo ""
echo "Running Tests"
echo "-------------------------------------------------------------------"
echo ""
uv run pytest -rs