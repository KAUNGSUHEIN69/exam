import employess as emp

employees = [
    {"name": "Alice", "projects_completed": 10, "hours_worked": 200, "rating": 4.5},
    {"name": "Bob", "projects_completed": 7, "hours_worked": 150, "rating": 4.2},
    {"name": "Charlie", "projects_completed": 5, "hours_worked": 120, "rating": 3.8},
    {"name": "David", "projects_completed": 8, "hours_worked": 180, "rating": 4.7},
    {"name": "Eve", "projects_completed": 6, "hours_worked": 140, "rating": 4.0},
]

def test_high_rated_employees():
    result = emp.high_rated_employees(4.6)
    expect = [{"name": "David", "projects_completed": 8, "hours_worked": 180, "rating": 4.7}]
    assert result == expect

def test_get_top_performer():
    result = emp.get_top_performer()
    expect = {"name": "Alice", "projects_completed": 10, "hours_worked": 200, "rating": 4.5}
    assert result == expect