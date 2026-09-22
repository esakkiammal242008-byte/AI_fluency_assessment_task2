COURSES = {
    "CS101": 12000,
    "AI202": 18000,
    "DS303": 15000,
}


def get_course_fee(course_code):
    course_code = course_code.upper()

    if course_code not in COURSES:
        return f"Course {course_code} not found."

    return COURSES[course_code]


def calculator(expression):
    try:
        allowed = set("0123456789+-*/(). ")
        if not all(char in allowed for char in expression):
            return "Invalid expression."

        result = eval(expression, {"__builtins__": {}}, {})
        return result

    except Exception as e:
        return f"Calculation error: {e}"